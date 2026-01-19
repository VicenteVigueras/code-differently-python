from typing import Dict, NotRequired, Optional, TypedDict
from .quiz_question import QuizQuestion
from .answer_choice import AnswerChoice
import yaml


class QuizConfig:
    __answers_by_provider: Dict[str,list[str]]
    __questions_by_provider: Dict[str, list[QuizQuestion]]
    __quiz_taker: str = ''

    def __init__(self, path: str):
        self.__load_config(path)

    def __load_config(self, config_path: str) -> None:
        with open(config_path, "r") as file:
            data = yaml.safe_load(file)

        answers = data['quiz'].get('answers')
        questions = data['quiz'].get('questions')

        if answers:
            self.set_answers(answers)
        
        if questions:
            self.set_questions(questions)

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

    def set_questions(self, questions_by_provider: Dict[str, list[QuizConfig]]):
        if not questions_by_provider:
            self.__questions_by_provider = Dict()
            return
        self.__questions_by_provider = Dict()
        

#   public setQuestions(questionsByProvider: Record<string, QuestionConfig[]>) {
#     if (!questionsByProvider) {
#       this.questionsByProvider = new Map();
#       return;
#     }
#     this.questionsByProvider = new Map(
#       Object.entries(questionsByProvider).map(([key, value]) => [
#         key,
#         this.convertToQuizQuestions(value),
#       ])
#     );
#   }

#   private convertToQuizQuestions(configs: QuestionConfig[]): QuizQuestion[] {
#     return configs.map((config, index) => {
#       if (!config.choices) {
#         return new QuizQuestion(index, config.prompt, '');
#       } else {
#         return new MultipleChoiceQuizQuestion(
#           index,
#           config.prompt,
#           new Map(Object.entries(config.choices)) as Map<AnswerChoice, string>,
#           AnswerChoice.UNANSWERED);
        
#       }
#     });
#   }


#   public getQuestions(provider: string): QuizQuestion[] | undefined {
#     return this.questionsByProvider.get(provider);
#   }

#   public async checkAnswer(provider: string, questionNumber: number, actualAnswer: string): Promise<boolean> {
#     const answers = this.answersByProvider.get(provider);
#     if (!answers) {
#       throw new Error(`No answers found for provider: ${provider}`);
#     }
#     return bcrypt.compare(actualAnswer, answers[questionNumber]);
#   }

#   public size(provider: string): number {
#     const answers = this.answersByProvider.get(provider);
#     return answers ? answers.length : 0;
#   }
# }
