from TuringMachine import TuringMachine


def main():
    tm = TuringMachine("MachineDefinition.json")
    is_accepted = tm.run("000111")
    print(is_accepted)

if __name__ == "__main__":
    main()
