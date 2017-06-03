from wowair import WowAirQuery

# Fetch available cities
cities = WowAirQuery.get_cities()
for c in sorted(cities, key=lambda city: cities[city]):
    print cities[c], c

# Fetch tickets for the next week from Montreal to Dublin
wowair = WowAirQuery(origin='YUL', destination='DUB')
for ticket in wowair.get_tickets():
    print ticket
