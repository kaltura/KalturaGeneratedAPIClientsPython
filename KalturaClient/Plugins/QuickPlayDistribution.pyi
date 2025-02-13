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

class KalturaQuickPlayDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaQuickPlayDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaQuickPlayDistributionProvider(KalturaDistributionProvider):
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

class KalturaQuickPlayDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    xml: str
    videoFilePaths: List[KalturaString]
    thumbnailFilePaths: List[KalturaString]
    def __init__(self,
            fieldValues: str = NotImplemented,
            xml: str = NotImplemented,
            videoFilePaths: List[KalturaString] = NotImplemented,
            thumbnailFilePaths: List[KalturaString] = NotImplemented): ...

    def getXml(self) -> str: ...
    def setXml(self, newXml: str) -> None: ...
    def getVideoFilePaths(self) -> List[KalturaString]: ...
    def setVideoFilePaths(self, newVideoFilePaths: List[KalturaString]) -> None: ...
    def getThumbnailFilePaths(self) -> List[KalturaString]: ...
    def setThumbnailFilePaths(self, newThumbnailFilePaths: List[KalturaString]) -> None: ...

class KalturaQuickPlayDistributionProfile(KalturaConfigurableDistributionProfile):
    sftpHost: str
    sftpLogin: str
    sftpPass: str
    sftpBasePath: str
    channelTitle: str
    channelLink: str
    channelDescription: str
    channelManagingEditor: str
    channelLanguage: str
    channelImageTitle: str
    channelImageWidth: str
    channelImageHeight: str
    channelImageLink: str
    channelImageUrl: str
    channelCopyright: str
    channelGenerator: str
    channelRating: str
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
            sftpHost: str = NotImplemented,
            sftpLogin: str = NotImplemented,
            sftpPass: str = NotImplemented,
            sftpBasePath: str = NotImplemented,
            channelTitle: str = NotImplemented,
            channelLink: str = NotImplemented,
            channelDescription: str = NotImplemented,
            channelManagingEditor: str = NotImplemented,
            channelLanguage: str = NotImplemented,
            channelImageTitle: str = NotImplemented,
            channelImageWidth: str = NotImplemented,
            channelImageHeight: str = NotImplemented,
            channelImageLink: str = NotImplemented,
            channelImageUrl: str = NotImplemented,
            channelCopyright: str = NotImplemented,
            channelGenerator: str = NotImplemented,
            channelRating: str = NotImplemented): ...

    def getSftpHost(self) -> str: ...
    def setSftpHost(self, newSftpHost: str) -> None: ...
    def getSftpLogin(self) -> str: ...
    def setSftpLogin(self, newSftpLogin: str) -> None: ...
    def getSftpPass(self) -> str: ...
    def setSftpPass(self, newSftpPass: str) -> None: ...
    def getSftpBasePath(self) -> str: ...
    def setSftpBasePath(self, newSftpBasePath: str) -> None: ...
    def getChannelTitle(self) -> str: ...
    def setChannelTitle(self, newChannelTitle: str) -> None: ...
    def getChannelLink(self) -> str: ...
    def setChannelLink(self, newChannelLink: str) -> None: ...
    def getChannelDescription(self) -> str: ...
    def setChannelDescription(self, newChannelDescription: str) -> None: ...
    def getChannelManagingEditor(self) -> str: ...
    def setChannelManagingEditor(self, newChannelManagingEditor: str) -> None: ...
    def getChannelLanguage(self) -> str: ...
    def setChannelLanguage(self, newChannelLanguage: str) -> None: ...
    def getChannelImageTitle(self) -> str: ...
    def setChannelImageTitle(self, newChannelImageTitle: str) -> None: ...
    def getChannelImageWidth(self) -> str: ...
    def setChannelImageWidth(self, newChannelImageWidth: str) -> None: ...
    def getChannelImageHeight(self) -> str: ...
    def setChannelImageHeight(self, newChannelImageHeight: str) -> None: ...
    def getChannelImageLink(self) -> str: ...
    def setChannelImageLink(self, newChannelImageLink: str) -> None: ...
    def getChannelImageUrl(self) -> str: ...
    def setChannelImageUrl(self, newChannelImageUrl: str) -> None: ...
    def getChannelCopyright(self) -> str: ...
    def setChannelCopyright(self, newChannelCopyright: str) -> None: ...
    def getChannelGenerator(self) -> str: ...
    def setChannelGenerator(self, newChannelGenerator: str) -> None: ...
    def getChannelRating(self) -> str: ...
    def setChannelRating(self, newChannelRating: str) -> None: ...

class KalturaQuickPlayDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaQuickPlayDistributionProviderFilter(KalturaQuickPlayDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaQuickPlayDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaQuickPlayDistributionProfileFilter(KalturaQuickPlayDistributionProfileBaseFilter):
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

class KalturaQuickPlayDistributionClientPluginServicesProxy: