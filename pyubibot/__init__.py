"""
Simple python library for UbiBot REST API.
See https://www.ubibot.io/category/faqs/ for more details.
ubibot.com account credentials are needed to use this lib.
Enabling tags sharing is not required.
see www.ubibot.io/ for more information.
I am in no way affiliated with UbiBot.io.
Copyrights: (c) 2020 Danny Tsang, see LICENSE file for details
Creation Date: 24/02/2020.
"""

import logging
import requests
from datetime import datetime


import pyubibot.constants as CONST
from pyubibot.channels import Channel

_LOGGER = logging.getLogger(__name__)


class Ubibot:
    """Principal class for Channels."""

    _HEADERS = CONST.HEADERS

    def __init__(self, account_key):
        """Initialize Ubibot platform."""
        self._account_key = account_key
        self._channels = {}
        self._response = None

    def get_channels(self):
        """Load all channels."""
        try:
            response = requests.get(url=CONST.CHANNELS_URL,
                                    params={"account_key": self._account_key},
                                    headers=self._HEADERS).json()

            if response.get("result") == "success":
                c = response["channels"]
                for channel in c:
                    channel_id = channel["channel_id"]
                    self._channels[channel_id] = Channel(channel, channel_id)
                _LOGGER.info("Channels reloaded at: %s", datetime.now())
            else:
                raise Exception(self._response.get("errorCode"))
        except (Exception) as error:
            _LOGGER.error("failed to load channels - %s", error)
            raise error

        return self._channels

    def get_channel(self, channel_id):
        """Get a single channel data by channel_id."""
        try:
            response = requests.get(url=CONST.CHANNEL_URL+channel_id,
                                    params={"account_key": self._account_key},
                                    headers=self._HEADERS).json()

            if response.get("result") == "success":
                # Replace channel in the list with updated data.
                self._channels[channel_id] = Channel(response["channel"], channel_id)
                _LOGGER.info("Channel reloaded at: %s", datetime.now())

                return self._channels[channel_id]
            else:
                raise Exception(self._response.get("errorCode"))
        except (Exception) as error:
            _LOGGER.error("failed to load channel - %s", error)
            raise error
