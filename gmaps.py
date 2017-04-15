from googlemaps import convert
from googlemaps.convert import as_list


def distance_matrix(client, origins, destinations,
                    mode=None, language=None, avoid=None, units=None,
                    departure_time=None, arrival_time=None, transit_mode=None,
                    transit_routing_preference=None, traffic_model=None):
	 params = {
        "origins": convert.location_list(origins),
        "destinations": convert.location_list(destinations)
    }

    return client._request("/maps/api/distancematrix/json", params)
