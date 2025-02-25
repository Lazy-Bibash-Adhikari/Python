
def getIntInput(prompt):

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def getYesNoInput(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ["y","n"]:
            return response == "y"
        print("Invalid input. Please enter 'y' or 'n'.")

