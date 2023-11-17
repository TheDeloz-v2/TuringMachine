from FileReader import FileReader
from Tape import Tape


class TuringMachine:
    def __init__(self, filename):
        file = FileReader(filename)
        # By now, file has all the information we need to build the Turing Machine.
        self.states = file.states
        self.alphabet = file.alphabet
        self.tape_alphabet = file.tape_alphabet
        self.initial_state = file.initial_state
        self.accepting_states = file.accepting_states
        self.transition_function = file.transition_function

        self.current_state = self.initial_state
        self.tape = None

    def run(self, input_string):
        self.tape = Tape(input_string, self.tape_alphabet)
