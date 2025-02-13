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

class KalturaCodeCuePointOrderBy(object):
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

class KalturaCodeCuePoint(KalturaCuePoint):
    code: str
    description: str
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
            code: str = NotImplemented,
            description: str = NotImplemented,
            endTime: int = NotImplemented,
            duration: int = NotImplemented): ...

    def getCode(self) -> str: ...
    def setCode(self, newCode: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getEndTime(self) -> int: ...
    def setEndTime(self, newEndTime: int) -> None: ...
    def getDuration(self) -> int: ...

class KalturaCodeCuePointBaseFilter(KalturaCuePointFilter):
    codeLike: str
    codeMultiLikeOr: str
    codeMultiLikeAnd: str
    codeEqual: str
    codeIn: str
    descriptionLike: str
    descriptionMultiLikeOr: str
    descriptionMultiLikeAnd: str
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
            codeLike: str = NotImplemented,
            codeMultiLikeOr: str = NotImplemented,
            codeMultiLikeAnd: str = NotImplemented,
            codeEqual: str = NotImplemented,
            codeIn: str = NotImplemented,
            descriptionLike: str = NotImplemented,
            descriptionMultiLikeOr: str = NotImplemented,
            descriptionMultiLikeAnd: str = NotImplemented,
            endTimeGreaterThanOrEqual: int = NotImplemented,
            endTimeLessThanOrEqual: int = NotImplemented,
            durationGreaterThanOrEqual: int = NotImplemented,
            durationLessThanOrEqual: int = NotImplemented): ...

    def getCodeLike(self) -> str: ...
    def setCodeLike(self, newCodeLike: str) -> None: ...
    def getCodeMultiLikeOr(self) -> str: ...
    def setCodeMultiLikeOr(self, newCodeMultiLikeOr: str) -> None: ...
    def getCodeMultiLikeAnd(self) -> str: ...
    def setCodeMultiLikeAnd(self, newCodeMultiLikeAnd: str) -> None: ...
    def getCodeEqual(self) -> str: ...
    def setCodeEqual(self, newCodeEqual: str) -> None: ...
    def getCodeIn(self) -> str: ...
    def setCodeIn(self, newCodeIn: str) -> None: ...
    def getDescriptionLike(self) -> str: ...
    def setDescriptionLike(self, newDescriptionLike: str) -> None: ...
    def getDescriptionMultiLikeOr(self) -> str: ...
    def setDescriptionMultiLikeOr(self, newDescriptionMultiLikeOr: str) -> None: ...
    def getDescriptionMultiLikeAnd(self) -> str: ...
    def setDescriptionMultiLikeAnd(self, newDescriptionMultiLikeAnd: str) -> None: ...
    def getEndTimeGreaterThanOrEqual(self) -> int: ...
    def setEndTimeGreaterThanOrEqual(self, newEndTimeGreaterThanOrEqual: int) -> None: ...
    def getEndTimeLessThanOrEqual(self) -> int: ...
    def setEndTimeLessThanOrEqual(self, newEndTimeLessThanOrEqual: int) -> None: ...
    def getDurationGreaterThanOrEqual(self) -> int: ...
    def setDurationGreaterThanOrEqual(self, newDurationGreaterThanOrEqual: int) -> None: ...
    def getDurationLessThanOrEqual(self) -> int: ...
    def setDurationLessThanOrEqual(self, newDurationLessThanOrEqual: int) -> None: ...

class KalturaCodeCuePointFilter(KalturaCodeCuePointBaseFilter):
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
            codeLike: str = NotImplemented,
            codeMultiLikeOr: str = NotImplemented,
            codeMultiLikeAnd: str = NotImplemented,
            codeEqual: str = NotImplemented,
            codeIn: str = NotImplemented,
            descriptionLike: str = NotImplemented,
            descriptionMultiLikeOr: str = NotImplemented,
            descriptionMultiLikeAnd: str = NotImplemented,
            endTimeGreaterThanOrEqual: int = NotImplemented,
            endTimeLessThanOrEqual: int = NotImplemented,
            durationGreaterThanOrEqual: int = NotImplemented,
            durationLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaCodeCuePointClientPluginServicesProxy: