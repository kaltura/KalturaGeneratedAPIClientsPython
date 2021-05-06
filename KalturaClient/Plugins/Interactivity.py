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
from .FileSync import *
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
class KalturaBaseInteractivity(KalturaObjectBase):
    def __init__(self,
            data=NotImplemented,
            version=NotImplemented,
            entryId=NotImplemented,
            updatedAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.data = data

        # @var int
        # @readonly
        self.version = version

        # @var string
        # @readonly
        self.entryId = entryId

        # Interactivity update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = updatedAt


    PROPERTY_LOADERS = {
        'data': getXmlNodeText, 
        'version': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'updatedAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseInteractivity.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseInteractivity")
        kparams.addStringIfDefined("data", self.data)
        return kparams

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getVersion(self):
        return self.version

    def getEntryId(self):
        return self.entryId

    def getUpdatedAt(self):
        return self.updatedAt


# @package Kaltura
# @subpackage Client
class KalturaInteractivityDataFieldsFilter(KalturaObjectBase):
    def __init__(self,
            fields=NotImplemented):
        KalturaObjectBase.__init__(self)

        # A string containing CSV list of fields to include
        # @var string
        self.fields = fields


    PROPERTY_LOADERS = {
        'fields': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInteractivityDataFieldsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaInteractivityDataFieldsFilter")
        kparams.addStringIfDefined("fields", self.fields)
        return kparams

    def getFields(self):
        return self.fields

    def setFields(self, newFields):
        self.fields = newFields


# @package Kaltura
# @subpackage Client
class KalturaInteractivityRootFilter(KalturaInteractivityDataFieldsFilter):
    def __init__(self,
            fields=NotImplemented):
        KalturaInteractivityDataFieldsFilter.__init__(self,
            fields)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaInteractivityDataFieldsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInteractivityRootFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaInteractivityDataFieldsFilter.toParams(self)
        kparams.put("objectType", "KalturaInteractivityRootFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaInteractivityNodeFilter(KalturaInteractivityDataFieldsFilter):
    def __init__(self,
            fields=NotImplemented):
        KalturaInteractivityDataFieldsFilter.__init__(self,
            fields)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaInteractivityDataFieldsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInteractivityNodeFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaInteractivityDataFieldsFilter.toParams(self)
        kparams.put("objectType", "KalturaInteractivityNodeFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaInteractivityInteractionFilter(KalturaInteractivityDataFieldsFilter):
    def __init__(self,
            fields=NotImplemented):
        KalturaInteractivityDataFieldsFilter.__init__(self,
            fields)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaInteractivityDataFieldsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInteractivityInteractionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaInteractivityDataFieldsFilter.toParams(self)
        kparams.put("objectType", "KalturaInteractivityInteractionFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaInteractivityDataFilter(KalturaObjectBase):
    def __init__(self,
            rootFilter=NotImplemented,
            nodeFilter=NotImplemented,
            interactionFilter=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaInteractivityRootFilter
        self.rootFilter = rootFilter

        # @var KalturaInteractivityNodeFilter
        self.nodeFilter = nodeFilter

        # @var KalturaInteractivityInteractionFilter
        self.interactionFilter = interactionFilter


    PROPERTY_LOADERS = {
        'rootFilter': (KalturaObjectFactory.create, 'KalturaInteractivityRootFilter'), 
        'nodeFilter': (KalturaObjectFactory.create, 'KalturaInteractivityNodeFilter'), 
        'interactionFilter': (KalturaObjectFactory.create, 'KalturaInteractivityInteractionFilter'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInteractivityDataFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaInteractivityDataFilter")
        kparams.addObjectIfDefined("rootFilter", self.rootFilter)
        kparams.addObjectIfDefined("nodeFilter", self.nodeFilter)
        kparams.addObjectIfDefined("interactionFilter", self.interactionFilter)
        return kparams

    def getRootFilter(self):
        return self.rootFilter

    def setRootFilter(self, newRootFilter):
        self.rootFilter = newRootFilter

    def getNodeFilter(self):
        return self.nodeFilter

    def setNodeFilter(self, newNodeFilter):
        self.nodeFilter = newNodeFilter

    def getInteractionFilter(self):
        return self.interactionFilter

    def setInteractionFilter(self, newInteractionFilter):
        self.interactionFilter = newInteractionFilter


# @package Kaltura
# @subpackage Client
class KalturaInteractivity(KalturaBaseInteractivity):
    def __init__(self,
            data=NotImplemented,
            version=NotImplemented,
            entryId=NotImplemented,
            updatedAt=NotImplemented):
        KalturaBaseInteractivity.__init__(self,
            data,
            version,
            entryId,
            updatedAt)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseInteractivity.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInteractivity.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseInteractivity.toParams(self)
        kparams.put("objectType", "KalturaInteractivity")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVolatileInteractivity(KalturaBaseInteractivity):
    def __init__(self,
            data=NotImplemented,
            version=NotImplemented,
            entryId=NotImplemented,
            updatedAt=NotImplemented):
        KalturaBaseInteractivity.__init__(self,
            data,
            version,
            entryId,
            updatedAt)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBaseInteractivity.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVolatileInteractivity.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseInteractivity.toParams(self)
        kparams.put("objectType", "KalturaVolatileInteractivity")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaInteractivityService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entryId, kalturaInteractivity):
        """Add a interactivity object"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("kalturaInteractivity", kalturaInteractivity)
        self.client.queueServiceActionCall("interactivity_interactivity", "add", "KalturaInteractivity", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaInteractivity')

    def delete(self, entryId):
        """Delete a interactivity object by entry id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("interactivity_interactivity", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, entryId, dataFilter = NotImplemented):
        """Retrieve a interactivity object by entry id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("dataFilter", dataFilter)
        self.client.queueServiceActionCall("interactivity_interactivity", "get", "KalturaInteractivity", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaInteractivity')

    def update(self, entryId, version, kalturaInteractivity):
        """Update an existing interactivity object"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        kparams.addObjectIfDefined("kalturaInteractivity", kalturaInteractivity)
        self.client.queueServiceActionCall("interactivity_interactivity", "update", "KalturaInteractivity", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaInteractivity')


# @package Kaltura
# @subpackage Client
class KalturaVolatileInteractivityService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entryId, kalturaVolatileInteractivity):
        """add a volatile interactivity object"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("kalturaVolatileInteractivity", kalturaVolatileInteractivity)
        self.client.queueServiceActionCall("interactivity_volatileinteractivity", "add", "KalturaVolatileInteractivity", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVolatileInteractivity')

    def delete(self, entryId):
        """Delete a volatile interactivity object by entry id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("interactivity_volatileinteractivity", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, entryId):
        """Retrieve a volatile interactivity object by entry id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("interactivity_volatileinteractivity", "get", "KalturaVolatileInteractivity", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVolatileInteractivity')

    def update(self, entryId, version, kalturaVolatileInteractivity):
        """Update a volatile interactivity object"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        kparams.addObjectIfDefined("kalturaVolatileInteractivity", kalturaVolatileInteractivity)
        self.client.queueServiceActionCall("interactivity_volatileinteractivity", "update", "KalturaVolatileInteractivity", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVolatileInteractivity')

########## main ##########
class KalturaInteractivityClientPlugin(KalturaClientPlugin):
    # KalturaInteractivityClientPlugin
    instance = None

    # @return KalturaInteractivityClientPlugin
    @staticmethod
    def get():
        if KalturaInteractivityClientPlugin.instance == None:
            KalturaInteractivityClientPlugin.instance = KalturaInteractivityClientPlugin()
        return KalturaInteractivityClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'interactivity': KalturaInteractivityService,
            'volatileInteractivity': KalturaVolatileInteractivityService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaBaseInteractivity': KalturaBaseInteractivity,
            'KalturaInteractivityDataFieldsFilter': KalturaInteractivityDataFieldsFilter,
            'KalturaInteractivityRootFilter': KalturaInteractivityRootFilter,
            'KalturaInteractivityNodeFilter': KalturaInteractivityNodeFilter,
            'KalturaInteractivityInteractionFilter': KalturaInteractivityInteractionFilter,
            'KalturaInteractivityDataFilter': KalturaInteractivityDataFilter,
            'KalturaInteractivity': KalturaInteractivity,
            'KalturaVolatileInteractivity': KalturaVolatileInteractivity,
        }

    # @return string
    def getName(self):
        return 'interactivity'

