# Searching for a node in BST
class Node:
    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;

class BST:
    def __init__(self):
        self.root=None;

    def search(self,value):
        temp = self.root;
        while(temp!=None):
            if(temp.data==value):
                return 1;
            elif(value<temp.data):
                temp=temp.left;
            else:
                temp=temp.right;
        return 0;

