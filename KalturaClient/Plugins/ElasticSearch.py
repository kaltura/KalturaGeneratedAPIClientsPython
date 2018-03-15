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
# Copyright (C) 2006-2018  Kaltura Inc.
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
class KalturaESearchItemType(object):
    EXACT_MATCH = 1
    PARTIAL = 2
    STARTS_WITH = 3
    EXISTS = 4
    RANGE = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchOperatorType(object):
    AND_OP = 1
    OR_OP = 2
    NOT_OP = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCaptionFieldName(object):
    CAPTION_CONTENT = "caption_assets.lines.content"
    CAPTION_END_TIME = "caption_assets.lines.end_time"
    CAPTION_START_TIME = "caption_assets.lines.start_time"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryFieldName(object):
    CATEGORY_CONTRIBUTION_POLICY = "contribution_policy"
    CATEGORY_CREATED_AT = "created_at"
    CATEGORY_DEPTH = "depth"
    CATEGORY_DESCRIPTION = "description"
    CATEGORY_DIRECT_ENTRIES_COUNT = "direct_entries_count"
    CATEGORY_DIRECT_SUB_CATEGORIES_COUNT = "direct_sub_categories_count"
    CATEGORY_DISPLAY_IN_SEARCH = "display_in_search"
    CATEGORY_ENTRIES_COUNT = "entries_count"
    CATEGORY_FULL_IDS = "full_ids"
    CATEGORY_FULL_NAME = "full_name"
    CATEGORY_INHERITANCE_TYPE = "inheritance_type"
    CATEGORY_INHERITED_PARENT_ID = "inherited_parent_id"
    CATEGORY_KUSER_ID = "kuser_id"
    CATEGORY_KUSER_IDS = "kuser_ids"
    CATEGORY_MEMBERS_COUNT = "members_count"
    CATEGORY_MODERATION = "moderation"
    CATEGORY_NAME = "name"
    CATEGORY_PARENT_ID = "parent_id"
    CATEGORY_PENDING_ENTRIES_COUNT = "pending_entries_count"
    CATEGORY_PENDING_MEMBERS_COUNT = "pending_members_count"
    CATEGORY_PRIVACY = "privacy"
    CATEGORY_PRIVACY_CONTEXT = "privacy_context"
    CATEGORY_PRIVACY_CONTEXTS = "privacy_contexts"
    CATEGORY_REFERENCE_ID = "reference_id"
    CATEGORY_TAGS = "tags"
    CATEGORY_UPDATED_AT = "updated_at"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryOrderByFieldName(object):
    CATEGORY_CREATED_AT = "created_at"
    CATEGORY_UPDATED_AT = "updated_at"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchCuePointFieldName(object):
    CUE_POINT_ANSWERS = "cue_points.cue_point_answers"
    CUE_POINT_END_TIME = "cue_points.cue_point_end_time"
    CUE_POINT_EXPLANATION = "cue_points.cue_point_explanation"
    CUE_POINT_HINT = "cue_points.cue_point_hint"
    CUE_POINT_ID = "cue_points.cue_point_id"
    CUE_POINT_NAME = "cue_points.cue_point_name"
    CUE_POINT_QUESTION = "cue_points.cue_point_question"
    CUE_POINT_START_TIME = "cue_points.cue_point_start_time"
    CUE_POINT_SUB_TYPE = "cue_points.cue_point_sub_type"
    CUE_POINT_TAGS = "cue_points.cue_point_tags"
    CUE_POINT_TEXT = "cue_points.cue_point_text"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchEntryFieldName(object):
    ENTRY_ID = "_id"
    ENTRY_ACCESS_CONTROL_ID = "access_control_id"
    ENTRY_ADMIN_TAGS = "admin_tags"
    ENTRY_CATEGORIES = "categories"
    ENTRY_CATEGORY_NAME = "categories.name"
    ENTRY_CATEGORY_IDS = "category_ids"
    ENTRY_CONVERSION_PROFILE_ID = "conversion_profile_id"
    ENTRY_CREATED_AT = "created_at"
    ENTRY_CREATOR_ID = "creator_kuser_id"
    ENTRY_CREDIT = "credit"
    ENTRY_DESCRIPTION = "description"
    ENTRY_END_DATE = "end_date"
    ENTRY_ENTITLED_USER_EDIT = "entitled_kusers_edit"
    ENTRY_ENTITLED_USER_PUBLISH = "entitled_kusers_publish"
    ENTRY_TYPE = "entry_type"
    ENTRY_EXTERNAL_SOURCE_TYPE = "external_source_type"
    ENTRY_USER_ID = "kuser_id"
    ENTRY_LENGTH_IN_MSECS = "length_in_msecs"
    ENTRY_MEDIA_TYPE = "media_type"
    ENTRY_MODERATION_STATUS = "moderation_status"
    ENTRY_NAME = "name"
    ENTRY_PARENT_ENTRY_ID = "parent_id"
    ENTRY_PUSH_PUBLISH = "push_publish"
    ENTRY_RECORDED_ENTRY_ID = "recorded_entry_id"
    ENTRY_REDIRECT_ENTRY_ID = "redirect_entry_id"
    ENTRY_REFERENCE_ID = "reference_id"
    ENTRY_SITE_URL = "site_url"
    ENTRY_SOURCE_TYPE = "source_type"
    ENTRY_START_DATE = "start_date"
    ENTRY_TAGS = "tags"
    ENTRY_TEMPLATE_ENTRY_ID = "template_entry_id"
    ENTRY_UPDATED_AT = "updated_at"
    ENTRY_VIEWS = "views"
    ENTRY_VOTES = "votes"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchEntryOrderByFieldName(object):
    ENTRY_CREATED_AT = "created_at"
    ENTRY_END_DATE = "end_date"
    ENTRY_NAME = "name.keyword"
    ENTRY_START_DATE = "start_date"
    ENTRY_UPDATED_AT = "updated_at"
    ENTRY_VIEWS = "views"
    ENTRY_VOTES = "votes"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchSortOrder(object):
    ORDER_BY_ASC = "asc"
    ORDER_BY_DESC = "desc"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchUserFieldName(object):
    USER_CREATED_AT = "created_at"
    USER_EMAIL = "email"
    USER_FIRST_NAME = "first_name"
    USER_GROUP_IDS = "group_ids"
    USER_TYPE = "kuser_type"
    USER_LAST_NAME = "last_name"
    USER_PERMISSION_NAMES = "permission_names"
    USER_ROLE_IDS = "role_ids"
    USER_SCREEN_NAME = "screen_name"
    USER_TAGS = "tags"
    USER_UPDATED_AT = "updated_at"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaESearchUserOrderByFieldName(object):
    USER_CREATED_AT = "created_at"
    USER_UPDATED_AT = "updated_at"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaESearchBaseItem(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchBaseItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchBaseItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchHighlight(KalturaObjectBase):
    def __init__(self,
            fieldName=NotImplemented,
            hits=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.fieldName = fieldName

        # @var array of KalturaString
        self.hits = hits


    PROPERTY_LOADERS = {
        'fieldName': getXmlNodeText, 
        'hits': (KalturaObjectFactory.createArray, 'KalturaString'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchHighlight.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchHighlight")
        kparams.addStringIfDefined("fieldName", self.fieldName)
        kparams.addArrayIfDefined("hits", self.hits)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName

    def getHits(self):
        return self.hits

    def setHits(self, newHits):
        self.hits = newHits


# @package Kaltura
# @subpackage Client
class KalturaESearchItemData(KalturaObjectBase):
    def __init__(self,
            highlight=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaESearchHighlight
        self.highlight = highlight


    PROPERTY_LOADERS = {
        'highlight': (KalturaObjectFactory.createArray, 'KalturaESearchHighlight'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchItemData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchItemData")
        kparams.addArrayIfDefined("highlight", self.highlight)
        return kparams

    def getHighlight(self):
        return self.highlight

    def setHighlight(self, newHighlight):
        self.highlight = newHighlight


# @package Kaltura
# @subpackage Client
class KalturaESearchItemDataResult(KalturaObjectBase):
    def __init__(self,
            totalCount=NotImplemented,
            items=NotImplemented,
            itemsType=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.totalCount = totalCount

        # @var array of KalturaESearchItemData
        self.items = items

        # @var string
        self.itemsType = itemsType


    PROPERTY_LOADERS = {
        'totalCount': getXmlNodeInt, 
        'items': (KalturaObjectFactory.createArray, 'KalturaESearchItemData'), 
        'itemsType': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchItemDataResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchItemDataResult")
        kparams.addIntIfDefined("totalCount", self.totalCount)
        kparams.addArrayIfDefined("items", self.items)
        kparams.addStringIfDefined("itemsType", self.itemsType)
        return kparams

    def getTotalCount(self):
        return self.totalCount

    def setTotalCount(self, newTotalCount):
        self.totalCount = newTotalCount

    def getItems(self):
        return self.items

    def setItems(self, newItems):
        self.items = newItems

    def getItemsType(self):
        return self.itemsType

    def setItemsType(self, newItemsType):
        self.itemsType = newItemsType


# @package Kaltura
# @subpackage Client
class KalturaESearchOrderByItem(KalturaObjectBase):
    def __init__(self,
            sortOrder=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaESearchSortOrder
        self.sortOrder = sortOrder


    PROPERTY_LOADERS = {
        'sortOrder': (KalturaEnumsFactory.createString, "KalturaESearchSortOrder"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchOrderByItem")
        kparams.addStringEnumIfDefined("sortOrder", self.sortOrder)
        return kparams

    def getSortOrder(self):
        return self.sortOrder

    def setSortOrder(self, newSortOrder):
        self.sortOrder = newSortOrder


# @package Kaltura
# @subpackage Client
class KalturaESearchOrderBy(KalturaObjectBase):
    def __init__(self,
            orderItems=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaESearchOrderByItem
        self.orderItems = orderItems


    PROPERTY_LOADERS = {
        'orderItems': (KalturaObjectFactory.createArray, 'KalturaESearchOrderByItem'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchOrderBy.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchOrderBy")
        kparams.addArrayIfDefined("orderItems", self.orderItems)
        return kparams

    def getOrderItems(self):
        return self.orderItems

    def setOrderItems(self, newOrderItems):
        self.orderItems = newOrderItems


# @package Kaltura
# @subpackage Client
class KalturaESearchOperator(KalturaESearchBaseItem):
    def __init__(self,
            operator=NotImplemented,
            searchItems=NotImplemented):
        KalturaESearchBaseItem.__init__(self)

        # @var KalturaESearchOperatorType
        self.operator = operator

        # @var array of KalturaESearchBaseItem
        self.searchItems = searchItems


    PROPERTY_LOADERS = {
        'operator': (KalturaEnumsFactory.createInt, "KalturaESearchOperatorType"), 
        'searchItems': (KalturaObjectFactory.createArray, 'KalturaESearchBaseItem'), 
    }

    def fromXml(self, node):
        KalturaESearchBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchOperator.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchOperator")
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
class KalturaESearchParams(KalturaObjectBase):
    def __init__(self,
            searchOperator=NotImplemented,
            objectStatuses=NotImplemented,
            objectId=NotImplemented,
            orderBy=NotImplemented,
            useHighlight=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaESearchOperator
        self.searchOperator = searchOperator

        # @var string
        self.objectStatuses = objectStatuses

        # @var string
        self.objectId = objectId

        # @var KalturaESearchOrderBy
        self.orderBy = orderBy

        # @var bool
        self.useHighlight = useHighlight


    PROPERTY_LOADERS = {
        'searchOperator': (KalturaObjectFactory.create, 'KalturaESearchOperator'), 
        'objectStatuses': getXmlNodeText, 
        'objectId': getXmlNodeText, 
        'orderBy': (KalturaObjectFactory.create, 'KalturaESearchOrderBy'), 
        'useHighlight': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchParams")
        kparams.addObjectIfDefined("searchOperator", self.searchOperator)
        kparams.addStringIfDefined("objectStatuses", self.objectStatuses)
        kparams.addStringIfDefined("objectId", self.objectId)
        kparams.addObjectIfDefined("orderBy", self.orderBy)
        kparams.addBoolIfDefined("useHighlight", self.useHighlight)
        return kparams

    def getSearchOperator(self):
        return self.searchOperator

    def setSearchOperator(self, newSearchOperator):
        self.searchOperator = newSearchOperator

    def getObjectStatuses(self):
        return self.objectStatuses

    def setObjectStatuses(self, newObjectStatuses):
        self.objectStatuses = newObjectStatuses

    def getObjectId(self):
        return self.objectId

    def setObjectId(self, newObjectId):
        self.objectId = newObjectId

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy

    def getUseHighlight(self):
        return self.useHighlight

    def setUseHighlight(self, newUseHighlight):
        self.useHighlight = newUseHighlight


# @package Kaltura
# @subpackage Client
class KalturaESearchRange(KalturaObjectBase):
    def __init__(self,
            greaterThanOrEqual=NotImplemented,
            lessThanOrEqual=NotImplemented,
            greaterThan=NotImplemented,
            lessThan=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.greaterThanOrEqual = greaterThanOrEqual

        # @var int
        self.lessThanOrEqual = lessThanOrEqual

        # @var int
        self.greaterThan = greaterThan

        # @var int
        self.lessThan = lessThan


    PROPERTY_LOADERS = {
        'greaterThanOrEqual': getXmlNodeInt, 
        'lessThanOrEqual': getXmlNodeInt, 
        'greaterThan': getXmlNodeInt, 
        'lessThan': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchRange.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchRange")
        kparams.addIntIfDefined("greaterThanOrEqual", self.greaterThanOrEqual)
        kparams.addIntIfDefined("lessThanOrEqual", self.lessThanOrEqual)
        kparams.addIntIfDefined("greaterThan", self.greaterThan)
        kparams.addIntIfDefined("lessThan", self.lessThan)
        return kparams

    def getGreaterThanOrEqual(self):
        return self.greaterThanOrEqual

    def setGreaterThanOrEqual(self, newGreaterThanOrEqual):
        self.greaterThanOrEqual = newGreaterThanOrEqual

    def getLessThanOrEqual(self):
        return self.lessThanOrEqual

    def setLessThanOrEqual(self, newLessThanOrEqual):
        self.lessThanOrEqual = newLessThanOrEqual

    def getGreaterThan(self):
        return self.greaterThan

    def setGreaterThan(self, newGreaterThan):
        self.greaterThan = newGreaterThan

    def getLessThan(self):
        return self.lessThan

    def setLessThan(self, newLessThan):
        self.lessThan = newLessThan


# @package Kaltura
# @subpackage Client
class KalturaESearchResult(KalturaObjectBase):
    def __init__(self,
            object=NotImplemented,
            highlight=NotImplemented,
            itemsData=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaObjectBase
        self.object = object

        # @var array of KalturaESearchHighlight
        self.highlight = highlight

        # @var array of KalturaESearchItemDataResult
        self.itemsData = itemsData


    PROPERTY_LOADERS = {
        'object': (KalturaObjectFactory.create, 'KalturaObjectBase'), 
        'highlight': (KalturaObjectFactory.createArray, 'KalturaESearchHighlight'), 
        'itemsData': (KalturaObjectFactory.createArray, 'KalturaESearchItemDataResult'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchResult")
        kparams.addObjectIfDefined("object", self.object)
        kparams.addArrayIfDefined("highlight", self.highlight)
        kparams.addArrayIfDefined("itemsData", self.itemsData)
        return kparams

    def getObject(self):
        return self.object

    def setObject(self, newObject):
        self.object = newObject

    def getHighlight(self):
        return self.highlight

    def setHighlight(self, newHighlight):
        self.highlight = newHighlight

    def getItemsData(self):
        return self.itemsData

    def setItemsData(self, newItemsData):
        self.itemsData = newItemsData


# @package Kaltura
# @subpackage Client
class KalturaESearchResponse(KalturaObjectBase):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.totalCount = totalCount

        # @var array of KalturaESearchResult
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'totalCount': getXmlNodeInt, 
        'objects': (KalturaObjectFactory.createArray, 'KalturaESearchResult'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchResponse")
        return kparams

    def getTotalCount(self):
        return self.totalCount

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaESearchCaptionItemData(KalturaESearchItemData):
    def __init__(self,
            highlight=NotImplemented,
            line=NotImplemented,
            startsAt=NotImplemented,
            endsAt=NotImplemented,
            language=NotImplemented,
            captionAssetId=NotImplemented):
        KalturaESearchItemData.__init__(self,
            highlight)

        # @var string
        self.line = line

        # @var int
        self.startsAt = startsAt

        # @var int
        self.endsAt = endsAt

        # @var string
        self.language = language

        # @var string
        self.captionAssetId = captionAssetId


    PROPERTY_LOADERS = {
        'line': getXmlNodeText, 
        'startsAt': getXmlNodeInt, 
        'endsAt': getXmlNodeInt, 
        'language': getXmlNodeText, 
        'captionAssetId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchItemData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCaptionItemData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItemData.toParams(self)
        kparams.put("objectType", "KalturaESearchCaptionItemData")
        kparams.addStringIfDefined("line", self.line)
        kparams.addIntIfDefined("startsAt", self.startsAt)
        kparams.addIntIfDefined("endsAt", self.endsAt)
        kparams.addStringIfDefined("language", self.language)
        kparams.addStringIfDefined("captionAssetId", self.captionAssetId)
        return kparams

    def getLine(self):
        return self.line

    def setLine(self, newLine):
        self.line = newLine

    def getStartsAt(self):
        return self.startsAt

    def setStartsAt(self, newStartsAt):
        self.startsAt = newStartsAt

    def getEndsAt(self):
        return self.endsAt

    def setEndsAt(self, newEndsAt):
        self.endsAt = newEndsAt

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getCaptionAssetId(self):
        return self.captionAssetId

    def setCaptionAssetId(self, newCaptionAssetId):
        self.captionAssetId = newCaptionAssetId


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryOrderByItem(KalturaESearchOrderByItem):
    def __init__(self,
            sortOrder=NotImplemented,
            sortField=NotImplemented):
        KalturaESearchOrderByItem.__init__(self,
            sortOrder)

        # @var KalturaESearchCategoryOrderByFieldName
        self.sortField = sortField


    PROPERTY_LOADERS = {
        'sortField': (KalturaEnumsFactory.createString, "KalturaESearchCategoryOrderByFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchOrderByItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchOrderByItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryOrderByItem")
        kparams.addStringEnumIfDefined("sortField", self.sortField)
        return kparams

    def getSortField(self):
        return self.sortField

    def setSortField(self, newSortField):
        self.sortField = newSortField


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryResult(KalturaESearchResult):
    def __init__(self,
            object=NotImplemented,
            highlight=NotImplemented,
            itemsData=NotImplemented):
        KalturaESearchResult.__init__(self,
            object,
            highlight,
            itemsData)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchResult.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryResult")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchCuePointItemData(KalturaESearchItemData):
    def __init__(self,
            highlight=NotImplemented,
            cuePointType=NotImplemented,
            id=NotImplemented,
            name=NotImplemented,
            text=NotImplemented,
            tags=NotImplemented,
            startTime=NotImplemented,
            endTime=NotImplemented,
            subType=NotImplemented,
            question=NotImplemented,
            answers=NotImplemented,
            hint=NotImplemented,
            explanation=NotImplemented):
        KalturaESearchItemData.__init__(self,
            highlight)

        # @var string
        self.cuePointType = cuePointType

        # @var string
        self.id = id

        # @var string
        self.name = name

        # @var string
        self.text = text

        # @var string
        self.tags = tags

        # @var string
        self.startTime = startTime

        # @var string
        self.endTime = endTime

        # @var string
        self.subType = subType

        # @var string
        self.question = question

        # @var string
        self.answers = answers

        # @var string
        self.hint = hint

        # @var string
        self.explanation = explanation


    PROPERTY_LOADERS = {
        'cuePointType': getXmlNodeText, 
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'text': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'startTime': getXmlNodeText, 
        'endTime': getXmlNodeText, 
        'subType': getXmlNodeText, 
        'question': getXmlNodeText, 
        'answers': getXmlNodeText, 
        'hint': getXmlNodeText, 
        'explanation': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchItemData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCuePointItemData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItemData.toParams(self)
        kparams.put("objectType", "KalturaESearchCuePointItemData")
        kparams.addStringIfDefined("cuePointType", self.cuePointType)
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("text", self.text)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("startTime", self.startTime)
        kparams.addStringIfDefined("endTime", self.endTime)
        kparams.addStringIfDefined("subType", self.subType)
        kparams.addStringIfDefined("question", self.question)
        kparams.addStringIfDefined("answers", self.answers)
        kparams.addStringIfDefined("hint", self.hint)
        kparams.addStringIfDefined("explanation", self.explanation)
        return kparams

    def getCuePointType(self):
        return self.cuePointType

    def setCuePointType(self, newCuePointType):
        self.cuePointType = newCuePointType

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getText(self):
        return self.text

    def setText(self, newText):
        self.text = newText

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, newStartTime):
        self.startTime = newStartTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, newEndTime):
        self.endTime = newEndTime

    def getSubType(self):
        return self.subType

    def setSubType(self, newSubType):
        self.subType = newSubType

    def getQuestion(self):
        return self.question

    def setQuestion(self, newQuestion):
        self.question = newQuestion

    def getAnswers(self):
        return self.answers

    def setAnswers(self, newAnswers):
        self.answers = newAnswers

    def getHint(self):
        return self.hint

    def setHint(self, newHint):
        self.hint = newHint

    def getExplanation(self):
        return self.explanation

    def setExplanation(self, newExplanation):
        self.explanation = newExplanation


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryOrderByItem(KalturaESearchOrderByItem):
    def __init__(self,
            sortOrder=NotImplemented,
            sortField=NotImplemented):
        KalturaESearchOrderByItem.__init__(self,
            sortOrder)

        # @var KalturaESearchEntryOrderByFieldName
        self.sortField = sortField


    PROPERTY_LOADERS = {
        'sortField': (KalturaEnumsFactory.createString, "KalturaESearchEntryOrderByFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchOrderByItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchOrderByItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryOrderByItem")
        kparams.addStringEnumIfDefined("sortField", self.sortField)
        return kparams

    def getSortField(self):
        return self.sortField

    def setSortField(self, newSortField):
        self.sortField = newSortField


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryResult(KalturaESearchResult):
    def __init__(self,
            object=NotImplemented,
            highlight=NotImplemented,
            itemsData=NotImplemented):
        KalturaESearchResult.__init__(self,
            object,
            highlight,
            itemsData)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchResult.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryResult")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchItem(KalturaESearchBaseItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented):
        KalturaESearchBaseItem.__init__(self)

        # @var string
        self.searchTerm = searchTerm

        # @var KalturaESearchItemType
        self.itemType = itemType

        # @var KalturaESearchRange
        self.range = range


    PROPERTY_LOADERS = {
        'searchTerm': getXmlNodeText, 
        'itemType': (KalturaEnumsFactory.createInt, "KalturaESearchItemType"), 
        'range': (KalturaObjectFactory.create, 'KalturaESearchRange'), 
    }

    def fromXml(self, node):
        KalturaESearchBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchItem")
        kparams.addStringIfDefined("searchTerm", self.searchTerm)
        kparams.addIntEnumIfDefined("itemType", self.itemType)
        kparams.addObjectIfDefined("range", self.range)
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


# @package Kaltura
# @subpackage Client
class KalturaESearchMetadataItemData(KalturaESearchItemData):
    def __init__(self,
            highlight=NotImplemented,
            xpath=NotImplemented,
            metadataProfileId=NotImplemented,
            metadataFieldId=NotImplemented,
            valueText=NotImplemented,
            valueInt=NotImplemented):
        KalturaESearchItemData.__init__(self,
            highlight)

        # @var string
        self.xpath = xpath

        # @var int
        self.metadataProfileId = metadataProfileId

        # @var int
        self.metadataFieldId = metadataFieldId

        # @var string
        self.valueText = valueText

        # @var int
        self.valueInt = valueInt


    PROPERTY_LOADERS = {
        'xpath': getXmlNodeText, 
        'metadataProfileId': getXmlNodeInt, 
        'metadataFieldId': getXmlNodeInt, 
        'valueText': getXmlNodeText, 
        'valueInt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaESearchItemData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchMetadataItemData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItemData.toParams(self)
        kparams.put("objectType", "KalturaESearchMetadataItemData")
        kparams.addStringIfDefined("xpath", self.xpath)
        kparams.addIntIfDefined("metadataProfileId", self.metadataProfileId)
        kparams.addIntIfDefined("metadataFieldId", self.metadataFieldId)
        kparams.addStringIfDefined("valueText", self.valueText)
        kparams.addIntIfDefined("valueInt", self.valueInt)
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

    def getValueText(self):
        return self.valueText

    def setValueText(self, newValueText):
        self.valueText = newValueText

    def getValueInt(self):
        return self.valueInt

    def setValueInt(self, newValueInt):
        self.valueInt = newValueInt


# @package Kaltura
# @subpackage Client
class KalturaESearchQuery(KalturaESearchBaseItem):
    def __init__(self,
            eSearchQuery=NotImplemented):
        KalturaESearchBaseItem.__init__(self)

        # @var string
        self.eSearchQuery = eSearchQuery


    PROPERTY_LOADERS = {
        'eSearchQuery': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaESearchBaseItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchQuery.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchBaseItem.toParams(self)
        kparams.put("objectType", "KalturaESearchQuery")
        kparams.addStringIfDefined("eSearchQuery", self.eSearchQuery)
        return kparams

    def getESearchQuery(self):
        return self.eSearchQuery

    def setESearchQuery(self, newESearchQuery):
        self.eSearchQuery = newESearchQuery


# @package Kaltura
# @subpackage Client
class KalturaESearchUserOrderByItem(KalturaESearchOrderByItem):
    def __init__(self,
            sortOrder=NotImplemented,
            sortField=NotImplemented):
        KalturaESearchOrderByItem.__init__(self,
            sortOrder)

        # @var KalturaESearchUserOrderByFieldName
        self.sortField = sortField


    PROPERTY_LOADERS = {
        'sortField': (KalturaEnumsFactory.createString, "KalturaESearchUserOrderByFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchOrderByItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserOrderByItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchOrderByItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUserOrderByItem")
        kparams.addStringEnumIfDefined("sortField", self.sortField)
        return kparams

    def getSortField(self):
        return self.sortField

    def setSortField(self, newSortField):
        self.sortField = newSortField


# @package Kaltura
# @subpackage Client
class KalturaESearchUserResult(KalturaESearchResult):
    def __init__(self,
            object=NotImplemented,
            highlight=NotImplemented,
            itemsData=NotImplemented):
        KalturaESearchResult.__init__(self,
            object,
            highlight,
            itemsData)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserResult.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchResult.toParams(self)
        kparams.put("objectType", "KalturaESearchUserResult")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchCaptionItem(KalturaESearchItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchItem.__init__(self,
            searchTerm,
            itemType,
            range)

        # @var KalturaESearchCaptionFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchCaptionFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCaptionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCaptionItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchCategoryItem(KalturaESearchItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchItem.__init__(self,
            searchTerm,
            itemType,
            range)

        # @var KalturaESearchCategoryFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchCategoryFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCategoryItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCategoryItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchCuePointItem(KalturaESearchItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            fieldName=NotImplemented,
            cuePointType=NotImplemented):
        KalturaESearchItem.__init__(self,
            searchTerm,
            itemType,
            range)

        # @var KalturaESearchCuePointFieldName
        self.fieldName = fieldName

        # @var KalturaCuePointType
        self.cuePointType = cuePointType


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchCuePointFieldName"), 
        'cuePointType': (KalturaEnumsFactory.createString, "KalturaCuePointType"), 
    }

    def fromXml(self, node):
        KalturaESearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchCuePointItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItem.toParams(self)
        kparams.put("objectType", "KalturaESearchCuePointItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        kparams.addStringEnumIfDefined("cuePointType", self.cuePointType)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName

    def getCuePointType(self):
        return self.cuePointType

    def setCuePointType(self, newCuePointType):
        self.cuePointType = newCuePointType


# @package Kaltura
# @subpackage Client
class KalturaESearchEntryItem(KalturaESearchItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchItem.__init__(self,
            searchTerm,
            itemType,
            range)

        # @var KalturaESearchEntryFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchEntryFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchEntryItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItem.toParams(self)
        kparams.put("objectType", "KalturaESearchEntryItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchMetadataItem(KalturaESearchItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            xpath=NotImplemented,
            metadataProfileId=NotImplemented,
            metadataFieldId=NotImplemented):
        KalturaESearchItem.__init__(self,
            searchTerm,
            itemType,
            range)

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
        KalturaESearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchMetadataItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItem.toParams(self)
        kparams.put("objectType", "KalturaESearchMetadataItem")
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
class KalturaESearchUnifiedItem(KalturaESearchItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented):
        KalturaESearchItem.__init__(self,
            searchTerm,
            itemType,
            range)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaESearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUnifiedItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUnifiedItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaESearchUserItem(KalturaESearchItem):
    def __init__(self,
            searchTerm=NotImplemented,
            itemType=NotImplemented,
            range=NotImplemented,
            fieldName=NotImplemented):
        KalturaESearchItem.__init__(self,
            searchTerm,
            itemType,
            range)

        # @var KalturaESearchUserFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchUserFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchUserItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchItem.toParams(self)
        kparams.put("objectType", "KalturaESearchUserItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaESearchService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getAllowedSearchTypes(self, searchItem):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("searchItem", searchItem)
        self.client.queueServiceActionCall("elasticsearch_esearch", "getAllowedSearchTypes", "KalturaKeyValue", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, 'KalturaKeyValue')

    def searchCategory(self, searchParams, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("searchParams", searchParams)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("elasticsearch_esearch", "searchCategory", "KalturaESearchResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaESearchResponse')

    def searchEntry(self, searchParams, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("searchParams", searchParams)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("elasticsearch_esearch", "searchEntry", "KalturaESearchResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaESearchResponse')

    def searchUser(self, searchParams, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("searchParams", searchParams)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("elasticsearch_esearch", "searchUser", "KalturaESearchResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaESearchResponse')

########## main ##########
class KalturaElasticSearchClientPlugin(KalturaClientPlugin):
    # KalturaElasticSearchClientPlugin
    instance = None

    # @return KalturaElasticSearchClientPlugin
    @staticmethod
    def get():
        if KalturaElasticSearchClientPlugin.instance == None:
            KalturaElasticSearchClientPlugin.instance = KalturaElasticSearchClientPlugin()
        return KalturaElasticSearchClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'eSearch': KalturaESearchService,
        }

    def getEnums(self):
        return {
            'KalturaESearchItemType': KalturaESearchItemType,
            'KalturaESearchOperatorType': KalturaESearchOperatorType,
            'KalturaESearchCaptionFieldName': KalturaESearchCaptionFieldName,
            'KalturaESearchCategoryFieldName': KalturaESearchCategoryFieldName,
            'KalturaESearchCategoryOrderByFieldName': KalturaESearchCategoryOrderByFieldName,
            'KalturaESearchCuePointFieldName': KalturaESearchCuePointFieldName,
            'KalturaESearchEntryFieldName': KalturaESearchEntryFieldName,
            'KalturaESearchEntryOrderByFieldName': KalturaESearchEntryOrderByFieldName,
            'KalturaESearchSortOrder': KalturaESearchSortOrder,
            'KalturaESearchUserFieldName': KalturaESearchUserFieldName,
            'KalturaESearchUserOrderByFieldName': KalturaESearchUserOrderByFieldName,
        }

    def getTypes(self):
        return {
            'KalturaESearchBaseItem': KalturaESearchBaseItem,
            'KalturaESearchHighlight': KalturaESearchHighlight,
            'KalturaESearchItemData': KalturaESearchItemData,
            'KalturaESearchItemDataResult': KalturaESearchItemDataResult,
            'KalturaESearchOrderByItem': KalturaESearchOrderByItem,
            'KalturaESearchOrderBy': KalturaESearchOrderBy,
            'KalturaESearchOperator': KalturaESearchOperator,
            'KalturaESearchParams': KalturaESearchParams,
            'KalturaESearchRange': KalturaESearchRange,
            'KalturaESearchResult': KalturaESearchResult,
            'KalturaESearchResponse': KalturaESearchResponse,
            'KalturaESearchCaptionItemData': KalturaESearchCaptionItemData,
            'KalturaESearchCategoryOrderByItem': KalturaESearchCategoryOrderByItem,
            'KalturaESearchCategoryResult': KalturaESearchCategoryResult,
            'KalturaESearchCuePointItemData': KalturaESearchCuePointItemData,
            'KalturaESearchEntryOrderByItem': KalturaESearchEntryOrderByItem,
            'KalturaESearchEntryResult': KalturaESearchEntryResult,
            'KalturaESearchItem': KalturaESearchItem,
            'KalturaESearchMetadataItemData': KalturaESearchMetadataItemData,
            'KalturaESearchQuery': KalturaESearchQuery,
            'KalturaESearchUserOrderByItem': KalturaESearchUserOrderByItem,
            'KalturaESearchUserResult': KalturaESearchUserResult,
            'KalturaESearchCaptionItem': KalturaESearchCaptionItem,
            'KalturaESearchCategoryItem': KalturaESearchCategoryItem,
            'KalturaESearchCuePointItem': KalturaESearchCuePointItem,
            'KalturaESearchEntryItem': KalturaESearchEntryItem,
            'KalturaESearchMetadataItem': KalturaESearchMetadataItem,
            'KalturaESearchUnifiedItem': KalturaESearchUnifiedItem,
            'KalturaESearchUserItem': KalturaESearchUserItem,
        }

    # @return string
    def getName(self):
        return 'elasticSearch'

