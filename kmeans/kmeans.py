#iencoding=utf-8

import numpy as np

def kmeans(X, k, maxIt):

    numPoints, numDim = X.shape

    dataSet = np.zeros((numPoints, numDim + 1))
    dataSet[:, :-1] = X

    #initialize centroids randomly
    centroids = dataSet[np.random.randint(numPoints, size = k), :]

    #randomly assign labels to initial centroid
    centroids[:, -1] = range(1, k + 1)

    #initialize book keeping vars
    iterations = 0
    oldCentroids = None

    #run the main k-means algorithm
    while not shouldStop(oldCentroids, centroids, iterations, maxIt):
        print("iteration:  ", iterations)
        print("dataSet:   ", dataSet)
        print("centroids:   ", centroids)

        oldCentroids = np.copy(centroids)
        iterations += 1

        updateLabels(dataSet, centroids)

        centroids = getCentroids(dataSet, k)

    return dataSet

def shouldStop(oldCentroids, centroids, iterations, maxIt):
    if iterations > maxIt:
        return True
    return np.array_equal(oldCentroids, centroids)

def updateLabels(dataSet, centroids):
    numPoints,numDim = dataSet.shape
    for i in range(0, numPoints):
        dataSet[i, -1] = getLabelFromClosestCentroid(dataSet[i, :-1], centroids)


def getLabelFromClosestCentroid(dataSetRow, centroids):
    label = centroids[0, -1]
    minDist = np.linalg.norm(dataSetRow - centroids[0, :-1])
    for i in range(1, centroids.shape[0]):
        dist = np.linalg.norm(dataSetRow - centroids[i, :-1])
        if dist < minDist:
            minDist = dist
            label = centroids[i, -1]
    print("minDist:", minDist)
    return label

def getCentroids(dataSet, k):

    result = np.zeros((k, dataSet.shape[1]))
    for i in range(1, k + 1):
        oneCluster = dataSet[dataSet[:, -1] == i, :-1]
        result[i - 1, :-1] = np.mean(oneCluster, axis = 0)
        result[i - 1, -1] = i

    return result

x1 = np.array([1, 1])
x2 = np.array([2, 1])
x3 = np.array([4, 3])
x4 = np.array([5, 4])
testX = np.vstack((x1, x2, x3, x4))
import ipdb
ipdb.set_trace()

result = kmeans(testX, 2, 10)
print("final result:", result)
