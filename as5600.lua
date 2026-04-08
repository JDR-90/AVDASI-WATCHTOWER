-- AS5600 I2C Lua script with 50 Hz DataFlash logging

local AS5600_ADDR = 0x36
local ANGLE_MSB   = 0x0E

local LOG_NAME = "AS56"

-- initialise I2C device (bus 0)
local dev = i2c:get_device(0, AS5600_ADDR)

local last_print = 0

function update()

    if not dev then
        gcs:send_text(6, "AS5600: I2C device not found")
        return update, 1000
    end

    -- read 2 bytes from angle register
    local data = dev:read_registers(ANGLE_MSB, 2)

    if not data then
        gcs:send_text(6, "AS5600: read failed")
        return update, 200
    end

    local msb = data[1]
    local lsb = data[2]

    -- convert to 12-bit raw value
    local raw = ((msb << 8) | lsb) & 0x0FFF

    -- convert to degrees
    local angle = raw * 360.0 / 4096.0

    ------------------------------------------------
    -- WRITE TO DATAFLASH BIN LOG
    ------------------------------------------------
    logger:write(
        LOG_NAME,      -- message name in log
        "Raw,Angle",   -- field names
        "If",          -- I = uint16, f = float
        raw,
        angle
    )

    ------------------------------------------------
    -- debug message every ~2 seconds
    ------------------------------------------------
    local now = millis()
    if now - last_print > 2000 then
        gcs:send_text(0, string.format("AS5600 %.2f deg", angle))
        last_print = now
    end

    -- run again in 20 ms → 50 Hz
    return update, 20
end

return update()