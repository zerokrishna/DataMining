def is_palindrome(word):
    rev = ''
    for ch in word:
        rev = ch + rev
    if rev == word:
        return True
    else:
        return False
    
word = input('Enter a word: ')
if(is_palindrome(word)):
    print('Word is palindrome')
else:
    print('Word is not palidrome')