# from ig import igdb
# from igdb_api_python import igdb
import os
import time

from igdb_api_python.igdb import igdb as igdb

# ENTER YOUR KEY HERE
igdb = igdb(os.environ['api_key'])

# RETRIEVE ONE GAME
result = igdb.games(1942)
for game in result.body:
    print("Retrieved: " + game["name"])

# Get information about ,multiple games
result = igdb.games({
    'ids': [27193, 23212, 1942]
})

# Get information about ,multiple games
result = igdb.pulses(25039)

# GET PLAYSTATION GAMES
result = igdb.platforms({
    'ids': 42,
    'fields': 'games'
})
print(result.body)

# GET PLAYSTATION GAMES
result = igdb.platforms({
    'ids': 42,
    'fields': ['games', 'name']
})

# GET COMING SOOM PLAYSTATION 4 GAMES
result = igdb.release_dates({
    'filters': {
        "[platform][eq]": 48,
        "[date][gt]": int(round(time.time() * 1000))
    },
    'order': "date:asc",
    'fields': "game"
})
# 5 game companies with name descending and offset of 5
result = igdb.companies({
    'fields': 'name',
    'limit': 5,
    'offset': 5,
    'order': 'name:desc'
})

# expand game and platform
result = igdb.release_dates({
    'ids': 86653,
    'expand': ['game', 'platform']
})

# Expand game
result = igdb.release_dates({
    'ids': 86653,
    'expand': "game",
})

# Scroll on people
result = igdb.people({
    'fields': 'name',
    'scroll': 1,
    'limit': 50
})

# This is the first page
print(str(result.body[0]["id"]))
# Get page 2
r = igdb.scroll(result)
print(r.body)
# Get page 3
r = igdb.scroll(result)
print(r.body)
