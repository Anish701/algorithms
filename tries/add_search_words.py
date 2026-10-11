class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        itr = self.root
        for c in word:
            if c not in itr.children:
                itr.children[c] = TrieNode()
            itr = itr.children[c]
        itr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(start: int, node1: TrieNode) -> bool:
            itr = node1
            for i in range(start, len(word)):
                if word[i] == '.':
                    for node in itr.children.values():
                        if dfs(i + 1, node):
                            return True
                    return False
                else:
                    if word[i] not in itr.children:
                        return False
                    itr = itr.children[word[i]]
            return itr.word

        return dfs(0, self.root)
