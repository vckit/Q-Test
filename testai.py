import random

easy_computer_science_test = {
    "question1": {
        "question": "What does HTML stand for?",
        "options": ["Hyper Text Markup Language", "High Technology Modern Language", "Hyperlink and Text Markup Language"],
        "correct_answer_index": 0
    },
    "question2": {
        "question": "Which programming language is known for its use in web development and is often used on the client-side?",
        "options": ["Python", "JavaScript", "C++"],
        "correct_answer_index": 1
    },
    "question3": {
        "question": "What is the main function of an operating system?",
        "options": ["To format hard drives", "To provide a user interface", "To manage computer hardware and software resources"],
        "correct_answer_index": 2
    },
    "question4": {
        "question": "What is a database used for?",
        "options": ["Storing and retrieving data", "Playing video games", "Sending emails"],
        "correct_answer_index": 0
    },
    "question5": {
        "question": "Which data structure follows the Last-In-First-Out (LIFO) principle?",
        "options": ["Queue", "Stack", "Linked List"],
        "correct_answer_index": 1
    },
    "question6": {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Power Unit", "Control Processing Unit"],
        "correct_answer_index": 0
    },
    "question7": {
        "question": "Which of the following is a high-level programming language?",
        "options": ["Assembly language", "Java", "Machine language"],
        "correct_answer_index": 1
    },
    "question8": {
        "question": "What does URL stand for?",
        "options": ["Uniform Resource Locator", "Universal Reference Language", "United Resource Library"],
        "correct_answer_index": 0
    },
    "question9": {
        "question": "Which protocol is used for secure communication over the Internet?",
        "options": ["HTTP", "FTP", "HTTPS"],
        "correct_answer_index": 2
    },
    "question10": {
        "question": "What does IDE stand for in the context of software development?",
        "options": ["Integrated Development Environment", "Interactive Design Environment", "Internet Development Engine"],
        "correct_answer_index": 0
    },
}

medium_computer_science_test = {
    "question1": {"question": "What is the purpose of an if-else statement in programming?",
                  "options": ["To create a loop", "To define a function", "To make decisions in the code"],
                  "correct_answer_index": 2},
    "question2": {"question": "What does the acronym 'SQL' stand for in the context of databases?",
                  "options": ["Structured Query Language", "Simple Query Language", "System Query Language"],
                  "correct_answer_index": 0},
    "question3": {"question": "In object-oriented programming, what is encapsulation?",
                  "options": ["A type of loop", "A way to package data and methods into a single unit", "A form of inheritance"],
                  "correct_answer_index": 1},
    "question4": {"question": "What is the primary purpose of a constructor in a class?",
                  "options": ["To destroy objects", "To initialize object properties", "To create class variables"],
                  "correct_answer_index": 1},
    "question5": {"question": "What data structure uses the First-In-First-Out (FIFO) principle?",
                  "options": ["Queue", "Stack", "Linked List"],
                  "correct_answer_index": 0},
    "question6": {"question": "Which programming language is often used for scientific and numerical computing?",
                  "options": ["Python", "JavaScript", "Ruby"],
                  "correct_answer_index": 0},
    "question7": {"question": "What is the primary function of the 'elif' statement in Python?",
                  "options": ["To create a new variable", "To handle exceptions", "To add more conditions after an 'if' statement"],
                  "correct_answer_index": 2},
    "question8": {"question": "What is the term for a variable that is accessible throughout an entire program?",
                  "options": ["Local variable", "Global variable", "Private variable"],
                  "correct_answer_index": 1},
    "question9": {"question": "Which sorting algorithm has an average-case time complexity of O(n log n)?",
                  "options": ["Bubble Sort", "Quick Sort", "Insertion Sort"],
                  "correct_answer_index": 1},
    "question10": {"question": "What is the purpose of a 'try' and 'except' block in exception handling?",
                   "options": ["To skip the program", "To handle errors gracefully and prevent program crashes", "To create custom exceptions"],
                   "correct_answer_index": 1}
}

complex_computer_science_test = {
    "question1": {"question": "What is the time complexity of a binary search algorithm in the worst case?",
                  "options": ["O(n)", "O(log n)", "O(n log n)"],
                  "correct_answer_index": 1},
    "question2": {"question": "Which sorting algorithm has an average-case time complexity of O(n log n)?",
                  "options": ["Bubble Sort", "Quick Sort", "Insertion Sort"],
                  "correct_answer_index": 1},
    "question3": {"question": "What is the purpose of a hash function in data structures?",
                  "options": ["To sort data efficiently", "To encrypt data", "To map data to a fixed-size array"],
                  "correct_answer_index": 2},
    "question4": {"question": "What is the role of an API (Application Programming Interface) in software development?",
                  "options": ["To provide a graphical user interface", "To define a set of rules for communication between software components", "To create web applications"],
                  "correct_answer_index": 1},
    "question5": {"question": "In object-oriented programming, what is encapsulation?",
                  "options": ["The process of converting code into machine code", "The process of hiding the internal details of an object and restricting access to its data", "The process of writing test cases for code"],
                  "correct_answer_index": 1},
    "question6": {"question": "Which data structure is typically used to implement a LIFO (Last-In-First-Out) behavior?",
                  "options": ["Queue", "Stack", "Linked List"],
                  "correct_answer_index": 1},
    "question7": {"question": "What is the difference between TCP and UDP in networking?",
                  "options": ["TCP is connectionless, while UDP is connection-oriented", "TCP provides error-checking and guarantees the order of data delivery, while UDP does not", "TCP is faster than UDP"],
                  "correct_answer_index": 1},
    "question8": {"question": "What is recursion in programming?",
                  "options": ["A loop that repeats a specific number of times", "A function that calls itself in its own definition", "A method of code optimization"],
                  "correct_answer_index": 1},
    "question9": {"question": "What is the process of dynamic memory allocation in C++?",
                  "options": ["Automatic memory management", "Manual memory management using operators like new and delete", "Memory allocation during compile time"],
                  "correct_answer_index": 1},
    "question10": {"question": "What is the primary function of a CDN (Content Delivery Network) in web development?",
                   "options": ["To store backups of a website", "To reduce website load times by caching content across a network of servers", "To generate website traffic"],
                   "correct_answer_index": 1}
}

def shuffle_options(question_data):
    options = question_data["options"][:]
    random.shuffle(options)
    return options

shuffled_easy_test = {
    key: {
        "question": question_data["question"],
        "options": shuffle_options(question_data),
        "difficulty": "easy"
    }
    for key, question_data in easy_computer_science_test.items()
}

shuffled_medium_test = {
    key: {
        "question": question_data["question"],
        "options": shuffle_options(question_data),
        "difficulty": "easy"
    }
    for key, question_data in medium_computer_science_test.items()
}

shuffled_complex_test = {
    key: {
        "question": question_data["question"],
        "options": shuffle_options(question_data),
        "difficulty": "easy"
    }
    for key, question_data in complex_computer_science_test.items()
}

def take_test(test):
    student_answers = {}

    print("Welcome to the Computer Science Test!")
    print("Please enter the number corresponding to your answer (e.g., '1', '2', '3').\n")

    for question_number, (key, question_data) in enumerate(test.items(), start=1):
        # Check if difficulty exists, if not default to "Unknown"
        difficulty = question_data.get('difficulty', 'Unknown').capitalize()
        print(f"Question {question_number}: {question_data['question']} (Difficulty: {difficulty})")
        # Rest of the function remains the same...

        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

        while True:
            student_answer = input("Your answer: ").strip()
            if student_answer.isdigit():
                option_number = int(student_answer)
                if 1 <= option_number <= len(question_data["options"]):
                    break
            print("Invalid input. Please enter a valid number corresponding to your answer.")

        student_answers[key] = option_number - 1

    return student_answers

student_answers_easy = take_test(shuffled_easy_test)

#student_answers_intermediate = take_test(shuffled_medium_test)

#student_answers_complex = take_test(shuffled_complex_test)

def calculate_and_display_results(test_name, student_answers, test_data):
    correct_count = 0
    total_questions = len(test_data)

    for question_key, question_data in test_data.items():
        correct_answer_index = question_data["correct_answer_index"]
        student_answer_index = student_answers[question_key]

        print("\nQuestion:", question_data["question"])
        print("Your Answer:", question_data["options"][student_answer_index])
        print("Correct Answer:", question_data["options"][correct_answer_index])

        if student_answer_index == correct_answer_index:
            correct_count += 1

    score = (correct_count / total_questions) * 100

    print(f"\nYou answered {correct_count} out of {total_questions} questions correctly in the {test_name} test.")
    print(f"Your score: {score:.2f}%")

    return correct_count, score  # Ensure to return the score and correct count


#calculate_and_display_results("Easy", student_answers_easy, easy_computer_science_test)

#calculate_and_display_results("Intermediate", student_answers_intermediate, medium_computer_science_test)

#calculate_and_display_results("Complex", student_answers_complex, complex_computer_science_test)

def generate_trial_test(easy_test, medium_test, complex_test, num_questions=10):
    trial_test = {}

    # Define the percentage of questions for each difficulty level
    easy_percentage = 0.70  # 70%
    medium_percentage = 0.25  # 25%
    complex_percentage = 0.05  # 05%

    # Calculate the number of questions from each difficulty level
    num_easy = int(num_questions * easy_percentage)
    num_medium = int(num_questions * medium_percentage)
    num_complex = num_questions - (num_easy + num_medium)

    # Randomly select questions from each level
    selected_easy = random.sample(list(easy_test.items()), num_easy)
    selected_medium = random.sample(list(medium_test.items()), num_medium)
    selected_complex = random.sample(list(complex_test.items()), num_complex)

    # Add difficulty labels
    labeled_easy = [(q, 'easy') for q in selected_easy]
    labeled_medium = [(q, 'medium') for q in selected_medium]
    labeled_complex = [(q, 'complex') for q in selected_complex]

    # Combine selected questions and shuffle them
    selected_questions = labeled_easy + labeled_medium + labeled_complex
    random.shuffle(selected_questions)

    # Format the trial test in the desired format
    for i, (question, difficulty) in enumerate(selected_questions):
        trial_test[f"question{i + 1}"] = {
            "question": question[1]["question"],  # access nested "question" key
            "options": question[1]["options"],  # add "options" key to the final_test question
            "correct_answer_index": question[1]["correct_answer_index"],  # add "correct_answer_index" key
            "difficulty": difficulty
        }
    return trial_test

trail_test = generate_trial_test(easy_computer_science_test, medium_computer_science_test, complex_computer_science_test, num_questions=10)
trail_student_answers = take_test(trail_test)
calculate_and_display_results("Trail", trail_student_answers, trail_test)

def generate_final_test(easy_test, medium_test, complex_test, num_questions=10):
    final_test = {}

    num_easy = num_questions // 3
    num_medium = num_questions // 3
    num_complex = num_questions - (num_easy + num_medium)

    selected_easy = random.sample(list(easy_test.items()), num_easy)
    selected_medium = random.sample(list(medium_test.items()), num_medium)
    selected_complex = random.sample(list(complex_test.items()), num_complex)

    labeled_easy = [(q, 'easy') for q in selected_easy]
    labeled_medium = [(q, 'medium') for q in selected_medium]
    labeled_complex = [(q, 'complex') for q in selected_complex]

    selected_questions = labeled_easy + labeled_medium + labeled_complex
    random.shuffle(selected_questions)

    for i, (question, difficulty) in enumerate(selected_questions):
        final_test[f"question{i + 1}"] = {
            "question": question[1]["question"],  # access nested "question" key
            "options": question[1]["options"],  # add "options" key to the final_test question
            "correct_answer_index": question[1]["correct_answer_index"],  # add "correct_answer_index" key
            "difficulty": difficulty
        }

    return final_test
final_test = generate_final_test(easy_computer_science_test, medium_computer_science_test, complex_computer_science_test, num_questions=10)
final_student_answers = take_test(final_test)
calculate_and_display_results("Final", final_student_answers, final_test)

