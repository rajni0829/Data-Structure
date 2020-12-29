#QUEUE (Enqueue and Dequeue)
import  numpy as np
class Queue():
    def __init__(self,name,age,clas):
        self.name =name
        self.age = age
        self.clas = clas

    def print_info(self):
        info = np.array([self.name,self.age,self.clas])
        return info

s1 = Queue("a", 20, 8)
s2 = Queue("b", 45, 9)
s3 = Queue("c", 5, 1)
s4 = Queue("a", 20, 8)
s5 = Queue("b", 45, 9)
s6 = Queue("c", 5, 1)

lis = [s1,s2,s3,s4,s5,s6]
queue_arr = np.empty(7,Queue)

head = 0
tail = 0

def enqueue(x,tail,arr):
    arr[tail] = x
    print(queue_arr[tail])
    tail+= 1
    return tail

def dequeue(head,arr):

    print(queue_arr[head])
    arr[head] = None
    head += 1
    return head
i = 0
choice = 1
while choice != 0:
    print(" 0.exit")
    print(" 1.enq")
    print(" 2.deq")
    choice = int(input("\nChoose (0-2) : "))

    if choice == 0:
        print("exit code")
        break

    if choice == 1:
        if tail == 6 and head == 0:
            print("error overflow")
            break

        elif tail > 6:
            tail = 0
            break

        elif tail == head -1:
            print("error overflow")

        else:
            tail = enqueue(lis[i].print_info(),tail,queue_arr)
            i += 1

    elif choice == 2:
            if head == tail:
                print("error underflow")
                break


            elif head > 6:
                head = 0
                break

            else:
                head = dequeue(head,queue_arr)

    else:
        print("\nInvalid choice")

for i in range(0,6):
    print("\n")
    print(queue_arr[i])

