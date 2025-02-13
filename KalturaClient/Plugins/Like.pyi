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

class KalturaLikeOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaLike(KalturaObjectBase):
    entryId: str
    userId: str
    createdAt: int
    def __init__(self,
            entryId: str = NotImplemented,
            userId: str = NotImplemented,
            createdAt: int = NotImplemented): ...

    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...
    def getUserId(self) -> str: ...
    def setUserId(self, newUserId: str) -> None: ...
    def getCreatedAt(self) -> int: ...
    def setCreatedAt(self, newCreatedAt: int) -> None: ...

class KalturaLikeListResponse(KalturaListResponse):
    objects: List[KalturaLike]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaLike] = NotImplemented): ...

    def getObjects(self) -> List[KalturaLike]: ...

class KalturaLikeBaseFilter(KalturaRelatedFilter):
    entryIdEqual: str
    entryIdIn: str
    userIdEqual: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented): ...

    def getEntryIdEqual(self) -> str: ...
    def setEntryIdEqual(self, newEntryIdEqual: str) -> None: ...
    def getEntryIdIn(self) -> str: ...
    def setEntryIdIn(self, newEntryIdIn: str) -> None: ...
    def getUserIdEqual(self) -> str: ...
    def setUserIdEqual(self, newUserIdEqual: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...

class KalturaLikeFilter(KalturaLikeBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaLikeService(KalturaServiceBase):
    def checkLikeExists(self, entryId: str, userId: str = NotImplemented) -> bool: ...
    def like(self, entryId: str) -> bool: ...
    def list(self, filter: KalturaLikeFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaLikeListResponse: ...
    def unlike(self, entryId: str) -> bool: ...

class KalturaLikeClientPluginServicesProxy:
    like: KalturaLikeService