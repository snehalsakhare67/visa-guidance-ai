# 🌍 AI Immigration Assistant

AI-powered web app that simplifies visa requirements and application steps using **ScaleDown prompt compression + Groq LLM (free)**.

Users enter country, visa type, and profile → the app generates clear, structured visa guidance.

---

## 🚀 Features
- Compresses prompts using **ScaleDown API**
- Generates AI responses using **Groq (free)**
- Clean structured output:
  - Eligibility  
  - Documents  
  - Steps  
  - Processing Time  
  - Tips  
- Simple Flask interface  
- Portfolio-ready project  

---

## 🛠 Tech Stack
Python, Flask, HTML/CSS, ScaleDown API, Groq API, dotenv

---

## 🔑 Setup

### 1. Clone repository
```bash
git clone https://github.com/your-username/immigration-assistant.git
cd immigration-assistant
2. Install dependencies
pip install -r requirements.txt

3. Add API keys

Create a .env file in the root folder:

SCALEDOWN_API_KEY=your_key
GROQ_API_KEY=your_key

▶️ Run the app
python app.py


Open in browser:

http://127.0.0.1:5000

🧪 Sample Input
Country: Canada  
Visa Type: Student  
Profile: Indian student


Output → clean structured visa guidance.

🧠 How It Works

User input → prompt compressed via ScaleDown → sent to Groq → AI generates visa guidance → displayed in UI.