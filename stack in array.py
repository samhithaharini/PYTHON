""" correct implementation """

class Stack:
    def __init__(self,size):
        self.stack=[None]*size
        self.top=-1
        self.size=size
    def push(self,item):
        if self.top>=self.size-1:
            print("stack overflow")
        else:
            self.top+=1
            self.stack[self.top]=item
    def pop(self):
        if self.top==-1:
            print("stack underflow")
        else:
            item=self.stack[self.top]
            self.top-=1
    def peek(self):
        if self.top==-1:
            print("stack is empty")
        else:
            print("peek: ",self.stack[self.top])
    def display(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            print(self.stack[:self.top+1])

size=int(input("Enter the size: "))
obj=Stack(size)
while True:
    choice=int(input("1.push 2.pop 3.peek 4.display 5.exit"))
    if choice==1:
        item=int(input("Enter the item: "))
        obj.push(item)
    elif choice==2:
        obj.pop()
    elif choice==3:
        obj.peek()
    elif choice==4:
        obj.display()
    else:
        break
