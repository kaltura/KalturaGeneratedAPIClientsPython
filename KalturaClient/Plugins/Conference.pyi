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
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaConferenceRoomStatus(object):
    CREATED = 1
    READY = 2
    ENDED = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaConferenceServerNodeOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    HEARTBEAT_TIME_ASC = "+heartbeatTime"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    HEARTBEAT_TIME_DESC = "-heartbeatTime"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaRoomDetails(KalturaObjectBase):
    serverUrl: str
    entryId: str
    token: str
    expiry: int
    serverName: str
    def __init__(self,
            serverUrl: str = NotImplemented,
            entryId: str = NotImplemented,
            token: str = NotImplemented,
            expiry: int = NotImplemented,
            serverName: str = NotImplemented): ...

    def getServerUrl(self) -> str: ...
    def setServerUrl(self, newServerUrl: str) -> None: ...
    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...
    def getToken(self) -> str: ...
    def setToken(self, newToken: str) -> None: ...
    def getExpiry(self) -> int: ...
    def setExpiry(self, newExpiry: int) -> None: ...
    def getServerName(self) -> str: ...
    def setServerName(self, newServerName: str) -> None: ...

class KalturaConferenceEntryServerNode(KalturaEntryServerNode):
    confRoomStatus: KalturaConferenceRoomStatus
    registered: int
    def __init__(self,
            id: int = NotImplemented,
            entryId: str = NotImplemented,
            serverNodeId: int = NotImplemented,
            partnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaEntryServerNodeStatus = NotImplemented,
            serverType: KalturaEntryServerNodeType = NotImplemented,
            confRoomStatus: KalturaConferenceRoomStatus = NotImplemented,
            registered: int = NotImplemented): ...

    def getConfRoomStatus(self) -> KalturaConferenceRoomStatus: ...
    def getRegistered(self) -> int: ...

class KalturaConferenceServerNode(KalturaServerNode):
    serviceBaseUrl: str
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            heartbeatTime: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            hostName: str = NotImplemented,
            status: KalturaServerNodeStatus = NotImplemented,
            type: KalturaServerNodeType = NotImplemented,
            tags: str = NotImplemented,
            dc: int = NotImplemented,
            parentId: str = NotImplemented,
            environment: str = NotImplemented,
            serviceBaseUrl: str = NotImplemented): ...

    def getServiceBaseUrl(self) -> str: ...
    def setServiceBaseUrl(self, newServiceBaseUrl: str) -> None: ...

class KalturaConferenceEntryServerNodeBaseFilter(KalturaEntryServerNodeFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            serverNodeIdEqual: int = NotImplemented,
            serverNodeIdIn: str = NotImplemented,
            serverNodeIdNotIn: str = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaEntryServerNodeStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serverTypeEqual: KalturaEntryServerNodeType = NotImplemented,
            serverTypeIn: str = NotImplemented,
            serverTypeNotIn: str = NotImplemented): ...
        pass

class KalturaConferenceServerNodeBaseFilter(KalturaServerNodeFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            heartbeatTimeGreaterThanOrEqual: int = NotImplemented,
            heartbeatTimeLessThanOrEqual: int = NotImplemented,
            nameEqual: str = NotImplemented,
            nameIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            hostNameLike: str = NotImplemented,
            hostNameMultiLikeOr: str = NotImplemented,
            hostNameMultiLikeAnd: str = NotImplemented,
            statusEqual: KalturaServerNodeStatus = NotImplemented,
            statusIn: str = NotImplemented,
            typeEqual: KalturaServerNodeType = NotImplemented,
            typeIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            dcEqual: int = NotImplemented,
            dcIn: str = NotImplemented,
            parentIdLike: str = NotImplemented,
            parentIdMultiLikeOr: str = NotImplemented,
            parentIdMultiLikeAnd: str = NotImplemented,
            environmentEqual: str = NotImplemented,
            environmentIn: str = NotImplemented): ...
        pass

class KalturaConferenceEntryServerNodeFilter(KalturaConferenceEntryServerNodeBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            serverNodeIdEqual: int = NotImplemented,
            serverNodeIdIn: str = NotImplemented,
            serverNodeIdNotIn: str = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaEntryServerNodeStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serverTypeEqual: KalturaEntryServerNodeType = NotImplemented,
            serverTypeIn: str = NotImplemented,
            serverTypeNotIn: str = NotImplemented): ...
        pass

class KalturaConferenceServerNodeFilter(KalturaConferenceServerNodeBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            heartbeatTimeGreaterThanOrEqual: int = NotImplemented,
            heartbeatTimeLessThanOrEqual: int = NotImplemented,
            nameEqual: str = NotImplemented,
            nameIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            hostNameLike: str = NotImplemented,
            hostNameMultiLikeOr: str = NotImplemented,
            hostNameMultiLikeAnd: str = NotImplemented,
            statusEqual: KalturaServerNodeStatus = NotImplemented,
            statusIn: str = NotImplemented,
            typeEqual: KalturaServerNodeType = NotImplemented,
            typeIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            dcEqual: int = NotImplemented,
            dcIn: str = NotImplemented,
            parentIdLike: str = NotImplemented,
            parentIdMultiLikeOr: str = NotImplemented,
            parentIdMultiLikeAnd: str = NotImplemented,
            environmentEqual: str = NotImplemented,
            environmentIn: str = NotImplemented): ...
        pass

class KalturaConferenceClientPluginServicesProxy: