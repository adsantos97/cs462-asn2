_author_ = 'arizza santos'
# Course: CS 462
# April 18, 2018
# Assignment 2: Dynamic Programming and Greedy Algorithms

import random
import timeit # used for wall clock time
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
        max_weight += x

    #print "Total Weight: ", max_weight
    max_weight = int(round(max_weight * 0.75)) # 75% and round
    return max_weight

# purpose: brute force implementation of 0-1 Knapsack Problem
# input: max_w - maximum weight of the prob_instance
#        n - number of objects
#        w - list of weights
#        v - list of values
# return: optimal (value) solution
def brute_force(max_w, n, w, v):
    if n == 0 or max_w == 0:
        return 0

    if w[n-1] > max_w:
        return brute_force(max_w, n-1, w, v)
    else:
        return max(v[n-1] + brute_force(max_w-w[n-1], n-1, w, v), 
                  brute_force(max_w, n-1, w, v))

# purpose: dynamic programming implementation of 0-1 Knapsack Problem
# input: max_w - maximum weight of the prob_instance
#        n - number of objects
#        wt - list of weights
#        v - list of values
# return: optimal (value) solution
def dynamic_programming(max_w, n, wt, v):
    K = [[0 for x in range(max_w+1)] for y in range(n+1)]
    #print len(K)
    #print "at entry: ", len(K[0])

    for i in range(n+1):
        for w in range(max_w+1):
            if  i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(v[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][max_w]

# purpose: comparison function to sort object to v/w ratio
# input: obj - individual object
# return: v/w ratio
def vw_compare(obj):
    return float(obj[0])/obj[1] # obj[0] is (v)alue, obj[1] is (w)eight

# purpose: greedy implementation of 0-1 Knapsack Problem
# input: max_w - maximum weight of the prob_instance
#        n - number of objects
#        vw - objects with values and weights
# return: solution
def greedy(max_w, n, vw):
    current_w = 0
    solution = 0
    #print "vw: ", vw
    val_densities = sorted(vw, key=vw_compare, reverse=True)
    #print "val: ",val_densities
    for i in range(len(val_densities)):
         #print "object: ", val_densities[i]
         #print float(val_densities[i][0])/val_densities[i][1]
         if current_w + val_densities[i][1] <= max_w:
             current_w += val_densities[i][1]
             solution += val_densities[i][0]

    return solution                     

# purpose: make a list of value and weight pairs
# input: v - list of values
#        w - list of weights
# return: val_weights - list of objects with values and weights
def vals_wts(v, w):
    val_weights = []
    for n in range(len(v)):
        val_weights.append([v[n],w[n]])

    return val_weights

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

        if choice == 'b':
            print "n\tMax Weight\tSolution\tTime(ms)"
            for i in range(start, n+1, step):
                # generate random problem instance using i
                v = generate_rand_ints(i) 
                #print v
                w = generate_rand_ints(i)
                #print w
                max_w = max_weight(w)             
     
                start_time = timeit.default_timer()
                solution = brute_force(max_w, i, w, v)
                elapsed = int((timeit.default_timer() - start_time) * 1000)
                print "{}\t{}\t\t{}\t\t{}".format(i, max_w, solution, elapsed)

        elif choice == 'g':
            print "n\tMax Weight\t\tSolution\t\tTime(ms)"
            for i in range(start, n+1, step):
                # generate random problem instance using i 
                v = generate_rand_ints(i)
                #print v
                w = generate_rand_ints(i)
                #print w
                max_w = max_weight(w)
                vw = vals_wts(v, w)
     
                start_time = timeit.default_timer()
                solution = greedy(max_w, i, vw)
                elapsed = int((timeit.default_timer() - start_time) * 1000)
                print "{}\t{}\t\t{}\t\t{}".format(i, max_w, solution, elapsed)

        elif choice == 'd':
            print "n\tMax Weight\tSolution\tTime(ms)\tRatio"
            for i in range(start, n+1, step):
                # generate random problem instance using i
                v = generate_rand_ints(i)
                #print v
                w = generate_rand_ints(i)
                #print w
                max_w = max_weight(w)
                vw = vals_wts(v, w) # used for greedy solution
                
                g_solution = greedy(max_w, i, vw)
                start_time = timeit.default_timer()
                solution = dynamic_programming(max_w, i, w, v)
                elapsed = int((timeit.default_timer() - start_time) * 1000)

                ratio = float(g_solution)/solution
                #print ratio
                #r = float("{0:.2f}".format(ratio)
                print "{}\t{}\t\t{}\t\t{}\t\t{}".format(i, max_w, solution, elapsed, ratio)

        else:
            print "Invalid algorithm choice!"
             
main()
        

