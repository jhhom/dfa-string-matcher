There are three helper functions, (1) `new_dfa_from_patterns`, (2) `match_paragraph`, (3) `display_match_infos`.

`new_dfa_from_patterns` method constructs DFA given a list of patterns by simply running the DFA insert method for each of the patterns.

`match_paragraph` finds words matched by the DFA given an input text and returns the information of the matches. The information consists of the pattern matched, the positions of the starting and ending character of the word.

`display_match_infos` visualize the patterns found in the input text.

The `match_paragraph` function is the main function that runs the DFA against the paragraph and gets all the matching words.

<br>

**The procedure of `match_paragraph` is as follows:**

1. For each character in the paragraph, pass the character to DFA for processing using the `step_and_check` method.
2. As detailed above, the DFA’s `step_and_check` will receive the character and transition to the next state. If there is no available transition, it will indicate that it is in a trap state by returning two flags to indicate its status. First flag indicates whether it is matching the beginning of a word. Second flag to indicate whether it is in a trap state, accepting state, or in the middle of a match.
3. Based on the flags returned by the DFA, match_paragraph function records the match information. If DFA is in an accepting state, it will add the matched word thus far, along with the starting and ending position of the word into an array. If DFA is in the beginning of a match, it will record the position of the character and initialize the matched word to the character. If the DFA is in the middle of a match, it will concatenate the next character to the matched string thus far. If the DFA is in a trap state, it will reset the matched string to an empty string.
4. Finally, the function will return the array storing the information of every occurrence of pattern matched by the DFA in the input text.
