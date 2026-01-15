class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        curr_num = self.question_number
        question = self.question_list[curr_num]
        user_input = input(f"Q.{curr_num + 1} {question.text} (True/False)?: ")
        self.check_answer(user_input, question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_input, answer):
        if user_input.lower() == answer.lower():
            self.score += 1
            print("   You got it right!")
        else:
            print("   You got it wrong!")

        print(f"   The correct answer was {answer}.")
        print(f"   Your current score is: {self.score}/{self.question_number + 1}.")
        self.question_number += 1

