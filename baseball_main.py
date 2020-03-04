from tkinter import *
from tkinter import messagebox
from player import Player
import time

class Game_UI():
    def __init__(self):
        self.root = Tk()
        self.root.title("Baseball Number Game")
        self.root.geometry("550x600+500+300")
        self.title_label = Label(self.root, text = "Baseball Number Game!")
        
        self.p1_frame = LabelFrame(self.root, text = Player1.player, padx = 20, pady = 10)
        self.p1_guessnumber = Label(self.p1_frame, text = "****")
        self.p1_seperator = Label(self.p1_frame, text = " : ")
        self.p1_result = Label(self.p1_frame, text = "- ball - strike")
        self.p1_row = 0

        self.p2_frame = LabelFrame(self.root, text = Player2.player, padx = 20, pady = 10)
        self.p2_guessnumber = Label(self.p2_frame, text = "****")
        self.p2_seperator = Label(self.p2_frame, text = " : ")
        self.p2_result = Label(self.p2_frame, text = "- ball - stike")
        self.p2_row = 0 

        self.entry_instr = Label(self.root, text = "Player 1 Enter Number:")
        self.e1 = Entry(self.root, width = 10)
        self.submit_button = Button(self.root, text = "Submit", command = self.submit_click)
        self.exit_button = Button(self.root, text = "Quit", command = self.root.quit)
    
    def grid_widget(self):
        self.title_label.grid(row = 0, column = 1, padx = 0, pady = 20, columnspan = 2)
        
        self.p1_frame.grid(row = 1, column = 0, columnspan = 2, padx = 50)
        self.p1_guessnumber.grid(row = self.p1_row, column = 0)
        self.p1_seperator.grid(row = self.p1_row, column = 1)
        self.p1_result.grid(row = self.p1_row, column = 2)
        
        self.p2_frame.grid(row = 1, column = 2, columnspan = 2)
        self.p2_guessnumber.grid(row = self.p2_row, column = 0)
        self.p2_seperator.grid(row = self.p2_row, column = 1)
        self.p2_result.grid(row = self.p2_row, column = 2)
        
        self.entry_instr.grid(row = 2, column = 0, columnspan = 2, pady = 20, sticky = "E")
        self.e1.grid(row = 2, column = 2, pady = 20, columnspan = 2, sticky = "W")
        self.submit_button.grid(row = 3, column = 1)
        self.exit_button.grid(row = 3, column = 2)
    
    def update_widgets(self):
        self.p1_frame = LabelFrame(self.root, text = Player1.player, padx = 20, pady = 10)
        self.p1_guessnumber = Label(self.p1_frame, text = "****")
        self.p1_seperator = Label(self.p1_frame, text = " : ")
        self.p1_result = Label(self.p1_frame, text = "- strike - ball")

        self.p2_frame = LabelFrame(self.root, text = Player2.player, padx = 20, pady = 10)
        self.p2_guessnumber = Label(self.p2_frame, text = "****")
        self.p2_seperator = Label(self.p2_frame, text = " : ")
        self.p2_result = Label(self.p2_frame, text = "- strike - ball")

        self.e1 = Entry(self.root, width = 10)
        self.submit_button = Button(self.root, text = "Submit", command = self.submit_click)
        self.exit_button = Button(self.root, text = "Quit", command = self.root.quit)

        self.grid_widget()

    def submit_click(self):

        if Player1.turn == True:
            player = Player1
            #theres a delay with tkinter when calling widget update
            player_str = "Player 2"
            ans = Player2.number
            p_frame = self.p1_frame
            self.p1_row += 1
            p_row = self.p1_row
            
            Player1.turn = False
            Player2.turn = True
           
        else:
            player = Player2
            #theres a delay with tkinter when calling widget update
            player_str = "Player 1"
            ans = Player1.number
            p_frame = self.p2_frame
            self.p2_row += 1
            p_row = self.p2_row

            Player2.turn = False
            Player1.turn = True

        number = self.e1.get()

        #check if number is valid
        guess_valid, error_type = player.check_number(number)

        if guess_valid:
            player.guess = number
            self.e1.delete(0, 'end')
            res = []
            res = player.check_ans(ans)
            player.strike = res[0]
            player.ball = res[1]
            player.check_win()

            #terminate if victory
            if player.win:
                if player == Player1:
                    player_str = "Player 1"
                else:
                    player_str = "Player 2"
                response = messagebox.showinfo("Victory", player_str + " wins")
                time.sleep(1)
                self.root.destroy()

            self.entry_instr = Label(self.root, text = player_str + " Enter Number:")
            new_number = Label(p_frame, text = number)
            p_seperator = Label(p_frame, text = " : ")
            p_result = Label(p_frame, text = str(player.strike) + " strike, " + str(player.ball) + " ball")

            self.entry_instr.grid(row = 2, column = 0, columnspan = 2, pady = 20, sticky = "E")
            new_number.grid(row = p_row, column = 0)
            p_seperator.grid(row = p_row, column = 1)
            p_result.grid(row = p_row, column = 2)

        else:
            self.e1.delete(0, 'end')

            if Player1.turn == False:
                Player1.turn = True
                Player2.turn = False
            
            elif Player2.turn == False:
                Player2.turn = True
                Player1.turn = False

            if error_type == 1:
                response = messagebox.showerror("Error", "Enter 4 numbers...")
                
            elif error_type == 2:
                response = messagebox.showerror("Error", "Enter non-repeating numbers...")


    def set_numbers(self):
        global p1_e
        global p2_e
        global p1_input
        global p2_input
        x = self.root.winfo_x()
        y = self.root.winfo_y()

        p1_input = Toplevel()
        p1_input.geometry("+%d+%d" % (x + 500, y + 150))
        p1_input.title("Player 1 Number")
        p1_e = Entry(p1_input, width = 10, show = "*")
        p1_submit = Button(p1_input, text = "Enter", command = lambda: self.input_click("p1"))
        p1_e.grid(row = 0, column = 0, padx = 20, pady = 30, sticky = "E")
        p1_submit.grid(row = 0, column = 1, padx = 10, sticky = "W")

        p2_input = Toplevel()
        p2_input.geometry("+%d+%d" % (x + 850, y + 150))
        p2_input.title("Player 2 Number")
        p2_e = Entry(p2_input, width = 10, show = "*")
        p2_submit = Button(p2_input, text = "Enter", command = lambda: self.input_click("p2"))
        p2_e.grid(row = 0, column = 0, padx = 20, pady = 30, sticky = "E")
        p2_submit.grid(row = 0, column = 1, padx = 10, sticky = "W")
    
    #made for set_numbers functions
    def input_click(self, player):
        global p1_e
        global p2_e
        global p1_input
        global p2_input

        if player == "p1":
            p1_number = list(p1_e.get())
            p1_e.delete(0, 'end')
            number_check, error_type = Player.check_number(p1_number)

            if error_type == 1:
                response = messagebox.showerror("Error", "Enter 4 numbers...")
            elif error_type == 2:
                response = messagebox.showerror("Error", "Enter non-repeating numbers...")

            if number_check:
                Player1.number = p1_number
                Player1.ready = True
                p1_input.destroy()
                Player1.update_name()
                self.update_widgets()
       
        if player == "p2":
            p2_number = list(p2_e.get())
            p2_e.delete(0, 'end')
            number_check, error_type = Player.check_number(p2_number)

            if error_type == 1:
                response = messagebox.showerror("Error", "Enter 4 numbers...")
            elif error_type == 2:
                response = messagebox.showerror("Error", "Enter non-repeating numbers...")

            if number_check:
                Player2.number = p2_number
                Player2.ready = True
                p2_input.destroy()
                Player2.update_name()
                self.update_widgets()
        
            

#main function
def run_app():
    Game_ui.grid_widget()
    Game_ui.set_numbers()    
    Game_ui.root.mainloop()


if __name__ == '__main__':
    Player1 = Player("Player 1")
    Player1.turn = True
    Player2 = Player("Player 2")
    Game_ui = Game_UI()
    run_app()
