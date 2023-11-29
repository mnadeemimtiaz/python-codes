class Elevator:
    def __init__(floor, start_level, end_level):
        floor.current_level = start_level
        floor.start_level = start_level
        floor.end_level = end_level

   
    def level_up(floor):
        if floor.current_level < floor.end_level:
            floor.current_level += 1
            print(f"Elevator moved up to Floor {floor.current_level}")
        else:
            print(f"Elevator is already at the top Floor{floor.end_level}")

    def level_down(floor):
        if floor.current_level > floor.start_level:
            floor.current_level -= 1
            print(f"Elevator moved down to Floor {floor.current_level}")
        else:
            print(f"Elevator is already at the bottom Floor {floor.start_level}")

    def go_to_level(floor, target_level):
        if target_level < floor.start_level or target_level > floor.end_level:
            print(f"Invalid  Building Floor selected ! {target_level}. Elevator is only between {floor.start_level} and {floor.end_level}.")
            return

        while floor.current_level != target_level:
            if target_level > floor.current_level:
                floor.level_up()
            else:
                floor.level_down()



if __name__ == "__main__":
    elevator = Elevator(start_level=0, end_level=15)

    target_level = int(input("Enter the target Floor: "))
    elevator.go_to_level(target_level)
