#Write a Python program to import built-in array module and display the namespace of the said module.
import array as arr
print(arr.__name__)
for name in arr.__dict__:
    print(name)
