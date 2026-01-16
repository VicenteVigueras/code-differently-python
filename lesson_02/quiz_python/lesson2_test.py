
def test_make_quiz_questions():
    from lesson2 import Lesson2
    Lesson2 = Lesson2()
    assert len(Lesson2.make_quiz_questions()) == 11

