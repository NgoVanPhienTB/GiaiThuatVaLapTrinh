class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.pre = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def showList(self):
        node = self.tail
        if node is None:
            print("Empty")
        while node is not None:
            print(node.data,end=" ")
            node=node.pre

    def insertAtFirst(self,data):
        node = Node(data)
        if self.head is None:
            self.head=self.tail=node
        else:
            node.next=self.head
            self.head.pre=node
            self.head=node

    def insertAtEnd(self,data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
           node.pre = self.tail
           self.tail.next=node
           self.tail=node

    def insertPosision(self,position,data):
        pass

    def deleteAtFirst(self):
        if self.head is None:
            print("Empty")
        else:
            self.head.next.pre = None
            temp = self.head
            self.head = temp.next
            del temp

    def deleteAtEnd(self):
        if self.head is None:
            print("Empty")
        else:
            self.tail.pre.next=None
            temp = self.tail
            self.tail=temp.pre
            del temp

    def delete(self, key):
        if self.head is None:
            print("Empty")
        else:
            while self.head.data == key:
                temp = self.head.next
                self.deleteAtFirst()
                self.head=temp
            node = self.head
            temp=self.head
            while node is not None:
                if node.data == key:
                   if node.next is None :
                       self.deleteAtEnd()
                   else:
                       temp.next = node.next
                       noneDel = node
                       node = node.next
                       node.pre = temp
                       noneDel.pre=noneDel.next=None
                       del noneDel
                       continue
                temp = node
                node = node.next

    def search(self,node,data):
        if node is None:
            return False
        if node.data==data:
             return True
        return self.search(node.pre,data)
if __name__ == '__main__':
    list = DoubleLinkedList()
    # list.insertAtFirst(1)
    # list.insertAtFirst(5)
    # list.insertAtFirst(3)
    # list.insertAtFirst(6)
    list.insertAtEnd(1)
    list.insertAtEnd(1)
    list.insertAtEnd(1)
    list.insertAtEnd(4)
    list.insertAtEnd(5)
    list.insertAtEnd(6)
    list.insertAtEnd(6)
    list.insertAtEnd(4)
    list.insertAtEnd(1)
    list.insertAtEnd(1)
    list.showList()
    print()
    # list.deleteAtEnd()
    list.delete(6)
    list.showList()
    print(list.search(list.tail,7))
