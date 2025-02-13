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
from .Vendor import *
from .Metadata import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaMicrosoftTeamsDropFolderFile(KalturaDropFolderFile):
    remoteId: str
    ownerId: str
    additionalUserIds: str
    description: str
    targetCategoryIds: str
    name: str
    contentUrl: str
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
            remoteId: str = NotImplemented,
            ownerId: str = NotImplemented,
            additionalUserIds: str = NotImplemented,
            description: str = NotImplemented,
            targetCategoryIds: str = NotImplemented,
            name: str = NotImplemented,
            contentUrl: str = NotImplemented): ...

    def getRemoteId(self) -> str: ...
    def setRemoteId(self, newRemoteId: str) -> None: ...
    def getOwnerId(self) -> str: ...
    def setOwnerId(self, newOwnerId: str) -> None: ...
    def getAdditionalUserIds(self) -> str: ...
    def setAdditionalUserIds(self, newAdditionalUserIds: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getTargetCategoryIds(self) -> str: ...
    def setTargetCategoryIds(self, newTargetCategoryIds: str) -> None: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getContentUrl(self) -> str: ...
    def setContentUrl(self, newContentUrl: str) -> None: ...

class KalturaMicrosoftTeamsIntegrationSetting(KalturaIntegrationSetting):
    clientSecret: str
    clientId: str
    userMetadataProfileId: int
    scopes: str
    encryptionKey: str
    def __init__(self,
            id: int = NotImplemented,
            status: KalturaVendorIntegrationStatus = NotImplemented,
            defaultUserId: str = NotImplemented,
            accountId: str = NotImplemented,
            createUserIfNotExist: KalturaNullableBoolean = NotImplemented,
            conversionProfileId: int = NotImplemented,
            handleParticipantsMode: KalturaHandleParticipantsMode = NotImplemented,
            deletionPolicy: KalturaNullableBoolean = NotImplemented,
            createdAt: str = NotImplemented,
            updatedAt: str = NotImplemented,
            partnerId: int = NotImplemented,
            enableMeetingUpload: KalturaNullableBoolean = NotImplemented,
            enableMeetingChat: KalturaNullableBoolean = NotImplemented,
            clientSecret: str = NotImplemented,
            clientId: str = NotImplemented,
            userMetadataProfileId: int = NotImplemented,
            scopes: str = NotImplemented,
            encryptionKey: str = NotImplemented): ...

    def getClientSecret(self) -> str: ...
    def setClientSecret(self, newClientSecret: str) -> None: ...
    def getClientId(self) -> str: ...
    def setClientId(self, newClientId: str) -> None: ...
    def getUserMetadataProfileId(self) -> int: ...
    def setUserMetadataProfileId(self, newUserMetadataProfileId: int) -> None: ...
    def getScopes(self) -> str: ...
    def setScopes(self, newScopes: str) -> None: ...
    def getEncryptionKey(self) -> str: ...

class KalturaMicrosoftTeamsDropFolder(KalturaRemoteDropFolder):
    integrationId: int
    tenantId: str
    clientSecret: str
    clientId: str
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
            integrationId: int = NotImplemented,
            tenantId: str = NotImplemented,
            clientSecret: str = NotImplemented,
            clientId: str = NotImplemented): ...

    def getIntegrationId(self) -> int: ...
    def setIntegrationId(self, newIntegrationId: int) -> None: ...
    def getTenantId(self) -> str: ...
    def getClientSecret(self) -> str: ...
    def getClientId(self) -> str: ...

class KalturaMicrosoftTeamsDropFolderClientPluginServicesProxy: