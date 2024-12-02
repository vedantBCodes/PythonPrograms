#Inserting a node in Binary Search Tree (BST)

# Creating a node for BST

class Node:
    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;

class BST:
    def __init__(self):
        self.root=None;

    def insert(self,value):
        newNode=Node(value);
        if(self.root==None):
            self.root=newNode;
        else:
            temp=self.root;
            while(temp!=None):
                if(value<temp.data):
                    if(temp.left==None):
                        temp.left=newNode;
                        break;
                    else:
                        temp=temp.left;
                else:
                    if(temp.right==None):
                        temp.right=newNode;
                        break;
                    else:
                        temp=temp.right;


