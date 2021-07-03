from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def generate_question_bank():
    question_bank = []
    for question in question_data:
        new_q = Question(question["text"], question["answer"])
        question_bank.append(new_q)
    return question_bank


question_bank = generate_question_bank()
my_quiz_brain = QuizBrain(question_bank)


while(my_quiz_brain.are_left_questions()):
    my_quiz_brain.print_question()
    my_quiz_brain.is_the_user_answer_correct()
    my_quiz_brain.pass_to_the_next_question()