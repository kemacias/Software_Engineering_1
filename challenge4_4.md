### Kate Macias
### Software Engineering 1
### Fall 2026


# My Code

```python
# Kate Macias
# Software Engineering
# Fall 2026
#

# You can't modify this code
# 
# 

from tkinter.constants import X


class SidewinderJoystick:
    BUTTON_UP = 2
    BUTTON_DOWN = 3

    def get_x_axis(self, stick_id) # returns -1.0 to 1.0
    def get_y_axis(self, stick_id) # returns -1.0 to 1.0
    def button(self, button_id)    # Returns BUTTON_UP or BUTTON_DOWN

class XboxGamepad:
    def get_x_axis(stick_id) # returns -128 to 127
    def get_y_axis(stick_id) # returns -128 to 127
    def button_status(button_id)  # float from 0.0 (up) to 1.0 (down)


    #----------------------------------------#
def compatible_xbox(controller_1):
    comp_x_axis = 127 / XboxGamepad.get_x_axis(stick_id) * 100
    comp_y_axis = 127 / XboxGamepad.get_y_axis(stick_id) * 100
    return comp_x_axis_xbox, comp_y_axis_xbox


def compatible_sw(controller_1):
    comp_x_axis = 1 / SidewinderJoystick.get_x_axis(stick_id) * 100
    comp_y_axis = 1 / SidewinderJoystick.get_y_axis(stick_id) * 100
    return comp_x_axis_sw, comp_y_axis_sw

def compatible_key(controller_1):
    if x_axis_key > 0:
        comp_x_axis = 100
    else:
        y_axis_key = 0:
    if y_axis_key > 0:
        comp_y_axis = 100
    else:
        comp_y_axis = 0
    return comp_x_axis_sw, comp_y_axis_sw

if config.joystick == SIDEWINDER:
    joystick = compatible_sw(SidewinderJoystick.self)
elif config.joystick == compatible_xbox(XboxGamepad.self):
    joystick = WrappedXboxController()

p = Player(joystick)

# ... Game code continues ...



class Player:
    def __init__(self, sidewinder):
        self.x = 0
        self.y = 0
        self.sidewinder = sidewinder

        def update()  # called every game frame
            self.x += sidewinder.get_x_axis(1)
            self.y += sidewinder.get_y_axis(1)

            if sidewinder.button(4) == SidewinderJoystick.BUTTON_DOWN:
                self.fire_lasers()

            self.update_graphics()

        # ...
        # You can't modify this code



    sidewinder = SidewinderJoystick()
    p = Player(sidewinder)

    # ... Game code continues ...
```

## One or two sentences (or code if you prefer) describing how you might also add the keyboard as a method of input in addition to the two joysticks.

### I would follow the same logic with a function that turned the keyboard input into a percentage of the range of inputs it accepts. keyboards would be a little different since they are on or off, so it would be 0% or 100% (see compatible_key() )

## Answer: how was the author of the original code being short-sighted?

### He didn't account for the variety of inputs of the different controllers. with just his code its really difficult to add new controller support.
