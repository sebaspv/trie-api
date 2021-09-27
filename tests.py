import unittest
from Tree import Trie

class AddingAndDeletingTest(unittest.TestCase):
    def testAddWord(self):
        """Test word adding to Trie"""
        testing_trie = Trie()
        testing_trie.add_word("hello")
        self.assertEqual(testing_trie.get_words(), ["hello"])

    def testRemoveWord(self):
        """Test removing words from Trie"""
        testing_trie = Trie()
        testing_trie.remove_word("hello") # remove previously added word
        self.assertEqual(testing_trie.get_words(), []) # words should now be empty
    
    def testPrefixWord(self):
        testing_trie = Trie()
        """Test getting the correct prefix suggestions from Trie"""
        testing_trie.add_word("hello")
        testing_trie.add_word("hi") 
        testing_trie.add_word("bye") # add multiple words to Trie
        self.assertEqual(testing_trie.get_prefixes("h"), ["hello", "hi"]) # the Trie should suggest both of this words, excluding bye