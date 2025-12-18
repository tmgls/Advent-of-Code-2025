input = open("input", 'r', encoding="UTF-8").read().strip().split('\n')

machine_plans = [[line.split(' ')[0], line.split(' ')[1:-1], line.split(' ')[-1]] for line in input]

class machine:
    def __init__(self, lights, buttons, joltage):
        self.lights = [int(x == '#') for x in lights[1:-1]]
        self.buttons = [[int(b) for b in button[1:-1].split(',')] for button in buttons]
        self.joltage = joltage

    def try_presses(self, press_list):
        light_state = [0 for light in self.lights]
        for press in press_list:
            for light in press:
                light_state[light] = (light_state[light] + 1) % 2
        return (light_state == self.lights)

machines = [machine(plan[0], plan[1], plan[2]) for plan in machine_plans]

def rec_press(machine, presses):
    if not len(presses):
        presses = [[button] for button in machine.buttons]
    else:
        new_presses = []
        for button in machine.buttons:
            for pl in presses:
                if button not in pl:
                    new_presses.append([*pl, button])
        presses = new_presses

    for press_list in presses:
        if machine.try_presses(press_list):
            return len(press_list)

    return rec_press(machine, presses)

total = 0
for m in machines:
    total += rec_press(m, [])
print(total)
# part 2
# now each press is not a bitwise xor; could be many presses
