# 🔐 Password Generator Pro

A modern and secure password generator built with **Python**, **CustomTkinter**, and **Pyperclip**.

Generate strong passwords instantly, customize password settings, check password strength, copy passwords to your clipboard, and maintain a password history — all through a clean desktop interface.

---

## 📸 Preview

> Add screenshots of your application inside a `screenshots/` folder and update the image links below.

```md
![Main Window](screenshots/main.png)
```

---

## ✨ Features

- 🔒 Secure password generation using Python's `secrets` module
- 📏 Adjustable password length (8–64 characters)
- 🔤 Include uppercase letters
- 🔡 Include lowercase letters
- 🔢 Include numbers
- 🔣 Include special characters
- 📋 One-click copy to clipboard
- 💪 Password strength indicator
- 🕒 Password history tracking
- 🌙 Dark mode support
- ☀️ Light mode support
- 🎨 Modern UI using CustomTkinter
- 🧱 Object-Oriented Programming (OOP) structure

---

## 🛠️ Built With

- Python
- CustomTkinter
- Pyperclip
- Secrets Module
- String Module

---

## 📂 Project Structure

```text
password-generator-pro/
│
├── assets/
│   ├── logo.ico
│   └── logo.png
│
├── screenshots/
│   └── main.png
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/password-generator-pro.git
```

### 2. Navigate to the Project

```bash
cd password-generator-pro
```

### 3. Install Dependencies

```bash
pip install customtkinter pyperclip
```

### 4. Run the Application

```bash
python main.py
```

---

## 🎯 How It Works

1. Select the desired password length.
2. Choose which character types to include:
   - Uppercase letters
   - Lowercase letters
   - Numbers
   - Symbols

3. Click **Generate Password**.
4. Copy the password using the **Copy Password** button.
5. View generated passwords in the history section.

---

## 🔐 Why Use `secrets` Instead of `random`?

This project uses Python's built-in `secrets` module because it is specifically designed for:

- Password generation
- Authentication systems
- Security-sensitive applications

It provides stronger randomness than the standard `random` module.

---

## 📈 Future Improvements

- Password export to TXT/CSV
- Password manager integration
- Password entropy calculation
- QR code sharing
- Multiple password generation
- Save settings between sessions
- Custom themes

---

## 🧠 What I Learned

Through this project I practiced:

- Python Programming
- Object-Oriented Programming
- GUI Development
- Event Handling
- Clipboard Operations
- Secure Password Generation
- Software Project Structure

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐.

---

## 👩‍💻 Author

**Preeti Sasmal**

- Python Developer
- Aspiring Software Engineer
- AI & Mathematics Enthusiast

---

## 📜 License

This project is licensed under the MIT License.
