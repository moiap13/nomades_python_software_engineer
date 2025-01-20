import customtkinter as ctk

from random_password_generator import generate_password


# Initialize the CustomTkinter app
app = ctk.CTk()
app.title("Random Password Generator")
app.geometry("400x350")

# Function to update the label showing slider value
def update_length_label(value):
    
    length_label.configure(text=f"Length: {int(value)}")

def generate_click():
    password = generate_password(uppercase_var.get(), lowercase_var.get(), digits_var.get(), special_var.get(), length_slider.get()) 
    password_entry.delete(0, ctk.END)
    password_entry.insert(0, password)

# Password length slider
ctk.CTkLabel(app, text="Password Length:").pack(pady=(20, 5))

# Label to show current slider value
length_label = ctk.CTkLabel(app, text="Length: 12")
length_label.pack(pady=5)

# Slider for selecting password length
length_slider = ctk.CTkSlider(app, from_=4, to=32, number_of_steps=28, command=update_length_label)
length_slider.set(12)
length_slider.pack(pady=5)

# Options for password character types
uppercase_var = ctk.BooleanVar(value=True)
lowercase_var = ctk.BooleanVar(value=True)
digits_var = ctk.BooleanVar(value=True)
special_var = ctk.BooleanVar(value=True)

ctk.CTkCheckBox(app, text="Include Uppercase Letters", variable=uppercase_var).pack(anchor='w', padx=20, pady=5)
ctk.CTkCheckBox(app, text="Include Lowercase Letters", variable=lowercase_var).pack(anchor='w', padx=20, pady=5)
ctk.CTkCheckBox(app, text="Include Digits", variable=digits_var).pack(anchor='w', padx=20, pady=5)
ctk.CTkCheckBox(app, text="Include Special Characters", variable=special_var).pack(anchor='w', padx=20, pady=5)

# Entry for displaying the generated password
password_entry = ctk.CTkEntry(app, width=300)
password_entry.pack(pady=(10, 20))

# Button to generate password
generate_button = ctk.CTkButton(app, text="Generate Password", command=generate_click)
generate_button.pack(pady=10)

# Run the app
app.mainloop()
