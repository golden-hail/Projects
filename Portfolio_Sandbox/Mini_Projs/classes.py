'''
A user interface contains two types of user input controls: TextInput, which accepts all characters and NumericInput, which accepts only digits.

Implement the class TextInput that contains:

Method add(self, character) - adds the given character to the current value

Method get_value(self) - returns the current value

Implement the class NumericInput that:

Inherits TextInput


Overrides the add method so that each non-numeric character is ignored

For example, the following code should output "10":

input = NumericInput()
input.add("1")
input.add("a")
input.add("0")
print(input.get_value())
'''

class TextInput:
    # Set empty constructor for class
    def __init__(self):
        self.value = ""

    # Add the new character
    def add(self, character):
        self.value += character

    # Get value for new self
    def get_value(self):
        return self.value

# Inherit TextInput returned value
class NumericInput(TextInput):
    def add(self, character):
        # Only add the character if it is a digit ('0'-'9')
        # Filter: Check if the character is a digit (passed input as a string so isinstance wont work)
        if character.isdigit():
            # Delegate: Pass valid digits to the parent class's add method
            super().add(character)


if __name__ == '__main__':
    input = NumericInput()
    input.add("1")
    input.add("a")
    input.add("0")
    print(input.get_value())  # Outputs "10"