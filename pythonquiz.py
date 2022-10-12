# a dictionary that stores the questions and answers
# have a variable that tracks the score of the user
# loop through the dictionary using the key value pairs
# display all questions to theuser and allow them to answer
# notify if right or wrong
# display final results

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "Where is Wall Street located?",
        "answer": "Manhattan"
    },
    "question4": {
        "question": "Where is Tokyo located?",
        "answer": "Japan"
    },
    "question5": {
        "question": "Where is Seoul located?",
        "answer": "South Korea"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 2
        print("Your score is: " + str(score))
    else:
        print("Wrong!")
        print("The answer is: " + value['answer'])
        print("Your score is: " + str(score))