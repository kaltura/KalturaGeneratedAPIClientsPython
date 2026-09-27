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

class KalturaRainFocusDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaRainFocusDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaRainFocusDistributionProvider(KalturaDistributionProvider):
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

class KalturaRainFocusDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    def __init__(self,
            fieldValues: str = NotImplemented): ...
        pass

class KalturaRainFocusDistributionProfile(KalturaConfigurableDistributionProfile):
    oauthTokenUrl: str
    videoPublishEndpointUrl: str
    oauthScope: str
    clientId: str
    clientSecretPrimary: str
    clientSecretSecondary: str
    activeSecret: str
    mediaType: int
    playerId: str
    metadataProfileId: str
    metadataFieldNames: str
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
            oauthTokenUrl: str = NotImplemented,
            videoPublishEndpointUrl: str = NotImplemented,
            oauthScope: str = NotImplemented,
            clientId: str = NotImplemented,
            clientSecretPrimary: str = NotImplemented,
            clientSecretSecondary: str = NotImplemented,
            activeSecret: str = NotImplemented,
            mediaType: int = NotImplemented,
            playerId: str = NotImplemented,
            metadataProfileId: str = NotImplemented,
            metadataFieldNames: str = NotImplemented): ...

    def getOauthTokenUrl(self) -> str: ...
    def setOauthTokenUrl(self, newOauthTokenUrl: str) -> None: ...
    def getVideoPublishEndpointUrl(self) -> str: ...
    def setVideoPublishEndpointUrl(self, newVideoPublishEndpointUrl: str) -> None: ...
    def getOauthScope(self) -> str: ...
    def setOauthScope(self, newOauthScope: str) -> None: ...
    def getClientId(self) -> str: ...
    def setClientId(self, newClientId: str) -> None: ...
    def getClientSecretPrimary(self) -> str: ...
    def setClientSecretPrimary(self, newClientSecretPrimary: str) -> None: ...
    def getClientSecretSecondary(self) -> str: ...
    def setClientSecretSecondary(self, newClientSecretSecondary: str) -> None: ...
    def getActiveSecret(self) -> str: ...
    def setActiveSecret(self, newActiveSecret: str) -> None: ...
    def getMediaType(self) -> int: ...
    def setMediaType(self, newMediaType: int) -> None: ...
    def getPlayerId(self) -> str: ...
    def setPlayerId(self, newPlayerId: str) -> None: ...
    def getMetadataProfileId(self) -> str: ...
    def setMetadataProfileId(self, newMetadataProfileId: str) -> None: ...
    def getMetadataFieldNames(self) -> str: ...
    def setMetadataFieldNames(self, newMetadataFieldNames: str) -> None: ...

class KalturaRainFocusDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaRainFocusDistributionProviderFilter(KalturaRainFocusDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaRainFocusDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaRainFocusDistributionProfileFilter(KalturaRainFocusDistributionProfileBaseFilter):
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

class KalturaRainFocusDistributionClientPluginServicesProxy: