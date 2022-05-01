# ask for admin
from sys import executable as exe, argv
from ctypes import windll
windll.shell32.ShellExecuteW(None, 'runas', exe, ' '.join(argv), None, None)

from os import system as cmd
from winshell import shortcut as mklink,Shortcut

def CreateShortcut(file:str,output:str,desc:str="A file/app.",args:str="") -> Shortcut:
    with mklink(output) as link:
        link.path = file
        link.description = desc
        link.arguments = args
        return link