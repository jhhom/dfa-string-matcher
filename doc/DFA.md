The DFA is implemented using a class. The basic unit of a DFA is the individual state. The state is implemented as a class that stores a hash map and a boolean flag. The hash map represents state transitions as a mapping of a word character to the next state. Each state also stores a boolean flag that tells if the state is an accepting state. The DFA class consists of 3 object variables, (1) the initial state, (2) the current active state, (3) the previous status of the DFA. The current active state is the state that the DFA is in when processing a character. It can be thought of as the state that our finger points to when we are tracing whether a DFA accepts or rejects a word. The previous status of DFA is used for the purpose of checking if a character is the beginning of a match, if it is we would like to store the position of the match. The previous status refers to whether the current state results from the transition of the preceding character.

The DFA class contains 4 methods, (1) insert, (2) step, (3) step_and_check, and (4) reset. The insert method is used to construct, build or extend the DFA to be able to match for the newly inserted pattern along with the existing patterns. The step method takes in the next character of the word and updates the DFA, mainly it updates the current active state, or the state that our finger points to. The step_and_check method steps through the word character by character and also checks if the character is the beginning of a possible word or match. The reset method resets the DFA, by updating the state that our finger points to, to the initial state of the DFA.

<br>

**The procedure of the `insert` method is as follows:**

1. Given we want to insert a new pattern to match, say “Malaysia”. Walk through the DFA to see if there is a path of transitions that match each of the characters in the word.

2. Let’s say there is a path with the prefix “Mal”, but after “Mal”, we arrive at a state where there is no available transition for the next character “a”.

3. In such a case where there is only a path in the DFA that matches the prefix of the word up to a certain length and not the full word, we will add new states and along the states, we add transitions to connect them using each remaining character in the word. The last added state after the transition of the last “a” in “Malaysia” will be flagged as an “accepting” state.

4. On the other hand, in the case that there is a path of transitions in the DFA that match the full word “Malaysia” character by character, we will flag the state after the transition of the last “a” in “Malaysia” as an accepting state if the state is not already an accepting state.

5. With that, the DFA now is able to match for the new pattern in addition to the existing patterns it is able to match.

<br>

**The procedure of the `step` method is as follows:**

1. Takes in one character from a paragraph or a word

2. Check if there is an available transition for the character. An available transition is indicated by having a mapping of the character to the next state in the hashmap of the current active state of the DFA (i.e the state that our finger currently points to)

3. If there is no available transition, returns “TRAP” to indicate that DFA is in a trap state

4. If there is available transition, updates the current active state of the DFA (i.e the state that our finger currently points to) to the next state after transition

5. If there is available transition and the next state is an accepting state, return “ACCEPT” to indicate that DFA is in an accepting state

6. If there is available transition but the next state is not an accepting state, return “CONTINUE” to indicate that DFA is in process of matching a possibly accepted word

<br>

**The procedure of the `step_and_check` method is as follows:**

1. Takes in one character from a paragraph or a word

2. Runs the procedure of step as above

3. Determines if this character is the first character of a possibly accepted word by checking if DFA is in a trap state when processing the preceding character and the DFA is in “CONTINUE” state, or has available transition for currently processed character

<br>

**The procedure of the `reset` method is as follows:**

1. Set the current active state of DFA (i.e the state that our finger points to), to the initial state of DFA.
2. The DFA is now reset and can be used to match for a new word.
