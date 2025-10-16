# 🎥 Livestream Overlay Backend (Flask + MongoDB)

This backend provides REST APIs and real-time socket updates for managing overlays (text or image) on top of a livestream video.  
It’s built using **Flask**, **MongoDB**, and **Socket.IO**.

---

## 🚀 Features
- CRUD API for overlays (Create, Read, Update, Delete)
- Real-time updates using Flask-SocketIO
- Support for **text** and **image** overlays
- RTSP livestream endpoint for MJPEG streaming

---

## 🛠 Tech Stack
- **Backend:** Flask (Python)
- **Database:** MongoDB
- **Real-Time:** Socket.IO
- **Streaming:** OpenCV + RTSP + MJPEG
- **Frontend:** React (separate repo)

---

## 📦 Project Structure
backend/
├─ app.py
├─ config.py
├─ stream_manager.py
├─ utils.py
├─ requirements.txt

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment & Install Dependencies
```bash
cd backend
python -m venv venv
venv\Scripts\activate   # on Windows
pip install -r requirements.txt
2️⃣ Start MongoDB
Ensure MongoDB is running locally or update config.py with your MongoDB connection string.

3️⃣ Run Flask App
bash
Copy code
python app.py
The backend will start on:
👉 http://localhost:5000

🔌 API Endpoints
Method	Endpoint	Description
POST	/overlays	Create new overlay
GET	/overlays	Retrieve all overlays
PUT	/overlays/<id>	Update overlay by ID
DELETE	/overlays/<id>	Delete overlay by ID
GET	/stream?url=<RTSP_URL>	Stream live video

🧾 Example Overlay Payloads
Text Overlay

json
Copy code
{
  "type": "text",
  "content": "Hello World",
  "position": { "x": 50, "y": 50 },
  "fontSize": 24,
  "color": "#ffffff",
  "opacity": 0.8
}
Image Overlay

json
Copy code
{
  "type": "image",
  "url": "https://example.com/logo.png",
  "position": { "x": 100, "y": 50 },
  "width": 150,
  "height": 50,
  "opacity": 0.7
}
🧠 Real-Time Events (Socket.IO)
Event	Description
overlay_added	Emitted when a new overlay is created
overlay_updated	Emitted when overlay details are updated
overlay_deleted	Emitted when overlay is removed

🧪 Testing
Use Postman or cURL to test CRUD APIs.
