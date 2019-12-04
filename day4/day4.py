import numpy as np
def possiblePasswords(valueRange):
    passwords = []
    for password in range(valueRange[0], valueRange[1]):
        if check_facts(password):
            passwords.append(password)
    print('Number of possible passwords is: %s' %(str(len(passwords))))
    return passwords

def check_facts(password):
    '''get logical list for list comparison
    6 digit number -> True since puzzle input has range between 6 digits numbers
    adjacent digits are the same -> there has to be a zero when calculating the difference
    Never decrease from left to right -> left digits <= right digit
    '''
    password = list(map(int, list(str(password))))
    for i in range(len(password)-1):
        if not all(password[i] <= p for p in password[i:]):
            return False
        if 0 not in [p[0] - p[1] for p in list(zip(password[:-1], password[1:]))]:
            return False
    return True

def possiblePasswordsDigits(passwords):
    passwordsMatching = []
    for password in passwords:
        if check_matching_digits(password):
            passwordsMatching.append(password)
    print('Number of possible passwords is: %s' %(str(len(passwordsMatching))))

def check_matching_digits(password):
    p = np.array(list(map(int, list(str(password)))))
    if 2 not in [sum(p==i) for i in set(p)]:
        return False
    return True


if __name__ == '__main__':
    with open('input.txt', "r") as f:
            puzzle = [l.strip() for l in f.readlines()]
    for i in range(len(puzzle)):
        puzzle[i] = list(map(int, puzzle[i].split('-')))
    if len(puzzle) == 1:
        puzzle = puzzle[0]
        passwords = possiblePasswords(puzzle)
        possiblePasswordsDigits(passwords)
    else:
        print('Puzzle input unkown')
