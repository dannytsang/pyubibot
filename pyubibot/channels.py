import logging
import json
from datetime import datetime

_LOGGER = logging.getLogger(__name__)


class Channel:
    """Model representing single channel.
    Provides accessor methods to easily traverse channel data.
    """

    def __init__(self, data, channel_id):
        """Initialise with Channel information"""
        self._data = data
        self._channel_id = channel_id

    @property
    def get_id(self):
        return self._channel_id

    @property
    def get_name(self):
        return self._name

    @property
    def get_data(self):
        return self._data

    def get_value(self, field_name):
        """Get top level value based on field name"""
        return self._data.get(field_name)

    def get_field_name_by_sensor(self, name):
        """Fields the field holding a sensor.
        For example: field1:Temperator,field2:"Humidity",field3:"Light"
        Passing "Temperator" will return "field1" which can be used to find the last recorded value for temperator.
        """
        i = 1
        field_name = None
        while "field" + str(i) in self._data.get("last_values"):
            if self._data.get("field" + str(i)) == name:
                return "field" + str(i)
            elif i > 100:
                # fail safe assuming there is no more than 100 fields per channel.
                return None
            else:
                i += 1

    def get_last_value(self):
        """Returns last recorded values in a dictionary."""
        return json.loads(self._data.get("last_values"))

    def get_last_value_by_field(self, field_name):
        """Returns the last value record for given field."""
        return self.get_last_value().get(field_name).get("value")

    def get_last_updated_by_field(self, field_name):
        """Returns the last value record for given field."""
        return datetime.strptime(self.get_last_value().get(field_name).get("created_at"), "%Y-%m-%dT%H:%M:%SZ")
