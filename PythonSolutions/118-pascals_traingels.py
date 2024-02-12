def generate(numRows):
    result = []
    for i in range(1, numRows+1):
        buff = [1] * i
        # buff[0] = 1
        # buff[-1] = 1
        # print(buff)
        for j in range(1, i - 1):
            buff[j] = result[i - 2][j - 1] + result[i - 2][j]
            # print(result[i-2][j-1] + result[i-2][j])
        result.append(buff)
        
    return result

numRows = 7
print(generate(numRows))