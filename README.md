# 🎤 FastAPI Text-to-Speech (TTS) App

A simple **Text-to-Speech (TTS)** application built with **FastAPI** that converts text into speech using **Smallest AI**. The app provides an interactive web interface to listen to the generated speech and download the MP3 file.

## 🚀 Features

✅ **Convert Text to Speech** using Smallest AI API  
✅ **Listen to the Generated Speech** directly in the browser  
✅ **Download the Audio** as an MP3 file  
✅ **FastAPI Backend** with an interactive API  
✅ **Simple Web UI** using HTML & JavaScript  

## 📂 Project Structure
```
📂 fastapi-tts-app
│-- 📄 main.py  # FastAPI application
│-- 📄 .env  # Environment variables (API key)
│-- 📄 requirements.txt  # Python dependencies
│-- 📄 README.md  # Project documentation
```

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/fastapi-tts-app.git
cd fastapi-tts-app
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file and add your **Smallest AI API key**:
```
SMALLEST_API_KEY=your_api_key_here
```

### 5️⃣ Run the FastAPI App
```sh
uvicorn main:app --reload
```

### 6️⃣ Open the Web Interface
Go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
Enter text, click **Convert**, listen to the generated speech, and download the MP3 file!  

## 📌 API Endpoints

| Method | Endpoint | Description |
|--------|------------|-----------------|
| `POST` | `/text-to-speech/` | Converts text to speech and returns an audio file |
| `GET`  | `/` | Web UI to enter text, listen, and download audio |

## 📜 License
This project is licensed under the **MIT License**.

## ⭐ Contributing
Contributions are welcome! Feel free to **fork** this repo and submit a **pull request**.

---

💡 **Have suggestions or issues?** Open an [issue](https://github.com/your-username/fastapi-tts-app/issues) or reach out!

Happy coding! 🚀

