from enum import Enum


class BidirectionalCallbackBidirectionalCallbackType(str, Enum):
    CONNECT_WISE_CALLBACK = "connect-wise-callback"
    DESK_CALLBACK = "desk-callback"
    ES_WATCHER_CALLBACK = "es-watcher-callback"
    HIP_CHAT_ADD_ON_CALLBACK = "hip-chat-add-on-callback"
    HIP_CHAT_CALLBACK_V2 = "hip-chat-callback-v2"
    ICINGA2_CALLBACK = "icinga2-callback"
    ICINGA_CALLBACK = "icinga-callback"
    MARID_CALLBACK = "marid-callback"
    MATTERMOST_CALLBACK = "mattermost-callback"
    NAGIOS_BASED_V1_CALLBACK = "nagios-based-v1-callback"
    NAGIOS_BASED_V2_CALLBACK = "nagios-based-v2-callback"
    NAGIOS_XIV1_CALLBACK = "nagios-xiv1-callback"
    NAGIOS_XIV2_CALLBACK = "nagios-xiv2-callback"
    SLACK_APP_CALLBACK = "slack-app-callback"
    SLACK_CALLBACK = "slack-callback"
    SOLARWINDS_CALLBACK = "solarwinds-callback"
    SOLAR_WINDS_WEB_HELP_DESK_CALLBACK = "solar-winds-web-help-desk-callback"
    STACKDRIVER_CALLBACK = "stackdriver-callback"
    STATUS_IO_CALLBACK = "status-io-callback"
    TRACK_IT_CALLBACK = "track-it-callback"
    XMPP_CALLBACK = "xmpp-callback"
    ZABBIX_CALLBACK = "zabbix-callback"
    ZENOSS_CALLBACK = "zenoss-callback"

    def __str__(self) -> str:
        return str(self.value)
