"""
--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
"""
import sys

with open("../input.txt") as input_file:
    wires = input_file.read().split("\n")

dots = {}

length_to_cross = []

wire_actions = [
    wires[0].split(","),
    wires[1].split(",")
    ]
# print(wire_actions)

x = [0, 0]
y = [0, 0]
length_moved = 0

actions_done = 0

intersections = []

for action_num in range(len(wire_actions[0])): # iterate the right number of times

    for wirenum in [0, 1]:

        actions_done += 1

        action = wire_actions[wirenum][action_num]
        # print(action)
        amount = int(action[1:])
        for _ in range(amount):
            if action[0] == "U":
                y[wirenum] += 1
            elif action[0] == "D":
                y[wirenum] -= 1
            elif action[0] == "L":
                x[wirenum] -= 1
            elif action[0] == "R":
                x[wirenum] += 1

            length_moved += 1

            coord = "%s_%s" % (x[wirenum], y[wirenum])
            # print(coord)
            if coord in dots:
                if dots[coord] == (wirenum + 1):
                    # print("Crashed with itself")
                    pass
                else:
                    dots[coord] = dots[coord] | (wirenum + 1) # 1 OR 2
                    if dots[coord] == 3:
                        print("Found first intersection (must be shortest)")
                        intersections.append({"x": x[wirenum], "y": y[wirenum]})

            else:
                dots[coord] = wirenum + 1

print(intersections)



totals = []

# go through each wire to see exactly how far they both go to reach it
for i in range(len(intersections)):
    done = [False, False]
    for wirenum in [0, 1]:
        print("wire", wirenum)
        x = 0
        y = 0
        total_length_moved = 0
        for action_num in range(len(wire_actions[0])): # iterate the right number of times

            if done[wirenum]:
                break

            action = wire_actions[wirenum][action_num]
            # print(action)
            amount = int(action[1:])
            for _ in range(amount):
                if action[0] == "U":
                    y += 1
                elif action[0] == "D":
                    y -= 1
                elif action[0] == "L":
                    x -= 1
                elif action[0] == "R":
                    x += 1

                total_length_moved += 1

                if x == intersections[i]['x'] and y == intersections[i]['y']:
                    intersections[i]['wire'+str(wirenum)] = total_length_moved
                    if wirenum == 1:
                        totals.append(intersections[i]['wire'+str(0)]+intersections[i]['wire'+str(1)])


print(intersections)
print(sorted(totals))
