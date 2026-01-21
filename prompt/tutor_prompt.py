# prompts/tutor_prompt.py
# This file creates a personalized prompt for the AI tutor

def generate_tutor_prompt(question, user_level):
    # Create different explanations based on learner level

    if user_level == "beginner":
        style = "Explain in very simple terms with examples."
    elif user_level == "intermediate":
        style = "Explain with some technical details."
    else:
        style = "Explain in deep technical detail."

    prompt = f"""
You are a personalized AI tutor.

Student level: {user_level}
Instruction style: {style}

Question:
{question}

Answer:
"""
    return prompt
