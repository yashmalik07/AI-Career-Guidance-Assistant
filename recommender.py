from career_data import CAREER_DATA


def recommend_careers(user_skills, user_interest):

    recommendations = []

    user_skills = [skill.lower() for skill in user_skills]
    user_interest = user_interest.lower()

    for career, data in CAREER_DATA.items():

        required_skills = [
            skill.lower() for skill in data["skills"]
        ]

        interests = [
            interest.lower() for interest in data["interests"]
        ]

        skill_matches = 0

        for skill in user_skills:
            if skill in required_skills:
                skill_matches += 1

        interest_match = 1 if user_interest in interests else 0

        total_skills = len(required_skills)

        skill_score = (
            skill_matches / total_skills
        ) * 100

        final_score = skill_score + (interest_match * 20)

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

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return recommendations[:3]
