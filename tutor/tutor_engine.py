# tutor/tutor_engine.py
# Core logic for generating personalized tutor responses

from prompt.tutor_prompt import generate_tutor_prompt
# Correct import (folder name is `prompt`, not `prompts`)

def tutor_engine(question, user_profile):
    # Generate personalized prompt based on user level

    prompt = generate_tutor_prompt(
        question=question,
        user_level=user_profile["level"]
    )

    # Mock LLM response (replace with real LLM later)
    response = f"[Tutor Response for {user_profile['level']} learner] {question}"

    return response
