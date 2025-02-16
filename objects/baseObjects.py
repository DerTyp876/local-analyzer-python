
# TODO new objects: healthcare, police

# TODO Address object "addr:"
# ? offices 
# ? How to handle districts


class Place:
    def __init__(self, _nodeIds, _type, _name, _address = None, _contact = None, _openingHours = None):
        self.nodeIds = _nodeIds
        self.type = _type
        self.name = _name
        self.address = _address
        self.contact = _contact
        self.openingHours = _openingHours

class Node:
    def __init__(self, _id, _lon, _lat, _version, _timestamp, _changeset, _uid, _user):
        self.id = int(_id)
        self.lon = str(_lon)
        self.lat = str(_lat)
        self.version = str(_version)
        self.timestamp = str(_timestamp)
        self.changeset = int(_changeset)
        self.uid = int(_uid)
        self.user = str(_user)


class NodeTag:
    def __init__(self, _id, _nodeId, _key, _value):
        self.id = int(_id)
        self.nodeId = int(_nodeId)
        self.key = str(_key)
        self.value = str(_value)

class Way:
    def __init__(self, _id, _version, _timestamp, _changeset, _uid, _user):
        self.id = int(_id)
        self.version = str(_version)
        self.timestamp = str(_timestamp)
        self.changeset = int(_changeset)
        self.uid = int(_uid)
        self.user = str(_user)


class WayTag:
    def __init__(self, _id, _wayId, _key, _value):
        self.id = int(_id)
        self.wayId = int(_wayId)
        self.key = str(_key)
        self.value = str(_value)
