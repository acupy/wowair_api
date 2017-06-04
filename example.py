from wowair import WowAirQuery
from datetime import timedelta, date

# Fetch available cities
cities = WowAirQuery.get_cities()
for c in sorted(cities, key=lambda city: cities[city]):
    print cities[c], c

# Fetch tickets for the next week from Montreal to Dublin
query = WowAirQuery(origin='YUL', destination='DUB')
for ticket in query.get_tickets():
    print ticket

# Fetch Available tickets for the NEXT 30 DAYS from New York to Anywhere
depart_date_from = date.today()
depart_date_to = depart_date_from + timedelta(days=30)
query = WowAirQuery(origin='EWR', depart_date=(depart_date_from, depart_date_to))
for ticket in query.get_tickets():
    if ticket.status == 'Available':
        print ticket
