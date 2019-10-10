import math  
from random import shuffle 

global vetorClasses
vetorClasses = []

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

    return (math.sqrt(distance), y[-1])



def classify(feature,k,training):
    global vetorClasses
    distancias = []
    for i in training:
        distancias.append(EuclideanDistance(feature,i))
    distancias.sort()    

    for i in range(0,k):
        vetorClasses[int(distancias[i][1])] += 1
    
    maior = 0
    for i in range(len(vetorClasses)):
        if vetorClasses[i] >= vetorClasses[maior]:
            maior = i
    clearArray()        
    return maior

def clearArray():
    for i in range(len(vetorClasses)):
        vetorClasses[i] = 0

    

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
    global vetorClasses

    for i in range(0,10):
        vetorClasses.append(0)

    data = readDataFun('treinamento.txt')

    accuracyFun(5,data,700)
  
if __name__ == '__main__': 
    main() 