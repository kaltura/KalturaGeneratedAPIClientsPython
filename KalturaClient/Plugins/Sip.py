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
# Copyright (C) 2006-2021  Kaltura Inc.
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
class KalturaSipSourceType(object):
    PICTURE_IN_PICTURE = 1
    TALKING_HEADS = 2
    SCREEN_SHARE = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSipServerNodeOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    HEARTBEAT_TIME_ASC = "+heartbeatTime"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    HEARTBEAT_TIME_DESC = "-heartbeatTime"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaSipEntryServerNode(KalturaEntryServerNode):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            serverNodeId=NotImplemented,
            partnerId=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            serverType=NotImplemented,
            sipRoomId=NotImplemented,
            sipPrimaryAdpId=NotImplemented,
            sipSecondaryAdpId=NotImplemented):
        KalturaEntryServerNode.__init__(self,
            id,
            entryId,
            serverNodeId,
            partnerId,
            createdAt,
            updatedAt,
            status,
            serverType)

        # @var string
        # @readonly
        self.sipRoomId = sipRoomId

        # @var string
        # @readonly
        self.sipPrimaryAdpId = sipPrimaryAdpId

        # @var string
        # @readonly
        self.sipSecondaryAdpId = sipSecondaryAdpId


    PROPERTY_LOADERS = {
        'sipRoomId': getXmlNodeText, 
        'sipPrimaryAdpId': getXmlNodeText, 
        'sipSecondaryAdpId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaEntryServerNode.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSipEntryServerNode.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntryServerNode.toParams(self)
        kparams.put("objectType", "KalturaSipEntryServerNode")
        return kparams

    def getSipRoomId(self):
        return self.sipRoomId

    def getSipPrimaryAdpId(self):
        return self.sipPrimaryAdpId

    def getSipSecondaryAdpId(self):
        return self.sipSecondaryAdpId


# @package Kaltura
# @subpackage Client
class KalturaSipServerNode(KalturaServerNode):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            heartbeatTime=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            hostName=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            tags=NotImplemented,
            dc=NotImplemented,
            parentId=NotImplemented,
            environment=NotImplemented):
        KalturaServerNode.__init__(self,
            id,
            partnerId,
            createdAt,
            updatedAt,
            heartbeatTime,
            name,
            systemName,
            description,
            hostName,
            status,
            type,
            tags,
            dc,
            parentId,
            environment)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaServerNode.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSipServerNode.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaServerNode.toParams(self)
        kparams.put("objectType", "KalturaSipServerNode")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaSipEntryServerNodeBaseFilter(KalturaEntryServerNodeFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            serverNodeIdEqual=NotImplemented,
            serverNodeIdIn=NotImplemented,
            serverNodeIdNotIn=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serverTypeEqual=NotImplemented,
            serverTypeIn=NotImplemented,
            serverTypeNotIn=NotImplemented):
        KalturaEntryServerNodeFilter.__init__(self,
            orderBy,
            advancedSearch,
            entryIdEqual,
            entryIdIn,
            serverNodeIdEqual,
            serverNodeIdIn,
            serverNodeIdNotIn,
            createdAtLessThanOrEqual,
            createdAtGreaterThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serverTypeEqual,
            serverTypeIn,
            serverTypeNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaEntryServerNodeFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSipEntryServerNodeBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntryServerNodeFilter.toParams(self)
        kparams.put("objectType", "KalturaSipEntryServerNodeBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaSipServerNodeBaseFilter(KalturaServerNodeFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            heartbeatTimeGreaterThanOrEqual=NotImplemented,
            heartbeatTimeLessThanOrEqual=NotImplemented,
            nameEqual=NotImplemented,
            nameIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            hostNameLike=NotImplemented,
            hostNameMultiLikeOr=NotImplemented,
            hostNameMultiLikeAnd=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            parentIdLike=NotImplemented,
            parentIdMultiLikeOr=NotImplemented,
            parentIdMultiLikeAnd=NotImplemented,
            environmentEqual=NotImplemented,
            environmentIn=NotImplemented):
        KalturaServerNodeFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            heartbeatTimeGreaterThanOrEqual,
            heartbeatTimeLessThanOrEqual,
            nameEqual,
            nameIn,
            systemNameEqual,
            systemNameIn,
            hostNameLike,
            hostNameMultiLikeOr,
            hostNameMultiLikeAnd,
            statusEqual,
            statusIn,
            typeEqual,
            typeIn,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            dcEqual,
            dcIn,
            parentIdLike,
            parentIdMultiLikeOr,
            parentIdMultiLikeAnd,
            environmentEqual,
            environmentIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaServerNodeFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSipServerNodeBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaServerNodeFilter.toParams(self)
        kparams.put("objectType", "KalturaSipServerNodeBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaSipEntryServerNodeFilter(KalturaSipEntryServerNodeBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            serverNodeIdEqual=NotImplemented,
            serverNodeIdIn=NotImplemented,
            serverNodeIdNotIn=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serverTypeEqual=NotImplemented,
            serverTypeIn=NotImplemented,
            serverTypeNotIn=NotImplemented):
        KalturaSipEntryServerNodeBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            entryIdEqual,
            entryIdIn,
            serverNodeIdEqual,
            serverNodeIdIn,
            serverNodeIdNotIn,
            createdAtLessThanOrEqual,
            createdAtGreaterThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serverTypeEqual,
            serverTypeIn,
            serverTypeNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSipEntryServerNodeBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSipEntryServerNodeFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSipEntryServerNodeBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaSipEntryServerNodeFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaSipServerNodeFilter(KalturaSipServerNodeBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            heartbeatTimeGreaterThanOrEqual=NotImplemented,
            heartbeatTimeLessThanOrEqual=NotImplemented,
            nameEqual=NotImplemented,
            nameIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            hostNameLike=NotImplemented,
            hostNameMultiLikeOr=NotImplemented,
            hostNameMultiLikeAnd=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            dcEqual=NotImplemented,
            dcIn=NotImplemented,
            parentIdLike=NotImplemented,
            parentIdMultiLikeOr=NotImplemented,
            parentIdMultiLikeAnd=NotImplemented,
            environmentEqual=NotImplemented,
            environmentIn=NotImplemented):
        KalturaSipServerNodeBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            heartbeatTimeGreaterThanOrEqual,
            heartbeatTimeLessThanOrEqual,
            nameEqual,
            nameIn,
            systemNameEqual,
            systemNameIn,
            hostNameLike,
            hostNameMultiLikeOr,
            hostNameMultiLikeAnd,
            statusEqual,
            statusIn,
            typeEqual,
            typeIn,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            dcEqual,
            dcIn,
            parentIdLike,
            parentIdMultiLikeOr,
            parentIdMultiLikeAnd,
            environmentEqual,
            environmentIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSipServerNodeBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSipServerNodeFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSipServerNodeBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaSipServerNodeFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaPexipService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def generateSipUrl(self, entryId, regenerate = False, sourceType = 1):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addBoolIfDefined("regenerate", regenerate);
        kparams.addIntIfDefined("sourceType", sourceType);
        self.client.queueServiceActionCall("sip_pexip", "generateSipUrl", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def handleIncomingCall(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("sip_pexip", "handleIncomingCall", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def listRooms(self, offset = 0, pageSize = 500, activeOnly = False):
        kparams = KalturaParams()
        kparams.addIntIfDefined("offset", offset);
        kparams.addIntIfDefined("pageSize", pageSize);
        kparams.addBoolIfDefined("activeOnly", activeOnly);
        self.client.queueServiceActionCall("sip_pexip", "listRooms", "KalturaStringValue", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, 'KalturaStringValue')

########## main ##########
class KalturaSipClientPlugin(KalturaClientPlugin):
    # KalturaSipClientPlugin
    instance = None

    # @return KalturaSipClientPlugin
    @staticmethod
    def get():
        if KalturaSipClientPlugin.instance == None:
            KalturaSipClientPlugin.instance = KalturaSipClientPlugin()
        return KalturaSipClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'pexip': KalturaPexipService,
        }

    def getEnums(self):
        return {
            'KalturaSipSourceType': KalturaSipSourceType,
            'KalturaSipServerNodeOrderBy': KalturaSipServerNodeOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaSipEntryServerNode': KalturaSipEntryServerNode,
            'KalturaSipServerNode': KalturaSipServerNode,
            'KalturaSipEntryServerNodeBaseFilter': KalturaSipEntryServerNodeBaseFilter,
            'KalturaSipServerNodeBaseFilter': KalturaSipServerNodeBaseFilter,
            'KalturaSipEntryServerNodeFilter': KalturaSipEntryServerNodeFilter,
            'KalturaSipServerNodeFilter': KalturaSipServerNodeFilter,
        }

    # @return string
    def getName(self):
        return 'sip'

