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

class KalturaWatchLaterUserEntry(KalturaUserEntry):
    def __init__(self,
            id: int = NotImplemented,
            entryId: str = NotImplemented,
            userId: str = NotImplemented,
            partnerId: int = NotImplemented,
            status: KalturaUserEntryStatus = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            type: KalturaUserEntryType = NotImplemented): ...
        pass

class KalturaWatchLaterUserEntryAdvancedFilter(KalturaSearchItem):
    idEqual: int
    idIn: str
    userIdEqual: str
    userIdIn: str
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    extendedStatusEqual: KalturaUserEntryExtendedStatus
    extendedStatusIn: str
    def __init__(self,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            extendedStatusEqual: KalturaUserEntryExtendedStatus = NotImplemented,
            extendedStatusIn: str = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getUserIdEqual(self) -> str: ...
    def setUserIdEqual(self, newUserIdEqual: str) -> None: ...
    def getUserIdIn(self) -> str: ...
    def setUserIdIn(self, newUserIdIn: str) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...
    def getExtendedStatusEqual(self) -> KalturaUserEntryExtendedStatus: ...
    def setExtendedStatusEqual(self, newExtendedStatusEqual: KalturaUserEntryExtendedStatus) -> None: ...
    def getExtendedStatusIn(self) -> str: ...
    def setExtendedStatusIn(self, newExtendedStatusIn: str) -> None: ...

class KalturaWatchLaterUserEntryFilter(KalturaUserEntryFilter):
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
            partnerId: int = NotImplemented): ...
        pass

class KalturaWatchLaterClientPluginServicesProxy: