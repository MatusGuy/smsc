# ask for admin
from sys import executable as exe, argv, exit as abort
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
        abort()

from os import system as cmd, path, getcwd as cwd
from win32com.client import Dispatch
shell = Dispatch("WScript.Shell") # kind of like an import

DEBUG = False

bcolors = {
    "HEADER": '\033[95m',
    "OKBLUE": '\033[94m',
    "OKCYAN": '\033[96m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m'
}

def PrintWithColour(color:str,msg:str):
    print(color+msg+bcolors["ENDC"])

def GetFullPathFromAbbreviatedPath(path:str) -> str:
    if path[0] == ".":
        path = path.replace(".",cwd(),1)
    
    return path

def FakeBreakpoint(msg:str):
    if DEBUG:
        resp = input(msg+"\ncontinue program? y/n: ")
        if resp == "n":
            abort()

def CreateShortcut(file:str,output:str,args:str=""):
    file = f'"{GetFullPathFromAbbreviatedPath(file)}"'

    FakeBreakpoint(f"file: {file}; output: {output}")

    try:
        link = shell.CreateShortCut(output)
        link.TargetPath = file
        link.WorkingDirectory = path.dirname(output)
        link.Arguments = args
        link.save()
    except Exception as err:
        PrintWithColour(bcolors["FAIL"],f"ERROR: {err.args[2][2]}")
        abort()

    FakeBreakpoint(f"link: {link}")

    return link

argv = [" "," "," "]

if len(argv) < 3:
    PrintWithColour(bcolors["FAIL"],"ERROR: Insufficient arguments")
    abort()

lnkArgs = ""
try:
    lnkArgs = argv[3]
except IndexError:
    PrintWithColour(bcolors["WARNING"],"WARNING: Shortcut args unspecified.")

CreateShortcut(
    argv[1],
    argv[2],
    lnkArgs
)