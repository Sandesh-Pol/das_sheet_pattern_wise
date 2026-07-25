class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end="- > ")
            temp = temp.next
        
        print('None')


    # insert at front 
    def insert_fr(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new


    # insert at end 
    def insert_end(self,data):
        new = Node(data)
        new.next = None

        if self.head is None:
            self.head = new
            return
        
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new

    # insert at pos
    def insert_pos(self, pos, data):

        if pos == 0:
            self.insert_front(data)
            return

        new = Node(data)

        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new.next = temp.next
        temp.next = new

    def delete_fr(self):
        if self.head:
            self.head = self.head.next

    
    def delete_end(self):

        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        temp = self.head

        while temp.next:

            temp = temp.next

        temp.next = None


    def delete_pos(self,pos):

        if self.head is None:
            return
        
        if pos==1:
            self.delete_fr()
            return
        
        temp = self.head

        for _ in range(pos-1):

            if temp.next is None:
                return
            
            temp = temp.next

        if temp.next is None:
            return
        
        temp.next = temp.next.next


    def length(self):

        count = 0

        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count

    def search(self, value):

        temp = self.head

        while temp:

            if temp.data == value:
                return True

            temp = temp.next

        return False
    

ll = LinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.insert_fr(5)
ll.insert_pos(15,2)

ll.display()

print("Length:", ll.length())
print("Search 20:", ll.search(20))

ll.delete_fr()
ll.delete_end()
ll.delete_pos(1)

ll.display()

        

        
        





        




    
