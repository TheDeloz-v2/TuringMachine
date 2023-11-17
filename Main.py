from TuringMachine import TuringMachine


def main():
    tm = TuringMachine("MachineDefinition.json")
    tm.run("000111")


if __name__ == "__main__":
    main()
