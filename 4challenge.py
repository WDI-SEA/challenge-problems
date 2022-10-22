# Garbage collector

# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

# dict for each truck and the time it spent collecting trash
# iterate over garbage list and 

def garbage_collector(garbage, travel):
    # dict to keep track of total time spent collecting garbage
    trucks = {
        "M": 0,
        "P": 0,
        "G": 0
    }
    # dict to keep track of the last house a truck visited
    last_house = {
        "M": 0,
        "P": 0,
        "G": 0
    }
    # iterate over garbage list
    for i, house in enumerate(garbage):
        # iterate over house string
        for trash in house:
            # if a type of garbage is there
            if trash in trucks:
                # add 1 min to that trucks time
                trucks[trash] += 1
                # set this house to be the last house that truck visited
                last_house[trash] = i
    
    # to calculate total travel time
    # check each truck's last house visited
    for truck in last_house:
        # iterate over travel list up to whatever index of the last house visited
        for i in range(last_house[truck]):
            # add together all the values
            trucks[truck] += travel[i]
    
    # return the total time taken
    return trucks["M"] + trucks["P"] + trucks["G"]

print(garbage_collector(["G","P","GP","GG"], [2,4,3]))
print(garbage_collector(["MMM","PGM","GP"], [3,10]))