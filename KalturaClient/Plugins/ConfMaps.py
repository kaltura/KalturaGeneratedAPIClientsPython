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
class KalturaConfMapsStatus(object):
    STATUS_DISABLED = 0
    STATUS_ENABLED = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaConfMaps(KalturaObjectBase):
    def __init__(self,
            name=NotImplemented,
            content=NotImplemented,
            isEditable=NotImplemented,
            lastUpdate=NotImplemented,
            relatedHost=NotImplemented,
            version=NotImplemented,
            sourceLocation=NotImplemented,
            remarks=NotImplemented,
            status=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Name of the map
        # @var string
        # @insertonly
        self.name = name

        # Ini file content
        # @var string
        self.content = content

        # IsEditable - true / false
        # @var bool
        # @readonly
        self.isEditable = isEditable

        # Time of the last update
        # @var int
        # @readonly
        self.lastUpdate = lastUpdate

        # Regex that represent the host/s that this map affect
        # @var string
        self.relatedHost = relatedHost

        # @var int
        # @readonly
        self.version = version

        # @var KalturaConfMapsSourceLocation
        # @insertonly
        self.sourceLocation = sourceLocation

        # @var string
        # @insertonly
        self.remarks = remarks

        # map status
        # @var KalturaConfMapsStatus
        self.status = status


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'content': getXmlNodeText, 
        'isEditable': getXmlNodeBool, 
        'lastUpdate': getXmlNodeInt, 
        'relatedHost': getXmlNodeText, 
        'version': getXmlNodeInt, 
        'sourceLocation': (KalturaEnumsFactory.createString, "KalturaConfMapsSourceLocation"), 
        'remarks': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaConfMapsStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfMaps.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConfMaps")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("content", self.content)
        kparams.addStringIfDefined("relatedHost", self.relatedHost)
        kparams.addStringEnumIfDefined("sourceLocation", self.sourceLocation)
        kparams.addStringIfDefined("remarks", self.remarks)
        kparams.addIntEnumIfDefined("status", self.status)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getContent(self):
        return self.content

    def setContent(self, newContent):
        self.content = newContent

    def getIsEditable(self):
        return self.isEditable

    def getLastUpdate(self):
        return self.lastUpdate

    def getRelatedHost(self):
        return self.relatedHost

    def setRelatedHost(self, newRelatedHost):
        self.relatedHost = newRelatedHost

    def getVersion(self):
        return self.version

    def getSourceLocation(self):
        return self.sourceLocation

    def setSourceLocation(self, newSourceLocation):
        self.sourceLocation = newSourceLocation

    def getRemarks(self):
        return self.remarks

    def setRemarks(self, newRemarks):
        self.remarks = newRemarks

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus


# @package Kaltura
# @subpackage Client
class KalturaConfMapsListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaConfMaps
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaConfMaps'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfMapsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaConfMapsListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaConfMapsBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            nameEqual=NotImplemented,
            relatedHostEqual=NotImplemented,
            versionEqual=NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.nameEqual = nameEqual

        # @var string
        self.relatedHostEqual = relatedHostEqual

        # @var int
        self.versionEqual = versionEqual


    PROPERTY_LOADERS = {
        'nameEqual': getXmlNodeText, 
        'relatedHostEqual': getXmlNodeText, 
        'versionEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaRelatedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfMapsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedFilter.toParams(self)
        kparams.put("objectType", "KalturaConfMapsBaseFilter")
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addStringIfDefined("relatedHostEqual", self.relatedHostEqual)
        kparams.addIntIfDefined("versionEqual", self.versionEqual)
        return kparams

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getRelatedHostEqual(self):
        return self.relatedHostEqual

    def setRelatedHostEqual(self, newRelatedHostEqual):
        self.relatedHostEqual = newRelatedHostEqual

    def getVersionEqual(self):
        return self.versionEqual

    def setVersionEqual(self, newVersionEqual):
        self.versionEqual = newVersionEqual


# @package Kaltura
# @subpackage Client
class KalturaConfMapsFilter(KalturaConfMapsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            nameEqual=NotImplemented,
            relatedHostEqual=NotImplemented,
            versionEqual=NotImplemented):
        KalturaConfMapsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            nameEqual,
            relatedHostEqual,
            versionEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaConfMapsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfMapsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaConfMapsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaConfMapsFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaConfMapsClientPlugin(KalturaClientPlugin):
    # KalturaConfMapsClientPlugin
    instance = None

    # @return KalturaConfMapsClientPlugin
    @staticmethod
    def get():
        if KalturaConfMapsClientPlugin.instance == None:
            KalturaConfMapsClientPlugin.instance = KalturaConfMapsClientPlugin()
        return KalturaConfMapsClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaConfMapsStatus': KalturaConfMapsStatus,
        }

    def getTypes(self):
        return {
            'KalturaConfMaps': KalturaConfMaps,
            'KalturaConfMapsListResponse': KalturaConfMapsListResponse,
            'KalturaConfMapsBaseFilter': KalturaConfMapsBaseFilter,
            'KalturaConfMapsFilter': KalturaConfMapsFilter,
        }

    # @return string
    def getName(self):
        return 'confMaps'

