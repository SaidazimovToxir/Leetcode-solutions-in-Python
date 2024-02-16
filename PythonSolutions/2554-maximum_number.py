def countValidIntegers(banned, n, mid):
    # banned_set = set(banned)
    # count = 0
    # current_sum = 0
    # i = 1

    # while i <= n and count <= mid:
    #     if i not in banned_set and current_sum + i <= mid:
    #         current_sum += i
    #         count += 1
    #     i += 1

    # return count
    
    bannedSet = set(banned)
    # print(bannedSet)
    
    count = 0
    currentSum = 0
    i = 1
    
    while i <= n and count <= maxSum:
        if i not in bannedSet and currentSum + i <= maxSum:
            currentSum += i
            count += 1
        
        i += 1
        
    return count

banned = [1,6,5]; n = 5; maxSum = 6

print(countValidIntegers(banned,n,maxSum))