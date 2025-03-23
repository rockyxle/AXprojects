from car import Car

mcqueen = Car("Mazda", "RX7", 1993, "red")

print("The car's brand is " + mcqueen.make)
print(mcqueen.model)
print(mcqueen.year)
print(mcqueen.color, "\n")


mcqueen.drive()

mcqueen.stop()