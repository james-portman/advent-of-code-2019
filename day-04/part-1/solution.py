"""
--- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 256310-732736.
"""
def main():
    matches = []
    input = [256310, 732736]
    for i in range(input[0], input[1]+1):
        if check(i):
            matches.append(i)

    print(matches)
    print(len(matches))

def check(input):
    string_input = str(input)

    # digits never decrease
    for i in range(len(string_input)-1):
        if int(string_input[i]) > int(string_input[i+1]):
            return False

    # 2 adjacent digits match
    doubles = False
    for i in range(len(string_input)-1):
        if string_input[i] == string_input[i+1]:
            doubles = True
            break

    return doubles



if __name__ == '__main__':
    main()
