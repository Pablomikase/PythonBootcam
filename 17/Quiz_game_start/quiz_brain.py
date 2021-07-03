class QuizBrain:
    current_text = ""
    current_answare = ""
    current_questionNumber = 0
    question_list = []
    user_answer = ""
    score = 0
    tries = 0

    def __init__(self, question_dictionary):
        self.current_text = question_dictionary[self.current_questionNumber].text
        self.current_answare = question_dictionary[self.current_questionNumber].answer
        self.question_list = question_dictionary

    def pass_to_the_next_question(self):
        self.current_questionNumber += 1
        self.current_text = self.question_list[self.current_questionNumber].text
        self.current_answare = self.question_list[self.current_questionNumber].answer

    def print_question(self):
        self.user_answer = input(f"Q.{self.current_questionNumber + 1} --> {self.current_text}  (True/False)? ").lower()
        if self.user_answer == "true" or self.user_answer == "false":
            print("The answer is valid....")
        else:
            print("Insert a valid answer please, only true or false...")
            self.print_question()

    def is_the_user_answer_correct(self):
        if self.user_answer == self.current_answare.lower():
            print("You got it RIGHT¡")
            self.score += 1

        else:
            print("You are WRONG :(")
        self.tries += 1
        print(f"The correct answare is {self.current_answare}")
        print(f"Your current score is: {self.score}/{self.tries}")

    def are_left_questions(self):
        if self.current_questionNumber<len(self.question_list):
            return True