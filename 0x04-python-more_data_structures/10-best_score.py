#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        large = 0

        for key in keys:
            if a_dictionary[key] > large:
                large = a_dictionary[key]
                name = key

        return name
