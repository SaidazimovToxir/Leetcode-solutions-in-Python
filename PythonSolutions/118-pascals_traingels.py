def generate(numRows):
    result = []
    for i in range(1, numRows+1):
        buff = [1] * i
        for j in range(1, i - 1):
            buff[j] = result[i - 2][j - 1] + result[i - 2][j]
            print(result[i-2][j-1])
        result.append(buff)
        
    return result

numRows = 5
print(generate(numRows))
