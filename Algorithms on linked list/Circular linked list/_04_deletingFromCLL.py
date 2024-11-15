class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1. Deleting the first node Deletion in circular singly linked list at beginning
def delete_from_front(self):
    if self.head is None:  # List is empty
          print("List is empty. No node to delete.")
          return

    if self.head.next == self.head:   # Only one node in the list
        self.head = None
        return

    # More than one node in the list
    temp = self.head
    temp1 = self.head
    while temp.next != self.head:  # Traverse to the last node
        temp = temp.next
    temp.next = temp1.next  # Update last node to point to second node
    self.head = temp1.next  # Move the head to the next node


# 2. Deleting the last node:circular-singly-linked-list
def delete_from_end(self):
     if self.head is None: # List is empty
        print("List is empty. No node to delete.")
        return

     if self.head.next == self.head: # Only one node in the list
        self.head = None
        return

     temp = self.head
     temp1 = None
# Traverse to the last node
     while temp.next != self.head:
         temp1 = temp
         temp = temp.next

     temp1.next = self.head # Update the second last node to point to head
# temp.next=None

# 3. Deleting a specific node by value
def delete_node(self, key):
    if self.head is None: # List is empty
        print("List is empty.")
        return
    temp = self.head
    temp3 = self.head   # check this line of code again (it may be wrong)
    emp1 = None

# Case 1: If the node to be deleted is the head node
    if temp.data == key:
        if temp.next == self.head: # Single node case
            self.head = None
            return
    while temp.next != self.head: # Traverse to the last node
        temp = temp.next
    temp3.next= self.head
    temp.next = temp3.next # Update the last node's next pointer
    self.head = temp3.next # Move the head to the next node
    return