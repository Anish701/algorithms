class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.word = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        itr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if not itr.children[index]:
                itr.children[index] = TrieNode()
            itr = itr.children[index]

        itr.word = True        


    def search(self, word: str) -> bool:
        itr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not itr.children[index]:
                return False
            itr = itr.children[index]
        return itr.word


    def startsWith(self, prefix: str) -> bool:
        itr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not itr.children[index]:
                return False
            itr = itr.children[index]
        return True
