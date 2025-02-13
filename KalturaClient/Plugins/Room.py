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
# @package Kaltura
# @subpackage Client
from __future__ import absolute_import

from .Core import *
from ..Base import (
    getXmlNodeBool,
    getXmlNodeFloat,
    getXmlNodeInt,
    getXmlNodeText,
    KalturaClientPlugin,
    KalturaEnumsFactory,
    KalturaObjectBase,
    KalturaObjectFactory,
    KalturaParams,
    KalturaServiceBase,
)

########## enums ##########
# @package Kaltura
# @subpackage Client
class KalturaRoomType(object):
    ROOM = 1
    BREAKOUT = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
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

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaRoomEntry(KalturaBaseEntry):
    def __init__(self,
            id = NotImplemented,
            name = NotImplemented,
            multiLingual_name = NotImplemented,
            description = NotImplemented,
            multiLingual_description = NotImplemented,
            partnerId = NotImplemented,
            userId = NotImplemented,
            creatorId = NotImplemented,
            tags = NotImplemented,
            multiLingual_tags = NotImplemented,
            adminTags = NotImplemented,
            categories = NotImplemented,
            categoriesIds = NotImplemented,
            status = NotImplemented,
            moderationStatus = NotImplemented,
            moderationCount = NotImplemented,
            type = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            rank = NotImplemented,
            totalRank = NotImplemented,
            votes = NotImplemented,
            groupId = NotImplemented,
            partnerData = NotImplemented,
            downloadUrl = NotImplemented,
            searchText = NotImplemented,
            licenseType = NotImplemented,
            version = NotImplemented,
            thumbnailUrl = NotImplemented,
            accessControlId = NotImplemented,
            startDate = NotImplemented,
            endDate = NotImplemented,
            referenceId = NotImplemented,
            replacingEntryId = NotImplemented,
            replacedEntryId = NotImplemented,
            replacementStatus = NotImplemented,
            partnerSortValue = NotImplemented,
            conversionProfileId = NotImplemented,
            redirectEntryId = NotImplemented,
            rootEntryId = NotImplemented,
            parentEntryId = NotImplemented,
            operationAttributes = NotImplemented,
            entitledUsersEdit = NotImplemented,
            entitledUsersPublish = NotImplemented,
            entitledUsersView = NotImplemented,
            capabilities = NotImplemented,
            templateEntryId = NotImplemented,
            displayInSearch = NotImplemented,
            application = NotImplemented,
            applicationVersion = NotImplemented,
            blockAutoTranscript = NotImplemented,
            defaultLanguage = NotImplemented,
            responseLanguage = NotImplemented,
            roomType = NotImplemented,
            broadcastEntryId = NotImplemented,
            templateRoomEntryId = NotImplemented):
        KalturaBaseEntry.__init__(self,
            id,
            name,
            multiLingual_name,
            description,
            multiLingual_description,
            partnerId,
            userId,
            creatorId,
            tags,
            multiLingual_tags,
            adminTags,
            categories,
            categoriesIds,
            status,
            moderationStatus,
            moderationCount,
            type,
            createdAt,
            updatedAt,
            rank,
            totalRank,
            votes,
            groupId,
            partnerData,
            downloadUrl,
            searchText,
            licenseType,
            version,
            thumbnailUrl,
            accessControlId,
            startDate,
            endDate,
            referenceId,
            replacingEntryId,
            replacedEntryId,
            replacementStatus,
            partnerSortValue,
            conversionProfileId,
            redirectEntryId,
            rootEntryId,
            parentEntryId,
            operationAttributes,
            entitledUsersEdit,
            entitledUsersPublish,
            entitledUsersView,
            capabilities,
            templateEntryId,
            displayInSearch,
            application,
            applicationVersion,
            blockAutoTranscript,
            defaultLanguage,
            responseLanguage)

        # @var KalturaRoomType
        self.roomType = roomType

        # The entryId of the broadcast that the room streaming to
        # @var str
        self.broadcastEntryId = broadcastEntryId

        # The entryId of the room where settings will be taken from
        # @var str
        self.templateRoomEntryId = templateRoomEntryId


    PROPERTY_LOADERS = {
        'roomType': (KalturaEnumsFactory.createInt, "KalturaRoomType"), 
        'broadcastEntryId': getXmlNodeText, 
        'templateRoomEntryId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRoomEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntry.toParams(self)
        kparams.put("objectType", "KalturaRoomEntry")
        kparams.addIntEnumIfDefined("roomType", self.roomType)
        kparams.addStringIfDefined("broadcastEntryId", self.broadcastEntryId)
        kparams.addStringIfDefined("templateRoomEntryId", self.templateRoomEntryId)
        return kparams

    def getRoomType(self):
        return self.roomType

    def setRoomType(self, newRoomType):
        self.roomType = newRoomType

    def getBroadcastEntryId(self):
        return self.broadcastEntryId

    def setBroadcastEntryId(self, newBroadcastEntryId):
        self.broadcastEntryId = newBroadcastEntryId

    def getTemplateRoomEntryId(self):
        return self.templateRoomEntryId

    def setTemplateRoomEntryId(self, newTemplateRoomEntryId):
        self.templateRoomEntryId = newTemplateRoomEntryId


# @package Kaltura
# @subpackage Client
class KalturaRoomEntryListResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaRoomEntry]
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaRoomEntry'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRoomEntryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRoomEntryListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaRoomEntryBaseFilter(KalturaBaseEntryFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            nameLike = NotImplemented,
            nameMultiLikeOr = NotImplemented,
            nameMultiLikeAnd = NotImplemented,
            nameEqual = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            userIdEqual = NotImplemented,
            userIdIn = NotImplemented,
            userIdNotIn = NotImplemented,
            creatorIdEqual = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            adminTagsLike = NotImplemented,
            adminTagsMultiLikeOr = NotImplemented,
            adminTagsMultiLikeAnd = NotImplemented,
            categoriesMatchAnd = NotImplemented,
            categoriesMatchOr = NotImplemented,
            categoriesNotContains = NotImplemented,
            categoriesIdsMatchAnd = NotImplemented,
            categoriesIdsMatchOr = NotImplemented,
            categoriesIdsNotContains = NotImplemented,
            categoriesIdsEmpty = NotImplemented,
            statusEqual = NotImplemented,
            statusNotEqual = NotImplemented,
            statusIn = NotImplemented,
            statusNotIn = NotImplemented,
            moderationStatusEqual = NotImplemented,
            moderationStatusNotEqual = NotImplemented,
            moderationStatusIn = NotImplemented,
            moderationStatusNotIn = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            rankLessThanOrEqual = NotImplemented,
            rankGreaterThanOrEqual = NotImplemented,
            totalRankLessThanOrEqual = NotImplemented,
            totalRankGreaterThanOrEqual = NotImplemented,
            groupIdEqual = NotImplemented,
            searchTextMatchAnd = NotImplemented,
            searchTextMatchOr = NotImplemented,
            accessControlIdEqual = NotImplemented,
            accessControlIdIn = NotImplemented,
            startDateGreaterThanOrEqual = NotImplemented,
            startDateLessThanOrEqual = NotImplemented,
            startDateGreaterThanOrEqualOrNull = NotImplemented,
            startDateLessThanOrEqualOrNull = NotImplemented,
            endDateGreaterThanOrEqual = NotImplemented,
            endDateLessThanOrEqual = NotImplemented,
            endDateGreaterThanOrEqualOrNull = NotImplemented,
            endDateLessThanOrEqualOrNull = NotImplemented,
            referenceIdEqual = NotImplemented,
            referenceIdIn = NotImplemented,
            replacingEntryIdEqual = NotImplemented,
            replacingEntryIdIn = NotImplemented,
            replacedEntryIdEqual = NotImplemented,
            replacedEntryIdIn = NotImplemented,
            replacementStatusEqual = NotImplemented,
            replacementStatusIn = NotImplemented,
            partnerSortValueGreaterThanOrEqual = NotImplemented,
            partnerSortValueLessThanOrEqual = NotImplemented,
            rootEntryIdEqual = NotImplemented,
            rootEntryIdIn = NotImplemented,
            parentEntryIdEqual = NotImplemented,
            entitledUsersEditMatchAnd = NotImplemented,
            entitledUsersEditMatchOr = NotImplemented,
            entitledUsersPublishMatchAnd = NotImplemented,
            entitledUsersPublishMatchOr = NotImplemented,
            entitledUsersViewMatchAnd = NotImplemented,
            entitledUsersViewMatchOr = NotImplemented,
            tagsNameMultiLikeOr = NotImplemented,
            tagsAdminTagsMultiLikeOr = NotImplemented,
            tagsAdminTagsNameMultiLikeOr = NotImplemented,
            tagsNameMultiLikeAnd = NotImplemented,
            tagsAdminTagsMultiLikeAnd = NotImplemented,
            tagsAdminTagsNameMultiLikeAnd = NotImplemented,
            displayInSearchEqual = NotImplemented,
            displayInSearchIn = NotImplemented,
            freeText = NotImplemented,
            excludedFreeTextGroups = NotImplemented,
            descriptionLike = NotImplemented,
            isRoot = NotImplemented,
            categoriesFullNameIn = NotImplemented,
            categoryAncestorIdIn = NotImplemented,
            redirectFromEntryId = NotImplemented,
            conversionProfileIdEqual = NotImplemented,
            roomTypeEqual = NotImplemented):
        KalturaBaseEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            userIdIn,
            userIdNotIn,
            creatorIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesNotContains,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            categoriesIdsNotContains,
            categoriesIdsEmpty,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            rankLessThanOrEqual,
            rankGreaterThanOrEqual,
            totalRankLessThanOrEqual,
            totalRankGreaterThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            parentEntryIdEqual,
            entitledUsersEditMatchAnd,
            entitledUsersEditMatchOr,
            entitledUsersPublishMatchAnd,
            entitledUsersPublishMatchOr,
            entitledUsersViewMatchAnd,
            entitledUsersViewMatchOr,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            displayInSearchEqual,
            displayInSearchIn,
            freeText,
            excludedFreeTextGroups,
            descriptionLike,
            isRoot,
            categoriesFullNameIn,
            categoryAncestorIdIn,
            redirectFromEntryId,
            conversionProfileIdEqual)

        # @var KalturaRoomType
        self.roomTypeEqual = roomTypeEqual


    PROPERTY_LOADERS = {
        'roomTypeEqual': (KalturaEnumsFactory.createInt, "KalturaRoomType"), 
    }

    def fromXml(self, node):
        KalturaBaseEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRoomEntryBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaRoomEntryBaseFilter")
        kparams.addIntEnumIfDefined("roomTypeEqual", self.roomTypeEqual)
        return kparams

    def getRoomTypeEqual(self):
        return self.roomTypeEqual

    def setRoomTypeEqual(self, newRoomTypeEqual):
        self.roomTypeEqual = newRoomTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaRoomEntryFilter(KalturaRoomEntryBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            nameLike = NotImplemented,
            nameMultiLikeOr = NotImplemented,
            nameMultiLikeAnd = NotImplemented,
            nameEqual = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            userIdEqual = NotImplemented,
            userIdIn = NotImplemented,
            userIdNotIn = NotImplemented,
            creatorIdEqual = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            adminTagsLike = NotImplemented,
            adminTagsMultiLikeOr = NotImplemented,
            adminTagsMultiLikeAnd = NotImplemented,
            categoriesMatchAnd = NotImplemented,
            categoriesMatchOr = NotImplemented,
            categoriesNotContains = NotImplemented,
            categoriesIdsMatchAnd = NotImplemented,
            categoriesIdsMatchOr = NotImplemented,
            categoriesIdsNotContains = NotImplemented,
            categoriesIdsEmpty = NotImplemented,
            statusEqual = NotImplemented,
            statusNotEqual = NotImplemented,
            statusIn = NotImplemented,
            statusNotIn = NotImplemented,
            moderationStatusEqual = NotImplemented,
            moderationStatusNotEqual = NotImplemented,
            moderationStatusIn = NotImplemented,
            moderationStatusNotIn = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            rankLessThanOrEqual = NotImplemented,
            rankGreaterThanOrEqual = NotImplemented,
            totalRankLessThanOrEqual = NotImplemented,
            totalRankGreaterThanOrEqual = NotImplemented,
            groupIdEqual = NotImplemented,
            searchTextMatchAnd = NotImplemented,
            searchTextMatchOr = NotImplemented,
            accessControlIdEqual = NotImplemented,
            accessControlIdIn = NotImplemented,
            startDateGreaterThanOrEqual = NotImplemented,
            startDateLessThanOrEqual = NotImplemented,
            startDateGreaterThanOrEqualOrNull = NotImplemented,
            startDateLessThanOrEqualOrNull = NotImplemented,
            endDateGreaterThanOrEqual = NotImplemented,
            endDateLessThanOrEqual = NotImplemented,
            endDateGreaterThanOrEqualOrNull = NotImplemented,
            endDateLessThanOrEqualOrNull = NotImplemented,
            referenceIdEqual = NotImplemented,
            referenceIdIn = NotImplemented,
            replacingEntryIdEqual = NotImplemented,
            replacingEntryIdIn = NotImplemented,
            replacedEntryIdEqual = NotImplemented,
            replacedEntryIdIn = NotImplemented,
            replacementStatusEqual = NotImplemented,
            replacementStatusIn = NotImplemented,
            partnerSortValueGreaterThanOrEqual = NotImplemented,
            partnerSortValueLessThanOrEqual = NotImplemented,
            rootEntryIdEqual = NotImplemented,
            rootEntryIdIn = NotImplemented,
            parentEntryIdEqual = NotImplemented,
            entitledUsersEditMatchAnd = NotImplemented,
            entitledUsersEditMatchOr = NotImplemented,
            entitledUsersPublishMatchAnd = NotImplemented,
            entitledUsersPublishMatchOr = NotImplemented,
            entitledUsersViewMatchAnd = NotImplemented,
            entitledUsersViewMatchOr = NotImplemented,
            tagsNameMultiLikeOr = NotImplemented,
            tagsAdminTagsMultiLikeOr = NotImplemented,
            tagsAdminTagsNameMultiLikeOr = NotImplemented,
            tagsNameMultiLikeAnd = NotImplemented,
            tagsAdminTagsMultiLikeAnd = NotImplemented,
            tagsAdminTagsNameMultiLikeAnd = NotImplemented,
            displayInSearchEqual = NotImplemented,
            displayInSearchIn = NotImplemented,
            freeText = NotImplemented,
            excludedFreeTextGroups = NotImplemented,
            descriptionLike = NotImplemented,
            isRoot = NotImplemented,
            categoriesFullNameIn = NotImplemented,
            categoryAncestorIdIn = NotImplemented,
            redirectFromEntryId = NotImplemented,
            conversionProfileIdEqual = NotImplemented,
            roomTypeEqual = NotImplemented):
        KalturaRoomEntryBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            partnerIdEqual,
            partnerIdIn,
            userIdEqual,
            userIdIn,
            userIdNotIn,
            creatorIdEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            adminTagsLike,
            adminTagsMultiLikeOr,
            adminTagsMultiLikeAnd,
            categoriesMatchAnd,
            categoriesMatchOr,
            categoriesNotContains,
            categoriesIdsMatchAnd,
            categoriesIdsMatchOr,
            categoriesIdsNotContains,
            categoriesIdsEmpty,
            statusEqual,
            statusNotEqual,
            statusIn,
            statusNotIn,
            moderationStatusEqual,
            moderationStatusNotEqual,
            moderationStatusIn,
            moderationStatusNotIn,
            typeEqual,
            typeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            rankLessThanOrEqual,
            rankGreaterThanOrEqual,
            totalRankLessThanOrEqual,
            totalRankGreaterThanOrEqual,
            groupIdEqual,
            searchTextMatchAnd,
            searchTextMatchOr,
            accessControlIdEqual,
            accessControlIdIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            startDateGreaterThanOrEqualOrNull,
            startDateLessThanOrEqualOrNull,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            endDateGreaterThanOrEqualOrNull,
            endDateLessThanOrEqualOrNull,
            referenceIdEqual,
            referenceIdIn,
            replacingEntryIdEqual,
            replacingEntryIdIn,
            replacedEntryIdEqual,
            replacedEntryIdIn,
            replacementStatusEqual,
            replacementStatusIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            rootEntryIdEqual,
            rootEntryIdIn,
            parentEntryIdEqual,
            entitledUsersEditMatchAnd,
            entitledUsersEditMatchOr,
            entitledUsersPublishMatchAnd,
            entitledUsersPublishMatchOr,
            entitledUsersViewMatchAnd,
            entitledUsersViewMatchOr,
            tagsNameMultiLikeOr,
            tagsAdminTagsMultiLikeOr,
            tagsAdminTagsNameMultiLikeOr,
            tagsNameMultiLikeAnd,
            tagsAdminTagsMultiLikeAnd,
            tagsAdminTagsNameMultiLikeAnd,
            displayInSearchEqual,
            displayInSearchIn,
            freeText,
            excludedFreeTextGroups,
            descriptionLike,
            isRoot,
            categoriesFullNameIn,
            categoryAncestorIdIn,
            redirectFromEntryId,
            conversionProfileIdEqual,
            roomTypeEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRoomEntryBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRoomEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRoomEntryBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaRoomEntryFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaRoomService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entry):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("entry", entry)
        self.client.queueServiceActionCall("room_room", "add", "KalturaRoomEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaRoomEntry')

    def attachRecordedEntry(self, roomEntryId, mediaEntryId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("roomEntryId", roomEntryId)
        kparams.addStringIfDefined("mediaEntryId", mediaEntryId)
        self.client.queueServiceActionCall("room_room", "attachRecordedEntry", "KalturaMediaEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaMediaEntry')

    def delete(self, roomId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("roomId", roomId)
        self.client.queueServiceActionCall("room_room", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, roomId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("roomId", roomId)
        self.client.queueServiceActionCall("room_room", "get", "KalturaRoomEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaRoomEntry')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("room_room", "list", "KalturaRoomEntryListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaRoomEntryListResponse')

    def update(self, roomId, room):
        kparams = KalturaParams()
        kparams.addStringIfDefined("roomId", roomId)
        kparams.addObjectIfDefined("room", room)
        self.client.queueServiceActionCall("room_room", "update", "KalturaRoomEntry", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaRoomEntry')

########## main ##########
class KalturaRoomClientPlugin(KalturaClientPlugin):
    # KalturaRoomClientPlugin
    instance = None

    # @return KalturaRoomClientPlugin
    @staticmethod
    def get():
        if KalturaRoomClientPlugin.instance == None:
            KalturaRoomClientPlugin.instance = KalturaRoomClientPlugin()
        return KalturaRoomClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'room': KalturaRoomService,
        }

    def getEnums(self):
        return {
            'KalturaRoomType': KalturaRoomType,
            'KalturaRoomEntryOrderBy': KalturaRoomEntryOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaRoomEntry': KalturaRoomEntry,
            'KalturaRoomEntryListResponse': KalturaRoomEntryListResponse,
            'KalturaRoomEntryBaseFilter': KalturaRoomEntryBaseFilter,
            'KalturaRoomEntryFilter': KalturaRoomEntryFilter,
        }

    # @return string
    def getName(self):
        return 'room'

