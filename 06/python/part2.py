class Object:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None


file = open("../data/input", "r")
data = file.read().splitlines()
file.close()

com = Object("COM")

objects = [
    com
]

for datum in data:
    parentName = datum.split(")")[0]
    childName = datum.split(")")[1]
    parentObject = None
    childObject = None

    for object in objects:
        if object.name == parentName:
            parentObject = object

            break

    if parentObject is None:
        parentObject = Object(parentName)
        objects.append(parentObject)

    for object in objects:
        if object.name == childName:
            childObject = object

            break

    if childObject is None:
        childObject = Object(childName)
        objects.append(childObject)

    parentObject.children.append(childObject)
    childObject.parent = parentObject

sanObject = None
youObject = None

for object in objects:
    if object.name == "SAN":
        sanObject = object

        break

for object in objects:
    if object.name == "YOU":
        youObject = object

        break

if sanObject is None:
    print("Unable to find Santa")

if youObject is None:
    print("Unable to find you")

sanLine = [
    sanObject
]

temp = sanObject
while temp is not com:
    sanLine.append(temp.parent)
    temp = temp.parent

youLine = [
    youObject
]

temp = youObject
while temp is not com:
    youLine.append(temp.parent)
    temp = temp.parent

commonObject = None
for object in sanLine:
    if object in youLine:
        commonObject = object

        break

if commonObject is None:
    print("Unable to find common parent")

print("Number of orbital transfers =", youLine.index(commonObject) + sanLine.index(commonObject) - 2)
