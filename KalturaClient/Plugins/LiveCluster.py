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
########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaLiveClusterMediaServerNode(KalturaMediaServerNode):
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
            deliveryProfileIds=NotImplemented,
            config=NotImplemented,
            applicationName=NotImplemented,
            mediaServerPortConfig=NotImplemented,
            mediaServerPlaybackDomainConfig=NotImplemented):
        KalturaMediaServerNode.__init__(self,
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
            environment,
            deliveryProfileIds,
            config,
            applicationName,
            mediaServerPortConfig,
            mediaServerPlaybackDomainConfig)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMediaServerNode.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveClusterMediaServerNode.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaServerNode.toParams(self)
        kparams.put("objectType", "KalturaLiveClusterMediaServerNode")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaLiveClusterMediaServerNodeBaseFilter(KalturaMediaServerNodeFilter):
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
        KalturaMediaServerNodeFilter.__init__(self,
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
        KalturaMediaServerNodeFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveClusterMediaServerNodeBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaServerNodeFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveClusterMediaServerNodeBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaLiveClusterMediaServerNodeFilter(KalturaLiveClusterMediaServerNodeBaseFilter):
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
        KalturaLiveClusterMediaServerNodeBaseFilter.__init__(self,
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
        KalturaLiveClusterMediaServerNodeBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLiveClusterMediaServerNodeFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLiveClusterMediaServerNodeBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaLiveClusterMediaServerNodeFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaLiveClusterClientPlugin(KalturaClientPlugin):
    # KalturaLiveClusterClientPlugin
    instance = None

    # @return KalturaLiveClusterClientPlugin
    @staticmethod
    def get():
        if KalturaLiveClusterClientPlugin.instance == None:
            KalturaLiveClusterClientPlugin.instance = KalturaLiveClusterClientPlugin()
        return KalturaLiveClusterClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaLiveClusterMediaServerNode': KalturaLiveClusterMediaServerNode,
            'KalturaLiveClusterMediaServerNodeBaseFilter': KalturaLiveClusterMediaServerNodeBaseFilter,
            'KalturaLiveClusterMediaServerNodeFilter': KalturaLiveClusterMediaServerNodeFilter,
        }

    # @return string
    def getName(self):
        return 'liveCluster'

