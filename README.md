# 📧 Email Drafting Agent – GenAI Hackathon Mini Challenge #2

A smart AI-powered email drafting assistant that converts bullet-point input into a polished professional email. Built using OpenAI GPT-3.5 and deployed via Flask + ngrok, this agent is fully functional on GenAI AgentOS and accessible via REST API for live testing.

---

## 🧠 How It Works

You provide key points like:

- Recipient name
- Purpose
- Key details
- Closing line

And the agent returns:

- ✅ Subject line  
- ✅ Natural greeting  
- ✅ Structured body  
- ✅ Professional closing  

---

## 🧩 Tech Stack

- Python 3.10+
- OpenAI API (gpt-3.5-turbo)
- Flask + Flask-CORS
- GenAI AgentOS
- ngrok (for live endpoint)

---

## 🚀 Local Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/email-drafting-agent-genai.git
cd email-drafting-agent-genai

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate       # Linux/macOS
# OR
venv\Scripts\activate        # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Set Your OpenAI API Key

Option 1: Edit `.env` file

```env
OPENAI_API_KEY=sk-xxxx...
```

Option 2: Set it in your code (not recommended for production)

```python
client = OpenAI(api_key="sk-xxxx")
```

---

## 🧪 Run Locally

```bash
python app.py
```

Output:

```
✅ Email Drafting Agent is live!
```

Now your Flask server is running at:  
**http://localhost:5000/draft-email**

---

## 🌍 Deploy with ngrok (Bonus Points)

Install ngrok:  
[https://ngrok.com/download](https://ngrok.com/download)

Run it:

```bash
ngrok http 5000
```

You’ll get a link like:

```
Forwarding → https://xxxx-xx-xx-xx.ngrok-free.app
```

🎉 Your API is now public! Share this link in your submission.

---

## 📬 How to Use (API Example)

```bash
curl -X POST https://<your-ngrok-url>/draft-email \
     -H "Content-Type: application/json" \
     -d '{
           "bullets": "- Recipient: Dr. Mehta\n- Purpose: Schedule a follow-up meeting\n- Mention last meeting date (June 30)\n- Ask for availability next week\n- Closing: Looking forward to your response"
         }'
```

Response:

```json
{
  "email": "Subject: Follow-Up Meeting Request\n\nDear Dr. Mehta, ..."
}
```

---

## 🧠 Prompt Logic

The model is guided by this system message:

> “You are a professional email drafting assistant. Based on the bullet points below, generate a complete email. Include subject, greeting, body, and closing.”

---

## 📂 File Structure

```
email_drafting_agent/
├── app.py                # Flask backend with OpenAI integration
├── README.md             # You're reading this!
├── requirements.txt      # Python dependencies
└── (optional) .env       # Store API keys here
```

---

## ✅ Submission Checklist

| Requirement                             | Status ✅ |
|----------------------------------------|----------|
| AgentOS-registered functional agent     | ✅        |
| Produces polished email from bullets    | ✅        |
| Professional tone maintained            | ✅        |
| Public GitHub with clear documentation  | ✅        |
| ngrok deployment live (bonus)           | ✅        |

---

