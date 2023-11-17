def sum_strings(a, b):
    
    if not a and not b:
        return '0'

    if len(a) < len(b):
        a, b = b, a
    b = b.zfill(len(a))

    res = ''
    carry = 0

    for i in range(len(a)-1, -1, -1):
        total = carry
        total += int(a[i]) + int(b[i])
        res += str(total % 10)
        carry = total // 10

    if carry:
        res += str(carry)

    return res[::-1].lstrip('0') or '0'