### Kate Macias
### Software Engineering 1
### Fall 2026

# On Car Computer


## Types
Floor = int                
Direction = Up/Down/Idle
DoorResult = Opened/Closed

## On-car computer: Inputs
button_press(button: int) -> None
floor_sensor(floor: Floor) -> None

## On-car computer: Outputs
set_display(floor: Floor) -> bool          
open_doors() -> DoorResult
