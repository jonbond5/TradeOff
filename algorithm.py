from trader import *

l = {}

def findLoop(node):
    for n in node:
        g = 0
        n.setColor(1)
        for e in n.getEdge():
            print 'here'
            for key in e:
                print key.getName()
                if key.getColor() != int(0):
                    temp = e
                    g = 1
        if g == 1:
            l.append(temp[0].getName(), temp[1])
        n.setColor(2)
    return l

class nodes:
    have_list = []
    wants_list = []
    edges = []
    color = 0
    name = ''

    def __init__(self,n, hav, want):
        self.name = n
        self.have_list = hav
        self.wants_list = want
        
    def addEdge(self, target, item):
        self.edges.append({target: item})

    def getHave(self):
        return self.have_list

    def getWant(self):
        return self.wants_list

    def getEdge(self):
        return self.edges

    def setColor(self, num):
        color = num

    def getColor(self):
        return self.color

    def getName(self):
        return self.name

class graph:
    node_list = []

    def __init__(self):
        for usr in getUsers():
            name = usr['details']['username']
            t = getUserByField('username',str(name))
            requestList = [i.details['name'] for i in t.enumerateWantedMerch()]
            tradingList = [i.details['name'] for i in t.enumerateMerch()]
            temp = nodes(str(name),tradingList, requestList)
            self.node_list.append(temp)

    def build(self):
        for n in self.node_list:
            for m in self.node_list:
                for h in n.getHave():
                    for w in m.getWant():
                        if w == h:
                            print n.getName() in m.getName()
                            if n.getName() in m.getName():
                                pass
                            else:
                                n.addEdge(m, h)


    def getNodes(self):
        return self.node_list


g = graph()
g.build()
print g.getNodes()[1]
print 'have', g.getNodes()[1].getHave()
print 'want', g.getNodes()[1].getWant()
print 'edge', g.getNodes()[1].getEdge()
print findLoop(g.getNodes())




