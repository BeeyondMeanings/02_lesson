import random

questions = {
    "Who is the current president of the United States of America?": "Donald Trump",
    "Who is the present secretary of state of US?": "Marco Rubio",
    "Who is currently the world's richest man/woman?": "Elon Musk",
    "Who is the founder and CEO of facebook?": "Mark Zukerberg",
    "Who is the 2026 5th richest man in the world?": "Mark Zukerberg",
    "How much is mark zukerberg's networth?": "$222B",
    "Which country is refered to as the Giant of Africa?": "Nigeria",
    "The number one country with the highest number of people living with sickle cell?": "Nigeria",
    "Name the biggest oil producing country in the world?": "United States",
    "Mention the makers of mercedes Benz product?": "German Company",
    "Is Nigeria among the oil producing country?": "Yes",
    "Who is the current president of Nigeria?": "Bola Tinubu",
    "Which religion does the president of Nigeria practices?": "Islam",
    "Is Nigeria truly a country of particular concern as described by President Donald Trump?": "Less probably",
    "Who is the founder and CEO of Instagram?": "Kevin Systrom",
    "In Nigeria, is there a tribe referred to as the igbos?": "Yes",
    "Which system of government is Nigeria practicing currently?": "Democracy",
    "What is the simpler and most common definition of Democracy?": "Government of the people, by the people, and for the people",
    "Who is currently the richest man in Africa?": "Aliko Dangote",
    "Which country do African richest man Aliko Dangote comes from?": "Nigeria",
    "Which product is Aliko Dangote known for?": "Cement",
    "Is Nigeria a multi-ethnic, multi-cultural and multi-religious state?": "Yes",

}

def python_trivia_game():
    question_list = list(questions.keys())
    total_questions = len(question_list)
    score = 0

    selected_question = random.sample(question_list, total_questions)
    for idx, question in enumerate(selected_question):
        print(f"Question {idx+1}:\n")
        print(question)


        user_answer = input("Your answer: ").lower().strip()
        correct_answer = questions[question].lower().strip()

        if user_answer == correct_answer:
            print(f"Correct! You got it right!")
            score += 1
        else:

            print(f"Wrong! The correct_answer is: {questions[question]}\n")

            print(f"Game over! Your score is: {score}/{total_questions}.\n")
            return

        print(f"Congratulations! You answered correctly!\n")
        print(f"Score: {score}/{total_questions}.\n")


python_trivia_game()
