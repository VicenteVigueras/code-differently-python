from typing import Dict, Optional, TypedDict
from .quiz_question import QuizQuestion
from .answer_choice import AnswerChoice
from .multiple_choice_quiz_question import MultipleChoiceQuizQuestion
# import yaml

class QuestionConfig(TypedDict):
    prompt: str
    # choices: NotRequired[Dict['AnswerChoice', str]]

class QuizConfig:
    __answers_by_provider: Dict[str,list[str]]
    __questions_by_provider: Dict[str, list[QuizQuestion]]
    __quiz_taker: str = ''

    def __init__(self, path: str):
        self.__load_config(path)

    # def __load_config(self, config_path: str) -> None:
    #     with open(config_path, "r") as file:
    #         data = yaml.safe_load(file)

    #     answers = data['quiz'].get('answers')
    #     questions = data['quiz'].get('questions')

    #     if answers:
    #         self.set_answers(answers)
        
    #     if questions:
    #         self.set_questions(questions)

    def set_answers(self, answers_by_provider: Dict[str, list[str]]) -> None:
        for provider, answers in answers_by_provider.items():
            answers_by_provider[provider] = [
                answer.replace("$2y$", "$2b$")
            for answer in answers
        ]
        self.answers_by_provider = answers_by_provider

    def set_quiz_taker(self, quiz_taker: str) -> None:
        self.__quiz_taker = quiz_taker

    def get_quiz_taker(self) -> str:
        return self.__quiz_taker

    def set_questions(self, questions_by_provider: Dict[str, list[QuestionConfig]]) -> None:
        if not questions_by_provider:
            self.__questions_by_provider = Dict()
            return
        self.__questions_by_provider = {
        key: self.__convert_to_quiz_questions(value) 
        for key, value in questions_by_provider.items()
        }

    def __convert_to_quiz_questions(self, configs: list[QuestionConfig]) -> list[QuizQuestion]:
        return [
            MultipleChoiceQuizQuestion(
                index, 
                config.prompt, 
                dict(config.choices), 
                AnswerChoice.UNANSWERED
            ) 
            if config.choices else 
            QuizQuestion(index, config.prompt, '')
            for index, config in enumerate(configs)
        ]
 
    def get_questions(self, provider: str) -> list[QuizQuestion]:
        return self.__questions_by_provider.get(provider)

    def size(self, provider: str) -> int:
        answers = self.__answers_by_provider.get(provider)
        return len(answers) if answers else 0

"""
TODO: Implement bycrypt
"""
#   public async checkAnswer(provider: string, questionNumber: number, actualAnswer: string): Promise<boolean> {
#     const answers = this.answersByProvider.get(provider);
#     if (!answers) {
#       throw new Error(`No answers found for provider: ${provider}`);
#     }
#     return bcrypt.compare(actualAnswer, answers[questionNumber]);
#   }


    
      