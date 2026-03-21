-- read_angle.lua
local uart_id = 2
local baud = 115

function init()
    uart = io.Serial(uart_id, baud)
end

function loop()
    local line = uart:read()
    if line then
        local angle = tonumber(line)
        -- send as MAVLink named value
        mavlink:send_named_value_float("AS5600_ANGLE", angle)
    end
end