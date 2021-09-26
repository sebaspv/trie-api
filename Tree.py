class Node:
    '''
    Trie node class.
    Receives a string and yields its available next characters.
    '''
    def __init__(self):
        self.words = {}
        self.end = False
    def search_words(self, prefix):
        if self.end:
            yield prefix # yield words with available prefix
        # get autocompletion from root
        for curr_char, child in self.words.items():
            yield from child.search_words(prefix + curr_char)
    
class Trie:
    '''
    Trie search tree class.
    All of the characters are composed of the Node() class.
    '''
    def __init__(self):
        self.root = Node() # initialize tree from empty node

    def add_word(self, word):
        """Insert word to Trie"""
        current = self.root
        for char in word:
            node = current.words.get(char)
            if not node:
                node = Node()
                current.words[char] = node # add character to word set
            current = node
        current.end = True # end node when there are no more characters

    def remove_word(self, word):
        """Remove given word from Trie"""
        current = self.root
        if self.search_word(word):
            for char in word:
                current = current.words[char] # remove from root if word exists
            current.end = False

    def search_word(self, word):
        """Search if word is in Trie"""
        current = self.root
        for char in word:
            node = current.words.get(char) # get char from word searched
            if not node:
                return False # return false if word not in trie
            current = node
        return current.end # if word isn't finished, continue
            
    def prefix_word(self, prefix):
        """Create word suggestions stored in Trie from a given prefix"""
        curr = self.root
        for char in prefix:
            curr = curr.words.get(char) # search for character in trie
            if curr is None:
                return # return empty if no words have prefix
        yield from curr.search_words(prefix) # yield words with prefix

    def get_prefixes(self, keyword):
        """Return words as string which starts with keyword"""
        return list(self.prefix_word(keyword))

    def get_words(self):
        """List stored words in Trie"""
        return  list(self.prefix_word(""))

    def display_trie(self):
        return self.root