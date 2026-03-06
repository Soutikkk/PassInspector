# 🛡️ PassInspector

A simple, elegant, and beginner-friendly web application built with **Python Flask** that verifies email formats and evaluates password strength. Featuring a stunning aesthetic frosted glass UI with dynamic aurora mesh gradients! ✨ 

## 🌟 Features
- **Email Validation:** Checks for proper formatting (e.g., `user@example.com`) using built-in Python Regular Expressions (`re`).
- **Password Strength Checker:** Evaluates password security based on precise criteria:
  - 🛑 **Weak:** Less than 6 characters
  - ⚠️ **Medium:** 6–8 characters (or longer but lacking numbers and uppercase letters)
  - ✅ **Strong:** More than 8 characters, containing at least one number and one uppercase letter
- **Aesthetic UI:** A beautifully designed frontend using pure vanilla CSS, featuring glassmorphism elements, dynamic shifting background blobs, and sleek interactive inputs.
- **Beginner Friendly:** Clean, heavily documented Python code perfect for students learning Flask framework basics.

## 🚀 Tech Stack
- **Backend:** Python, Flask (No external complex libraries)
- **Frontend:** HTML5, CSS3 (Vanilla)
- **Design:** Custom frosted glass, Google Fonts ('Inter' used), SVG Icons

## Screenshots
<img width="1169" height="872" alt="app2" src="https://github.com/user-attachments/assets/3dd9a4c9-6f13-4b95-b792-369a2bdd0e9e" />


## 📁 Project Structure
```text
PassInspector/
│
├── app.py             # Main Flask application logic
├── templates/
│   └── index.html     # Frontend UI and form template (Jinja2)
└── README.md          # Project documentation
```

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Soutikkk/PassInspector.git
   cd PassInspector
   ```

2. **Install Flask Requirements:**
   Make sure you have Python installed on your system.
   ```bash
   pip install Flask
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **View in your browser:**
   Open a web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## 💡 How It Works
1. The user inputs their email and password on the aesthetically pleasing frontend.
2. The form submits the data via a `POST` request to the same route (`/`).
3. The backend (`app.py`) validates the input using built-in string methods and Python's `re` module.
4. The backend then returns the evaluation results (`Valid/Invalid`, `Weak/Medium/Strong`) back to the `index.html` template.
5. The frontend utilizes Jinja2 syntax to dynamically render color-coded success/warning badges under the inputs without needing any complex JavaScript.

---
*Built with ❤️ to make learning Flask simple, beautiful, and engaging.*
