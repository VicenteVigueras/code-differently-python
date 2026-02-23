from typing import Optional

class QuizQuestion:
    _question_number: int
    _question: str
    _correct_answer: Optional[str] = None
    
    def __init__(self, question_number: int, question: str, correct_answer: str):
        self._question_number = question_number
        self._question = question
        self._correct_answer = correct_answer

    def get_question_number(self) -> int:
        return self._question_number
    
    def get_question_prompt(self) -> str:
        return self._question

    def get_answer(self) -> str: 
        return self._correct_answer if self._correct_answer is not None else ''
    
    def set_answer(self, answer: Optional[str]) -> None:
        self._correct_answer = answer

    def prompt_for_answer(self, require_answer = False) -> None: 
        response: Optional[str] = None

        if response is not None:
            print("Value not accepted, try again.\n")

        if response.upper() == 'S':
            self.set_answer(None) 
            return

    
