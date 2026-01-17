from enum import Enum

class AnswerChoice(Enum):
    UNANSWERED = "UNANSWERED"
    A = "A"
    B = "B"
    C = "C"
    D = "D"

class MultipleChoiceQuestion: 
        def __init__(self, question_number, question, choices, answer):
            self.question_number = question_number  
            self.question = question  
            self.choices = choices
            self.answer = answer

        def get_answer(self):
            return self.answer


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
            Lesson2.__make_question_0(),
            Lesson2.__make_question_1(),
            Lesson2.__make_question_2(),
            Lesson2.__make_question_3(),
            Lesson2.__make_question_4(),
            Lesson2.__make_question_5(),
            Lesson2.__make_question_6(),
            Lesson2.__make_question_7(),
            Lesson2.__make_question_8(),
            Lesson2.__make_question_9(),
            Lesson2.__make_question_10(),
        ]
    
    @staticmethod
    def __make_question_0():
        question = "What is the main purpose of version control?"
        choices = {
            "A": "To make backups of files",
            "B": "To keep a record of changes over time",
            "C": "To delete unnecessary files",
            "D": "To run code more efficiently"
        }
        answer = AnswerChoice.B
        question_0 = MultipleChoiceQuestion(0, question, choices, answer)
        return question_0
    
    @staticmethod
    def __make_question_1():
        question = "What is a fork in Git?"
        choices = {
            "A": "A duplicate copy of a repository that you own and modify",
            "B": "A temporary backup of the code",
            "C": "A tool for merging branches",
            "D": "A way to delete a repository"
        }
        answer = AnswerChoice.A
        return MultipleChoiceQuestion(1, question, choices, answer)
    
    @staticmethod
    def __make_question_2():
        question = "Which of the following is NOT part of the basic Git workflow?"
        choices = {
            "A": "Pull the latest changes",
            "B": "Commit changes locally",
            "C": "Push changes to the server",
            "D": "Write code directly in GitHub"
        }
        answer = AnswerChoice.D
        return MultipleChoiceQuestion(2, question, choices, answer)
    
    @staticmethod
    def __make_question_3():
        question = "What command is used to combine changes from different branches?"
        choices = {
            "A": "git commit",
            "B": "git merge",
            "C": "git branch",
            "D": "git pull"
        }
        answer = AnswerChoice.B
        return MultipleChoiceQuestion(3, question, choices, answer)
    
    @staticmethod
    def __make_question_4():
        question = "Which IDE is being used in the class?"
        choices = {
            "A": "Eclipse",
            "B": "IntelliJ IDEA",
            "C": "NetBeans",
            "D": "VS Code"
        }
        answer = AnswerChoice.D
        question_0 = MultipleChoiceQuestion(4, question, choices, answer)
        return question_0
    
    @staticmethod
    def __make_question_5():
        question = "What feature allows developers to work from the same pre-configured environment in VS Code?"
        choices = {
            "A": "Extensions",
            "B": "Debugger",
            "C": "Dev Containers",
            "D": "Source Control"
        }
        answer = AnswerChoice.C
        question_0 = MultipleChoiceQuestion(5, question, choices, answer)
        return question_0

    @staticmethod
    def __make_question_6():
        question = "What is NOT a reason for using an IDE?"
        choices = {
            "A": "Editing and refactoring code",
            "B": "Browsing code",
            "C": "Playing music",
            "D": "Managing source control"
        }
        answer = AnswerChoice.C
        return MultipleChoiceQuestion(6, question, choices, answer)

    @staticmethod
    def __make_question_7():
        question = "What is the command to list files in the current directory?"
        choices = {
            "A": "pwd",
            "B": "ls",
            "C": "cd",
            "D": "mkdir"
        }
        answer = AnswerChoice.B
        return MultipleChoiceQuestion(7, question, choices, answer)

    @staticmethod
    def __make_question_8():
        question = "Which command is used to change directories in the terminal?"
        choices = {
            "A": "pwd",
            "B": "ls",
            "C": "cd",
            "D": "mkdir"
        }
        answer = AnswerChoice.C
        return MultipleChoiceQuestion(8, question, choices, answer)

    @staticmethod
    def __make_question_9():
        question = "What does the command `chmod` do?"
        choices = {
            "A": "Change file or directory permissions",
            "B": "List files in a directory",
            "C": "Remove a file or directory",
            "D": "Copy a file or directory"
        }
        answer = AnswerChoice.A
        return MultipleChoiceQuestion(9, question, choices, answer)
      
    @staticmethod
    def __make_question_10():
        question = "What is the shortcut for getting to the Mac terminal?"
        choices = {
            "A": "⌘ + Shift + T",
            "B": '⌘ + Spacebar, then type "terminal"',
            "C": "⌘ + Q",
            "D": '⌘ + S, then type "terminal"'
        }
        answer = AnswerChoice.A
        return MultipleChoiceQuestion(10, question, choices, answer)

if __name__ == "__main__":
    Lesson2().run()
