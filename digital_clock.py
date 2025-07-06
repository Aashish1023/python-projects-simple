import tkinter as tk
from time import strftime
import datetime

#Create the main window
root = tk.Tk()
root.title("Digital clock")

# Set the background color
root.geometry("400x200")
root.configure(bg="black")

# Create a label to display the time
label = tk.Label(root, font=("calibri", 40, "bold"), bg="black", fg="white")
label.pack(anchor='center', pady=20)

#date label
date_label = tk.Label(root, font=("calibri", 20),background="black", fg="white")
date_label.pack(anchor='center' )

# Function to update the time
def time():
    current_time = strftime('%I:%M:%S %p')
    current_date = datetime.datetime.now().strftime('%A, %B %d, %Y') 

    label.config(text=current_time)
    date_label.config(text=current_date) 
    label.after(1000, time)  # Update every second


# call the time function once to start
time()

# Run the main Loop
root.mainloop()