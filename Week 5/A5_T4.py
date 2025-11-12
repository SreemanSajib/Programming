def askDimension(PPrompt: str) -> float:
   Feed = int(input(f"Insert {PPrompt}: "))
   return Feed #return this info to the position where the function was called from


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

print("Program starting.")
Width = askDimension("width") #Jump to function askDimension
Height = askDimension("height") #Jump to function askDimension
Area = calcRectangleArea(Width, Height) #Jump to function calcRectangleArea()

print("")
print(f"Area is {Area}²")
print("Program ending.")
