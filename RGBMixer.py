import numpy as np
import cv2 as ct
from tkinter import * # type: ignore
from tkinter.ttk import * # type: ignore
import tkinter.font as tkFont
from PIL import Image, ImageTk
import pyperclip

class app:
	def __init__(self):
		self.img = np.zeros((240,360,3), np.uint8)
		self.show_img = None
		self.height, self.width, self.cannel = self.img.shape
		self.red = 0
		self.green = 0
		self.blue = 0
		self.code = None

		self.root = Tk()
		self.canvas = Canvas(self.root, width=self.width, height=self.height)
		self.focused = None

		self.dfont = tkFont.nametofont("TkDefaultFont")
		self.family = self.dfont.actual("family")
		self.size = self.dfont.actual("size")

		self.root.title("RGBMixer")
		self.root.bind('<Key>', self.keypress)
		self.canvas.pack()

		self.show()

	def keypress(self, event):
		if event.keysym in {'Escape'}:
			if self.focused == None:
				self.root.quit()
			else:
				self.root.focus_set() # type: ignore
	
	def create_frame(self, obj, pd=8):
		return Frame(obj, padding=pd) # type: ignore
	
	def create_label(self, frm, txt):
		return Label(frm, text=txt, font=(self.family, int(self.size*1.3)))
	
	def create_entry(self, frm, show=None):
		def focus_in(event):
			self.focused = "entry"

		def focus_out(event):
			self.focused = None

		context = StringVar()
		obj = Entry(frm, textvariable=context, show=show) # type: ignore
		obj.bind("<FocusIn>", focus_in) # type: ignore
		obj.bind("<FocusOut>", focus_out) # type: ignore
		return obj, context
	
	def create_button(self, frm, txt, cmd):
		def focus_in(event):
			self.focused = "button"

		def focus_out(event):
			self.focused = None

		obj = Button(frm, text=txt, command=cmd) # type: ignore
		obj.bind("<FocusIn>", focus_in) # type: ignore
		obj.bind("<FocusOut>", focus_out) # type: ignore
		obj.bind("<Return>", lambda event: obj.invoke()) # type: ignore
		return obj

	def adapt(self):
		color_code = self.color_code.get() # type: ignore
		if len(color_code) not in {3,6}:
			pass

		number = len(color_code)

		red = color_code[number//3*1-1*number//3:number//3*1] # type: ignore
		green = color_code[number//3*2-1*number//3:number//3*2] # type: ignore
		blue = color_code[number//3*3-1*number//3:number//3*3] # type: ignore

		self.code = color_code

		try:
			red, green, blue = int(red, 16), int(green, 16), int(blue, 16)
		except ValueError:
			return

		self.img[0:self.height, 0:self.width] = [blue, green, red]
		self.currentLabel["text"] = f"R: {red}\t G: {green}\tB: {blue}"
		self.codeLabel["text"] = f"Code: {self.code}"

		self.show()

	def update(self):
		def checkVal(val):
			try: 
				val = int(val)
				return min(max(val, 0), 255)
			except ValueError:
				return 0

		red = checkVal(self.red.get()) # type: ignore
		green = checkVal(self.green.get()) # type: ignore
		blue = checkVal(self.blue.get()) # type: ignore  

		self.code = "".join([f'{red:x}'.zfill(2), f'{green:x}'.zfill(2), f'{blue:x}'.zfill(2)])

		self.img[0:self.height, 0:self.width] = [blue, green, red]
		self.currentLabel["text"] = f"R: {red}\t G: {green}\tB: {blue}"
		self.codeLabel["text"] = f"Code: {self.code}"

		self.show()

	def show(self):
		img = ct.cvtColor(self.img, ct.COLOR_BGR2RGB) # type: ignore
		pil_img = Image.fromarray(img)
		self.show_img = ImageTk.PhotoImage(pil_img)
		self.canvas.create_image(0, 0, image=self.show_img, anchor="nw")



	def exe(self):
		currentFrm = self.create_frame(self.root)

		redFrm = self.create_frame(self.root)
		greenFrm = self.create_frame(self.root)
		blueFrm = self.create_frame(self.root)

		codeFrm = self.create_frame(self.root, 28)


		self.code = "".join([f'{self.red:x}'.zfill(2), f'{self.green:x}'.zfill(2), f'{self.blue:x}'.zfill(2)])

		self.currentLabel = self.create_label(currentFrm, f"R: {self.red}\tG: {self.green}\tB: {self.blue}")
		self.codeLabel = self.create_label(currentFrm, f"Code: {self.code}")

		redLabel = self.create_label(redFrm, "R")
		greenLabel = self.create_label(greenFrm, "G")
		blueLabel = self.create_label(blueFrm, "B")

		codeLabel = self.create_label(codeFrm, "Code")


		redEntry, self.red = self.create_entry(redFrm)
		greenEntry, self.green = self.create_entry(greenFrm)
		blueEntry, self.blue = self.create_entry(blueFrm)

		codeEntry, self.color_code = self.create_entry(codeFrm)


		commit = self.create_button(self.root, "Change", self.update)
		clipboard = self.create_button(currentFrm, "Copy", lambda: pyperclip.copy(self.code))
		adapt = self.create_button(codeFrm, "Adapt", self.adapt)

		currentFrm.pack()
		self.currentLabel.pack(side=TOP)
		self.codeLabel.pack(side=TOP)
		clipboard.pack(side=TOP) # type: ignore

		redFrm.pack()
		redLabel.pack(side=LEFT)
		redEntry.pack(side=LEFT)

		greenFrm.pack()
		greenLabel.pack(side=LEFT)
		greenEntry.pack(side=LEFT)

		blueFrm.pack()
		blueLabel.pack(side=LEFT)
		blueEntry.pack(side=LEFT)

		commit.pack() # type: ignore

		codeFrm.pack()
		codeLabel.pack(side=LEFT)
		codeEntry.pack(side=LEFT)
		adapt.pack() # type: ignore

		self.root.mainloop()


def main():
	Application = app()
	Application.exe()

if __name__ == "__main__":
	main()