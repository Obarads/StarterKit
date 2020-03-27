# ref: https://qiita.com/gogotealove/items/11f9e83218926211083a
import sys, os

def bit(data):
    N = len(data)
    res = []
    for i in range(2**N):
        add_res = []
        for j in range(N):
            if ((i >> j) & 1):
                add_res.append(data[j])
        res.append(add_res)
    return res

print(bit([1,2,3]))