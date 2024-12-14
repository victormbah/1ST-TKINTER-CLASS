import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("My First tkinter project")

label = tk.Label(root, text="WELCOME!", font= ('Courier',18))
label.pack(padx=28, pady=28)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

frame = tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

frame1 = tk.Button(frame, text='1', font=('Arial', 18))
frame1.grid(row=0, column=0, sticky=tk.W+tk.E)

frame2 = tk.Button(frame, text='2', font=('Arial', 18))
frame2.grid(row=0, column=1, sticky=tk.W+tk.E)

frame3 = tk.Button(frame, text='3', font=('Arial', 18))
frame3.grid(row=0, column=2, sticky=tk.W+tk.E)

frame4 = tk.Button(frame, text='4', font=('Arial', 18))
frame4.grid(row=1, column=0, sticky=tk.W+tk.E)

frame5 = tk.Button(frame, text='5', font=('Arial', 18))
frame5.grid(row=1, column=1, sticky=tk.W+tk.E)

frame6 = tk.Button(frame, text='6', font=('Arial', 18))
frame6.grid(row=1, column=2, sticky=tk.W+tk.E)

# Pack the frame into the root window
frame.pack(fill='x')


button = tk.Button(root, text='Click Me!', font= ('Courier',10))
button.pack(padx=10, pady=10)


root.mainloop() 
 