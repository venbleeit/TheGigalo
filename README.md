# 🖱️ TheGigalo

**TheGigalo** is a lightweight Python utility that keeps your Windows screen awake by simulating subtle mouse movements in a small 50x50 pixel square. Ideal for when you're working remotely, attending virtual meetings, or stepping away momentarily — without triggering the screen lock or sleep mode.

---

## ⚙️ Features

- ⬆️ Keeps your screen awake with continuous mouse movement
- 📐 Moves in a square pattern (50x50 pixels)
- ⌨️ Start/Stop with `Enter` key
- 🪶 Simple and lightweight — no GUI or bloat

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/TheGigalo.git
cd TheGigalo
```

### 2. Install Python Dependencies

Ensure you have Python 3 installed.

Then install required libraries:

```bash
pip install pyautogui keyboard
```

> If `pip` is not recognized, try `python -m pip install pyautogui keyboard`

---

## ▶️ How to Use

Run the script from the terminal:

```bash
python mouse_jiggler.py
```

### Usage Instructions

1. **Start**: Press `Enter` to begin mouse jiggling.
2. **Stop**: Press `Enter` again while the app is running to stop it safely.

📝 The mouse will move in a repeating 50x50 pixel square pattern every few milliseconds.

---

## 🪛 Troubleshooting

- `ModuleNotFoundError`: Run `pip install pyautogui keyboard`
- Run the command prompt as **Administrator** if `keyboard` requires elevated permissions.
- This tool is designed for **Windows only**.

---

## 📦 Optional: Create a Standalone `.exe`

To package it into an executable:

```bash
pip install pyinstaller
pyinstaller --onefile mouse_jiggler.py
```

This will create a `dist/mouse_jiggler.exe` file for direct use.

---

## 📄 License

MIT License. Feel free to use, modify, and distribute responsibly.

---

## 👨‍💻 Author

Peter Blignaut  
[GitHub Profile](https://github.com/yourusername)
