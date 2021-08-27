import numpy as np
import matplotlib.pyplot as plt

'''Le pregunta uno a uno de los valores de la data cual de los centroides 
   esta mas cerca y le asugna a cada uno de esos valores un centroide'''
def group_assignment(data,centroids):
    grouping_vec_c = np.zeros(len(data))
    for i in range(len(data)):
        dist = np.zeros(len(centroids))
        for j in range(len(centroids)):
            dist[j] = np.linalg.norm(data[i] - centroids[j])
        min_dist = min(dist)
        for j in range(len(centroids)):
            if min_dist == dist[j]:
                grouping_vec_c[i] = j+1
    return grouping_vec_c
'''Retorna un array del mismo largor que la data donde se ve a que grupo pertenece ese valor'''
'''si la data es [2,3,4,5,6,8,9,11] y los grupos son (1) primos y (2) no primos, grouping_vec_c = [1,1,2,1,2,2,2,1]'''


#_ACTUALIZACIÓN DE LOS CENTROIDES_
# grouping => el valor de salida de la función "group_assignment()"
'''Recolecto cada valor de cada centroide y le saco su promedio creando un nuevo centroide más centrado'''
def update_centroid(data, grouping, centroids):
    new_centroids = []
    for i in range(len(centroids)):
        cent = np.zeros(len(data[0]))
        count = 0
        for j in range(len(data)):
            if grouping[j] == (i+1):
                cent = cent+data[j]
                count += 1
        group_average = cent/count
        new_centroids.append(group_average)
    return new_centroids


'''Promedio de las distancias con el centroide'''
def clustering_objective(data, grouping, centroids):
    J_obj = 0
    for i in range(len(data)):
        for j in range(len(centroids)):
            if grouping[i] == (j+1):
                J_obj += np.linalg.norm(data[i] - centroids[j])**2
    J_obj = J_obj/len(data)
    return J_obj


#Función de ensamble
def Kmeans_alg(data, centroids):
    iteration = 0
    J_obj_vector = []
    Stop = False
    while Stop == False:
        grouping = group_assignment(data, centroids)
        new_centroids = update_centroid(data, grouping, centroids)
        J_obj = clustering_objective(data, grouping,new_centroids)
        J_obj_vector.append(J_obj)
        iteration += 1

        '''Si el movimiento de los centroides ya es muy bajo, Termina de iterar'''
        if np.linalg.norm(np.array(new_centroids) - np.array(centroids)) < 1e-6:
            Stop = True
        else:
            centroids = new_centroids
    return new_centroids, grouping, J_obj_vector, iteration


if __name__ == '__main__':
    fig,ax = plt.subplots(1,1,figsize=(7,7),dpi=120)
    X = np.concatenate([[0.3*np.random.randn(2) for i in range(100)],\
                        [[1,1] + 0.3*np.random.randn(2) for i in range(100)], \
                        [[1,-1]+ 0.3* np.random.randn(2) for i in range(100)]])
    ax.scatter( X[:,0],X[:,1])
    ax.set_xlim(-1.5,2.5)
    ax.set_ylim(-2,2)
    plt.show()

    A = Kmeans_alg(X,X[:3])