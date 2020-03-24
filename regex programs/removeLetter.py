"""
A program to remove a letter from a sentence or from a long string. If you know what I mean =)
"""

strings = "Shall I compare thee to a summers day"

letterToRemove = "e"


def removeLetter(strings, letter):
    return "".join(strings.split(letter))


print(removeLetter(strings, letterToRemove))
