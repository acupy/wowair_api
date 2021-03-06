.. image:: https://img.shields.io/pypi/v/wowair.svg
   :target: https://pypi.python.org/pypi/wowair
.. image:: https://img.shields.io/pypi/l/wowair.svg
   :target: https://pypi.python.org/pypi/wowair
.. image:: https://img.shields.io/github/issues/acupy/wowair_api.svg
   :target: https://github.com/acupy/wowair_api
.. image:: https://img.shields.io/github/issues-closed/acupy/wowair_api.svg
   :target: https://github.com/acupy/wowair_api

Install
=======

Run the following command to install wowair using pip

.. code-block:: bash

    $ pip install wowair

Usage:
======

.. code-block:: python

    from wowair import WowAirQuery, Currency
    from datetime import timedelta, date

    # Fetch available cities
    cities = WowAirQuery.get_cities()
    for c in sorted(cities, key=lambda city: cities[city]):
        print cities[c], c

    # Fetch tickets for the next week from Montreal to Dublin
    query = WowAirQuery(origin='YUL', destination='DUB')
    for ticket in query.get_tickets():
        print ticket

    # Fetch Available tickets from New York to Anywhere in the NEXT 30 DAYS
    depart_date_from = date.today()
    depart_date_to = depart_date_from + timedelta(days=30)
    query = WowAirQuery(origin='EWR',
                        depart_date=(depart_date_from, depart_date_to),
                        currency=Currency.USD)
    for ticket in query.get_tickets():
        if ticket.status == 'Available':
            print ticket
