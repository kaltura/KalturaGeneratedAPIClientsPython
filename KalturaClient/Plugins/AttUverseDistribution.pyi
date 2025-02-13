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

class KalturaAttUverseDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaAttUverseDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaAttUverseDistributionFile(KalturaObjectBase):
    remoteFilename: str
    localFilePath: str
    assetType: KalturaAssetType
    assetId: str
    def __init__(self,
            remoteFilename: str = NotImplemented,
            localFilePath: str = NotImplemented,
            assetType: KalturaAssetType = NotImplemented,
            assetId: str = NotImplemented): ...

    def getRemoteFilename(self) -> str: ...
    def setRemoteFilename(self, newRemoteFilename: str) -> None: ...
    def getLocalFilePath(self) -> str: ...
    def setLocalFilePath(self, newLocalFilePath: str) -> None: ...
    def getAssetType(self) -> KalturaAssetType: ...
    def setAssetType(self, newAssetType: KalturaAssetType) -> None: ...
    def getAssetId(self) -> str: ...
    def setAssetId(self, newAssetId: str) -> None: ...

class KalturaAttUverseDistributionProvider(KalturaDistributionProvider):
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

class KalturaAttUverseDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    filesForDistribution: List[KalturaAttUverseDistributionFile]
    remoteAssetFileUrls: str
    remoteThumbnailFileUrls: str
    remoteCaptionFileUrls: str
    def __init__(self,
            fieldValues: str = NotImplemented,
            filesForDistribution: List[KalturaAttUverseDistributionFile] = NotImplemented,
            remoteAssetFileUrls: str = NotImplemented,
            remoteThumbnailFileUrls: str = NotImplemented,
            remoteCaptionFileUrls: str = NotImplemented): ...

    def getFilesForDistribution(self) -> List[KalturaAttUverseDistributionFile]: ...
    def setFilesForDistribution(self, newFilesForDistribution: List[KalturaAttUverseDistributionFile]) -> None: ...
    def getRemoteAssetFileUrls(self) -> str: ...
    def setRemoteAssetFileUrls(self, newRemoteAssetFileUrls: str) -> None: ...
    def getRemoteThumbnailFileUrls(self) -> str: ...
    def setRemoteThumbnailFileUrls(self, newRemoteThumbnailFileUrls: str) -> None: ...
    def getRemoteCaptionFileUrls(self) -> str: ...
    def setRemoteCaptionFileUrls(self, newRemoteCaptionFileUrls: str) -> None: ...

class KalturaAttUverseDistributionProfile(KalturaConfigurableDistributionProfile):
    feedUrl: str
    ftpHost: str
    ftpUsername: str
    ftpPassword: str
    ftpPath: str
    channelTitle: str
    flavorAssetFilenameXslt: str
    thumbnailAssetFilenameXslt: str
    assetFilenameXslt: str
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
            feedUrl: str = NotImplemented,
            ftpHost: str = NotImplemented,
            ftpUsername: str = NotImplemented,
            ftpPassword: str = NotImplemented,
            ftpPath: str = NotImplemented,
            channelTitle: str = NotImplemented,
            flavorAssetFilenameXslt: str = NotImplemented,
            thumbnailAssetFilenameXslt: str = NotImplemented,
            assetFilenameXslt: str = NotImplemented): ...

    def getFeedUrl(self) -> str: ...
    def getFtpHost(self) -> str: ...
    def setFtpHost(self, newFtpHost: str) -> None: ...
    def getFtpUsername(self) -> str: ...
    def setFtpUsername(self, newFtpUsername: str) -> None: ...
    def getFtpPassword(self) -> str: ...
    def setFtpPassword(self, newFtpPassword: str) -> None: ...
    def getFtpPath(self) -> str: ...
    def setFtpPath(self, newFtpPath: str) -> None: ...
    def getChannelTitle(self) -> str: ...
    def setChannelTitle(self, newChannelTitle: str) -> None: ...
    def getFlavorAssetFilenameXslt(self) -> str: ...
    def setFlavorAssetFilenameXslt(self, newFlavorAssetFilenameXslt: str) -> None: ...
    def getThumbnailAssetFilenameXslt(self) -> str: ...
    def setThumbnailAssetFilenameXslt(self, newThumbnailAssetFilenameXslt: str) -> None: ...
    def getAssetFilenameXslt(self) -> str: ...
    def setAssetFilenameXslt(self, newAssetFilenameXslt: str) -> None: ...

class KalturaAttUverseDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaAttUverseDistributionProviderFilter(KalturaAttUverseDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaAttUverseDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaAttUverseDistributionProfileFilter(KalturaAttUverseDistributionProfileBaseFilter):
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

class KalturaAttUverseService(KalturaServiceBase):
    def getFeed(self, distributionProfileId: int, hash: str) -> IO[Any]: ...

class KalturaAttUverseDistributionClientPluginServicesProxy:
    attUverse: KalturaAttUverseService