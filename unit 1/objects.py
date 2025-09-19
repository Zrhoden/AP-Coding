# object is a construct for storing data and functions together34

class carMaker :
    def __init__(self, name, color, seating, year, model, miles):
        self.name = name
        self.color = color
        self.seating = seating
        self.year = year
        self.model = model
        self.miles = miles

def printInfo(self):
    print('heres your car FAQS')
    print('name:' + self.name)
    print('year:' + str(self.year))
    print('miles:'+ str(self.miles))

    def windshieldwipers(self):
        print('when raining turn on')

    def airbag(self):
        print('when driving a certain speed and a collision happens; open')

    def turningSignals(self, up, down):
        if up:
            print('turn left')
        elif down:
            print('turn right')
        else:
            print('dont turn signals on')

    def bluetooth(self, year):
        if year > 2020:
            print('you have bluetooth')
        else:
            print('no bluettoh on this model')

carOption1 = carMaker('carolla', 'black')

class phoneMaker : 
    def __init__(self, model, color, cameras, number, year):
        self.model = model
        self.color = color
        self.cameras = cameras
        self.number = number
        self.year = year

        def printInfo(self):
            print('heres your phone FAQS')
            print('model:' + self.model)
            print('color:' + str(self.color))
            print('cameras:'+ str(self.cameras))
            print('number:' + str(self.number))

    def faceId(self, year ):
        if year < 2017:
            print('you have face id')
        else:
            print('no face id on this model')

phoneOption1 = phoneMaker('0o0')