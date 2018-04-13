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
    for i in range(1, n+1):
        rand_ints.append(random.randint(1, n))
    return rand_ints

# purpose: generate list of integers [1,n]
# input: start - starting integer
#        n - number of objects(integers)
#        step - increment between each integer
# return: ints - list of integers
def generate_ints(start, n, step):
    ints = []
    for i in range(start, n+1, step):
        ints.append(i)
    return ints

def generate_prob_instance(start, n, step):
    objects = generate_ints(start, n, step)
    weights = generate_rand_ints(n)
    values = generate_rand_ints(n)
    obj = []
    for i, w, v in itertools.izip(objects, weights, values):
        print("Object {}: {} {}".format(i, w, v))

    ## create a list of problem instances
    objs_list = []
    objs = []
    print objects
    for j in range(n/step):
        objs.append(objects[j])
        objs.append(weights[j])
        objs.append(values[j])
        objs_list.append(objs)
        print objs
        objs = []
    print objs_list

def main():
    print("Generating random numbers")
    list_ints = generate_ints(25, 100, 25)
    print(list_ints)
    generate_prob_instance(25, 100, 25)

main()
