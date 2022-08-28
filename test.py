
class Node:
    def __init__(self,data=None):
        self.data = data 
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self, head=None, tail=None):
        self.head= head
        self.tail= tail

    def insert(self,data):
        entry = Node(data)
        if self.head is None:
            self.head = entry
            return

        current = self.head
        while(True):
            if(current.next is None):
                current.next = entry
                entry.prev = current
                self.tail = current.next
                break
            current = current.next
            
    def display(self):
        current = self.head
        while(current is not None): 
            print( current.data, "->", end=" ")
            current = current.next
        print("None")
            

    def length(self):
        count=0
        current = self.head
        while (current != None):
            count+=1
            current = current.next
        return count

    def get(self, index):
        current_index=0
        current = self.head
        while (current_index != index):
            current = current.next
            current_index+=1
        return current.data

    def delete(self, index):
        current_index=0
        current=self.head
        while(current_index != index):
            prev = current
            current = current.next
            current_index+=1
        prev.next = current.next

    def merge(self, list1):
        current = dummy = Node(0)
        while (list1 != None or self.head != None):
            if (list1.data <= list2.data):
                current.next = list1
                list1=list1.next
            else:
                current.next = list2
                list2=list2.next
        if not list1:
            current.next = list2
        else:
            current.next = list1
        return dummy.next
    def repeated(self):
        current = New = self.head
        while(True):
            if current == self.head:
                New.next = current
            else:
                i=0
                while(i<self.length):
                    if current.data == self.get(i):
                        self.delete(current)
                    else:
                        i+=1
                New.next = current
            current = current.next
            if current == None:
                break
        New.display()
    def middle(self):
        current = self.head
        middle = self.length() // 2
        while(current.data != self.get(middle)):
            current = current.next
        while(current is not None):
            print(current.data, "->", end=" ")
            current = current.next
        print("None")
    def reverse(self):
        current = self.tail
        while(current is not None):
            print(current.data, "->", end=" ")
            current = current.prev
        print("None")
    def sortedsum(self, alist):
        current = self.head
        ptr2 = alist.head
        while(current.next is not None):
            sum1 = (current.data + ptr2.data)
            current.data = sum1 % 10
            current = current.next
            current.data += sum1//10
            ptr2 = ptr2.next
        current.data = current.data + ptr2.data
    def oddfirst(self):
        dummy = Node(0)
        odd = self.head
        while(odd.next.next is not None):
            odd = odd.next.next
            dummy.next = odd 
            dummy = dummy.next
        even = self.head.next
        while(even.next.next is not None):
            dummy.next = even
            even = even.next.next
            dummy = dummy.next



list1 = linkedlist()
list2 = linkedlist()
list3 = linkedlist()

list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
list1.insert(5)
list1.insert(6)

list1.oddfirst()
list1.display()
