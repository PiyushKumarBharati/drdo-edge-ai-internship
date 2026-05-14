
def max_num(num1,num2,num3):
    if num1>num2 and num1>num3 :
       return num1
    elif num2>num3 and num2>num1 :
        return num2
    elif num3>num1 and num3>num2 :
        return num3
    else :
        return -1

res=max_num(40,400,402)

if res==-1:
    print("all values are equal")
else:
    print(str(res) +" is the max value")

letter=input("Enter a letter: ")

if letter.lower() in "aeiou":
    print("The letter is a vowel")
else:
    print("the letter is a consonant")