import mesa 
class AgentA (mesa.Agent) : 
    def __init__(self,id,model): 
        super().__init__(id,model)
    def step(self) : 
        self.model.i += 1
        print(i)
class AgentB(mesa.Agent):
    def __init__(self,id,model):
        super().__init__(id,model)
    def step(self):
        self.model.i += 2
        print(i)
class Env (mesa.Model ):
    def __init__(self): 
        super().__init__()
        self.i = 0
        self.A = AgentA(0,self)
        self.B = AgentB(1,self)
        self.plannification = mesa.time.BaseScheduler(self)
        self.plannification.add(self.A)
        self.count = 0
    def step(self):
        self.plannification.step()
        self.count +=1 
        if self.count == 8 : 
            self.plannification.remove(self.A)
            self.plannification.add(self.B)
        if self.count == 17 : 
            self.plannification.remove(self.B)
        print(self.i)
model = Env() 
for i in range(17):
    model.step()
        

                
