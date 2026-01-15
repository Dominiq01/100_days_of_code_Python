from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User("001", "Dominik")
# user_2 = User('002', "Pablo")
# user_1.follow(user_2)
#
# print(user_1.username)
# print(user_1.following)
# print(user_2.followers)

question_bank = []

for el in question_data:
    question_bank.append(Question(el["question"], el["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("\n")
print("You've completed the quiz.")
print(f"Your final score was: {quiz_brain.score}/{len(question_bank)}")