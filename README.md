# SentriCam: Smart CCTV with Person-aware Alerts

**Overview**  
SentriCam is an intelligent CCTV system that uses real-time face detection and recognition to classify visitors into three categories: Resident, Frequent Visitor, or Unknown. Based on classification, it triggers context-aware alerts — silent logs for Residents, SMS notifications for Frequent Visitors, and urgent call alerts for Unknowns — all demonstrated using a laptop camera.

---

**Problem Statement**  
Traditional CCTV systems are passive and flood users with irrelevant alerts or miss important intrusions. SentriCam provides proactive, privacy-focused surveillance with real-time, person-aware notifications to improve security and reduce false alarms.

---

**Key Features**  
- Real-time face detection and recognition  
- Visitor classification: Resident, Frequent Visitor, Unknown  
- Context-sensitive alerts:  
  - **Resident:** Silent logging  
  - **Frequent Visitor:** SMS notification (Twilio)  
  - **Unknown:** Urgent call alert (Twilio)  
- Privacy-respecting local encrypted database  
- Simple UI with live camera feed, alert logs, and enrollment  
- Scalable for homes, offices, and institutions  

---

**Architecture**  
Camera Input
↓
Face Detection (OpenCV/MediaPipe)
↓
Face Recognition & Embeddings (FaceNet/dlib)
↓
Decision Engine (classification & alert logic)
↓
Notification Module (silent log / SMS / call)


---

**Technology Stack**  
- Python 3.9+  
- OpenCV, dlib, face_recognition  
- Flask (web UI) / PyQT (desktop UI)  
- SQLite (local encrypted DB)  
- Twilio API for SMS and phone calls  
- Firebase (optional push notifications)  

---

**Setup Instructions**

1. **Clone the repository:**
   git clone https://github.com/yourusername/sentricam.git
   cd sentricam

2. **Install dependencies:**
   pip install opencv-python face-recognition dlib flask twilio sqlite3

3. **Project folder structure:**
   /SentriCam
   ├── app.py
   ├── setup_database.py
   ├── add_test_log.py
   ├── known_faces/
   ├── database/
   ├── static/
   ├── templates/

4. **Initialize the database:**
   python setup_database.py

5. **Enroll known faces:**
   - Place 5–10 clear images per person in a subfolder under `/known_faces/` (e.g., `/known_faces/John/`).

6. **Configure Twilio:**
   - Add your Twilio `account_sid`, `auth_token`, and phone numbers in a `.env` file (do not commit this file).

7. **Run the app:**
   python app.py

8. **Test the logs page:**
   - (Optional) Add a test log with `python add_test_log.py`
   - Visit `http://127.0.0.1:5000/logs` to see logs.

Open `http://127.0.0.1:5000` in a browser to access the UI.

---

**Usage & Demo Flow**

1. Start the app — camera stream and live detection begin.  
2. Show Resident face — logged silently without alert.  
3. Show Frequent Visitor face (e.g., yourself) — SMS alert sent.  
4. Show Unknown visitor — triggers urgent phone call alert.  
5. Review alert logs and camera feed live via UI.

---

**Screenshots**

![Live Detection View](static/live_demo.png)  
*Live face detection with bounding boxes and labels*

![Alert Log View](static/log_example.png)  
*Alert log showing visitor classification and timestamps*

---

**Benefits**

- Intelligent, context-aware alert classification  
- Privacy-focused: stores encrypted data locally  
- Reduced false alerts, faster response to real threats  
- Easy enrollment and flexible for small to large-scale setups  

---

**Team**  
- Abhiram N Udupa 
- Anujith S Nayak  
- Team "Solutionauts" @ AceAthon

---

**Future Enhancements**

- Deploy on Raspberry Pi for edge CCTV integration  
- Support multi-camera networks and cloud dashboards  
- Add behavior analytics (loitering, suspicious activity)  
- Blockchain-based alert log verification for tamper-proof history  
- Mobile app for real-time monitoring and alerts  

---

**Acknowledgements**  
OpenCV, dlib, face_recognition, Twilio, Flask, Firebase.

---
