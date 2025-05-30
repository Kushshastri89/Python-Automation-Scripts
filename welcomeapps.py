import os
import time
import subprocess
from tkinter import Tk, Label

# 1. Show welcome popup for 2+ seconds
def show_popup():
    root = Tk()
    root.title("Welcome")
    root.geometry("250x100+100+100")
    Label(root, text="🎵 Welcome! Starting your tools... 🎮", font=("Arial", 10)).pack(pady=20)
    root.after(2500, root.destroy)  # Close after 2.5 seconds
    root.mainloop()

# 2. Open YouTube Music in Microsoft Edge
def open_youtube_music():
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    if os.path.exists(edge_path):
        subprocess.Popen([edge_path, "https://music.youtube.com"])
    else:
        print("❌ Microsoft Edge not found!")

# 3. Open Visual Studio Code
def open_vscode():
    subprocess.Popen(r"C:\Users\ACER\AppData\Local\Programs\Microsoft VS Code\Code.exe")

# --- Main ---
show_popup()
time.sleep(0.5)
open_youtube_music()
open_vscode()
