class Car: #Create an object
    
    def __init__(self, make, model, year, color): # Pass in parameters to be used
        self.make = make
        self.year = year 
        self.model = model
        self.color = color
     
    def drive (self):
        print("This " +self.model+ " car is driving")

    def stop (self):
        print("The " + self.model + " has stopped")