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
from .DropFolder import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaDropFolderTrRdsFileHandlerConfig(KalturaDropFolderFileHandlerConfig):
    leadPattern: str
    additionalPatterns: str
    def __init__(self,
            handlerType: KalturaDropFolderFileHandlerType = NotImplemented,
            leadPattern: str = NotImplemented,
            additionalPatterns: str = NotImplemented): ...

    def getLeadPattern(self) -> str: ...
    def setLeadPattern(self, newLeadPattern: str) -> None: ...
    def getAdditionalPatterns(self) -> str: ...
    def setAdditionalPatterns(self, newAdditionalPatterns: str) -> None: ...

class KalturaTrRdsDropFolder(KalturaSftpDropFolder):
    syncMetadataProfile: int
    targetMetadataProfile: int
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            description: str = NotImplemented,
            type: KalturaDropFolderType = NotImplemented,
            status: KalturaDropFolderStatus = NotImplemented,
            conversionProfileId: int = NotImplemented,
            dc: int = NotImplemented,
            path: str = NotImplemented,
            fileSizeCheckInterval: int = NotImplemented,
            fileDeletePolicy: KalturaDropFolderFileDeletePolicy = NotImplemented,
            fileDeleteRegex: str = NotImplemented,
            autoFileDeleteDays: int = NotImplemented,
            fileHandlerType: KalturaDropFolderFileHandlerType = NotImplemented,
            fileNamePatterns: str = NotImplemented,
            fileHandlerConfig: KalturaDropFolderFileHandlerConfig = NotImplemented,
            tags: str = NotImplemented,
            errorCode: KalturaDropFolderErrorCode = NotImplemented,
            errorDescription: str = NotImplemented,
            ignoreFileNamePatterns: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            lastAccessedAt: int = NotImplemented,
            incremental: bool = NotImplemented,
            lastFileTimestamp: int = NotImplemented,
            metadataProfileId: int = NotImplemented,
            categoriesMetadataFieldName: str = NotImplemented,
            enforceEntitlement: bool = NotImplemented,
            shouldValidateKS: bool = NotImplemented,
            host: str = NotImplemented,
            port: int = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented,
            privateKey: str = NotImplemented,
            publicKey: str = NotImplemented,
            passPhrase: str = NotImplemented,
            syncMetadataProfile: int = NotImplemented,
            targetMetadataProfile: int = NotImplemented): ...

    def getSyncMetadataProfile(self) -> int: ...
    def setSyncMetadataProfile(self, newSyncMetadataProfile: int) -> None: ...
    def getTargetMetadataProfile(self) -> int: ...
    def setTargetMetadataProfile(self, newTargetMetadataProfile: int) -> None: ...

class KalturaTrRdsSyncDropFolderClientPluginServicesProxy: