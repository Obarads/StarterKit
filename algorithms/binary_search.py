# https://qiita.com/Brutus/items/5653c6d3683d25e2cf89

def binary_search(arr:list, target:int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return target, mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

arr = [i for i in range(0,100000000,5)]
print(binary_search(arr,99995))
print(binary_search(arr,99999))
