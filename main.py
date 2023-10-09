import random

# Define the questions and their answer options
questions = {
    "1. What is the capital of France?": ["Paris", "London", "Berlin"],
    "2. Which planet is known as the Red Planet?": ["Mars", "Venus", "Jupiter"],
    "3. What is the largest mammal on Earth?": ["Elephant", "Blue Whale", "Giraffe"],
    "4. What gas do plants absorb from the atmosphere?": ["Oxygen", "Carbon Dioxide", "Nitrogen"],
    "5. Who wrote the play 'Romeo and Juliet'?": ["Charles Dickens", "William Shakespeare", "Jane Austen"],
    "6. What is the chemical symbol for gold?": ["Go", "Gd", "Au"],
    "7. Which gas do humans breathe out when they exhale?": ["Oxygen", "Nitrogen", "Carbon Dioxide"],
    "8. What is the largest planet in our solar system?": ["Earth", "Mars", "Jupiter"],
    "9. Who is known as the 'Father of Modern Physics'?": ["Albert Einstein", "Isaac Newton", "Galileo Galilei"],
    "10. What is the chemical symbol for water?": ["H2O", "CO2", "O2"],
    "11. Which country is famous for the Great Wall?": ["Japan", "China", "India"],
    "12. What is the smallest prime number?": ["0", "1", "2"]
}

# Create a dictionary to store correct answers
correct_answers = {
    "1. What is the capital of France?": "Paris",
    "2. Which planet is known as the Red Planet?": "Mars",
    "3. What is the largest mammal on Earth?": "Blue Whale",
    "4. What gas do plants absorb from the atmosphere?": "Carbon Dioxide",
    "5. Who wrote the play 'Romeo and Juliet'?": "William Shakespeare",
    "6. What is the chemical symbol for gold?": "Au",
    "7. Which gas do humans breathe out when they exhale?": "Carbon Dioxide",
    "8. What is the largest planet in our solar system?": "Jupiter",
    "9. Who is known as the 'Father of Modern Physics'?": "Albert Einstein",
    "10. What is the chemical symbol for water?": "H2O",
    "11. Which country is famous for the Great Wall?": "China",
    "12. What is the smallest prime number?": "2"
}

# Shuffle answer options for each question
for question, options in questions.items():
    random.shuffle(options)

# Create a dictionary to store student answers
student_answers = {}

# Display the questions and collect student answers
for question, options in questions.items():
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    while True:
        user_answer = input("Enter the answer (1, 2, or 3): ")
        if user_answer in ['1', '2', '3']:
            student_answers[question] = options[int(user_answer) - 1]
            break
        else:
            print("Invalid input. Please enter '1', '2', or '3'.")

# Calculate and display the results
correct_count = 0
total_questions = len(questions)

for question, student_answer in student_answers.items():
    correct_answer = correct_answers[question]
    print(f"Question: {question}")
    print(f"Your answer: {student_answer}")
    print(f"Correct answer: {correct_answer}")
    if student_answer == correct_answer:
        correct_count += 1

score = (correct_count / total_questions) * 100

print(f"\nYou answered {correct_count} out of {total_questions} questions correctly.")
print(f"Your score: {score:.2f}%")
