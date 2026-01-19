from collections.abc import Iterable
from .quiz_question import QuizQuestion
from .answer_choice import AnswerChoice
from .multiple_choice_question import MultipleChoiceQuestion

class QuizPrinter:
    def print_quiz(self, quiz_questions: Iterable[QuizQuestion]) -> None:
        for question in quiz_questions:
            self.print_question(question)

    def print_question(self, question: QuizQuestion, print_answer: bool = True) -> None:
        print(f'Question {question.get_question_number()}: {question.get_question_prompt()}')
        if (isinstance(question, MultipleChoiceQuestion)):
            print("placeholder")
        if not print_answer:
            return


#   printQuizQuestion(question: QuizQuestion, printAnswer: boolean = true): void {
#     console.log(`Question ${question.getQuestionNumber()}: ${question.getQuestionPrompt()}`);

#     if (question instanceof MultipleChoiceQuizQuestion) {
#       this.printPossibleAnswers(question);
#     }

#     if (!printAnswer) {
#       return;
#     }

#     console.log(`>> Your answer: ${question.getAnswer()}`);
#     console.log();
#   }

#   private printPossibleAnswers(question: MultipleChoiceQuizQuestion): void {
#     for (const option of Object.values(AnswerChoice)) {
#       if (option === AnswerChoice.UNANSWERED) {
#         continue;
#       }
#       const answer = question.getAnswerForOption(option);
#       if (answer === null || answer === undefined) {
#         continue;
#       }
#       console.log(`${option}: ${answer}`);
#     }
#   }
# }
