# Creating Node class which represents each element in the linked list
class Node:
    def __init__(self,data):
        self.data=data;
        self.next=None;

# LinkedList class to handle the linked list operations
class LinedList:
    def __init__(self):
        self.head=None;   # Initial head of the list is empty

    def  print(self):
        temp=self.head;
        while(temp!=None):
            print(temp.data,end=" ");
            temp=temp.next;
        print("None");

linked_list_obj=LinedList();   #Creating object of LinkedList class which calls the _init_() method of Linked list class
linked_list_obj.print();