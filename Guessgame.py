print("Welcome to the Guess game, please Guess a Number between 1 - 20 , there is one luckey number that will win you 1000 rs\n"
      "you will get 5 chance,"
      "so good luck")
num = 0
while(True):
    num = num+1
    i = 12
    i=int(input("Enter a number\n"))
    if i<12:
        print("Your luckey numbere is not",i ,"its more than that")
        continue
    elif i==12:
        print("congratulations you have entered 12, it is correct answer, you have won 1000 rs..")
        break

    elif i>20:
        print("please enter number between 1-20")

    elif num==5:
        print("You have used your 5 chance to win 1000 rs, You can try next time")
        break

    else:
        print("Your luckey numbere is not",i ,"its less than that")
