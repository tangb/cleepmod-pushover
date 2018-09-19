#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.events.formatter import Formatter
from raspiot.events.alertPushProfile import AlertPushProfile

class AlertPushSendToPushFormatter(Formatter):
    """
    Push data to PushProfile
    """
    def __init__(self, events_factory):
        """
        Constuctor

        Args:
            events_factory (EventsFactory): events factory instance
        """
        Formatter.__init__(self, events_factory, u'alert.push.send', AlertPushProfile())

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

