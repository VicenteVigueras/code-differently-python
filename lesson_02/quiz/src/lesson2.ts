import {
  AnswerChoice,
  MultipleChoiceQuizQuestion,
  QuizPrinter,
  QuizQuestion,
} from "codedifferently-instructional";

export class Lesson2 {
  run(): void {
    const quizQuestions = Lesson2.makeQuizQuestions();
    if (!quizQuestions) throw new Error("Quiz questions cannot be null");
    const printer = new QuizPrinter();
    printer.printQuiz(quizQuestions);
  }

  static makeQuizQuestions(): QuizQuestion[] {
    return [
      Lesson2.makeQuestion0(),
    ];
  }

  private static makeQuestion0(): QuizQuestion {
    return new MultipleChoiceQuizQuestion(
      0,
      "What is the main purpose of version control?",
      new Map([
        [AnswerChoice.A, "To make backups of files"],
        [AnswerChoice.B, "To keep a record of changes over time"],
        [AnswerChoice.C, "To delete unnecessary files"],
        [AnswerChoice.D, "To run code more efficiently"],
      ]),
      AnswerChoice.UNANSWERED, // Replace `UNANSWERED` with the correct answer.
    );
  }
}

if (!process.env.JEST_WORKER_ID) {
  new Lesson2().run();
}
