from codedifferently_instructional import AnswerChoice
from codedifferently_instructional import MultipleChoiceQuestion
from codedifferently_instructional import QuizPrinter
from codedifferently_instructional import QuizQuestion

class Lesson2:
    
    @staticmethod
    def run():
        quiz_questions = Lesson2.make_quiz_questions()
        if not quiz_questions:
            print("No quiz questions found.")
            return # Replace with Error handling in the future
        printer = QuizPrinter()
        printer.print_quiz(quiz_questions)

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
            Lesson2.__make_question_10()
        ]
    
    @staticmethod
    def __make_question_0() -> QuizQuestion:
        question = "What is the main purpose of version control?"
        choices = {
            AnswerChoice.A: "To make backups of files",
            AnswerChoice.B: "To keep a record of changes over time",
            AnswerChoice.C: "To delete unnecessary files",
            AnswerChoice.D: "To run code more efficiently"
        }
        answer = AnswerChoice.B
        question_0 = MultipleChoiceQuestion(0, question, choices, answer)
        return question_0
    
    @staticmethod
    def __make_question_1() -> QuizQuestion:
        question = "What is a fork in Git?"
        choices = {
            AnswerChoice.A: "A duplicate copy of a repository that you own and modify",
            AnswerChoice.B: "A temporary backup of the code",
            AnswerChoice.C: "A tool for merging branches",
            AnswerChoice.D: "A way to delete a repository"
        }
        answer = AnswerChoice.A
        return MultipleChoiceQuestion(1, question, choices, answer)
    
    @staticmethod
    def __make_question_2() -> QuizQuestion:
        question = "Which of the following is NOT part of the basic Git workflow?"
        choices = {
            AnswerChoice.A: "Pull the latest changes",
            AnswerChoice.B: "Commit changes locally",
            AnswerChoice.C: "Push changes to the server",
            AnswerChoice.D: "Write code directly in GitHub"
        }
        answer = AnswerChoice.D
        return MultipleChoiceQuestion(2, question, choices, answer)
    
    @staticmethod
    def __make_question_3() -> QuizQuestion:
        question = "What command is used to combine changes from different branches?"
        choices = {
            AnswerChoice.A: "git commit",
            AnswerChoice.B: "git merge",
            AnswerChoice.C: "git branch",
            AnswerChoice.D: "git pull"
        }
        answer = AnswerChoice.B
        return MultipleChoiceQuestion(3, question, choices, answer)
    
    @staticmethod
    def __make_question_4() -> QuizQuestion:
        question = "Which IDE is being used in the class?"
        choices = {
            AnswerChoice.A: "Eclipse",
            AnswerChoice.B: "IntelliJ IDEA",
            AnswerChoice.C: "NetBeans",
            AnswerChoice.D: "VS Code"
        }
        answer = AnswerChoice.D
        question_0 = MultipleChoiceQuestion(4, question, choices, answer)
        return question_0
    
    @staticmethod
    def __make_question_5() -> QuizQuestion:
        question = "What feature allows developers to work from the same pre-configured environment in VS Code?"
        choices = {
            AnswerChoice.A: "Extensions",
            AnswerChoice.B: "Debugger",
            AnswerChoice.C: "Dev Containers",
            AnswerChoice.D: "Source Control"
        }
        answer = AnswerChoice.C
        question_0 = MultipleChoiceQuestion(5, question, choices, answer)
        return question_0

    @staticmethod
    def __make_question_6() -> QuizQuestion:
        question = "What is NOT a reason for using an IDE?"
        choices = {
            AnswerChoice.A: "Editing and refactoring code",
            AnswerChoice.B: "Browsing code",
            AnswerChoice.C: "Playing music",
            AnswerChoice.D: "Managing source control"
        }
        answer = AnswerChoice.C
        return MultipleChoiceQuestion(6, question, choices, answer)

    @staticmethod
    def __make_question_7() -> QuizQuestion:
        question = "What is the command to list files in the current directory?"
        choices = {
            AnswerChoice.A: "pwd",
            AnswerChoice.B: "ls",
            AnswerChoice.C: "cd",
            AnswerChoice.D: "mkdir"
        }
        answer = AnswerChoice.B
        return MultipleChoiceQuestion(7, question, choices, answer)

    @staticmethod
    def __make_question_8() -> QuizQuestion:
        question = "Which command is used to change directories in the terminal?"
        choices = {
            AnswerChoice.A: "pwd",
            AnswerChoice.B: "ls",
            AnswerChoice.C: "cd",
            AnswerChoice.D: "mkdir"
        }
        answer = AnswerChoice.C
        return MultipleChoiceQuestion(8, question, choices, answer)

    @staticmethod
    def __make_question_9() -> QuizQuestion:
        question = "What does the command `chmod` do?"
        choices = {
            AnswerChoice.A: "Change file or directory permissions",
            AnswerChoice.B: "List files in a directory",
            AnswerChoice.C: "Remove a file or directory",
            AnswerChoice.D: "Copy a file or directory"
        }
        answer = AnswerChoice.A
        return MultipleChoiceQuestion(9, question, choices, answer)
      
    @staticmethod
    def __make_question_10() -> QuizQuestion:
        question = "What is the shortcut for getting to the Mac terminal?"
        choices = {
            AnswerChoice.A: "⌘ + Shift + T",
            AnswerChoice.B: '⌘ + Spacebar, then type "terminal"',
            AnswerChoice.C: "⌘ + Q",
            AnswerChoice.D: '⌘ + S, then type "terminal"'
        }
        answer = AnswerChoice.B
        return MultipleChoiceQuestion(10, question, choices, answer)

if __name__ == "__main__":
    Lesson2().run()
