if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    maxs=arr[-1]
    arr.sort(reverse=True)
    for x in arr:
        if x!=maxs:
            result = x
            print(result)
            break
