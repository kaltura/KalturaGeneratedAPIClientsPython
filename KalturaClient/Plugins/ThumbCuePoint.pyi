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

class KalturaThumbCuePointOrderBy(object):
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

class KalturaTimedThumbAssetOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    DELETED_AT_ASC = "+deletedAt"
    SIZE_ASC = "+size"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    DELETED_AT_DESC = "-deletedAt"
    SIZE_DESC = "-size"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaThumbCuePoint(KalturaCuePoint):
    assetId: str
    description: str
    title: str
    subType: KalturaThumbCuePointSubType
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
            assetId: str = NotImplemented,
            description: str = NotImplemented,
            title: str = NotImplemented,
            subType: KalturaThumbCuePointSubType = NotImplemented): ...

    def getAssetId(self) -> str: ...
    def setAssetId(self, newAssetId: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getTitle(self) -> str: ...
    def setTitle(self, newTitle: str) -> None: ...
    def getSubType(self) -> KalturaThumbCuePointSubType: ...
    def setSubType(self, newSubType: KalturaThumbCuePointSubType) -> None: ...

class KalturaTimedThumbAsset(KalturaThumbAsset):
    cuePointId: str
    def __init__(self,
            id: str = NotImplemented,
            entryId: str = NotImplemented,
            partnerId: int = NotImplemented,
            version: int = NotImplemented,
            size: int = NotImplemented,
            tags: str = NotImplemented,
            fileExt: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            deletedAt: int = NotImplemented,
            description: str = NotImplemented,
            partnerData: str = NotImplemented,
            partnerDescription: str = NotImplemented,
            actualSourceAssetParamsIds: str = NotImplemented,
            sizeInBytes: int = NotImplemented,
            thumbParamsId: int = NotImplemented,
            width: int = NotImplemented,
            height: int = NotImplemented,
            status: KalturaThumbAssetStatus = NotImplemented,
            cuePointId: str = NotImplemented): ...

    def getCuePointId(self) -> str: ...
    def setCuePointId(self, newCuePointId: str) -> None: ...

class KalturaThumbCuePointBaseFilter(KalturaCuePointFilter):
    descriptionLike: str
    descriptionMultiLikeOr: str
    descriptionMultiLikeAnd: str
    titleLike: str
    titleMultiLikeOr: str
    titleMultiLikeAnd: str
    subTypeEqual: KalturaThumbCuePointSubType
    subTypeIn: str
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
            descriptionLike: str = NotImplemented,
            descriptionMultiLikeOr: str = NotImplemented,
            descriptionMultiLikeAnd: str = NotImplemented,
            titleLike: str = NotImplemented,
            titleMultiLikeOr: str = NotImplemented,
            titleMultiLikeAnd: str = NotImplemented,
            subTypeEqual: KalturaThumbCuePointSubType = NotImplemented,
            subTypeIn: str = NotImplemented): ...

    def getDescriptionLike(self) -> str: ...
    def setDescriptionLike(self, newDescriptionLike: str) -> None: ...
    def getDescriptionMultiLikeOr(self) -> str: ...
    def setDescriptionMultiLikeOr(self, newDescriptionMultiLikeOr: str) -> None: ...
    def getDescriptionMultiLikeAnd(self) -> str: ...
    def setDescriptionMultiLikeAnd(self, newDescriptionMultiLikeAnd: str) -> None: ...
    def getTitleLike(self) -> str: ...
    def setTitleLike(self, newTitleLike: str) -> None: ...
    def getTitleMultiLikeOr(self) -> str: ...
    def setTitleMultiLikeOr(self, newTitleMultiLikeOr: str) -> None: ...
    def getTitleMultiLikeAnd(self) -> str: ...
    def setTitleMultiLikeAnd(self, newTitleMultiLikeAnd: str) -> None: ...
    def getSubTypeEqual(self) -> KalturaThumbCuePointSubType: ...
    def setSubTypeEqual(self, newSubTypeEqual: KalturaThumbCuePointSubType) -> None: ...
    def getSubTypeIn(self) -> str: ...
    def setSubTypeIn(self, newSubTypeIn: str) -> None: ...

class KalturaThumbCuePointFilter(KalturaThumbCuePointBaseFilter):
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
            descriptionLike: str = NotImplemented,
            descriptionMultiLikeOr: str = NotImplemented,
            descriptionMultiLikeAnd: str = NotImplemented,
            titleLike: str = NotImplemented,
            titleMultiLikeOr: str = NotImplemented,
            titleMultiLikeAnd: str = NotImplemented,
            subTypeEqual: KalturaThumbCuePointSubType = NotImplemented,
            subTypeIn: str = NotImplemented): ...
        pass

class KalturaTimedThumbAssetBaseFilter(KalturaThumbAssetFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            sizeGreaterThanOrEqual: int = NotImplemented,
            sizeLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            deletedAtGreaterThanOrEqual: int = NotImplemented,
            deletedAtLessThanOrEqual: int = NotImplemented,
            typeIn: str = NotImplemented,
            thumbParamsIdEqual: int = NotImplemented,
            thumbParamsIdIn: str = NotImplemented,
            statusEqual: KalturaThumbAssetStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented): ...
        pass

class KalturaTimedThumbAssetFilter(KalturaTimedThumbAssetBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            sizeGreaterThanOrEqual: int = NotImplemented,
            sizeLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            deletedAtGreaterThanOrEqual: int = NotImplemented,
            deletedAtLessThanOrEqual: int = NotImplemented,
            typeIn: str = NotImplemented,
            thumbParamsIdEqual: int = NotImplemented,
            thumbParamsIdIn: str = NotImplemented,
            statusEqual: KalturaThumbAssetStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented): ...
        pass

class KalturaThumbCuePointClientPluginServicesProxy: