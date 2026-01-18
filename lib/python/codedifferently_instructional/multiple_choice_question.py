class MultipleChoiceQuestion: 
        def __init__(self, question_number, question, choices, answer):
            self.question_number = question_number  
            self.question = question  
            self.choices = choices
            self.answer = answer

        def get_answer(self):
            return self.answer
