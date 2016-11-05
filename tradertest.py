#!/usr/bin/env python2

from trader import Merchandise, Trader, getUserByField


# This registers graboy and grebby and returns them. If you want instances of
# pre-existing users, use Merchandise.getTrader(), or specify how I should give
# them to you.

# user1 = Trader({'username': 'graboy', 'password': 'password123'})
# user2 = Trader({'username': 'grebby', 'password': '123password'})

# This gets registered users
user1 = getUserByField('username', 'graboy')
user2 = getUserByField('username', 'grebby')

# The dictionary you pass it is stored in .details
apple = Merchandise({'name': 'apple'})
grape = Merchandise({'name': 'grape'})
pear  = Merchandise({'name': 'pear'})
pumpkin  = Merchandise({'name': 'pumpkin'})

# e.g.: apple.details['name'] == 'apple'

# createMerch: called when a user wants to put a new item of theirs up for
# trade.
user1.createMerch(apple) 
user1.createMerch(pear) 

user2.createMerch(grape) 
user2.createMerch(pumpkin) 

# Prints some ordering of "apple", "pear". enumerateMerch() is a generator that
# yields Merchandise objects.
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

# Prints owner of the pumpkin. getTrader() returns Trader object.
print pumpkin.getTrader().details['username']

# user1 wants his pear back
user1.addWantedMerch(pear)

# Print passwords of all users who have an item that user1 wants
for merch in user1.enumerateWantedMerch(): print merch.getTrader().details['password']
