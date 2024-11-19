class Element:
    def __init__(self, name, start, finish):
        self.name = name
        self.start = start
        self.finish = finish

def compare(elementA, elementB):
    return elementB.finish - elementA.finish

elements = [
    Element("watch", 9, 10),
    Element("shirt", 1, 8),
    Element("tie", 2, 5),
    Element("jacket", 3, 4),
    Element("belt", 6, 7),
    Element("pants", 12, 15),
    Element("undershorts", 11, 16),
    Element("socks", 17, 18),
    Element("shoes", 13, 14)
]

elements.sort(key=lambda x: x.finish, reverse=True)

print("topological sort:")
for element in elements:
    print(element.name)

----------------------OUTPUT--------------------------
topological sort:
socks
undershorts
pants
shoes
watch
shirt
belt
tie
jacket

Process finished with exit code 0
