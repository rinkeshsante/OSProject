class db():
    'this is info'

    def __init__(self):
        self.myList = []
        self.readFile()
        print(self.myList)

    def readFile(self):
        try:
            self.fileContent = open('database.txt', 'r')
            for item in self.fileContent:
                self.myList.append(self.itemCreater(item))
        except:
            self.fileContent = open('database.txt', 'w')
        self.fileContent.close()

    def writeFile(self):
        self.fileContent = open('database.txt', 'w')
        for item in self.myList:
            line = ''
            for subitem in item:
                line = line + ' '+str(subitem)
            self.fileContent.write(line.strip() + '\n')
        self.printList()

    def printList(self):
        print(self.myList)

    def itemCreater(self, line):
        name, price, count, availibilty = line.split()
        price, count = int(price), int(count)
        return (name, price, count, availibilty)

    def userInput(self):
        name = input('enter product name :')
        price = int(input('enter the price of one item :'))
        count = int(input('enter the count of item :'))
        availibilty = input('enter availibility :')

        self.myList.append((name,price,count,availibilty))


g = db()
g.userInput()
g.writeFile()
