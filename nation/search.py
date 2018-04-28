import pickle
import nation

def getDictionary(fileName):
    infile = open(fileName, 'rb')
    nations =pickle.load(infile)
    infile.close()
    return nations

def inputNameOfNation(nations):
    nation = input("Input a name of a UN member nation: ")
    while nation not in nations:
        print("Not a member of the UN.Please try again.")
        nation = input("Input a name of a UN member nation: ")

def displayData(nations,nation):
    print("Continent:", nations[nation]['continent'])
    print("Populaton:",nations[nation]['pop'], "million people")
    print("Area:",nations[nation]['area'],"square miles")

nations = getDictionary("nationsDict.dat")
nation = inputNameOfNation(nations)
displayData(nations,nation)
