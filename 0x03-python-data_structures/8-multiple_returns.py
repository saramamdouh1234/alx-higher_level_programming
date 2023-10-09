#!/usr/bin/python3
def multiple_returns(sentence):
    tuples = len(sentence)
    if tuples > 0:
        first = sentence[0]
    else:
        first = None
    return (tuples, first)
