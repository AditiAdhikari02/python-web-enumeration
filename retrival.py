import tkinter as tk
from tkinter import filedialog
import os


def retrieve_data():
    # Get the selected file path
    file_path = file_entry.get()

    # Check if the file exists
    if not os.path.exists(file_path):
        status_label.config(text="File not found!", fg="red")
        return

    # Try to read the file contents
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            data_text.delete(1.0, tk.END)  # Clear the text box
            data_text.insert(tk.END, data)  # Insert the retrieved data
            status_label.config(text="Data retrieved successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

def browse_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
    file_entry.delete(0, tk.END)  # Clear the file entry field
    file_entry.insert(tk.END, file_path)  # Insert the selected file path

# Create the main window
root = tk.Tk()
root.title("Lost Data Retrieval")

# Create the file entry field and button
file_label = tk.Label(root, text="Select a file:")
file_label.grid(row=0, column=0, padx=5, pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Create the retrieve data button
retrieve_button = tk.Button(root, text="Retrieve Data", command=retrieve_data)
retrieve_button.grid(row=1, column=1, padx=5, pady=5)

# Create the status label
status_label = tk.Label(root, text="", fg="black")
status_label.grid(row=2, column=1, padx=5, pady=5)

# Create the data text box
data_text = tk.Text(root, width=60, height=10)
data_text.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()