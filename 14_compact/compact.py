def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # old way:
    # newList = []
    # for value in lst:
    #     if value:
    #         newList.append(value)
    # return newList

    #using comprehension:
    return [value for value in lst if value]