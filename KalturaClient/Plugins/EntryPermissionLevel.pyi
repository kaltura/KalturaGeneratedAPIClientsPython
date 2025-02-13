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

class KalturaUserEntryPermissionLevel(object):
    SPEAKER = 1
    ROOM_MODERATOR = 2
    ATTENDEE = 3
    ADMIN = 4
    PREVIEW_ONLY = 5
    CHAT_MODERATOR = 6
    PANELIST = 7

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaPermissionLevel(KalturaObjectBase):
    permissionLevel: KalturaUserEntryPermissionLevel
    def __init__(self,
            permissionLevel: KalturaUserEntryPermissionLevel = NotImplemented): ...

    def getPermissionLevel(self) -> KalturaUserEntryPermissionLevel: ...
    def setPermissionLevel(self, newPermissionLevel: KalturaUserEntryPermissionLevel) -> None: ...

class KalturaPermissionLevelUserEntry(KalturaUserEntry):
    permissionLevels: List[KalturaPermissionLevel]
    permissionOrder: int
    def __init__(self,
            id: int = NotImplemented,
            entryId: str = NotImplemented,
            userId: str = NotImplemented,
            partnerId: int = NotImplemented,
            status: KalturaUserEntryStatus = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            type: KalturaUserEntryType = NotImplemented,
            permissionLevels: List[KalturaPermissionLevel] = NotImplemented,
            permissionOrder: int = NotImplemented): ...

    def getPermissionLevels(self) -> List[KalturaPermissionLevel]: ...
    def setPermissionLevels(self, newPermissionLevels: List[KalturaPermissionLevel]) -> None: ...
    def getPermissionOrder(self) -> int: ...
    def setPermissionOrder(self, newPermissionOrder: int) -> None: ...

class KalturaPermissionLevelUserEntryFilter(KalturaUserEntryFilter):
    permissionLevels: List[KalturaPermissionLevel]
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
            permissionLevels: List[KalturaPermissionLevel] = NotImplemented): ...

    def getPermissionLevels(self) -> List[KalturaPermissionLevel]: ...
    def setPermissionLevels(self, newPermissionLevels: List[KalturaPermissionLevel]) -> None: ...

class KalturaEntryPermissionLevelClientPluginServicesProxy: