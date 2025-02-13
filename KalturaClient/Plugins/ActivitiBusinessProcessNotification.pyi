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
from .BusinessProcessNotification import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaActivitiBusinessProcessServerOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaActivitiBusinessProcessServerProtocol(object):
    HTTP = "http"
    HTTPS = "https"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaActivitiBusinessProcessServer(KalturaBusinessProcessServer):
    host: str
    port: int
    protocol: KalturaActivitiBusinessProcessServerProtocol
    username: str
    password: str
    def __init__(self,
            id: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            status: KalturaBusinessProcessServerStatus = NotImplemented,
            type: KalturaBusinessProcessProvider = NotImplemented,
            dc: int = NotImplemented,
            host: str = NotImplemented,
            port: int = NotImplemented,
            protocol: KalturaActivitiBusinessProcessServerProtocol = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented): ...

    def getHost(self) -> str: ...
    def setHost(self, newHost: str) -> None: ...
    def getPort(self) -> int: ...
    def setPort(self, newPort: int) -> None: ...
    def getProtocol(self) -> KalturaActivitiBusinessProcessServerProtocol: ...
    def setProtocol(self, newProtocol: KalturaActivitiBusinessProcessServerProtocol) -> None: ...
    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...

class KalturaActivitiBusinessProcessServerBaseFilter(KalturaBusinessProcessServerFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            statusEqual: KalturaBusinessProcessServerStatus = NotImplemented,
            statusNotEqual: KalturaBusinessProcessServerStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            typeEqual: KalturaBusinessProcessProvider = NotImplemented,
            typeIn: str = NotImplemented,
            dcEqual: int = NotImplemented,
            dcEqOrNull: int = NotImplemented,
            currentDcOrExternal: KalturaNullableBoolean = NotImplemented,
            currentDc: KalturaNullableBoolean = NotImplemented): ...
        pass

class KalturaActivitiBusinessProcessServerFilter(KalturaActivitiBusinessProcessServerBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            statusEqual: KalturaBusinessProcessServerStatus = NotImplemented,
            statusNotEqual: KalturaBusinessProcessServerStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            typeEqual: KalturaBusinessProcessProvider = NotImplemented,
            typeIn: str = NotImplemented,
            dcEqual: int = NotImplemented,
            dcEqOrNull: int = NotImplemented,
            currentDcOrExternal: KalturaNullableBoolean = NotImplemented,
            currentDc: KalturaNullableBoolean = NotImplemented): ...
        pass

class KalturaActivitiBusinessProcessNotificationClientPluginServicesProxy: