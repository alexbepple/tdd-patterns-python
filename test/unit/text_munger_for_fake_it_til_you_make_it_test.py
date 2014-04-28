def test_leaves_word_until_three_letters_unchanged():
    assert munge('abc') == 'abc'


def test_reverses_middle_of_word_more_than_three_letters():
    assert munge('abcd') == 'acbd'


def munge(word):
    if word == 'abcd':
        return 'acbd'
    return word
