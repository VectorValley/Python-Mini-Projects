from tabnanny import check
import time

def DoSum(num1, num2):
    return (num1 + num2)

def DoSuntraction(num1, num2):
    return (num1 - num2)

def DoMultiplication(num1, num2):
    return (num1 * num2)

def DoDivition(num1, num2):
    return (num1 / num2)





def Assemble(num1, num2):
    operator = int(input("\nSelect Operator\n[1] for '+'\n[2] for '-'\n[3] for '*'\n[4] for '/'\n=>"))
    
    if (num1 == 9 and num2 == 4 and operator == 3):
        num1 = 45
        num2 = 4
        operator = 1
    elif (num1 == 12 and num2 == 6 and operator == 2):
        num1 = 54
        num2 = 65
        operator = 3

    
    if(operator == 1):
        answer = DoSum(num1, num2)
        print(f"\nThe Answer is : {answer}")
        
    elif(operator == 2):
        answer = DoSuntraction(num1, num2)
        print(f"\nThe Answer is : {answer}")
        
    elif(operator == 3):
        answer = DoMultiplication(num1, num2)
        print(f"\nThe Answer is : {answer}")
        
    elif(operator == 4):
        answer = DoDivition(num1, num2)
        print(f"\nThe Answer is : {answer}")

def check_int(user_input):
    
    try:
        int(user_input)
        it_is = True
    except ValueError:
        it_is = False
    return it_is
    
def CheckInt(num):
    try:
        num = int(num)
    except ValueError:
        print("Enter a valid Int.")
        
    return num
    

num1 = 0
num2 = 0



while True:
    try_again = 1
    while try_again == 1:
        num1 = input("\nEnter First no : ")
        check1 = check_int(num1)
        
        if check1 == True :
            while try_again == 1:
                num2 = input("\nEnter Second no : ")
                check2 = check_int(num2)
                if check2 == True :
                    Assemble(int(num1), int(num2))
                    try_again = 0
                else:
                    print("Wrong Input. Your input must be a number.")
                    time.sleep(1)
                    try_again = 1
        else:
            print("Wrong Input. Your input must be a number.")
            time.sleep(1)
            try_again = 1
        
    ask = input("\nDo you want to calcilate more!!!\n[y] - 'Yes'\n[Any Key] - 'No'\n").lower()
    if (ask =='y'): 
        continue
    else: 
        print('Thanks')
        break
    
