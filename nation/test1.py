import pickle
class nation:
       def __init__(self, name='', continent='', pop='', area='', pop_density=''):
               self._name = name
               self._continent = continent
               self._pop = pop
               self._area = area
               self._pop_density =pop_density

       def setName(self, name):
               self._name = name

       def setContinent(self, continent):
               self._continent = continent

       def setPop(self, pop):
               self._pop = pop

       def setArea(self, area):
               self._area = area

       def getName(self, name):
               return self._name

       def getContinent(self, continent):
               return self._continent

       def getPop(self, pop):
               return self._pop

       def getArea(self, area):
               return self._area

       def pop_density(self):
               return (self._pop / self._area)
       def __str__(self):
               return ("The poplation density of" + str(self._name) + "is" + str(self.pop_density()))


f = open('UN.txt')
dict = {}
for line in f:
         words = line.split(",")
         _nation=nation(continent='', pop='', area='', pop_density='')

         _nation.setName(words[0])
         _nation.setContinent(words[1])
         _nation.setPop(words[2])
         _nation.setArea(words[3])
         dict[words[0]] = _nation

outfile = open("nationDick.dat",'wb')
pickle.dump(dict,outfile)
outfile.close()
