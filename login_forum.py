import tkinter as tk

# window setings
window = tk.Tk()
window.title("Login Forum")
window.geometry("400x300") 
window.configure(bg="black")

# frame setings
frame = tk.Frame(window, bg="black")
frame.pack(pady=200)

# labels and entries
label_1 = tk.Label(frame, text="Username:",bg="black", fg="white")
label_1.grid(row=0, column=0, padx=30, pady=2.5)

entry_1 = tk.Entry(frame)
entry_1.grid(row=0, column=1,padx=30, pady=2.5)  \

label_2 = tk.Label(frame, text="enter url:",bg="black", fg="white")
label_2.grid(row=1, column=0, padx=30, pady=2.5)

entry_2 = tk.Entry(frame)
entry_2.grid(row=1, column=1,padx=30, pady=2.5)  

label_3 = tk.Label(frame, text="enter website name:",bg="black", fg="white")
label_3.grid(row=2, column=0, padx=30, pady=2.5)

entry_3 = tk.Entry(frame)
entry_3.grid(row=2, column=1,padx=30, pady=2.5)  

button_1 = tk.Button(frame, text="Submit",bg="black")
button_1.grid(row=3, column=1, padx=30, pady=30)

button_1 = tk.Button(frame, text="exit ", command=window.quit,bg="black")
button_1.grid(row=3, column=0, padx=30, pady=30)

button_1 = tk.Button(frame, text="terms of service",bg="black")
button_1.grid(row=4, column=0, padx=100, pady=2.5,sticky="news",columnspan=2) 

button_1 = tk.Button(frame, text="privacy policy",bg="black")
button_1.grid(row=5, column=0, padx=100, pady=2.5,sticky="news" ,columnspan=2)


window.mainloop()



