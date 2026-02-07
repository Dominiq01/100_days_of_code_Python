import html
from data import get_questions
from Day_34.quizler_app.question_model import Question

class QuizBrain:

    def __init__(self):
        self.question_number = 0
        self.score = 0
        self.question_list = []
        self.current_question = None
        self.quiz_init()

    def quiz_init(self):
        question_data = get_questions()
        for question in question_data:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.question_list.append(new_question)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False



