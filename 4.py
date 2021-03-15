def kirpic_lang(strr):
    gl = 'уеаоэяию'
    fin_str = ''
    for i in strr:
        if i in gl:
            fin_str += i + 'к' + i
        else:
            fin_str += i
    return fin_str

mystr = str(input())

print(kirpic_lang(mystr))
