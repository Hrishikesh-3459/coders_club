# Write a program to check whether a character is vowel or consonant
c = input("Enter a character: ")
if c.lower() in ["a", "e", "i", "o", "u"]:
    print("The entered character is a vowel")
else:
    print("The entered character is a consonant")
    