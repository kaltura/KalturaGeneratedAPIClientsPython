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

class KalturaSipSourceType(object):
    PICTURE_IN_PICTURE = 1
    TALKING_HEADS = 2
    SCREEN_SHARE = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaSipServerNodeOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    HEARTBEAT_TIME_ASC = "+heartbeatTime"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    HEARTBEAT_TIME_DESC = "-heartbeatTime"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaSipEntryServerNode(KalturaEntryServerNode):
    sipRoomId: str
    sipPrimaryAdpId: str
    sipSecondaryAdpId: str
    def __init__(self,
            id: int = NotImplemented,
            entryId: str = NotImplemented,
            serverNodeId: int = NotImplemented,
            partnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaEntryServerNodeStatus = NotImplemented,
            serverType: KalturaEntryServerNodeType = NotImplemented,
            sipRoomId: str = NotImplemented,
            sipPrimaryAdpId: str = NotImplemented,
            sipSecondaryAdpId: str = NotImplemented): ...

    def getSipRoomId(self) -> str: ...
    def getSipPrimaryAdpId(self) -> str: ...
    def getSipSecondaryAdpId(self) -> str: ...

class KalturaSipServerNode(KalturaServerNode):
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
            environment: str = NotImplemented): ...
        pass

class KalturaSipEntryServerNodeBaseFilter(KalturaEntryServerNodeFilter):
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

class KalturaSipServerNodeBaseFilter(KalturaServerNodeFilter):
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

class KalturaSipEntryServerNodeFilter(KalturaSipEntryServerNodeBaseFilter):
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

class KalturaSipServerNodeFilter(KalturaSipServerNodeBaseFilter):
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

class KalturaPexipService(KalturaServiceBase):
    def generateSipUrl(self, entryId: str, regenerate: bool = False, sourceType: int = 1) -> str: ...
    def handleIncomingCall(self) -> None: ...
    def listRooms(self, offset: int = 0, pageSize: int = 500, activeOnly: bool = False) -> List[KalturaStringValue]: ...

class KalturaSipClientPluginServicesProxy:
    pexip: KalturaPexipService