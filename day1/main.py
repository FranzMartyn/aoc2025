
def part_one(lines, dial):
    count = 0
    for line in lines:
        rotation = line[0]
        number = int(line[1:])
        dial = (dial - number if rotation == "L"  else dial + number) % 100
        count += (dial == 0)
    return count

def part_two(lines, dial):
    count = 0
    for line in lines:
        rotation = line[0]
        number = int(line[1:])
        for i in range(number):
            # This solution is as cheap as a 5€ phone but hey it works
            dial = dial - 1 if rotation == "L"  else dial + 1
            if not 0 < dial < 100:
                count += 1
            dial = dial % 100
    return count


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = input_file.readlines()
    dial = 50
    print(part_two(lines, dial))

