
## 📅 Week 0: System Setup Basics

---

## 1. 🧱 Install VS Code

🔗 [Download VS Code](https://code.visualstudio.com/Download)

| OS                    | File Type |
| --------------------- | --------- |
| Windows               | `.exe`    |
| macOS                 | `.zip`    |
| Linux (Ubuntu/Debian) | `.deb`    |

**During Installation, ensure:**

* ✅ Add to PATH
* ✅ Register Code as editor
* ✅ Add “Open with Code” to right-click menu

---

## 2. 🐍 Python Virtual Environment & Development Setup

### ➤ Install Python

🔗 [Download Python](https://www.python.org/downloads/)

### ➤ Create a Virtual Environment

```bash
python -m venv venv
```

#### Activate the Environment:

* **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```
* **Windows:**

  ```cmd
  venv\Scripts\activate
  ```

### ➤ Install Python Extension in VS Code

🔗 [Python Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

---

## 3. 📷 Install OpenCV & Google Vision OCR (Inside `venv`)

### ➤ Install Required Packages

```bash
pip install opencv-python
pip install opencv-python-headless
pip install google-cloud-vision
```

### ➤ Google Vision Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. **Enable Vision API**
4. **Create a service account** and download the **credentials JSON**

#### Set the environment variable:

* **Linux/macOS:**

  ```bash
  export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
  ```

* **Windows:**

  ```cmd
  set GOOGLE_APPLICATION_CREDENTIALS=path\to\your\credentials.json
  ```

---

## 4. 💻 Install Flutter & Dart

### ➤ Download Flutter SDK

🔗 [Flutter Install Guide](https://docs.flutter.dev/get-started/install)

Follow instructions based on your OS.

#### Add Flutter to PATH:

* **macOS/Linux:**

  ```bash
  export PATH="$PATH:/path-to-flutter/bin"  # in .bashrc or .zshrc
  ```
* **Windows:**
  Add `flutter/bin` to **System Environment Variable PATH**

### ➤ Run Flutter Doctor

```bash
flutter doctor
```

* Follow the instructions shown to resolve any issues

### ➤ Install Flutter & Dart Extensions in VS Code

* 🔗 [Flutter Extension](https://marketplace.visualstudio.com/items?itemName=Dart-Code.flutter)
* 🔗 [Dart Extension](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code)

---

## 🎥 Additional Resources

* **VS Code Setup:**
  [YouTube: Setup VS Code](https://youtu.be/bN6DE-4uFNo?si=ZuU774JYCPxkRcM4)

* **Flutter Setup:**
  [YouTube: Setup Flutter](https://youtu.be/BqHOtlh3Dd4?si=t4CcFjsCVfzmEgm6)

* **Python Virtual Environment:**
  [YouTube: Virtual Envs](https://youtu.be/nt6LlFTWOkg?si=n83_Gz8QZ3wicfw3)
