import sys
import os
import subprocess
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk  # Ensure PIL is installed: pip install Pillow
import json
import socket


def find_file(filename):
    """Locate a file relative to the executable or script location."""
    base_dir = get_script_dir()
    potential_paths = [
        os.path.join(base_dir, 'icons', filename),  # Adjusted path for bundled resources
        os.path.join(base_dir, filename)
    ]
    for path in potential_paths:
        if os.path.isfile(path):
            return path
    raise FileNotFoundError(f"{filename} not found in any of the specified paths.")


def get_script_dir():
    """Get the directory where the script or executable is located."""
    if getattr(sys, 'frozen', False):  # Running as a bundled executable
        return os.path.dirname(sys.executable)
    else:  # Running as a Python script
        return os.path.dirname(os.path.abspath(__file__))
    
    
def find_and_execute_exe(exe_name, task_name):
    """Find and execute the specified executable with output redirection."""
    base_dir = get_script_dir()
    exe_path = os.path.join(base_dir, exe_name)

    if not os.path.isfile(exe_path):
        messagebox.showerror("Error", f"{exe_name} not found at {exe_path}.")
        return

    computer_name = os.getenv('COMPUTERNAME') or socket.gethostname()
    results_folder = os.path.join(base_dir, computer_name)
    os.makedirs(results_folder, exist_ok=True)

    results_file = os.path.join(results_folder, f"{task_name}.txt")
    command = f'"{exe_path}" > "{results_file}" 2>&1'
    print(f"Executing command: {command}")

    try:
        subprocess.Popen(command, shell=True, cwd=base_dir)
        messagebox.showinfo("Success", f"{task_name} process started. Results saved to: {results_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Error executing {task_name} process: {str(e)}")
        

def open_RESULTS_folder():
    """Open the results folder in the file explorer."""
    computer_name = os.getenv('COMPUTERNAME') or socket.gethostname()
    base_dir = get_script_dir()
    results_folder = os.path.join(base_dir, computer_name)

    if os.path.exists(results_folder):
        subprocess.Popen(f'explorer "{results_folder}"')
    else:
        messagebox.showerror("Error", f"RESULTS folder not found: {results_folder}")


class GradientButton(tk.Frame):
    def __init__(self, parent, text, command=None, width=20):
        super().__init__(parent, bg="#000000")

        print(f"Creating button with text: {text}, width: {width}")
        self.button = tk.Button(self, text=text, command=command,
                                font=("Comic Sans MS", 12, "bold"),
                                bg="#FFEB3B", fg="black",
                                borderwidth=0, padx=12, pady=12,
                                activebackground="#FFD54F",
                                highlightthickness=0,
                                relief="flat",
                                width=width,
                                anchor='center')

        self.button.pack(expand=True, fill='both')
        self.button.bind("<Enter>", self.on_hover)
        self.button.bind("<Leave>", self.on_leave)
        self.button.bind("<ButtonPress>", self.on_click)
        self.button.bind("<ButtonRelease>", self.on_release)

    def on_hover(self, event):
        self.button.config(bg="#FFD54F")

    def on_leave(self, event):
        self.button.config(bg="#FFEB3B")

    def on_click(self, event):
        self.button.config(bg="#FFC107")

    def on_release(self, event):
        self.button.config(bg="#FFD54F")


def browse_folder(folder_type):
    folder_path = filedialog.askdirectory()
    if folder_path:
        messagebox.showinfo(f"{folder_type} Folder Selected", f"You selected: {folder_path}")


def data_folder_function():
    selected_file = filedialog.askopenfilename()
    if selected_file:
        find_and_execute_exe("HASH VALUE.exe", "Hash Value")
        find_and_execute_exe("META DATA.exe", "Meta Data")


root = tk.Tk()
root.title("Cyber Crime Helpline LLP - Digital Forensics Toolkit")

top_margin = 100
bottom_margin = 100
left_margin = 150
right_margin = 150

root.geometry(f"{1400 - left_margin - right_margin}x{900 - top_margin - bottom_margin}")
root.configure(bg="#000000")

for i in range(3):
    root.grid_columnconfigure(i, weight=1)

title_label = tk.Label(root, text="CYBER CRIME HELPLINE LLP", font=("Comic Sans MS", 35, "bold"), fg="red", bg="#000000")
title_label.grid(row=0, column=0, columnspan=3, pady=(22, 5), sticky="n")

subtitle_label = tk.Label(root, text="DIGITAL FORENSICS TOOLKIT", font=("Comic Sans MS", 25, "bold"), fg="#F7F7F7", bg="#000000")
subtitle_label.grid(row=1, column=0, columnspan=3, pady=(0, 5), sticky="n")

left_image_path = find_file('cchlogo.jpg')
if left_image_path:
    try:
        left_image = Image.open(left_image_path)
        left_logo = ImageTk.PhotoImage(left_image)
        left_logo_label = tk.Label(root, image=left_logo, bg="#000000")
        left_logo_label.grid(row=0, column=0, sticky="nw", padx=(30, 0), pady=(15, 0))
    except Exception as e:
        messagebox.showwarning("Image Load Failed", f"Failed to load the logo image. Error: {str(e)}")
        default_image = Image.new("RGB", (200, 100), color="gray")
        default_logo = ImageTk.PhotoImage(default_image)
        default_logo_label = tk.Label(root, image=default_logo, bg="#000000")
        default_logo_label.grid(row=0, column=0, sticky="nw", padx=(30, 0), pady=(15, 0))
else:
    messagebox.showwarning("Image Not Found", "The logo image 'cchlogo.jpg' was not found. Using default placeholder.")
    default_image = Image.new("RGB", (200, 100), color="gray")
    default_logo = ImageTk.PhotoImage(default_image)
    default_logo_label = tk.Label(root, image=default_logo, bg="#000000")
    default_logo_label.grid(row=0, column=0, sticky="nw", padx=(30, 0), pady=(15, 0))


top_dashed_line = tk.Label(root, text="===================================================================",
                           font=("Comic Sans MS", 12, "bold"), fg="white", bg="#000000")
top_dashed_line.grid(row=5, column=0, columnspan=3, pady=(20, 5), sticky="nsew")

button_data = [
    ("HASH VALUE", "Hash Value.exe"),
    ("META DATA", "Meta Data.exe"),
    ("WINDOWS AUDIT", "Windows Audit.exe"),
    ("ACTIVITY DETAILS", "Activity Details.exe"),
    ("WIRELESS DETAILS", "Wireless Details.exe"),
    ("SERVER AUDIT", "Server Audit.exe"),
    ("BROWSER FORENSICS", "Browser Forensics.exe"),
    ("FILES EXTRACTION", "Files Extraction.exe"),
    ("COMPLETE FORENSICS", "Complete Forensics.exe")
]

button_width = 15

for index, (text, exe_name) in enumerate(button_data):
    row = index // 3
    col = index % 3

    button_frame = tk.Frame(root, bg="black")
    button_frame.grid(row=row + 2, column=col, padx=10, pady=10, sticky="nsew")

    button = GradientButton(button_frame, text,
                            command=lambda exe_name=exe_name, text=text: find_and_execute_exe(exe_name, text),
                            width=button_width)
    button.button.config(font=("Comic Sans MS", 12, "bold"), padx=8, pady=8)
    button.pack(expand=True, fill='both')


folders_frame = tk.Frame(root, bg="#000000")
folders_frame.grid(row=6, column=0, columnspan=3, pady=(30, 10))

data_folder_button = GradientButton(folders_frame, "DATA FOLDER", command=data_folder_function, width=20)
data_folder_button.pack(side="left", padx=10, fill='both')

results_folder_button = GradientButton(folders_frame, "RESULTS FOLDER", command=open_RESULTS_folder, width=20)
results_folder_button.pack(side="left", padx=10, fill='both')

bottom_dashed_line = tk.Label(root, text="===================================================================",
                              font=("Comic Sans MS", 12, "bold"), fg="white", bg="#000000")
bottom_dashed_line.grid(row=7, column=0, columnspan=3, pady=(20, 5), sticky="nsew")


# Smooth marquee scroll function
def smooth_marquee_scroll():
    current_x = marquee_label.winfo_x()
    
    # If the text has fully moved off the left side, reset it to the right side
    if current_x < -marquee_label.winfo_width():
        marquee_label.place(x=root.winfo_width())
    else:
        marquee_label.place(x=current_x - 2)  # Move 2 pixels to the left for smooth scrolling
    
    root.after(50, smooth_marquee_scroll)  # Adjust timing for smoothness (20ms interval)

# Updated marquee configuration using pixel-based scrolling
marquee_text = "THIS IS A PROPRIETARY TOOL OF CYBER CRIME HELPLINE LLP. FOR COURSES AND INVESTIGATIONS, WHATSAPP ON +91 9595427200.THIS IS A PROPRIETARY TOOL OF CYBER CRIME HELPLINE LLP. FOR COURSES AND INVESTIGATIONS, WHATSAPP ON +91 9595427200.  " * 3
marquee_label = tk.Label(root, text=marquee_text, font=("Comic Sans MS", 18, "bold"), fg="white", bg="#000000", anchor='w')

# Set the initial position of the marquee label outside the visible area on the right
marquee_label.place(x=root.winfo_width(), y=650)  # Adjust y as per your grid or layout

smooth_marquee_scroll()

root.mainloop()
