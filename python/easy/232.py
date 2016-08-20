def is_palindrome(input):
    stripped = ''.join(input.split(' ')).lower()

    if stripped == stripped[::-1]:
        return True
    else:
        return False
