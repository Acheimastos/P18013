def maxSequence(a,size):

    max_so_far = 0
    max_ending_here = 0
    b= []
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_ending_here < 0:
            max_ending_here = 0
            s=i+1
        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            start=s
            end=i
    for j in range(start,end+1):
        b .append(a[j])

    return max_so_far, b

a = ([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print ("Maximum contiguous sum is", maxSequence(a,len(a)))

