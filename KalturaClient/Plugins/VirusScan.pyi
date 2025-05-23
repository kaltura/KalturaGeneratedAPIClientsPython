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

class KalturaVirusFoundAction(object):
    NONE = 0
    DELETE = 1
    CLEAN_NONE = 2
    CLEAN_DELETE = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVirusScanJobResult(object):
    SCAN_ERROR = 1
    FILE_IS_CLEAN = 2
    FILE_WAS_CLEANED = 3
    FILE_INFECTED = 4

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVirusScanProfileStatus(object):
    DISABLED = 1
    ENABLED = 2
    DELETED = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVirusScanEngineType(object):
    CLAMAV_SCAN_ENGINE = "clamAVScanEngine.ClamAV"
    SYMANTEC_SCAN_DIRECT_ENGINE = "symantecScanEngine.SymantecScanDirectEngine"
    SYMANTEC_SCAN_ENGINE = "symantecScanEngine.SymantecScanEngine"
    SYMANTEC_SCAN_JAVA_ENGINE = "symantecScanEngine.SymantecScanJavaEngine"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVirusScanProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVirusScanProfile(KalturaObjectBase):
    id: int
    createdAt: int
    updatedAt: int
    partnerId: int
    name: str
    status: KalturaVirusScanProfileStatus
    engineType: KalturaVirusScanEngineType
    entryFilter: KalturaBaseEntryFilter
    actionIfInfected: KalturaVirusFoundAction
    def __init__(self,
            id: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            status: KalturaVirusScanProfileStatus = NotImplemented,
            engineType: KalturaVirusScanEngineType = NotImplemented,
            entryFilter: KalturaBaseEntryFilter = NotImplemented,
            actionIfInfected: KalturaVirusFoundAction = NotImplemented): ...

    def getId(self) -> int: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getPartnerId(self) -> int: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getStatus(self) -> KalturaVirusScanProfileStatus: ...
    def setStatus(self, newStatus: KalturaVirusScanProfileStatus) -> None: ...
    def getEngineType(self) -> KalturaVirusScanEngineType: ...
    def setEngineType(self, newEngineType: KalturaVirusScanEngineType) -> None: ...
    def getEntryFilter(self) -> KalturaBaseEntryFilter: ...
    def setEntryFilter(self, newEntryFilter: KalturaBaseEntryFilter) -> None: ...
    def getActionIfInfected(self) -> KalturaVirusFoundAction: ...
    def setActionIfInfected(self, newActionIfInfected: KalturaVirusFoundAction) -> None: ...

class KalturaParseCaptionAssetJobData(KalturaJobData):
    captionAssetId: str
    def __init__(self,
            captionAssetId: str = NotImplemented): ...

    def getCaptionAssetId(self) -> str: ...
    def setCaptionAssetId(self, newCaptionAssetId: str) -> None: ...

class KalturaVirusScanJobData(KalturaJobData):
    fileContainer: KalturaFileContainer
    flavorAssetId: str
    scanResult: KalturaVirusScanJobResult
    virusFoundAction: KalturaVirusFoundAction
    def __init__(self,
            fileContainer: KalturaFileContainer = NotImplemented,
            flavorAssetId: str = NotImplemented,
            scanResult: KalturaVirusScanJobResult = NotImplemented,
            virusFoundAction: KalturaVirusFoundAction = NotImplemented): ...

    def getFileContainer(self) -> KalturaFileContainer: ...
    def setFileContainer(self, newFileContainer: KalturaFileContainer) -> None: ...
    def getFlavorAssetId(self) -> str: ...
    def setFlavorAssetId(self, newFlavorAssetId: str) -> None: ...
    def getScanResult(self) -> KalturaVirusScanJobResult: ...
    def setScanResult(self, newScanResult: KalturaVirusScanJobResult) -> None: ...
    def getVirusFoundAction(self) -> KalturaVirusFoundAction: ...
    def setVirusFoundAction(self, newVirusFoundAction: KalturaVirusFoundAction) -> None: ...

class KalturaVirusScanProfileBaseFilter(KalturaFilter):
    idEqual: int
    idIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    partnerIdEqual: int
    partnerIdIn: str
    nameEqual: str
    nameLike: str
    statusEqual: KalturaVirusScanProfileStatus
    statusIn: str
    engineTypeEqual: KalturaVirusScanEngineType
    engineTypeIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            nameLike: str = NotImplemented,
            statusEqual: KalturaVirusScanProfileStatus = NotImplemented,
            statusIn: str = NotImplemented,
            engineTypeEqual: KalturaVirusScanEngineType = NotImplemented,
            engineTypeIn: str = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...
    def getPartnerIdEqual(self) -> int: ...
    def setPartnerIdEqual(self, newPartnerIdEqual: int) -> None: ...
    def getPartnerIdIn(self) -> str: ...
    def setPartnerIdIn(self, newPartnerIdIn: str) -> None: ...
    def getNameEqual(self) -> str: ...
    def setNameEqual(self, newNameEqual: str) -> None: ...
    def getNameLike(self) -> str: ...
    def setNameLike(self, newNameLike: str) -> None: ...
    def getStatusEqual(self) -> KalturaVirusScanProfileStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaVirusScanProfileStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getEngineTypeEqual(self) -> KalturaVirusScanEngineType: ...
    def setEngineTypeEqual(self, newEngineTypeEqual: KalturaVirusScanEngineType) -> None: ...
    def getEngineTypeIn(self) -> str: ...
    def setEngineTypeIn(self, newEngineTypeIn: str) -> None: ...

class KalturaVirusScanProfileListResponse(KalturaListResponse):
    objects: List[KalturaVirusScanProfile]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaVirusScanProfile] = NotImplemented): ...

    def getObjects(self) -> List[KalturaVirusScanProfile]: ...

class KalturaVirusScanProfileFilter(KalturaVirusScanProfileBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            nameLike: str = NotImplemented,
            statusEqual: KalturaVirusScanProfileStatus = NotImplemented,
            statusIn: str = NotImplemented,
            engineTypeEqual: KalturaVirusScanEngineType = NotImplemented,
            engineTypeIn: str = NotImplemented): ...
        pass

class KalturaVirusScanProfileService(KalturaServiceBase):
    def add(self, virusScanProfile: KalturaVirusScanProfile) -> KalturaVirusScanProfile: ...
    def delete(self, virusScanProfileId: int) -> KalturaVirusScanProfile: ...
    def get(self, virusScanProfileId: int) -> KalturaVirusScanProfile: ...
    def list(self, filter: KalturaVirusScanProfileFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaVirusScanProfileListResponse: ...
    def scan(self, flavorAssetId: str, virusScanProfileId: int = NotImplemented) -> int: ...
    def update(self, virusScanProfileId: int, virusScanProfile: KalturaVirusScanProfile) -> KalturaVirusScanProfile: ...

class KalturaVirusScanClientPluginServicesProxy:
    virusScanProfile: KalturaVirusScanProfileService