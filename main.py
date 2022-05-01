# ask for admin
from sys import executable as exe, argv, exit as die
from ctypes import windll

REQUIRES_ADMIN = False # if planning to make a shortcut in the start menu folder, then disabling this won't make that happen

def IsAdmin() -> bool:
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False

if REQUIRES_ADMIN and not IsAdmin():
    adminErrorMsg = """Program needs admin rights to copy files to the start menu folder.
If that's not what you want to do, and really need this script, change the REQUIRES_ADMIN constant to False."""

    windll.shell32.ShellExecuteW(None, 'runas', exe, ' '.join(argv), None, None)
    if not IsAdmin():
        print(adminErrorMsg)
        die()

from os import system as cmd, path, getcwd as cwd
from win32com.client import Dispatch
shell = Dispatch("WScript.Shell") # kind of like an import

DEBUG = False

def GetFullPathFromAbbreviatedPath(path:str) -> str:
    if path[0] == ".":
        path = path.replace(".",cwd(),1)
    
    return path

def FakeBreakpoint(msg:str):
    if DEBUG:
        resp = input(msg+"\ncontinue program? y/n: ")
        if resp == "n":
            die()

def CreateShortcut(file:str,output:str,desc:str="A file/app.",args:str=""):
    file = f'"{GetFullPathFromAbbreviatedPath(file)}"'

    FakeBreakpoint(f"file: {file}; output: {output}")

    link = shell.CreateShortCut(output)
    link.TargetPath = file
    link.WorkingDirectory = path.dirname(output)
    link.Arguments = args
    link.save()

    FakeBreakpoint(f"link: {link}")

    return link

print(argv)
CreateShortcut(
    argv[1],
    argv[2],
    argv[3],
    argv[4]
)