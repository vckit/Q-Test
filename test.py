import random

# Define the questions, answer options, and correct answers for the Easy level computer science test.
easy_computer_science_test = {
    "question1": {
        "question": "What does HTML stand for?",
        "options": ["A) Hyper Text Markup Language", "B) High Technology Modern Language", "C) Hyperlink and Text Markup Language"],
        "correct_answer": "A) Hyper Text Markup Language"
    },
    "question2": {
        "question": "Which programming language is known for its use in web development and is often used on the client-side?",
        "options": ["A) Python", "B) JavaScript", "C) C++"],
        "correct_answer": "B) JavaScript"
    },
    "question3": {
        "question": "What is the main function of an operating system?",
        "options": ["A) To format hard drives", "B) To provide a user interface", "C) To manage computer hardware and software resources"],
        "correct_answer": "C) To manage computer hardware and software resources"
    },
    "question4": {
        "question": "What is a database used for?",
        "options": ["A) Storing and retrieving data", "B) Playing video games", "C) Sending emails"],
        "correct_answer": "A) Storing and retrieving data"
    },
    "question5": {
        "question": "Which data structure follows the Last-In-First-Out (LIFO) principle?",
        "options": ["A) Queue", "B) Stack", "C) Linked List"],
        "correct_answer": "B) Stack"
    },
    "question6": {
        "question": "What does CPU stand for?",
        "options": ["A) Central Processing Unit", "B) Computer Power Unit", "C) Control Processing Unit"],
        "correct_answer": "A) Central Processing Unit"
    },
    "question7": {
        "question": "Which of the following is a high-level programming language?",
        "options": ["A) Assembly language", "B) Java", "C) Machine language"],
        "correct_answer": "B) Java"
    },
    "question8": {
        "question": "What does URL stand for?",
        "options": ["A) Uniform Resource Locator", "B) Universal Reference Language", "C) United Resource Library"],
        "correct_answer": "A) Uniform Resource Locator"
    },
    "question9": {
        "question": "Which protocol is used for secure communication over the Internet?",
        "options": ["A) HTTP", "B) FTP", "C) HTTPS"],
        "correct_answer": "C) HTTPS"
    },
    "question10": {
        "question": "What does IDE stand for in the context of software development?",
        "options": ["A) Integrated Development Environment", "B) Interactive Design Environment", "C) Internet Development Engine"],
        "correct_answer": "A) Integrated Development Environment"
    },
    "question11": {
        "question": "Which company developed the Python programming language?",
        "options": ["A) Microsoft", "B) Google", "C) Guido van Rossum"],
        "correct_answer": "C) Guido van Rossum"
    },
    "question12": {
        "question": "What is the file extension for a Python source code file?",
        "options": ["A) .exe", "B) .txt", "C) .py"],
        "correct_answer": "C) .py"
    },
}

medium_computer_science_test = {
    "question1": {
        "question": "What is the purpose of an if-else statement in programming?",
        "options": [
            "A) To create a loop",
            "B) To define a function",
            "C) To make decisions in the code"
        ],
        "correct_answer": "C) To make decisions in the code"
    },
    "question2": {
        "question": "What does the acronym 'SQL' stand for in the context of databases?",
        "options": [
            "A) Structured Query Language",
            "B) Simple Query Language",
            "C) System Query Language"
        ],
        "correct_answer": "A) Structured Query Language"
    },
    "question3": {
        "question": "In object-oriented programming, what is encapsulation?",
        "options": [
            "A) A type of loop",
            "B) A way to package data and methods into a single unit",
            "C) A form of inheritance"
        ],
        "correct_answer": "B) A way to package data and methods into a single unit"
    },
    "question4": {
        "question": "What is the primary purpose of a constructor in a class?",
        "options": [
            "A) To destroy objects",
            "B) To initialize object properties",
            "C) To create class variables"
        ],
        "correct_answer": "B) To initialize object properties"
    },
    "question5": {
        "question": "What data structure uses the First-In-First-Out (FIFO) principle?",
        "options": [
            "A) Queue",
            "B) Stack",
            "C) Linked List"
        ],
        "correct_answer": "A) Queue"
    },
    "question6": {
        "question": "Which programming language is often used for scientific and numerical computing?",
        "options": [
            "A) Python",
            "B) JavaScript",
            "C) Ruby"
        ],
        "correct_answer": "A) Python"
    },
    "question7": {
        "question": "What is the primary function of the 'elif' statement in Python?",
        "options": [
            "A) To create a new variable",
            "B) To handle exceptions",
            "C) To add more conditions after an 'if' statement"
        ],
        "correct_answer": "C) To add more conditions after an 'if' statement"
    },
    "question8": {
        "question": "What is the term for a variable that is accessible throughout an entire program?",
        "options": [
            "A) Local variable",
            "B) Global variable",
            "C) Private variable"
        ],
        "correct_answer": "B) Global variable"
    },
    "question9": {
        "question": "Which sorting algorithm has an average-case time complexity of O(n log n)?",
        "options": [
            "A) Bubble Sort",
            "B) Quick Sort",
            "C) Insertion Sort"
        ],
        "correct_answer": "B) Quick Sort"
    },
    "question10": {
        "question": "What is the purpose of a 'try' and 'except' block in exception handling?",
        "options": [
            "A) To skip the program",
            "B) To handle errors gracefully and prevent program crashes",
            "C) To create custom exceptions"
        ],
        "correct_answer": "B) To handle errors gracefully and prevent program crashes"
    },
}


# Function to shuffle answer options for a given question
def shuffle_options(question_data):
    options = question_data["options"][:]
    random.shuffle(options)
    return options

# Shuffle answer options for each question and store in a separate dictionary
shuffled_easy_test = {key: {"question": question_data["question"], "options": shuffle_options(question_data)}
                     for key, question_data in easy_computer_science_test.items()}

# Function to administer the test
def take_test(test):
    student_answers = {}

    print("Welcome to the Easy-level Computer Science Test!")
    print("Please enter the letter corresponding to your answer (e.g., 'A', 'B', 'C').\n")

    # Iterate through the shuffled questions
    for key, question_data in shuffled_easy_test.items():
        print(question_data["question"])
        for option in question_data["options"]:
            print(option)

        # Get the student's answer
        while True:
            student_answer = input("Your answer: ").strip().upper()
            if student_answer in ["A", "B", "C"]:
                break
            else:
                print("Invalid input. Please enter 'A', 'B', or 'C' for your answer.")

        # Store the student's answer in the dictionary
        student_answers[key] = student_answer

    return student_answers

# Administer the test
student_answers = take_test(shuffled_easy_test)

# Calculate the number of correct answers
correct_count = 0
total_questions = len(easy_computer_science_test)

for key, question_data in easy_computer_science_test.items():
    correct_answer = question_data["correct_answer"]
    student_answer = student_answers[key]

    if student_answer == correct_answer:
        correct_count += 1

# Calculate and display the results
correct_count = 0
total_questions = len(easy_computer_science_test)

for question_key, question_data in easy_computer_science_test.items():
    correct_answer = question_data["correct_answer"]
    student_answer = student_answers[question_key]

    print("\nQuestion:", question_data["question"])
    print("Your Answer:", student_answer)
    print("Correct Answer:", correct_answer)

    if student_answer == correct_answer.split(")")[0]:
        correct_count += 1

score = (correct_count / total_questions) * 100

print(f"\nYou answered {correct_count} out of {total_questions} questions correctly.")
print(f"Your score: {score:.2f}%")
