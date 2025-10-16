import mesa 
class Agent_Ach (mesa.Agent) : 
    def __init__(self,id,model): 
        super().__init__(id,model)
    def step(self): 
        self.offres = []
        for agent in self.model.agents : 
            if isinstance(agent,Agent_Ven): 
                offre = agent.offre()
                if offre : 
                    self.offres.append(offre)
        if self.offres : 
            best = self.offres[0]
            for ofr in self.offres : 
                if best["price"] > ofr["price"] : 
                    best = ofr 
            print(f"meilleur prix est {best['price']}:")
class Agent_Ven (mesa.Agent) : 
    def __init__(self,id,price,model): 
        super().__init__(id,model)
        self.price = price
    def offre(self) : 
        return {'price':self.price}
    def step(self): 
        pass
class Env(mesa.Model):
    def __init__(self):
        self.A = Agent_Ach(0,self)
        self.V1 = Agent_Ven(1,100.00,self)
        self.V2 = Agent_Ven(2,120.00,self)
        self.V3 = Agent_Ven(3,130.00,self)
        self.plan = mesa.time.BaseScheduler(self)
        self.plan.add(self.A)
        self.plan.add(self.V1)
        self.plan.add(self.V2)
        self.plan.add(self.V3)
    def step(self) :
        self.plan.step()
model = Env()
model.step()
       

        
