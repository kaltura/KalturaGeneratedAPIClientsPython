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
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaRoomType(object):
    ROOM = 1
    BREAKOUT = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaRoomEntryOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    END_DATE_ASC = "+endDate"
    MODERATION_COUNT_ASC = "+moderationCount"
    NAME_ASC = "+name"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    RANK_ASC = "+rank"
    RECENT_ASC = "+recent"
    START_DATE_ASC = "+startDate"
    TOTAL_RANK_ASC = "+totalRank"
    UPDATED_AT_ASC = "+updatedAt"
    WEIGHT_ASC = "+weight"
    CREATED_AT_DESC = "-createdAt"
    END_DATE_DESC = "-endDate"
    MODERATION_COUNT_DESC = "-moderationCount"
    NAME_DESC = "-name"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"
    RANK_DESC = "-rank"
    RECENT_DESC = "-recent"
    START_DATE_DESC = "-startDate"
    TOTAL_RANK_DESC = "-totalRank"
    UPDATED_AT_DESC = "-updatedAt"
    WEIGHT_DESC = "-weight"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaRoomEntry(KalturaBaseEntry):
    roomType: KalturaRoomType
    broadcastEntryId: str
    templateRoomEntryId: str
    def __init__(self,
            id: str = NotImplemented,
            name: str = NotImplemented,
            multiLingual_name: List[KalturaMultiLingualString] = NotImplemented,
            description: str = NotImplemented,
            multiLingual_description: List[KalturaMultiLingualString] = NotImplemented,
            partnerId: int = NotImplemented,
            userId: str = NotImplemented,
            creatorId: str = NotImplemented,
            tags: str = NotImplemented,
            multiLingual_tags: List[KalturaMultiLingualString] = NotImplemented,
            adminTags: str = NotImplemented,
            categories: str = NotImplemented,
            categoriesIds: str = NotImplemented,
            status: KalturaEntryStatus = NotImplemented,
            moderationStatus: KalturaEntryModerationStatus = NotImplemented,
            moderationCount: int = NotImplemented,
            type: KalturaEntryType = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            rank: float = NotImplemented,
            totalRank: int = NotImplemented,
            votes: int = NotImplemented,
            groupId: int = NotImplemented,
            partnerData: str = NotImplemented,
            downloadUrl: str = NotImplemented,
            searchText: str = NotImplemented,
            licenseType: KalturaLicenseType = NotImplemented,
            version: int = NotImplemented,
            thumbnailUrl: str = NotImplemented,
            accessControlId: int = NotImplemented,
            startDate: int = NotImplemented,
            endDate: int = NotImplemented,
            referenceId: str = NotImplemented,
            replacingEntryId: str = NotImplemented,
            replacedEntryId: str = NotImplemented,
            replacementStatus: KalturaEntryReplacementStatus = NotImplemented,
            partnerSortValue: int = NotImplemented,
            conversionProfileId: int = NotImplemented,
            redirectEntryId: str = NotImplemented,
            rootEntryId: str = NotImplemented,
            parentEntryId: str = NotImplemented,
            operationAttributes: List[KalturaOperationAttributes] = NotImplemented,
            entitledUsersEdit: str = NotImplemented,
            entitledUsersPublish: str = NotImplemented,
            entitledUsersView: str = NotImplemented,
            capabilities: str = NotImplemented,
            templateEntryId: str = NotImplemented,
            displayInSearch: KalturaEntryDisplayInSearchType = NotImplemented,
            application: KalturaEntryApplication = NotImplemented,
            applicationVersion: str = NotImplemented,
            blockAutoTranscript: bool = NotImplemented,
            defaultLanguage: str = NotImplemented,
            responseLanguage: str = NotImplemented,
            roomType: KalturaRoomType = NotImplemented,
            broadcastEntryId: str = NotImplemented,
            templateRoomEntryId: str = NotImplemented): ...

    def getRoomType(self) -> KalturaRoomType: ...
    def setRoomType(self, newRoomType: KalturaRoomType) -> None: ...
    def getBroadcastEntryId(self) -> str: ...
    def setBroadcastEntryId(self, newBroadcastEntryId: str) -> None: ...
    def getTemplateRoomEntryId(self) -> str: ...
    def setTemplateRoomEntryId(self, newTemplateRoomEntryId: str) -> None: ...

class KalturaRoomEntryListResponse(KalturaListResponse):
    objects: List[KalturaRoomEntry]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaRoomEntry] = NotImplemented): ...

    def getObjects(self) -> List[KalturaRoomEntry]: ...

class KalturaRoomEntryBaseFilter(KalturaBaseEntryFilter):
    roomTypeEqual: KalturaRoomType
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            nameMultiLikeOr: str = NotImplemented,
            nameMultiLikeAnd: str = NotImplemented,
            nameEqual: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            userIdNotIn: str = NotImplemented,
            creatorIdEqual: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            adminTagsLike: str = NotImplemented,
            adminTagsMultiLikeOr: str = NotImplemented,
            adminTagsMultiLikeAnd: str = NotImplemented,
            categoriesMatchAnd: str = NotImplemented,
            categoriesMatchOr: str = NotImplemented,
            categoriesNotContains: str = NotImplemented,
            categoriesIdsMatchAnd: str = NotImplemented,
            categoriesIdsMatchOr: str = NotImplemented,
            categoriesIdsNotContains: str = NotImplemented,
            categoriesIdsEmpty: KalturaNullableBoolean = NotImplemented,
            statusEqual: KalturaEntryStatus = NotImplemented,
            statusNotEqual: KalturaEntryStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            moderationStatusEqual: KalturaEntryModerationStatus = NotImplemented,
            moderationStatusNotEqual: KalturaEntryModerationStatus = NotImplemented,
            moderationStatusIn: str = NotImplemented,
            moderationStatusNotIn: str = NotImplemented,
            typeEqual: KalturaEntryType = NotImplemented,
            typeIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            rankLessThanOrEqual: float = NotImplemented,
            rankGreaterThanOrEqual: float = NotImplemented,
            totalRankLessThanOrEqual: int = NotImplemented,
            totalRankGreaterThanOrEqual: int = NotImplemented,
            groupIdEqual: int = NotImplemented,
            searchTextMatchAnd: str = NotImplemented,
            searchTextMatchOr: str = NotImplemented,
            accessControlIdEqual: int = NotImplemented,
            accessControlIdIn: str = NotImplemented,
            startDateGreaterThanOrEqual: int = NotImplemented,
            startDateLessThanOrEqual: int = NotImplemented,
            startDateGreaterThanOrEqualOrNull: int = NotImplemented,
            startDateLessThanOrEqualOrNull: int = NotImplemented,
            endDateGreaterThanOrEqual: int = NotImplemented,
            endDateLessThanOrEqual: int = NotImplemented,
            endDateGreaterThanOrEqualOrNull: int = NotImplemented,
            endDateLessThanOrEqualOrNull: int = NotImplemented,
            referenceIdEqual: str = NotImplemented,
            referenceIdIn: str = NotImplemented,
            replacingEntryIdEqual: str = NotImplemented,
            replacingEntryIdIn: str = NotImplemented,
            replacedEntryIdEqual: str = NotImplemented,
            replacedEntryIdIn: str = NotImplemented,
            replacementStatusEqual: KalturaEntryReplacementStatus = NotImplemented,
            replacementStatusIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            rootEntryIdEqual: str = NotImplemented,
            rootEntryIdIn: str = NotImplemented,
            parentEntryIdEqual: str = NotImplemented,
            entitledUsersEditMatchAnd: str = NotImplemented,
            entitledUsersEditMatchOr: str = NotImplemented,
            entitledUsersPublishMatchAnd: str = NotImplemented,
            entitledUsersPublishMatchOr: str = NotImplemented,
            entitledUsersViewMatchAnd: str = NotImplemented,
            entitledUsersViewMatchOr: str = NotImplemented,
            tagsNameMultiLikeOr: str = NotImplemented,
            tagsAdminTagsMultiLikeOr: str = NotImplemented,
            tagsAdminTagsNameMultiLikeOr: str = NotImplemented,
            tagsNameMultiLikeAnd: str = NotImplemented,
            tagsAdminTagsMultiLikeAnd: str = NotImplemented,
            tagsAdminTagsNameMultiLikeAnd: str = NotImplemented,
            displayInSearchEqual: KalturaEntryDisplayInSearchType = NotImplemented,
            displayInSearchIn: str = NotImplemented,
            freeText: str = NotImplemented,
            excludedFreeTextGroups: str = NotImplemented,
            descriptionLike: str = NotImplemented,
            isRoot: KalturaNullableBoolean = NotImplemented,
            categoriesFullNameIn: str = NotImplemented,
            categoryAncestorIdIn: str = NotImplemented,
            redirectFromEntryId: str = NotImplemented,
            conversionProfileIdEqual: int = NotImplemented,
            roomTypeEqual: KalturaRoomType = NotImplemented): ...

    def getRoomTypeEqual(self) -> KalturaRoomType: ...
    def setRoomTypeEqual(self, newRoomTypeEqual: KalturaRoomType) -> None: ...

class KalturaRoomEntryFilter(KalturaRoomEntryBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            nameMultiLikeOr: str = NotImplemented,
            nameMultiLikeAnd: str = NotImplemented,
            nameEqual: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            userIdNotIn: str = NotImplemented,
            creatorIdEqual: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            adminTagsLike: str = NotImplemented,
            adminTagsMultiLikeOr: str = NotImplemented,
            adminTagsMultiLikeAnd: str = NotImplemented,
            categoriesMatchAnd: str = NotImplemented,
            categoriesMatchOr: str = NotImplemented,
            categoriesNotContains: str = NotImplemented,
            categoriesIdsMatchAnd: str = NotImplemented,
            categoriesIdsMatchOr: str = NotImplemented,
            categoriesIdsNotContains: str = NotImplemented,
            categoriesIdsEmpty: KalturaNullableBoolean = NotImplemented,
            statusEqual: KalturaEntryStatus = NotImplemented,
            statusNotEqual: KalturaEntryStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            moderationStatusEqual: KalturaEntryModerationStatus = NotImplemented,
            moderationStatusNotEqual: KalturaEntryModerationStatus = NotImplemented,
            moderationStatusIn: str = NotImplemented,
            moderationStatusNotIn: str = NotImplemented,
            typeEqual: KalturaEntryType = NotImplemented,
            typeIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            rankLessThanOrEqual: float = NotImplemented,
            rankGreaterThanOrEqual: float = NotImplemented,
            totalRankLessThanOrEqual: int = NotImplemented,
            totalRankGreaterThanOrEqual: int = NotImplemented,
            groupIdEqual: int = NotImplemented,
            searchTextMatchAnd: str = NotImplemented,
            searchTextMatchOr: str = NotImplemented,
            accessControlIdEqual: int = NotImplemented,
            accessControlIdIn: str = NotImplemented,
            startDateGreaterThanOrEqual: int = NotImplemented,
            startDateLessThanOrEqual: int = NotImplemented,
            startDateGreaterThanOrEqualOrNull: int = NotImplemented,
            startDateLessThanOrEqualOrNull: int = NotImplemented,
            endDateGreaterThanOrEqual: int = NotImplemented,
            endDateLessThanOrEqual: int = NotImplemented,
            endDateGreaterThanOrEqualOrNull: int = NotImplemented,
            endDateLessThanOrEqualOrNull: int = NotImplemented,
            referenceIdEqual: str = NotImplemented,
            referenceIdIn: str = NotImplemented,
            replacingEntryIdEqual: str = NotImplemented,
            replacingEntryIdIn: str = NotImplemented,
            replacedEntryIdEqual: str = NotImplemented,
            replacedEntryIdIn: str = NotImplemented,
            replacementStatusEqual: KalturaEntryReplacementStatus = NotImplemented,
            replacementStatusIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            rootEntryIdEqual: str = NotImplemented,
            rootEntryIdIn: str = NotImplemented,
            parentEntryIdEqual: str = NotImplemented,
            entitledUsersEditMatchAnd: str = NotImplemented,
            entitledUsersEditMatchOr: str = NotImplemented,
            entitledUsersPublishMatchAnd: str = NotImplemented,
            entitledUsersPublishMatchOr: str = NotImplemented,
            entitledUsersViewMatchAnd: str = NotImplemented,
            entitledUsersViewMatchOr: str = NotImplemented,
            tagsNameMultiLikeOr: str = NotImplemented,
            tagsAdminTagsMultiLikeOr: str = NotImplemented,
            tagsAdminTagsNameMultiLikeOr: str = NotImplemented,
            tagsNameMultiLikeAnd: str = NotImplemented,
            tagsAdminTagsMultiLikeAnd: str = NotImplemented,
            tagsAdminTagsNameMultiLikeAnd: str = NotImplemented,
            displayInSearchEqual: KalturaEntryDisplayInSearchType = NotImplemented,
            displayInSearchIn: str = NotImplemented,
            freeText: str = NotImplemented,
            excludedFreeTextGroups: str = NotImplemented,
            descriptionLike: str = NotImplemented,
            isRoot: KalturaNullableBoolean = NotImplemented,
            categoriesFullNameIn: str = NotImplemented,
            categoryAncestorIdIn: str = NotImplemented,
            redirectFromEntryId: str = NotImplemented,
            conversionProfileIdEqual: int = NotImplemented,
            roomTypeEqual: KalturaRoomType = NotImplemented): ...
        pass

class KalturaRoomService(KalturaServiceBase):
    def add(self, entry: KalturaRoomEntry) -> KalturaRoomEntry: ...
    def attachRecordedEntry(self, roomEntryId: str, mediaEntryId: str) -> KalturaMediaEntry: ...
    def delete(self, roomId: str) -> None: ...
    def get(self, roomId: str) -> KalturaRoomEntry: ...
    def list(self, filter: KalturaRoomEntryFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaRoomEntryListResponse: ...
    def update(self, roomId: str, room: KalturaRoomEntry) -> KalturaRoomEntry: ...

class KalturaRoomClientPluginServicesProxy:
    room: KalturaRoomService