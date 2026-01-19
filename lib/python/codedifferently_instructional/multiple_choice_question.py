from .quiz_question import QuizQuestion
from .answer_choice import AnswerChoice
from typing import Dict

class MultipleChoiceQuestion(QuizQuestion): 
    _question_number: int
    _question: str
    _answer_choices: Dict[AnswerChoice, str]
    _answer: AnswerChoice

    def __init__(self, question_number: int, question: str, answer_choices: Dict[str, str], answer: AnswerChoice):
        super().__init__(question_number, question, answer)
        self._answer_choices = answer_choices
    
    def get_answer_for_option(self, option: AnswerChoice) -> str:
        return self._answer_choices.get(option)


 
"""
TODO: Implement the rest of the functionality in python
"""   
# import { Scanner } from './scanner.js';

# export class MultipleChoiceQuizQuestion extends QuizQuestion {
#   private answersByOption: Map<AnswerChoice, string>;

#   constructor(
#     questionNumber: number,
#     question: string,
#     answerOptions: Map<AnswerChoice, string>,
#     correctAnswer: AnswerChoice
#   ) {
#     super(questionNumber, question, correctAnswer);
#     this.answersByOption = answerOptions;
#   }

#   public getAnswerChoices(): Set<AnswerChoice> {
#     return new Set(this.answersByOption.keys());
#   }

#   public getAnswerForOption(option: AnswerChoice): string | undefined {
#     return this.answersByOption.get(option);
#   }

#   public promptForAnswer(scanner: Scanner): void {
#     let response: string | null = null;
#     let answer: AnswerChoice | null = null;

#     do {
#       // If a response was given but not accepted, announce that.
#       if (response !== null) {
#         console.log("Value not accepted, try again.\n");
#       }

#       // Get a response.
#       console.log(">> Your answer (or 's' to skip): ");
#       response = scanner.next().toUpperCase().trim();

#       // If the user wants to skip, let them.
#       if (response === 'S') {
#         this.setAnswer(null);
#         return;
#       }

#       // Try to parse the answer.
#       if (['A', 'B', 'C', 'D'].includes(response)) {
#         answer = response as AnswerChoice;
#       }
#     } while (answer === null || !this.answersByOption.has(answer));

#     // Set the question answer.
#     this.setAnswer(answer);
#   }

#   public setAnswer(answer: AnswerChoice | null): void {
#     super.setAnswer(answer ?? AnswerChoice.UNANSWERED);
#   }
# }

