#instance -> to create an instance of a class, you use the the class name, followed by parentheses.
#method -> def value
#constructor ->initialisation (__init__)
#inheritance -> base and derived classes


#1.Python Program to Implement a Stack
class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        if self.items == []:
            return True

    def push(self,append_value):
        self.items.append(append_value)
        return self.items

    def pop(self):
        return self.items.pop()

st = Stack()

choice = 1
while choice != 3:
    print("\n 1.Push value ")
    print(" 2.Pop")
    print(" 3.Quit")
    choice = int(input("\nWhich Operation would you like to perform ? (1-3) : "))


    if choice == 1:
        a = int(input("\nEnter Value you want to Append : "))
        print("pushed value ->",st.push(a))

    elif choice == 2:
        if st.is_empty():
            print("Stack is empty")
        else:
            print("Popped value ->",st.pop())

    # elif choice == 3:
    #     break
    else:
        print("invalid choice !")
print()