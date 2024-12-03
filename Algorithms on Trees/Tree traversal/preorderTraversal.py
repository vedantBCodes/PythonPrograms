#Pre-order Tree traversal

# Creating a node

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

    def returnRoot(self):
        return self.root;
    def preorder(self,root):
        if(root==None):
            return;
        print(root.data,end=" ");
        self.preorder(root.left);
        self.preorder(root.right);

obj=BST();
obj.insert(50);
obj.insert(10);
obj.insert(5);
obj.insert(15);
obj.insert(20);
obj.insert(12);
obj.insert(70);
obj.insert(55);
obj.insert(80);

rootNode=obj.returnRoot();
obj.preorder(rootNode);

