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
########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaBumper(KalturaObjectBase):
    def __init__(self,
            entryId = NotImplemented,
            url = NotImplemented,
            sources = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var str
        self.entryId = entryId

        # @var str
        self.url = url

        # @var List[KalturaPlaybackSource]
        # @readonly
        self.sources = sources


    PROPERTY_LOADERS = {
        'entryId': getXmlNodeText, 
        'url': getXmlNodeText, 
        'sources': (KalturaObjectFactory.createArray, 'KalturaPlaybackSource'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBumper.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBumper")
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addStringIfDefined("url", self.url)
        return kparams

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getSources(self):
        return self.sources


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaBumperService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entryId, bumper):
        """Adds a bumper to an entry"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("bumper", bumper)
        self.client.queueServiceActionCall("bumper_bumper", "add", "KalturaBumper", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaBumper')

    def delete(self, entryId):
        """Delete bumper by EntryId"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("bumper_bumper", "delete", "KalturaBumper", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaBumper')

    def get(self, entryId):
        """Allows to get the bumper"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("bumper_bumper", "get", "KalturaBumper", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaBumper')

    def update(self, entryId, bumper):
        """Allows to update a bumper"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("bumper", bumper)
        self.client.queueServiceActionCall("bumper_bumper", "update", "KalturaBumper", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaBumper')

########## main ##########
class KalturaBumperClientPlugin(KalturaClientPlugin):
    # KalturaBumperClientPlugin
    instance = None

    # @return KalturaBumperClientPlugin
    @staticmethod
    def get():
        if KalturaBumperClientPlugin.instance == None:
            KalturaBumperClientPlugin.instance = KalturaBumperClientPlugin()
        return KalturaBumperClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'bumper': KalturaBumperService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaBumper': KalturaBumper,
        }

    # @return string
    def getName(self):
        return 'bumper'

