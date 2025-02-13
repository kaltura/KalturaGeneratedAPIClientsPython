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
from .CuePoint import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaFreewheelGenericDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaFreewheelGenericDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaFreewheelGenericDistributionProvider(KalturaDistributionProvider):
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

class KalturaFreewheelGenericDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    videoAssetFilePaths: List[KalturaString]
    thumbAssetFilePath: str
    cuePoints: List[KalturaCuePoint]
    def __init__(self,
            fieldValues: str = NotImplemented,
            videoAssetFilePaths: List[KalturaString] = NotImplemented,
            thumbAssetFilePath: str = NotImplemented,
            cuePoints: List[KalturaCuePoint] = NotImplemented): ...

    def getVideoAssetFilePaths(self) -> List[KalturaString]: ...
    def setVideoAssetFilePaths(self, newVideoAssetFilePaths: List[KalturaString]) -> None: ...
    def getThumbAssetFilePath(self) -> str: ...
    def setThumbAssetFilePath(self, newThumbAssetFilePath: str) -> None: ...
    def getCuePoints(self) -> List[KalturaCuePoint]: ...
    def setCuePoints(self, newCuePoints: List[KalturaCuePoint]) -> None: ...

class KalturaFreewheelGenericDistributionProfile(KalturaConfigurableDistributionProfile):
    apikey: str
    email: str
    sftpPass: str
    sftpLogin: str
    contentOwner: str
    upstreamVideoId: str
    upstreamNetworkName: str
    upstreamNetworkId: str
    categoryId: str
    replaceGroup: bool
    replaceAirDates: bool
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
            apikey: str = NotImplemented,
            email: str = NotImplemented,
            sftpPass: str = NotImplemented,
            sftpLogin: str = NotImplemented,
            contentOwner: str = NotImplemented,
            upstreamVideoId: str = NotImplemented,
            upstreamNetworkName: str = NotImplemented,
            upstreamNetworkId: str = NotImplemented,
            categoryId: str = NotImplemented,
            replaceGroup: bool = NotImplemented,
            replaceAirDates: bool = NotImplemented): ...

    def getApikey(self) -> str: ...
    def setApikey(self, newApikey: str) -> None: ...
    def getEmail(self) -> str: ...
    def setEmail(self, newEmail: str) -> None: ...
    def getSftpPass(self) -> str: ...
    def setSftpPass(self, newSftpPass: str) -> None: ...
    def getSftpLogin(self) -> str: ...
    def setSftpLogin(self, newSftpLogin: str) -> None: ...
    def getContentOwner(self) -> str: ...
    def setContentOwner(self, newContentOwner: str) -> None: ...
    def getUpstreamVideoId(self) -> str: ...
    def setUpstreamVideoId(self, newUpstreamVideoId: str) -> None: ...
    def getUpstreamNetworkName(self) -> str: ...
    def setUpstreamNetworkName(self, newUpstreamNetworkName: str) -> None: ...
    def getUpstreamNetworkId(self) -> str: ...
    def setUpstreamNetworkId(self, newUpstreamNetworkId: str) -> None: ...
    def getCategoryId(self) -> str: ...
    def setCategoryId(self, newCategoryId: str) -> None: ...
    def getReplaceGroup(self) -> bool: ...
    def setReplaceGroup(self, newReplaceGroup: bool) -> None: ...
    def getReplaceAirDates(self) -> bool: ...
    def setReplaceAirDates(self, newReplaceAirDates: bool) -> None: ...

class KalturaFreewheelGenericDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaFreewheelGenericDistributionProviderFilter(KalturaFreewheelGenericDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaFreewheelGenericDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaFreewheelGenericDistributionProfileFilter(KalturaFreewheelGenericDistributionProfileBaseFilter):
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

class KalturaFreewheelGenericDistributionClientPluginServicesProxy: