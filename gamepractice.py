import random

questions = {
      "What do you call a place you deposit money in?": "bank",
      "What do you call the machine that dispense cash in the bank?": "ATM",
      "The slip used to deposit money in a bank is called what?": "teller",
      "What do you call the slip used in withdrawing money in the bank?": "withdrawal slip",
      "Slip issued to someone to get money from your account on your instruction is called what?": "cheque book",
      "What is the full meaning of ATM?": "automated teller machine",
      "What do you call the machine used by money vendors to receive and transfer money?": "pos machine",
      "Name one online bank in Nigeria?": "opay",
      "Name two online banks in Nigeria that is so famous in the country?": "opay",
      "Mention the name of Nigeria's apex bank?": "central bank of nigeria"
}

def python_trivia_game():
    question_list = list(questions.keys())
    total_questions = 10
    score = 0

    selected_question = random.sample(question_list, total_questions)

    for idx, question in enumerate(selected_question):
      print(f"{idx + 1}.{question}")
      user_answer = input("your answer: ").lower().strip()
      correct_answer = questions[question]

      if user_answer == correct_answer.lower():
        print("correct!\n")
        score += 1
      else:
         print(f"wrong. The correct answer is: {correct_answer}.\n")


    print(f"Game over! your final score is: {score}/{total_questions}")


python_trivia_game()

