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

class KalturaGameObjectType(object):
    LEADERBOARD = "1"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaUserScoreProperties(KalturaObjectBase):
    rank: int
    userId: str
    score: int
    def __init__(self,
            rank: int = NotImplemented,
            userId: str = NotImplemented,
            score: int = NotImplemented): ...

    def getRank(self) -> int: ...
    def setRank(self, newRank: int) -> None: ...
    def getUserId(self) -> str: ...
    def setUserId(self, newUserId: str) -> None: ...
    def getScore(self) -> int: ...
    def setScore(self, newScore: int) -> None: ...

class KalturaUserScorePropertiesResponse(KalturaListResponse):
    objects: List[KalturaUserScoreProperties]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaUserScoreProperties] = NotImplemented): ...

    def getObjects(self) -> List[KalturaUserScoreProperties]: ...

class KalturaUserScorePropertiesBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented): ...
        pass

class KalturaUserScorePropertiesFilter(KalturaUserScorePropertiesBaseFilter):
    gameObjectId: str
    gameObjectType: KalturaGameObjectType
    userIdEqual: str
    placesAboveUser: int
    placesBelowUser: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            gameObjectId: str = NotImplemented,
            gameObjectType: KalturaGameObjectType = NotImplemented,
            userIdEqual: str = NotImplemented,
            placesAboveUser: int = NotImplemented,
            placesBelowUser: int = NotImplemented): ...

    def getGameObjectId(self) -> str: ...
    def setGameObjectId(self, newGameObjectId: str) -> None: ...
    def getGameObjectType(self) -> KalturaGameObjectType: ...
    def setGameObjectType(self, newGameObjectType: KalturaGameObjectType) -> None: ...
    def getUserIdEqual(self) -> str: ...
    def setUserIdEqual(self, newUserIdEqual: str) -> None: ...
    def getPlacesAboveUser(self) -> int: ...
    def setPlacesAboveUser(self, newPlacesAboveUser: int) -> None: ...
    def getPlacesBelowUser(self) -> int: ...
    def setPlacesBelowUser(self, newPlacesBelowUser: int) -> None: ...

class KalturaUserScoreService(KalturaServiceBase):
    def delete(self, gameObjectId: str, gameObjectType: str, userId: str) -> KalturaUserScorePropertiesResponse: ...
    def list(self, filter: KalturaUserScorePropertiesFilter, pager: KalturaFilterPager = NotImplemented) -> KalturaUserScorePropertiesResponse: ...
    def update(self, gameObjectId: str, gameObjectType: str, userId: str, score: int) -> KalturaUserScorePropertiesResponse: ...

class KalturaGameClientPluginServicesProxy:
    userScore: KalturaUserScoreService