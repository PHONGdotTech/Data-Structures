class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
    def __init__(self):
        # first node in the list 
        self.head = None
        self.tail = None

    # def add_to_end(self, value):
    #     # regardless of if the list is empty or not, we need to wrap the value in a Node 
    #     new_node = Node(value)
    #     # what if the list is empty? 
    #     if not self.head and not self.tail:
    #         self.head = new_node
    #     # what if the list isn't empty?
    #     else:
    #         # what node do we want to add the new node to? 
    #         # the last node in the list 
    #         # we can get to the last node in the list by traversing it 
    #         current = self.head 
    #         while current.get_next() is not None:
    #             current = current.get_next()
    #         # we're at the end of the linked list 
    #         current.set_next(new_node)

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_from_end(self):
        # what if the list is empty? 
        if not self.head and not self.tail:
            return None
        # what if the list isn't empty?
        else:
            # what node do we want to remove the last node from? 
            # the last node in the list. keep track with current
            current = self.head
            # use previous to keep track of 2nd to last
            previous = current
            # if the head does not have a next node, it is the only node, so remove it
            if current.get_next() is None:
                self.head = None
                self.tail = None
            else:
                # traverse the list to get the last and next to last element
                while current.get_next() is not None:
                    # before assigning next to current, assign current to previous
                    previous = current
                    current = current.get_next()
                # we're at the end of the linked list
                # set the previous's next node to none to remove the current from list
                previous.set_next(None)
            # return current.value to be printed
            # current.value is head if the only node, else it is last node
            return current.value

    def add_to_head(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
    
    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            self.head = self.head.get_next()
            return value

    def get_length(self):
        if not self.head:
            return 0
        else:
            current = self.head
            length = 1
            while current.get_next() is not None:
                current = current.get_next()
                length = length+1
            return length