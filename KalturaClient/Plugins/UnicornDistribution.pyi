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

class KalturaUnicornDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaUnicornDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaUnicornDistributionProvider(KalturaDistributionProvider):
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

class KalturaUnicornDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    catalogGuid: str
    title: str
    mediaChanged: bool
    flavorAssetVersion: str
    notificationBaseUrl: str
    def __init__(self,
            fieldValues: str = NotImplemented,
            catalogGuid: str = NotImplemented,
            title: str = NotImplemented,
            mediaChanged: bool = NotImplemented,
            flavorAssetVersion: str = NotImplemented,
            notificationBaseUrl: str = NotImplemented): ...

    def getCatalogGuid(self) -> str: ...
    def setCatalogGuid(self, newCatalogGuid: str) -> None: ...
    def getTitle(self) -> str: ...
    def setTitle(self, newTitle: str) -> None: ...
    def getMediaChanged(self) -> bool: ...
    def setMediaChanged(self, newMediaChanged: bool) -> None: ...
    def getFlavorAssetVersion(self) -> str: ...
    def setFlavorAssetVersion(self, newFlavorAssetVersion: str) -> None: ...
    def getNotificationBaseUrl(self) -> str: ...
    def setNotificationBaseUrl(self, newNotificationBaseUrl: str) -> None: ...

class KalturaUnicornDistributionProfile(KalturaConfigurableDistributionProfile):
    username: str
    password: str
    domainName: str
    channelGuid: str
    apiHostUrl: str
    domainGuid: str
    adFreeApplicationGuid: str
    remoteAssetParamsId: int
    storageProfileId: str
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
            username: str = NotImplemented,
            password: str = NotImplemented,
            domainName: str = NotImplemented,
            channelGuid: str = NotImplemented,
            apiHostUrl: str = NotImplemented,
            domainGuid: str = NotImplemented,
            adFreeApplicationGuid: str = NotImplemented,
            remoteAssetParamsId: int = NotImplemented,
            storageProfileId: str = NotImplemented): ...

    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...
    def getDomainName(self) -> str: ...
    def setDomainName(self, newDomainName: str) -> None: ...
    def getChannelGuid(self) -> str: ...
    def setChannelGuid(self, newChannelGuid: str) -> None: ...
    def getApiHostUrl(self) -> str: ...
    def setApiHostUrl(self, newApiHostUrl: str) -> None: ...
    def getDomainGuid(self) -> str: ...
    def setDomainGuid(self, newDomainGuid: str) -> None: ...
    def getAdFreeApplicationGuid(self) -> str: ...
    def setAdFreeApplicationGuid(self, newAdFreeApplicationGuid: str) -> None: ...
    def getRemoteAssetParamsId(self) -> int: ...
    def setRemoteAssetParamsId(self, newRemoteAssetParamsId: int) -> None: ...
    def getStorageProfileId(self) -> str: ...
    def setStorageProfileId(self, newStorageProfileId: str) -> None: ...

class KalturaUnicornDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaUnicornDistributionProviderFilter(KalturaUnicornDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaUnicornDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaUnicornDistributionProfileFilter(KalturaUnicornDistributionProfileBaseFilter):
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

class KalturaUnicornService(KalturaServiceBase):
    def notify(self, id: int) -> None: ...

class KalturaUnicornDistributionClientPluginServicesProxy:
    unicorn: KalturaUnicornService