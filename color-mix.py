import numpy as np
import cv2 as ct
import tkinter as tk
import PIL as pl

class app:
	def __init__(self):
		self.img = np.zeros((720,720,3), np.uint8)
		self.key = None
		self.height, self.width, self.cannel = self.img.shape

	def show(self):
		ct.imshow("Canvas", self.img)
		
	def keypress(self):
		self.key = ct.waitKey(0)
		if self.key in {ord('q'), 27}:
			ct.destroyAllWindows()
			return True
		elif self.key in {ord('r'), ord('g'), ord('b')}:
			self.change()
		
	def change(self):
		self.img[self.height//4:(self.height//4)*3, self.width//4:(self.width//4)*3] = [150 if self.key != ord('b') else 255, 150 if self.key != ord('g') else 255, 150 if self.key != ord('r') else 255]

	def exe(self):
		while True:
			if self.keypress() == True: break
			self.show()

def main():
	Application = app()
	Application.exe()

if __name__ == "__main__":
	main()