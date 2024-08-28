from tkinter import * # type: ignore
from tkinter.ttk import * # type: ignore
from PIL import Image, ImageTk

class app:
    def __init__(self):
        # x, y の値の定義
        self.width = 800
        self.height = 450
        
        # クリック位置
        self.clickX, self.clickY = None, None
        
        # 画像関連
        

        # キャンバス関連
        self.root = None
        self.canvas = None
        self.createCanvas()
        
    def click(self, event):
        self.clickX = event.x
        self.clickY = event.y
        print(self.clickX, self.clickY)
        
    def keyPress(self, event):
        key = event.keysym
        if key in {'q', 'Escape'}:
            self.root.quit() # type: ignore
        
    def createCanvas(self):
        self.root = Tk()
        self.root.title("Canvas")
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.bind('<Key>', self.keyPress)
        
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.create_rectangle(0, 0, self.width, self.height, fill="#000")
        self.canvas.place(x=0, y=0)
        
    def exe(self):
        self.root.mainloop() # type: ignore


def main():
    Application = app()
    Application.exe()

if __name__ == "__main__":
    main()