# verify admin perms
from sys import exit as abort, argv
from program import ProgramPrint

RUN = __name__ == "__main__"

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
    
# ACTUAL PROGRAM THINGS
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
            abort()

def CreateShortcut(file:str,output:str,arguments:str=""):
    file = f'"{GetFullPathFromAbbreviatedPath(file)}"'

    FakeBreakpoint(f"file: {file}; output: {output}")

    try:
        link = shell.CreateShortCut(output)
        link.TargetPath = file
        link.WorkingDirectory = path.dirname(output)
        link.Arguments = arguments
        link.save()
    except Exception as err:
        PrintWithColour(bcolors["FAIL"],f"ERROR: {err.args[2][2]}")
        abort()

    FakeBreakpoint(f"link: {link}")

    return link

def main(args:list[str]=argv):
    if len(args) < 3:
        PrintWithColour(bcolors["FAIL"],"ERROR: Insufficient arguments")
        abort()

    lnkArgs = ""
    try:
        lnkArgs = args[3]
    except IndexError:
        PrintWithColour(bcolors["WARNING"],"WARNING: Shortcut args unspecified.")

    CreateShortcut(
        args[1],
        args[2],
        lnkArgs
    )

if RUN: main(argv)