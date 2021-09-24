#%%

def printLogestIncSubArr(arr) :
    m = 1
    l = 1
    n=len(arr)
    maxIndex = 0

    for i in range(1, n) :
        if (arr[i] > arr[i-1]) :
            l =l + 1
        else :
            if (m < l)  :
                m = l
                maxIndex = i - m
            l = 1   
    if (m < l) :
        m = l
        maxIndex = n - m
    return arr[maxIndex]


arr = [5, 6, 2, 5, 7, 8, 9, 1, 2]
printLogestIncSubArr(arr)
# %%