from tkinter import *
import os
import MenuFunctions as MeF
import ctypes
import time
import MainFunctions as MF
beginTime = time.time()
print("initialize window...", end="")
MainWindow = Tk()
MainWindow.title("HackZero")
width = MainWindow.winfo_screenwidth()
height = MainWindow.winfo_screenheight()
MainWindow.geometry("%dx%d" % (width, height))
MainWindow.configure(bg="black")
MainWindow.iconbitmap('favicon.ico')
print("done in " + str(time.time() - beginTime) + " seconds")
beginTime = time.time()
# Handle the menubar
print("initialize menubar...", end="")
menubar = Menu(MainWindow, background="#000000", foreground="#ffffff", activebackground="#000000", activeforeground="#ffffff")
MainWindow.config(menu=menubar)
settings_menu = Menu(menubar, tearoff=0)
settings_menu.add_command(label="Settings", command=None)
settings_menu.add_command(label="", command=None)
program_menu = Menu(menubar,tearoff=0)
program_menu.add_command(label="Doesn't Require Admin Permissions")
program_menu.add_command(label="Script to App", command=lambda:MeF.Script2App())
program_menu.add_command(label="IP Locator", command=lambda:MeF.IPLocator())
program_menu.add_command(label="EditZero", command=lambda:MF.EditZeroService())
program_menu.add_command(label="Server/IP Status Checker", command=lambda:MeF.ServerIPStatusCheck())
program_menu.add_command(label="Enable Offline Mode", command=lambda:MF.EnableOfflineMode())
program_menu.add_command(label="Incognito Browser", command=lambda:MF.BrowseZeroService())
program_menu.add_command(label="Quick Tools", command=lambda:MeF.QuickTools())
program_menu.add_command(label="Anonymous E-Mail", command=lambda:MeF.AnonymousEmail())
program_menu.add_command(label="CloudZero", command=lambda:MF.CloudZeroService())
program_menu.add_command(label="Computer Analyzation", command=lambda:MeF.CMPTRAnalyze())
program_menu.add_command(label="sethc.exe Activate Hack", command=lambda:MeF.SethcHack())
program_menu.add_command(label="OS Downloader", command=lambda:MeF.OSDownload())
program_menu.add_command(label="Create Bootable Media", command=lambda:MeF.BootableMediaCreate())
program_menu.add_command(label="Compare File Properties", command=lambda:MeF.CompareFilePrpts())
program_menu.add_separator()
program_menu.add_command(label='Exit', command=lambda:exit())
menubar.add_cascade(label="Programs", menu=program_menu)
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')
menubar.add_cascade(label="Help",menu=help_menu)
print("done in " + str(time.time() - beginTime) + " seconds")
beginTime = time.time()
print("initialize context menu...", end="")
context_menu = Menu(MainWindow, tearoff=0)
context_menu.add_command(label="Settings...", command=None)
context_menu.add_command(label="About...", command=None)
context_menu.add_separator()
context_menu.add_command(label="Exit", command=MainWindow.destroy)
def ACM(event): # activate context menu
    try:
        context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()
MainWindow.bind("<ButtonRelease-3>", ACM)
print("done in " + str(time.time() - beginTime) + " seconds")
MainWindow.mainloop()
print("program end")
#adsf
