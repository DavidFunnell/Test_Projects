
input_word = input("insert a word: ")
length = len(input_word)
i=0
x=1
y=0
while i < length:
    if(input_word[i] == input_word[-x]):
        y+=1
    else:
        y+=0
    x+=1
    i+=1
if(y==length):
    print("Is a palindrome")
else:
    print("is not a palindrome")


