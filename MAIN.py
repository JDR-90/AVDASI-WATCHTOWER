import sys
import threading
import os

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtWidgets import QSizePolicy, QSplashScreen
from PySide6.QtCore import Signal, QObject, QTimer, Qt
from PySide6.QtGui import QFont, QIcon, QPixmap
from ui_main import Ui_Form

from pymavlink import mavutil

from FC_CONNECT_ROUTER import *
from MODE_SWITCH import *
from TELEMETRY_CSV_ROUTER import *
from ANGLE_COMMAND import *
from ANGLE_CONVERSION import *
from PLOTTING import _run_plot

####################
#PRINTS SENT TO OUTPUT BOX
####################
class PrintRedirect(QObject):
    OutputBoxSignal = Signal(str)
    def write(self, text):
        if text.strip() != "":
            self.OutputBoxSignal.emit(text)

    def bin(self):
        pass


####################
#MAIN WINDOW SETUP
####################
WINDOW_NAME = "W.A.T.C.H.T.O.W.E.R - Delta Blaze GUI"
font = QFont("Consolas")
font.setPointSize(10)

class MainWindow(QWidget):
    OutputBoxSignal = Signal(str)
    startPlotSignal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        font = QFont("Consolas")
        font.setPointSize(10)
        self.ui.OutputBox.setReadOnly(True)
        self.ui.OutputBox.setFont(font)
        self.mavlink = None
        
        # Set window title
        self.setWindowTitle(WINDOW_NAME)
        
        # Make window auto-adjustable in size
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #.SetupConnection()

        #Plot animation handle
        self.startPlotSignal.connect(self.start_plot_mainthread)
        self.plot_anim = None

        #Redierct print to OutputBox
        self.redirect = PrintRedirect()
        self.redirect.OutputBoxSignal.connect(self.append_output)
        sys.stdout = self.redirect
        sys.stderr = self.redirect

        #Angle Limits Dictionary
        self.limits = {
            "Port Flap": (0, 30),                   # 0 to 30
            "Port Aileron": (-40, 40),              # -40 to 40
            "Starboard Flap": (0, 30),              # 0 to 30
            "Starboard Aileron": (-40, 40),         # -40 to 40
            "Rudder": (-40, 40),                    # -40 to 40
            "Elevator": (-45, 45)                   # -45 to 45
        }

        #Control Surface Dictionary
        self.surface_funcs = {
            "Port Flap": set_p_flap,
            "Port Aileron": set_p_aileron,
            "Starboard Flap": set_s_flap,
            "Starboard Aileron": set_s_aileron,
            "Rudder": set_rudder,
            "Elevator": set_elevator
        }

        #Auto flap angle Dictionaries
        self.port_config = {
               "TO": 20,
               "CR": 0,
               "LD": 30
               }
        self.star_config = {
               "TO": 20,
               "CR": 0,
               "LD": 30
               }
        
        #Control surface buttons
        self.ui.FlapButtonPort.clicked.connect(lambda: self.handle_surface_cmd("Port Flap", self.ui.FlapEntryPort.text()))
        self.ui.AileronButtonPort.clicked.connect(lambda: self.handle_surface_cmd("Port Aileron", self.ui.AileronEntryPort.text()))
        self.ui.FlapButtonStar.clicked.connect(lambda: self.handle_surface_cmd("Starboard Flap", self.ui.FlapEntryStar.text()))
        self.ui.AileronButtonStar.clicked.connect(lambda: self.handle_surface_cmd("Starboard Aileron", self.ui.AileronEntryStar.text()))
        self.ui.RudderButton.clicked.connect(lambda: self.handle_surface_cmd("Rudder", self.ui.RudderEntry.text()))
        self.ui.ElevatorButton.clicked.connect(lambda: self.handle_surface_cmd("Elevator", self.ui.ElevatorEntry.text()))

        #Auto angle buttons
        self.ui.PortTakeOff.clicked.connect(lambda:self.handle_AutoAngle("Port Flap", 'P', 'TO'))
        self.ui.PortCruise.clicked.connect(lambda:self.handle_AutoAngle("Port Flap", 'P', 'CR'))
        self.ui.PortLanding.clicked.connect(lambda:self.handle_AutoAngle("Port Flap", 'P', 'LD'))
        self.ui.StarTakeOff.clicked.connect(lambda:self.handle_AutoAngle("Starboard Flap", 'S', 'TO'))
        self.ui.StarCruise.clicked.connect(lambda:self.handle_AutoAngle("Starboard Flap", 'S', 'CR'))
        self.ui.StarLanding.clicked.connect(lambda:self.handle_AutoAngle("Starboard Flap", 'S', 'LD'))

        #Control surface entry
        self.ui.FlapEntryPort.returnPressed.connect(lambda: self.handle_surface_cmd("Port Flap", self.ui.FlapEntryPort.text()))
        self.ui.AileronEntryPort.returnPressed.connect(lambda: self.handle_surface_cmd("Port Aileron", self.ui.AileronEntryPort.text()))
        self.ui.FlapEntryStar.returnPressed.connect(lambda: self.handle_surface_cmd("Starboard Flap", self.ui.FlapEntryStar.text()))
        self.ui.AileronEntryStar.returnPressed.connect(lambda: self.handle_surface_cmd("Starboard Aileron", self.ui.AileronEntryStar.text()))
        self.ui.RudderEntry.returnPressed.connect(lambda: self.handle_surface_cmd("Rudder", self.ui.RudderEntry.text()))
        self.ui.ElevatorEntry.returnPressed.connect(lambda: self.handle_surface_cmd("Elevator", self.ui.ElevatorEntry.text()))

        #UAV Control buttons
        self.ui.FBWBButton.clicked.connect(lambda: self.start_mode_thread('s'))
        self.ui.ManualButton.clicked.connect(lambda: self.start_mode_thread('m'))

        self.ui.OverrideStartButton.clicked.connect(lambda: self.handle_override("Start"))
        self.ui.OverrideStopButton.clicked.connect(lambda: self.handle_override("Stop"))

        self.ui.Kit7Connect.clicked.connect(lambda: self.start_connection_thread(7))
        self.ui.Kit8Connect.clicked.connect(lambda: self.start_connection_thread(8))
        self.ui.Kit9Connect.clicked.connect(lambda: self.start_connection_thread(9))
        print("DELTA BLAZE - GUI loaded successfully\n")

    #def SetupConnection(self):
    #    self.ui.ConnectionStartButton.clicked.connect(self.start_connection_thread)
        
    ####################
    #DISPLAY ON OUTPUT BOX
    ####################
    def append_output(self, text):
        self.ui.OutputBox.append(text)


    ####################
    #ENTRY & BUTTON SETUP
    ####################
    def handle_surface_cmd(self, surface, value):
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


    def handle_AutoAngle(self, surface, side, command):
        if side == 'P':
            value = self.port_config[command]
            threading.Thread(target=self.backend_surface_cmd,
                         args=(surface, value),
                         daemon=True).start()
        if side == 'S':
            value = self.star_config[command]
            threading.Thread(target=self.backend_surface_cmd,
                         args=(surface, value),
                         daemon=True).start()


    def handle_override(self, command):
        if not self.mavlink:
            print("Error - Cannot send command (no connection)")
            return
        try:
            if command == "Start":
                start_override(self.mavlink)
                print("[CMD] Override started")
            elif command == "Stop":
                stop_override(self.mavlink)
                print("[CMD] Override stopped")
        except Exception as exception:
            print (f"Error - failed to send {command} override command")


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


    def start_connection_thread(self, kit):
        threading.Thread(target=self.backend_connect, args=(kit,), daemon=True).start()


    def backend_connect(self, kit):
        try:

            print("[CONNECT] Starting MAVLink connection, wait 3 seconds...")
            self.mavlink = connection_start(kit)

            if self.mavlink is None:
                print("Error - No heartbeat detected")
                return
            
            print("[CONNECT] Connected. Starting listener thread...")
            run_status_refresh(self.mavlink)
            
            # Start CSV logging with kit-specific sensor conversion
            start_csv_logging(kit=kit)

            self.startPlotSignal.emit()

        except Exception as e:
            print (f"Error - MAVLink connection failed: {e}")


    def start_mode_thread(self, mode):
        threading.Thread(target=self.backend_switch_mode, args=(mode,), daemon=True).start()
        

    def backend_switch_mode(self, mode):
        if not self.mavlink:
            print("Error - Cannot switch modes (no connection)")#
            return
        command_mode(self.mavlink, mode)


    def closeEvent(self, event):
        """
        Handle window close event to clean up CSV logging.
        """
        stop_csv_logging()
        event.accept()


    def start_plot_mainthread(self):

        # Starts the Matplotlib plotting window.
        # This runs on the Qt main thread via a signal.

        if self.plot_anim is None:
            self.plot_anim = _run_plot(self.mavlink)


####################
# RUN AVIONICS
####################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create and show splash screen
    splash_path = os.path.join(os.path.dirname(__file__), "watchtower.png")
    splash_pixmap = QPixmap(splash_path)
    splash = QSplashScreen(splash_pixmap)
    splash.setWindowFlags(splash.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)
    splash.show()
    app.processEvents()
    
    # Initialize main window
    window = MainWindow()
    icon_path = os.path.join(os.path.dirname(__file__), "logo.ico")
    window.setWindowIcon(QIcon(icon_path))
    
    # Show main window
    window.show()
    
    # Keep splash on top and visible
    splash.raise_()
    splash.activateWindow()
    
    # Close splash after 1.5 seconds using Qt timer
    def close_splash():
        splash.hide()
    
    QTimer.singleShot(3500, close_splash)
    
    sys.exit(app.exec())
