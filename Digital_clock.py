import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.configure(bg='black')

# Create and configure the label
label = tk.Label(root, font=('Arial', 40, 'bold'), background='black', foreground='lime')
label.pack(anchor='center', expand=True)

# Define the time-update function
def update_time():
    time_string = strftime('%H:%M:%S')  # Format: 24-hour HH:MM:SS
    label.config(text=time_string)
    label.after(1000, update_time)  # Call this function again after 1 second

# Start the clock
update_time()

# Run the GUI event loop
root.mainloop()
