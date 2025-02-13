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
from .Caption import *
from .CuePoint import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaComcastMrssDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaComcastMrssDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaComcastMrssDistributionProvider(KalturaDistributionProvider):
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

class KalturaComcastMrssDistributionProfile(KalturaConfigurableDistributionProfile):
    metadataProfileId: int
    feedUrl: str
    feedTitle: str
    feedLink: str
    feedDescription: str
    feedLastBuildDate: str
    itemLink: str
    cPlatformTvSeries: List[KalturaKeyValue]
    cPlatformTvSeriesField: str
    shouldIncludeCuePoints: bool
    shouldIncludeCaptions: bool
    shouldAddThumbExtension: bool
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
            metadataProfileId: int = NotImplemented,
            feedUrl: str = NotImplemented,
            feedTitle: str = NotImplemented,
            feedLink: str = NotImplemented,
            feedDescription: str = NotImplemented,
            feedLastBuildDate: str = NotImplemented,
            itemLink: str = NotImplemented,
            cPlatformTvSeries: List[KalturaKeyValue] = NotImplemented,
            cPlatformTvSeriesField: str = NotImplemented,
            shouldIncludeCuePoints: bool = NotImplemented,
            shouldIncludeCaptions: bool = NotImplemented,
            shouldAddThumbExtension: bool = NotImplemented): ...

    def getMetadataProfileId(self) -> int: ...
    def setMetadataProfileId(self, newMetadataProfileId: int) -> None: ...
    def getFeedUrl(self) -> str: ...
    def getFeedTitle(self) -> str: ...
    def setFeedTitle(self, newFeedTitle: str) -> None: ...
    def getFeedLink(self) -> str: ...
    def setFeedLink(self, newFeedLink: str) -> None: ...
    def getFeedDescription(self) -> str: ...
    def setFeedDescription(self, newFeedDescription: str) -> None: ...
    def getFeedLastBuildDate(self) -> str: ...
    def setFeedLastBuildDate(self, newFeedLastBuildDate: str) -> None: ...
    def getItemLink(self) -> str: ...
    def setItemLink(self, newItemLink: str) -> None: ...
    def getCPlatformTvSeries(self) -> List[KalturaKeyValue]: ...
    def setCPlatformTvSeries(self, newCPlatformTvSeries: List[KalturaKeyValue]) -> None: ...
    def getCPlatformTvSeriesField(self) -> str: ...
    def setCPlatformTvSeriesField(self, newCPlatformTvSeriesField: str) -> None: ...
    def getShouldIncludeCuePoints(self) -> bool: ...
    def setShouldIncludeCuePoints(self, newShouldIncludeCuePoints: bool) -> None: ...
    def getShouldIncludeCaptions(self) -> bool: ...
    def setShouldIncludeCaptions(self, newShouldIncludeCaptions: bool) -> None: ...
    def getShouldAddThumbExtension(self) -> bool: ...
    def setShouldAddThumbExtension(self, newShouldAddThumbExtension: bool) -> None: ...

class KalturaComcastMrssDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaComcastMrssDistributionProviderFilter(KalturaComcastMrssDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaComcastMrssDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaComcastMrssDistributionProfileFilter(KalturaComcastMrssDistributionProfileBaseFilter):
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

class KalturaComcastMrssDistributionClientPluginServicesProxy: