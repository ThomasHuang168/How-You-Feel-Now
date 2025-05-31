import tkinter as tk
from tkinter import messagebox
import logging
from pathlib import Path
import re
from datetime import datetime

# Configure logging to write to responses.log with timestamp
logPath:Path = Path("responses") / datetime.now().strftime("%Y%m%d.csv")
logPath.parent.mkdir(parents=True, exist_ok=True)
    
logging.basicConfig(filename=str(logPath), level=logging.INFO, 
                    format="%(asctime)s - %(message)s",)


def show_responses():
    with logPath.open("r")as fr:
        logLines = fr.readlines()
        logLines.reverse()
        log_text["state"] = tk.NORMAL
        log_text.delete(1.0, tk.END)
        log_text.insert(tk.END, "".join(logLines))
        log_text["state"] = tk.DISABLED

def save_response(feeling):
    postcode = postcode_entry.get()

    if not postcode:
        messagebox.showwarning("Input Error", "Please enter your postcode.")
        return
    elif not re.fullmatch(r'[A-Z]{1,2}[0-9R][0-9A-Z]? [0-9][A-Z]{2}', postcode):
        messagebox.showwarning("Input Error", f"{postcode} is not a proper Postcode")
        return

    
    log_entry = f"Postcode: {postcode}, Feeling: {feeling}"
    logging.info(log_entry)

    show_responses()
    
    # messagebox.showinfo("Success", "Response saved successfully!")
    postcode_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Mood and Location Survey")
root.attributes('-fullscreen', True)  # Enable fullscreen

# Exit fullscreen with Escape key
root.bind("<Escape>", lambda event: root.attributes('-fullscreen', False))

# Label and entry field for postcode
tk.Label(root, text="Your Postcode:", font=("Arial", 28)).pack(pady=20)
postcode_entry = tk.Entry(root, font=("Arial", 24))
postcode_entry.pack()

# Label for mood selection
tk.Label(root, text="How are you now?", font=("Arial", 28)).pack(pady=40)

# Frame for horizontal layout of buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, padx=20, pady=5,)

# Mood buttons with colors and emojis
tk.Button(button_frame, text="😢 Bad", font=("Arial", 32), bg="red", fg="white", 
          command=lambda: save_response("Bad"), width=10, height=3,).pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10,)

tk.Button(button_frame, text="😐 Ok", font=("Arial", 32), bg="yellow", fg="black", 
          command=lambda: save_response("Ok"), width=10, height=3,).pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10,)

tk.Button(button_frame, text="😊 Good", font=("Arial", 32), bg="green", fg="white", 
          command=lambda: save_response("Good"), width=10, height=3,).pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10,)

# Log viewer/editor
tk.Label(root, text="Responses", font=("Arial", 20)).pack(pady=20)
log_text = tk.Text(root, font=("Arial", 16), height=10, width=80, wrap=tk.WORD, state=tk.DISABLED)

log_text.pack(pady=10)
show_responses()

# Run the application
root.mainloop()
