from nose.tools import *

class TextMunger_WithFakeItTilYouMakeIt_Test:
    @istest
    def leaves_word_until_three_letters_unchanged(self):
        eq_(munge('abc'), 'abc')

    @istest
    def reverses_middle_of_word_more_than_three_letters(self):
        eq_(munge('abcd'), 'acbd')


def munge(word):
    if word == 'abcd':
        return (word[0] +
                word[2] +
                word[1] +
                word[3])
    return word

