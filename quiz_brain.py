class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.q_list = q_list
    def still_question(self):
        if self.question_number < len(self.q_list):
            return True
        else:
            return False
    def next_question(self):
        self.question_number += 1
        current_question = self.q_list[self.question_number]
        user_answer = input(f"Q.{self.question_number}:{current_question.text} (True/False)?")
        self.check_answer(user_answer , current_question.ans)
    def check_answer(self , user_answer , correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"you got it you score is {self.score}")
        else:
            print("thats wrong")
        print(f"your correct answer  is {correct_answer}")
        print(f"{self.score}/{self.question_number}")

        