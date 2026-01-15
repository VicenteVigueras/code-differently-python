from enum import Enum

class AnswerChoice(Enum):
    UNANSWERED = "UNANSWERED",
    A = "A",
    B = "B",
    C = "C",
    D = "D",


class MultipleChoiceQuestion: 
        def __init__(self, question_number, question, choices, answer):
            self.question_number = question_number  
            self.question = question  
            print(f"{question_number}. {question}\n")
            self.choices = choices
            print(f"{choices}")
            self.answer = answer
            print(f"answer: {answer}")


class Lesson2:
    @staticmethod
    def run():
        quiz_questions = Lesson2.make_quiz_questions()
        if not quiz_questions:
            print("No quiz questions found.")
            return

    @staticmethod
    def make_quiz_questions():
        return [
            Lesson2.make_question_0()
        ]
    
    @staticmethod
    def make_question_0():
        question = "What is the main purpose of version control?"
        choices = {
            "A": "To make backups of files",
            "B": "To keep a record of changes over time",
            "C": "To delete unnecessary files",
            "D": "To run code more efficiently"
        }
        answer = "A"
        question_0 = MultipleChoiceQuestion(0, question, choices, answer)
        return question_0
    
Lesson2().run()