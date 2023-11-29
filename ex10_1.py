class Elevator:
    def __init__(self, start_level, end_level):
        self.current_level = start_level
        self.start_level = start_level
        self.end_level = end_level

    def go_to_level(self, target_level):
        if target_level < self.start_level or target_level > self.end_level:
            print(f"Invalid  Building Floor selected ! {target_level}. Elevator is only between {self.start_level} and {self.end_level}.")
            return

        while self.current_level != target_level:
            if target_level > self.current_level:
                self.level_up()
            else:
                self.level_down()

    def level_up(self):
        if self.current_level < self.end_level:
            self.current_level += 1
            print(f"Elevator moved up to Floor {self.current_level}")
        else:
            print(f"Elevator is already at the top Floor{self.end_level}")

    def level_down(self):
        if self.current_level > self.start_level:
            self.current_level -= 1
            print(f"Elevator moved down to Floor {self.current_level}")
        else:
            print(f"Elevator is already at the bottom Floor {self.start_level}")

if __name__ == "__main__":
    elevator = Elevator(start_level=0, end_level=15)

    target_level = int(input("Enter the target Floor: "))
    elevator.go_to_level(target_level)
