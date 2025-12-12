
def divide_in_half(i: int) -> tuple[str, str]:
    s = str(i)
    return s[0:len(s)//2], s[len(s)//2:]

def part_one(input_: str):
    # [[start, end], [start, end], ..]
    sum_ = 0
    ranges: list[list[str]] = input_.split(",")
    for range_ in ranges:
        start, end = range_.split("-")
        for i in range(int(start), int(end)+1):
            first, second = divide_in_half(i)
            if first == second:
                sum_ += i
    print(sum_)



if __name__ == "__main__":
    with open("input.txt") as file:
        input_ = file.read()
    part_one(input_)

