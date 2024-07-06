import time

yn: list[str] = ["yes", "no"]

def quizIntro () -> str:
    print(f"✨Welcome to Tasnim's Quiz✨\n")
    time.sleep(0.25)

    while True:
        st1: str = input("Do you want to play? (Yes/No): ").strip().lower()
        if st1 == "yes":
            break
        elif st1 == "no":
            print("Thank you! Come back again whenever you're ready to play.")
            quit()
            break
        print("Please enter a valid response (Yes/No).")
    
    while True:
        name: str = input("Please enter your name: ").strip().capitalize()
        if not name.isdigit():
            break
        print("Invalid name. Please enter a valid name.")
    
    time.sleep(0.5)
    print(f"\nHi {name}! It's beem great to see you!\n")
    print("📚Rules📚")
    print("1. There will be a total of 10 questions, and you'll have to answer all of them. Please write only the answer(s). Otherwise, it'll be considered an incorrect response.")
    print("2. For every correct answer, you'll gain 1 point.")
    print("2. For every incorrect answer, you'll lose 0.25 point.")
    print("Note: Please don't include unnecessary spaces or any puncutation or special signs in your answers.\n")
    time.sleep(0.5)

    while True:
        st2: str = input("Are you ready to dive into the realm of quiz? (Yes/No): ").strip().lower()
        if st2 in yn:
            break
        print("Please enter a valid response (Yes/No).")

    return st1, name, st2

def ask (ques: str, corAns: str) -> int:
    ans: str = input(f"{ques}? ").strip().lower()
    if ans == corAns.lower():
        print("✔ Correct!\n")
        return 1   
    else:
        print("❌Whoops, incorrect!")
        print(f"The correct answer is {corAns}\n")
        return -0.25
    
def quiz (name: str) -> str:
    print(f"\nLet's Begin\n")
    time.sleep(0.5)

    score: int = 0
    correct: int = 0
    incorrect: int = 0

    qna: list = [
        ("What is the capital of Bangladesh", "Dhaka"),
        ("What is the currency of Bangladesh", "Taka"),
        ("What is the full form of ICT", "Information and Communication Technology"),
        ("What is the full form of RAM", "Random Access Memory"),
        ("10×50-10=", "490"),
        ("What is the full form of ROM", "Read Only Memory"),
        ("What is the SI unit of time", "Second"),
        ("NaOH is a ____ (Acid/Base)", "Base"),
        ("Is Plasma Membrane a cytoplasmic organelle (Yes/No)", "No"),
        ("Which animal is the tallest", "Giraffe")
    ]

    for ques, corAns in qna:
        scoreChange = ask(ques, corAns)
        score += scoreChange

        if scoreChange == 1:
            correct += 1
        else:
            incorrect += 1

        time.sleep(0.5)
            
    print(f"\n🎉 Congrats {name}! You've finished the quiz! 🎉\n")
    print(f"Correct Answer: {correct}")
    print(f"Incorrect Amswer: {incorrect}")
    print(f"Score: {score}")

    accuracy = correct/10*100

    print(f"Accuracy: {accuracy}%\n")

    if score >= 8:
        print("🌟 Excellent job! You're a quiz master! 🌟\n")
    elif score >=5 and score < 8:
        print("👍 Good effort! You did well.\n")
    else:
        print("🙁Better luck next time! Keep practicing.\n")

    while True:
        restart: str = input("Do you want to play the quiz again? (Yes/No): ").strip().lower()
        if restart in yn:
            break
        print("Please enter a valid response (Yes/No)")
        
    return restart

def main () -> None:
    st1, name, st2 = quizIntro()
    
    if st2 == "yes":
        restart = quiz(name)
    
        if restart == "yes":
            quiz(name)
        else:
            print("Thank you for playing! Goodbye! 👋")
            quit()
    else:
        print("Thank you! Come back when you're ready to play.")
        quit()
    
    

if __name__ == "__main__":
    main()




