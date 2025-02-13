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
# @package Kaltura
# @subpackage Client
class KalturaESearchHistoryAggregateFieldName(object):
    SEARCH_TERM = "search_term"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaESearchHistory(KalturaObjectBase):
    def __init__(self,
            searchTerm = NotImplemented,
            searchedObject = NotImplemented,
            timestamp = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var str
        # @readonly
        self.searchTerm = searchTerm

        # @var str
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
class KalturaESearchHistoryAggregationItem(KalturaESearchAggregationItem):
    def __init__(self,
            size = NotImplemented,
            fieldName = NotImplemented):
        KalturaESearchAggregationItem.__init__(self,
            size)

        # @var KalturaESearchHistoryAggregateFieldName
        self.fieldName = fieldName


    PROPERTY_LOADERS = {
        'fieldName': (KalturaEnumsFactory.createString, "KalturaESearchHistoryAggregateFieldName"), 
    }

    def fromXml(self, node):
        KalturaESearchAggregationItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchHistoryAggregationItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchAggregationItem.toParams(self)
        kparams.put("objectType", "KalturaESearchHistoryAggregationItem")
        kparams.addStringEnumIfDefined("fieldName", self.fieldName)
        return kparams

    def getFieldName(self):
        return self.fieldName

    def setFieldName(self, newFieldName):
        self.fieldName = newFieldName


# @package Kaltura
# @subpackage Client
class KalturaESearchHistoryFilter(KalturaESearchBaseFilter):
    def __init__(self,
            searchTermStartsWith = NotImplemented,
            searchedObjectIn = NotImplemented,
            timestampRange = NotImplemented,
            aggregation = NotImplemented):
        KalturaESearchBaseFilter.__init__(self)

        # @var str
        self.searchTermStartsWith = searchTermStartsWith

        # @var str
        self.searchedObjectIn = searchedObjectIn

        # @var KalturaESearchRange
        self.timestampRange = timestampRange

        # @var KalturaESearchHistoryAggregationItem
        self.aggregation = aggregation


    PROPERTY_LOADERS = {
        'searchTermStartsWith': getXmlNodeText, 
        'searchedObjectIn': getXmlNodeText, 
        'timestampRange': (KalturaObjectFactory.create, 'KalturaESearchRange'), 
        'aggregation': (KalturaObjectFactory.create, 'KalturaESearchHistoryAggregationItem'), 
    }

    def fromXml(self, node):
        KalturaESearchBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaESearchHistoryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaESearchBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaESearchHistoryFilter")
        kparams.addStringIfDefined("searchTermStartsWith", self.searchTermStartsWith)
        kparams.addStringIfDefined("searchedObjectIn", self.searchedObjectIn)
        kparams.addObjectIfDefined("timestampRange", self.timestampRange)
        kparams.addObjectIfDefined("aggregation", self.aggregation)
        return kparams

    def getSearchTermStartsWith(self):
        return self.searchTermStartsWith

    def setSearchTermStartsWith(self, newSearchTermStartsWith):
        self.searchTermStartsWith = newSearchTermStartsWith

    def getSearchedObjectIn(self):
        return self.searchedObjectIn

    def setSearchedObjectIn(self, newSearchedObjectIn):
        self.searchedObjectIn = newSearchedObjectIn

    def getTimestampRange(self):
        return self.timestampRange

    def setTimestampRange(self, newTimestampRange):
        self.timestampRange = newTimestampRange

    def getAggregation(self):
        return self.aggregation

    def setAggregation(self, newAggregation):
        self.aggregation = newAggregation


# @package Kaltura
# @subpackage Client
class KalturaESearchHistoryListResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented,
            aggregations = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaESearchHistory]
        # @readonly
        self.objects = objects

        # @var List[KalturaESearchAggregationResponseItem]
        # @readonly
        self.aggregations = aggregations


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaESearchHistory'), 
        'aggregations': (KalturaObjectFactory.createArray, 'KalturaESearchAggregationResponseItem'), 
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

    def getAggregations(self):
        return self.aggregations


# @package Kaltura
# @subpackage Client
class KalturaSearchHistoryCsvJobData(KalturaExportCsvJobData):
    def __init__(self,
            userName = NotImplemented,
            userMail = NotImplemented,
            outputPath = NotImplemented,
            sharedOutputPath = NotImplemented,
            filter = NotImplemented):
        KalturaExportCsvJobData.__init__(self,
            userName,
            userMail,
            outputPath,
            sharedOutputPath)

        # @var KalturaESearchHistoryFilter
        self.filter = filter


    PROPERTY_LOADERS = {
        'filter': (KalturaObjectFactory.create, 'KalturaESearchHistoryFilter'), 
    }

    def fromXml(self, node):
        KalturaExportCsvJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchHistoryCsvJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaExportCsvJobData.toParams(self)
        kparams.put("objectType", "KalturaSearchHistoryCsvJobData")
        kparams.addObjectIfDefined("filter", self.filter)
        return kparams

    def getFilter(self):
        return self.filter

    def setFilter(self, newFilter):
        self.filter = newFilter


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaSearchHistoryService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def delete(self, searchTerm):
        kparams = KalturaParams()
        kparams.addStringIfDefined("searchTerm", searchTerm)
        self.client.queueServiceActionCall("searchhistory_searchhistory", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def exportToCsv(self, filter):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("searchhistory_searchhistory", "exportToCsv", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def list(self, filter = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("searchhistory_searchhistory", "list", "KalturaESearchHistoryListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaESearchHistoryListResponse')

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
            'searchHistory': KalturaSearchHistoryService,
        }

    def getEnums(self):
        return {
            'KalturaESearchHistoryAggregateFieldName': KalturaESearchHistoryAggregateFieldName,
        }

    def getTypes(self):
        return {
            'KalturaESearchHistory': KalturaESearchHistory,
            'KalturaESearchHistoryAggregationItem': KalturaESearchHistoryAggregationItem,
            'KalturaESearchHistoryFilter': KalturaESearchHistoryFilter,
            'KalturaESearchHistoryListResponse': KalturaESearchHistoryListResponse,
            'KalturaSearchHistoryCsvJobData': KalturaSearchHistoryCsvJobData,
        }

    # @return string
    def getName(self):
        return 'searchHistory'

