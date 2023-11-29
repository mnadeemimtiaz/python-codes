class Elevator:
    def __init__(self, start_level, end_level):
        self.current_level = start_level
        self.start_level = start_level
        self.end_level = end_level

    def level_up(self):
        if self.current_level < self.end_level:
            self.current_level += 1
            print(f"Elevator moved up to Level {self.current_level}")
        else:
            print(f"Elevator is already at the top Level {self.end_level}")

    def level_down(self):
        if self.current_level > self.start_level:
            self.current_level -= 1
            print(f"Elevator moved down to Level {self.current_level}")
        else:
            print(f"Elevator is already at the bottom Level {self.start_level}")

    def go_to_level(self, dest_lvl):
        if dest_lvl < self.start_level or dest_lvl > self.end_level:
            print(f"Invalid Building Level selected! {dest_lvl}. Elevator is only between {self.start_level} and {self.end_level}.")
            return

        while self.current_level != dest_lvl:
            if dest_lvl > self.current_level:
                self.level_up()
            else:
                self.level_down()


class Building:
    def __init__(self, bottom_level, top_level, num_elevators):
        self.bottom_level = bottom_level
        self.top_level = top_level
        self.elevators = [Elevator(bottom_level, top_level) for _ in range(num_elevators)]

    def run_elevator(self, elev_no, dest_lvl):
        if not (0 <= elev_no < len(self.elevators)):
            pass
        elevator = self.elevators[elev_no]
        elevator.go_to_level(dest_lvl)


if __name__ == "__main__":
    bottom_level = 0
    top_level = 15
    num_elevators = 3

    building = Building(bottom_level, top_level, num_elevators)

    building.run_elevator(1, 5)
    building.run_elevator(2, 10)
