from StoreTasks import store


def solve_task(pid, var):
    print("solving task")
    if pid == 0:
        return echo(var)
    elif pid == 1:
        return echo_square(var)
    elif pid == 2:
        return series(var)
    elif pid == 3:
        return apple(var)
    elif pid == 4:
        return star(var)
    elif pid == 5:
        return star_advance(var)
    elif pid == 6:
        return FIB(var)


def echo(number):
        return number 

def echo_square(number):
    return int(number ** 2)

def series(number):
    return int((number * (number + 1)) / 2)

def apple(number):
    # apple_num = 500 % number   # these apple to sell
    # money = 0
    # discount = 1
    # while(apple_num > 0):
    #     if apple_num >= 10:
    #         money = money + 10 * 30 * discount
    #         apple_num -= 10
    #     else:
    #         money = money + apple_num * 30 * discount
    #         apple_num = 10
    #     discount -= 0.05
        
    # return int(money)
    return store.get_apple(number)

def star(number):
    # ans = ''
    # for i in range(number):
    #     for _ in range(i + 1):
    #         ans = ans + '*'
    #     if i < number-1:
    #         ans = ans + "\n"

    # return ans
    return store.get_star(number)

def star_advance(number):
    # ans = ''
    # for i in range(number):
    #     for _ in range(number - i - 1):
    #         ans += ' '
    #     for _ in range((i + 1)*2 - 1):
    #         ans += '*'
    #     if i < number - 1:
    #         ans += "\n"
    # return ans
    return store.get_advance_star(number)

def FIB(number):
    # a = [0 for i in range(200)]
    # a[1] = 1
    # a[2] = 1

    # for i in range(3, number + 1):
    #     a[i] = a[i-1] + a[i-2]
        
    # ans = int(a[number])    
    # return ans
    return store.get_FIB(number)


# test
if __name__ == '__main__':
    
    x = int(input("input something "))
    print("echo_square:\n", repr(echo_square(x)))
    print("series:\n", repr(series(x)))
    print("apple:\n", repr(apple(x)))
    print("star:\n", repr(star(x)))
    print("star_advance:\n", repr(star_advance(x)))
    print("FIB:\n", repr(FIB(x)))
    

# The following are old unsed tasks
# def solve_task1(number):   # square
#     ans: str
#     flag = False
#     for i in range(16):
#         y = (i+1)**2 + (i+2)**2 + (i+3)**2
#         if y == number:
#             ans = "yes"
#             flag = True
#             break

#     if flag == False:
#         ans = "no"
#     return ans


# def solve_task2(number):   # star
#     ans = ''
#     for i in range(number):
#         for _ in range(i + 1):
#             ans = ans + '*'
#         ans = ans + "\n"
#     ans.strip()
#     return ans

# def solve_task3(number):   # FIB
#     a = [0 for i in range(200)]
#     a[1] = 1
#     a[2] = 1

#     for i in range(3, number + 1):
#         a[i] = a[i-1] + a[i-2]
        
#     ans = str(a[number])    
#     return ans

# def solve_task4(number):   # identity matrix
#     ans = ''
#     for i in range(number):
#         for j in range(number):
#             if i == j:
#                 ans = ans + '1'
#             else:
#                 ans = ans + '0'
#         ans = ans + "\n"
#     return ans

# def solve_task5(number):   # recursive
#     ans = task4_recur(number)
#     ans = str(ans)
#     return ans



# def solve_task6(number):  # easy problem
#     global a
#     ans = ''
#     n = number
#     size = 2**n
#     a = [[0] * size for _ in range(size)]
#     task5_recur(0, 0, n)
    
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             ans = ans + str(a[i][j])
#             if j < len(a[i])-1:
#                 ans += ' '
#         ans = ans + "\n"

#     return ans



# # def solve_task6(number):
# #     ans = ''
    

# def task4_recur(x: int):
#     if x % 2 == 0:
#         return task4_recur(x / 2)
#     elif x != 1:
#         return task4_recur(x - 1) + task4_recur(x + 1)
#     return 1


# a = []
# c = 1
# def task5_recur(px, py, n):
#         global c
#         if n == 0:
#             a[px][py] = c
#             c += 1
#             return
#         task5_recur(px, py, n-1)
#         task5_recur(px, py + 2**(n-1), n-1)
#         task5_recur(px + 2**(n-1), py, n-1)
#         task5_recur(px + 2**(n-1), py + 2**(n-1), n-1)
#         return