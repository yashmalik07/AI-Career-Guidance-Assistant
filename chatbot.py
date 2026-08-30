import re
import random

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()


INTENTS = {

    "greeting": {
        "patterns": [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good evening"
        ],
        "responses": [
            "Hello! 👋 I'm your AI Career Guidance Assistant.",
            "Hi! 👋 Let's find a suitable career path for you."
        ]
    },

    "career": {
        "patterns": [
            "career",
            "career path",
            "job",
            "profession",
            "career options"
        ],
        "responses": [
            "I can help you explore different career paths based on your skills and interests."
        ]
    },

    "skills": {
        "patterns": [
            "skills",
            "skill",
            "what should i learn",
            "required skills"
        ],
        "responses": [
            "Tell me your current skills and I'll help you identify the skills required for suitable careers."
        ]
    },

    "recommendation": {
        "patterns": [
            "recommend",
            "recommendation",
            "suggest",
            "suggestion",
            "guide",
            "which career"
        ],
        "responses": [
            "Sure! I can recommend careers based on your skills and interests."
        ]
    },

    "thanks": {
        "patterns": [
            "thanks",
            "thank you",
            "thank"
        ],
        "responses": [
            "You're welcome! 😊",
            "Glad I could help! 🎯"
        ]
    }
}


def preprocess_text(text):

    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    words = text.split()

    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

    return words


def get_response(user_input):

    processed_words = preprocess_text(user_input)

    for intent, data in INTENTS.items():

        for pattern in data["patterns"]:

            pattern_words = preprocess_text(pattern)

            if any(
                word in processed_words
                for word in pattern_words
            ):
                return random.choice(
                    data["responses"]
                )

    return (
        "I'm not sure I understood. "
        "Try asking me about careers, skills, "
        "recommendations or career paths."
    )
