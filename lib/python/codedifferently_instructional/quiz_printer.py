from collections.abc import Iterable
from .quiz_question import QuizQuestion
from .answer_choice import AnswerChoice
from .multiple_choice_question import MultipleChoiceQuestion

class QuizPrinter:
    def print_quiz(self, quiz_questions: Iterable[QuizQuestion]) -> None:
        print("=" * 80 + "\n")
        for question in quiz_questions:
            self.print_question(question)
        print("=" * 80)

    def print_question(self, question: QuizQuestion, print_answer: bool = True) -> None:
        print(f'Question {question.get_question_number()}: {question.get_question_prompt()}')
        if (isinstance(question, MultipleChoiceQuestion)):
            self.__print_possible_answers(question)
        
        if not print_answer:
            return
        
        print(f">> Your answer: {question.get_answer()} \n")
        

    def __print_possible_answers(self, question: MultipleChoiceQuestion) -> None:
        for option in AnswerChoice:
            if option == AnswerChoice.UNANSWERED:
                continue
            answer = question.get_answer_for_option(option)
            if answer is None:
                continue
            print(f"{option.value}: {answer}")