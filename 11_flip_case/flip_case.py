def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    char_lst = []
    for char in phrase:
        if char == to_swap.lower():
            char_lst.append(char.upper())
        elif char == to_swap.upper():
            char_lst.append(char.lower())
        else:
            char_lst.append(char)
    return ''.join(char_lst)
            