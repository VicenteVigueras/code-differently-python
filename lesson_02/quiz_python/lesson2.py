class Lesson2:
    def run():
        quiz_questions = Lesson2.make_quiz_questions()
        if not quiz_questions:
            print("No quiz questions found.")
            return
        printer = QuizPrinter()
        printer.print_quiz(quiz_questions)