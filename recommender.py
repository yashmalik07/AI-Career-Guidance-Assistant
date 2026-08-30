from career_data import CAREER_DATA


def recommend_careers(user_skills, user_interest):

    recommendations = []

    user_skills = [skill.lower() for skill in user_skills]
    user_interest = user_interest.lower()

    for career, data in CAREER_DATA.items():

        required_skills = [
            skill.lower()
            for skill in data["skills"]
        ]

        interests = [
            interest.lower()
            for interest in data["interests"]
        ]

        # Count matching skills
        skill_matches = 0

        for skill in user_skills:
            if skill in required_skills:
                skill_matches += 1

        # Check interest match
        interest_match = (
            1 if user_interest in interests else 0
        )

        # Calculate skill score
        total_skills = len(required_skills)

        skill_score = (
            skill_matches / total_skills
        ) * 100

        # Add extra points for matching interest
        final_score = skill_score + (
            interest_match * 20
        )

        # Maximum score = 100
        if final_score > 100:
            final_score = 100

        recommendations.append({
            "career": career,
            "score": round(final_score, 2),
            "matched_skills": skill_matches,
            "description": data["description"],
            "required_skills": data["skills"],
            "salary": data["salary"],
            "demand": data["demand"]
        })

    # Highest score first
    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Return top 3 careers
    return recommendations[:3]
