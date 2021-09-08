class stack:
    def __init__(self):
        self.stack=list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if (len(self.stack)>0):
            print(self.stack.pop())
        else:
            print( 'There are no elements')
    def peek(self):
        if(len(self.stack)>0):
            print(self.stack[len(self.stack)-1])
        else:
            print(None)
obj=stack()
obj.push(1)
obj.push(5)
obj.push(9)
print(obj.stack)
obj.pop()
print(obj.stack)


