# to create a MessageSpaceProbabilityFxns object that represents
# the message space of identification.


from probabilityfunction import MessageSpaceProbability
import math


# helper function to get denominator of prefix probabilities
def getTotalProbability():
    sum = 314686575
    return sum


"""
Creates prefix cumulative probability distribution
"""


def get_cumulative_probability(mesg, sum):
    with open("idsorted.txt") as f:
        i = 0;
        for line in f:
            i = i + 1
            if line.strip() == str(mesg):
                return i * (float(1) / sum)


"""
Creates list of ordered prefixes
"""


def create_prefix_ordered_list():
    lines = [line.rstrip('\n') for line in open('filename')]
    return lines


# given random message string as int, return int message with last digit appended such that new string is Luhn-valid
def luhn(m):
    sum = 0
    for i in list(str(m)):
        sum += int(i)
    last = (9 * sum) % 10
    return m * 10 + last


class IdentificationProbability(MessageSpaceProbability):

    def __init__(self):
        self.sum = getTotalProbability()

        # define probability distribution fxn
        # this actually doesn't depend on the prefix but only the length of the string....
        # whatever
        def probability(self, m):
            return float(1) / 314686575

        # define cumul distribution fxn
        def cumulative(self, m):
            with open("idsorted.txt") as f:
                i = 0
                for line in f:
                    i = i + 1
                    if line.strip() == str(m):
                        return i * (float(1) / 314686575)

        # define next message fxn
        # simplified to never carry over to another prefix
        def next_message(self, m):
            with open("idsorted.txt") as f:
                i = 0
                find = 0
                for line in f:
                    i = i + 1
                    if find == 1:
                        return line.strip()
                    if line.strip() == str(m):
                        find = 1

        # Initialize MessageSpaceProbabilityFxns
        MessageSpaceProbability.__init__(self, cumulative, probability, next_message)
