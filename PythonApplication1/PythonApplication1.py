from tkinter import *
from random import randint

class Game:
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.snake_coords = [[28, 28]]
        self.dot_coords = [randint(0, 63) for i in range(2)]
        self.vector = {"Up":(0,-1), "Down":(0, 1), "Left": (-1,0), "Right": (1, 0)}
        self.direction = self.vector["Right"]
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.set_direction)
        self.GAME()
    def set_dot(self):
        self.dot_coords = [randint(0, 63) for i in range(2)]
        if self.dot_coords in self.snake_coords:
            self.set_dot()
    def set_direction(self, event):
        if event.keysym in self.vector:
            self.direction = self.vector[event.keysym]
    def draw(self):
        self.canvas.delete(ALL)
        x_dot, y_dot = self.dot_coords
        self.canvas.create_rectangle(x_dot*10, y_dot*10, (x_dot+1)*10, (y_dot+1)*10, fill="green", width=1)
        for x, y in self.snake_coords:
            self.canvas.create_rectangle(x*10, y*10, (x+1)*10, (y+1)*10, fill="black", width=0)
    @staticmethod
    def coord_check(coord):
        return 0 if coord > 63 else 63 if coord < 0 else coord
    def GAME(self):
        self.draw()
        x,y = self.snake_coords[0]
        x += self.direction[0]; y += self.direction[1]
        x = self.coord_check(x)
        y = self.coord_check(y)
        if x == self.dot_coords[0] and y == self.dot_coords[1]:
            self.set_dot()
        elif [x, y] in self.snake_coords:
            self.snake_coords = []
        else:
            self.snake_coords.pop()
        self.snake_coords.insert(0, [x,y])
        self.canvas.after(100, self.GAME)
        
        
root = Tk()
canvas = Canvas(root, width=640, height=640, bg="white")
canvas.pack()
game = Game(canvas)
root.mainloop()