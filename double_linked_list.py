class Node:
    def __init__(self,value=None):
        self.prev = None
        self.data = value
        self.next = None

class DoubleLinkedList():

    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end="- > ")
            temp = temp.next

        print('None')


    def insert_end(self,value):

        new = Node(value)
        if self.head is None:
            self.head = new
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next  = new
        new.prev = temp


    def insert_fr(self,data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        new.next = self.head
        self.head.prev = new
        self.head = new


    def insert_pos(self, pos, data):

        if pos == 0:
            self.insert_fr(data)
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
        new.prev = temp

        if temp.next is not None:
            temp.next.prev = new

        temp.next = new

    def delete_ll(self, value):

        if self.head is None:
            print("List is empty..!")
            return

        temp = self.head

        if temp.data == value:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            return

        while temp is not None:

            if temp.data == value:

                if temp.next is not None:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                else:
                    temp.prev.next = None

                return

            temp = temp.next

        print("Value not found")

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

ll = DoubleLinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.insert_fr(5)

ll.insert_pos(2, 15)

ll.display()

print("Length:", ll.length())
print("Search 20:", ll.search(20))

ll.delete_ll(10)
ll.delete_ll(20)

ll.display()
