THEME_COLOR = '#375362'

import tkinter
import html
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title('Quizzler App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_card = tkinter.Label(text=f'Score: 0', bg=THEME_COLOR, fg='white')
        self.score_card.grid(column=1, row=0)

        self.canvas = tkinter.Canvas(width=300, height=250, bg='white')
        self.quiz_text = self.canvas.create_text(150, 125, width=270, text='Some Question', fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=2, columnspan=2, pady=50)

        self.correct_button = tkinter.Button(text='✔', command=self.true_pressed)
        self.correct_button.grid(column=0, row=4)

        self.wrong_button = tkinter.Button(text='❌', command=self.false_pressed)
        self.wrong_button.grid(column=1, row=4)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        if self.quiz.still_has_question():
            self.canvas.config(bg='white')
            self.score_card.config(text=f'Score: {self.quiz.score}')
            q_text = html.unescape(self.quiz.next_question())
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.config(bg='white')
            self.canvas.itemconfig(self.quiz_text, text=f'You have completed. Score: {self.quiz.score}/{len(self.quiz.question_list)}')
            self.correct_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

