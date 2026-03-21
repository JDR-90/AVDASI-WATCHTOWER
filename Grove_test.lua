local bus = 1       -- I²C2 on Cube+
local addr = 0x36   -- AS5600 default address

local dev = i2c.get_device(bus, addr)
if dev then
    -- Try reading the Z position registers (0x1A = ZPOS_HIGH, 0x1B = ZPOS_LOW)
    local ok, data = dev:read_registers(0x1A, 2)
    if ok then
        local pos = data[1] * 256 + data[2]
        gcs:send_text(0, string.format("AS5600 detected! Z position: %d", pos))
    else
        gcs:send_text(0, "AS5600 found but read failed")
    end
else
    gcs:send_text(0, "No device at 0x36 on bus 1")
end
