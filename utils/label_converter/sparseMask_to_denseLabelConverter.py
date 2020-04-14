import numpy as np

def sparseMask_to_denseLabelConverter(mask):
    sum_res = np.sum(mask,0) > 0
    converted_num = np.arange(0,np.sum(sum_res))
    label_converter = np.full(len(sum_res),-1,np.int32)
    label_converter[sum_res] = converted_num
    return label_converter

arr = np.array(
    [
        [1,0,0,0,0],
        [0,0,0,1,0],
        [1,0,0,0,0],
        [0,0,1,0,0]
    ]
)

print(sparseMask_to_denseLabelConverter(arr))
