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
# Copyright (C) 2006-2020  Kaltura Inc.
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
class KalturaConferenceRoomStatus(object):
    CREATED = 1
    READY = 2
    ENDED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaConferenceServerNodeOrderBy(object):
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
class KalturaRoomDetails(KalturaObjectBase):
    def __init__(self,
            serverUrl=NotImplemented,
            entryId=NotImplemented,
            token=NotImplemented,
            expiry=NotImplemented,
            serverName=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.serverUrl = serverUrl

        # @var string
        self.entryId = entryId

        # @var string
        self.token = token

        # @var int
        self.expiry = expiry

        # @var string
        self.serverName = serverName


    PROPERTY_LOADERS = {
        'serverUrl': getXmlNodeText, 
        'entryId': getXmlNodeText, 
        'token': getXmlNodeText, 
        'expiry': getXmlNodeInt, 
        'serverName': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRoomDetails.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRoomDetails")
        kparams.addStringIfDefined("serverUrl", self.serverUrl)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addStringIfDefined("token", self.token)
        kparams.addIntIfDefined("expiry", self.expiry)
        kparams.addStringIfDefined("serverName", self.serverName)
        return kparams

    def getServerUrl(self):
        return self.serverUrl

    def setServerUrl(self, newServerUrl):
        self.serverUrl = newServerUrl

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getToken(self):
        return self.token

    def setToken(self, newToken):
        self.token = newToken

    def getExpiry(self):
        return self.expiry

    def setExpiry(self, newExpiry):
        self.expiry = newExpiry

    def getServerName(self):
        return self.serverName

    def setServerName(self, newServerName):
        self.serverName = newServerName


# @package Kaltura
# @subpackage Client
class KalturaConferenceEntryServerNode(KalturaEntryServerNode):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            serverNodeId=NotImplemented,
            partnerId=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            serverType=NotImplemented,
            confRoomStatus=NotImplemented,
            registered=NotImplemented):
        KalturaEntryServerNode.__init__(self,
            id,
            entryId,
            serverNodeId,
            partnerId,
            createdAt,
            updatedAt,
            status,
            serverType)

        # @var KalturaConferenceRoomStatus
        # @readonly
        self.confRoomStatus = confRoomStatus

        # @var int
        # @readonly
        self.registered = registered


    PROPERTY_LOADERS = {
        'confRoomStatus': (KalturaEnumsFactory.createInt, "KalturaConferenceRoomStatus"), 
        'registered': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaEntryServerNode.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConferenceEntryServerNode.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntryServerNode.toParams(self)
        kparams.put("objectType", "KalturaConferenceEntryServerNode")
        return kparams

    def getConfRoomStatus(self):
        return self.confRoomStatus

    def getRegistered(self):
        return self.registered


# @package Kaltura
# @subpackage Client
class KalturaConferenceServerNode(KalturaServerNode):
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
            environment=NotImplemented,
            serviceBaseUrl=NotImplemented):
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

        # @var string
        self.serviceBaseUrl = serviceBaseUrl


    PROPERTY_LOADERS = {
        'serviceBaseUrl': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaServerNode.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConferenceServerNode.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaServerNode.toParams(self)
        kparams.put("objectType", "KalturaConferenceServerNode")
        kparams.addStringIfDefined("serviceBaseUrl", self.serviceBaseUrl)
        return kparams

    def getServiceBaseUrl(self):
        return self.serviceBaseUrl

    def setServiceBaseUrl(self, newServiceBaseUrl):
        self.serviceBaseUrl = newServiceBaseUrl


# @package Kaltura
# @subpackage Client
class KalturaConferenceEntryServerNodeBaseFilter(KalturaEntryServerNodeFilter):
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
        self.fromXmlImpl(node, KalturaConferenceEntryServerNodeBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntryServerNodeFilter.toParams(self)
        kparams.put("objectType", "KalturaConferenceEntryServerNodeBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaConferenceServerNodeBaseFilter(KalturaServerNodeFilter):
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
        self.fromXmlImpl(node, KalturaConferenceServerNodeBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaServerNodeFilter.toParams(self)
        kparams.put("objectType", "KalturaConferenceServerNodeBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaConferenceEntryServerNodeFilter(KalturaConferenceEntryServerNodeBaseFilter):
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
        KalturaConferenceEntryServerNodeBaseFilter.__init__(self,
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
        KalturaConferenceEntryServerNodeBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConferenceEntryServerNodeFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConferenceEntryServerNodeBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaConferenceEntryServerNodeFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaConferenceServerNodeFilter(KalturaConferenceServerNodeBaseFilter):
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
        KalturaConferenceServerNodeBaseFilter.__init__(self,
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
        KalturaConferenceServerNodeBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConferenceServerNodeFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConferenceServerNodeBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaConferenceServerNodeFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaConferenceClientPlugin(KalturaClientPlugin):
    # KalturaConferenceClientPlugin
    instance = None

    # @return KalturaConferenceClientPlugin
    @staticmethod
    def get():
        if KalturaConferenceClientPlugin.instance == None:
            KalturaConferenceClientPlugin.instance = KalturaConferenceClientPlugin()
        return KalturaConferenceClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaConferenceRoomStatus': KalturaConferenceRoomStatus,
            'KalturaConferenceServerNodeOrderBy': KalturaConferenceServerNodeOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaRoomDetails': KalturaRoomDetails,
            'KalturaConferenceEntryServerNode': KalturaConferenceEntryServerNode,
            'KalturaConferenceServerNode': KalturaConferenceServerNode,
            'KalturaConferenceEntryServerNodeBaseFilter': KalturaConferenceEntryServerNodeBaseFilter,
            'KalturaConferenceServerNodeBaseFilter': KalturaConferenceServerNodeBaseFilter,
            'KalturaConferenceEntryServerNodeFilter': KalturaConferenceEntryServerNodeFilter,
            'KalturaConferenceServerNodeFilter': KalturaConferenceServerNodeFilter,
        }

    # @return string
    def getName(self):
        return 'conference'

