import tkinter as tk

def close_app(event=None):
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg="black")

label = tk.Label(
    root,
    text="YOU HAVE BEEN HACKED!\n\nAll Data Is Being Uploaded...",
    fg="red",
    bg="black",
    font=("Arial", 40, "bold")
)
label.pack(expand=True)

# Press ESC to close
root.bind("<Escape>", close_app)

root.mainloop()
