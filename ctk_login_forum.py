import customtkinter as ctk

# Window settings
app = ctk.CTk()
app.title("Login Form")
app.geometry("400x300")





title_label = ctk.CTkLabel(
    app,
    text="Login Form",
    font=("Times New Roman", 40, "bold"),
    text_color="white"
)
title_label.pack(pady=20)


frame = ctk.CTkFrame(app)
frame.pack(pady=20)



label_1 = ctk.CTkLabel(frame, text="Username:", text_color="white", font=("ranan", 25))
label_1.grid(row=0, column=0, padx=30, pady=10)

entry_1 = ctk.CTkEntry(frame, width=200)
entry_1.grid(row=0, column=1, padx=30, pady=10)

label_2 = ctk.CTkLabel(frame, text="Enter URL:", text_color="white", font=("ranan", 25,))
label_2.grid(row=1, column=0, padx=30, pady=10)
entry_2 = ctk.CTkEntry(frame, width=200)
entry_2.grid(row=1, column=1, padx=30, pady=10)


label_3 = ctk.CTkLabel(frame, text="Enter Website Name:", text_color="white", font=("ranan", 25))
label_3.grid(row=2, column=0, padx=30, pady=10)
entry_3 = ctk.CTkEntry(frame, width=200)
entry_3.grid(row=2, column=1, padx=30, pady=10)
# Function to handle submit button click
def submit_action():    
    username_input = entry_1.get()
    url_input = entry_2.get()
    website_name_input = entry_3.get()
    print("Username:", username_input)
    print("URL:", url_input)
    print("Website Name:", website_name_input)  


submit_button = ctk.CTkButton(
    frame,
    text="Submit",fg_color="darkgreen",hover_color="green",
    command=lambda: [submit_action(), app.quit()],
    font=("Raanan", 20)
)

submit_button.grid(row=3, column=1, padx=30, pady=20)
exit_button = ctk.CTkButton(frame, text="Exit", command=app.quit, font=("ranan", 20),hover_color="red", fg_color="darkred")
exit_button.grid(row=3, column=0, padx=30, pady=20)
tos_button = ctk.CTkButton(frame, text="Terms of Service", font=("ranan", 20),hover_color="grey", fg_color="black",border_color="white",border_width=1)
tos_button.grid(row=4, column=0, padx=100, pady=10, sticky="news", columnspan=2)
privacy_button = ctk.CTkButton(frame, text="Privacy Policy", font=("ranan", 20),hover_color="grey", fg_color="black",border_color="white",border_width=1)
privacy_button.grid(row=5, column=0, padx=100,pady=10, sticky="news", columnspan=2)









app.mainloop()
