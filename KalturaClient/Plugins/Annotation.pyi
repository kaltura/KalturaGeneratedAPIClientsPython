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

class KalturaAnnotationOrderBy(object):
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

class KalturaAnnotation(KalturaCuePoint):
    parentId: str
    text: str
    endTime: int
    duration: int
    depth: int
    childrenCount: int
    directChildrenCount: int
    isPublic: KalturaNullableBoolean
    searchableOnEntry: KalturaNullableBoolean
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
            parentId: str = NotImplemented,
            text: str = NotImplemented,
            endTime: int = NotImplemented,
            duration: int = NotImplemented,
            depth: int = NotImplemented,
            childrenCount: int = NotImplemented,
            directChildrenCount: int = NotImplemented,
            isPublic: KalturaNullableBoolean = NotImplemented,
            searchableOnEntry: KalturaNullableBoolean = NotImplemented): ...

    def getParentId(self) -> str: ...
    def setParentId(self, newParentId: str) -> None: ...
    def getText(self) -> str: ...
    def setText(self, newText: str) -> None: ...
    def getEndTime(self) -> int: ...
    def setEndTime(self, newEndTime: int) -> None: ...
    def getDuration(self) -> int: ...
    def getDepth(self) -> int: ...
    def getChildrenCount(self) -> int: ...
    def getDirectChildrenCount(self) -> int: ...
    def getIsPublic(self) -> KalturaNullableBoolean: ...
    def setIsPublic(self, newIsPublic: KalturaNullableBoolean) -> None: ...
    def getSearchableOnEntry(self) -> KalturaNullableBoolean: ...
    def setSearchableOnEntry(self, newSearchableOnEntry: KalturaNullableBoolean) -> None: ...

class KalturaAnnotationListResponse(KalturaListResponse):
    objects: List[KalturaAnnotation]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaAnnotation] = NotImplemented): ...

    def getObjects(self) -> List[KalturaAnnotation]: ...

class KalturaAnnotationBaseFilter(KalturaCuePointFilter):
    parentIdEqual: str
    parentIdIn: str
    textLike: str
    textMultiLikeOr: str
    textMultiLikeAnd: str
    endTimeGreaterThanOrEqual: int
    endTimeLessThanOrEqual: int
    durationGreaterThanOrEqual: int
    durationLessThanOrEqual: int
    isPublicEqual: KalturaNullableBoolean
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
            parentIdEqual: str = NotImplemented,
            parentIdIn: str = NotImplemented,
            textLike: str = NotImplemented,
            textMultiLikeOr: str = NotImplemented,
            textMultiLikeAnd: str = NotImplemented,
            endTimeGreaterThanOrEqual: int = NotImplemented,
            endTimeLessThanOrEqual: int = NotImplemented,
            durationGreaterThanOrEqual: int = NotImplemented,
            durationLessThanOrEqual: int = NotImplemented,
            isPublicEqual: KalturaNullableBoolean = NotImplemented): ...

    def getParentIdEqual(self) -> str: ...
    def setParentIdEqual(self, newParentIdEqual: str) -> None: ...
    def getParentIdIn(self) -> str: ...
    def setParentIdIn(self, newParentIdIn: str) -> None: ...
    def getTextLike(self) -> str: ...
    def setTextLike(self, newTextLike: str) -> None: ...
    def getTextMultiLikeOr(self) -> str: ...
    def setTextMultiLikeOr(self, newTextMultiLikeOr: str) -> None: ...
    def getTextMultiLikeAnd(self) -> str: ...
    def setTextMultiLikeAnd(self, newTextMultiLikeAnd: str) -> None: ...
    def getEndTimeGreaterThanOrEqual(self) -> int: ...
    def setEndTimeGreaterThanOrEqual(self, newEndTimeGreaterThanOrEqual: int) -> None: ...
    def getEndTimeLessThanOrEqual(self) -> int: ...
    def setEndTimeLessThanOrEqual(self, newEndTimeLessThanOrEqual: int) -> None: ...
    def getDurationGreaterThanOrEqual(self) -> int: ...
    def setDurationGreaterThanOrEqual(self, newDurationGreaterThanOrEqual: int) -> None: ...
    def getDurationLessThanOrEqual(self) -> int: ...
    def setDurationLessThanOrEqual(self, newDurationLessThanOrEqual: int) -> None: ...
    def getIsPublicEqual(self) -> KalturaNullableBoolean: ...
    def setIsPublicEqual(self, newIsPublicEqual: KalturaNullableBoolean) -> None: ...

class KalturaAnnotationFilter(KalturaAnnotationBaseFilter):
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
            parentIdEqual: str = NotImplemented,
            parentIdIn: str = NotImplemented,
            textLike: str = NotImplemented,
            textMultiLikeOr: str = NotImplemented,
            textMultiLikeAnd: str = NotImplemented,
            endTimeGreaterThanOrEqual: int = NotImplemented,
            endTimeLessThanOrEqual: int = NotImplemented,
            durationGreaterThanOrEqual: int = NotImplemented,
            durationLessThanOrEqual: int = NotImplemented,
            isPublicEqual: KalturaNullableBoolean = NotImplemented): ...
        pass

class KalturaAnnotationService(KalturaServiceBase):
    def add(self, annotation: KalturaCuePoint) -> KalturaAnnotation: ...
    def addFromBulk(self, fileData: IO[Any]) -> KalturaCuePointListResponse: ...
    def clone(self, id: str, entryId: str, parentId: str = NotImplemented) -> KalturaAnnotation: ...
    def count(self, filter: KalturaCuePointFilter = NotImplemented) -> int: ...
    def delete(self, id: str) -> None: ...
    def get(self, id: str) -> KalturaCuePoint: ...
    def list(self, filter: KalturaCuePointFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaAnnotationListResponse: ...
    def serveBulk(self, filter: KalturaCuePointFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> IO[Any]: ...
    def update(self, id: str, annotation: KalturaCuePoint) -> KalturaAnnotation: ...
    def updateCuePointsTimes(self, id: str, startTime: int, endTime: int = NotImplemented) -> KalturaCuePoint: ...
    def updateStatus(self, id: str, status: int) -> None: ...

class KalturaAnnotationClientPluginServicesProxy:
    annotation: KalturaAnnotationService