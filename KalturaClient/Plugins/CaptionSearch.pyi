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
from .Caption import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaCaptionAssetItem(KalturaObjectBase):
    asset: KalturaCaptionAsset
    entry: KalturaBaseEntry
    startTime: int
    endTime: int
    content: str
    def __init__(self,
            asset: KalturaCaptionAsset = NotImplemented,
            entry: KalturaBaseEntry = NotImplemented,
            startTime: int = NotImplemented,
            endTime: int = NotImplemented,
            content: str = NotImplemented): ...

    def getAsset(self) -> KalturaCaptionAsset: ...
    def setAsset(self, newAsset: KalturaCaptionAsset) -> None: ...
    def getEntry(self) -> KalturaBaseEntry: ...
    def setEntry(self, newEntry: KalturaBaseEntry) -> None: ...
    def getStartTime(self) -> int: ...
    def setStartTime(self, newStartTime: int) -> None: ...
    def getEndTime(self) -> int: ...
    def setEndTime(self, newEndTime: int) -> None: ...
    def getContent(self) -> str: ...
    def setContent(self, newContent: str) -> None: ...

class KalturaCaptionAssetItemListResponse(KalturaListResponse):
    objects: List[KalturaCaptionAssetItem]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaCaptionAssetItem] = NotImplemented): ...

    def getObjects(self) -> List[KalturaCaptionAssetItem]: ...

class KalturaEntryCaptionAssetSearchItem(KalturaSearchItem):
    contentLike: str
    contentMultiLikeOr: str
    contentMultiLikeAnd: str
    def __init__(self,
            contentLike: str = NotImplemented,
            contentMultiLikeOr: str = NotImplemented,
            contentMultiLikeAnd: str = NotImplemented): ...

    def getContentLike(self) -> str: ...
    def setContentLike(self, newContentLike: str) -> None: ...
    def getContentMultiLikeOr(self) -> str: ...
    def setContentMultiLikeOr(self, newContentMultiLikeOr: str) -> None: ...
    def getContentMultiLikeAnd(self) -> str: ...
    def setContentMultiLikeAnd(self, newContentMultiLikeAnd: str) -> None: ...

class KalturaCaptionAssetItemFilter(KalturaCaptionAssetFilter):
    contentLike: str
    contentMultiLikeOr: str
    contentMultiLikeAnd: str
    partnerDescriptionLike: str
    partnerDescriptionMultiLikeOr: str
    partnerDescriptionMultiLikeAnd: str
    languageEqual: KalturaLanguage
    languageIn: str
    labelEqual: str
    labelIn: str
    startTimeGreaterThanOrEqual: int
    startTimeLessThanOrEqual: int
    endTimeGreaterThanOrEqual: int
    endTimeLessThanOrEqual: int
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
            captionParamsIdEqual: int = NotImplemented,
            captionParamsIdIn: str = NotImplemented,
            formatEqual: KalturaCaptionType = NotImplemented,
            formatIn: str = NotImplemented,
            statusEqual: KalturaCaptionAssetStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            contentLike: str = NotImplemented,
            contentMultiLikeOr: str = NotImplemented,
            contentMultiLikeAnd: str = NotImplemented,
            partnerDescriptionLike: str = NotImplemented,
            partnerDescriptionMultiLikeOr: str = NotImplemented,
            partnerDescriptionMultiLikeAnd: str = NotImplemented,
            languageEqual: KalturaLanguage = NotImplemented,
            languageIn: str = NotImplemented,
            labelEqual: str = NotImplemented,
            labelIn: str = NotImplemented,
            startTimeGreaterThanOrEqual: int = NotImplemented,
            startTimeLessThanOrEqual: int = NotImplemented,
            endTimeGreaterThanOrEqual: int = NotImplemented,
            endTimeLessThanOrEqual: int = NotImplemented): ...

    def getContentLike(self) -> str: ...
    def setContentLike(self, newContentLike: str) -> None: ...
    def getContentMultiLikeOr(self) -> str: ...
    def setContentMultiLikeOr(self, newContentMultiLikeOr: str) -> None: ...
    def getContentMultiLikeAnd(self) -> str: ...
    def setContentMultiLikeAnd(self, newContentMultiLikeAnd: str) -> None: ...
    def getPartnerDescriptionLike(self) -> str: ...
    def setPartnerDescriptionLike(self, newPartnerDescriptionLike: str) -> None: ...
    def getPartnerDescriptionMultiLikeOr(self) -> str: ...
    def setPartnerDescriptionMultiLikeOr(self, newPartnerDescriptionMultiLikeOr: str) -> None: ...
    def getPartnerDescriptionMultiLikeAnd(self) -> str: ...
    def setPartnerDescriptionMultiLikeAnd(self, newPartnerDescriptionMultiLikeAnd: str) -> None: ...
    def getLanguageEqual(self) -> KalturaLanguage: ...
    def setLanguageEqual(self, newLanguageEqual: KalturaLanguage) -> None: ...
    def getLanguageIn(self) -> str: ...
    def setLanguageIn(self, newLanguageIn: str) -> None: ...
    def getLabelEqual(self) -> str: ...
    def setLabelEqual(self, newLabelEqual: str) -> None: ...
    def getLabelIn(self) -> str: ...
    def setLabelIn(self, newLabelIn: str) -> None: ...
    def getStartTimeGreaterThanOrEqual(self) -> int: ...
    def setStartTimeGreaterThanOrEqual(self, newStartTimeGreaterThanOrEqual: int) -> None: ...
    def getStartTimeLessThanOrEqual(self) -> int: ...
    def setStartTimeLessThanOrEqual(self, newStartTimeLessThanOrEqual: int) -> None: ...
    def getEndTimeGreaterThanOrEqual(self) -> int: ...
    def setEndTimeGreaterThanOrEqual(self, newEndTimeGreaterThanOrEqual: int) -> None: ...
    def getEndTimeLessThanOrEqual(self) -> int: ...
    def setEndTimeLessThanOrEqual(self, newEndTimeLessThanOrEqual: int) -> None: ...

class KalturaCaptionAssetItemService(KalturaServiceBase):
    def list(self, captionAssetId: str, captionAssetItemFilter: KalturaCaptionAssetItemFilter = NotImplemented, captionAssetItemPager: KalturaFilterPager = NotImplemented) -> KalturaCaptionAssetItemListResponse: ...
    def search(self, entryFilter: KalturaBaseEntryFilter = NotImplemented, captionAssetItemFilter: KalturaCaptionAssetItemFilter = NotImplemented, captionAssetItemPager: KalturaFilterPager = NotImplemented) -> KalturaCaptionAssetItemListResponse: ...
    def searchEntries(self, entryFilter: KalturaBaseEntryFilter = NotImplemented, captionAssetItemFilter: KalturaCaptionAssetItemFilter = NotImplemented, captionAssetItemPager: KalturaFilterPager = NotImplemented) -> KalturaBaseEntryListResponse: ...

class KalturaCaptionSearchClientPluginServicesProxy:
    captionAssetItem: KalturaCaptionAssetItemService