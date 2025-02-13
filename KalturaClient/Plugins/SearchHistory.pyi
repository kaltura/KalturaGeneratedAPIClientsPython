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
from typing import List, IO, Any
from .Core import *
from .ElasticSearch import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaESearchHistoryAggregateFieldName(object):
    SEARCH_TERM = "search_term"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaESearchHistory(KalturaObjectBase):
    searchTerm: str
    searchedObject: str
    timestamp: int
    def __init__(self,
            searchTerm: str = NotImplemented,
            searchedObject: str = NotImplemented,
            timestamp: int = NotImplemented): ...

    def getSearchTerm(self) -> str: ...
    def getSearchedObject(self) -> str: ...
    def getTimestamp(self) -> int: ...

class KalturaESearchHistoryAggregationItem(KalturaESearchAggregationItem):
    fieldName: KalturaESearchHistoryAggregateFieldName
    def __init__(self,
            size: int = NotImplemented,
            fieldName: KalturaESearchHistoryAggregateFieldName = NotImplemented): ...

    def getFieldName(self) -> KalturaESearchHistoryAggregateFieldName: ...
    def setFieldName(self, newFieldName: KalturaESearchHistoryAggregateFieldName) -> None: ...

class KalturaESearchHistoryFilter(KalturaESearchBaseFilter):
    searchTermStartsWith: str
    searchedObjectIn: str
    timestampRange: KalturaESearchRange
    aggregation: KalturaESearchHistoryAggregationItem
    def __init__(self,
            searchTermStartsWith: str = NotImplemented,
            searchedObjectIn: str = NotImplemented,
            timestampRange: KalturaESearchRange = NotImplemented,
            aggregation: KalturaESearchHistoryAggregationItem = NotImplemented): ...

    def getSearchTermStartsWith(self) -> str: ...
    def setSearchTermStartsWith(self, newSearchTermStartsWith: str) -> None: ...
    def getSearchedObjectIn(self) -> str: ...
    def setSearchedObjectIn(self, newSearchedObjectIn: str) -> None: ...
    def getTimestampRange(self) -> KalturaESearchRange: ...
    def setTimestampRange(self, newTimestampRange: KalturaESearchRange) -> None: ...
    def getAggregation(self) -> KalturaESearchHistoryAggregationItem: ...
    def setAggregation(self, newAggregation: KalturaESearchHistoryAggregationItem) -> None: ...

class KalturaESearchHistoryListResponse(KalturaListResponse):
    objects: List[KalturaESearchHistory]
    aggregations: List[KalturaESearchAggregationResponseItem]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaESearchHistory] = NotImplemented,
            aggregations: List[KalturaESearchAggregationResponseItem] = NotImplemented): ...

    def getObjects(self) -> List[KalturaESearchHistory]: ...
    def getAggregations(self) -> List[KalturaESearchAggregationResponseItem]: ...

class KalturaSearchHistoryCsvJobData(KalturaExportCsvJobData):
    filter: KalturaESearchHistoryFilter
    def __init__(self,
            userName: str = NotImplemented,
            userMail: str = NotImplemented,
            outputPath: str = NotImplemented,
            sharedOutputPath: str = NotImplemented,
            filter: KalturaESearchHistoryFilter = NotImplemented): ...

    def getFilter(self) -> KalturaESearchHistoryFilter: ...
    def setFilter(self, newFilter: KalturaESearchHistoryFilter) -> None: ...

class KalturaSearchHistoryService(KalturaServiceBase):
    def delete(self, searchTerm: str) -> None: ...
    def exportToCsv(self, filter: KalturaESearchHistoryFilter) -> str: ...
    def list(self, filter: KalturaESearchHistoryFilter = NotImplemented) -> KalturaESearchHistoryListResponse: ...

class KalturaSearchHistoryClientPluginServicesProxy:
    searchHistory: KalturaSearchHistoryService