import random, time, math

s = time.time()
li = [int(10000*random.random()) for i in range(10000000)]
e = li[2354]
li.sort()
print("Creating time:\t", time.time()-s)
print(f"List range:\t {len(li):,}")
print("Wanted:\t\t", [e])
print("NOTE! Time:\t 1x1000")
print("=====================================\n")

def bn(l, e):
    high = len(l)
    low = 0
    while high > low:
        i = (high + low) // 2
        if e == l[i]: return [e, i]
        elif e < l[i]: high = i
        else: low = i
    return -1

def it(l, e):
    low = 0
    high = (len(l)-1)
    while low <= high and e >= l[low] and e <= l[high]:
        i = low + int(((float(high - low) / (l[high] - l[low])) * (e - l[low])))
        if l[i] == e:
            return [e, i]
        if l[i] < e:
            low = i+1;
        else:
            high = i-1;
    return -1

def fb(l, e):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(l):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while fibM > 1:
        i = min(index + fibM_minus_2, (len(l)-1))
        if l[i] < e:
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif l[i] > e:
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return [e, i]
    if fibM_minus_1 and index < (len(l)-1) and l[index+1] == e:
        return index+1;
    return -1

def jm(l, e):
    length = len(l)
    jump = int(math.sqrt(length))
    left, right = 0, 0
    while left < length and l[left] <= e:
        right = min(length - 1, left + jump)
        if l[left] <= e and l[right] >= e:
            break
        left += jump;
    if left >= length or l[left] > e:
        return -1
    right = min(length - 1, right)
    i = left
    while i <= right and l[i] <= e:
        if l[i] == e:
            return [e, i]
        i += 1
    return -1

def ex(l, e):
    if l[0] == e:
        return 0
    i = 1
    while i < len(l) and l[i] <= e:
        i = i * 2
    return bn(li[:min(i, len(l))], e)

def ln(l, e):
    for i in range(len(l)):
        if l[i] == e:
            return [e, i]
    return -1

s = time.time()
print(bn(li, e))
print("binary time:", 1000*(time.time()-s), "\n")

s = time.time()
print(it(li, e))
print("interpolation time:", 1000*(time.time()-s), "\n")

s = time.time()
print(fb(li, e))
print("fibonacci time:", 1000*(time.time()-s), "\n")

s = time.time()
print(jm(li, e))
print("jumping time:", 1000*(time.time()-s), "\n")

s = time.time()
print([e, e in li])
print("membership in time:", 1000*(time.time()-s), "\n")

s = time.time()
print(ex(li, e))
print("exponential time:", 1000*(time.time()-s), "\n")

s = time.time()
print(ln(li, e))
print("linear time:", 1000*(time.time()-s), "\n")
