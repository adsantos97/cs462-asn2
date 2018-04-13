_author_ = 'arizza santos'
# Course: CS 462
# April 18, 2018
# Assignment 2: Dynamic Programming and Greedy Algorithms

import random
import itertools

# purpose: generate random integers
# input: n - number of objects(integers)
# return: rand_ints - list of random integers
def generate_rand_ints(n):
    rand_ints = []
    for i in range(n):
        rand_ints.append(random.randint(1, n))
    return rand_ints

# purpose: generate list of integers [1,n]
# input: n - number of objects(integers)
# return: ints - list of integers
def generate_ints(n):
    ints = []
    for i in range(n+1):
        ints.append(i+1)
    return ints

def generate_prob_instance(n):
    objects = generate_ints(n)
    weights = generate_rand_ints(n)
    values = generate_rand_ints(n)
    for i, w, v in itertools.izip(objects, weights, values):
        print("Object {}: {} {}".format(i, w, v))

def main():
    print("Generating random numbers")
    list_ints = generate_rand_ints(10)
    print(list_ints)
    generate_prob_instance(10)


main()
