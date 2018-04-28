class nation
    def __init__(self, name , continent, pop, area, pop_density ):
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

    def setPop_density(self, pop_density):
        self._pop_density = pop_density


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

    def
