from typing import Union, Dict


CONTINUE = 'CONTINUE'
ACCEPT = 'ACCEPT'
TRAP = 'TRAP'

DFA_State = Union[CONTINUE, ACCEPT, TRAP]

class State:
    def __init__(self):
        self.next_states: Dict[str, State] = {}
        self.is_accept: bool = False


class DFA:
    def __init__(self):
        self.initial: State = State()
        self.current: State = self.initial
        self.previous_status = None


    def insert(self, word: str) -> None:
        current = self.initial

        for c in word:
            if c not in current.next_states:
                current.next_states[c] = State()
            current = current.next_states[c]
        current.is_accept = True


    def step(self, character: str) -> DFA_State:
        if character in self.current.next_states:
            self.current = self.current.next_states[character]
            if self.current.is_accept:
                self.reset()
                return ACCEPT
            return CONTINUE
        self.reset()
        return TRAP


    def step_and_check(self, character: str) -> tuple[DFA_State, bool]:
        status = self.step(character)
        is_start_of_a_match = self.previous_status == TRAP and status == CONTINUE
        self.previous_status = status
        return status, is_start_of_a_match


    def reset(self) -> None:
        self.current = self.initial