#quiz

def ask_question(question, options, correct_answer):

    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    answer = input("Please enter the number of your answer: ")

    if options[int(answer) - 1] == correct_answer:
        return True
    else:
        return False


def start_quiz():
    questions = [
        {
            "question": "Who is winner of ipl 2019",
            "options": ["delhi", "Rcb", "mumbai", "chennai"],
            "correct_answer": "mumbai"
        },
        {
            "question": "Which of these is the smallest planet in our solar system?",
            "options": ["Earth", "Mars", "Mercury", "Venus"],
            "correct_answer": "Mercury"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"],
            "correct_answer": "Shakespeare"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "correct_answer": "Pacific"
        }
    ]

    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!\n")

    for question_data in questions:
        if ask_question(question_data["question"], question_data["options"], question_data["correct_answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was: {question_data['correct_answer']}\n")

    print(f"Quiz over! Your final score is {score}/{total_questions}.")


if __name__ == "__main__":
    start_quiz()