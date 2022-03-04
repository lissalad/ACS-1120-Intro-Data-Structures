#!python


from tkinter import N


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        
        if self.is_empty():
          return 0

        count = 1
        node = self.head
        while node != self.tail:
          count += 1
          node = node.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty():
          self.head = new_node
          self.tail = new_node
        # TODO: Else append node after tail
        else:
          self.tail.next = new_node
          self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.is_empty():
          self.head = new_node
          self.tail = new_node
        else:
          new_node.next = self.head
          self.head = new_node

    def find(self, item):
      # checks if empty
      if self.is_empty():
        return False

      # checks if item is at the end
      if self.tail.data == item:
        return True

      # loops through nodes
      node = self.head
      while node != self.tail:
        if node.data == item:
          return True
        node = node.next
      return False

# ---------------------------------------------------------------- #
    def delete(self, item):

      # check if listogram is empty
      if self.is_empty():
        raise ValueError('Item not found: {}'.format(item))

      # check if item in listogram
      if not self.find(item):
        raise ValueError('Item not found: {}'.format(item))
      
      # checks if length 1
      if self.head.data == item:
        if self.tail.data == item:
          self.head = None
          self.tail = None
          return

      # checks if head
      if self.head.data == item:
        self.head = self.head.next
        # self.head = None
        print("this was the head")
        return

      # checks if tail
      if self.tail.data == item:
        self.tail = self.previous(self.tail)
        # print(self.tail.next)
        print(self.tail)

        # self.tail.next = None
        print("this was the tail")
        return 

      # loop looks for node item
      node = self.head

      while node != self.tail:
        if node.next != self.tail:
          if node.next.data == item:
            node.next = node.next.next
            return
        else:
          self.tail = node
          node.next = None
          print("new tail")
          return
        node = node.next

      raise ValueError('Item not found: {}'.format(item))

    def previous(self, node):
      before = self.head
      while before != None:
          if before.next == node:
            return before
          before = before.next
      return

if __name__ == "__main__":
  ll = LinkedList(['A', 'B', 'C'])
  assert ll.head.data == 'A'  # First item
  assert ll.tail.data == 'C'  # Last item
  ll.delete('A')
  assert ll.head.data == 'B'  # New head
  assert ll.tail.data == 'C'  # Unchanged
  ll.delete('C')
  assert ll.head.data == 'B'  # Unchanged
  assert ll.tail.data == 'B'  # New tail
  ll.delete('B')
  print("HEAD:")
  print(ll.head)
  assert ll.head is None  # No head
  assert ll.tail is None  # No tail

 # ---------------------------------------------------------------- #
  # test = LinkedList(['E','L',"I","S","S","A"])
  # test.delete("A")
  # print(test.find("A"))
  # print(test)
  # print(test.previous(test.tail).next)

    # my_ll.delete("B")
    # print(my_ll.length())
    # my_ll.delete('E')
    # print(my_ll.previous('F'))
    # my_ll.delete("C")
    # print(my_ll)

    


