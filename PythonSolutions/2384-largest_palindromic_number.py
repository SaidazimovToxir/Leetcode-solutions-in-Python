def largest_palindromic_number(num):
    dict1 = {}
    
    for i in num:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    
    keys = list(dict1.keys())
    keys.sort()
    
    max1 = -1
    res = ''
    
    for i in keys:
        if dict1[i] >= 2:
            res += i * (dict1[i] // 2)
            if dict1[i] % 2 != 0:
                max1 = max(int(i), max1)
        else:
            max1 = max(int(i), max1)
    
    if res == '':
        return str(max1)
    elif res[-1] == '0' and res[0] == '0' and max1 == -1:
        return '0'
    
    if res[-1] == '0':
        res = ''
    
    return res[::-1] + (str(max1) if max1 != -1 else '') + res


print(largest_palindromic_number("444947137"))
print(largest_palindromic_number("00009"))
print(largest_palindromic_number("00001105"))
