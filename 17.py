ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

hundred = 'hundred'

thousand = 'thousand'

def numToWord(num):
    ret = ''
    i = 0
    if num >= 1000:
        ret += ones[int(str(num)[i])]
        ret += thousand
        i += 1
    if num > 99:
        if int(str(num)[i]) != 0: 
            ret += ones[int(str(num)[i])]
            ret += hundred
            if int(str(num)[i+1:]) != 0:
                ret += 'and'
        i += 1
    if num >= 20:
        ret += tens[int(str(num)[i])]
        i += 1
    if int(str(num)[-2:]) >= 10 and int(str(num)[-2:]) < 20:
        ret += ones[int(str(num)[-2:])]
        return ret
    ret += ones[int(str(num)[-1:])]
    return ret

total = 0
for i in range(1000):
    total += len(numToWord(i + 1))
print total
