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

class KalturaVarPartnerUsageItem(KalturaObjectBase):
    partnerId: int
    partnerName: str
    partnerStatus: KalturaPartnerStatus
    partnerPackage: int
    partnerCreatedAt: int
    views: int
    plays: int
    entriesCount: int
    totalEntriesCount: int
    videoEntriesCount: int
    imageEntriesCount: int
    audioEntriesCount: int
    mixEntriesCount: int
    bandwidth: float
    totalStorage: float
    storage: float
    deletedStorage: float
    peakStorage: float
    avgStorage: float
    combinedStorageBandwidth: float
    transcodingUsage: float
    dateId: str
    def __init__(self,
            partnerId: int = NotImplemented,
            partnerName: str = NotImplemented,
            partnerStatus: KalturaPartnerStatus = NotImplemented,
            partnerPackage: int = NotImplemented,
            partnerCreatedAt: int = NotImplemented,
            views: int = NotImplemented,
            plays: int = NotImplemented,
            entriesCount: int = NotImplemented,
            totalEntriesCount: int = NotImplemented,
            videoEntriesCount: int = NotImplemented,
            imageEntriesCount: int = NotImplemented,
            audioEntriesCount: int = NotImplemented,
            mixEntriesCount: int = NotImplemented,
            bandwidth: float = NotImplemented,
            totalStorage: float = NotImplemented,
            storage: float = NotImplemented,
            deletedStorage: float = NotImplemented,
            peakStorage: float = NotImplemented,
            avgStorage: float = NotImplemented,
            combinedStorageBandwidth: float = NotImplemented,
            transcodingUsage: float = NotImplemented,
            dateId: str = NotImplemented): ...

    def getPartnerId(self) -> int: ...
    def setPartnerId(self, newPartnerId: int) -> None: ...
    def getPartnerName(self) -> str: ...
    def setPartnerName(self, newPartnerName: str) -> None: ...
    def getPartnerStatus(self) -> KalturaPartnerStatus: ...
    def setPartnerStatus(self, newPartnerStatus: KalturaPartnerStatus) -> None: ...
    def getPartnerPackage(self) -> int: ...
    def setPartnerPackage(self, newPartnerPackage: int) -> None: ...
    def getPartnerCreatedAt(self) -> int: ...
    def setPartnerCreatedAt(self, newPartnerCreatedAt: int) -> None: ...
    def getViews(self) -> int: ...
    def setViews(self, newViews: int) -> None: ...
    def getPlays(self) -> int: ...
    def setPlays(self, newPlays: int) -> None: ...
    def getEntriesCount(self) -> int: ...
    def setEntriesCount(self, newEntriesCount: int) -> None: ...
    def getTotalEntriesCount(self) -> int: ...
    def setTotalEntriesCount(self, newTotalEntriesCount: int) -> None: ...
    def getVideoEntriesCount(self) -> int: ...
    def setVideoEntriesCount(self, newVideoEntriesCount: int) -> None: ...
    def getImageEntriesCount(self) -> int: ...
    def setImageEntriesCount(self, newImageEntriesCount: int) -> None: ...
    def getAudioEntriesCount(self) -> int: ...
    def setAudioEntriesCount(self, newAudioEntriesCount: int) -> None: ...
    def getMixEntriesCount(self) -> int: ...
    def setMixEntriesCount(self, newMixEntriesCount: int) -> None: ...
    def getBandwidth(self) -> float: ...
    def setBandwidth(self, newBandwidth: float) -> None: ...
    def getTotalStorage(self) -> float: ...
    def setTotalStorage(self, newTotalStorage: float) -> None: ...
    def getStorage(self) -> float: ...
    def setStorage(self, newStorage: float) -> None: ...
    def getDeletedStorage(self) -> float: ...
    def setDeletedStorage(self, newDeletedStorage: float) -> None: ...
    def getPeakStorage(self) -> float: ...
    def setPeakStorage(self, newPeakStorage: float) -> None: ...
    def getAvgStorage(self) -> float: ...
    def setAvgStorage(self, newAvgStorage: float) -> None: ...
    def getCombinedStorageBandwidth(self) -> float: ...
    def setCombinedStorageBandwidth(self, newCombinedStorageBandwidth: float) -> None: ...
    def getTranscodingUsage(self) -> float: ...
    def setTranscodingUsage(self, newTranscodingUsage: float) -> None: ...
    def getDateId(self) -> str: ...
    def setDateId(self, newDateId: str) -> None: ...

class KalturaPartnerUsageListResponse(KalturaListResponse):
    total: KalturaVarPartnerUsageItem
    objects: List[KalturaVarPartnerUsageItem]
    def __init__(self,
            totalCount: int = NotImplemented,
            total: KalturaVarPartnerUsageItem = NotImplemented,
            objects: List[KalturaVarPartnerUsageItem] = NotImplemented): ...

    def getTotal(self) -> KalturaVarPartnerUsageItem: ...
    def setTotal(self, newTotal: KalturaVarPartnerUsageItem) -> None: ...
    def getObjects(self) -> List[KalturaVarPartnerUsageItem]: ...
    def setObjects(self, newObjects: List[KalturaVarPartnerUsageItem]) -> None: ...

class KalturaVarPartnerUsageTotalItem(KalturaVarPartnerUsageItem):
    def __init__(self,
            partnerId: int = NotImplemented,
            partnerName: str = NotImplemented,
            partnerStatus: KalturaPartnerStatus = NotImplemented,
            partnerPackage: int = NotImplemented,
            partnerCreatedAt: int = NotImplemented,
            views: int = NotImplemented,
            plays: int = NotImplemented,
            entriesCount: int = NotImplemented,
            totalEntriesCount: int = NotImplemented,
            videoEntriesCount: int = NotImplemented,
            imageEntriesCount: int = NotImplemented,
            audioEntriesCount: int = NotImplemented,
            mixEntriesCount: int = NotImplemented,
            bandwidth: float = NotImplemented,
            totalStorage: float = NotImplemented,
            storage: float = NotImplemented,
            deletedStorage: float = NotImplemented,
            peakStorage: float = NotImplemented,
            avgStorage: float = NotImplemented,
            combinedStorageBandwidth: float = NotImplemented,
            transcodingUsage: float = NotImplemented,
            dateId: str = NotImplemented): ...
        pass

class KalturaVarConsoleService(KalturaServiceBase):
    def getPartnerUsage(self, partnerFilter: KalturaPartnerFilter = NotImplemented, usageFilter: KalturaReportInputFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaPartnerUsageListResponse: ...
    def updateStatus(self, id: int, status: int) -> None: ...

class KalturaVarConsoleClientPluginServicesProxy:
    varConsole: KalturaVarConsoleService