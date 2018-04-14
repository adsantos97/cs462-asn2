_author_ = 'arizza santos'
# Course: CS 462
# April 18, 2018
# Assignment 2: Dynamic Programming and Greedy Algorithms

import random
import timeit
import itertools
import sys

# purpose: generate a list of random integers
# input: n - number of objects(integers)
# return: rand_ints - list of random integers
def generate_rand_ints(n):
    rand_ints = []
    for i in range(n):
        rand_ints.append(random.randint(1, n))
    return rand_ints

# purpose: find the maximum weight that is possible to carry
# input: weights - list of weights
# return: maximum weight (75% of the sum)
def max_weight(weights):
    max_weight = 0    

    for x in weights:
        print x
        max_weight += x

    #print "Total Weight: ", max_weight
    max_weight = int(round(max_weight * 0.75)) # 75% and round
    return max_weight

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
	if len(sys.argv) != 2:
		    print "Please type: python asn2.py <start> <n> <step> <algorithm>"
		    print "Choices of algorithm: {} - brute force, {} - greedy, " \
		          "{} - dynamic programming".format('b','g','d')
	else:
	    #start = int(sys.argv[1])
	    n = int(sys.argv[1])
	    #step = int(sys.argv[3])
	    #choice = sys.argv[4]
	    #print "Start = {} | n = {} | Step = {}\n".format(start, n, step)
	    w = generate_rand_ints(n)
	    v = generate_rand_ints(n)
	    max_w = max_weight(w)
            print "Weights: {}\nValues: {}".format(w,v)
            print max_w
	    print brute_force(max_w, n, w, v)

main()
        

