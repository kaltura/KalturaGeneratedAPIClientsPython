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
class KalturaBeaconIndexType(object):
    LOG = "Log"
    STATE = "State"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBeaconObjectTypes(object):
    SCHEDULE_RESOURCE_BEACON = "1"
    ENTRY_SERVER_NODE_BEACON = "2"
    SERVER_NODE_BEACON = "3"
    ENTRY_BEACON = "4"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBeaconOrderBy(object):
    OBJECT_ID_ASC = "+objectId"
    UPDATED_AT_ASC = "+updatedAt"
    OBJECT_ID_DESC = "-objectId"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaBeacon(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            indexType=NotImplemented,
            updatedAt=NotImplemented,
            relatedObjectType=NotImplemented,
            eventType=NotImplemented,
            objectId=NotImplemented,
            privateData=NotImplemented,
            rawData=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Beacon id
        # @var string
        # @readonly
        self.id = id

        # Beacon indexType
        # @var string
        # @readonly
        self.indexType = indexType

        # Beacon update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # The object which this beacon belongs to
        # @var KalturaBeaconObjectTypes
        self.relatedObjectType = relatedObjectType

        # @var string
        self.eventType = eventType

        # @var string
        self.objectId = objectId

        # @var string
        self.privateData = privateData

        # @var string
        self.rawData = rawData


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'indexType': getXmlNodeText, 
        'updatedAt': getXmlNodeInt, 
        'relatedObjectType': (KalturaEnumsFactory.createString, "KalturaBeaconObjectTypes"), 
        'eventType': getXmlNodeText, 
        'objectId': getXmlNodeText, 
        'privateData': getXmlNodeText, 
        'rawData': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBeacon.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBeacon")
        kparams.addStringEnumIfDefined("relatedObjectType", self.relatedObjectType)
        kparams.addStringIfDefined("eventType", self.eventType)
        kparams.addStringIfDefined("objectId", self.objectId)
        kparams.addStringIfDefined("privateData", self.privateData)
        kparams.addStringIfDefined("rawData", self.rawData)
        return kparams

    def getId(self):
        return self.id

    def getIndexType(self):
        return self.indexType

    def getUpdatedAt(self):
        return self.updatedAt

    def getRelatedObjectType(self):
        return self.relatedObjectType

    def setRelatedObjectType(self, newRelatedObjectType):
        self.relatedObjectType = newRelatedObjectType

    def getEventType(self):
        return self.eventType

    def setEventType(self, newEventType):
        self.eventType = newEventType

    def getObjectId(self):
        return self.objectId

    def setObjectId(self, newObjectId):
        self.objectId = newObjectId

    def getPrivateData(self):
        return self.privateData

    def setPrivateData(self, newPrivateData):
        self.privateData = newPrivateData

    def getRawData(self):
        return self.rawData

    def setRawData(self, newRawData):
        self.rawData = newRawData


# @package Kaltura
# @subpackage Client
class KalturaBeaconBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            relatedObjectTypeIn=NotImplemented,
            eventTypeIn=NotImplemented,
            objectIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var string
        self.relatedObjectTypeIn = relatedObjectTypeIn

        # @var string
        self.eventTypeIn = eventTypeIn

        # @var string
        self.objectIdIn = objectIdIn


    PROPERTY_LOADERS = {
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'relatedObjectTypeIn': getXmlNodeText, 
        'eventTypeIn': getXmlNodeText, 
        'objectIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBeaconBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBeaconBaseFilter")
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addStringIfDefined("relatedObjectTypeIn", self.relatedObjectTypeIn)
        kparams.addStringIfDefined("eventTypeIn", self.eventTypeIn)
        kparams.addStringIfDefined("objectIdIn", self.objectIdIn)
        return kparams

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getRelatedObjectTypeIn(self):
        return self.relatedObjectTypeIn

    def setRelatedObjectTypeIn(self, newRelatedObjectTypeIn):
        self.relatedObjectTypeIn = newRelatedObjectTypeIn

    def getEventTypeIn(self):
        return self.eventTypeIn

    def setEventTypeIn(self, newEventTypeIn):
        self.eventTypeIn = newEventTypeIn

    def getObjectIdIn(self):
        return self.objectIdIn

    def setObjectIdIn(self, newObjectIdIn):
        self.objectIdIn = newObjectIdIn


# @package Kaltura
# @subpackage Client
class KalturaBeaconEnhanceFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            externalElasticQueryObject=NotImplemented,
            indexTypeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.externalElasticQueryObject = externalElasticQueryObject

        # @var KalturaBeaconIndexType
        self.indexTypeEqual = indexTypeEqual


    PROPERTY_LOADERS = {
        'externalElasticQueryObject': getXmlNodeText, 
        'indexTypeEqual': (KalturaEnumsFactory.createString, "KalturaBeaconIndexType"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBeaconEnhanceFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBeaconEnhanceFilter")
        kparams.addStringIfDefined("externalElasticQueryObject", self.externalElasticQueryObject)
        kparams.addStringEnumIfDefined("indexTypeEqual", self.indexTypeEqual)
        return kparams

    def getExternalElasticQueryObject(self):
        return self.externalElasticQueryObject

    def setExternalElasticQueryObject(self, newExternalElasticQueryObject):
        self.externalElasticQueryObject = newExternalElasticQueryObject

    def getIndexTypeEqual(self):
        return self.indexTypeEqual

    def setIndexTypeEqual(self, newIndexTypeEqual):
        self.indexTypeEqual = newIndexTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaBeaconListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaBeacon
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaBeacon'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBeaconListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaBeaconListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaBeaconFilter(KalturaBeaconBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            relatedObjectTypeIn=NotImplemented,
            eventTypeIn=NotImplemented,
            objectIdIn=NotImplemented,
            indexTypeEqual=NotImplemented):
        KalturaBeaconBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            relatedObjectTypeIn,
            eventTypeIn,
            objectIdIn)

        # @var KalturaBeaconIndexType
        self.indexTypeEqual = indexTypeEqual


    PROPERTY_LOADERS = {
        'indexTypeEqual': (KalturaEnumsFactory.createString, "KalturaBeaconIndexType"), 
    }

    def fromXml(self, node):
        KalturaBeaconBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBeaconFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBeaconBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaBeaconFilter")
        kparams.addStringEnumIfDefined("indexTypeEqual", self.indexTypeEqual)
        return kparams

    def getIndexTypeEqual(self):
        return self.indexTypeEqual

    def setIndexTypeEqual(self, newIndexTypeEqual):
        self.indexTypeEqual = newIndexTypeEqual


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaBeaconService(KalturaServiceBase):
    """Sending beacons on objects"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, beacon, shouldLog = 0):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("beacon", beacon)
        kparams.addIntIfDefined("shouldLog", shouldLog);
        self.client.queueServiceActionCall("beacon_beacon", "add", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def enhanceSearch(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("beacon_beacon", "enhanceSearch", "KalturaBeaconListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaBeaconListResponse')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("beacon_beacon", "list", "KalturaBeaconListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaBeaconListResponse')

########## main ##########
class KalturaBeaconClientPlugin(KalturaClientPlugin):
    # KalturaBeaconClientPlugin
    instance = None

    # @return KalturaBeaconClientPlugin
    @staticmethod
    def get():
        if KalturaBeaconClientPlugin.instance == None:
            KalturaBeaconClientPlugin.instance = KalturaBeaconClientPlugin()
        return KalturaBeaconClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'beacon': KalturaBeaconService,
        }

    def getEnums(self):
        return {
            'KalturaBeaconIndexType': KalturaBeaconIndexType,
            'KalturaBeaconObjectTypes': KalturaBeaconObjectTypes,
            'KalturaBeaconOrderBy': KalturaBeaconOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaBeacon': KalturaBeacon,
            'KalturaBeaconBaseFilter': KalturaBeaconBaseFilter,
            'KalturaBeaconEnhanceFilter': KalturaBeaconEnhanceFilter,
            'KalturaBeaconListResponse': KalturaBeaconListResponse,
            'KalturaBeaconFilter': KalturaBeaconFilter,
        }

    # @return string
    def getName(self):
        return 'beacon'

