# ask for admin
from sys import executable as exe, argv
from ctypes import windll
#windll.shell32.ShellExecuteW(None, 'runas', exe, ' '.join(argv), None, None)

from os import system as cmd, path, getcwd as cwd
from win32com.client import Dispatch
shell = Dispatch("WScript.Shell") # kind of like an import

def GetFullPathFromAbbreviatedPath(path:str) -> str:
    if path[0] == ".":
        newpath = path.replace(".",cwd(),1)
    
    return newpath

def CreateShortcut(file:str,output:str,desc:str="A file/app.",args:str=""):
    link = shell.CreateShortCut(output)
    link.Targetpath = file
    link.WorkingDirectory = path.dirname(output)
    link.Arguments = args
    return link

print(argv)
CreateShortcut(
    argv[1],
    argv[2],
    argv[3],
    argv[4]
)