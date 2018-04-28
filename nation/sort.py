import matplotlib.pyplot as plt
import pickle
import nation

def getDictionary(fileName):
    infile = open(fileName, 'rb')
    nations =pickle.load(infile)
    infile.close()
    return nations

nations = getDictionary("nationsDict.dat")
for country in nations:
    pop_density = _nation.pop_density()
pop_density.sort

plt.bar(nations[nation]['name'], nations[nation]['pop_density'])
plt.title('TOP 10 NATIONS')
plt.xlabel('Country')
plt.ylabel('Population Density')
plt.show()
