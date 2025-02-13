# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platforms allow them to do with
# text.
#
# Copyright (C) 2006-2023  Kaltura Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# @ignore
# ===================================================================================================
from typing import List, IO, Any
from .Core import *
from .CuePoint import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaEventCuePointOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    INT_ID_ASC = "+intId"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    START_TIME_ASC = "+startTime"
    TRIGGERED_AT_ASC = "+triggeredAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    INT_ID_DESC = "-intId"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"
    START_TIME_DESC = "-startTime"
    TRIGGERED_AT_DESC = "-triggeredAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEventType(object):
    BROADCAST_START = "1"
    BROADCAST_END = "2"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEventCuePoint(KalturaCuePoint):
    eventType: KalturaEventType
    def __init__(self,
            id: str = NotImplemented,
            intId: int = NotImplemented,
            cuePointType: KalturaCuePointType = NotImplemented,
            status: KalturaCuePointStatus = NotImplemented,
            entryId: str = NotImplemented,
            partnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            triggeredAt: int = NotImplemented,
            tags: str = NotImplemented,
            startTime: int = NotImplemented,
            userId: str = NotImplemented,
            partnerData: str = NotImplemented,
            partnerSortValue: int = NotImplemented,
            forceStop: KalturaNullableBoolean = NotImplemented,
            thumbOffset: int = NotImplemented,
            systemName: str = NotImplemented,
            isMomentary: bool = NotImplemented,
            copiedFrom: str = NotImplemented,
            eventType: KalturaEventType = NotImplemented): ...

    def getEventType(self) -> KalturaEventType: ...
    def setEventType(self, newEventType: KalturaEventType) -> None: ...

class KalturaEventCuePointBaseFilter(KalturaCuePointFilter):
    eventTypeEqual: KalturaEventType
    eventTypeIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            cuePointTypeEqual: KalturaCuePointType = NotImplemented,
            cuePointTypeIn: str = NotImplemented,
            statusEqual: KalturaCuePointStatus = NotImplemented,
            statusIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            triggeredAtGreaterThanOrEqual: int = NotImplemented,
            triggeredAtLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            startTimeGreaterThanOrEqual: int = NotImplemented,
            startTimeLessThanOrEqual: int = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            partnerSortValueEqual: int = NotImplemented,
            partnerSortValueIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            forceStopEqual: KalturaNullableBoolean = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            freeText: str = NotImplemented,
            userIdEqualCurrent: KalturaNullableBoolean = NotImplemented,
            userIdCurrent: KalturaNullableBoolean = NotImplemented,
            eventTypeEqual: KalturaEventType = NotImplemented,
            eventTypeIn: str = NotImplemented): ...

    def getEventTypeEqual(self) -> KalturaEventType: ...
    def setEventTypeEqual(self, newEventTypeEqual: KalturaEventType) -> None: ...
    def getEventTypeIn(self) -> str: ...
    def setEventTypeIn(self, newEventTypeIn: str) -> None: ...

class KalturaEventCuePointFilter(KalturaEventCuePointBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            cuePointTypeEqual: KalturaCuePointType = NotImplemented,
            cuePointTypeIn: str = NotImplemented,
            statusEqual: KalturaCuePointStatus = NotImplemented,
            statusIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            triggeredAtGreaterThanOrEqual: int = NotImplemented,
            triggeredAtLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            startTimeGreaterThanOrEqual: int = NotImplemented,
            startTimeLessThanOrEqual: int = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            partnerSortValueEqual: int = NotImplemented,
            partnerSortValueIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            forceStopEqual: KalturaNullableBoolean = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            freeText: str = NotImplemented,
            userIdEqualCurrent: KalturaNullableBoolean = NotImplemented,
            userIdCurrent: KalturaNullableBoolean = NotImplemented,
            eventTypeEqual: KalturaEventType = NotImplemented,
            eventTypeIn: str = NotImplemented): ...
        pass

class KalturaEventCuePointClientPluginServicesProxy: