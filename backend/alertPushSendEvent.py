#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raspiot.libs.internals.event import Event

class AlertPushSendEvent(Event):
    """
    alert.push.send event
    """

    EVENT_NAME = u'alert.push.send'
    EVENT_SYSTEM = False
    EVENT_PARAMS = [
        u'title',
        u'priority',
        u'message',
        u'devices',
        u'attachment',
        u'timestamp'
    ]

    def __init__(self, bus, formatters_broker, events_broker):
        """
        Constructor

        Args:
            bus (MessageBus): message bus instance
            formatters_broker (FormattersBroker): formatters broker instance
            events_broker (EventsBroker): events broker instance
        """
        Event.__init__(self, bus, formatters_broker, events_broker)

