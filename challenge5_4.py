# Kate Macias
# Software Engineering 1
# Fall 2026


import math, pprint

class EventManager:
    R = 6378100     # radius of the earth in m

    def __init__(self, eventList):
        self.eventList = eventList

    def distance(self, lat1, lon1, lat2, lon2):
        # https://stackoverflow.com/a/27943

        dLat = self.deg2rad(lat2 - lat1)
        dLon = self.deg2rad(lon2 - lon1)
        a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
            math.cos(self.deg2rad(lat1)) * math.cos(self.deg2rad(lat2)) * \
            math.sin(dLon / 2) * math.sin(dLon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
        return self.R * c    # distance in m

    def deg2rad(self, d):
        return d * math.pi / 180

    def findEventsNear(self, lat, lon, maxDist=5000):
        events = []

        for event in self.eventList:
            name, type, elat, elon, _ = event.split(":")
            elat = float(elat)
            elon = float(elon)

            if self.distance(lat, lon, elat, elon) < maxDist:
                events.append(event)

        return events

    def findEarthquakesNear(self, cityName):
        cityRecord = None

        for event in self.eventList:
            name, type, elat, elon, _ = event.split(":")
            elat = float(elat)
            elon = float(elon)

            if type == "city" and name == cityName:
                cityRecord = event

        if cityRecord is None:
            return None

        name, type, clat, clon, _ = cityRecord.split(":")
        clat = float(clat)
        clon = float(clon)

        events = []

        for event in self.eventList:
            name, type, elat, elon, _ = event.split(":")
            elat = float(elat)
            elon = float(elon)

            if type == "earthquake":
                if self.distance(elat, elon, clat, clon) < 5000:
                    events.append(event)

        return events

    def addVolcanoEvent(self, name, lat, lon, time):
        self.eventList.append(f"{name}:volcano:{lat}:{lon}:{time}")

    def addEarthquakeEvent(self, name, lat, lon, time):
        self.eventList.append(f"{name}:earthquake:{lat}:{lon}:{time}")

    def addGeyser(self, name, lat, lon, time):
        self.eventList.append(f"{name}:geyser:{lat}:{lon}:{time}")

    def addHotspring(self, name, lat, lon):
        self.eventList.append(f"{name}:hotspring:{lat}:{lon}:-1")

    def addFumarole(self, name, lat, lon):
        self.eventList.append(f"{name}:fumarole:{lat}:{lon}:-1")

    def addCity(self, name, lat, lon):
        self.eventList.append(f"{name}:city:{lat}:{lon}:-1")

starting_events = [
    "some volcano:volcano:40.12120:-121.3455:21451",
    "some earthquake:earthquake:40.51230:-121.23425:87153",
    "another earthquake:earthquake:39.23890:-120.23985:17354",
    "yet another earthquake:earthquake:39.23223:-120.23125:16524",
    "another volcano:volcano:43.32890:-122.3289:23856",
    "a geyser:geyser:39.23223:-120.23125:-1",
    "Townville:city:44.05645:-121.30812:-1"
]

em = EventManager(starting_events)

em.addHotspring("my favorite hotspring", 46.1231, -115.23234)
em.addCity("Cityton", 40.5232, -121.23453)
em.addVolcanoEvent("yet another volcano", 15.52232, -107.03521, 256923)

x = em.findEventsNear(40.5, -121.2, 163000)
pprint.pprint(x)

print("------------------------")

x = em.findEarthquakesNear("Cityton")
pprint.pprint(x)
