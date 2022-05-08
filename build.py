from os import system as cmd

MAIN = "main.py"
OUTPUT = "smsc.exe"

ICON = "smsc.ico"
VERSION = "0.1.0.0"
COMPANY = "© MatusGuy 2022-2023"
PRODUCT = "Desktop application"
PRODUCT_VER = "1.0.0.0"
DESC = "SMSC - Start Menu Shortcut Creator"

DISABLE_CMD_WINDOW = False
FORCE_STDOUT_SPEC = False

MANIFEST = ""

UAC = False

DEL_CMD = True # delete the .cmd file created after compilation

command = "nuitka --follow-imports "

def add2command(txt:str):
    global command
    command += txt+" "

if OUTPUT: add2command(f'-o "{OUTPUT}"')
if ICON: add2command(f'--windows-icon-from-ico="{ICON}"')
if VERSION: add2command(f'--windows-file-version="{VERSION}"')
if COMPANY: add2command(f'--windows-company-name="{COMPANY}"')
if PRODUCT: add2command(f'--windows-product-name="{PRODUCT}"')
if PRODUCT_VER: add2command(f'--windows-product-version="{PRODUCT_VER}"')
#if MANIFEST: add2command(f"--") (idk how to include manifest file yet, what even is manifest)
if UAC: add2command("--windows-uac-admin")
if DISABLE_CMD_WINDOW: add2command("--windows-disable-console")
if FORCE_STDOUT_SPEC: add2command("--windows-force-stdout-spec=%PROGRAM%.out.txt")

add2command(MAIN)

print("Sending command: "+command)
result = cmd(command)

print("Compilation protocol complete, gave errorcode "+str(result))

if DEL_CMD:
    name = MAIN.split(".")[0]
    print(f"Deleting {name}.cmd")
    cmd(f"del {name}.cmd")