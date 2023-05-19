from helpers import *
from db.seed import *
from trivia_api import *
#from tkinter import Tk, Canvas, StringVar, Label, Rabiobutton, Button, messagebox
from random import shuffle
import html, sys

def welcome_message():

    print("Welcome to the useless trivia game! It's quieter and lonelier than bar trivia but may allow you to finally use some of the pointless fun facts your learned while earning your Liberal Arts degree.")
    print("Before we can proceed, you must login.")

    user_status = input("Are you new here? (yes/no)L\: ").lower()

    if user_status == "yes":
        create_new_user()
    elif user_status == "no":
        welcome_returning_user()
    else:
        print("Invalid input. Please try again.")
        welcome_message()

    while True:
        display_menu()

        choice = input("Enter your selection: ")

        if choice == '1':
            quiz = start_game()
            for i in range(10):
                print(quiz.display_question())
                answer = input("Select option ")
                print(quiz.quiz.check_correct(answer))
            quiz.display_result()
            sys.exit(0)
        # elif choice == '2':
        #     display_stats(user)
        elif choice == '3':
            # quit
            break
        else:
            print("That's not a valid option. Please try again.")

def display_menu():
    print("Thank you for validating your credentials! Now, please select an option to proceed:")
    print("1. Start game")
    print("2. Display stats/achievements")
    print("3. Get the hell outta here")

def start_game():
    print("Let's get started!")

    question_container = []
    for question in question_data:
        options = []
        question_text = html.unescape(question["question"])
        correct_answer = html.unescape(question["correct_answer"])
        incorrect_answers = question["incorrect_answers"]
        for ans in incorrect_answers:
            options.append(html.unescape(ans))
        options.append(correct_answer)
        shuffle(options)
        next_question = QuestionModel(question_text, correct_answer, options)
        question_container.append(next_question)

    quiz = QuizMechanics(question_container)
    return QuizUI(quiz)

    # #select category
    # categories = [result for result in questions]
    # print(categories)

    # print("Select a category:")
    # for i, categories in enumerate(categories, start=1):
    #     print("f{i}. {categories}")

    # category_choice = input("Enter the category number: ")

    # selected_category = categories[int(category_choice) - 1]

    # #select difficulty
    # difficulty_levels = list(set(result["difficulty"] for result in questions["results"]))

    # print("Select the difficulty level: ")
    # for i, level in enumerate(difficulty_levels, start =1):
    #     print(f"{i}. {level}")

    # difficulty_choice = input("Enter the difficulty level number: ")
    # selected_difficulty = difficulty_levels[int(difficulty_choice) - 1]

    # filtered_questions = [
    #     result for result in questions["results"]
    #     if result["category"] == selected_category and result["difficulty"] == selected_difficulty
    # ]

    # return(filtered_questions)



if __name__ == '__main__':
    welcome_message()
