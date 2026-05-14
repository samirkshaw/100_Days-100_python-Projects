class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}. {question.text} (True/False): ").strip().capitalize()
        if answer == question.answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! Correct answer was: {question.answer}\n")

    def final_score(self):
        print(f"Game over! Final score: {self.score}/{self.question_number}")