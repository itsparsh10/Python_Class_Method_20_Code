#WAP for an online quiz system. Implement classes for
# quizzes, questions, and users. Include methods for taking quizzes, scoring, and
# displaying results.
class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_answer):
        return user_answer == self.correct_option


class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

    def take_quiz(self):
        user_score = 0
        for i, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}: {question.text}")
            for j, option in enumerate(question.options, start=1):
                print(f"{j}. {option}")

            user_answer = int(input("Your answer (enter the option number): "))
            if question.is_correct(user_answer):
                print("Correct!")
                user_score += 1
            else:
                print(f"Wrong! Correct answer is option {question.correct_option}")

        return user_score


class User:
    def __init__(self, name):
        self.name = name

    def take_quiz(self, quiz):
        print(f"\n{self.name}, welcome to the {quiz.name}!")
        user_score = quiz.take_quiz()
        print(f"\nYour final score: {user_score}/{len(quiz.questions)}")


def main():
    # Create questions
    question1 = Question("What is the capital of France?", ["Paris", "Berlin", "London", "Madrid"], 1)
    question2 = Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1)
    question3 = Question("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2)

    # Create a quiz
    quiz = Quiz("General Knowledge Quiz", [question1, question2, question3])

    # Create a user
    a=input("Enter your name: ")
    user = User(a)

    # User takes the quiz
    user.take_quiz(quiz)

if __name__=="__main__":
    main()