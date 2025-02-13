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

class KalturaUverseDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaUverseDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaUverseDistributionProvider(KalturaDistributionProvider):
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

class KalturaUverseDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    localAssetFilePath: str
    remoteAssetUrl: str
    remoteAssetFileName: str
    def __init__(self,
            fieldValues: str = NotImplemented,
            localAssetFilePath: str = NotImplemented,
            remoteAssetUrl: str = NotImplemented,
            remoteAssetFileName: str = NotImplemented): ...

    def getLocalAssetFilePath(self) -> str: ...
    def setLocalAssetFilePath(self, newLocalAssetFilePath: str) -> None: ...
    def getRemoteAssetUrl(self) -> str: ...
    def setRemoteAssetUrl(self, newRemoteAssetUrl: str) -> None: ...
    def getRemoteAssetFileName(self) -> str: ...
    def setRemoteAssetFileName(self, newRemoteAssetFileName: str) -> None: ...

class KalturaUverseDistributionProfile(KalturaConfigurableDistributionProfile):
    feedUrl: str
    channelTitle: str
    channelLink: str
    channelDescription: str
    channelLanguage: str
    channelCopyright: str
    channelImageTitle: str
    channelImageUrl: str
    channelImageLink: str
    ftpHost: str
    ftpLogin: str
    ftpPassword: str
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
            channelTitle: str = NotImplemented,
            channelLink: str = NotImplemented,
            channelDescription: str = NotImplemented,
            channelLanguage: str = NotImplemented,
            channelCopyright: str = NotImplemented,
            channelImageTitle: str = NotImplemented,
            channelImageUrl: str = NotImplemented,
            channelImageLink: str = NotImplemented,
            ftpHost: str = NotImplemented,
            ftpLogin: str = NotImplemented,
            ftpPassword: str = NotImplemented): ...

    def getFeedUrl(self) -> str: ...
    def getChannelTitle(self) -> str: ...
    def setChannelTitle(self, newChannelTitle: str) -> None: ...
    def getChannelLink(self) -> str: ...
    def setChannelLink(self, newChannelLink: str) -> None: ...
    def getChannelDescription(self) -> str: ...
    def setChannelDescription(self, newChannelDescription: str) -> None: ...
    def getChannelLanguage(self) -> str: ...
    def setChannelLanguage(self, newChannelLanguage: str) -> None: ...
    def getChannelCopyright(self) -> str: ...
    def setChannelCopyright(self, newChannelCopyright: str) -> None: ...
    def getChannelImageTitle(self) -> str: ...
    def setChannelImageTitle(self, newChannelImageTitle: str) -> None: ...
    def getChannelImageUrl(self) -> str: ...
    def setChannelImageUrl(self, newChannelImageUrl: str) -> None: ...
    def getChannelImageLink(self) -> str: ...
    def setChannelImageLink(self, newChannelImageLink: str) -> None: ...
    def getFtpHost(self) -> str: ...
    def setFtpHost(self, newFtpHost: str) -> None: ...
    def getFtpLogin(self) -> str: ...
    def setFtpLogin(self, newFtpLogin: str) -> None: ...
    def getFtpPassword(self) -> str: ...
    def setFtpPassword(self, newFtpPassword: str) -> None: ...

class KalturaUverseDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaUverseDistributionProviderFilter(KalturaUverseDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaUverseDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaUverseDistributionProfileFilter(KalturaUverseDistributionProfileBaseFilter):
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

class KalturaUverseService(KalturaServiceBase):
    def getFeed(self, distributionProfileId: int, hash: str) -> IO[Any]: ...

class KalturaUverseDistributionClientPluginServicesProxy:
    uverse: KalturaUverseService