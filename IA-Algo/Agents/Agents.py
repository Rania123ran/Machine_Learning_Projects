import mesa 
import random
import math
class AgentA (mesa.Agent): 
    def __init__(self,id,model) : 
        super().__init__(id,model)
    def step(self): 
        print("Agent B change de position !")
class AgentB(mesa.Agent): 
    def __init__(self,id,model): 
        super().__init__(id,model)
    def step(self): 
        res = pow(random.randint(0,100),2) + math.log(pow(random.randint(0,100),3))
        print(f"res :{res}")
        if(res %2 == 0):
            print("Ok !")
        else : 
            print("No !")
class Env(mesa.Model):
    def __init__(self):
        super().__init__()
        self.plan = mesa.time.BaseScheduler(self)
        self.A = AgentA(0,self)
        self.B = AgentB(1,self)
        self.plan.add(self.A)
        self.plan.add(self.B)
    def step(self): 
        self.plan.step()
model = Env()
model.step()