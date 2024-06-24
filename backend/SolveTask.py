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

def solve_task0(number):   # square
    ans: str
    flag = False
    for i in range(16):
        y = (i+1)**2 + (i+2)**2 + (i+3)**2
        if y == number:
            ans = "yes"
            flag = True
            break

    if flag == False:
        ans = "no"
    return ans


def solve_task1(number):   # star
    ans = ''
    for i in range(number):
        for j in range(i + 1):
            ans = ans + '*'
        ans = ans + "\n" 
    return ans

def solve_task2(number):   # FIB
    a = [0 for i in range(200)]
    a[1] = 1
    a[2] = 1

    for i in range(3, number):
        a[i] = a[i-1] + a[i-2]
        
    ans = str(a[i])    
    return ans

def solve_task3(number):   # identity matrix
    ans = ''
    for i in range(number):
        for j in range(number):
            if i == j:
                ans = ans + '1'
            else:
                ans = ans + '0'
        ans = ans + "\n"
    return ans

def solve_task4(number):   # recursive
    ans = task4_recur(number)
    ans = str(ans)
    return ans



def solve_task5(number):  # easy problem
    global a
    ans = ''
    n = number
    size = 2**n
    a = [[0] * size for _ in range(size)]
    task5_recur(0, 0, n)
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            ans = ans + str(a[i][j]) + " "
        ans = ans + "\n"

    return ans



# def solve_task6(number):
#     ans = ''
    

def task4_recur(x: int):
    if x % 2 == 0:
        return task4_recur(x / 2)
    elif x != 1:
        return task4_recur(x - 1) + task4_recur(x + 1)
    return 1


a = []
c = 1
def task5_recur(px, py, n):
        global c
        if n == 0:
            a[px][py] = c
            c += 1
            return
        task5_recur(px, py, n-1)
        task5_recur(px, py + 2**(n-1), n-1)
        task5_recur(px + 2**(n-1), py, n-1)
        task5_recur(px + 2**(n-1), py + 2**(n-1), n-1)
        return
# def task4_recur(x: int):
