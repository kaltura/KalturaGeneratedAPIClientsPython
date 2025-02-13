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

class KalturaRatingCountOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaRatingCount(KalturaObjectBase):
    entryId: str
    rank: int
    count: int
    def __init__(self,
            entryId: str = NotImplemented,
            rank: int = NotImplemented,
            count: int = NotImplemented): ...

    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...
    def getRank(self) -> int: ...
    def setRank(self, newRank: int) -> None: ...
    def getCount(self) -> int: ...
    def setCount(self, newCount: int) -> None: ...

class KalturaRatingCountListResponse(KalturaListResponse):
    objects: List[KalturaRatingCount]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaRatingCount] = NotImplemented): ...

    def getObjects(self) -> List[KalturaRatingCount]: ...

class KalturaRatingCountBaseFilter(KalturaRelatedFilter):
    entryIdEqual: str
    rankIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            entryIdEqual: str = NotImplemented,
            rankIn: str = NotImplemented): ...

    def getEntryIdEqual(self) -> str: ...
    def setEntryIdEqual(self, newEntryIdEqual: str) -> None: ...
    def getRankIn(self) -> str: ...
    def setRankIn(self, newRankIn: str) -> None: ...

class KalturaRatingCountFilter(KalturaRatingCountBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            entryIdEqual: str = NotImplemented,
            rankIn: str = NotImplemented): ...
        pass

class KalturaRatingService(KalturaServiceBase):
    def checkRating(self, entryId: str) -> int: ...
    def getRatingCounts(self, filter: KalturaRatingCountFilter) -> KalturaRatingCountListResponse: ...
    def rate(self, entryId: str, rank: int) -> int: ...
    def removeRating(self, entryId: str) -> bool: ...

class KalturaRatingClientPluginServicesProxy:
    rating: KalturaRatingService