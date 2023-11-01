import tkinter as tk
import kivi

# place a label on the root window
root = tk.Tk()

message1 = tk.Label(root, text="ali")
message2 = tk.Label(root, text="hassan")
message3 = tk.Label(root, text="akbar")
message1.pack()
message2.pack()
message3.pack()

root.mainloop()