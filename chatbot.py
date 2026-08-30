import re
import random
import nltk

from nltk.stem import WordNetLemmatizer


# Download required NLP resources
nltk.download("punkt")
nltk.download("wordnet")


# Create lemmatizer
lemmatizer = WordNetLemmatizer()


# ---------------- INTENTS ----------------

INTENTS = {

    "greeting": {
        "patterns": [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good evening",
            "good afternoon"
        ],
        "responses": [
            "Hello! 👋 I'm your AI Career Guidance Assistant.",
            "Hi! 👋 Let's explore the right career path for you.",
            "Hey! 😊 How can I help you with your career?"
        ]
    },


    "career": {
        "patterns": [
            "career",
            "career path",
            "job",
            "profession",
            "career options",
            "career choices"
        ],
        "responses": [
            "I can help you explore different career paths based on your skills and interests.",
            "There are many career paths in technology, data, AI, software development and cybersecurity."
        ]
    },


    "skills": {
        "patterns": [
            "skill",
            "skills",
            "required skills",
            "what should i learn",
            "what skills do i need",
            "skills required"
        ],
        "responses": [
            "Tell me your current skills and I can help identify the skills you should learn next.",
            "Different careers require different skills. I can help you find the required skills."
        ]
    },


    "recommendation": {
        "patterns": [
            "recommend",
            "recommendation",
            "recommendations",
            "suggest",
            "suggestion",
            "guide",
            "which career",
            "best career"
        ],
        "responses": [
            "Sure! I can recommend careers based on your skills and interests.",
            "Absolutely! Let's find careers that match your profile."
        ]
    },


    "salary": {
        "patterns": [
            "salary",
            "pay",
            "income",
            "earn",
            "salary range",
            "package"
        ],
        "responses": [
            "Salary depends on skills, experience, location and company. I can show estimated salary ranges for different careers."
        ]
    },


    "trends": {
        "patterns": [
            "trend",
            "trends",
            "future",
            "demand",
            "growing career",
            "future career",
            "job market"
        ],
        "responses": [
            "AI, Machine Learning, Data Science, Cyber Security, Cloud Computing and DevOps are important technology career areas."
        ]
    },


    "thanks": {
        "patterns": [
            "thanks",
            "thank you",
            "thank",
            "appreciate it"
        ],
        "responses": [
            "You're welcome! 😊",
            "Glad I could help! 🎯",
            "Anytime! Best of luck with your career journey! 🚀"
        ]
    },


    "goodbye": {
        "patterns": [
            "bye",
            "goodbye",
            "see you",
            "exit",
            "quit"
        ],
        "responses": [
            "Goodbye! 👋 Best of luck with your career journey!",
            "See you! 🚀 Keep learning and growing!"
        ]
    }
}


# ---------------- TEXT PREPROCESSING ----------------

def preprocess_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    # Split text into words
    words = text.split()

    # Lemmatization
    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

    return words


# ---------------- INTENT CLASSIFICATION ----------------

def classify_intent(user_input):

    processed_input = preprocess_text(
        user_input
    )

    best_intent = None
    best_score = 0

    for intent, data in INTENTS.items():

        score = 0

        for pattern in data["patterns"]:

            pattern_words = preprocess_text(
                pattern
            )

            # Count matching words
            for word in pattern_words:

                if word in processed_input:
                    score += 1

        if score > best_score:

            best_score = score
            best_intent = intent

    if best_intent is None:
        return "unknown"

    return best_intent


# ---------------- RESPONSE GENERATION ----------------

def get_response(user_input):

    intent = classify_intent(
        user_input
    )

    if intent in INTENTS:

        responses = INTENTS[intent]["responses"]

        return random.choice(
            responses
        )

    return (
        "I'm not sure I understood that. 🤔 "
        "Try asking me about careers, skills, "
        "salary, trends, or recommendations."
    )
