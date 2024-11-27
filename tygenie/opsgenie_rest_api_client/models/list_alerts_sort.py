from enum import Enum


class ListAlertsSort(str, Enum):
    ACKNOWLEDGED = "acknowledged"
    ALIAS = "alias"
    COUNT = "count"
    CREATEDAT = "createdAt"
    INTEGRATION_NAME = "integration.name"
    INTEGRATION_TYPE = "integration.type"
    ISSEEN = "isSeen"
    LASTOCCURREDAT = "lastOccurredAt"
    MESSAGE = "message"
    OWNER = "owner"
    REPORT_ACKNOWLEDGEDBY = "report.acknowledgedBy"
    REPORT_ACKTIME = "report.ackTime"
    REPORT_CLOSEDBY = "report.closedBy"
    REPORT_CLOSETIME = "report.closeTime"
    SNOOZED = "snoozed"
    SNOOZEDUNTIL = "snoozedUntil"
    SOURCE = "source"
    STATUS = "status"
    TINYID = "tinyId"
    UPDATEDAT = "updatedAt"

    def __str__(self) -> str:
        return str(self.value)
