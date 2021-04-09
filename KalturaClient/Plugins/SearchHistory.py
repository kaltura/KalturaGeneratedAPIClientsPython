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
class KalturaESearchHistory(KalturaObjectBase):
    def __init__(self,
            searchTerm=NotImplemented,
            searchedObject=NotImplemented,
            timestamp=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.searchTerm = searchTerm

        # @var string
        # @readonly
        self.searchedObject = searchedObject

        # @var int
        # @readonly
        self.timestamp = timestamp


    PROPERTY_LOADERS = {
        'searchTerm': getXmlNodeText, 
        'searchedObject': getXmlNodeText, 
        'timestamp': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchHistory.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaESearchHistory")
        return kparams

    def getSearchTerm(self):
        return self.searchTerm

    def getSearchedObject(self):
        return self.searchedObject

    def getTimestamp(self):
        return self.timestamp


# @package Kaltura
# @subpackage Client
class KalturaESearchHistoryListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaESearchHistory
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaESearchHistory'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchHistoryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaESearchHistoryListResponse")
        return kparams

    def getObjects(self):
        return self.objects


########## services ##########
########## main ##########
class KalturaSearchHistoryClientPlugin(KalturaClientPlugin):
    # KalturaSearchHistoryClientPlugin
    instance = None

    # @return KalturaSearchHistoryClientPlugin
    @staticmethod
    def get():
        if KalturaSearchHistoryClientPlugin.instance == None:
            KalturaSearchHistoryClientPlugin.instance = KalturaSearchHistoryClientPlugin()
        return KalturaSearchHistoryClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaESearchHistory': KalturaESearchHistory,
            'KalturaESearchHistoryListResponse': KalturaESearchHistoryListResponse,
        }

    # @return string
    def getName(self):
        return 'searchHistory'

