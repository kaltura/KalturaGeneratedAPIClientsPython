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

class KalturaBeaconIndexType(object):
    LOG = "Log"
    STATE = "State"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBeaconObjectTypes(object):
    SCHEDULE_RESOURCE_BEACON = "1"
    ENTRY_SERVER_NODE_BEACON = "2"
    SERVER_NODE_BEACON = "3"
    ENTRY_BEACON = "4"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBeaconOrderBy(object):
    OBJECT_ID_ASC = "+objectId"
    UPDATED_AT_ASC = "+updatedAt"
    OBJECT_ID_DESC = "-objectId"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBeaconScheduledResourceFieldName(object):
    EVENT_TYPE = "event_type"
    IS_LOG = "is_log"
    OBJECT_ID = "object_id"
    RECORDING = "recording"
    RESOURCE_NAME = "resource_name"
    STATUS = "status"
    UPDATED_AT = "updated_at"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBeaconScheduledResourceOrderByFieldName(object):
    STATUS = "app_status"
    RECORDING = "recording_phase"
    RESOURCE_NAME = "resource_Name"
    UPDATED_AT = "updated_at"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBeacon(KalturaObjectBase):
    id: str
    indexType: str
    updatedAt: int
    relatedObjectType: KalturaBeaconObjectTypes
    eventType: str
    objectId: str
    privateData: str
    rawData: str
    def __init__(self,
            id: str = NotImplemented,
            indexType: str = NotImplemented,
            updatedAt: int = NotImplemented,
            relatedObjectType: KalturaBeaconObjectTypes = NotImplemented,
            eventType: str = NotImplemented,
            objectId: str = NotImplemented,
            privateData: str = NotImplemented,
            rawData: str = NotImplemented): ...

    def getId(self) -> str: ...
    def getIndexType(self) -> str: ...
    def getUpdatedAt(self) -> int: ...
    def getRelatedObjectType(self) -> KalturaBeaconObjectTypes: ...
    def setRelatedObjectType(self, newRelatedObjectType: KalturaBeaconObjectTypes) -> None: ...
    def getEventType(self) -> str: ...
    def setEventType(self, newEventType: str) -> None: ...
    def getObjectId(self) -> str: ...
    def setObjectId(self, newObjectId: str) -> None: ...
    def getPrivateData(self) -> str: ...
    def setPrivateData(self, newPrivateData: str) -> None: ...
    def getRawData(self) -> str: ...
    def setRawData(self, newRawData: str) -> None: ...

class KalturaBeaconSearchParams(KalturaObjectBase):
    objectId: str
    def __init__(self,
            objectId: str = NotImplemented): ...

    def getObjectId(self) -> str: ...
    def setObjectId(self, newObjectId: str) -> None: ...

class KalturaBeaconSearchScheduledResourceOrderByItem(KalturaESearchOrderByItem):
    sortField: KalturaBeaconScheduledResourceOrderByFieldName
    def __init__(self,
            sortOrder: KalturaESearchSortOrder = NotImplemented,
            sortField: KalturaBeaconScheduledResourceOrderByFieldName = NotImplemented): ...

    def getSortField(self) -> KalturaBeaconScheduledResourceOrderByFieldName: ...
    def setSortField(self, newSortField: KalturaBeaconScheduledResourceOrderByFieldName) -> None: ...

class KalturaBeaconSearchScheduledResourceOrderBy(KalturaObjectBase):
    orderItems: List[KalturaBeaconSearchScheduledResourceOrderByItem]
    def __init__(self,
            orderItems: List[KalturaBeaconSearchScheduledResourceOrderByItem] = NotImplemented): ...

    def getOrderItems(self) -> List[KalturaBeaconSearchScheduledResourceOrderByItem]: ...
    def setOrderItems(self, newOrderItems: List[KalturaBeaconSearchScheduledResourceOrderByItem]) -> None: ...

class KalturaBeaconBaseFilter(KalturaFilter):
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    relatedObjectTypeIn: str
    relatedObjectTypeEqual: KalturaBeaconObjectTypes
    eventTypeIn: str
    objectIdIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            relatedObjectTypeIn: str = NotImplemented,
            relatedObjectTypeEqual: KalturaBeaconObjectTypes = NotImplemented,
            eventTypeIn: str = NotImplemented,
            objectIdIn: str = NotImplemented): ...

    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...
    def getRelatedObjectTypeIn(self) -> str: ...
    def setRelatedObjectTypeIn(self, newRelatedObjectTypeIn: str) -> None: ...
    def getRelatedObjectTypeEqual(self) -> KalturaBeaconObjectTypes: ...
    def setRelatedObjectTypeEqual(self, newRelatedObjectTypeEqual: KalturaBeaconObjectTypes) -> None: ...
    def getEventTypeIn(self) -> str: ...
    def setEventTypeIn(self, newEventTypeIn: str) -> None: ...
    def getObjectIdIn(self) -> str: ...
    def setObjectIdIn(self, newObjectIdIn: str) -> None: ...

class KalturaBeaconEnhanceFilter(KalturaFilter):
    externalElasticQueryObject: str
    indexTypeEqual: KalturaBeaconIndexType
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            externalElasticQueryObject: str = NotImplemented,
            indexTypeEqual: KalturaBeaconIndexType = NotImplemented): ...

    def getExternalElasticQueryObject(self) -> str: ...
    def setExternalElasticQueryObject(self, newExternalElasticQueryObject: str) -> None: ...
    def getIndexTypeEqual(self) -> KalturaBeaconIndexType: ...
    def setIndexTypeEqual(self, newIndexTypeEqual: KalturaBeaconIndexType) -> None: ...

class KalturaBeaconListResponse(KalturaListResponse):
    objects: List[KalturaBeacon]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaBeacon] = NotImplemented): ...

    def getObjects(self) -> List[KalturaBeacon]: ...

class KalturaBeaconScheduledResourceOperator(KalturaBeaconScheduledResourceBaseItem):
    operator: KalturaESearchOperatorType
    searchItems: List[KalturaBeaconScheduledResourceBaseItem]
    def __init__(self,
            operator: KalturaESearchOperatorType = NotImplemented,
            searchItems: List[KalturaBeaconScheduledResourceBaseItem] = NotImplemented): ...

    def getOperator(self) -> KalturaESearchOperatorType: ...
    def setOperator(self, newOperator: KalturaESearchOperatorType) -> None: ...
    def getSearchItems(self) -> List[KalturaBeaconScheduledResourceBaseItem]: ...
    def setSearchItems(self, newSearchItems: List[KalturaBeaconScheduledResourceBaseItem]) -> None: ...

class KalturaBeaconScheduledResourceSearchParams(KalturaBeaconSearchParams):
    searchOperator: KalturaBeaconScheduledResourceOperator
    orderBy: KalturaBeaconSearchScheduledResourceOrderBy
    def __init__(self,
            objectId: str = NotImplemented,
            searchOperator: KalturaBeaconScheduledResourceOperator = NotImplemented,
            orderBy: KalturaBeaconSearchScheduledResourceOrderBy = NotImplemented): ...

    def getSearchOperator(self) -> KalturaBeaconScheduledResourceOperator: ...
    def setSearchOperator(self, newSearchOperator: KalturaBeaconScheduledResourceOperator) -> None: ...
    def getOrderBy(self) -> KalturaBeaconSearchScheduledResourceOrderBy: ...
    def setOrderBy(self, newOrderBy: KalturaBeaconSearchScheduledResourceOrderBy) -> None: ...

class KalturaBeaconFilter(KalturaBeaconBaseFilter):
    indexTypeEqual: KalturaBeaconIndexType
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            relatedObjectTypeIn: str = NotImplemented,
            relatedObjectTypeEqual: KalturaBeaconObjectTypes = NotImplemented,
            eventTypeIn: str = NotImplemented,
            objectIdIn: str = NotImplemented,
            indexTypeEqual: KalturaBeaconIndexType = NotImplemented): ...

    def getIndexTypeEqual(self) -> KalturaBeaconIndexType: ...
    def setIndexTypeEqual(self, newIndexTypeEqual: KalturaBeaconIndexType) -> None: ...

class KalturaBeaconScheduledResourceItem(KalturaBeaconAbstractScheduledResourceItem):
    fieldName: KalturaBeaconScheduledResourceFieldName
    def __init__(self,
            searchTerm: str = NotImplemented,
            itemType: KalturaESearchItemType = NotImplemented,
            range: KalturaESearchRange = NotImplemented,
            fieldName: KalturaBeaconScheduledResourceFieldName = NotImplemented): ...

    def getFieldName(self) -> KalturaBeaconScheduledResourceFieldName: ...
    def setFieldName(self, newFieldName: KalturaBeaconScheduledResourceFieldName) -> None: ...

class KalturaBeaconService(KalturaServiceBase):
    def add(self, beacon: KalturaBeacon, shouldLog: int = 0) -> bool: ...
    def enhanceSearch(self, filter: KalturaBeaconEnhanceFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaBeaconListResponse: ...
    def list(self, filter: KalturaBeaconFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaBeaconListResponse: ...
    def searchScheduledResource(self, searchParams: KalturaBeaconSearchParams, pager: KalturaPager = NotImplemented) -> KalturaBeaconListResponse: ...

class KalturaBeaconClientPluginServicesProxy:
    beacon: KalturaBeaconService