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

class KalturaMsnDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaMsnDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaMsnDistributionProvider(KalturaDistributionProvider):
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

class KalturaMsnDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    xml: str
    def __init__(self,
            fieldValues: str = NotImplemented,
            xml: str = NotImplemented): ...

    def getXml(self) -> str: ...
    def setXml(self, newXml: str) -> None: ...

class KalturaMsnDistributionProfile(KalturaConfigurableDistributionProfile):
    username: str
    password: str
    domain: str
    csId: str
    source: str
    sourceFriendlyName: str
    pageGroup: str
    sourceFlavorParamsId: int
    wmvFlavorParamsId: int
    flvFlavorParamsId: int
    slFlavorParamsId: int
    slHdFlavorParamsId: int
    msnvideoCat: str
    msnvideoTop: str
    msnvideoTopCat: str
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
            domain: str = NotImplemented,
            csId: str = NotImplemented,
            source: str = NotImplemented,
            sourceFriendlyName: str = NotImplemented,
            pageGroup: str = NotImplemented,
            sourceFlavorParamsId: int = NotImplemented,
            wmvFlavorParamsId: int = NotImplemented,
            flvFlavorParamsId: int = NotImplemented,
            slFlavorParamsId: int = NotImplemented,
            slHdFlavorParamsId: int = NotImplemented,
            msnvideoCat: str = NotImplemented,
            msnvideoTop: str = NotImplemented,
            msnvideoTopCat: str = NotImplemented): ...

    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...
    def getDomain(self) -> str: ...
    def setDomain(self, newDomain: str) -> None: ...
    def getCsId(self) -> str: ...
    def setCsId(self, newCsId: str) -> None: ...
    def getSource(self) -> str: ...
    def setSource(self, newSource: str) -> None: ...
    def getSourceFriendlyName(self) -> str: ...
    def setSourceFriendlyName(self, newSourceFriendlyName: str) -> None: ...
    def getPageGroup(self) -> str: ...
    def setPageGroup(self, newPageGroup: str) -> None: ...
    def getSourceFlavorParamsId(self) -> int: ...
    def setSourceFlavorParamsId(self, newSourceFlavorParamsId: int) -> None: ...
    def getWmvFlavorParamsId(self) -> int: ...
    def setWmvFlavorParamsId(self, newWmvFlavorParamsId: int) -> None: ...
    def getFlvFlavorParamsId(self) -> int: ...
    def setFlvFlavorParamsId(self, newFlvFlavorParamsId: int) -> None: ...
    def getSlFlavorParamsId(self) -> int: ...
    def setSlFlavorParamsId(self, newSlFlavorParamsId: int) -> None: ...
    def getSlHdFlavorParamsId(self) -> int: ...
    def setSlHdFlavorParamsId(self, newSlHdFlavorParamsId: int) -> None: ...
    def getMsnvideoCat(self) -> str: ...
    def setMsnvideoCat(self, newMsnvideoCat: str) -> None: ...
    def getMsnvideoTop(self) -> str: ...
    def setMsnvideoTop(self, newMsnvideoTop: str) -> None: ...
    def getMsnvideoTopCat(self) -> str: ...
    def setMsnvideoTopCat(self, newMsnvideoTopCat: str) -> None: ...

class KalturaMsnDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaMsnDistributionProviderFilter(KalturaMsnDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaMsnDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaMsnDistributionProfileFilter(KalturaMsnDistributionProfileBaseFilter):
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

class KalturaMsnDistributionClientPluginServicesProxy: