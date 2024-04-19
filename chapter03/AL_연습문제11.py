def substr(str, x, y):
    count = 0   
    n = len(str)
    for i in range (n-1) :
        if str[i] == x :
            for j in range (i+1, n) :
                if str[j] == y :
                    count += 1
    return count
