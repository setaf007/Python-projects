def findVowel(letter):
    vowels = 'aeiou'
    return letter in vowels


letter = input("Enter letter: ")
if (findVowel(letter) == True):
    print("Letter is a vowel")
else:
    print("Letter is not a vowel")
