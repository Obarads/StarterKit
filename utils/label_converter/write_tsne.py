from tsnecuda import TSNE
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# file_name: string
# embedding: numpy [elements,features] len(elements)=X len(features)=D
# ins_label: numpy [elements, number_of_labels] len(number_of_labels)=1
# sem_label: not implemented

def write_tsne(file_name, embedding, ins_label, sem_label=None):
    x_embedding = TSNE().fit_transform(embedding)
    embedding_and_ins_label = pd.concat([pd.DataFrame(x_embedding), pd.DataFrame(data=ins_label,columns=["label"])], axis=1)
    sns.FacetGrid(embedding_and_ins_label, hue="label", height=6).map(plt.scatter, 0, 1).add_legend()
    plt.savefig(file_name)
    plt.close()
 