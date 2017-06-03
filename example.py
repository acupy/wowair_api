from wowair import WowAirQuery

wowair = WowAirQuery(origin='YUL')
for ticket in wowair.get_tickets():
    print ticket
