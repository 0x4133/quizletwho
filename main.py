import random
import time

def display_loading_bar(duration):
    for i in range(duration):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

def get_question_answers():
    question = input("Enter a question (or press Enter to finish): ")
    if not question:
        return None

    answers = []
    correct_answer = None
    for i in range(4):
        answer = input(f"Enter answer {i+1} (or press Enter to skip): ")
        if answer:
            answers.append(answer)
            if not correct_answer:
                is_correct = input("Is this the correct answer? (y/n): ")
                if is_correct.lower() == "y":
                    correct_answer = answer

    if len(answers) < 2:
        print("Error: At least 2 answers are required for each question.")
        return get_question_answers()

    if not correct_answer:
        print("Error: Please specify the correct answer.")
        return get_question_answers()

    return {"question": question, "answers": answers, "correct_answer": correct_answer, "is_true_false": len(answers) == 2}

def create_quiz():
    print("Welcome to the Quiz Creator!")
    print("Enter your questions and answers below.")
    print("For true/false questions, provide only 2 answers.")
    print()

    questions = []
    while True:
        question_answers = get_question_answers()
        if not question_answers:
            break
        questions.append(question_answers)

    print("\nCreating quiz", end="")
    display_loading_bar(3)

    print("\nShuffling questions and answers", end="")
    display_loading_bar(3)

    shuffled_questions = []
    answer_key = []
    for question in questions:
        if question["is_true_false"]:
            shuffled_questions.append(question)
            answer_key.append({"question": question["question"], "correct_answer": question["correct_answer"]})
        else:
            shuffled_question = {
                "question": question["question"],
                "answers": question["answers"].copy(),
                "is_true_false": False
            }
            random.shuffle(shuffled_question["answers"])
            shuffled_questions.append(shuffled_question)
            answer_key.append({"question": question["question"], "correct_answer": question["correct_answer"]})

    random.shuffle(shuffled_questions)

    print("\nSaving quiz to file", end="")
    display_loading_bar(3)

    with open("quiz.txt", "w") as file:
        for i, question in enumerate(shuffled_questions, start=1):
            file.write(f"Question {i}: {question['question']}\n")
            for j, answer in enumerate(question["answers"], start=1):
                file.write(f"{j}. {answer}\n")
            file.write("\n")

    print("\nSaving answer key to file", end="")
    display_loading_bar(3)

    with open("answer_key.txt", "w") as file:
        for i, answer in enumerate(answer_key, start=1):
            file.write(f"Question {i}: {answer['question']}\n")
            file.write(f"Correct Answer: {answer['correct_answer']}\n")
            file.write("\n")

    print("\nQuiz and answer key saved successfully!")
    print("Thank you for using the Quiz Creator!")

if __name__ == "__main__":
    create_quiz()