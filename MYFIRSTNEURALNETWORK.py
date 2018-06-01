import random
class neuron:
    def __init__(self,input,output):
        self.weight = random.randint(0,200)
        self.bais = random.randint(0,200)
        self.inputl = input
        self.outputl = output
        self.output = 0
    def forward(self):
        for i in self.inputl:
            self.output = self.output + i*self.weight + self.bais
        return self.output
input = [1]
output = []
answer = 101

smartsam = neuron(input,output)
smartsam.forward()

error = abs(answer - smartsam.output)
best = error

for i in range(0,1000):
    smartsam = neuron(input,output)
    smartsam.forward()
    error = abs(answer - smartsam.output)
    if error < best:
        best = error
        print(str(i)+':'+str(smartsam.output))
