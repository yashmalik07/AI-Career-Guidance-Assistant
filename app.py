import streamlit as st

from recommender import recommend_careers
from chatbot import get_response


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Career Guidance Assistant",
    page_icon="🧭",
    layout="wide"
)


# ---------------- HEADER ----------------

st.title("🧭 AI Career Guidance Assistant")

st.write(
    "Find suitable career paths based on your "
    "skills, interests, and goals."
)

st.divider()


# ---------------- SIDEBAR ----------------

st.sidebar.title("👤 Student Profile")

name = st.sidebar.text_input(
    "Your Name"
)

education = st.sidebar.selectbox(
    "Education",
    [
        "B.Tech",
        "BCA",
        "B.Sc",
        "BBA",
        "BA",
        "Other"
    ]
)

skills = st.sidebar.multiselect(
    "Select Your Skills",
    [
        "Python",
        "SQL",
        "Excel",
        "Statistics",
        "Machine Learning",
        "Java",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Linux",
        "Docker",
        "Kubernetes",
        "AWS",
        "Networking",
        "Cryptography",
        "Data Visualization",
        "Communication",
        "Market Research"
    ]
)

interest = st.sidebar.selectbox(
    "Area of Interest",
    [
        "Data",
        "Artificial Intelligence",
        "Machine Learning",
        "Software Development",
        "Web Development",
        "Cyber Security",
        "Cloud Computing",
        "DevOps",
        "Business",
        "Technology",
        "Product Management"
    ]
)


# ---------------- RECOMMENDATION ----------------

st.header("🎯 Career Recommendation")

if st.button(
    "Get Career Recommendations",
    use_container_width=True
):

    if len(skills) == 0:

        st.warning(
            "Please select at least one skill."
        )

    else:

        recommendations = recommend_careers(
            skills,
            interest
        )

        st.success(
            f"Career recommendations for {name if name else 'you'}"
        )

        for index, career in enumerate(
            recommendations,
            start=1
        ):

            st.subheader(
                f"{index}. {career['career']}"
            )

            st.write(
                career["description"]
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Match Score",
                    f"{career['score']}%"
                )

            with col2:
                st.metric(
                    "Skills Matched",
                    career["matched_skills"]
                )

            with col3:
                st.metric(
                    "Demand",
                    career["demand"]
                )

            st.write(
                f"💰 **Estimated Salary:** "
                f"{career['salary']}"
            )

            st.write(
                "🔧 **Required Skills:**"
            )

            st.write(
                ", ".join(
                    career["required_skills"]
                )
            )

            st.divider()


# ---------------- CHATBOT ----------------

st.header("🤖 Career Assistant Chatbot")

st.write(
    "Ask questions about careers, skills, "
    "recommendations, or career paths."
)


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )


user_input = st.chat_input(
    "Ask your career question..."
)


if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)


    response = get_response(
        user_input
    )


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "🧭 AI Career Guidance Assistant | "
    "Python + NLP + Recommendation System"
)
