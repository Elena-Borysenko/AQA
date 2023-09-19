casino_blacklist = {'Alan Adams', 'Tod Baker', 'Elizabeth Bennett'}
poker_blacklist = {'Tod Baker', 'Betty Brooks', 'Sam Burton'}
alcohol_blacklist = {'Eliza Carter', 'Cortney Cox', 'Tod Baker'}

casino_blacklist.intersection_update(poker_blacklist, alcohol_blacklist)
print(casino_blacklist)