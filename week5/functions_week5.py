#function_lab5.py

#Question 3
def collect_lost(loot_options,belt):
    print("Random loot process:")
    loot_roll=random.choice(range(1,len(loot_options)+1))
    loot= loot_options.pop(loot_roll -1)
    print("   |   Your belt: ",belt)
    return loot_options,belt