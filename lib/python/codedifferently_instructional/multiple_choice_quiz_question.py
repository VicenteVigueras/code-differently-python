from .quiz_question import QuizQuestion
from .answer_choice import AnswerChoice
from typing import Dict, Optional

class MultipleChoiceQuizQuestion(QuizQuestion): 
    _answers_by_option: Dict[AnswerChoice, str]

    def __init__(self, 
                 question_number: int, 
                 question: str, 
                 answer_options: Dict[AnswerChoice, str], 
                 correct_answer: AnswerChoice
                 ):
        super().__init__(question_number, question, correct_answer)
        self._answers_by_option = answer_options
    

    def get_answer_choices(self) -> set[AnswerChoice]: 
        return set(self._answers_by_option.keys())
    
    def get_answer_for_option(self, option: AnswerChoice) -> Optional[str]:
        return self._answers_by_option.get(option)
    
    def set_answer(self, answer: Optional[AnswerChoice]) -> None:
        super().set_answer(answer if answer is not None else AnswerChoice.UNANSWERED)

    def prompt_for_answer(self) -> None: 
        response: Optional[str] = None
        answer: Optional[AnswerChoice] = None

        while(answer is None or answer not in self._answers_by_option):
            if response is not None:
                print("Value not accepted, try again.\n")

            response = input(">> Your answer (or 's' to skip): ")
            answer = response

            if response.upper() == 'S':
                self.set_answer(None) 
                return
            
            if response in ['A', 'B', 'C', 'D']:
                answer = AnswerChoice[response]
        
        self.set_answer(answer)