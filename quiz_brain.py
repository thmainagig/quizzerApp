class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.score = 0
        self.question_number = 0
        self.current_question = None

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number +=1
        return f'Q.{self.question_number}: {self.current_question.text} (True/False):'

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.title() == correct_answer.title():
            self.score += 1
            return True
        else:
            return False


