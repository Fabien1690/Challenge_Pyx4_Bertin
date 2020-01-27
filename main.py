from itertools import starmap, filterfalse
from typing import re
import functools

import numpy as np
import math


def reverse_string_iter(str_in):
    """Returns the input string in reverse order using iteration"""
    str_out = ""
    for char in str_in :
        str_out = char + str_out
    return (str_out)

def reverse_string_recur(str_in, str_out = ""):
    """Returns the input string in reverse using recursion"""
    if len(str_out) < len(str_in):
        return (reverse_string_recur(str_in, str_out + str_in[len(str_in)-len(str_out)-1]))
    return str_out

authorized_people = ["Alice", "Bob", "Carol", "Dave", "Mallory", "Oscar"]

def filter_authorized_people(list_in):
    """Returns the list of people that already are in the list of authoried people.
    To get the list of authorized people, use get_authorized_people()"""
    assert type(list_in) == list or type(list_in) == np.ndarray,"Please enter " \
        "a list or an array. The class of your input is " + format(type(list_in)) + "."
    return [person for person in list_in if person in authorized_people]

def get_authorized_people():
    return(authorized_people)

def reduction_median_value(list_in):
    """Returns the mean value of the numbers in the input list"""
    if type(list_in) == np.ndarray:
        return [reduction_median_value(element) for element in list_in]
    it = iter(list_in)
    median_value = 0
    number_values = 0
    for element in it :
        median_value = median_value + element
        number_values = number_values + 1
    return median_value/number_values

def reduction_median_in_array(array_in):
    """Returns the list of median numbers of each line present in the input list"""
    return [reduction_median_value(element) for element in array_in ]
