from enum import Enum
from itertools import dropwhile
import re
from sys import path
from tkinter.messagebox import NO
from typing import Optional

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
                    print('{}, '.format(temp.value),end='')
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
            elif(self.head==None):
                return None
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
class Queue:

    def __init__(self) -> None:
        self.storage=LinkedList()
    
    def enqueue(self,value):
        self.storage.append(value)
    def print(self):
        self.storage.print()
    def nodeque(self):
        return self.storage.node(0).value
    def dequeue(self):
        wyswietl=self.storage.node(0)
        self.storage.pop()
        return wyswietl
    def __len__(self):
        return len(self.storage)
    def show_last(self):
        return self.storage.node(len(self)-1)
class EdgeType(Enum):
    directed = 1
    undirected = 2
class Vertex:
    def __init__(self,data,index) -> None:
        self.data=data
        self.index=index
class Edge:
    def __init__(self,source,destination,weight: Optional[float] = None) -> None:
        self.source=source
        self.destination=destination
        self.weight=weight
        
class Graph:
    def __init__(self) -> None:
        self.adjacencies={}
        self.ind=1
    def Create_vertex(self,data):
        self.adjacencies[Vertex(data,self.get_index())]=list()

    def add_direct_edge(self,source,destination,weight: Optional[float] = None):
        self.adjacencies[source].append(Edge(source,destination,weight))

    def add_undirected_edge(self,source,destination, weight: Optional[float] = None ):
        self.adjacencies[source].append(Edge(source,destination,weight))
        self.adjacencies[destination].append(Edge(destination,source,weight))
        
    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None):
        if(edge==1):
            self.add_direct_edge(source,destination,weight)
        elif(edge==2):
            self.add_undirected_edge(source,destination,weight)
    def __str__(self) -> str:
        for x in graf.adjacencies.keys():
            print(x.data,":",end='')
            for y in self.adjacencies[x]:
                print(y.destination.data, end=',')
            print("")
        return " "
    def get_index(self):
        return len(self.adjacencies)
    def BFS(self, s):
        visited=[]
        print(s.data)
        visited.append(s)
        queue=Queue()
        queue.enqueue(s)
        while(len(queue)!=0):
            for x in self.adjacencies[queue.dequeue().value]:
                jest_na_liscie=False
                for y in range(0,len(visited)):
                    if(x.destination.data==visited[y].data):
                        jest_na_liscie=True
                if(jest_na_liscie==False):
                        print(x.destination.data)
                        queue.enqueue(x.destination)
                        visited.append(x.destination)
            queue.dequeue()
    def DFT (self,v,visited=list()):
        
        wystapil=0
        for x in range(0,len(visited)):
            if(v==visited[x]):
                wystapil=1
        if (wystapil==0):
            print(v.data)
            visited.append(v)
            for x in self.adjacencies[v]:
                self.DFT(x.destination,visited)
    
class GraphPath:
    def __init__(self,start,end,grafik=Graph()) -> None:
        self.start=start
        self.end = end
        self.grafik=grafik
        
    def szukaj_wszerz(self):
        path=Queue()
        droga=[self.start]
        visited=[]
        visited.append(self.start)
        path.enqueue(droga)
        while(len(path)!=0):
            now=path.dequeue().value
            v=now[-1]
            for n in self.grafik.adjacencies[v]: 
                visit=False
                for y in range(0,len(visited)):
                    if(n.destination.data==visited[y].data):
                        visit=True
                if(visit==False):
                    np=[]
                    for x in now:
                        np.append(x)
                    np.append(n.destination)
                    visited.append(n.destination)
                    path.enqueue(np)
                    if(n.destination==self.end):
                        for x in np:
                            print(x.data)

def paths_count(graf : Graph,a,b,visited=[],pomoc: Optional[int]=0):
    visited=visited
    if (a in visited):
        return 
    visited=visited+[a]
    for x in graf.adjacencies[a]:
        visit=False
        for y in range(0,len(visited)):
                if(x.destination==visited[y]):
                        visit=True
        if(visit==False):
            if(x.destination==b):
                pomoc=pomoc+1
            else:
                pomoc=paths_count(graf,x.destination,b,visited,pomoc)       
    return pomoc
  

graf=Graph()
# graf.Create_vertex("v0")
# graf.Create_vertex("v1")
# graf.Create_vertex("v2")
# graf.Create_vertex("v3")
# graf.Create_vertex("v4")
# graf.Create_vertex("v5")
# key_list = list(graf.adjacencies.keys())
# graf.add_direct_edge(key_list[0], key_list[1])
# graf.add_direct_edge(key_list[0], key_list[5])
# graf.add_direct_edge(key_list[2], key_list[1])
# graf.add_direct_edge(key_list[2], key_list[3])
# graf.add_direct_edge(key_list[3], key_list[4])
# graf.add_direct_edge(key_list[4], key_list[1])
# graf.add_direct_edge(key_list[4], key_list[5])
# graf.add_direct_edge(key_list[5], key_list[1])
# graf.add_direct_edge(key_list[5], key_list[2])

# # ============================
# graf.Create_vertex("A")
# graf.Create_vertex("B")
# graf.Create_vertex("C")
# graf.Create_vertex("D")

# key_list = list(graf.adjacencies.keys())
# graf.add_direct_edge(key_list[0],key_list[1])
# graf.add_direct_edge(key_list[0],key_list[2])
# graf.add_direct_edge(key_list[2],key_list[1])
# graf.add_direct_edge(key_list[2],key_list[3])
# graf.add_direct_edge(key_list[1],key_list[3])
# ==================
graf.Create_vertex(0)
graf.Create_vertex(1)
graf.Create_vertex(2)
graf.Create_vertex(3)
graf.Create_vertex(4)
graf.Create_vertex(5)
graf.Create_vertex(6)
graf.Create_vertex(7)
key_list=list(graf.adjacencies.keys())
graf.add_direct_edge(key_list[0],key_list[1])
graf.add_direct_edge(key_list[1],key_list[2])
graf.add_direct_edge(key_list[1],key_list[3])
graf.add_direct_edge(key_list[2],key_list[5])
graf.add_direct_edge(key_list[4],key_list[1])
graf.add_direct_edge(key_list[4],key_list[6])
graf.add_direct_edge(key_list[5],key_list[4])
graf.add_direct_edge(key_list[6],key_list[3])
graf.add_direct_edge(key_list[7],key_list[5])

print(graf)

print("wynik:",paths_count(graf,key_list[0],key_list[3]))

# graf.DFT(key_list[0])
# graf.show()

# paths_count(graf,key_list[0],key_list[5])