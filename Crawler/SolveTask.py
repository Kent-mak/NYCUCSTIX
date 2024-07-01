def solve_task(pid, var):
    if pid == 0:
        return solve_task0(var)
    elif pid == 1:
        return solve_task1(var)
    elif pid == 2:
        return solve_task2(var)
    elif pid == 3:
        return solve_task3(var)
    elif pid == 4:
        return solve_task4(var)
    elif pid == 5:
        return solve_task5(var)
    elif pid == 6:
        return solve_task6(var)

def solve_task0(number):
    return number 

def solve_task1(number):  # square
    return number**2


def solve_task2(number):   # series
    return int((number)*(number+1)/2)

def solve_task3(number):   # apple
    left_apple = 500 % number
    price = 30
    money = 0
    rate = 1
    while left_apple > 0:
        current_apple = 0
        if left_apple >= 10:
            current_apple = 10
        else:
            current_apple = left_apple

        money += current_apple * price * rate
        
        rate -= 0.05
        left_apple -= current_apple
    return (int(money))

def solve_task4(number):
    result = ""
    for i in range(number):
        for j in range(i + 1):
            result += "*"
        result += "\n"
    return result


def solve_task5(number):   # star-advanced
    a = ""
    for i in range(number):
        for j in range(number-i-1):
            a += " "
        for j in range((i+1)*2 - 1):
            a += "*"
        a += '\n'
    a = a[:-1] # 把最後一個"\n"刪掉
    return a


a = [0] * (200 + 1)  # 使用 number+1 大小的列表，索引從0到number
a[1] = 1
a[2] = 1
def solve_task6(number):
    
    if number <= 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    elif a[number] != 0:
        return a[number]
    elif a[number] == 0:
        a[number] = solve_task6(number - 1) + solve_task6(number - 2)
        return a[number]
    