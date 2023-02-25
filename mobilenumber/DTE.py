# DTE.py

# Implementation of the distribution transforming encoder (DTE)
# using the API for a message space described in probabilityfunction.py

import random
import probabilityfunction

# Define length of seed space
SEED_SPACE_LENGTH = 64
seed_space = 2 ** SEED_SPACE_LENGTH - 1

"""
Takes in a message and a MessageSpaceProbability  returns a corresponding random bit string in the seed space.
"""


def encode(m, p):
    # get range of seed space to pick random string from
    start = p.cumulative_distribution(m) * seed_space
    end = int(start + p.probability_distribution(m) * seed_space) - 1
    start = int(start)

    # pick random string from corresponding seed space
    seed = int(random.random() * (end - start) + start)

    return seed


"""
Takes in a seed and a MessageSpaceProbability  find corresponding message.
"""


def decode(s, p):
    seed_location = float(s) / seed_space
    current_probability = 0
    (key, value) = (0, 0)
    with open("cumulative_probability_table.txt") as f:
        for line in f:
            (pre_key, pre_value) = (key, value)
            (key, value) = line.strip().split(",")
            current_probability = float(key)
            if current_probability > seed_location:
                return pre_value
