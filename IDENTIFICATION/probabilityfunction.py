# probabilityfunctionAPI

# This file describes the API required to build the probability functions
# used by the Distribution Transforming Encoder (DTE) for a message space


"""
The cumulative probability distribution function for the ordered message
space. Takes in a string for the message and returns a probability value
between <= 1 and > 0 representing where in the ordered probability space
that message lies.
"""


def cumulative_distribution(message):
    return


"""
The probability distribution function for the ordered message space. Takes
in a string for the message and returns a probability value between <= 1
and > 0 representing the probability of that single message.
"""


def probability_distribution(message):
    return


"""
Given an input message, return the next message in the ordered message space.
"""


def next_message(message):
    return


"""
Class used to bundle all the above functions into one object for easy access.
"""


class MessageSpaceProbability:
    """
    Creator method takes in specified functions.
    """

    def __init__(self, cumulative, probability, next_msg):
        self.cumulative = cumulative
        self.probability = probability
        self.next_message = next_message

    def cumulative_distribution(self, m):
        return self.cumulative(self, m)

    def probability_distribution(self, m):
        return self.probability(self, m)

    def next_message(self, m):
        return self.next_message(self, m)
