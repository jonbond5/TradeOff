#!/usr/bin/env python2

from trader import Merchandise, Trader


# This registers graboy and grebby and returns them. If you want instances of
# pre-existing users
user1 = Trader({'username': 'graboy', 'password': 'password123'})
user2 = Trader({'username': 'grebby', 'password': '123password'})


# The dictionary you pass it is stored in .details
apple = Merchandise({'name': 'apple'})
grape = Merchandise({'name': 'grape'})
pear  = Merchandise({'name': 'pear'})
pumpkin  = Merchandise({'name': 'pumpkin'})

# e.g.: apple.details['name'] == 'apple'

# createMerch: called when a user wants to put up a new item of theirs for
# trade.
user1.createMerch(apple) 
user1.createMerch(pear) 

user2.createMerch(grape) 
user2.createMerch(pumpkin) 

# Prints some ordering of "apple", "pear":
for merch in user1.enumerateMerch(): print merch.details['name'] 

# Prints some ordering of "grape", "pumpkin":
for merch in user2.enumerateMerch(): print merch.details['name'] 

# user1 wants user2's pumpkin:
user1.addWantedMerch(pumpkin)

# user2 wants user1's pear:
user2.addWantedMerch(pear)

# Should print what user1 wants, a pumpkin:
for merch in user1.enumerateWantedMerch(): print merch.details['name']

# Pear-pumpkin trade:
user1.transferMerch(pear, user2)
user2.transferMerch(pumpkin, user1)

# What do they have now after the trade? 
# (Prints apple pumpkin, then pear grape)
for merch in user1.enumerateMerch(): print merch.details['name'] 
for merch in user2.enumerateMerch(): print merch.details['name'] 

# Shouldn't print anything since user1 got his pumpkin:
for merch in user1.enumerateWantedMerch(): print merch.details['name'] 

# Owner of the pumpkin:
pumpkin.getTrader().details['
