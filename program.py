from sys import argv, exit as abort, executable as exe
from ctypes import windll

REQUIRES_ADMIN = True # if planning to make a shortcut in the start menu folder, then disabling this won't make that happen

def ProgramPrint(content):
    print(content)

def IsAdmin() -> bool:
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False

if __name__ == "__main__":
    # ask for admin
    from main import main
    
    print("SMSC - Start Menu Shortcut Creator")
    print("usage: smsc file output [arguments]")

    if IsAdmin():
        main(argv)
    elif REQUIRES_ADMIN:
        windll.shell32.ShellExecuteW(None, 'runas', exe, ' '.join(argv), None, None)
    else:
        main(argv)