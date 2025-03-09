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

class KalturaRsvpUserEntryOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaRsvpUserEntry(KalturaUserEntry):
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

class KalturaRsvpUserEntryBaseFilter(KalturaUserEntryFilter):
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

class KalturaRsvpUserEntryFilter(KalturaRsvpUserEntryBaseFilter):
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

class KalturaRsvpClientPluginServicesProxy: