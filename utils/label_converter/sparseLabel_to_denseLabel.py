import numpy as np

def sparseLabel_to_denseLabelConverter(label):
    unique_label = np.unique(label)
    converted_num = np.arange(0,len(unique_label))
    label_converter = np.full(np.max(unique_label)+1,-1)
    label_converter[unique_label] = converted_num
    return label_converter

def sparseLabel_to_denseLabel(label):
    converter = sparseLabel_to_denseLabelConverter(label)
    converted_label = list(map(lambda x:converter[x],label))
    return converted_label

def batch_sparseLabel_to_denseLabel(labels):
    return np.apply_along_axis(sparseLabel_to_denseLabel, 1, labels)

label = np.array(
    [0,3,0,2]
)

print(sparseLabel_to_denseLabelConverter(label))
print(sparseLabel_to_denseLabel(label))

batch_labels = label = np.array([
    [0,3,0,2],
    [1,11,9,3]
])

print(batch_sparseLabel_to_denseLabel(batch_labels))