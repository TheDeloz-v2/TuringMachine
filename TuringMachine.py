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

        self.max_transitions = 1000

        self.current_state = self.initial_state
        self.tape = None

    def run(self, input_string):
        """
        This function runs the Turing Machine with the given input string.
        :param input_string: The input string to be processed by the Turing Machine.
        :return: True if the Turing Machine accepts the input string, False otherwise.
        """
        for char in input_string:
            if char not in self.tape_alphabet:
                print(f"Invalid input string: {input_string}")
                print(f"Character '{char}' is not in the alphabet.")
                return False
            
        self.tape = Tape(input_string, self.tape_alphabet)
        call_depth = 0

        while call_depth < self.max_transitions:
            call_depth += 1
            self._print_tape()
            if self.current_state in self.accepting_states:
                return True
            else:
                try:
                    # Perform one step of the Turing Machine. If it fails, by any reason, it will raise an exception.
                    self._step()
                except:
                    return False

    def _step(self):
        """
        This function performs one step of the Turing Machine.
        :return: None
        """
        # Get the current symbol under the head.
        current_symbol = self.tape.get_symbol()
        # Get the transition function for the current state and symbol.
        transition_function = self.transition_function[self.current_state][current_symbol]
        # Get the next state.
        self.current_state = transition_function[0]
        # Write the new symbol.
        self.tape.write_symbol(transition_function[1])
        # Move the head.
        self.tape.move_head(transition_function[2])

    def _print_tape(self):
        print(f"{self.current_state} | {self.tape}")
    
    def _getFinalString(self):
        return self.tape
