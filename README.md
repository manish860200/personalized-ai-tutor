# 🎓 Personalized AI Tutor

A Personalized AI Tutor system that adapts explanations based on the learner’s level, remembers user preferences, and improves responses using feedback-driven memory.

---

## 🚀 Project Overview

The **Personalized AI Tutor** is a GenAI-powered application designed to deliver customized learning experiences.  
It dynamically adjusts explanations based on the user's skill level and stores learning preferences using memory, enabling smarter and more relevant tutoring over time.

This project demonstrates **core GenAI concepts** such as:
- Prompt engineering
- User memory
- Adaptive responses
- Modular AI system design

---

## 🧠 Key Features

- 📌 **User Memory Management**
  - Stores learner level, interests, and feedback
- 🎯 **Adaptive Learning**
  - Adjusts explanations for beginner, intermediate, and advanced users
- 🔁 **Context-Aware Responses**
  - Uses previous interactions to improve future answers
- 🧩 **Modular Architecture**
  - Clean separation of memory, prompts, and tutor logic
- ⚙️ **Production-Ready Structure**
  - Easy to extend with LLMs, APIs, or vector databases

---

## 🗂️ Project Structure

personalized-ai-tutor/
│
├── memory/
│ └── user_memory.py # Stores and retrieves user learning data
│
├── prompt/
│ └── tutor_prompt.py # Builds personalized tutor prompts
│
├── tutor/
│ └── tutor_engine.py # Core tutoring logic
│
├── app.py # Entry point of the application
├── config.py # Configuration settings
├── requirements.txt # Project dependencies
└── README.md # Project documentation