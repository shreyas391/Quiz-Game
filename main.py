from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data:
    text = questions["text"] 
    answer = questions["answer"]
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz \nYour final score is {quiz.score}/{quiz.question_number}\n")