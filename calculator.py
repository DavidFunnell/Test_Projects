#This is a calculator where people can input numbers and tell you if you what to do with them

total = 0
number_1_input = float(input("What is the first number you would like to input?"))
number_2_input = float(input("What is the second number you would like to input?"))
action = input("What would you like to do to these numbers?")

def math_function(num1,num2,action):
    if(action == "+") or (action == "add"):
        return num1 + int(num2)
    elif(action == "-") or (action == "subtract"):
        return int(num1) - int(num2)
    elif(action == "*") or (action == "multiply"):
        return int(num1)*int(num2)
    elif(action == "/") or (action == "divide"):
        return int(num1)/int(num2)

print(math_function(number_1_input,number_2_input,action))
