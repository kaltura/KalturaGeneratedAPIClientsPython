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

class KalturaViewHistoryUserEntry(KalturaUserEntry):
    playbackContext: str
    lastTimeReached: int
    lastUpdateTime: int
    playlistLastEntryId: str
    extendedStatus: KalturaUserEntryExtendedStatus
    def __init__(self,
            id: int = NotImplemented,
            entryId: str = NotImplemented,
            userId: str = NotImplemented,
            partnerId: int = NotImplemented,
            status: KalturaUserEntryStatus = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            type: KalturaUserEntryType = NotImplemented,
            playbackContext: str = NotImplemented,
            lastTimeReached: int = NotImplemented,
            lastUpdateTime: int = NotImplemented,
            playlistLastEntryId: str = NotImplemented,
            extendedStatus: KalturaUserEntryExtendedStatus = NotImplemented): ...

    def getPlaybackContext(self) -> str: ...
    def setPlaybackContext(self, newPlaybackContext: str) -> None: ...
    def getLastTimeReached(self) -> int: ...
    def setLastTimeReached(self, newLastTimeReached: int) -> None: ...
    def getLastUpdateTime(self) -> int: ...
    def setLastUpdateTime(self, newLastUpdateTime: int) -> None: ...
    def getPlaylistLastEntryId(self) -> str: ...
    def setPlaylistLastEntryId(self, newPlaylistLastEntryId: str) -> None: ...
    def getExtendedStatus(self) -> KalturaUserEntryExtendedStatus: ...
    def setExtendedStatus(self, newExtendedStatus: KalturaUserEntryExtendedStatus) -> None: ...

class KalturaViewHistoryUserEntryAdvancedFilter(KalturaSearchItem):
    idEqual: str
    idIn: str
    userIdEqual: str
    userIdIn: str
    updatedAtGreaterThanOrEqual: str
    updatedAtLessThanOrEqual: str
    extendedStatusEqual: KalturaUserEntryExtendedStatus
    extendedStatusIn: str
    def __init__(self,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            updatedAtGreaterThanOrEqual: str = NotImplemented,
            updatedAtLessThanOrEqual: str = NotImplemented,
            extendedStatusEqual: KalturaUserEntryExtendedStatus = NotImplemented,
            extendedStatusIn: str = NotImplemented): ...

    def getIdEqual(self) -> str: ...
    def setIdEqual(self, newIdEqual: str) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getUserIdEqual(self) -> str: ...
    def setUserIdEqual(self, newUserIdEqual: str) -> None: ...
    def getUserIdIn(self) -> str: ...
    def setUserIdIn(self, newUserIdIn: str) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> str: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: str) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> str: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: str) -> None: ...
    def getExtendedStatusEqual(self) -> KalturaUserEntryExtendedStatus: ...
    def setExtendedStatusEqual(self, newExtendedStatusEqual: KalturaUserEntryExtendedStatus) -> None: ...
    def getExtendedStatusIn(self) -> str: ...
    def setExtendedStatusIn(self, newExtendedStatusIn: str) -> None: ...

class KalturaViewHistoryUserEntryFilter(KalturaUserEntryFilter):
    extendedStatusEqual: KalturaUserEntryExtendedStatus
    extendedStatusIn: str
    extendedStatusNotIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            entryIdNotIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            userIdNotIn: str = NotImplemented,
            statusEqual: KalturaUserEntryStatus = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            typeEqual: KalturaUserEntryType = NotImplemented,
            userIdEqualCurrent: KalturaNullableBoolean = NotImplemented,
            isAnonymous: KalturaNullableBoolean = NotImplemented,
            privacyContextEqual: str = NotImplemented,
            privacyContextIn: str = NotImplemented,
            partnerId: int = NotImplemented,
            extendedStatusEqual: KalturaUserEntryExtendedStatus = NotImplemented,
            extendedStatusIn: str = NotImplemented,
            extendedStatusNotIn: str = NotImplemented): ...

    def getExtendedStatusEqual(self) -> KalturaUserEntryExtendedStatus: ...
    def setExtendedStatusEqual(self, newExtendedStatusEqual: KalturaUserEntryExtendedStatus) -> None: ...
    def getExtendedStatusIn(self) -> str: ...
    def setExtendedStatusIn(self, newExtendedStatusIn: str) -> None: ...
    def getExtendedStatusNotIn(self) -> str: ...
    def setExtendedStatusNotIn(self, newExtendedStatusNotIn: str) -> None: ...

class KalturaViewHistoryClientPluginServicesProxy: