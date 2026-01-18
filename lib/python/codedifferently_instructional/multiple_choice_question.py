class MultipleChoiceQuestion: 
    _question_number: int
    _question: str
    _choices: dict[str, str]
    _answer: str

    def __init__(self, question_number: int, question: str, choices: dict[str, str], answer: str):
        self._question_number = question_number  
        self._question = question  
        self._choices = choices
        self._answer = answer

    def get_answer(self) -> str:
        return self._answer