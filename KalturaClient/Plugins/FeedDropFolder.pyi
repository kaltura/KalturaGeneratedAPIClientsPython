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

class KalturaFeedItemInfo(KalturaObjectBase):
    itemXPath: str
    itemPublishDateXPath: str
    itemUniqueIdentifierXPath: str
    itemContentFileSizeXPath: str
    itemContentUrlXPath: str
    itemContentBitrateXPath: str
    itemHashXPath: str
    itemContentXpath: str
    contentBitrateAttributeName: str
    def __init__(self,
            itemXPath: str = NotImplemented,
            itemPublishDateXPath: str = NotImplemented,
            itemUniqueIdentifierXPath: str = NotImplemented,
            itemContentFileSizeXPath: str = NotImplemented,
            itemContentUrlXPath: str = NotImplemented,
            itemContentBitrateXPath: str = NotImplemented,
            itemHashXPath: str = NotImplemented,
            itemContentXpath: str = NotImplemented,
            contentBitrateAttributeName: str = NotImplemented): ...

    def getItemXPath(self) -> str: ...
    def setItemXPath(self, newItemXPath: str) -> None: ...
    def getItemPublishDateXPath(self) -> str: ...
    def setItemPublishDateXPath(self, newItemPublishDateXPath: str) -> None: ...
    def getItemUniqueIdentifierXPath(self) -> str: ...
    def setItemUniqueIdentifierXPath(self, newItemUniqueIdentifierXPath: str) -> None: ...
    def getItemContentFileSizeXPath(self) -> str: ...
    def setItemContentFileSizeXPath(self, newItemContentFileSizeXPath: str) -> None: ...
    def getItemContentUrlXPath(self) -> str: ...
    def setItemContentUrlXPath(self, newItemContentUrlXPath: str) -> None: ...
    def getItemContentBitrateXPath(self) -> str: ...
    def setItemContentBitrateXPath(self, newItemContentBitrateXPath: str) -> None: ...
    def getItemHashXPath(self) -> str: ...
    def setItemHashXPath(self, newItemHashXPath: str) -> None: ...
    def getItemContentXpath(self) -> str: ...
    def setItemContentXpath(self, newItemContentXpath: str) -> None: ...
    def getContentBitrateAttributeName(self) -> str: ...
    def setContentBitrateAttributeName(self, newContentBitrateAttributeName: str) -> None: ...

class KalturaFeedDropFolder(KalturaDropFolder):
    itemHandlingLimit: int
    feedItemInfo: KalturaFeedItemInfo
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
            itemHandlingLimit: int = NotImplemented,
            feedItemInfo: KalturaFeedItemInfo = NotImplemented): ...

    def getItemHandlingLimit(self) -> int: ...
    def setItemHandlingLimit(self, newItemHandlingLimit: int) -> None: ...
    def getFeedItemInfo(self) -> KalturaFeedItemInfo: ...
    def setFeedItemInfo(self, newFeedItemInfo: KalturaFeedItemInfo) -> None: ...

class KalturaFeedDropFolderFile(KalturaDropFolderFile):
    hash: str
    feedXmlPath: str
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
            batchJobId: int = NotImplemented,
            hash: str = NotImplemented,
            feedXmlPath: str = NotImplemented): ...

    def getHash(self) -> str: ...
    def setHash(self, newHash: str) -> None: ...
    def getFeedXmlPath(self) -> str: ...
    def setFeedXmlPath(self, newFeedXmlPath: str) -> None: ...

class KalturaFeedDropFolderClientPluginServicesProxy: