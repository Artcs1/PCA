import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def iris(data):
    return data[:,:-1]

def preprocessing(data):
    X = data - sp.mean(data,axis = 0)
    print(np.mean(X))
    print(np.std(X))
    return X
    
def PCA(data,comp = 2):
    n = data.shape[1]
    cov_matrix = np.cov(data.astype(float), rowvar=False)
    print(cov_matrix)
    
    eig_val_cov, eig_vec_cov = np.linalg.eig(cov_matrix)
    
    eig_pairs = [(np.abs(eig_val_cov[i]), eig_vec_cov[:,i]) for i in range(len(eig_val_cov))]

    #Sort the (eigenvalue, eigenvector) tuples from high to low
    eig_pairs.sort(key=lambda x: x[0], reverse=True)

    # Visually confirm that the list is correctly sorted by decreasing eigenvalues
    for i in eig_pairs:
        print(i[0])
        
    matrix_w = np.hstack((eig_pairs[0][1].reshape(n,1), eig_pairs[1][1].reshape(n,1)))
    print('Matrix W:\n', matrix_w)
    
    transformed = matrix_w.T.dot(data.T)
    print(transformed)

    plt.plot(transformed[0,0:49], transformed[1,0:49], 'o', markersize=7, color='blue', alpha=0.5, label='class1')
    plt.plot(transformed[0,50:99], transformed[1,50:99], '^', markersize=7, color='red', alpha=0.5, label='class2')
    plt.plot(transformed[0,100:149], transformed[1,100:149], 'X', markersize=7, color='green', alpha=0.5, label='class2')
    plt.xlim([-4,4])
    plt.ylim([-4,4])
    plt.xlabel('PCA1')
    plt.ylabel('PCA2')
    plt.legend()
    plt.title('dataset with reduction dimensionality')

    plt.show()

    return 

def main():
    datos = pd.read_csv("iris.data",sep = ",") 
    print(datos)
    X = datos.values
    X = iris(X)
    #print(X)
    X = preprocessing(X)
    PCA(X)
    #print(X)
if __name__ == "__main__":
    main()





