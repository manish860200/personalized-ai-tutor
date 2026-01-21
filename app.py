# app.py
# Entry point for Personalized AI Tutor system

from memory.user_memory import UserMemory
from tutor.tutor_engine import tutor_engine

if __name__ == "__main__":

    # Create user memory instance
    user_memory = UserMemory()

    # User asks a question
    user_question = "What is Machine Learning?"

    # Get current user profile
    profile = user_memory.get_profile()

    # Generate tutor response
    tutor_response = tutor_engine(user_question, profile)

    # Save interaction to memory
    user_memory.add_interaction(user_question, tutor_response)

    # Print output
    print("User Level:", profile["level"])
    print("Question:", user_question)
    print("Tutor Response:", tutor_response)

    # Simulate learning progress
    user_memory.update_level("intermediate")

    print("\nUpdated User Profile:")
    print(user_memory.get_profile())
