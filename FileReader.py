import json


class FileReader:
    """
    This class is responsible for reading the Turing Machine definition file and storing the data in the class
    """
    def __init__(self, filename):
        self.filename = filename
        self.states = None
        self.alphabet = None
        self.tape_alphabet = None
        self.initial_state = None
        self.accepting_states = None
        self.transition_function = None

        self._read()  # Read the file and store the data in the class variables.
        self._validate()  # Validate the data read from the file.

    def _read(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.states = data["states"]
                self.alphabet = data["alphabet"]
                self.tape_alphabet = data["tape_alphabet"] + ["B"]
                self.initial_state = data["initial_state"]
                self.accepting_states = data["accepting_states"]
                self.transition_function = data["transition_function"]
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
            exit(1)
        except json.decoder.JSONDecodeError:
            print(f"File {self.filename} is not a valid JSON file.")
            exit(1)
        except KeyError:
            print(f"File {self.filename} is not a valid Turing Machine definition file. Missing key.")
            exit(1)

    def _validate(self):
        """
        This function validates the data read from the file.
        :return: None if the data is valid, otherwise it exits the program.
        """
        pass
