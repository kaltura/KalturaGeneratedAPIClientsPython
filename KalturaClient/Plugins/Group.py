# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2019  Kaltura Inc.
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
from .ElasticSearch import *
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
class KalturaESearchGroupFieldName(object):
    CREATED_AT = "created_at"
    EMAIL = "email"
    FIRST_NAME = "first_name"
    GROUP_IDS = "group_ids"
    LAST_NAME = "last_name"
    PERMISSION_NAMES = "permission_names"
    ROLE_IDS = "role_ids"
    SCREEN_NAME = "screen_name"
    TAGS = "tags"
    UPDATED_AT = "updated_at"
    USER_ID = "user_id"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchGroupOrderByFieldName(object):
    CREATED_AT = "created_at"
    MEMBERS_COUNT = "members_count"
    USER_ID = "puser_id"
    SCREEN_NAME = "screen_name"
    UPDATED_AT = "updated_at"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaESearchGroupBaseItem(KalturaESearchBaseItem):
    def __init__(self):
        KalturaESearchBaseItem.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchGroupBaseItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchGroupBaseItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaGroup(KalturaBaseUser):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            screenName=NotImplemented,
            fullName=NotImplemented,
            email=NotImplemented,
            country=NotImplemented,
            state=NotImplemented,
            city=NotImplemented,
            zip=NotImplemented,
            thumbnailUrl=NotImplemented,
            description=NotImplemented,
            tags=NotImplemented,
            adminTags=NotImplemented,
            status=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            partnerData=NotImplemented,
            indexedPartnerDataInt=NotImplemented,
            indexedPartnerDataString=NotImplemented,
            storageSize=NotImplemented,
            language=NotImplemented,
            lastLoginTime=NotImplemented,
            statusUpdatedAt=NotImplemented,
            deletedAt=NotImplemented,
            allowedPartnerIds=NotImplemented,
            allowedPartnerPackages=NotImplemented,
            userMode=NotImplemented,
            membersCount=NotImplemented):
        KalturaBaseUser.__init__(self,
            id,
            partnerId,
            screenName,
            fullName,
            email,
            country,
            state,
            city,
            zip,
            thumbnailUrl,
            description,
            tags,
            adminTags,
            status,
            createdAt,
            updatedAt,
            partnerData,
            indexedPartnerDataInt,
            indexedPartnerDataString,
            storageSize,
            language,
            lastLoginTime,
            statusUpdatedAt,
            deletedAt,
            allowedPartnerIds,
            allowedPartnerPackages,
            userMode)

        # @var int
        # @readonly
        self.membersCount = membersCount


    PROPERTY_LOADERS = {
        'membersCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBaseUser.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGroup.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseUser.toParams(self)
        kparams.put("objectType", "KalturaGroup")
        return kparams

    def getMembersCount(self):
        return self.membersCount


# @package Kaltura
# @subpackage Client
class KalturaESearchGroupOperator(KalturaESearchGroupBaseItem):
    def __init__(self,
            operator=NotImplemented,
            searchItems=NotImplemented):
        KalturaESearchGroupBaseItem.__init__(self)

        # @var KalturaESearchOperatorType
        self.operator = operator

        # @var array of KalturaESearchGroupBaseItem
        self.searchItems = searchItems


    PROPERTY_LOADERS = {
        'operator': (KalturaEnumsFactory.createInt, "KalturaESearchOperatorType"), 
        'searchItems': (KalturaObjectFactory.createArray, 'KalturaESearchGroupBaseItem'), 
    }

    def fromXml(self, node):
        KalturaESearchGroupBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchGroupOperator.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchGroupBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchGroupOperator")
        kparams.addIntEnumIfDefined("operator", self.operator)
        kparams.addArrayIfDefined("searchItems", self.searchItems)
        return kparams

    def getOperator(self):
        return self.operator

    def setOperator(self, newOperator):
        self.operator = newOperator

    def getSearchItems(self):
        return self.searchItems

    def setSearchItems(self, newSearchItems):
        self.searchItems = newSearchItems


# @package Kaltura
# @subpackage Client
class KalturaGroupListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaGroup
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaGroup'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGroupListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaGroupListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaESearchAbstractGroupItem(KalturaESearchGroupBaseItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented):
        KalturaESearchGroupBaseItem.__init__(self)

        # @var string
        self.searchTerm = searchTerm

        # @var KalturaESearchItemType
        self.itemType = itemType

        # @var KalturaESearchRange
        self.range = range

        # @var bool
        self.addHighlight = addHighlight


    PROPERTY_LOADERS = {
        'searchTerm': getXmlNodeText, 
        'itemType': (KalturaEnumsFactory.createInt, "KalturaESearchItemType"), 
        'range': (KalturaObjectFactory.create, 'KalturaESearchRange'), 
        'addHighlight': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaESearchGroupBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchAbstractGroupItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchGroupBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchAbstractGroupItem")
        kparams.addStringIfDefined("searchTerm", self.searchTerm)
        kparams.addIntEnumIfDefined("itemType", self.itemType)
        kparams.addObjectIfDefined("range", self.range)
        kparams.addBoolIfDefined("addHighlight", self.addHighlight)
        return kparams

    def getSearchTerm(self):
        return self.searchTerm

    def setSearchTerm(self, newSearchTerm):
        self.searchTerm = newSearchTerm

    def getItemType(self):
        return self.itemType

    def setItemType(self, newItemType):
        self.itemType = newItemType

    def getRange(self):
        return self.range

    def setRange(self, newRange):
        self.range = newRange

    def getAddHighlight(self):
        return self.addHighlight

    def setAddHighlight(self, newAddHighlight):
        self.addHighlight = newAddHighlight


# @package Kaltura
# @subpackage Client
class KalturaESearchGroupItem(KalturaESearchAbstractGroupItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchAbstractGroupItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var KalturaESearchGroupFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchGroupFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchAbstractGroupItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchGroupItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractGroupItem.toParams(self)
        kparams.put("objectType", "KalturaESearchGroupItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchGroupMetadataItem(KalturaESearchAbstractGroupItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            addHighlight=NotImplemented,
            xpath=NotImplemented,
            metadataProfileId=NotImplemented,
            metadataFieldId=NotImplemented):
        KalturaESearchAbstractGroupItem.__init__(self,
            searchTerm,
            itemType,
            range,
            addHighlight)

        # @var string
        self.xpath = xpath

        # @var int
        self.metadataProfileId = metadataProfileId

        # @var int
        self.metadataFieldId = metadataFieldId


    PROPERTY_LOADERS = {
        'xpath': getXmlNodeText, 
        'metadataProfileId': getXmlNodeInt, 
        'metadataFieldId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaESearchAbstractGroupItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchGroupMetadataItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAbstractGroupItem.toParams(self)
        kparams.put("objectType", "KalturaESearchGroupMetadataItem")
        kparams.addStringIfDefined("xpath", self.xpath)
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addIntIfDefined("metadataFieldId", self.metadataFieldId)
        return kparams

    def getXpath(self):
        return self.xpath

    def setXpath(self, newXpath):
        self.xpath = newXpath

    def getMetadataProfileId(self):
        return self.metadataProfileId

    def setMetadataProfileId(self, newMetadataProfileId):
        self.metadataProfileId = newMetadataProfileId

    def getMetadataFieldId(self):
        return self.metadataFieldId

    def setMetadataFieldId(self, newMetadataFieldId):
        self.metadataFieldId = newMetadataFieldId


# @package Kaltura
# @subpackage Client
class KalturaGroupFilter(KalturaUserFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            partnerIdEqual=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            screenNameLike=NotImplemented,
            screenNameStartsWith=NotImplemented,
            emailLike=NotImplemented,
            emailStartsWith=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            firstNameStartsWith=NotImplemented,
            lastNameStartsWith=NotImplemented,
            isAdminEqual=NotImplemented,
            idOrScreenNameStartsWith=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            loginEnabledEqual=NotImplemented,
            roleIdEqual=NotImplemented,
            roleIdsEqual=NotImplemented,
            roleIdsIn=NotImplemented,
            firstNameOrLastNameStartsWith=NotImplemented,
            permissionNamesMultiLikeOr=NotImplemented,
            permissionNamesMultiLikeAnd=NotImplemented):
        KalturaUserFilter.__init__(self,
            orderBy,
            advancedSearch,
            partnerIdEqual,
            typeEqual,
            typeIn,
            screenNameLike,
            screenNameStartsWith,
            emailLike,
            emailStartsWith,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            firstNameStartsWith,
            lastNameStartsWith,
            isAdminEqual,
            idOrScreenNameStartsWith,
            idEqual,
            idIn,
            loginEnabledEqual,
            roleIdEqual,
            roleIdsEqual,
            roleIdsIn,
            firstNameOrLastNameStartsWith,
            permissionNamesMultiLikeOr,
            permissionNamesMultiLikeAnd)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUserFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGroupFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserFilter.toParams(self)
        kparams.put("objectType", "KalturaGroupFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaGroupService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, group):
        """Adds a new group (user of type group)."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("group", group)
        self.client.queueServiceActionCall("group_group", "add", "KalturaGroup", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaGroup')

    def clone(self, originalGroupId, newGroupId, newGroupName = NotImplemented):
        """clone the group (groupId), and set group id with the neeGroupName."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("originalGroupId", originalGroupId)
        kparams.addStringIfDefined("newGroupId", newGroupId)
        kparams.addStringIfDefined("newGroupName", newGroupName)
        self.client.queueServiceActionCall("group_group", "clone", "KalturaGroup", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaGroup')

    def delete(self, groupId):
        """Delete group by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("groupId", groupId)
        self.client.queueServiceActionCall("group_group", "delete", "KalturaGroup", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaGroup')

    def get(self, groupId):
        """Retrieves a group object for a specified group ID."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("groupId", groupId)
        self.client.queueServiceActionCall("group_group", "get", "KalturaGroup", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaGroup')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Lists group  objects that are associated with an account.
        	 Blocked users are listed unless you use a filter to exclude them.
        	 Deleted users are not listed unless you use a filter to include them."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("group_group", "list", "KalturaGroupListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaGroupListResponse')

    def update(self, groupId, group):
        """Update group by ID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("groupId", groupId)
        kparams.addObjectIfDefined("group", group)
        self.client.queueServiceActionCall("group_group", "update", "KalturaGroup", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaGroup')

########## main ##########
class KalturaGroupClientPlugin(KalturaClientPlugin):
    # KalturaGroupClientPlugin
    instance = None

    # @return KalturaGroupClientPlugin
    @staticmethod
    def get():
        if KalturaGroupClientPlugin.instance == None:
            KalturaGroupClientPlugin.instance = KalturaGroupClientPlugin()
        return KalturaGroupClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'group': KalturaGroupService,
        }

    def getEnums(self):
        return {
            'KalturaESearchGroupFieldName': KalturaESearchGroupFieldName,
            'KalturaESearchGroupOrderByFieldName': KalturaESearchGroupOrderByFieldName,
        }

    def getTypes(self):
        return {
            'KalturaESearchGroupBaseItem': KalturaESearchGroupBaseItem,
            'KalturaGroup': KalturaGroup,
            'KalturaESearchGroupOperator': KalturaESearchGroupOperator,
            'KalturaGroupListResponse': KalturaGroupListResponse,
            'KalturaESearchAbstractGroupItem': KalturaESearchAbstractGroupItem,
            'KalturaESearchGroupItem': KalturaESearchGroupItem,
            'KalturaESearchGroupMetadataItem': KalturaESearchGroupMetadataItem,
            'KalturaGroupFilter': KalturaGroupFilter,
        }

    # @return string
    def getName(self):
        return 'group'

