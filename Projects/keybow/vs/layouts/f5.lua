require "keybow"

function setup() -- Set custom lights up
    keybow.auto_lights(false)
    keybow.clear_lights()
end

lightStep = 21.25
countSteps = 0

function lightUp(buttonIndex)
    
    if countSteps > 255 then
        keybow.clear_lights()
        countSteps = 0
    end

    countSteps = countSteps + lightStep
    keybow.set_pixel(buttonIndex, 0, 0, countSteps)
end

function handle_key_00(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(0)
    end
end

function handle_key_01(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(1)
    end
end

function handle_key_02(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(2)
    end
end

function handle_key_03(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(3)
    end
end

function handle_key_04(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(4)
    end
end

function handle_key_05(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(5)
    end
end

function handle_key_06(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(6)
    end
end

function handle_key_07(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(7)
    end
end

function handle_key_08(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(8)
    end
end

function handle_key_09(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(9)
    end
end

function handle_key_10(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(10)
    end
end

function handle_key_11(pressed)
    if pressed then
        keybow.set_key(keybow.F5, pressed)
        lightUp(11)
    end
end
