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
        assert questions[i].get_answer().value == answers[i]
