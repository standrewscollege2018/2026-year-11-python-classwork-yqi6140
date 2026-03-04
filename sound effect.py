import winsound
listy = []
class soundprojecter:
    def __init__(self,ids,frequcy,time):
        self.ids = ids
        self.frequcy = frequcy
        self.time = time
        listy.append(self)
        winsound.Beep(self.frequcy,self.time)

soundprojecter(0,2500,1000)
soundprojecter(0,3400,1000)