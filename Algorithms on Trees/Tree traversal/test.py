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

    def preorder(self,root):   # Root --> Left --> Right
        if(root==None):
            return;                          #Hint
        print(root.data,end=" ");            #Root
        self.preorder(root.left);            #Left
        self.preorder(root.right);           #Right

obj=BST();



obj.insert(60);
obj.insert(40);
obj.insert(30);
obj.insert(50);
obj.insert(20);
obj.insert(35);
obj.insert(45);
obj.insert(55);
obj.insert(70);
obj.insert(65);
obj.insert(75);
obj.insert(63);
obj.insert(68);
obj.insert(72);
obj.insert(80);

rootNode=obj.returnRoot();
obj.preorder(rootNode);

