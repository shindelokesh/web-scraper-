import tkinter as tk


window = tk.Tk()
window.title("Login Forum")
window.geometry("400x300") 

label_1 = tk.Label(window, text="Username:")
label_1.grid(row=0, column=0, padx=30, pady=2.5)

entry_1 = tk.Entry(window)
entry_1.grid(row=0, column=1,padx=30, pady=2.5)  \

label_2 = tk.Label(window, text="enter url:")
label_2.grid(row=1, column=0, padx=30, pady=2.5)

entry_2 = tk.Entry(window)
entry_2.grid(row=1, column=1,padx=30, pady=2.5)  

label_3 = tk.Label(window, text="enter website name:")
label_3.grid(row=2, column=0, padx=30, pady=2.5)

entry_3 = tk.Entry(window)
entry_3.grid(row=2, column=1,padx=30, pady=2.5)  

button_1 = tk.Button(window, text="Submit")
button_1.grid(row=3, column=1, padx=30, pady=30)

button_1 = tk.Button(window, text="exit ", command=window.quit)
button_1.grid(row=3, column=0, padx=30, pady=30)

button_1 = tk.Button(window, text="terms of service")
button_1.grid(row=4, column=0, padx=100, pady=2.5) 

button_1 = tk.Button(window, text="privacy policy", command=window.quit)
button_1.grid(row=5, column=0, padx=100, pady=2.5,sticky="news")


window.mainloop()
