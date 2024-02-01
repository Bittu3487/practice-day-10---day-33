from question_module import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_question = Question(question_text , question_ans)
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
while quiz.still_question():
    quiz.next_question()