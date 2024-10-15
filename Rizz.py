def be_my_girlfriend():
    while True:
        question = input("Can you please be my girlfriend? (yes/no): ")
        question = question.lower()
        if question == "yes":
            print("@@@@@@@@")
            print(" @@@@@@")
            print("  @@@")
            print("  \|/")
            print("   | ")
            print(" __|__ ")
            
        elif question == "no":
            print("OOPS!!...I can't take no for an answer,Please try again!!🙁")
        else:
            print("Invalid Input,try again...")
        break
be_my_girlfriend()