"""
--- Part Two ---
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.

Given this additional criterion, but still ignoring the range rule, the following are now true:

112233 meets these criteria because the digits never decrease and all repeated digits are exactly two digits long.
123444 no longer meets the criteria (the repeated 44 is part of a larger group of 444).
111122 meets the criteria (even though 1 is repeated more than twice, it still contains a double 22).
How many different passwords within the range given in your puzzle input meet all of the criteria?

Your puzzle input is still 256310-732736.
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

    # number grouping
    counts = {}
    for number in string_input:
        if number not in counts:
            counts[number] = 1
        else:
            counts[number] += 1

    for key, count in counts.iteritems():
        if count == 2:
            return True
    return False



if __name__ == '__main__':
    main()
