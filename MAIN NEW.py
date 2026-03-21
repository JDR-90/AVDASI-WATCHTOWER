import sys
import threading

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Signal, QObject
from ui_main import Ui_Form

from pymavlink import mavutil

from FC_CONNECT import *
from MODE_SWITCH import *
from TELEMETRY import *
from ANGLE_COMMAND import *
from ANGLE_CONVERSION import *
from FLAP_CONFIG import *
import time

#MAKE OUTPUT BOX NOT INPUTTABLE
#---------------------------------------------------------

####################
#PRINTING -> UI OUTPUT BOX
####################
class PrintRedirect(QObject):
    OutputBoxSignal = Signal(str)
    def write(self, text):
        if text.strip() != "":
            self.OutputBoxSignal.emit(text)

    def bin(self):
        pass

####################
#MAIN WINDOW
####################
class MainWindow(QWidget):
    OutputBoxSignal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mavlink = None
        #self.SetupConnection()

        #Redierct print to OutputBox
        self.redirect = PrintRedirect()
        self.redirect.OutputBoxSignal.connect(self.append_output)
        sys.stdout = self.redirect
        sys.stderr = self.redirect

        #Angle Limits Dictionary
        self.limits = {
            "Flap": (0, 30),
            "Aileron": (-40, 40),
            "Rudder": (-40, 40),
            "Elevator": (-45, 45)
        }

        #Control Surface Dictionary
        self.surface_funcs = {
            "Flap": set_flaps,
            "Aileron": set_aileron,
            "Rudder": set_rudder,
            "Elevator": set_elevator
        }
        
        #Buttons
        self.ui.FlapButton.clicked.connect(lambda: self.handle_cmd("Flap", self.ui.FlapEntry.text()))
        self.ui.AileronButton.clicked.connect(lambda: self.handle_cmd("Aileron", self.ui.AileronEntry.text()))
        self.ui.RudderButton.clicked.connect(lambda: self.handle_cmd("Rudder", self.ui.RudderEntry.text()))
        self.ui.ElevatorButton.clicked.connect(lambda: self.handle_cmd("Elevator", self.ui.ElevatorEntry.text()))

        #Entry
        self.ui.FlapEntry.returnPressed.connect(lambda: self.handle_cmd("Flap", self.ui.FlapEntry.text()))
        self.ui.AileronEntry.returnPressed.connect(lambda: self.handle_cmd("Aileron", self.ui.AileronEntry.text()))
        self.ui.RudderEntry.returnPressed.connect(lambda: self.handle_cmd("Rudder", self.ui.RudderEntry.text()))
        self.ui.ElevatorEntry.returnPressed.connect(lambda: self.handle_cmd("Elevator", self.ui.ElevatorEntry.text()))

        #Connection and mode switch buttons
        self.ui.ConnectionStartButton.clicked.connect(self.start_connection_thread)
        self.ui.FBWBButton.clicked.connect(lambda: self.start_mode_thread('s'))
        self.ui.ManualButton.clicked.connect(lambda: self.start_mode_thread('m'))

        print("DELTA BLAZE - GUI loaded successfully\n")

    #def SetupConnection(self):
    #    self.ui.ConnectionStartButton.clicked.connect(self.start_connection_thread)
        
    ####################
    #SEND TO OUTPUTBOX
    ####################
    def append_output(self, text):
        self.ui.OutputBox.append(text)


    ####################
    #ENTRY SETUP
    ####################
    def handle_cmd(self, surface, value):
        if value == "":
            print(f"{surface}: No value entered")
            return
        try:
            value = float(value)
        except ValueError:
            print(f"{surface}: Invalid input '{value}'")
            return
        #Limits check
        min, max = self.limits[surface]
        if not (min <= value <= max):
            print(f"{surface}: Value {value}° outside limits ({min} to {max})")
            return

        #Send command in thread
        threading.Thread(target=self.backend_surface_cmd,
                         args=(surface, value),
                         daemon=True).start()


    ####################
    #THREADS
    ####################
    def backend_surface_cmd(self, surface, value):
        if not self.mavlink:
            print("Error - Cannot send command (no connection)")
            return
        print(f"[CMD] {surface} → {value}°")
        try:
            function = self.surface_funcs[surface]
            function(self.mavlink, value)
            print(f"[CMD] {surface} command sent")
        except Exception as exception:
            print(f"Error - Failed to send {surface} command")


    def start_connection_thread(self):
        threading.Thread(target=self.backend_connect, daemon=True).start()

    def backend_connect(self):
        try:
            print("[CONNECT] Starting MAVLink connection, wait 3 seconds...")
            self.mavlink = connection_start()
            if self.mavlink is None:
                print("Error - No heartbeat detected")
                return
            print("[CONNECT] Connected. Starting listener thread...")
            print(self.mavlink.mode_mapping()) 
            run_status_refresh(self.mavlink)
        except Exception as e:
            print (f"Error - MAVLink connection failed: {e}")


    def start_mode_thread(self, mode):
        threading.Thread(target=self.backend_switch_mode, args=(mode,), daemon=True).start()
        

    def backend_switch_mode(self, mode):
        if not self.mavlink:
            print("Error - Cannot switch modes (no connection)")#
            return
        command_mode(self.mavlink, mode)


####################
# RUN AVIONICS
####################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
