import numpy as np

class Student:
    def __init__(self,PRN,name,email,age,gender,pyh_grade):
        self.prn = PRN
        self.name = name
        self.email = email
        self.age = age
        self.gender = gender
        self.python_grade = pyh_grade

    def printinfo(self):
        printinfo = np.array([self.prn,self.name,self.email,self.age,self.gender,self.python_grade])
        print(printinfo)
        return " "

s1 = Student(1, 'chikku', '123@dypiu.ac.in', 12, 'M', 'A')
s2 = Student(2, 'saniya', '231@@dypiu.ac.in', 87, 'F', 'B')
s3 = Student(3, 'srushti', '567@dypiu.ac.in', 34, 'f', 'C')
s4 = Student(4, 'krutika', '227@dypiu.ac.in', 43, 'f', 'A+')
s5 = Student(5, 'aryan', '578@dypiu.ac.in', 67, 'm', 'B+')
s6 = Student(6, 'joshua', '768@dypiu.ac.in', 43, 'M', 'B+')
s7 = Student(7, 'DIvya', '123@dypiu.ac.in', 67, 'F', 'C')
s8 = Student(8, 'shubham', '138@dypiu.ac.in', 67, 'M', 'B')
s9 = Student(9, 'virat', '362@dypiu.ac.in', 19, 'M', 'A')
s10 = Student(10, 'sanjana', '236@dypiu.ac.in', 87, 'F', 'A+')

lis = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]

class Node():
   def __init__(self,key,pred,succ):
       self.key = key
       self.pred = pred
       self.succ = succ


class Doubly_Linkedlist():

   def __init__(self,head,tail):
        self.head = head
        self.tail = tail

   def insert(self, value):
       element = Node(value, None, None)
       # the new element will become the head
       if self.head == None:
            self.head = element
            self.head.succ=self.head.pred=element
            self.tail=self.head

       elif self.head==self.tail :
           self.head.pred=self.head.succ =element
           element.succ=element.pred=self.head
           self.tail=element

           self.tail.succ.key.printinfo()
           self.head.pred.key.printinfo()

       else:
           self.head.pred=self.tail.succ=element
           element.succ=self.head
           element.pred=self.tail
           self.tail=element

           self.tail.succ.key.printinfo()
           self.head.pred.key.printinfo()

   def printElements(self):
       w=1
       x = self.head
       if (x==None):
           print("LIST EMPTY")
           return " "
       else:
            while (x.succ!=self.head):
                (x.key.printinfo(), ",")
                x = x.succ
                w=w+1
            x.key.printinfo()
            print("Size of Linked List > ",w)
            return " "
            return " "

   def search(self, searchValue):
        var = self.head
        z=0
        if (var==None):
            print(" ")
        else:
            while var != None and var.key != searchValue:
                var = var.succ
                if var==self.head:
                    z=1
                    break
        return var,z
   def delete(self, x):
        a,z=theList.search(x)
        if a==None:
            print("")
        elif z==1:
            print("prn not found")
        else:
            if a==self.head:
                self.tail.succ=self.head.succ
                self.head.succ.pred=self.tail
                self.head=self.head.succ
            elif a==self.tail:
                self.tail.pred.succ = self.head
                self.head.pred = self.tail.pred
                self.tail = self.tail.pred
            else:
                a.pred.succ=a.succ
                a.succ.pred=a.pred


theList = Doubly_Linkedlist(None , None)
i = 0
while True:
    print("1 - FOR INSERTION >>,\n"
                  "2- FOR SEARCH >>, \n"
                  "3- FOR DELETION,\n"
                  "4- DO UH WANT TO ITERATE? ,\n"
                  "5-EXIT CODE\n")
    ans=int(input("Choose any one from above 5 >>"))

    if ans == 1:
        #for j in range(0,len(lis)):
        theList.insert(lis[i])
        i=i+1
        theList.printElements()

    elif ans == 2:
        ab = int(input("Enter Prn"))
        if ab>len(lis):
            print("invalid Prn")
        else:
            a,z=theList.search(lis[ab-1])
            if a==None:
                print("List Empty")
            elif z==1:
                print("PRN not Found")

            else:
                a.key.printinfo()

    elif ans == 3:
        ab=int(input("Enter Prn"))
        if ab>len(lis):
            print("invalid Prn")
        else:
            theList.delete(lis[ab-1])

            theList.printElements()

    elif ans == 4:
        theList.printElements()

    elif ans == 5:
        break

    else:
        print("Enter a valid Input > ")