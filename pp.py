def check_vowel(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)

string = 'omkar parab'
vowels = 'AEIOUaeiou'
check_vowel(string, vowels)
