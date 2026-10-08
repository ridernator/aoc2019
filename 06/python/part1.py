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
    parent = datum.split(")")[0]
    child = datum.split(")")[1]
    parentObject = None
    childObject = None

    for object in objects:
        if object.name == parent:
            parentObject = object

            break

    if parentObject is None:
        parentObject = Object(parent)
        objects.append(parentObject)

    for object in objects:
        if object.name == child:
            childObject = object

            break

    if childObject is None:
        childObject = Object(child)
        objects.append(childObject)

    parentObject.children.append(childObject)
    childObject.parent = parentObject

checksum = 0
for object in objects:
    temp = object

    while temp.parent is not None:
        temp = temp.parent
        checksum += 1

print("Checksum is", checksum)
