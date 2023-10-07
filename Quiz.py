import random

# Define a list of questions and answers
questions = [
    {
        "question": "How many countries are there in asia ?",
        "answer": "48"
    },
    {
        "question": "Which planet is known as the Dwarf Planet?",
        "answer": "Pluto"
        
    },
    {
        "question": "How many States in India?",
        "answer": "28"
    }
]

# Function to shuffle the questions
def shuffle_questions(questions):
    random.shuffle(questions)

# Function to take the quiz
def take_quiz(questions):
    shuffle_questions(questions)
    score = 0

    for q in questions:
        print(q["question"])
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == q["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")
    
    print(f"You got {score}/{len(questions)} questions correct.")

# Main function
if __name__ == "__main__":
    print("Welcome to the Quiz App!\n")
    take_quiz(questions)
