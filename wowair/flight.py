class Flight:
    def __init__(self, origin_short_name, destination_short_name, departure_time, fare_with_taxes, currency, status):
        """
        Initialize Flight
        :param origin_short_name: string - departure city
        :param destination_short_name: string - destination city
        :param departure_time: datetime - departure time
        :param fare_with_taxes: float - price or the fare incl. tax
        :param currency: str - currency
        :param status: string - status, eg.: Available
        """
        self.origin_short_name = origin_short_name
        self.destination_short_name = destination_short_name
        self.departure_time = departure_time
        self.fare_with_taxes = fare_with_taxes
        self.currency = currency
        self.status = status

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.origin_short_name.encode('utf8'),
                                                self.destination_short_name.encode('utf8'),
                                                self.departure_time,
                                                self.fare_with_taxes,
                                                self.currency,
                                                self.status)
