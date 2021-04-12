#8. Write a Python class to reverse a string word by word.
class InverseString:

    def getString(self):
        self.string = input("Enter a string: ")
        return self.string

    def inverse(self):
        return self.string[::-1]

a = InverseString()
a.getString()
print(a.inverse())
