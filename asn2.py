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

# purpose: generate list of integers [start,n]
# input: start - starting integer
#        n - number of objects(integers)
#        step - increment between each integer
# return: ints - list of integers
def generate_ints(start, n, step):
    ints = []
    for i in range(start, n+1, step):
        ints.append(i)
    return ints

# purpose: generate a random problem instance
# input: start - starting integer
#        n - numbre of objects
#        step - increment between each integer
# return: list of objects with their weights and values
def generate_prob_instance(start, n, step):
    prob_instance = []
    obj = []

    objects = generate_ints(start, n, step)
    weights = generate_rand_ints(n)
    values = generate_rand_ints(n)

    for i in range(n/step):
        obj.append(objects[i])
        obj.append(weights[i])
        obj.append(values[i])
        prob_instance.append(obj)
        print obj
        obj = []

    # double check problem instance
    #for i, w, v in itertools.izip(objects, weights, values):
        #print("Object {}: {} {}".format(i, w, v))
    return prob_instance

# purpose: find the maximum weight that is possible to carry
# input: prob_instance - list of objects
# return: maximum weight (75% of the sum)
def max_weight(prob_instance):
    max_weight = 0    

    for obj in prob_instance:
        #for data in obj:
        max_weight += obj[1]

    #print max_weight
    max_weight = int(round(max_weight * 0.75))
    print max_weight

def main():
    print("Generating random numbers")
    start = 1
    n = 10
    step = 1
    list_ints = generate_ints(start, n, step)
    print(list_ints)
    problem = generate_prob_instance(start, n, step)
    max_weight(problem)

main()
