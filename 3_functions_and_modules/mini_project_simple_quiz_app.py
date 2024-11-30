def quiz():
    questions = [
        {"question": "What is 2 + 2?", "options": [4, 5, 6], "answer": 4},
        {"question": "What is 3 * 3?", "options": [6, 7, 9], "answer": 9},
    ]
    score = 0

    for q in questions:
        print(q["question"])
        print("Options:", q["options"])
        answer = int(input("Your answer: "))
        if answer == q["answer"]:
            score += 1

    print(f"Your score: {score}/{len(questions)}")


quiz()
