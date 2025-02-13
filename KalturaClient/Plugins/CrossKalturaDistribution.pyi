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

class KalturaCrossKalturaDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaCrossKalturaDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaCrossKalturaDistributionProvider(KalturaDistributionProvider):
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

class KalturaCrossKalturaDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    distributedFlavorAssets: str
    distributedThumbAssets: str
    distributedMetadata: str
    distributedCaptionAssets: str
    distributedCuePoints: str
    distributedThumbCuePoints: str
    distributedTimedThumbAssets: str
    def __init__(self,
            fieldValues: str = NotImplemented,
            distributedFlavorAssets: str = NotImplemented,
            distributedThumbAssets: str = NotImplemented,
            distributedMetadata: str = NotImplemented,
            distributedCaptionAssets: str = NotImplemented,
            distributedCuePoints: str = NotImplemented,
            distributedThumbCuePoints: str = NotImplemented,
            distributedTimedThumbAssets: str = NotImplemented): ...

    def getDistributedFlavorAssets(self) -> str: ...
    def setDistributedFlavorAssets(self, newDistributedFlavorAssets: str) -> None: ...
    def getDistributedThumbAssets(self) -> str: ...
    def setDistributedThumbAssets(self, newDistributedThumbAssets: str) -> None: ...
    def getDistributedMetadata(self) -> str: ...
    def setDistributedMetadata(self, newDistributedMetadata: str) -> None: ...
    def getDistributedCaptionAssets(self) -> str: ...
    def setDistributedCaptionAssets(self, newDistributedCaptionAssets: str) -> None: ...
    def getDistributedCuePoints(self) -> str: ...
    def setDistributedCuePoints(self, newDistributedCuePoints: str) -> None: ...
    def getDistributedThumbCuePoints(self) -> str: ...
    def setDistributedThumbCuePoints(self, newDistributedThumbCuePoints: str) -> None: ...
    def getDistributedTimedThumbAssets(self) -> str: ...
    def setDistributedTimedThumbAssets(self, newDistributedTimedThumbAssets: str) -> None: ...

class KalturaCrossKalturaDistributionProfile(KalturaConfigurableDistributionProfile):
    targetServiceUrl: str
    targetAccountId: int
    targetLoginId: str
    targetLoginPassword: str
    metadataXslt: str
    metadataXpathsTriggerUpdate: List[KalturaStringValue]
    distributeCaptions: bool
    distributeCuePoints: bool
    distributeRemoteFlavorAssetContent: bool
    distributeRemoteThumbAssetContent: bool
    distributeRemoteCaptionAssetContent: bool
    mapAccessControlProfileIds: List[KalturaKeyValue]
    mapConversionProfileIds: List[KalturaKeyValue]
    mapMetadataProfileIds: List[KalturaKeyValue]
    mapStorageProfileIds: List[KalturaKeyValue]
    mapFlavorParamsIds: List[KalturaKeyValue]
    mapThumbParamsIds: List[KalturaKeyValue]
    mapCaptionParamsIds: List[KalturaKeyValue]
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
            targetServiceUrl: str = NotImplemented,
            targetAccountId: int = NotImplemented,
            targetLoginId: str = NotImplemented,
            targetLoginPassword: str = NotImplemented,
            metadataXslt: str = NotImplemented,
            metadataXpathsTriggerUpdate: List[KalturaStringValue] = NotImplemented,
            distributeCaptions: bool = NotImplemented,
            distributeCuePoints: bool = NotImplemented,
            distributeRemoteFlavorAssetContent: bool = NotImplemented,
            distributeRemoteThumbAssetContent: bool = NotImplemented,
            distributeRemoteCaptionAssetContent: bool = NotImplemented,
            mapAccessControlProfileIds: List[KalturaKeyValue] = NotImplemented,
            mapConversionProfileIds: List[KalturaKeyValue] = NotImplemented,
            mapMetadataProfileIds: List[KalturaKeyValue] = NotImplemented,
            mapStorageProfileIds: List[KalturaKeyValue] = NotImplemented,
            mapFlavorParamsIds: List[KalturaKeyValue] = NotImplemented,
            mapThumbParamsIds: List[KalturaKeyValue] = NotImplemented,
            mapCaptionParamsIds: List[KalturaKeyValue] = NotImplemented): ...

    def getTargetServiceUrl(self) -> str: ...
    def setTargetServiceUrl(self, newTargetServiceUrl: str) -> None: ...
    def getTargetAccountId(self) -> int: ...
    def setTargetAccountId(self, newTargetAccountId: int) -> None: ...
    def getTargetLoginId(self) -> str: ...
    def setTargetLoginId(self, newTargetLoginId: str) -> None: ...
    def getTargetLoginPassword(self) -> str: ...
    def setTargetLoginPassword(self, newTargetLoginPassword: str) -> None: ...
    def getMetadataXslt(self) -> str: ...
    def setMetadataXslt(self, newMetadataXslt: str) -> None: ...
    def getMetadataXpathsTriggerUpdate(self) -> List[KalturaStringValue]: ...
    def setMetadataXpathsTriggerUpdate(self, newMetadataXpathsTriggerUpdate: List[KalturaStringValue]) -> None: ...
    def getDistributeCaptions(self) -> bool: ...
    def setDistributeCaptions(self, newDistributeCaptions: bool) -> None: ...
    def getDistributeCuePoints(self) -> bool: ...
    def setDistributeCuePoints(self, newDistributeCuePoints: bool) -> None: ...
    def getDistributeRemoteFlavorAssetContent(self) -> bool: ...
    def setDistributeRemoteFlavorAssetContent(self, newDistributeRemoteFlavorAssetContent: bool) -> None: ...
    def getDistributeRemoteThumbAssetContent(self) -> bool: ...
    def setDistributeRemoteThumbAssetContent(self, newDistributeRemoteThumbAssetContent: bool) -> None: ...
    def getDistributeRemoteCaptionAssetContent(self) -> bool: ...
    def setDistributeRemoteCaptionAssetContent(self, newDistributeRemoteCaptionAssetContent: bool) -> None: ...
    def getMapAccessControlProfileIds(self) -> List[KalturaKeyValue]: ...
    def setMapAccessControlProfileIds(self, newMapAccessControlProfileIds: List[KalturaKeyValue]) -> None: ...
    def getMapConversionProfileIds(self) -> List[KalturaKeyValue]: ...
    def setMapConversionProfileIds(self, newMapConversionProfileIds: List[KalturaKeyValue]) -> None: ...
    def getMapMetadataProfileIds(self) -> List[KalturaKeyValue]: ...
    def setMapMetadataProfileIds(self, newMapMetadataProfileIds: List[KalturaKeyValue]) -> None: ...
    def getMapStorageProfileIds(self) -> List[KalturaKeyValue]: ...
    def setMapStorageProfileIds(self, newMapStorageProfileIds: List[KalturaKeyValue]) -> None: ...
    def getMapFlavorParamsIds(self) -> List[KalturaKeyValue]: ...
    def setMapFlavorParamsIds(self, newMapFlavorParamsIds: List[KalturaKeyValue]) -> None: ...
    def getMapThumbParamsIds(self) -> List[KalturaKeyValue]: ...
    def setMapThumbParamsIds(self, newMapThumbParamsIds: List[KalturaKeyValue]) -> None: ...
    def getMapCaptionParamsIds(self) -> List[KalturaKeyValue]: ...
    def setMapCaptionParamsIds(self, newMapCaptionParamsIds: List[KalturaKeyValue]) -> None: ...

class KalturaCrossKalturaDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaCrossKalturaDistributionProviderFilter(KalturaCrossKalturaDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaCrossKalturaDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaCrossKalturaDistributionProfileFilter(KalturaCrossKalturaDistributionProfileBaseFilter):
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

class KalturaCrossKalturaDistributionClientPluginServicesProxy: