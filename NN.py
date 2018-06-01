class neuron:
    def __init__(self,input,output):
        self.weight = 0
        self.bais = 0
        self.inputl = input
        self.outputl = output
        self.output = 0
    def forward(self):
        for i in self.inputl:
            self.output = self.output + i*self.weight + self.bais
        return self.output
        