def getRow(rowIndex):
    result = [0] * (rowIndex + 1)
    prev = 0
    
    result[0] = 1
    
    for i in range(1, rowIndex + 1):
        for j in range(1,i):
            temp = result[j]
            result[j] += prev
            prev = temp
        
        result[i] = 1
    print(result)
        
    
print(getRow(4))