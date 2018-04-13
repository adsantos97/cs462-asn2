_author_ = 'arizza santos'
# Course: CS 462
# April 18, 2018
# Assignment 2: Dynamic Programming and Greedy Algorithms

import random
import timeit
import itertools
import sys

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

# purpose: generate one random problem instance
# input: start - starting integer
#        n - number of objects
#        step - increment between each integer
# return: list of objects with their weights and values
def generate_one_instance(start, n, step):
    prob_instance = []
    obj = []

    objects = generate_ints(start, n, step)
    weights = generate_rand_ints(n)
    values = generate_rand_ints(n)

    #print("Object\tWeight\tValue")

    for i in range(n/step):
        obj.append(objects[i])
        obj.append(weights[i])
        obj.append(values[i])
        prob_instance.append(obj)
        #print obj[0],"\t",obj[1],"\t",obj[2]
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
        max_weight += obj[1]

    #print "Total Weight: ", max_weight
    max_weight = int(round(max_weight * 0.75)) # 75% and round
    return max_weight

# purpose: make a list from a given problem instance
# input: prob_instance - list of objects with their weights and values
#        choice: 0 - objects, 1 - weights, 2 - values
# return: a list made from the given choice
def make_list(prob_instance, choice):
    l = []
    for obj in prob_instance:
        l.append(obj[choice])
    return l

# purpose: brute force implementation of 0-1 Knapsack Problem
# input: max_w - maximum weight of the prob_instance
#        n - number of objects
#        w - list of weights
#        v - list of values
# return: solution
def brute_force(max_w, n, w, v):
    if n == 0 or max_w == 0:
        return 0

    if w[n-1] > max_w:
        return brute_force(max_w, n-1, w, v)
    else:
        return max(v[n-1] + brute_force(max_w-w[n-1], n-1, w, v), 
                  brute_force(max_w, n-1, w, v))

def main():
    if len(sys.argv) != 5:
        print "Please type: python asn2.py <start> <n> <step> <algorithm>"
        print "Choices of algorithm: {} - brute force, {} - greedy, " \
              "{} - dynamic programming".format('b','g','d')
    else:
        start = int(sys.argv[1])
        n = int(sys.argv[2])
        step = int(sys.argv[3])
        choice = sys.argv[4]
        print "Start = {} | n = {} | Step = {}\n".format(start, n, step)

        print "n\tMax Weight\tSolution\tTime(ms)"
        for i in range(start, n+1, step):

            if choice == 'b':
                one = generate_one_instance(start, i, step)
                w = make_list(one, 1)
                v = make_list(one, 2)
                max_w = max_weight(one)
                
                start_time = timeit.default_timer()
                solution = brute_force(max_w, i, w, v)
                elapsed = int((timeit.default_timer() - start_time) * 1000)
                print "{}\t{}\t\t{}\t\t{}".format(i, max_w, solution, elapsed)

            elif choice == 'g':
                print "greedy"

            elif choice == 'd':
                print "dynamic programming"

            else:
                print "Invalid algorithm choice!" 

main()
