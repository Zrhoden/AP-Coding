# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.

'A linear search goes through each item in a list until it finds what its looking for, '
'while a binary search repeatedly divides a list in half until it finds what its looking for.'

# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.

listA = [10,24,34,35,67,98,101]

'6'

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.
listB = [1,40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]

'2'

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.

'An algorithm is a way of working with data in a computer and '
'solving problems like sorting and searching.'

# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.

'Linear search, because all they would have to do is go to the 7th floor and then to the room. '

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.

'Binary search, because you can think about the pairs of pants you wore recently '
'which elimnates the need to search every pair of pants you have.'

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.

class consoleMaker : 
    def __init__(self, model, color, number, year):
        self.model = model
        self.color = color
        self.number = number
        self.year = year

        def printInfo(self):
            print('heres your console FAQS')
            print('model:' + self.model)
            print('color:' + str(self.color))
            print('number:' + str(self.number))
            print('year:'+ str(self.year))

consoleOption1 = consoleMaker('Playstation', 'White', 'Five', '2020' )
consoleOption2 = consoleMaker('Xbox', 'Black', 'One', '2013')


# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 

class gameMaker :
    def __init__(self, console, gametype, number, year):
        self.consle = console
        self.gametype = gametype
        self.number = number
        self.year = year

        def printInfo(self):
            print('heres your game FAQS')
            print('model:' + self.console)
            print('color:' + str(self.gametype))
            print('number:' + str(self.number))
            print('year:'+ str(self.year))

gameOption1 = gameMaker('PS5', '2k', '26', '2025')
gameOption2 = gameMaker('PS5', 'Madden', '26', '2025')