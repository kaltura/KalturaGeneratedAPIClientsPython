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

class KalturaS3DropFolder(KalturaDropFolder):
    s3Host: str
    s3Region: str
    s3UserId: str
    s3Password: str
    useS3Arn: bool
    s3Arn: str
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
            s3Host: str = NotImplemented,
            s3Region: str = NotImplemented,
            s3UserId: str = NotImplemented,
            s3Password: str = NotImplemented,
            useS3Arn: bool = NotImplemented,
            s3Arn: str = NotImplemented): ...

    def getS3Host(self) -> str: ...
    def setS3Host(self, newS3Host: str) -> None: ...
    def getS3Region(self) -> str: ...
    def setS3Region(self, newS3Region: str) -> None: ...
    def getS3UserId(self) -> str: ...
    def setS3UserId(self, newS3UserId: str) -> None: ...
    def getS3Password(self) -> str: ...
    def setS3Password(self, newS3Password: str) -> None: ...
    def getUseS3Arn(self) -> bool: ...
    def setUseS3Arn(self, newUseS3Arn: bool) -> None: ...
    def getS3Arn(self) -> str: ...

class KalturaS3DropFolderFile(KalturaDropFolderFile):
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            dropFolderId: int = NotImplemented,
            fileName: str = NotImplemented,
            fileSize: float = NotImplemented,
            fileSizeLastSetAt: int = NotImplemented,
            status: KalturaDropFolderFileStatus = NotImplemented,
            type: KalturaDropFolderType = NotImplemented,
            parsedSlug: str = NotImplemented,
            parsedFlavor: str = NotImplemented,
            parsedUserId: str = NotImplemented,
            leadDropFolderFileId: int = NotImplemented,
            deletedDropFolderFileId: int = NotImplemented,
            entryId: str = NotImplemented,
            errorCode: KalturaDropFolderFileErrorCode = NotImplemented,
            errorDescription: str = NotImplemented,
            lastModificationTime: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            uploadStartDetectedAt: int = NotImplemented,
            uploadEndDetectedAt: int = NotImplemented,
            importStartedAt: int = NotImplemented,
            importEndedAt: int = NotImplemented,
            batchJobId: int = NotImplemented): ...
        pass

class KalturaS3DropFolderClientPluginServicesProxy: