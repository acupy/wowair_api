__BASE_API_URL = "https://booking.wowair.com/api/midgardur"
__API_VERSION = "v2"
__QUERY_STRING = ("departDateFrom={depart_date_from}&"
                 "departDateTo={depart_date_to}&"
                 "arrivalDateFrom={arrival_date_from}&"
                 "arrivalDateTo={arrival_date_to}&"
                 "origin={origin}&"
                 "destination={destination}&"
                 "fareTypeCategories=1&"
                 "useFlexDates=true&"
                 "culture=us&"
                 "infants=0&"
                 "children=0&"
                 "currency={currency}&"
                 "roundTrip=false&"
                 "adults={adults}&"
                 "promocode=")
REQUEST_URL_TEMPLATE = "{0}/{1}/flight?{2}".format(__BASE_API_URL,
                                                   __API_VERSION,
                                                   __QUERY_STRING)
CITY_URL = "https://wowair.is/api/wow/routes"
