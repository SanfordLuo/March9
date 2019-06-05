def searchNum(ls, num, lower=0, upper=None):
    if upper is None:
        upper = len(ls)-1
    mid = (lower + upper) // 2
    if mid == 0 and num != ls[0]:
        return "不存在"
    if mid == len(ls)-1 and num != ls[-1]:
        return "不存在"
    if num == ls[mid]:
        return mid, ls[mid]
    elif num < ls[mid]:
        return searchNum(ls, num, lower, mid)
    else:
        return searchNum(ls, num, mid+1, upper)

if __name__ == '__main__':
    L = [5, 8, 9, 12, 17, 19, 20, 22]
    n = 8
    result = searchNum(L, n)
    print(result)
