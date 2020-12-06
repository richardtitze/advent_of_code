def seat_id(instructions):
    return int(instructions.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0'), 2)


seats = [seat_id(line) for line in open("input.txt").readlines()]
seats.sort()


def problem1():
    print(seats[-1])


def problem2():
    for index, id in enumerate(seats):
        if seats[index+1] != id + 1:
            print(id+1)
            return

problem1()
problem2()