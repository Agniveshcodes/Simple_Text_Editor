import tkinter as tk
from tkinter import filedialog, messagebox

# Main window for text editor
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("600x400")

# Create Text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 10)
)

text.pack(expand=True, fill=tk.BOTH)

# Main Logic for our text editor

# Function 1 - to create a new file

def createNewFile () :
    text.delete(1.0, tk.END)
    
# Functiom 2 - to open a new file

def openNewFile () :
    # Show open file dialogue 
    filePath = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
               
    )   
     
    if filePath :
        # open file
        with open(filePath , "r") as newFile:
            # clear old text
            text.delete(1.0 , tk.END)
            text.insert(tk.END , newFile.read())
            
# Function 3 - to save the file

def saveFile () :
    # open ave file dialogue
    filePath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    ) 
    
    if filePath:
        try:
            with open(filePath, "w") as newFile:
                text.delete(1.0, tk.END)
                text.insert(tk.END, newFile.read())
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
# Making the menu
menu = tk.Menu(root)
root.config(menu=menu)
fileMenu = tk.Menu(menu, tearoff=0)


# New open file, save , exit options

# add fileMenu to menu bar 
menu.add_cascade(label="File" ,  menu=fileMenu)


fileMenu.add_command(label="New", command=createNewFile)
fileMenu.add_command(label="Open", command=openNewFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command=root.quit)
            
               
# --- NEW: This ensures the cursor starts in the text box ---
text.focus_set() 

# to start our app and keep window open
root.mainloop()