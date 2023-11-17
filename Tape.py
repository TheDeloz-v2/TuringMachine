class Tape:
    def __init__(self, input_string, tape_alphabet):
        self.tape_alphabet = tape_alphabet
        self.input_string = input_string
        self.tape = []
        self.head = 0
        self._init_tape()

    def _init_tape(self):
        """
        This function initializes the tape with the input string.
        :return: None
        """
        self.tape = ["ß"] + list(self.input_string) + ["ß"]
        self.head = 0
