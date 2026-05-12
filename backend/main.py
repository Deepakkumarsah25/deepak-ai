# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# # Load .env
# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# # API KEY
# API_KEY = os.getenv("gemini_api_key")

# # Configure Gemini
# genai.configure(api_key=API_KEY)

# # MODEL
# model = genai.GenerativeModel("models/gemini-2.5-flash")

# # Home Route
# @app.route("/")
# def home():
#     return jsonify({
#         "message": "Backend is running"
#     })

# # Chat Route
# @app.route("/chat", methods=["POST"])
# def chat():
#     try:
#         data = request.get_json()

#         prompt = data.get("prompt")

#         response = model.generate_content(
#             f"""
#             You are Gyani, a virtual assistant created by Deepak Kumar.

#             Rules:
#             - If someone asks who made you, who created you, or tum ko kisne banaya hai,
#               reply only: "Mujhe Deepak Kumar ne banaya hai."

#             - Keep answers short and friendly.

#             User Question:
#             {prompt}
#             """
#         )

#         return jsonify({
#             "response": response.text
#         })

#     except Exception as e:
#         return jsonify({
#             "response": str(e)
#         })

# # Run App
# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load Environment
load_dotenv()

# Flask App
app = Flask(__name__)
CORS(app)

# Gemini Setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# =========================
# OWNER DATA
# =========================

OWNER_NAME = "Deepak Kumar"

OWNER_SKILLS = """
HTML
CSS
JavaScript
React
Node.js
Express.js
MongoDB
Python
Flask
Tailwind CSS
API Development
"""

OWNER_INFO = f"""
Name: Deepak Kumar

Profession:
Full Stack Developer

Education:
3rd Year B.Tech Student

Skills:
{OWNER_SKILLS}

Hobbies:
Cooking
Coding
Learning New Technology

Experience:
Built MERN Stack Projects

Personality:
Friendly
Smart
Hardworking

Goal:
Become Successful Software Engineer
"""

# =========================
# CHAT ROUTE
# =========================

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "").strip()
        prompt_lower = prompt.lower()

        # Fixed Custom Answers
        if "kisne banaya" in prompt_lower or "who made you" in prompt_lower or "who created you" in prompt_lower or "tumko kisne banaya" in prompt_lower or "creator" in prompt_lower:
            return jsonify({"response": "Deepak Kumar created me."})

        elif any(word in prompt_lower for word in ["skill", "skills", "what skills", "kya aata hai", "technology", "tech stack", "frontend", "backend", "programming", "coding skills", "deepak ka skill kya hai", "what technologies does deepak use"]):
            return jsonify({"response": "Deepak knows HTML, CSS, JavaScript, React, Node.js, Express.js, MongoDB, Python, Flask, and Tailwind CSS."})

        elif any(word in prompt_lower for word in ["profession", "job", "work", "career", "developer", "what does deepak do", "deepak kya karta hai", "is deepak a developer"]):
            return jsonify({"response": "Deepak is a Full Stack Developer."})

        elif any(word in prompt_lower for word in ["education", "study", "student", "college", "degree", "btech", "qualification", "what is deepak studying"]):
            return jsonify({"response": "Deepak is a 3rd year B.Tech student."})

        elif any(word in prompt_lower for word in ["hobby", "hobbies", "interest", "pasand", "likes", "what are deepak hobbies"]):
            return jsonify({"response": "Deepak enjoys coding, cooking, and learning new technologies."})

        elif any(word in prompt_lower for word in ["experience", "project", "projects", "portfolio", "what projects has deepak built"]):
            return jsonify({"response": "Deepak has built real-world MERN stack projects."})

        elif any(word in prompt_lower for word in ["personality", "nature", "behavior", "attitude"]):
            return jsonify({"response": "Deepak is friendly, smart, and hardworking."})

        elif any(word in prompt_lower for word in ["goal", "dream", "future", "aim", "career goal"]):
            return jsonify({"response": "Deepak's goal is to become a successful software engineer."})

        elif any(word in prompt_lower for word in ["about deepak", "who is deepak", "tell me about deepak", "deepak kaun hai"]):
            return jsonify({"response": "Deepak Kumar is a Full Stack Developer and AI enthusiast who builds modern web apps and smart AI systems."})

        # Gemini Fallback
        response = model.generate_content(
            f"""
You are Gyani AI assistant created by Deepak Kumar.

IMPORTANT RULES:
- Never say you are Gemini.
- Never mention Google AI.
- Talk like a friendly Indian girl.
- Reply in Hindi-English mix.
- Keep answers short and natural.
- No markdown.
- No special symbols.
- No fake answers.
- Never change owner information.

OWNER INFORMATION:
{OWNER_INFO}

If user asks about owner, use only OWNER INFORMATION.

If information is not available, say:
"Mere paas uski information nahi hai."

User Question:
{prompt}
"""
        )
        reply = response.text.strip()
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)