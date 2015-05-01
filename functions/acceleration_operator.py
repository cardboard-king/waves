##  NAME:           definitions.py
##  TYPE:           function
##  AUTHOR:         Matthias
##  CREATED:        01.05.15
##  LAST MODIFIED:  01.05.15
#
##  SUMMARY:
##   A function
#



def acceleration_operator(function, speed, diff_order):
    diff1 = numeric_diff(function, diff_order)
    diff2 = numeric_mydiff(diff1, diff_order)
    result = np.zeros(function.size)
    np.put(result, np.arange(1, diff2.size), diff2)
    result = result*float(speed**2)
    return result
