from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_banks = []

for ques in question_data:
    question_banks.append(Question(ques['text'], ques['answer']))

quiz = QuizBrain(question_banks)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz")
quiz.final_scrore()
