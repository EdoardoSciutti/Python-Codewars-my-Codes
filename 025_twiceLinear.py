def dbl_linear(n):
    u = [1]
    i = 0
    j = 0
    while len(u) <= n:
        y = 2 * u[i] + 1
        z = 3 * u[j] + 1
        if y < z:
            u.append(y)
            i += 1
        elif y > z:
            u.append(z)
            j += 1
        else:
            u.append(y)
            i += 1
            j += 1
    return u[n]