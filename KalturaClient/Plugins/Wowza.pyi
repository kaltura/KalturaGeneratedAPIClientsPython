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

class KalturaWowzaMediaServerNodeOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    HEARTBEAT_TIME_ASC = "+heartbeatTime"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    HEARTBEAT_TIME_DESC = "-heartbeatTime"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaWowzaMediaServerNode(KalturaMediaServerNode):
    appPrefix: str
    transcoder: str
    GPUID: int
    liveServicePort: int
    liveServiceProtocol: str
    liveServiceInternalDomain: str
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
            deliveryProfileIds: List[KalturaKeyValue] = NotImplemented,
            config: str = NotImplemented,
            applicationName: str = NotImplemented,
            mediaServerPortConfig: List[KalturaKeyValue] = NotImplemented,
            mediaServerPlaybackDomainConfig: List[KalturaKeyValue] = NotImplemented,
            appPrefix: str = NotImplemented,
            transcoder: str = NotImplemented,
            GPUID: int = NotImplemented,
            liveServicePort: int = NotImplemented,
            liveServiceProtocol: str = NotImplemented,
            liveServiceInternalDomain: str = NotImplemented): ...

    def getAppPrefix(self) -> str: ...
    def setAppPrefix(self, newAppPrefix: str) -> None: ...
    def getTranscoder(self) -> str: ...
    def setTranscoder(self, newTranscoder: str) -> None: ...
    def getGPUID(self) -> int: ...
    def setGPUID(self, newGPUID: int) -> None: ...
    def getLiveServicePort(self) -> int: ...
    def setLiveServicePort(self, newLiveServicePort: int) -> None: ...
    def getLiveServiceProtocol(self) -> str: ...
    def setLiveServiceProtocol(self, newLiveServiceProtocol: str) -> None: ...
    def getLiveServiceInternalDomain(self) -> str: ...
    def setLiveServiceInternalDomain(self, newLiveServiceInternalDomain: str) -> None: ...

class KalturaWowzaMediaServerNodeBaseFilter(KalturaMediaServerNodeFilter):
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

class KalturaWowzaMediaServerNodeFilter(KalturaWowzaMediaServerNodeBaseFilter):
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

class KalturaWowzaClientPluginServicesProxy: