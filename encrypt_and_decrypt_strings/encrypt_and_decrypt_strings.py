from typing import List

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        # We need to map the keys to the values.
        self.word_key_val = {k : v for k, v in zip(keys, values)}
        # Crucially, we encrypt all the dictionary values as well.
        # This is the key. It transforms a one to many mapping
        # to a simply counting instances.
        self.list = [self.encrypt(word) for word in dictionary]

    def encrypt(self, word1: str) -> str:
        encrypted = ""
        # We need to map the word to the dictionary letter by letter.
        # Thus we loop and add the value to the word.
        #In the case that the letter isn't in the keys, you must return "".
        for c in word1:
            if c in self.word_key_val:
                encrypted += self.word_key_val[c]
            else:
                return ""
        return encrypted

    def decrypt(self, word2: str) -> int:
        # Since we have already precomputed the values in dictionary,
        # we can just count instances of the encryption within the list.
        count = 0
        for word in self.list:
            if word == word2:
                count += 1
        return count

encrypter = Encrypter(["a", "b", "c"], ["gh", "ij", "gh"], ["abc", "cba", "aac"])
encrypted = encrypter.encrypt("abc")
count = encrypter.decrypt(encrypted)

# ghijgh, 2
print(f"{encrypted}, {count}")
