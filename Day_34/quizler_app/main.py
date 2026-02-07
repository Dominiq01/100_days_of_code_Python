from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface


quiz = QuizBrain()
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
