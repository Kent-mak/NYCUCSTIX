class Tasks:
    def __init__(self):
        # init
        self.StoreApple = []
        self.StoreStar = []
        self.StoreAdvanceStar = []
        self.StoreFIB = [0 for i in range(210)]
        
    def apple(self):
        for number in range(30, 101):
            apple_num = 500 % number   # these apple to sell
            money = 0
            discount = 1
            while(apple_num > 0):
                if apple_num >= 10:
                    money = money + 10 * 30 * discount
                    apple_num -= 10
                else:
                    money = money + apple_num * 30 * discount
                    apple_num = 10
                discount -= 0.05
                
            self.StoreApple.append(money)

    def star(self):
        ans = ''
        for i in range(1, 101):
            for _ in range(i + 1):
                ans = ans + '*'
            self.StoreStar.append(ans)
            ans = ans + "\n"

    def star_advance(self):
        for number in range(1, 51):
            ans = ''
            for i in range(number):
                for _ in range(number - i - 1):
                    ans += ' '
                for _ in range((i + 1)*2 - 1):
                    ans += '*'
                if i != number - 1:
                    ans = ans + "\n"
            self.StoreAdvanceStar.append(ans)
        
    def FIB(self):
        # print(len(self.StoreFIB))
        self.StoreFIB[1] = 1
        self.StoreFIB[2] = 1
        for i in range(3, 200 + 1):
            self.StoreFIB[i] = self.StoreFIB[i-1] + self.StoreFIB[i-2]

    def get_apple(self, number):
        return self.StoreApple[number]
    
    def get_star(self, number):
        return self.StoreStar[number]
    
    def get_advance_star(self, number):
        return self.StoreAdvanceStar[number]
    
    def get_FIB(self, number):
        return self.StoreFIB[number]                         
    
        


# if __name__ == '__main__':
store = Tasks()
store.apple()
store.star()
store.star_advance()
store.FIB()
# print(store.StoreStar)
# print(store.StoreFIB)
# print(store.StoreAdvanceStar)
# print(store.StoreApple)