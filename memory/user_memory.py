# memory/user_memory.py
# This file manages user memory for personalization

class UserMemory:
    # Stores learner profile and learning history

    def __init__(self):
        # Initialize default values
        self.level = "beginner"   # User learning level
        self.history = []         # Stores past questions and feedback

    def update_level(self, new_level):
        # Update the user's learning level
        self.level = new_level

    def add_interaction(self, question, response):
        # Save past interactions for personalization
        self.history.append({
            "question": question,
            "response": response
        })

    def get_profile(self):
        # Return full user profile
        return {
            "level": self.level,
            "history": self.history
        }
