
def foreverloop():
    choice=0
    while(True):
        choice = int(input("do you want: \n 1) tea \n 2)coffe \n 3) add 5 kr \n 4) add 10 kr \n 5) Hot Chocolate \n 6)and 20 kr"))
        print("error")



        

state = 0 
#tea 10 kr
#coffe 15 kr
while state<=20 and state >=0:
    choice = int(input("do you want: \n 1) tea \n 2)coffe \n 3) add 5 kr \n 4) add 10 kr \n 5) hot chocolate \n 6) 20kr \n"))
    if state == 0:
        if choice == 1:
            print("error")
            foreverloop()
        elif choice== 2:
            print("error")
            foreverloop()
        elif choice==3:
            state=5
        elif choice==4:
            state=10
        elif choice==5:
            print("error")
        elif choice == 6:
            state = 20
        else:
            print("error in the input")
            foreverloop()
    elif state == 5:
        if choice == 1:
            print("error")
            foreverloop()
        elif choice== 2:
            print("error")
            foreverloop()
        elif choice==3:
            state=10
        elif choice==4:
            state=15
        elif choice==5:
            print("error")
            foreverloop()
        elif choice==6:
            print("error too much credit")
            foreverloop()
        else:
            print("error in the input")
            foreverloop()
    elif state==10:
        if choice == 1:
            print("tea served")
            state=0
        elif choice== 2:
            print("error")
            foreverloop()
        elif choice==3:
            state=15
        elif choice==4:
            state=20
        elif choice == 5:
            print("error")
            foreverloop()
        elif choice == 6:
            state = 20
        else:
            print("error in the input")
            foreverloop()
    elif state == 15:
        if choice == 1:
            state=5
            print("tea served")
        elif choice== 2:
            state=0
            print("coffe served")
        elif choice==3:
            state=20
        elif choice==4:
            print("error too much credit")
            foreverloop()
        elif choice == 5:
            print("error")
            foreverloop()
        elif choice == 6:
            print("error too much credit")
            foreverloop()
        else:
            print("error in the input")
            foreverloop()
    elif state == 20:
        if choice == 1:
            state=10
            print("tea served")
        elif choice== 2:
            state=5
            print("coffe served")
        elif choice==3:
            print("error too much credit")
            foreverloop()
        elif choice==4:
            print("error too much credit")
            foreverloop()
        elif choice==5:
            state=0
            print("hot chocolate served")
        elif choice==6:
            print("error too much credit")
            foreverloop()
        else:
            print("error in the input")
            foreverloop()     
    else:
        print("error")
        foreverloop()
        exit

while(True):
    choice = int(input("do you want 1) tea 2)coffe \n 3) add 5 kr \n 4) add 10 kr \n 5) hot chocolate \n 6) add 20kr \n"))
    print("error")
