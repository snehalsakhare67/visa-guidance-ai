AI Immigration Assistant – Documentation

Overview
AI Immigration Assistant is a Flask web application that simplifies visa requirements and application steps.  
It uses ScaleDown API to compress prompts and Groq AI to generate structured visa guidance.

Features
- Shows eligibility requirements  
- Lists required documents  
- Provides application steps  
- Shows processing time  
- Gives helpful tips  

Tech Stack
Python  
Flask  
HTML  
CSS  
ScaleDown API  
Groq API  

How It Works
1. User enters country, visa type, and profile.
2. The prompt is compressed using ScaleDown API.
3. The compressed prompt is sent to Groq AI.
4. Groq generates visa guidance.
5. Result is displayed on the webpage.

Run the Project
1. Install dependencies  
pip install -r requirements.txt  

2. Create .env file and add keys  
SCALEDOWN_API_KEY=your_key  
GROQ_API_KEY=your_key  

3. Run app  
python app.py  

4. Open browser  
http://127.0.0.1:5000  

Sample Input
Country: Canada  
Visa Type: Student  
Profile: Indian student  

Output
The system returns:
Eligibility  
Documents  
Steps  
Processing Time  
Tips  

