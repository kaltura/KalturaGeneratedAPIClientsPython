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

class KalturaDailymotionDistributionCaptionAction(object):
    UPDATE_ACTION = 1
    SUBMIT_ACTION = 2
    DELETE_ACTION = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaDailymotionDistributionCaptionFormat(object):
    SRT = 1
    STL = 2
    TT = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaDailymotionGeoBlockingMapping(object):
    DISABLED = 0
    ACCESS_CONTROL = 1
    METADATA = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaDailymotionDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDailymotionDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDailymotionDistributionCaptionInfo(KalturaObjectBase):
    language: str
    filePath: str
    remoteId: str
    action: KalturaDailymotionDistributionCaptionAction
    version: str
    assetId: str
    format: KalturaDailymotionDistributionCaptionFormat
    def __init__(self,
            language: str = NotImplemented,
            filePath: str = NotImplemented,
            remoteId: str = NotImplemented,
            action: KalturaDailymotionDistributionCaptionAction = NotImplemented,
            version: str = NotImplemented,
            assetId: str = NotImplemented,
            format: KalturaDailymotionDistributionCaptionFormat = NotImplemented): ...

    def getLanguage(self) -> str: ...
    def setLanguage(self, newLanguage: str) -> None: ...
    def getFilePath(self) -> str: ...
    def setFilePath(self, newFilePath: str) -> None: ...
    def getRemoteId(self) -> str: ...
    def setRemoteId(self, newRemoteId: str) -> None: ...
    def getAction(self) -> KalturaDailymotionDistributionCaptionAction: ...
    def setAction(self, newAction: KalturaDailymotionDistributionCaptionAction) -> None: ...
    def getVersion(self) -> str: ...
    def setVersion(self, newVersion: str) -> None: ...
    def getAssetId(self) -> str: ...
    def setAssetId(self, newAssetId: str) -> None: ...
    def getFormat(self) -> KalturaDailymotionDistributionCaptionFormat: ...
    def setFormat(self, newFormat: KalturaDailymotionDistributionCaptionFormat) -> None: ...

class KalturaDailymotionDistributionProvider(KalturaDistributionProvider):
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

class KalturaDailymotionDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    videoAssetFilePath: str
    accessControlGeoBlockingOperation: str
    accessControlGeoBlockingCountryList: str
    captionsInfo: List[KalturaDailymotionDistributionCaptionInfo]
    def __init__(self,
            fieldValues: str = NotImplemented,
            videoAssetFilePath: str = NotImplemented,
            accessControlGeoBlockingOperation: str = NotImplemented,
            accessControlGeoBlockingCountryList: str = NotImplemented,
            captionsInfo: List[KalturaDailymotionDistributionCaptionInfo] = NotImplemented): ...

    def getVideoAssetFilePath(self) -> str: ...
    def setVideoAssetFilePath(self, newVideoAssetFilePath: str) -> None: ...
    def getAccessControlGeoBlockingOperation(self) -> str: ...
    def setAccessControlGeoBlockingOperation(self, newAccessControlGeoBlockingOperation: str) -> None: ...
    def getAccessControlGeoBlockingCountryList(self) -> str: ...
    def setAccessControlGeoBlockingCountryList(self, newAccessControlGeoBlockingCountryList: str) -> None: ...
    def getCaptionsInfo(self) -> List[KalturaDailymotionDistributionCaptionInfo]: ...
    def setCaptionsInfo(self, newCaptionsInfo: List[KalturaDailymotionDistributionCaptionInfo]) -> None: ...

class KalturaDailymotionDistributionProfile(KalturaConfigurableDistributionProfile):
    user: str
    password: str
    geoBlockingMapping: KalturaDailymotionGeoBlockingMapping
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
            user: str = NotImplemented,
            password: str = NotImplemented,
            geoBlockingMapping: KalturaDailymotionGeoBlockingMapping = NotImplemented): ...

    def getUser(self) -> str: ...
    def setUser(self, newUser: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...
    def getGeoBlockingMapping(self) -> KalturaDailymotionGeoBlockingMapping: ...
    def setGeoBlockingMapping(self, newGeoBlockingMapping: KalturaDailymotionGeoBlockingMapping) -> None: ...

class KalturaDailymotionDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaDailymotionDistributionProviderFilter(KalturaDailymotionDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaDailymotionDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaDailymotionDistributionProfileFilter(KalturaDailymotionDistributionProfileBaseFilter):
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

class KalturaDailymotionDistributionClientPluginServicesProxy: