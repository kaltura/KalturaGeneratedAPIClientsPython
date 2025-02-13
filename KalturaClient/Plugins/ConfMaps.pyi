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

class KalturaConfMapsStatus(object):
    STATUS_DISABLED = 0
    STATUS_ENABLED = 1

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaConfMaps(KalturaObjectBase):
    name: str
    content: str
    rawData: str
    userId: str
    isEditable: bool
    createdAt: int
    relatedHost: str
    version: int
    sourceLocation: KalturaConfMapsSourceLocation
    remarks: str
    status: KalturaConfMapsStatus
    changeDescription: str
    def __init__(self,
            name: str = NotImplemented,
            content: str = NotImplemented,
            rawData: str = NotImplemented,
            userId: str = NotImplemented,
            isEditable: bool = NotImplemented,
            createdAt: int = NotImplemented,
            relatedHost: str = NotImplemented,
            version: int = NotImplemented,
            sourceLocation: KalturaConfMapsSourceLocation = NotImplemented,
            remarks: str = NotImplemented,
            status: KalturaConfMapsStatus = NotImplemented,
            changeDescription: str = NotImplemented): ...

    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getContent(self) -> str: ...
    def setContent(self, newContent: str) -> None: ...
    def getRawData(self) -> str: ...
    def setRawData(self, newRawData: str) -> None: ...
    def getUserId(self) -> str: ...
    def setUserId(self, newUserId: str) -> None: ...
    def getIsEditable(self) -> bool: ...
    def getCreatedAt(self) -> int: ...
    def getRelatedHost(self) -> str: ...
    def setRelatedHost(self, newRelatedHost: str) -> None: ...
    def getVersion(self) -> int: ...
    def getSourceLocation(self) -> KalturaConfMapsSourceLocation: ...
    def setSourceLocation(self, newSourceLocation: KalturaConfMapsSourceLocation) -> None: ...
    def getRemarks(self) -> str: ...
    def setRemarks(self, newRemarks: str) -> None: ...
    def getStatus(self) -> KalturaConfMapsStatus: ...
    def setStatus(self, newStatus: KalturaConfMapsStatus) -> None: ...
    def getChangeDescription(self) -> str: ...
    def setChangeDescription(self, newChangeDescription: str) -> None: ...

class KalturaConfMapsListResponse(KalturaListResponse):
    objects: List[KalturaConfMaps]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaConfMaps] = NotImplemented): ...

    def getObjects(self) -> List[KalturaConfMaps]: ...

class KalturaConfMapsBaseFilter(KalturaRelatedFilter):
    nameEqual: str
    relatedHostEqual: str
    versionEqual: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            nameEqual: str = NotImplemented,
            relatedHostEqual: str = NotImplemented,
            versionEqual: int = NotImplemented): ...

    def getNameEqual(self) -> str: ...
    def setNameEqual(self, newNameEqual: str) -> None: ...
    def getRelatedHostEqual(self) -> str: ...
    def setRelatedHostEqual(self, newRelatedHostEqual: str) -> None: ...
    def getVersionEqual(self) -> int: ...
    def setVersionEqual(self, newVersionEqual: int) -> None: ...

class KalturaConfMapsFilter(KalturaConfMapsBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            nameEqual: str = NotImplemented,
            relatedHostEqual: str = NotImplemented,
            versionEqual: int = NotImplemented): ...
        pass

class KalturaConfMapsClientPluginServicesProxy: