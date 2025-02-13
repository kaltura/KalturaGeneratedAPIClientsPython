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

class KalturaVerizonVcastDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVerizonVcastDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVerizonVcastDistributionProvider(KalturaDistributionProvider):
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

class KalturaVerizonVcastDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    xml: str
    def __init__(self,
            fieldValues: str = NotImplemented,
            xml: str = NotImplemented): ...

    def getXml(self) -> str: ...
    def setXml(self, newXml: str) -> None: ...

class KalturaVerizonVcastDistributionProfile(KalturaConfigurableDistributionProfile):
    ftpHost: str
    ftpLogin: str
    ftpPass: str
    providerName: str
    providerId: str
    entitlement: str
    priority: str
    allowStreaming: str
    streamingPriceCode: str
    allowDownload: str
    downloadPriceCode: str
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
            ftpHost: str = NotImplemented,
            ftpLogin: str = NotImplemented,
            ftpPass: str = NotImplemented,
            providerName: str = NotImplemented,
            providerId: str = NotImplemented,
            entitlement: str = NotImplemented,
            priority: str = NotImplemented,
            allowStreaming: str = NotImplemented,
            streamingPriceCode: str = NotImplemented,
            allowDownload: str = NotImplemented,
            downloadPriceCode: str = NotImplemented): ...

    def getFtpHost(self) -> str: ...
    def setFtpHost(self, newFtpHost: str) -> None: ...
    def getFtpLogin(self) -> str: ...
    def setFtpLogin(self, newFtpLogin: str) -> None: ...
    def getFtpPass(self) -> str: ...
    def setFtpPass(self, newFtpPass: str) -> None: ...
    def getProviderName(self) -> str: ...
    def setProviderName(self, newProviderName: str) -> None: ...
    def getProviderId(self) -> str: ...
    def setProviderId(self, newProviderId: str) -> None: ...
    def getEntitlement(self) -> str: ...
    def setEntitlement(self, newEntitlement: str) -> None: ...
    def getPriority(self) -> str: ...
    def setPriority(self, newPriority: str) -> None: ...
    def getAllowStreaming(self) -> str: ...
    def setAllowStreaming(self, newAllowStreaming: str) -> None: ...
    def getStreamingPriceCode(self) -> str: ...
    def setStreamingPriceCode(self, newStreamingPriceCode: str) -> None: ...
    def getAllowDownload(self) -> str: ...
    def setAllowDownload(self, newAllowDownload: str) -> None: ...
    def getDownloadPriceCode(self) -> str: ...
    def setDownloadPriceCode(self, newDownloadPriceCode: str) -> None: ...

class KalturaVerizonVcastDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaVerizonVcastDistributionProviderFilter(KalturaVerizonVcastDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaVerizonVcastDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaVerizonVcastDistributionProfileFilter(KalturaVerizonVcastDistributionProfileBaseFilter):
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

class KalturaVerizonVcastDistributionClientPluginServicesProxy: