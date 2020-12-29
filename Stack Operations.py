#instance -> to create an instance of a class, you use the the class name, followed by parentheses.
#method -> def vale
#constructor ->initialisation (__init__)
#inheritance -> base and derived classes

# Stack (Push & Pop)
import  numpy as np
class Stack():
    def __init__(self,name,age,clas):
        self.name =name
        self.age = age
        self.clas = clas

    def print_info(self):
        print_info_var = np.array([self.name,self.age,self.clas])
        # print(print_info)
        return print_info_var

s1 = Stack("a",20,8)
s2 = Stack("b",45,9)
s3 = Stack("c",5,1)
s4 = Stack("a",20,8)
s5 = Stack("b",45,9)
s6 = Stack("c",5,1)

lis = [s1,s2,s3,s4,s5,s6]
stack_arr = np.empty(6,Stack)

top = -1
def push(top,i,arr):
    top += 1
    arr[top] = i
    return top

user = input("Do you want to push values?\n y/n :")
i = -1  #
while user == "y":
    i += 1 # [0, -1], [1,0], [2,1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]
    if i == 6: # top
        print("Error Overflow")
        break

    else:
        top = push(top,lis[i].print_info(),stack_arr)  #
        print(stack_arr[i])
        user = input("Do you want to push more values?\n y/n :")



usr = input("Do you want to pop values? \n y/n :")
# top +=1
def pop(top,stack_arr):
        print(stack_arr[top])  # returns whats being poped
        stack_arr[top] = None
        top -= 1
        return top

while usr == "y":
    if top == 0:
        print("Error Underflow")
        break

    else:
        top = pop(top,stack_arr)
        usr = input("Do you want to pop more values? \n y/n :")


for i in range(0,top + 1):
    print("\n")
    print(stack_arr[i])

