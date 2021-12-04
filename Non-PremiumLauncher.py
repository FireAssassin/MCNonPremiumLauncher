from os import kill, path, system
import tkinter
import minecraft_launcher_lib
import subprocess
from tkinter import *
from tkinter import ttk, messagebox
import hashlib # for nonpremuim uuid making
from colorama import init, Fore #for coloured text within the console
from pypresence import Presence
import random
import json
import filecmp
from ttkthemes.themed_tk import ThemedTk

Radek = """
   ___
 /     \                        |                |   /
 |     |                        |                |  /
 |_____/    ______       ______ |     _____      | /
 |   \     /      \|    /      \|    /     \     |/
 |    \   |        |   |        |   |______/     | \ 
 |     \  |        |   |        |   |            |  \ 
 |      \  \______/\_   \______/\_   \_______/   |   \ 
"""

init() #initialises colorama
print(random.choice([Fore.YELLOW, Fore.MAGENTA, Fore.BLUE, Fore.CYAN, Fore.GREEN]) + Radek + Fore.RESET)
print(minecraft_launcher_lib.utils.get_minecraft_directory())
print(Fore.BLUE + "Sprawdzanie zawartości" + Fore.RESET)
def spr():
    file1 = "C:/Users/radek/AppData/Roaming/.minecraft/versions/OptiFine-1.18/OptiFine 1.18.jar"
    file2 = "OptiFine-1.18/OptiFine 1.18.jar"
    comp = filecmp.cmp(file1, file2, shallow=True)
    if comp is False:
        tkinter.messagebox.showerror(title="Błąd", message="""Masz nie zainstalowaną lub zmienioną wersje Minecraft'a
instrukcja do zainstalowania na """)
        print(Fore.RED + "[Błąd] " + Fore.MAGENTA + "Masz nie zainstalowaną lub zmienioną wersje Minecraft'a")
        print()
        exit()
    else:
        print("być wszytko git")
spr()





def play():
    latest_version = "1.17.1"
    minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()
    options = {
        "username": Username_Entry.get(),
        "uuid": str(hashlib.md5(str.encode(Username_Entry.get())).digest()),
        "token": "",
        "jvmArguments": [f"-Xmx{ram.get()['JVMRAM']}G"]
    }
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(latest_version, minecraft_directory, options)
    subprocess.call(minecraft_command)

class Config:
    Config = {}
    MinecraftDir = ""
    BG_Colour = '#2F3136'
    FG_Colour = "#2c3e50"
    Theme = "equilux"
    #Discord Rich Presence Settings
    RPCEnable = False
    ClientId = "673338815301287966"
    LargeImage = "pymymc_logo"
    ConfigImage = "config"
    RootImage = "main"
    VanillaImage = "vanilla"
    ModdedImage = "modded"

    Proxy = "" 
class A:
    #Colorama Aliases
    red = Fore.RED
    blue = Fore.BLUE
    black = Fore.BLACK
    res = Fore.RESET
    yellow = Fore.YELLOW
    green = Fore.GREEN
    magenta = Fore.MAGENTA

    class JsonFile:
        @classmethod
        def SaveDict(self, Dict, File):
            """Saves a dict as a file"""
            with open(File, 'w') as json_file:
                json.dump(Dict, json_file, indent=4)

        @classmethod
        def GetDict(self, file):
            """Returns a dict from file name"""
            if not path.exists(file):
                return {}
            else:
                with open(file) as f:
                    data = json.load(f)
                return data
class Path:
    Logo_Small = "img\\pymymc_logo_small.png"
    Logo_Icon = "img\\pymymc_ico.ico"

def DefaultPresence():
    """Sets the default presence"""
    if Config.RPCEnable:
        RPC.update(state="In the main menu.", large_image=Config.LargeImage, small_image=Config.RootImage)

def ExitHandler():
    """Function ran on the closing of the tk mainwindow"""
    MainWindow.destroy()
    exit()

if Config.RPCEnable:
    RPC = Presence(Config.ClientId)
    RPC.connect()
    DefaultPresence()
MainWindow = ThemedTk(theme=Config.Theme)
#Styles
s = ttk.Style()
s.configure('TButton', background=Config.FG_Colour, fieldbackground=Config.FG_Colour)
s.configure('TCheckbutton', background=Config.BG_Colour, foreground="white")
s.configure('TEntry', fieldbackground=Config.FG_Colour, background=Config.FG_Colour)
MainWindow.configure(background=Config.BG_Colour) # sets bg colour
MainWindow.title("PyMyMC") # sets window title
if system == "Windows":
    #other systems dont use ico
    MainWindow.iconbitmap(Path.Logo_Icon) # sets window icon
MainWindow.resizable(False, False) #makes the window not resizable
MainWindow.protocol("WM_DELETE_WINDOW", ExitHandler) #runs the function when the user presses the X button

    #Logo Image
PyMyMC_Logo = PhotoImage(file=Path.Logo_Small)
PyMyMC_Logo_Label = Label(MainWindow, image=PyMyMC_Logo)
PyMyMC_Logo_Label['bg'] = PyMyMC_Logo_Label.master['bg']
PyMyMC_Logo_Label.grid(row=0, column=0) 

#Username Label
Username_Label = Label(MainWindow, text="Email:", bg = Config.BG_Colour, fg = "white", font = "none 12")
Username_Label.grid(row=5, column=0, sticky=W)

#Username Entry
US_EntryText = StringVar() #
Username_Entry = ttk.Entry(MainWindow, width=20, textvariable=US_EntryText)
Username_Entry.grid(row=6, column = 0, sticky=W)

#Password Entry
ram = ttk.Entry(MainWindow, width=20)
ram.grid(row=8, column = 0, sticky=W)

#Play Button
Play_Button = ttk.Button(MainWindow, text="Play!", width=20, command = play)
Play_Button.grid(row = 11, column=0, sticky = W)

#Version Label
Version_Label = Label(MainWindow, text="Version: 1.18", bg = Config.BG_Colour, fg = "white", font = "none 12")
Version_Label.grid(row=9, column=0, sticky=W)

#Im just trying to get something working
Empty = []

MainWindow.mainloop()