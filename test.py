class db():
    'this is info'
    def __init__(self):
        self.myList = []
        self.readFile()
        print(self.myList)


    def readFile(self):
        try:
            self.fileContent = open('database.txt','r')
            for item in self.fileContent: 
                self.myList.append(item.split())
        except :
            self.fileContent = open('database.txt','w')
        self.fileContent.close()

    def writeFile(self):
        self.fileContent = open('database.txt','w')
        for item in self.myList:
            line = ''
            for subitem in item:
                line = line +' '+subitem
            self.fileContent.write(line.strip() + '\n')
        self.printList()

    def printList(self):
        print(self.myList)


g = db()
g.writeFile()
