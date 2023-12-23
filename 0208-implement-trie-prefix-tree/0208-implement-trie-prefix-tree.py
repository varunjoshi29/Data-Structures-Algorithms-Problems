class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWordEnd = False 

class Trie:

    def index(self, char):
        return ord(char) - ord('a')
    
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        current = self.root

        for i in range(len(word)):

            index = self.index(word[i])
            if current.children[index]:
                current = current.children[index]
            else:
                current.children[index] = TrieNode()
                current = current.children[index]
            
        current.isWordEnd = True


    def search(self, word: str) -> bool:
        current = self.root

        for i in range(len(word)):

            index = self.index(word[i])
            if current.children[index]:
                current = current.children[index]
            else:
                return False

        return current.isWordEnd

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for i in range(len(prefix)):
            index = self.index(prefix[i])
            if current.children[index]:
                current = current.children[index]
            else:
                return False

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)