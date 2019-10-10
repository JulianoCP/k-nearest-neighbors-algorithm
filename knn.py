import math  
from random import shuffle 

global vetorDistance
vetorDistance = [20]
global vetorClasses
vetorClasses = [20]

def readDataFun(fileName): 
  
    data = [] 
    f = open(fileName, 'r') 
    lines = f.read().splitlines()
    f.close() 

    for i in range(0, len(lines)): 
        line = lines[i];
        data.append(line) 

    return data 

def EuclideanDistance(x,y):
    distance = 0

    a = x.split(' ')
    b = y.split(' ')[:-1]

    for i in range(0,(len(a)-1)):
        distance += math.pow(float(a[i]) - float(b[i]),2) 

    return math.sqrt(distance)



def classify(feature,k,training):

    for i in training:
        distance = EuclideanDistance(feature,i)
        neighbors(distance,i[-1],k)
    
    classe = qtdNeighbors(k)

    return classe;

def qtdNeighbors(k):
    global vetorClasses

    vet = []
    for i in range(0,10):
        vet.append(0)

    for i in range(0,k):
        for j in range(0,10):
            if int(vetorClasses[i]) == j:
                vet[j] += 1

    max = 0
    for i in range(0,10):
        if vet[i] >= vet[max]:
            max = i

    return float(max)

def neighbors(distance,classe,k):
    global vetorDistance
    global vetorClasses

        

    for i in range(0,k):
        if distance < vetorDistance[i]:
            tmp = vetorDistance[i]
            vetorDistance[i] = distance
            distance = tmp
            tp = vetorClasses[i]
            vetorClasses[i] = classe
            classe = tp
            vetorDistance.sort()

    

def FoldsFun(k,data,iterations):
    corrects = 0.0
    total = len(data)

    training = data[iterations:len(data)]
    test = data[0:iterations]

    for item in test:
        itemClass = item[-1]
        feature = item[:-1]
        
        deduction = classify(feature,k,training)

        if(float(deduction) == float(itemClass)):
            corrects += 1

    accuracy = corrects / iterations
    return accuracy

def accuracyFun(k,data,iterations):
    accuracy = 0.0
    shuffle(data)

    accuracy = FoldsFun(k, data,iterations)

    print("Accuracy: %f" % accuracy)
  
    
def main():
    global vetorDistance
    global vetorClasses

    for i in range(0,4):
        vetorClasses.append(1)
        vetorDistance.append(1)

    data = readDataFun('treinamento.txt')
    accuracyFun(5,data,10)
  
if __name__ == '__main__': 
    main() 