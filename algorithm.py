import trader

# Initialize test cases
trader1 = Trader()
trader2 = Trader()
trader3 = Trader()
trader4 = Trader()
trader5 = Trader()
trader1.want = ['apple','banana','chode']
trader2.want = ['grape','apple']
trader3.want = ['computer','tape']
trader4.want = ['gun']
trader1.give = ['computer']
trader2.give = ['apple','dragonfuit']
trader3.give = ['gun']
trader4.give = ['grape']
database = [trader1,trader2,trader3,trader4]

def PSUEDOPARSE(wants):
    listOfPeople = []
    for person in database:
        for elem in person.give:
            if elem == wants:
                listOfPeople += [people]
                break
    return listOfPeople


# Find out how trader1 can trade with
def findWantToGive(trader):
    want = trader.want
    potential_traders
    
