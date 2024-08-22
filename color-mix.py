import numpy as np
import cv2 as ct
import tkinter as tk
from PIL import Image, ImageTk

class app:
	def __init__(self):
		self.bgr = np.zeros((180,360,3), np.uint8)
		self.rgb = np.array([0])
		self.height, self.width, self.cannel = self.bgr.shape

		self.root = tk.Tk()
		self.canvas = tk.Canvas(self.root, width=self.width, height=self.height)

		self.root.title("Canvas")
		self.root.bind('<Key>', self.keypress)
		self.canvas.pack()

		self.update()

	def keypress(self, event):
		key = event.char
		if key in {'q', chr(27)}:
			ct.destroyAllWindows()
			self.root.quit()
			return True
		elif key in {'r', 'g', 'b'}:
			self.change(key)
			self.update()
		
	def change(self, key):
		self.bgr[0:self.height, 0:self.width] = [150 if key != 'b' else 255, 150 if key != 'g' else 255, 150 if key != 'r' else 255]

	def update(self):
		self.rgb = ct.cvtColor(self.bgr, ct.COLOR_BGR2RGB)
		img_pil = Image.fromarray(self.rgb)
		self.img_tk = ImageTk.PhotoImage(img_pil)
		self.canvas.create_image(0, 0, image=self.img_tk, anchor="nw")

	def exe(self):

		self.root.mainloop()


def main():
	Application = app()
	Application.exe()

if __name__ == "__main__":
	main()