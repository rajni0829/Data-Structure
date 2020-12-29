#instance -> to create an instance of a class, you use the the class name, followed by parentheses.
#method -> def vale
#constructor ->initialisation (__init__)
#inheritance -> base and derived classes


#1.Python Program to Reverse a Stack using Recursion
class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def display(self):
        for data in reversed(self.items):
            print(data)
st = Stack()

def insert_at_bottom(st,data):
        if st.is_empty():
            st.push(data)
        else:
            popped = st.pop()       #saare elements ko pop karega ----------------- line 1
            insert_at_bottom(st,data)      #data jo append kiya vo dalega puch ne function firse call krkr --------------line 2
            st.push(popped)        # line 1 se jo value pop fi vo push kr dega line 2 k baad

def reversed_stack(st):
    if not st.is_empty():
        popped = st.pop()
        reversed_stack(st)
        insert_at_bottom(st,popped)

data_list = input("Please Enter the Element :")
for data in data_list:
    st.push(int(data))
st.display()
reversed_stack(st)
