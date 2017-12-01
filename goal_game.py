from tkinter import *
import random

G = Tk()
G.title("Running Game")


canvas2 = Canvas(G,width=500, height=666, bg='burlywood1')
canvas2.pack()
canvas2.create_text(250, 150, text="Running Game",fill="gray17",font=("OCR A Std",30))

def play():
    canvas2.destroy()
    mygame()

play = Button(canvas2,width=10,height=2,text="Play Game",command = play,font=("OCR A Std",10))
play.place(x=210,y=333)

class mygame():
    def __init__(self):
        self.G=G
        self.canvas = Canvas(G,width=500, height=666, bg='springgreen4')
        self.canvas.pack()
        self.score = 0
        self.px = 250
        self.py = 620
        self.vx = 0
        self.vy = 0
        self.pgx1 = 210
        self.pgy1 = 0
        self.pgx2 = 310
        self.pgy2 = 15
        self.human()
        self.goal()
        self.cycle()
        self.draw()
        # self.entergoal_and_hitcycle()
        self.canvas.bind('<Key>',self.control)
        self.canvas.focus_set()

    def human(self):
        self.hm = self.canvas.create_oval(self.px , self.py, self.px+25,self.py+25,fill="palegreen",width =2)

    def control(self,event):
        # print("pressed",repr(event.char))
        if event.char=="D" or event.char=="d":
            self.vy = 0
            self.vx = 6
        elif event.char=="A" or event.char=="a":
            self.vy = 0
            self.vx = -6
        elif event.char=="W" or event.char=="w":
            self.vx = 0
            self.vy = -6
        elif event.char=="S" or event.char=="s":
            self.vx = 0
            self.vy = 6
        elif event.char=="Q" or event.char=="q":
            self.vx = -6
            self.vy = -6
        elif event.char=="E" or event.char=="e":
            self.vx = 6
            self.vy = -6

    def update_human(self):
        self.px = self.px + self.vx
        self.py = self.py + self.vy
        # print(self.px,self.py)

    def goal(self):
        self.goall = self.canvas.create_rectangle(self.pgx1, self.pgy1, self.pgx2, self.pgy2, width = 2, fill = "lightcyan4")

    def score1(self):
        self.s=self.canvas.create_text(250, 500, text=("Your Score : ",self.score),fill="gray17",font=("OCR A Std",15))

    def entergoal_and_hitcycle(self):
        if (self.pgx1 -20) <= self.px <= (self.pgx2+20) and self.pgy1 <= self.py <= self.pgy2 or \
        self.pc1x1-20<=self.px<=self.pc1x2 and self.pc1y1-20<=self.py<=self.pc1y2 or \
        self.pc4x1-20<=self.px<=self.pc4x2 and self.pc4y1-20<=self.py<=self.pc4y2 or \
        self.pc7x1-20<=self.px<=self.pc7x2 and self.pc7y1-20<=self.py<=self.pc7y2:
            # self.canvas.delete(self.hm,self.cycle1)
            self.canvas.delete(self.hm,self.cycle1,self.cycle2,self.cycle3,self.cycle4,self.cycle5,\
                self.cycle6,self.cycle7,self.cycle8,self.cycle9,self.cycle10,self.cycle11)
            self.cycle()
            self.px = 250
            self.py = 620
            self.vx = 0
            self.vy = 0
            self.score += 10
            self.human()

        elif self.pc2x1-20<=self.px<=self.pc2x2 and self.pc2y1-20<=self.py<=self.pc2y2 or \
            self.pc3x1-20<=self.px<=self.pc3x2 and self.pc3y1-20<=self.py<=self.pc3y2 or \
            self.pc5x1-20<=self.px<=self.pc5x2 and self.pc5y1-20<=self.py<=self.pc5y2 or \
            self.pc6x1-20<=self.px<=self.pc6x2 and self.pc6y1-20<=self.py<=self.pc6y2 or\
            self.pc8x1-20<=self.px<=self.pc8x2 and self.pc8y1-20<=self.py<=self.pc8y2 or \
            self.pc9x1-20<=self.px<=self.pc9x2 and self.pc9y1-20<=self.py<=self.pc9y2 or \
            self.pc10x1-20<=self.px<=self.pc10x2 and self.pc10y1-20<=self.py<=self.pc10y2 or \
            self.pc11x1-20<=self.px<=self.pc11x2 and self.pc11y1-20<=self.py<=self.pc11y2:
            self.canvas.delete(self.hm)
            self.canvas.create_text(250, 250, text="You Die",fill="gray17",font=("OCR A Std",30))
            self.score1()
            self.button()

    def button(self):
        self.newgames = Button(self.canvas,width=10,height=2,text="New Game",command = self.newgame,font=("OCR A Std",10))
        self.newgames.place(x=210,y=333)
        
    def newgame(self):
        self.canvas.destroy()
        mygame()


    def cycle(self):
        self.pc1x1 = random.randint(10,(460/10)*10)
        self.pc1y1 = 30
        self.pc1x2 = self.pc1x1 + 40
        self.pc1y2 = self.pc1y1 + 40
        self.cycle1 = self.canvas.create_rectangle(self.pc1x1,self.pc1y1,self.pc1x2,self.pc1y2,fill="cyan",width=2)

        self.pc2x1 = random.randint(10,(460/10)*10)
        self.pc2y1 = 100
        self.pc2x2 = self.pc2x1 + 40
        self.pc2y2 = self.pc2y1 + 40
        self.cycle2 = self.canvas.create_oval(self.pc2x1,self.pc2y1,self.pc2x2,self.pc2y2,fill="coral",width=2)

        self.pc3x1 = random.randint(10,(460/10)*10)
        self.pc3y1 = 170
        self.pc3x2 = self.pc3x1 + 40
        self.pc3y2 = self.pc3y1 + 40
        self.cycle3 = self.canvas.create_oval(self.pc3x1,self.pc3y1,self.pc3x2,self.pc3y2,fill="coral",width=2)

        self.pc4x1 = random.randint(10,(460/10)*10)
        self.pc4y1 = 240
        self.pc4x2 = self.pc4x1 + 40
        self.pc4y2 = self.pc4y1 + 40
        self.cycle4 = self.canvas.create_rectangle(self.pc4x1,self.pc4y1,self.pc4x2,self.pc4y2,fill="cyan",width=2)

        self.pc7x1 = random.randint(10,(460/10)*10)
        self.pc7y1 = 310
        self.pc7x2 = self.pc7x1 + 40
        self.pc7y2 = self.pc7y1 + 40
        self.cycle7 = self.canvas.create_rectangle(self.pc7x1,self.pc7y1,self.pc7x2,self.pc7y2,fill="cyan",width=2)

        self.pc6x1 = random.randint(10,(460/10)*10)
        self.pc6y1 = 480
        self.pc6x2 = self.pc6x1 + 40
        self.pc6y2 = self.pc6y1 + 40
        self.cycle6 = self.canvas.create_oval(self.pc6x1,self.pc6y1,self.pc6x2,self.pc6y2,fill="coral",width=2)

        self.pc5x1 = random.randint(10,(460/10)*10)
        self.pc5y1 = 550
        self.pc5x2 = self.pc5x1 + 40
        self.pc5y2 = self.pc5y1 + 40
        self.cycle5 = self.canvas.create_oval(self.pc5x1,self.pc5y1,self.pc5x2,self.pc5y2,fill="coral",width=2)

        self.pc8x1 = random.randint(10,(460/10)*10)
        self.pc8y1 = 500
        self.pc8x2 = self.pc8x1 + 40
        self.pc8y2 = self.pc8y1 + 40
        self.cycle8 = self.canvas.create_oval(self.pc8x1,self.pc8y1,self.pc8x2,self.pc8y2,fill="coral",width=2)

        self.pc9x1 = random.randint(10,(460/10)*10)
        self.pc9y1 = 350
        self.pc9x2 = self.pc9x1 + 40
        self.pc9y2 = self.pc9y1 + 40
        self.cycle9 = self.canvas.create_oval(self.pc9x1,self.pc9y1,self.pc9x2,self.pc9y2,fill="coral",width=2)

        self.pc10x1 = random.randint(10,(460/10)*10)
        self.pc10y1 = 200
        self.pc10x2 = self.pc10x1 + 40
        self.pc10y2 = self.pc10y1 + 40
        self.cycle10 = self.canvas.create_oval(self.pc10x1,self.pc10y1,self.pc10x2,self.pc10y2,fill="coral",width=2)

        self.pc11x1 = random.randint(10,(460/10)*10)
        self.pc11y1 = 70
        self.pc11x2 = self.pc11x1 + 40
        self.pc11y2 = self.pc11y1 + 40
        self.cycle11 = self.canvas.create_oval(self.pc11x1,self.pc11y1,self.pc11x2,self.pc11y2,fill="coral",width=2)



    def draw(self):
        if self.px + self.vx <= 0 or \
          self.px >= 475:
           self.vx = -self.vx
        if self.py + self.vy <= 0 or \
          self.py >= 666 - 25:
          self.vy = -self.vy
        self.canvas.move(self.hm,self.vx,self.vy)
        self.update_human()
        self.entergoal_and_hitcycle()
        self.canvas.after(1000//60,self.draw)

G.mainloop()

