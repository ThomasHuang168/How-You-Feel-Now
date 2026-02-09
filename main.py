import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import logging
from pathlib import Path
import re
from datetime import datetime
import webbrowser

# Configure logging to write to responses.log with timestamp
logPath:Path = Path("responses") / datetime.now().strftime("%Y%m%d.csv")
logPath.parent.mkdir(parents=True, exist_ok=True)
    
logging.basicConfig(filename=str(logPath), level=logging.INFO, 
                    format="%(asctime)s, %(message)s", datefmt="%Y-%m-%d, %H:%M:%S")


# def show_responses():
#     with logPath.open("r")as fr:
#         logLines = fr.readlines()
#         logLines.reverse()
#         log_text["state"] = tk.NORMAL
#         log_text.delete(1.0, tk.END)
#         log_text.insert(tk.END, "".join(logLines))
#         log_text["state"] = tk.DISABLED

def open_feedback_link():
    webbrowser.open("https://docs.google.com/forms/d/e/1FAIpQLSdcFlKouCo0ckwc-HZeID-eVx6lqmJW9R4PkC_JynhWv25FEg/viewform")

def save_response(feeling):
    #postcode = postcode_entry.get()

    #if not postcode:
    #    messagebox.showwarning("Input Error", "Please enter your postcode.")
    #    return
    #elif not re.fullmatch(r'[A-Za-z]{1,2}[0-9R][0-9A-Za-z]? ?[0-9][A-Za-z]{2}', postcode):
    #    messagebox.showwarning("Input Error", f"{postcode} is not a proper Postcode")
    #    return

    #postcode = postc ode.upper()
    #postcode = re.sub(r'([A-Za-z]{1,2}[0-9R][0-9A-Za-z]?) ?([0-9][A-Za-z]{2})',r'\1 \2', postcode)
    #log_entry = f"{postcode}, {feeling}"
    log_entry = f"{feeling}"
    logging.info(log_entry)

    # show_responses()
    
    messagebox.showinfo("Success", "Response saved successfully!")
    #postcode_entry.delete(0, tk.END)

def create_circle_button(canvas:tk.Canvas, x, y, radius, color, text, command, text_color):
    """Creates a circular button using the Canvas widget"""
    circle = canvas.create_oval(x-radius, 
                                y-radius, 
                                x+radius, 
                                y+radius, 
                                fill=color, 
                                # outline="black",
                                )

    if text[-4:] != ".png":
        label = canvas.create_text(x, y, text=text, font=("Arial", 28), fill=text_color)
    else:
        image = PhotoImage(file=text)
        root.image=image
        label = canvas.create_image(x, y, image=image)

    def on_click(event):
        command()
    # Bind click event to the circular button
    canvas.tag_bind(circle, "<Button-1>", on_click)
    canvas.tag_bind(label, "<Button-1>", on_click)

# Create the main window
root = tk.Tk()
root.title("Mood and Location Survey")
root.attributes('-fullscreen', True)  # Enable fullscreen

# Exit fullscreen with Escape key
root.bind("<Escape>", lambda event: root.attributes('-fullscreen', False))

## Label and entry field for postcode
#tk.Label(root, text="Your Postcode:", font=("Arial", 28)).pack(pady=20)
#postcode_entry = tk.Entry(root, font=("Arial", 24))
#postcode_entry.pack()

# Label for mood selection
tk.Label(root, text="How are you doing?", font=("Arial", 28)).pack(pady=40)

# # Frame for horizontal layout of buttons
# button_frame = tk.Frame(root)
# button_frame.pack(fill=tk.BOTH, padx=20, pady=5,)

# Mood buttons with colors and emojis
# tk.Button(button_frame, text="😢 Bad", font=("Arial", 32), bg="red", fg="white", 
#           command=lambda: save_response("Bad"), width=10, height=3,).pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10,)

# tk.Button(button_frame, text="😐 Ok", font=("Arial", 32), bg="yellow", fg="black", 
#           command=lambda: save_response("Ok"), width=10, height=3,).pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10,)

# tk.Button(button_frame, text="😊 Good", font=("Arial", 32), bg="green", fg="white", 
#           command=lambda: save_response("Good"), width=10, height=3,).pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10,)
# Create canvas for circular buttons
canvas = tk.Canvas(root, width=1120, height=220)
canvas.pack()
create_circle_button(canvas, 110, 110, 100, "red", "😢 Bad", lambda: save_response("Bad"),"white")
create_circle_button(canvas, 410, 110, 100, "yellow", "😐 Ok", lambda: save_response("Ok"), "black")
create_circle_button(canvas, 710, 110, 100, "green", "😊 Good", lambda: save_response("Good"),"white")
create_circle_button(canvas, 1010, 110, 100, "",r"QR_code.png", open_feedback_link,"white")
# # Log viewer/editor
# tk.Label(root, text="Responses", font=("Arial", 20)).pack(pady=20)
# log_text = tk.Text(root, font=("Arial", 16), height=10, width=80, wrap=tk.WORD, state=tk.DISABLED)

# log_text.pack(pady=10)
# show_responses()

# Run the application
root.mainloop()
