def searchNum(ls, num, lower=0, upper=None):
    if upper is None:
        upper = len(ls)-1
    mid = (lower + upper) // 2
    if num == ls[mid]:
        return mid, ls[mid]
    elif num < ls[mid]:
        return searchNum(ls, num, lower, mid)
    else:
        return searchNum(ls, num, mid+1, upper)

if __name__ == '__main__':
    L = [5, 8, 9, 12, 17, 19, 20, 22]
    n = 12
    result = searchNum(L, n)
    print(result)
