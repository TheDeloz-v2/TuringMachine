class Tape:
    def __init__(self, input_string, tape_alphabet):
        self.tape_alphabet = tape_alphabet
        self.input_string = input_string
        self.tape = []
        self.head = 1
        self._init_tape()

    def _init_tape(self):
        """
        This function initializes the tape with the input string.
        :return: None
        """
        self.tape = ["B"] + list(self.input_string) + ["B"]
        self.head = 1

    def get_symbol(self):
        """
        This function returns the symbol under the head.
        :return: The symbol under the head.
        """
        return self.tape[self.head]

    def write_symbol(self, symbol):
        """
        This function writes a symbol to the tape.
        :param symbol: The symbol to write to the tape.
        :return: None
        """
        self.tape[self.head] = symbol

    def move_head(self, direction):
        """
        This function moves the head of the tape.
        :param direction: The direction to move the head. R for right, L for left, S for stay static.
        :return: None
        """
        if direction == "R":
            self.head += 1
            if self.head == len(self.tape):
                self.tape.append("B")
        elif direction == "L":
            self.head -= 1
            if self.head == -1:
                self.tape.insert(0, "B")
                self.head = 0
        elif direction == "S":
            self.head = self.head
        else:
            raise Exception("Invalid direction.")

    def __str__(self):
        """
        This function returns a string representation of the tape.
        :return: A string representation of the tape.
        """
        return_string = ""
        for i in range(len(self.tape)):
            if i == self.head:
                return_string += "[" + self.tape[i] + "]"
            else:
                return_string += self.tape[i]
        return return_string
