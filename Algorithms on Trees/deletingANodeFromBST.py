# Deleting a node from a Binary Search Tree (BST)

class Node:
    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;

class BST:
    def __init__(self):
        self.root=None;

    def delete(self,value):
        temp=self.root;
        parent=None;
        #Find the node to delete and its parent
        while(temp!=None or temp.data!=value):
            parent =temp;
            if(value<temp.data):
                temp=temp.left;
            else:
                temp=temp.right;
        if(temp==None):
            print(f"value {value} not found");
            return self.root;
        else:   # Value found
             # Case 1 : if the node has no child nodes
             if(temp.left==None and temp.right==None):
                 if(parent.left==temp):
                     parent.left=None;
                     return self.root;
                 else:
                     parent.right=None;
                     return self.root;

             # Case 2 : if the node has only one child
             if(temp.left==None and temp.right!=None):
                 if(parent.left==temp):
                     parent.left=temp.right;
                 else:
                     parent.right=temp.right;
             else:
                 if (parent.left == temp):
                     parent.left = temp.left;
                 else:
                     parent.right = temp.left;
             # Case 3 : if the node has both the child nodes
             # In such case , find the in-order successor (smallest node in right subtree)
             if (temp.left != None and temp.right != None):
                 current=temp.right;
                 currentParent=None;
                 while (current.left != None):
                     currentParent=current;
                     current = current.left;
                 # We found the successor , now replace deleting node by the successor
                 temp=current;
                 # Now if the current had any right node then attach the current's parent node with that right node
                 if(current.right!=None):
                     currentParent.left=current.right;
             return self.root;