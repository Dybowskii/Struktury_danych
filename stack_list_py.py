class node:
    def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def push(self,values):
        nowy_wezel=node(values)
        nowy_wezel.next=self.head
        self.head=nowy_wezel
        if(self.head.next==None):
            self.tail=self.head

    def append(self,value):
        nowy_wezel=node(value)
        if self.head is None:
            self.head=nowy_wezel
            return
        temp = self.head
        while (temp.next!=None):
            temp = temp.next
        temp.next=nowy_wezel
        temp=temp.next
        self.tail=temp
       

    def print(self):
        if (self.head==None):
            print("Lista jest pusta")
        else:
            temp = self.head
            while (temp.next!=None):
                if(temp.next!=None):
                    print(temp.value)
                else:
                    print(temp.value)
            
                temp=temp.next
            print(temp.value)
                
    def __len__(self):
        if(self.head==None):
            return 0
        temp = self.head
        dlugosc=0
        while (temp!=None):
            dlugosc+=1
            temp = temp.next
        return(dlugosc)

    def node(self,at):
        if (self.head==None):
            print("lista pusta")
            return
        temp = self.head
        dlugosc=0
        while (dlugosc!=at):
            dlugosc+=1
            temp = temp.next
        return(temp)
    
    def insertAfter(self, prev_node, new_value):
        new_node = node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def pop(self):
            if (self.head.next==None):
                self.head=None
            else:
                kasowana_wartosc = self.head 
                self.head = self.head.next
                kasowana_wartosc.next = None
            return kasowana_wartosc
    def remove (self,after):
        if(after.next==None):
            print("nie ma nic dalej do kasowania")
        else:
            after.next=after.next.next
            return
            
    def remove_last(self):
            n=0
            if (self.head.next==None):
                self.head=None
            else:
                temp=self.head
                while(temp.next!=None):
                    temp=temp.next
                    n+=1
                temp=self.head
                for x in range (0,n-1):
                    temp=temp.next
                self.tail=temp
                temp.next=None
            return
class stack:
    

    def __init__(self) -> None:
        self.storage=LinkedList()
    
    def push(self,value):
        self.storage.push(value)
    def print(self):
        
        self.storage.print()
        
    def pop(self):
        wyswietl=self.storage.node(0)
        self.storage.pop()
        return wyswietl
    def __len__(self):
        return len(self.storage)

    

            
new_stack=stack()
new_stack.push(3)
new_stack.push(7)
new_stack.push(4)
new_stack.print()
print("skasowana wartosc:",new_stack.pop().value)
new_stack.print()
print("==================")
print(len(new_stack))


