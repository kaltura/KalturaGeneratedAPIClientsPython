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

class KalturaAdCuePointOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    DURATION_ASC = "+duration"
    END_TIME_ASC = "+endTime"
    INT_ID_ASC = "+intId"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    START_TIME_ASC = "+startTime"
    TRIGGERED_AT_ASC = "+triggeredAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    DURATION_DESC = "-duration"
    END_TIME_DESC = "-endTime"
    INT_ID_DESC = "-intId"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"
    START_TIME_DESC = "-startTime"
    TRIGGERED_AT_DESC = "-triggeredAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaAdProtocolType(object):
    CUSTOM = "0"
    VAST = "1"
    VAST_2_0 = "2"
    VPAID = "3"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaAdType(object):
    VIDEO = "1"
    OVERLAY = "2"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaAdCuePoint(KalturaCuePoint):
    protocolType: KalturaAdProtocolType
    sourceUrl: str
    adType: KalturaAdType
    title: str
    endTime: int
    duration: int
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
            protocolType: KalturaAdProtocolType = NotImplemented,
            sourceUrl: str = NotImplemented,
            adType: KalturaAdType = NotImplemented,
            title: str = NotImplemented,
            endTime: int = NotImplemented,
            duration: int = NotImplemented): ...

    def getProtocolType(self) -> KalturaAdProtocolType: ...
    def setProtocolType(self, newProtocolType: KalturaAdProtocolType) -> None: ...
    def getSourceUrl(self) -> str: ...
    def setSourceUrl(self, newSourceUrl: str) -> None: ...
    def getAdType(self) -> KalturaAdType: ...
    def setAdType(self, newAdType: KalturaAdType) -> None: ...
    def getTitle(self) -> str: ...
    def setTitle(self, newTitle: str) -> None: ...
    def getEndTime(self) -> int: ...
    def setEndTime(self, newEndTime: int) -> None: ...
    def getDuration(self) -> int: ...
    def setDuration(self, newDuration: int) -> None: ...

class KalturaAdCuePointBaseFilter(KalturaCuePointFilter):
    protocolTypeEqual: KalturaAdProtocolType
    protocolTypeIn: str
    titleLike: str
    titleMultiLikeOr: str
    titleMultiLikeAnd: str
    endTimeGreaterThanOrEqual: int
    endTimeLessThanOrEqual: int
    durationGreaterThanOrEqual: int
    durationLessThanOrEqual: int
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
            protocolTypeEqual: KalturaAdProtocolType = NotImplemented,
            protocolTypeIn: str = NotImplemented,
            titleLike: str = NotImplemented,
            titleMultiLikeOr: str = NotImplemented,
            titleMultiLikeAnd: str = NotImplemented,
            endTimeGreaterThanOrEqual: int = NotImplemented,
            endTimeLessThanOrEqual: int = NotImplemented,
            durationGreaterThanOrEqual: int = NotImplemented,
            durationLessThanOrEqual: int = NotImplemented): ...

    def getProtocolTypeEqual(self) -> KalturaAdProtocolType: ...
    def setProtocolTypeEqual(self, newProtocolTypeEqual: KalturaAdProtocolType) -> None: ...
    def getProtocolTypeIn(self) -> str: ...
    def setProtocolTypeIn(self, newProtocolTypeIn: str) -> None: ...
    def getTitleLike(self) -> str: ...
    def setTitleLike(self, newTitleLike: str) -> None: ...
    def getTitleMultiLikeOr(self) -> str: ...
    def setTitleMultiLikeOr(self, newTitleMultiLikeOr: str) -> None: ...
    def getTitleMultiLikeAnd(self) -> str: ...
    def setTitleMultiLikeAnd(self, newTitleMultiLikeAnd: str) -> None: ...
    def getEndTimeGreaterThanOrEqual(self) -> int: ...
    def setEndTimeGreaterThanOrEqual(self, newEndTimeGreaterThanOrEqual: int) -> None: ...
    def getEndTimeLessThanOrEqual(self) -> int: ...
    def setEndTimeLessThanOrEqual(self, newEndTimeLessThanOrEqual: int) -> None: ...
    def getDurationGreaterThanOrEqual(self) -> int: ...
    def setDurationGreaterThanOrEqual(self, newDurationGreaterThanOrEqual: int) -> None: ...
    def getDurationLessThanOrEqual(self) -> int: ...
    def setDurationLessThanOrEqual(self, newDurationLessThanOrEqual: int) -> None: ...

class KalturaAdCuePointFilter(KalturaAdCuePointBaseFilter):
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
            protocolTypeEqual: KalturaAdProtocolType = NotImplemented,
            protocolTypeIn: str = NotImplemented,
            titleLike: str = NotImplemented,
            titleMultiLikeOr: str = NotImplemented,
            titleMultiLikeAnd: str = NotImplemented,
            endTimeGreaterThanOrEqual: int = NotImplemented,
            endTimeLessThanOrEqual: int = NotImplemented,
            durationGreaterThanOrEqual: int = NotImplemented,
            durationLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaAdCuePointClientPluginServicesProxy: