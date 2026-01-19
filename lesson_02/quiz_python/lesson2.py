from codedifferently_instructional import AnswerChoice
from codedifferently_instructional import MultipleChoiceQuestion
from codedifferently_instructional import QuizPrinter
from codedifferently_instructional import QuizQuestion

class Lesson2:
    
    @staticmethod
    def run() -> None:
        quiz_questions = Lesson2.make_quiz_questions()
        if not quiz_questions:
            raise ValueError("Quiz questions cannot be null")
        printer = QuizPrinter()
        printer.print_quiz(quiz_questions)

    @staticmethod
    def make_quiz_questions() -> list[QuizQuestion]:
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
        return MultipleChoiceQuestion(
            0, 
            "What is the main purpose of version control?", 
                {
                AnswerChoice.A: "To make backups of files",
                AnswerChoice.B: "To keep a record of changes over time",
                AnswerChoice.C: "To delete unnecessary files",
                AnswerChoice.D: "To run code more efficiently"
                }, 
            AnswerChoice.B
        )
         
    @staticmethod
    def __make_question_1() -> QuizQuestion:
        return MultipleChoiceQuestion(
            1, 
            "What is a fork in Git?", 
                {
                AnswerChoice.A: "A duplicate copy of a repository that you own and modify",
                AnswerChoice.B: "A temporary backup of the code",
                AnswerChoice.C: "A tool for merging branches",
                AnswerChoice.D: "A way to delete a repository"
                }, 
            AnswerChoice.A
        )
    
    @staticmethod
    def __make_question_2() -> QuizQuestion:
        return MultipleChoiceQuestion(
            2, 
            "Which of the following is NOT part of the basic Git workflow?", 
                {
                AnswerChoice.A: "Pull the latest changes",
                AnswerChoice.B: "Commit changes locally",
                AnswerChoice.C: "Push changes to the server",
                AnswerChoice.D: "Write code directly in GitHub"
                }, 
            AnswerChoice.D
        )
    
    @staticmethod
    def __make_question_3() -> QuizQuestion:
        return MultipleChoiceQuestion(
            3, 
            "What command is used to combine changes from different branches?", 
                {
                AnswerChoice.A: "git commit",
                AnswerChoice.B: "git merge",
                AnswerChoice.C: "git branch",
                AnswerChoice.D: "git pull"
                }, 
            AnswerChoice.B
        )
    
    @staticmethod
    def __make_question_4() -> QuizQuestion:
        return MultipleChoiceQuestion(
            4, 
            "Which IDE is being used in the class?", 
                {
                AnswerChoice.A: "Eclipse",
                AnswerChoice.B: "IntelliJ IDEA",
                AnswerChoice.C: "NetBeans",
                AnswerChoice.D: "VS Code"
                }, 
            AnswerChoice.D
        )
         
    @staticmethod
    def __make_question_5() -> QuizQuestion:
        return MultipleChoiceQuestion(
            5, 
            "What feature allows developers to work from the same pre-configured environment in VS Code?", 
                {
                AnswerChoice.A: "Extensions",
                AnswerChoice.B: "Debugger",
                AnswerChoice.C: "Dev Containers",
                AnswerChoice.D: "Source Control"
                }, 
            AnswerChoice.C
        )

    @staticmethod
    def __make_question_6() -> QuizQuestion:
        return MultipleChoiceQuestion(
            6, 
            "What is NOT a reason for using an IDE?", 
                {
                AnswerChoice.A: "Editing and refactoring code",
                AnswerChoice.B: "Browsing code",
                AnswerChoice.C: "Playing music",
                AnswerChoice.D: "Managing source control"
                }, 
            AnswerChoice.C
        )

    @staticmethod
    def __make_question_7() -> QuizQuestion:
        return MultipleChoiceQuestion(
            7, 
            "What is the command to list files in the current directory?", 
                {
                AnswerChoice.A: "pwd",
                AnswerChoice.B: "ls",
                AnswerChoice.C: "cd",
                AnswerChoice.D: "mkdir"
                }, 
            AnswerChoice.B
        )

    @staticmethod
    def __make_question_8() -> QuizQuestion:
        return MultipleChoiceQuestion(
            8, 
            "Which command is used to change directories in the terminal?", 
                {
                AnswerChoice.A: "pwd",
                AnswerChoice.B: "ls",
                AnswerChoice.C: "cd",
                AnswerChoice.D: "mkdir"
                }, 
            AnswerChoice.C
            )

    @staticmethod
    def __make_question_9() -> QuizQuestion:
        return MultipleChoiceQuestion(
            9, 
            "What does the command `chmod` do?", 
                {
                AnswerChoice.A: "Change file or directory permissions",
                AnswerChoice.B: "List files in a directory",
                AnswerChoice.C: "Remove a file or directory",
                AnswerChoice.D: "Copy a file or directory"
                }, 
            AnswerChoice.A
        )
      
    @staticmethod
    def __make_question_10() -> QuizQuestion:
        return MultipleChoiceQuestion(
            10, 
            "What is the shortcut for getting to the Mac terminal?", 
                {
                AnswerChoice.A: "⌘ + Shift + T",
                AnswerChoice.B: '⌘ + Spacebar, then type "terminal"',
                AnswerChoice.C: "⌘ + Q",
                AnswerChoice.D: '⌘ + S, then type "terminal"'
                }, 
            AnswerChoice.B
        )

if __name__ == "__main__":
    Lesson2().run()
