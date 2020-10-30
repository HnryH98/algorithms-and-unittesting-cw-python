import unittest
import wordTree
import os

class TestWordTree(unittest.TestCase):

    def setUp(self):
        f = open("testFile.txt", "w")
        f.write("This text is for testing the wordTree code. A file will be created containing these words before each test and will be deleted after each tests is run")
        f.write("This is $another.... line. ")
        f.write("capitalword")
        f.close()

    def tearDown(self):
        os.remove("testFile.txt")
        print("goodbye")

    def test_inorder(self): 
        tree = wordTree.createTree("testFile")
        result = wordTree.inorder(tree)
        print("RESULT: ", result)
        expectedResult = ['a', 'after', 'and', 'another', 'be', 'before', 'capitalword', 'code', 'containing',
                          'created', 'deleted', 'each', 'file', 'for', 'is', 'line', 'runthis', 'test', 'testing',
                          'tests', 'the', 'these', 'this', 'will', 'words', 'wordtree']
        self.assertEqual(result, expectedResult)
        self.assertNotEqual(result, ['a'])

    def test_searchForNonExistingWord(self):
        tree = wordTree.createTree("testFile")
        result = wordTree.searchNode(tree, "safdsdf")
        self.assertEqual(result, 0)

    def test_searchForExistingWord(self):
        tree = wordTree.createTree("testFile")
        result = wordTree.searchNode(tree, "file")
        self.assertEqual(result, 1)

    def test_searchForWordThatWasAttachedToPunctuation(self):
        tree = wordTree.createTree("testFile")
        result = wordTree.searchNode(tree, "another")
        self.assertEqual(result, 1)

    def test_searchForWordThatWasCapitalised(self):
        #check that words are converted to lower case
        tree = wordTree.createTree("testFile")
        result = wordTree.searchNode(tree, "capitalword")
        self.assertEqual(result, 1)

 
'''
    def test_createTreeWithInvalidFileName(self):
        result = wordTree.createTree("testFile")
        self.assertEqual(result, 0)

    def test_createTreeWithValidFile(self):
        result = wordTree.createTree("fileToRead")
        self.assertNotEqual(result, 0)
'''        

if __name__ == '__main__':
    unittest.main()
