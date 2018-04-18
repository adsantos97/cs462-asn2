def vw_compare(obj):
    return float(obj[0])/obj[1]

def knapsack(max_w, n, vw):
    current_w = 0
    solution = 0
    #print "vw: ", vw
    val_densities = sorted(vw, key=vw_compare, reverse=True)
    print "val: ",val_densities
    for i in range(len(val_densities)):
         #print "object: ", val_densities[i]
         #print float(val_densities[i][0])/val_densities[i][1]
         if current_w + val_densities[i][1] <= max_w:
             current_w += val_densities[i][1]
             solution += val_densities[i][0]
    return solution                     

# Driver program to test above function
vw = [[60,10], [100,20], [120,30]]
W = 50
n = len(vw)
print(knapsack(W, n, vw))
