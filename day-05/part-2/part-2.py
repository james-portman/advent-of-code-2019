"""
--- Part Two ---
The air conditioner comes online! Its cold air feels good for a while, but then the TEST alarms start to go off. Since the air conditioner can't vent its heat anywhere but back into the spacecraft, it's actually making the air inside the ship warmer.

Instead, you'll need to use the TEST to extend the thermal radiators. Fortunately, the diagnostic program (your puzzle input) is already equipped for this. Unfortunately, your Intcode computer is not.

Your computer is only missing a few opcodes:

Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
Like all instructions, these instructions need to support parameter modes as described above.

Normally, after an instruction is finished, the instruction pointer increases by the number of values in that instruction. However, if the instruction modifies the instruction pointer, that value is used and the instruction pointer is not automatically increased.

For example, here are several programs that take one input, compare it to the value 8, and then produce one output:

3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)
Here's a larger example:

3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99
The above example program uses an input instruction to ask for a single number. The program will then output 999 if the input value is below 8, output 1000 if the input value is equal to 8, or output 1001 if the input value is greater than 8.

This time, when the TEST diagnostic program runs its input instruction to get the ID of the system to test, provide it 5, the ID for the ship's thermal radiator controller. This diagnostic test suite only outputs one number, the diagnostic code.

What is the diagnostic code for system ID 5?
"""


import sys

def attempt(puzzle_input):
    ram = []

    with open("../input.txt") as input_file:
        input = input_file.read().split(",")

    for item in input:
        ram.append(int(item))

    # prep
    # ram[1] = input1
    # ram[2] = input2

    pc = 0

    while True:
        # print("")
        next = ram[pc]
        pc += 1

        next_str = f"{next:05d}"
        # print(next_str)

        opcode = int(next_str[-2:])

        p1_immediate = bool(int(next_str[-3]))
        p2_immediate = bool(int(next_str[-4]))
        p3_immediate = bool(int(next_str[-5]))

        # print(opcode, p1_immediate, p2_immediate, p3_immediate)


        # print(opcode)
        if opcode == 1 or opcode == 2:
            # print("add or multiply")
            x = ram[pc]
            # print(x)
            pc += 1
            if not p1_immediate:
                x = ram[x]

            y = ram[pc]
            # print(y)
            pc += 1
            if not p2_immediate:
                y = ram[y]

            z_addr = ram[pc]
            pc += 1

            if opcode == 1:
                z = x + y
            elif opcode == 2:
                z = x * y
            if p3_immediate:
                print("DONT KNOW WHAT TO DO")
                sys.exit(1)
            else:
                ram[z_addr] = z

        elif opcode == 3:
            # print("store input at address")
            address = ram[pc]
            pc += 1
            # print(address)
            ram[address] = puzzle_input[0]

        elif opcode == 4:
            # output parameter
            address = ram[pc]
            pc += 1
            print("OUTPUT -")
            print(ram[address])

        elif opcode == 5 or opcode == 6:
            param = ram[pc]
            pc += 1
            if not p1_immediate:
                param = ram[param]

            jump_to = ram[pc]
            pc += 1
            if not p2_immediate:
                jump_to = ram[jump_to]

            # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            if opcode == 5:
                if param != 0:
                    pc = jump_to

            # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
            elif opcode == 6:
                if param == 0:
                    pc = jump_to


        elif opcode == 7 or opcode == 8:

            p1 = ram[pc]
            pc += 1
            if not p1_immediate:
                p1 = ram[p1]

            p2 = ram[pc]
            pc += 1
            if not p2_immediate:
                p2 = ram[p2]

            p3 = ram[pc]
            pc += 1
            # if not p3_immediate:
            #     p3 = ram[p3]

            # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            if opcode == 7:
                if p1 < p2:
                    ram[p3] = 1
                else:
                    ram[p3] = 0

            # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0.
            elif opcode == 8:
                if p1 == p2:
                    ram[p3] = 1
                else:
                    ram[p3] = 0


        elif opcode == 99:
            # print("opcode 99 - exit")
            return ram[0]

        else:
            # print("Unknown opcode, ARGH")
            print(opcode)
            sys.exit(1)


attempt([5])











#
