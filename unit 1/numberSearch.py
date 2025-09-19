numberList = [1, 5, 10, 20, 39, 48, 83, 89, 72, 90]

number = 90

number2 = 1

def findNumber(numberList, number, number2) :
    for x in numberList:
        if x == number:
            print('largest number found')
        elif x == number2 :
            print('smallest number found')
        else :
            print('number not found')

findNumber(numberList, number, number2)



def reverseString(word):
    text = word[::-1]
    print(text)

reverseString('anything')