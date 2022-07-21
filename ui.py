from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas()
        self.canvas.config(bg='white', height=300, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        self.quiz_text = self.canvas.create_text(
            150,
            150,
            width=200,
            text='Yoojin',
            font=('Ariel', 20, 'italic'))

        self.score = Label(text=f'Score: {quiz_brain.score}', bg=THEME_COLOR, fg='white')
        self.score.grid(row=0, column=1)

        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, bd=0, command=self.click_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=self.false_img, highlightthickness=0, bd=0, command=self.click_false)
        self.false_button.grid(row=2, column=1)

        self.quiz_up()
        self.window.mainloop()

    def quiz_up(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.quiz_up)

