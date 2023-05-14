class QuizBrain(object):
    ''' QuizBrain model '''

    def __init__(self, question_lists: list):
        self.__current_num_question = 0
        self.__question_lists = question_lists
        self.__score = 0

    def still_has_questions(self):
        return self.__current_num_question < len(self.__question_lists)

    def next_question(self):
        question = self.__question_lists[self.__current_num_question]
        self.__current_num_question += 1
        answer = input(f"Q.{self.__current_num_question} {question.text()} (True/False): ")
        self.check_answer(answer, question.answer())

    def check_answer(self, actuall_answer, expect_answer):
        right = False
        if actuall_answer == expect_answer:
            print(f"You got it right!")
            self.__score += 1
        else:
            print(f"You are wrong")
            right = False

        print(f"The correct answer is: {expect_answer}.")
        print(f"Your current score is: {self.__score}/{self.__current_num_question}.")
        print('\n')

    def final_scrore(self):
        print(f"Your final score is: {self.__score}/{self.__current_num_question}")
