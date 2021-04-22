class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def showList(self):
        if self.head is None:
            print('Empty')
        else:
            node = self.head
            while node is not None:
                print(node.data,end=" ")
                node=node.next

    def insertAtStart(self,data):
        node = Node(data)
        if self.head is None:
            self.head=node.next
        else:
            node.next = self.head
            self.head = node

    def insertAtEnd(self,data):
        newNode = Node(data)
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = newNode

    def insertPosition(self,index,data):
        newNode = Node(data)
        node = self.head
        if index == 1 :
            self.insertAtStart(data)
            return
        while index > 2 and node.next is not None:
            node = node.next
            index -= 1

        if node.next is None:
            node.next = newNode
        else:
            newNode.next = node.next
            node.next = newNode

    def deleteAtFirst(self):
        if self.head is None:
            print("Empty")
        else:
            node = self.head
            if node.next is None:
                self.head=None
                del node
            else:
                node1 = node.next
                self.head = node1
                del node

    def deleteAtEnd(self):
        if self.head is None:
            print("Empty")
        else:
            node = self.head
            if node.next is None:
                self.head = None
                del node
            else:
                node1 = None
                while node.next is not None:
                    node1 = node
                    node = node.next
                node1.next = None
                del node

    def deletePosition(self,position):
        if self.head is None:
            print("Empty")
        else:
            if position == 1:
                self.deleteAtFirst()
                return
            else:
                node = self.head
                while position > 2 and node.next is not None:
                    node= node.next
                    position-=1
                if node.next is None:
                    self.deleteAtEnd()
                else:
                    temp = node.next
                    node.next=temp.next
                    del temp


    def delete(self,key):
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
                       temp.next=node.next
                       nodeDel = node
                       node = node.next
                       del nodeDel
                       continue
                temp = node
                node = node.next


    def search(self,key):
        if self.head is not None:
           node = self.head
           count = 0
           while node is not None:
               count+=1
               if node.data == key:
                   return count
               else:
                   node = node.next
           return False
        else:
            print("Empty")


if __name__ == '__main__':

    list = SinglyLinkedList()
    list.head=Node(1)
    list.insertAtStart(2)
    list.insertAtStart(5)
    list.insertAtStart(6)
    list.insertAtStart(9)
    list.insertAtStart(5)
    list.insertAtStart(5)
    list.insertAtEnd(5)
    list.insertPosition(7,10)
    list.showList()
    print()
    # print(list.search(10))
    # list.deleteAtFirst()
    list.delete(5)
    list.showList()



