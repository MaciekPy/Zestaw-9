class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0   # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):   # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(n)
        if self.head:   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:   # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:   # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        return node   # zwracamy usuwany node

    def search(self, data):   # klasy O(n)
        # Zwraca łącze do węzła o podanym kluczu lub None.
        node = self.head
        while node.next != None:
            if node.data == data:
                return node
            node = node.next
        if self.tail.data == data:
            node = self.tail
            return node
        return None

    def find_min(self):  # klasy O(n)
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.
        node = self.head
        minVal = float('inf')
        while node.next != None:
            if node.data < minVal:
                minVal = node.data
            node = node.next
        if self.tail.data < minVal:
            minVal = self.tail.data
        return minVal

    def find_max(self):   # klasy O(n)
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.
        node = self.head
        maxVal = float('-inf')
        while node.next != None:
            if node.data > maxVal:
                maxVal = node.data
            node = node.next
        if self.tail.data > maxVal:
            maxVal = self.tail.data
        return maxVal

    def reverse(self):   # klasy O(n)
        # Odwracanie kolejności węzłów na liście.
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print(self):
        node = self.head
        while node != None:
            print("[" + str(node.data) + "]")
            node = node.next


alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
print("length {}".format(alist.length))  # odczyt atrybutu
print("length {}".format(alist.count()))  # wykorzystujemy interfejs

node1 = Node()
node2 = Node()
node3 = Node()
node1 = alist.search(33)
node2 = alist.find_min()
node3 = alist.find_max()
print("Found : " + str(node1) + "\nMinVal : " +
      str(node2) + "\nMaxVal : " + str(node3))

print("Przed Reverse: ")
alist.print()
alist.reverse()
print("Po Reverse: ")
alist.print()
