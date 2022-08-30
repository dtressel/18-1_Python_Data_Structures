def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    lst = phrase.lower().split(' ')
    capitalized_lst = [word.capitalize() for word in lst]
    return ' '.join(capitalized_lst)