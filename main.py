import http.client
import urllib.error
import urllib.parse
import urllib.request
import json
import time
from os import path

api_key = 'f13b6b39374447729a83b60a69208005'


def wmata_get_bus_position():
    headers = {
        # Request headers
        'api_key': api_key,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'RouteID': 'X2',
        'Lat': '{number}',
        'Lon': '{number}',
        'Radius': '{number}',
    })

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Bus.svc/json/jBusPositions?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        data_json = json.loads(data)
        # s = json.dumps(data_json, indent=4, sort_keys=False)
        # print(s)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    # query VehicleID
    buses = ["5491", "5485"]
    bus_position_record = []
    for bus_id in buses:
        for bus_position in data_json["BusPositions"]:
            if bus_id == bus_position["VehicleID"]:
                # s = json.dumps(bus_position, indent=4, sort_keys=False)
                # print(s)
                bus_position_record.append(bus_position)
    return bus_position_record


def wmata_record_bus_position(filename=None, timespan=0.5):
    start_time = time.time()
    timespan_sec = timespan * 3600
    counter = 0
    if filename is None:
        filename = "bus_position_" + time.strftime("%Y%m%d-%H%M%S") + ".json"
    while time.time() - start_time < timespan_sec:
        bus_position_record = wmata_get_bus_position()
        with open(filename, "a") as outfile:
            json.dump(bus_position_record, outfile, indent=4, sort_keys=False)
            counter += 1
            print("record: ", counter)
        time.sleep(10)
    print("Done: total record", counter)


def wmata_get_path_details():
    headers = {
        # Request headers
        'api_key': api_key,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'RouteID': 'X2',
        'Date': '{string}',
    })

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Bus.svc/json/jRouteDetails?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        data_json = json.loads(data)
        s = json.dumps(data_json, indent=4, sort_keys=False)
        print(s)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def wmata_get_all_routes():
    headers = {
        # Request headers
        'api_key': api_key,
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Bus.svc/json/jRoutes?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        data_json = json.loads(data)
        s = json.dumps(data_json, indent=4, sort_keys=False)
        print(s)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def wmata_get_stop_and_schedule():
    headers = {
        # Request headers
        'api_key': api_key,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'RouteID': 'X2',
        'Date': '{string}',
        'IncludingVariations': 'false',
    })

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Bus.svc/json/jRouteSchedule?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        data_json = json.loads(data)
        s = json.dumps(data_json, indent=4, sort_keys=False)
        print(s)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def wmata_get_schedule_at_stop(stop_id=None):
    headers = {
        # Request headers
        'api_key': api_key,
    }
    if stop_id is None:
        stop_id = '1001195'
    params = urllib.parse.urlencode({
        # Request parameters
        'StopID': stop_id,
        'Date': '{string}',
    })

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Bus.svc/json/jStopSchedule?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        data_json = json.loads(data)
        s = json.dumps(data_json, indent=4, sort_keys=False)
        print(s)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def wmata_stop_search():
    headers = {
        # Request headers
        'api_key': api_key,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'Lat': '{number}',
        'Lon': '{number}',
        'Radius': '{number}',
    })

    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/Bus.svc/json/jStops?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        data_json = json.loads(data)
        s = json.dumps(data_json, indent=4, sort_keys=False)
        print(s)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


if __name__ == '__main__':
    # wmata_get_bus_position()
    # wmata_record_bus_position(None, 0.1)
    # wmata_get_path_details()
    # wmata_get_all_routes()
    # wmata_get_stop_and_schedule()
    # wmata_get_schedule_at_stop()
    wmata_stop_search()