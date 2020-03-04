class Player(object):
    def __init__(self, player = "Player"):
        self.player = player
        self.number = None
        self.ready = False
        self.guess = None
        self.ball = 0 
        self.strike = 0
        self.turn = False
        self.win = False
        
    def check_ans(self, ans):
        self.strike = 0
        self.ball = 0
        for i in range(len(ans)):
            if self.guess[i] == ans[i]:
                self.strike += 1
            elif self.guess[i] in ans and self.guess[i] != ans[i]:
                self.ball += 1
        
        return [self.strike, self.ball]
    
    def update_name(self):
        if self.ready == True:
            self.player = self.player + " Ready!"
    
    def check_win(self):
        if self.strike == 4:
            self.win = True

    #number has to be a list + make sure you check for non-digits
    @staticmethod
    def check_number(number):
        if len(number) != 4:
            return False, 1
        
        for i in range(len(number)):
            for j in range(i+1,len(number)):
                if number[i] == number[j]:
                    return False, 2

        return True, 0 





    


