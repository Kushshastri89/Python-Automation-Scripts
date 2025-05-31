import tkinter as tk
from tkinter import messagebox, scrolledtext
import pyperclip
import time
import threading
from datetime import datetime

SAVE_FILE = "clipboard_history.txt"

class ClipboardManager:
    def __init__(self, root):
        self.root = root
        self.root.title("📋 Clipboard Manager")
        self.root.geometry("600x450")

        self.displayed_texts = set()
        self.running = True
        self.last_text = ""

        self.history_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 10))
        self.history_box.pack(expand=True, fill='both', padx=10, pady=10)

        self.copy_button = tk.Button(self.root, text="Copy Selected", command=self.copy_selected)
        self.copy_button.pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Start monitoring clipboard in background
        threading.Thread(target=self.monitor_clipboard, daemon=True).start()

    def monitor_clipboard(self):
        while self.running:
            text = pyperclip.paste()
            if text and text != self.last_text:
                self.last_text = text  # Remember last clipboard value to catch even duplicates

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"[{timestamp}] {text}\n"

                # Always save to file
                with open(SAVE_FILE, "a", encoding="utf-8") as f:
                    f.write(log_entry + "\n")

                # Show only new content in GUI (avoids clutter)
                if text not in self.displayed_texts:
                    self.displayed_texts.add(text)
                    self.history_box.insert(tk.END, log_entry)
                    self.history_box.see(tk.END)

            time.sleep(1)

    def copy_selected(self):
        try:
            selected = self.history_box.get(tk.SEL_FIRST, tk.SEL_LAST)
            pyperclip.copy(selected)
            messagebox.showinfo("Copied", "Text copied to clipboard.")
        except tk.TclError:
            messagebox.showwarning("No Selection", "Please select some text first.")

    def on_close(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClipboardManager(root)
    root.mainloop()
