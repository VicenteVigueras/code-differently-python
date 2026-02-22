from typing import Optional

class QuizQuestion:
    _question_number: int
    _question: str
    _correct_answer: Optional[str] = None
    
    def __init__(self, question_number, question, correct_answer):
        self._question_number = question_number
        self._question = question
        self._correct_answer = correct_answer

    def get_question_number(self) -> int:
        return self._question_number
    
    def get_question_prompt(self) -> str:
        return self._question

    # not convinced with this impl - will most likely change
    # works though
    def get_answer(self) -> str: 
        if hasattr(self._correct_answer, 'name'):
            return self._correct_answer.name
        return str(self._correct_answer or "") 
    
    def set_answer(self, answer: Optional[str]) -> None:
        self._correct_answer = answer

"""
TODO: Implement the rest of the functionality in python
"""             

#   public promptForAnswer(scanner: Scanner, requireAnswer = false): void {
#     let response: string | null = null;

#     do {
#       // If a response was given but not accepted, announce that.
#       if (response !== null) {
#         console.log("Value not accepted, try again.\n");
#       }

#       // Get a response.
#       const prompt = `>> Your answer ${requireAnswer ? "(required)" : "(or 's' to skip)"}: `;
#       process.stdout.write(prompt);
#       response = scanner.next().trim();

#       // If the user wants to skip, let them.
#       if (!requireAnswer && response.toUpperCase() === "S") {
#         this.setAnswer(null);
#         return;
#       }
#     } while (requireAnswer && (response === '' || response.toUpperCase() === 'S'));

#     // Set the question answer.
#     this.setAnswer(response);
#   }

