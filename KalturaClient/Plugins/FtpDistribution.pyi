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
from .ContentDistribution import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaFtpDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaFtpDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaFtpScheduledDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaFtpDistributionFile(KalturaObjectBase):
    assetId: str
    filename: str
    contents: str
    localFilePath: str
    version: str
    hash: str
    def __init__(self,
            assetId: str = NotImplemented,
            filename: str = NotImplemented,
            contents: str = NotImplemented,
            localFilePath: str = NotImplemented,
            version: str = NotImplemented,
            hash: str = NotImplemented): ...

    def getAssetId(self) -> str: ...
    def setAssetId(self, newAssetId: str) -> None: ...
    def getFilename(self) -> str: ...
    def setFilename(self, newFilename: str) -> None: ...
    def getContents(self) -> str: ...
    def setContents(self, newContents: str) -> None: ...
    def getLocalFilePath(self) -> str: ...
    def setLocalFilePath(self, newLocalFilePath: str) -> None: ...
    def getVersion(self) -> str: ...
    def setVersion(self, newVersion: str) -> None: ...
    def getHash(self) -> str: ...
    def setHash(self, newHash: str) -> None: ...

class KalturaFtpDistributionProvider(KalturaDistributionProvider):
    def __init__(self,
            type: KalturaDistributionProviderType = NotImplemented,
            name: str = NotImplemented,
            scheduleUpdateEnabled: bool = NotImplemented,
            availabilityUpdateEnabled: bool = NotImplemented,
            deleteInsteadUpdate: bool = NotImplemented,
            intervalBeforeSunrise: int = NotImplemented,
            intervalBeforeSunset: int = NotImplemented,
            updateRequiredEntryFields: str = NotImplemented,
            updateRequiredMetadataXPaths: str = NotImplemented): ...
        pass

class KalturaFtpDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    filesForDistribution: List[KalturaFtpDistributionFile]
    def __init__(self,
            fieldValues: str = NotImplemented,
            filesForDistribution: List[KalturaFtpDistributionFile] = NotImplemented): ...

    def getFilesForDistribution(self) -> List[KalturaFtpDistributionFile]: ...
    def setFilesForDistribution(self, newFilesForDistribution: List[KalturaFtpDistributionFile]) -> None: ...

class KalturaFtpDistributionProfile(KalturaConfigurableDistributionProfile):
    protocol: KalturaDistributionProtocol
    host: str
    port: int
    basePath: str
    username: str
    password: str
    passphrase: str
    sftpPublicKey: str
    sftpPrivateKey: str
    disableMetadata: bool
    metadataXslt: str
    metadataFilenameXslt: str
    flavorAssetFilenameXslt: str
    thumbnailAssetFilenameXslt: str
    assetFilenameXslt: str
    asperaPublicKey: str
    asperaPrivateKey: str
    sendMetadataAfterAssets: bool
    def __init__(self,
            id: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            partnerId: int = NotImplemented,
            providerType: KalturaDistributionProviderType = NotImplemented,
            name: str = NotImplemented,
            status: KalturaDistributionProfileStatus = NotImplemented,
            submitEnabled: KalturaDistributionProfileActionStatus = NotImplemented,
            updateEnabled: KalturaDistributionProfileActionStatus = NotImplemented,
            deleteEnabled: KalturaDistributionProfileActionStatus = NotImplemented,
            reportEnabled: KalturaDistributionProfileActionStatus = NotImplemented,
            autoCreateFlavors: str = NotImplemented,
            autoCreateThumb: str = NotImplemented,
            optionalFlavorParamsIds: str = NotImplemented,
            requiredFlavorParamsIds: str = NotImplemented,
            optionalThumbDimensions: List[KalturaDistributionThumbDimensions] = NotImplemented,
            requiredThumbDimensions: List[KalturaDistributionThumbDimensions] = NotImplemented,
            optionalAssetDistributionRules: List[KalturaAssetDistributionRule] = NotImplemented,
            requiredAssetDistributionRules: List[KalturaAssetDistributionRule] = NotImplemented,
            sunriseDefaultOffset: int = NotImplemented,
            sunsetDefaultOffset: int = NotImplemented,
            recommendedStorageProfileForDownload: int = NotImplemented,
            recommendedDcForDownload: int = NotImplemented,
            recommendedDcForExecute: int = NotImplemented,
            distributeTrigger: KalturaDistributeTrigger = NotImplemented,
            supportImageEntry: bool = NotImplemented,
            fieldConfigArray: List[KalturaDistributionFieldConfig] = NotImplemented,
            itemXpathsToExtend: List[KalturaExtendingItemMrssParameter] = NotImplemented,
            useCategoryEntries: bool = NotImplemented,
            protocol: KalturaDistributionProtocol = NotImplemented,
            host: str = NotImplemented,
            port: int = NotImplemented,
            basePath: str = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented,
            passphrase: str = NotImplemented,
            sftpPublicKey: str = NotImplemented,
            sftpPrivateKey: str = NotImplemented,
            disableMetadata: bool = NotImplemented,
            metadataXslt: str = NotImplemented,
            metadataFilenameXslt: str = NotImplemented,
            flavorAssetFilenameXslt: str = NotImplemented,
            thumbnailAssetFilenameXslt: str = NotImplemented,
            assetFilenameXslt: str = NotImplemented,
            asperaPublicKey: str = NotImplemented,
            asperaPrivateKey: str = NotImplemented,
            sendMetadataAfterAssets: bool = NotImplemented): ...

    def getProtocol(self) -> KalturaDistributionProtocol: ...
    def setProtocol(self, newProtocol: KalturaDistributionProtocol) -> None: ...
    def getHost(self) -> str: ...
    def setHost(self, newHost: str) -> None: ...
    def getPort(self) -> int: ...
    def setPort(self, newPort: int) -> None: ...
    def getBasePath(self) -> str: ...
    def setBasePath(self, newBasePath: str) -> None: ...
    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...
    def getPassphrase(self) -> str: ...
    def setPassphrase(self, newPassphrase: str) -> None: ...
    def getSftpPublicKey(self) -> str: ...
    def setSftpPublicKey(self, newSftpPublicKey: str) -> None: ...
    def getSftpPrivateKey(self) -> str: ...
    def setSftpPrivateKey(self, newSftpPrivateKey: str) -> None: ...
    def getDisableMetadata(self) -> bool: ...
    def setDisableMetadata(self, newDisableMetadata: bool) -> None: ...
    def getMetadataXslt(self) -> str: ...
    def setMetadataXslt(self, newMetadataXslt: str) -> None: ...
    def getMetadataFilenameXslt(self) -> str: ...
    def setMetadataFilenameXslt(self, newMetadataFilenameXslt: str) -> None: ...
    def getFlavorAssetFilenameXslt(self) -> str: ...
    def setFlavorAssetFilenameXslt(self, newFlavorAssetFilenameXslt: str) -> None: ...
    def getThumbnailAssetFilenameXslt(self) -> str: ...
    def setThumbnailAssetFilenameXslt(self, newThumbnailAssetFilenameXslt: str) -> None: ...
    def getAssetFilenameXslt(self) -> str: ...
    def setAssetFilenameXslt(self, newAssetFilenameXslt: str) -> None: ...
    def getAsperaPublicKey(self) -> str: ...
    def setAsperaPublicKey(self, newAsperaPublicKey: str) -> None: ...
    def getAsperaPrivateKey(self) -> str: ...
    def setAsperaPrivateKey(self, newAsperaPrivateKey: str) -> None: ...
    def getSendMetadataAfterAssets(self) -> bool: ...
    def setSendMetadataAfterAssets(self, newSendMetadataAfterAssets: bool) -> None: ...

class KalturaFtpScheduledDistributionProvider(KalturaFtpDistributionProvider):
    def __init__(self,
            type: KalturaDistributionProviderType = NotImplemented,
            name: str = NotImplemented,
            scheduleUpdateEnabled: bool = NotImplemented,
            availabilityUpdateEnabled: bool = NotImplemented,
            deleteInsteadUpdate: bool = NotImplemented,
            intervalBeforeSunrise: int = NotImplemented,
            intervalBeforeSunset: int = NotImplemented,
            updateRequiredEntryFields: str = NotImplemented,
            updateRequiredMetadataXPaths: str = NotImplemented): ...
        pass

class KalturaFtpDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaFtpDistributionProviderFilter(KalturaFtpDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaFtpDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaDistributionProfileStatus = NotImplemented,
            statusIn: str = NotImplemented): ...
        pass

class KalturaFtpScheduledDistributionProviderBaseFilter(KalturaFtpDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaFtpDistributionProfileFilter(KalturaFtpDistributionProfileBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaDistributionProfileStatus = NotImplemented,
            statusIn: str = NotImplemented): ...
        pass

class KalturaFtpScheduledDistributionProviderFilter(KalturaFtpScheduledDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaFtpDistributionClientPluginServicesProxy: