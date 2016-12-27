def is_ordered(word: str) -> bool:
    for w in range(len(word)):
        if w == 0:
            continue

        w1 = ord(word[w - 1])
        w2 = ord(word[w])

        if w1 > w2:
            return False

    return True

def is_reversed(word: str) -> bool:
    for w in range(len(word)):
        if w == 0:
            continue

        w1 = ord(word[w - 1])
        w2 = ord(word[w])

        if w1 < w2:
            return False

    return True

if __name__ == '__main__':
    words = 'billowy biopsy chinos defaced chintz sponged bijoux abhors fiddle begins chimps wronged'
    words = words.split(' ')

    for word in words:
        if is_ordered(word):
            order = 'IN ORDER'
        elif is_reversed(word):
            order = 'REVERSE ORDER'
        else:
            order = "NOT IN ORDER"

        print(f'{word} {order}')


        
