require "keybow"

state = 0 -- 0 for home, 1 for Visual Studio, 2 for Visual Studio Code

-- Setup --

function setup() -- Set custom lights up
    keybow.auto_lights(false)
    keybow.clear_lights()
    keybow.set_pixel(0, 60,118,61) -- Green
    keybow.set_pixel(1, 28,137,210) -- Blue
    keybow.set_pixel(2, 140,104,200) -- Purple
end

-- Functions

function vsc_blue()
    keybow.set_pixel(3, 0, 0, 0) -- Off
    keybow.set_pixel(4, 28, 137, 210) -- Normal Blue
    keybow.set_pixel(5, 60, 169, 242) -- Light Blue

    keybow.set_pixel(6, 20,113,176) -- Dark Blue
    keybow.set_pixel(7, 0, 0, 0) -- Off
    keybow.set_pixel(8, 60, 169, 242) -- Light Blue
    
    keybow.set_pixel(9, 0, 0, 0) -- Off
    keybow.set_pixel(10, 28, 137, 210) -- Normal Blue
    keybow.set_pixel(11, 60, 169, 242) -- Light Blue
end 

function vs_purple()
    keybow.set_pixel(3, 0, 0, 0) -- Off
    keybow.set_pixel(4, 140,104,200) -- Normal Purple
    keybow.set_pixel(5, 179,145,237) -- Light Purple

    keybow.set_pixel(6, 90,58,142) -- Dark Purple
    keybow.set_pixel(7, 0, 0, 0) -- Off
    keybow.set_pixel(8, 179,145,237) -- Light Purple

    keybow.set_pixel(9, 0, 0, 0) -- Off
    keybow.set_pixel(10, 140,104,200) -- Normal Purple
    keybow.set_pixel(11, 179,145,237) -- Light Purple
end 

function home()
    -- Groups

    keybow.set_pixel(0, 60,118,61) -- Green
    keybow.set_pixel(1, 28,137,210) -- Blue
    keybow.set_pixel(2, 140,104,200) -- Purple

    -- Icon

    keybow.set_pixel(3, 0, 0, 0) -- Off
    keybow.set_pixel(4, 60, 118, 61) -- Green
    keybow.set_pixel(5, 0, 0, 0) -- Off

    keybow.set_pixel(6, 60, 118, 61) -- Green
    keybow.set_pixel(7, 0, 0, 0) -- Off
    keybow.set_pixel(8, 60, 118, 61) -- Green
    
    keybow.set_pixel(9, 60, 118, 61) -- Green
    keybow.set_pixel(10, 60, 118, 61) -- Green
    keybow.set_pixel(11, 60, 118, 61) -- Green
end 

-- Key mappings --

-- Reserved for groupings of keys

function handle_key_00(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        state = 0
        home()
    end
end

function handle_key_01(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        state = 1
        vsc_blue()
    end
end

function handle_key_02(pressed)
    if pressed then
        --keybow.set_key("", pressed)
        state = 2
        vs_purple()
    end
end

-- Command Keys

function handle_key_03(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end

function handle_key_04(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end

function handle_key_05(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end

function handle_key_06(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end

function handle_key_07(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end

function handle_key_08(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end

function handle_key_09(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end

function handle_key_10(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end

function handle_key_11(pressed)
    if pressed then
        keybow.set_key("", pressed)
    end
end
