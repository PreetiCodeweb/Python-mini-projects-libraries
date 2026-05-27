import customtkinter as ctk
import secrets
import string
import pyperclip


class PasswordGeneratorApp:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Password Generator Pro")
        self.root.geometry("700x550")
        self.root.resizable(False, False)

        self.password_history = []

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self.root,
            text="🔐 Password Generator Pro",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        self.password_entry = ctk.CTkEntry(
            self.root,
            width=500,
            height=45,
            font=("Consolas", 18)
        )
        self.password_entry.pack(pady=10)

        length_frame = ctk.CTkFrame(self.root)
        length_frame.pack(pady=10)

        ctk.CTkLabel(
            length_frame,
            text="Password Length:"
        ).pack(side="left", padx=10)

        self.length_slider = ctk.CTkSlider(
            length_frame,
            from_=8,
            to=64,
            number_of_steps=56,
            command=self.update_length_label
        )
        self.length_slider.set(16)
        self.length_slider.pack(side="left", padx=10)

        self.length_label = ctk.CTkLabel(
            length_frame,
            text="16"
        )
        self.length_label.pack(side="left")

        options_frame = ctk.CTkFrame(self.root)
        options_frame.pack(pady=15)

        self.upper_var = ctk.BooleanVar(value=True)
        self.lower_var = ctk.BooleanVar(value=True)
        self.number_var = ctk.BooleanVar(value=True)
        self.symbol_var = ctk.BooleanVar(value=True)

        ctk.CTkCheckBox(
            options_frame,
            text="Uppercase",
            variable=self.upper_var
        ).grid(row=0, column=0, padx=10, pady=5)

        ctk.CTkCheckBox(
            options_frame,
            text="Lowercase",
            variable=self.lower_var
        ).grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkCheckBox(
            options_frame,
            text="Numbers",
            variable=self.number_var
        ).grid(row=1, column=0, padx=10, pady=5)

        ctk.CTkCheckBox(
            options_frame,
            text="Symbols",
            variable=self.symbol_var
        ).grid(row=1, column=1, padx=10, pady=5)

        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=15)

        ctk.CTkButton(
            button_frame,
            text="Generate Password",
            command=self.generate_password,
            width=180
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            button_frame,
            text="Copy Password",
            command=self.copy_password,
            width=180
        ).grid(row=0, column=1, padx=10)

        self.strength_label = ctk.CTkLabel(
            self.root,
            text="Strength: N/A",
            font=("Arial", 16)
        )
        self.strength_label.pack(pady=10)

        self.history_box = ctk.CTkTextbox(
            self.root,
            width=600,
            height=150
        )
        self.history_box.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.root,
            text="Ready",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=5)

        self.theme_switch = ctk.CTkSwitch(
            self.root,
            text="Light Mode",
            command=self.toggle_theme
        )
        self.theme_switch.pack(pady=10)

    def update_length_label(self, value):
        self.length_label.configure(text=str(int(value)))

    def generate_password(self):

        characters = ""

        if self.upper_var.get():
            characters += string.ascii_uppercase

        if self.lower_var.get():
            characters += string.ascii_lowercase

        if self.number_var.get():
            characters += string.digits

        if self.symbol_var.get():
            characters += string.punctuation

        if not characters:
            self.status_label.configure(
                text="Select at least one option!"
            )
            return

        length = int(self.length_slider.get())

        password = "".join(
            secrets.choice(characters)
            for _ in range(length)
        )

        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)

        self.password_history.append(password)

        self.history_box.insert(
            "end",
            password + "\n"
        )

        self.update_strength(password)

        self.status_label.configure(
            text="Password generated successfully!"
        )

    def update_strength(self, password):

        score = 0

        if any(c.islower() for c in password):
            score += 1

        if any(c.isupper() for c in password):
            score += 1

        if any(c.isdigit() for c in password):
            score += 1

        if any(c in string.punctuation for c in password):
            score += 1

        if len(password) >= 16:
            score += 1

        strengths = {
            1: "Weak",
            2: "Medium",
            3: "Good",
            4: "Strong",
            5: "Very Strong"
        }

        self.strength_label.configure(
            text=f"Strength: {strengths.get(score, 'Weak')}"
        )

    def copy_password(self):

        password = self.password_entry.get()

        if password:
            pyperclip.copy(password)

            self.status_label.configure(
                text="Password copied to clipboard!"
            )

    def toggle_theme(self):

        if self.theme_switch.get():
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.run()