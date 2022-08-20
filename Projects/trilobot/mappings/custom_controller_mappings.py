from trilobot.simple_controller import SimpleController




def create_8bitdo_zero2_controller():
    """ Create a controller class for the 8BitDo Zero 2 gamepad controller.
    """
    controller = SimpleController("8BitDo Zero 2 gamepad")

    # Button and axis registrations
    controller.register_button("A", 305)
    controller.register_button("B", 304)
    controller.register_button("X", 307)
    controller.register_button("Y", 306)
    
    controller.register_button("Start", 311)
    controller.register_button("Select", 310)
    
    controller.register_button("L1", 308, alt_name="LB")
    controller.register_button("R1", 309, alt_name="RB")
    
    controller.register_axis_as_button("Left", 0, 0, 32768)
    controller.register_axis_as_button("Right", 0, 65535, 32768)
    controller.register_axis_as_button("Up", 1, 0, 32768)
    controller.register_axis_as_button("Down", 1, 65535, 32768)

    controller.register_axis_as_button("L_Left", 0, 0, 32768)
    controller.register_axis_as_button("L_Right", 0, 65535, 32768)
    controller.register_axis_as_button("L_Up", 1, 0, 32768)
    controller.register_axis_as_button("L_Down", 1, 65535, 32768)
    
    
    #controller.register_axis_as_button("Left", 0, 0, 32768)
    #controller.register_axis_as_button("Right", 0, 65535, 32768)
    
    #controller.register_axis_as_button("Up", 1, 0, 32768)
    #controller.register_axis_as_button("Down", 1, 65535, 32768)

    #controller.register_axis("LX", 0, 0, 65535)
    #controller.register_axis("LY", 1, 0, 65535)
    
    #controller.register_axis("LX", 0, 0, 127)
    #controller.register_axis("RX", 0, 255, 127)
    
    #controller.register_axis("LY", 0, 0, 127)
    #controller.register_axis("RY", 1, 255, 127)
    
    
    
    return controller


# Not Fully Working
def create_xbox_one_wireless_controller(stick_deadzone_percent=0.2):
    """ Create a controller class for the XBoxOne Wireless controller.
    stick_deadzone_percent: the deadzone amount to apply to the controller's analog sticks
    """
    controller = SimpleController("Xbox Wireless Controller")

    # Button and axis registrations for XBox One Controller
    controller.register_button("A", 304, alt_name="Cross")
    controller.register_button("B", 305, alt_name="Circle")
    controller.register_button("X", 307, alt_name="Square")
    controller.register_button("Y", 308, alt_name="Triangle")
    controller.register_button("Start", 315)
    controller.register_button("Select", 314)
    controller.register_button("Home", 316)
    controller.register_button("LB", 310, alt_name="L1")
    controller.register_axis_as_button("LT", 2, 255, 0, alt_name="L2")
    controller.register_button("RB", 311, alt_name="R1")
    controller.register_axis_as_button("RT", 5, 255, 0, alt_name="R2")
    controller.register_button("Left", 704)
    controller.register_button("Right", 705)
    controller.register_button("Up", 706)
    controller.register_button("Down", 707)
    controller.register_button("LS", 317, alt_name="L3")
    controller.register_button("RS", 318, alt_name="R3")

    controller.register_axis("LX", 0, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("LY", 1, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RX", 2, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_axis("RY", 3, -32768, 32768, deadzone_percent=stick_deadzone_percent)
    controller.register_trigger_axis("LT", 4, 0, 32768, alt_name="L2")
    controller.register_trigger_axis("RT", 5, 0, 32768, alt_name="R2")
    return controller

def choose_controller():
    """ Present the user with a selection menu for pre-configured controllers.
    """
    controller_list = [("8BitDo Zero 2", create_8bitdo_zero2_controller),
                       ("XBoxOne Wireless Controller", create_xbox_one_wireless_controller)]

    print("Currently supported controllers:")
    for i in range(0, len(controller_list)):
        print("  ", i, ") ", controller_list[i][0], sep="")

    try:
        controller_id = int(input("Select controller: "))
        if controller_id < 0 or controller_id >= len(controller_list):
            print("Not a valid controller. Exiting")
            quit()

        print("Selected:", controller_list[controller_id][0], end="\n\n")
        return controller_list[controller_id][1]()
    except ValueError:
        print("Not a number. Exiting")
        quit()
