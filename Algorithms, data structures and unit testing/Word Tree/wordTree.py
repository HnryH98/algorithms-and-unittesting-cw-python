from collections import Counter#for counting repeating words
from string import punctuation#for removing punctuation from words
    

'''Read file and then store unique words as nodes in a binary tree.
Then allow searching the nodes.
Can also print the tree in pre-order'''


def createTree(fileToRead):
    '''Reads file: "fileToRead.txt". Then splits unique words into a list. 
    Keeps track of repeating words. Decapitilises characters. Removes punctuation from words. 
    Then calls a function to insert the words into the BST.'''
    fullWordList = []#all words read from file
    uniqueWordList = []#unique words from file


    
    
    fullWordList = readFile(fileToRead)
    if fullWordList == 0:#if file was empty or invalid, end
        print ("Could not create tree.")
        return 0

    uniqueWordList = removeReapetedWords(fullWordList)
        
    tree=treeInsert(None,uniqueWordList.pop(0));#base node

    
    for word in uniqueWordList[1:]:
        treeInsert(tree,word)
    return tree

def readFile(fileToRead):
    '''createTree() helper function.
    Read a file and return words it contains as a list'''
    
    fileWordList = []
    if (isinstance(fileToRead, str)==False) or (punctuation in fileToRead):
        raise Exception("Invalid file name") 
        return 0
    
    try:
        f = open(fileToRead + '.txt')
        for line in f:
            fileWordList += line.split()
        f.close()

        if len(fileWordList) < 1:
            print("File empty")
            return 0
        else:
            print(fileWordList)
            return fileWordList
    
    except FileNotFoundError:
        print('File does not exist')
        return 0



    
def removeReapetedWords(wordList):
    '''Remove repeated words from a list'''
    repetition = Counter()#store num of repetitions for each word

    
    uniqueWordList =[]
    for word in wordList:#remove punctuation and decapitalise characters
        for c in punctuation:
            word= word.replace(c,"")#remove punctuation
        word = word.lower()#decapitalise
        if word in uniqueWordList:
            repetition[word]+=1
        else:
            uniqueWordList.append(word)
    return uniqueWordList
    



class BinTreeNode(object):
    '''This class is used to initiate and store the BST nodes and their attributes
        Attributes:
             word is any word stored in the BST
             left is used to connect the node to its left child
             right is used to connect the node to its right child
             parent is used to connect the node to its parent'''
    def __init__(self, word, parent):
        self.word=word 
        self.left=None 
        self.right=None
        self.parent=parent 
        
 
       
def treeInsert(tree, insertWord):
    '''Recursive function: Inserts word into the BST by comparing words'''
    if tree==None:
        tree=BinTreeNode(insertWord,None)
    else:
        if insertWord > tree.word:
            if tree.right==None:
                tree.right=BinTreeNode(insertWord,tree)#insert insertWord as a right child to tree
            else:
                treeInsert(tree.right,insertWord)
        else:
            if tree.left==None:
                tree.left=BinTreeNode(insertWord,tree)#insert insertWord as a left child to tree
            else:
                treeInsert(tree.left,insertWord)
    return tree


        
def searchNode (tree, searchWord): 
    '''Recursive function: Searches the BST for searchWord.
    Prints the path traversed from searching for it. '''
    if tree==None:
        print("NO The node was not found")
        return 0
    else:       
        print(tree.word)#Prints the path traversed while searching for searchWord
        if tree.word==searchWord:
            print ("YES The node was found")            
            return 1
        else:
            if tree.word>searchWord:
                return searchNode(tree.left,searchWord)
            if tree.word<searchWord:
                return searchNode(tree.right,searchWord)

def inorder(tree):
    '''Recursive function: returns a list of the the tree in alphabetical order'''
    traversalList = []
    if tree != None:
        traversalList = inorder(tree.left)
        traversalList.append(tree.word)
        traversalList = traversalList + inorder(tree.right)
    return traversalList

def preorder(tree):
    '''Recursive function: Prints the tree in preorder'''
    rest= []
    if tree == None:
        print("Tree does not exist.")
        return 

    print(tree.word)
    if (tree.left!=None):
        preorder(tree.left)
    if (tree.right!=None):
        preorder(tree.right)
     

def postorder(tree):
    '''Recursive function: Prints the tree in postorder'''

    if tree == None:
        print("Tree does not exist.")
        return
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.word)



 
if __name__ == '__main__':
    tree =  createTree("fileToRead")
    preorder(tree)
    postorder(tree)
    print(inorder(tree))

    print("______________")
    searchNode(tree, "publication")


 
    
