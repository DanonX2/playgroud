import random
class neuron:
    def __init__(self,input):
        self.weight = random.randint(0,200)
        self.bais = random.randint(0,200)
        self.inputl = input
        self.output = 0
    def forward(self):
        for i in self.inputl:
            self.output = self.output + i*self.weight + self.bais
        return self.output
def inputdatalayer(inputl):
    return inputl
class hiddenlayers:
    def __init__(self,inputlayer):
        self.learningrate = 200
        self.numofneuron = 1
        self.neuron = [neuron(INPUT)]
        self.output = []
    def buildneuron(self,num=1):
        for i in range(0,num):
            self.neuron.append(neuron(INPUT))
        self.numofneuron += num
    def forward(self):
        for i in range(0,self.numofneuron):
            self.output.append(self.neuron[i].forward())
        return self.output
class neuralnetwork:
    def __init__(self,input):
        self.numoflayer = 2
        self.layer = [input,hiddenlayers(input)]
        self.output = []
    def buildlayer(self,num=1):
        for i in range(0,num):
            self.layer.append(hiddenlayers(len(self.layer)-1))
        self.numoflayer += num
    def run(self):
        for i in range(1,self.numoflayer):
            self.output = self.layer[i].forward()
        return self.output





INPUT = inputdatalayer([1])
nn1 = neuralnetwork(INPUT)
nn1.buildlayer()
nn1.layer[1].buildneuron()
ansewr = 100
print(nn1.run())