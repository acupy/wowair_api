from datetime import timedelta, date
import requests

from wowair import WowAirError
from config import REQUEST_URL_TEMPLATE, CITY_URL
from flight import Flight
from thread import WowAirThread

class Currency(object):
    CAD = "CAD"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    ISK = "ISK"
    USD = "USD"
    SEK = "SEK"

class WowAirQuery(object):
    def __init__(self, origin, destination=[], depart_date=(), adults=1, currency=Currency.CAD):
        """
        Initialize WowAirQuery
        :param depart_date: date or tuple of date range, default range is a week
        :param origin: string - departure city
        :param destination: str or list - destination city or cities
        :param adults: int - number of adults
        """

        self.valid_cities = WowAirQuery.get_cities()

        ### DATE ###
        if isinstance(depart_date, tuple) and len(depart_date) == 2:
            self.depart_date_from = depart_date[0]
            self.depart_date_to = depart_date[1]
            self.arrival_date_from = depart_date[0]
            self.arrival_date_to = depart_date[1]
        elif isinstance(depart_date, date):
            self.depart_date_from = depart_date
            self.depart_date_to = depart_date
            self.arrival_date_from = depart_date
            self.arrival_date_to = depart_date
        else:
            default_depart_date_from = date.today()
            default_depart_date_to = default_depart_date_from + timedelta(weeks=1)
            # default values
            self.depart_date_from = default_depart_date_from
            self.depart_date_to = default_depart_date_to
            self.arrival_date_from = default_depart_date_from
            self.arrival_date_to = default_depart_date_to

        ### DEPATURE CITY ###
        if origin in self.valid_cities:
            self.origin = origin
        else:
            raise WowAirError('{0} is not in {1}'.format(origin, ', '.join(self.valid_cities.keys())))

        ### DESTINATION CITY ###
        if isinstance(destination, str):
            if destination in self.valid_cities:
                self.destination = [destination]
            else:
                raise WowAirError('{0} is not in {1}'.format(destination, ', '.join(self.valid_cities.keys())))
        elif isinstance(destination, list):
            if not destination or not set(destination) < set(self.valid_cities):
                self.destination = self.valid_cities.keys()
            else:
                self.destination = destination
        else:
            self.destination = []

        ### Number of adults ###
        if isinstance(adults, int):
            self.adults = adults
        else:
            # default values
            raise WowAirError('Number of adults is in a wrong format.')

        # Currency
        self.currency = currency

    def get_tickets(self):
        """
        Return available flights
        :return list - list of Fligh objects
        """
        threads = []
        flight_objs = []

        for request_url in self.__get_urls():
            the_thread = WowAirThread(WowAirQuery.__get_ticket_for_destination, request_url, flight_objs)
            the_thread.start()
            threads.append(the_thread)

        for the_thread in threads:
            the_thread.join()

        return flight_objs

    @staticmethod
    def get_cities():
        """
        Return the avaliable cities
        :return dict - {city_code: city_name}
        """
        request_result = requests.get(CITY_URL)
        return dict([(city['origin'], city['origin_desc']) for city in request_result.json()])

    @staticmethod
    def __get_ticket_for_destination(request_url, flight_objs):
        request_result = requests.get(request_url)
        flights = request_result.json()["flights"]

        for flight in flights:
            for fare in flight["fares"]:
                flight = Flight(flight["originShortName"].strip(),
                                flight["destinationShortName"].strip(),
                                flight["departureTime"],
                                fare["fareWithTaxes"],
                                fare["currency"],
                                flight["status"])
                flight_objs.append(flight)

    def __get_urls(self):
        """
        Return URLs to use in requests
        :return list - list of strings
        """
        links = []
        for destination in self.destination:
            links.append(REQUEST_URL_TEMPLATE.format(depart_date_from=self.depart_date_from.isoformat(),
                                                     depart_date_to=self.depart_date_to.isoformat(),
                                                     arrival_date_from=self.arrival_date_from.isoformat(),
                                                     arrival_date_to=self.arrival_date_to.isoformat(),
                                                     origin=self.origin,
                                                     destination=destination,
                                                     adults=self.adults,
                                                     currency=self.currency))
        return links
