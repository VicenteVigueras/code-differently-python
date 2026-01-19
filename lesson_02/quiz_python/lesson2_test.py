from lesson2 import Lesson2
import yaml

def load_answers():
    with open("quiz.yaml", "r") as file:
        data = yaml.safe_load(file)
    return data['quiz']['answers']['default']

def test_make_quiz_questions():
    assert len(Lesson2.make_quiz_questions()) == 11

def test_review_quiz():
    answers = load_answers()
    print(answers)
    questions = Lesson2.make_quiz_questions()
    print(questions)

    for i in range (0,len(questions)):
        assert questions[i].get_answer() == answers[i]


"""
TODO: Cross-check test with original version and implement any missing tests
"""
# const __filename = fileURLToPath(import.meta.url); // get the resolved path to the file
# const __dirname = path.dirname(__filename); // get the name of the directory
# const softExpect = proxy(expect);

# describe("Lesson2Test", () => {
#   const quizConfig: QuizConfig = new QuizConfig(
#     path.resolve(__dirname, "../quiz.yaml"),
#   );
#   let quizQuestions: QuizQuestion[];

#   const EXPECTED_NUMBER_OF_QUESTIONS = 11;

#   beforeEach(() => {
#     getQuestions();
#   });

#   const getQuestions = () => {
#     quizQuestions = Lesson2.makeQuizQuestions().sort(
#       (a, b) => a.getQuestionNumber() - b.getQuestionNumber(),
#     );
#   };

#   it("checkQuizQuestions_areAssembledCorrectly", () => {
#     // Expect the right number of questions.
#     expect(quizQuestions.length).toBe(EXPECTED_NUMBER_OF_QUESTIONS);

#     // Expect questions to be numbered correctly.
#     for (let i = 0; i < quizQuestions.length; i++) {
#       expect(quizQuestions[i].getQuestionNumber()).toBe(i);
#     }
#   });

#   it("checkQuizQuestions_promptsAreUnique", () => {
#     const questionPrompts = new Set(
#       quizQuestions.map((q) => q.getQuestionPrompt()),
#     );
#     expect(questionPrompts.size).toBe(EXPECTED_NUMBER_OF_QUESTIONS);
#   });

#   it("checkQuestions_answeredCorrectly", async () => {
#     expect(quizConfig.size("default")).toBe(quizQuestions.length);

#     for (const question of quizQuestions) {
#       const actualAnswer = question.getAnswer();

#       // Check that the question was answered.
#       softExpect(actualAnswer).not.toBe(AnswerChoice.UNANSWERED);

#       // Check that the answer is correct.
#       softExpect(
#         await quizConfig.checkAnswer(
#           "default",
#           question.getQuestionNumber(),
#           actualAnswer,
#         ),
#       ).toBe(true);
#     }

#     flush();
#   });
# });
