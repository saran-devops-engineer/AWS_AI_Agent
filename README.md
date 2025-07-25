
# 🤖 AI-Powered AWS Automation Assistant

This project is an AI-powered chatbot that helps you interact with AWS using **natural language** (like "Show me unused Elastic IPs"). It uses an **LLM (via OpenRouter)** to detect intent and run real AWS operations using **Boto3**.

---

## 📦 Features

- 🧠 Understands natural language using LLaMA 3 via OpenRouter
- ⚙️ Detects AWS-specific intents:
  - List unused Elastic IPs
  - List running EC2 instances
  - Describe all EIPs
- 📡 Executes real AWS tasks using Boto3
- 💬 Simple web frontend for user interaction
- 🔁 Falls back to generic LLM response if no AWS-related intent is found

---

## 🗂️ Project Structure

```
aws-assistant/
│
├── backend/
│   ├── app.py                 # Flask API entry point
│   ├── llm_client.py          # Handles communication with LLM (OpenRouter)
│   ├── aws_tasks.py           # AWS operations via Boto3
│   └── intent_router.py       # Intent detection and routing
│
├── frontend/
│   ├── app_ui.py              # Flask frontend app (serves HTML)
│   └── static/
│       ├── script.js          # Handles user interaction & API calls
│       └── style.css          # (Optional) styling
│
└── README.md                  # You're here!
```

---

## 🛠️ Prerequisites

- Python 3.8+
- Flask
- Boto3 (`pip install boto3`)
- An OpenRouter API Key (https://openrouter.ai)
- AWS credentials (in `~/.aws/credentials` or via env vars)
- Access to AWS account with necessary permissions

---

## 🔐 Configuration

### 1. **Set OpenRouter API key**

In `llm_client.py`, replace the placeholder:

```python
headers = {
    "Authorization": "Bearer sk-...",
    ...
}
```

### 2. **AWS Credentials**

Configure your AWS credentials using:

```bash
aws configure
```

Or use environment variables:

```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
```

---

## 🚀 How to Run

### Step 1: Start the Backend API

```bash
cd backend
python app.py
```

Runs the chatbot backend at `http://localhost:5000`.

---

### Step 2: Start the Frontend App

Open a new terminal:

```bash
cd frontend
python app_ui.py
```

Runs the frontend at `http://127.0.0.1:3000`.

---

### Step 3: Use the Assistant!

1. Open browser at: `http://127.0.0.1:3000`
2. Type messages like:
   - `Show me unused EIPs`
   - `List running EC2 instances`
   - `Describe all elastic IPs`
   - `Tell me about AWS`
3. Bot will respond based on detected intent and return AWS info.

---

## 💡 How It Works

| Component       | Role                                                                 |
|----------------|----------------------------------------------------------------------|
| `llm_client.py` | Sends user messages to LLaMA 3 via OpenRouter to extract intent       |
| `intent_router.py` | Maps natural language → intent → AWS task                         |
| `aws_tasks.py`  | Uses Boto3 to run actual AWS operations (e.g., list EIPs)            |
| `app.py`        | Flask backend API to handle chat requests                            |
| `script.js`     | Sends user input to backend and displays bot replies                 |
| `app_ui.py`     | Serves HTML frontend from Flask                                      |

---

## ✅ Future Improvements

- Add support for more AWS services (e.g., S3 buckets, IAM users)
- Authentication for production use
- UI enhancements and persistent chat history

---

## 🙌 Credits

- [OpenRouter](https://openrouter.ai/) for the LLaMA-3 API
- [Flask](https://flask.palletsprojects.com/)
- [AWS Boto3](https://boto3.amazonaws.com/)

