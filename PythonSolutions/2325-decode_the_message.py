def decode_message(key, message):
    dct = {}
    kIndex = 0

    for i in key:
        if i.isalpha() and i not in dct:
            dct[i] = chr(97 + kIndex)
            kIndex += 1



    decode = ''.join(dct[i] if i.isalpha() else i for i in message)
    # print([dct[i] if i.isalpha() else i for i in message])

    return decode

key = "eljuxhpwnyrdgtqkviszcfmabo"; message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

decode = decode_message(key, message)

print(decode) #Expect: "the five boxing wizards jump quickly"
