"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        self.length += 1
        current_head = self.head
        self.head = ListNode(value, None, current_head)
        if current_head:
            current_head.prev = self.head
            self.head.next = current_head
        if not self.tail:
            self.tail = self.head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        self.length -= 1
        current_head = self.head
        if current_head and current_head.next:
            current_head.next.prev = None
            self.head = current_head.next
            return current_head.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        self.length += 1
        current_tail = self.tail
        self.tail = ListNode(value, current_tail, None)
        if current_tail:
            current_tail.next = self.tail
        if not self.head:
            self.head = self.tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        self.length -= 1
        current_tail = self.tail
        if current_tail and current_tail.prev:
            current_tail.prev.next = None
            self.tail = current_tail.prev
            return current_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        current_node = node
        current_head = self.head
        if current_node and current_head and current_node != current_head and current_node != self.tail:
            # remove from dll by pointing current node's prev and next to eachother
            if current_node.next:
                current_node.next.prev = current_node.prev
            if current_node.prev:
                current_node.prev.next = current_node.next
            # set current node as new head
            self.head = current_node
            # point current node's next to current head
            self.head.next = current_head
            # set current head's prev to current node
            current_head.prev = self.head

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        current_node = node
        current_tail = self.tail
        if current_node and current_tail:
            # remove from dll by pointing current node's prev and next to eachother
            if current_node.next:
                current_node.next.prev = current_node.prev
            if current_node.prev:
                current_node.prev.next = current_node.next
            # set current node as new tail
            self.tail = current_node
            # point current node's prev to current tail
            self.tail.prev = current_tail
            # set current tail's next to current node
            current_tail.next = self.tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        current_node = node
        if current_node:
            print("this ran")
            if (current_node != self.head or current_node != self.tail) and current_node.next and current_node.prev:
                print("delete not ran")
                self.length -= 1
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
            elif current_node == self.head and current_node != self.tail:
                print("delete head ran")
                self.remove_from_head()
            elif current_node == self.tail and current_node != self.head:
                print("delete tail ran")
                self.remove_from_tail()
            elif current_node == self.head and current_node == self.tail:
                print("delete only one ran")
                self.length = 0
                self.tail = None
                self.head = None
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        current = self.head
        highest_value = current.value
        while current.next is not None:
            current = current.next
            if current.value > highest_value:
                highest_value = current.value
        return highest_value

dll = DoublyLinkedList()
dll.add_to_tail(1)
dll.add_to_head(9)
dll.add_to_tail(6)
print(f"check this {dll.head.value}")
print(f"check this {dll.head.next.value}")
print(f"check this {dll.tail.value}")
dll.remove_from_head()

print(f"check this {dll.head.value}")

# print(ListNode(1, None, 3).next)

