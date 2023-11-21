from TuringMachine import TuringMachine


def main():
    input_string = "1100011"
    tm = TuringMachine("MachineDefinition.json")
    is_accepted = tm.run(input_string)
    final_string = tm._getFinalString()
    
    if is_accepted:
        print(f"\nThe input string '{input_string}' was accepted by the Turing Machine.")
        print(f"The final string is '{final_string}'.")
    else:
        print(f"\nThe input string '{input_string}' was not accepted by the Turing Machine.")

if __name__ == "__main__":
    main()
