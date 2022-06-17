name = input("Enter Your Name : ")


age = int(input("Enter your age : "))



if age <=25:
    print("SORRY ! you are not eligible to play this game ")


elif age>=25:

    gender= input("Gender : ")
    
    print("let's start the game")




    
    import random


    while True:

        choices = ["snake", "water", "gun"]


        computer = random.choice(choices)
        
        player = input("SNAKE  GUN  OR WATER : ").lower()
        print("computer chose : "+ computer)



        if computer == player:

            print("Match Draw !")




        elif computer == "gun":

            if player == "water":


                print("Congratulation ! You Win The Game "+name)

            if player == "snake":
                print(" SORRY You Lose !  "+name)



        elif computer == "snake":

            if player == "gun":
                    print("Congratulation ! You Win The Game  " +name)

            if player == "water":
                    print("oops!  You Lose !  "+name)



        elif computer == "water":
            if player == "gun":
                    print("Better luck next time ! You Lose !  "+name)
            if player == "snake":
                    print("Let's party ! You Win The Game  "+name)

                    

        play_again=input("Would You Like To Play Again ? (Yes/No) : ")

        if play_again != "yes":
            break

    print("good bye & Take care")
    
    

    



    






  






   


