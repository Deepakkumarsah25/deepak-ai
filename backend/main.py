from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os

# =========================
# LOAD ENVIRONMENT
# =========================

load_dotenv()

# =========================
# FRONTEND PATH
# =========================

frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")

# =========================
# FLASK APP
# =========================

app = Flask(
    __name__,
    static_folder=frontend_path,
    static_url_path=""
)

CORS(app)

# =========================
# GEMINI SETUP
# =========================

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
# FRONTEND ROUTES
# =========================

@app.route("/")
def home():
    return send_from_directory(frontend_path, "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(frontend_path, path)

# =========================
# CHAT ROUTE
# =========================

@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        prompt = data.get("prompt", "").strip()

        prompt_lower = prompt.lower()

        # =========================
        # CREATOR
        # =========================

        if any(word in prompt_lower for word in [
            "kisne banaya",
            "who made you",
            "who created you",
            "tumko kisne banaya",
            "creator",
            "owner"
        ]):

            return jsonify({
                "response": "Mujhe Deepak Kumar ne banaya hai."
            })

        # =========================
        # SKILLS
        # =========================

        elif any(word in prompt_lower for word in [
            "skill",
            "skills",
            "what skills",
            "kya aata hai",
            "technology",
            "tech stack",
            "frontend",
            "backend",
            "programming",
            "coding skills",
            "deepak ka skill kya hai",
            "what technologies does deepak use"
        ]):

            return jsonify({
                "response": "Deepak ko HTML, CSS, JavaScript, React, Node.js, Express.js, MongoDB, Python, Flask aur Tailwind CSS aata hai."
            })

        # =========================
        # PROFESSION
        # =========================

        elif any(word in prompt_lower for word in [
            "profession",
            "job",
            "work",
            "career",
            "developer",
            "what does deepak do",
            "deepak kya karta hai",
            "is deepak a developer"
        ]):

            return jsonify({
                "response": "Deepak ek passionate Full Stack Developer hai."
            })

        # =========================
        # EDUCATION
        # =========================

        elif any(word in prompt_lower for word in [
            "education",
            "study",
            "student",
            "college",
            "degree",
            "btech",
            "qualification",
            "what is deepak studying"
        ]):

            return jsonify({
                "response": "Deepak abhi 3rd Year B.Tech Student hai."
            })

        # =========================
        # HOBBIES
        # =========================

        elif any(word in prompt_lower for word in [
            "hobby",
            "hobbies",
            "interest",
            "pasand",
            "likes",
            "what are deepak hobbies"
        ]):

            return jsonify({
                "response": "Deepak ko coding, cooking aur new technology seekhna pasand hai."
            })

        # =========================
        # EXPERIENCE
        # =========================

        elif any(word in prompt_lower for word in [
            "experience",
            "project",
            "projects",
            "portfolio",
            "Deepak is virgin or not ? ",
            "what projects has deepak built"
        ]):

            return jsonify({
                "response": "Deepak ne MERN Stack aur AI based real-world projects banaye hai."
            })

        # =========================
        # PERSONALITY
        # =========================

        elif any(word in prompt_lower for word in [
            "personality",
            "nature",
            "behavior",
            "attitude"
        ]):

            return jsonify({
                "response": "Deepak friendly, smart aur hardworking person hai."
            })

        # =========================
        # GOAL
        # =========================

        elif any(word in prompt_lower for word in [
            "goal",
            "dream",
            "future",
            "aim",
            "career goal"
        ]):

            return jsonify({
                "response": "Deepak ka goal successful software engineer banna hai."
            })

        # =========================
        # ABOUT DEEPAK
        # =========================

        elif any(word in prompt_lower for word in [
            "about deepak",
            "who is deepak",
            "tell me about deepak",
            "deepak kaun hai"
        ]):

            return jsonify({
                "response": "Deepak Kumar ek Full Stack Developer aur AI enthusiast hai jo modern web apps aur smart AI systems banata hai."
            })

        # =========================
        # GEMINI RESPONSE
        # =========================

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

        return jsonify({
            "response": reply
        })

    except Exception as e:

        return jsonify({
            "response": f"Error: {str(e)}"
        })

# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
