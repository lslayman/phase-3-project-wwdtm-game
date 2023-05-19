from trivia_api import *

class QuestionModel:
    def __init__(self, question: str, correct_answer: str, choices: list):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices

class QuizMechanics:
    
    def __init__(self, questions):
        self.question_num = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def next_question(self):
        self.current_question = self.questions[self.question_num]
        self.question_num += 1
        question_text = self.current_question.question_text
        question_options = self.current_question.choices
        return f"""
Q.{self.question_num}: {question_text}
a.{question_options[0]}
b.{question_options[1]}
c.{question_options[2]}
d.{question_options[3]}
"""

    def check_correct(self, user_answer):
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def show_score(self):
        wrong = self.question_num - self.score
        score_percent = int(self.score / self.question_num * 100)
        return (self.score, wrong, score_percent)
    
class QuizUI:
    def __init__(self, quiz_mechanics: QuizMechanics):
        self.quiz = quiz_mechanics
    
        #Stores user answer
        #self.user_answer = StringVar()

    def display_question(self):
        question_text = self.quiz.next_question()
        return question_text
    
    def display_result(self):
        correct, incorrect, final_score = self.quiz.show_score()

        correct = f"Correct: {correct}"
        print(correct)
        incorrect = f"Wrong: {incorrect}"
        print(incorrect)

        final_score = f"Score: {final_score}%"
        print(final_score)