class Database():
    'this is info'

    def __init__(self):
        self.myList = []
        self.count=0
        self.readFile()
    
    def fetch(self):
        return self.myList
    

    def readFile(self):
        try:
            self.fileContent = open('database.txt', 'r')
        except:
            self.fileContent = open('database.txt', 'w')
            #print('ok ')
        for item in self.fileContent:
            #print(item)
            self.itemCreater(item)
        self.fileContent.close()
        

    def writeFile(self):
        self.fileContent = open('database.txt', 'w')
        for item in self.myList:
            line = ''
            for subitem in item[1:]:
                line = line + ' '+str(subitem)
            self.fileContent.write(line.strip() + '\n')
        self.printList()

    def printList(self):###
        print(self.myList)

    def itemCreater(self, line):###
        name, idNo, price, qnt = line.split()
        self.insert(name, idNo, price, qnt)

    def insert(self,name,idNo,price,qnt):
        self.myList.append((self.count,name,idNo,price,qnt))
        self.count+=1

    def remove(self,id):
        del self.myList[int(id)]

    def update(self,id,idNo,name,price,qnt):
        del self.myList[int(id)]
        self.insert(idNo,name,price,qnt)


#g = db()
#g.userInput()
#g.writeFile()
