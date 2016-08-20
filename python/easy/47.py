def ceasar(_input, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖabcdefghijklmnopqrstuvxyzåäö '
    chiffered = ''

    for char in _input:
        if char in alphabet:
            if char == ' ':
                chiffered += char
            else:
                position = alphabet.index(char) + shift

                print(type(position))
                print(type(len(alphabet - 1)))

                if position > len(alphabet - 1):
                    chiffered += alphabet[shift+1]
        else:
            raise ValueError

    print(chiffered)
