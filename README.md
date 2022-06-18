# pyubibot
Ubibot API wrapped in Python implementation library.

Currently, only supports application key access to all "channels" (devices) associated to the account.

The base class is a Channel. Each channel has accessor methods to return the latest data from the channel.

Channels object holds multiple channel. All channels are held in a dictionary keyed on their channel_id.
