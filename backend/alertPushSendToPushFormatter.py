#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.libs.internals.formatter import Formatter
from raspiot.profiles.alertPushProfile import AlertPushProfile

class AlertPushSendToPushFormatter(Formatter):
    """
    Push data to PushProfile
    """
    def __init__(self, events_broker):
        """
        Constuctor

        Args:
            events_broker (EventsBroker): events broker instance
        """
        Formatter.__init__(self, events_broker, u'alert.push.send', AlertPushProfile())

    def _fill_profile(self, event_values, profile):
        """
        Fill profile with event data
        """
        profile.message = event_values[u'title']
        profile.message = event_values[u'priority']
        profile.message = event_values[u'message']
        profile.message = event_values[u'devices']
        profile.message = event_values[u'attachment']
        profile.message = event_values[u'timestamp']

        return profile

