from typing import Union
import json

CONTINUE = 'CONTINUE'
ACCEPT = 'ACCEPT'
TRAP = 'TRAP'


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.current: TrieNode = self.root
        self.previous_status = None

    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.end_of_word = True

    def step(self, character: str) -> Union[CONTINUE, ACCEPT, TRAP]:
        if character in self.current.children:
            self.current = self.current.children[character]
            if self.current.end_of_word:
                self.reset()
                return ACCEPT
            return CONTINUE
        self.reset()
        return TRAP

    def step_and_check(self, character: str):
        status = self.step(character)
        is_start_of_a_match = self.previous_status == TRAP and status == CONTINUE
        self.previous_status = status
        return status, is_start_of_a_match
    
    def reset(self):
        self.current = self.root

    

if __name__ == '__main__':
    trie = Trie()

    toMatch = json.load(open('word_list.json'))
    for match in toMatch:
        trie.insert(match)

    input_text = open('input.txt', 'r').read()
    match_infos = []

    start = 0
    end = None
    match = ''

    for i, char in enumerate(input_text):
        status, is_start = trie.step_and_check(char)
        if status == ACCEPT:
            end = i
            match += char
            match_infos.append((start, end, match))
            match = ''
        elif is_start:
            start = i
            match = char
        elif status == CONTINUE:
            match += char
        elif status == TRAP:
            match = ''

    print(match_infos)
