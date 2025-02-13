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

class KalturaFacebookDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaFacebookDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaFacebookCaptionDistributionInfo(KalturaObjectBase):
    language: str
    label: str
    filePath: str
    remoteId: str
    version: str
    assetId: str
    def __init__(self,
            language: str = NotImplemented,
            label: str = NotImplemented,
            filePath: str = NotImplemented,
            remoteId: str = NotImplemented,
            version: str = NotImplemented,
            assetId: str = NotImplemented): ...

    def getLanguage(self) -> str: ...
    def setLanguage(self, newLanguage: str) -> None: ...
    def getLabel(self) -> str: ...
    def setLabel(self, newLabel: str) -> None: ...
    def getFilePath(self) -> str: ...
    def setFilePath(self, newFilePath: str) -> None: ...
    def getRemoteId(self) -> str: ...
    def setRemoteId(self, newRemoteId: str) -> None: ...
    def getVersion(self) -> str: ...
    def setVersion(self, newVersion: str) -> None: ...
    def getAssetId(self) -> str: ...
    def setAssetId(self, newAssetId: str) -> None: ...

class KalturaFacebookDistributionProvider(KalturaDistributionProvider):
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

class KalturaFacebookDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    videoAssetFilePath: str
    thumbAssetId: str
    captionsInfo: List[KalturaFacebookCaptionDistributionInfo]
    def __init__(self,
            fieldValues: str = NotImplemented,
            videoAssetFilePath: str = NotImplemented,
            thumbAssetId: str = NotImplemented,
            captionsInfo: List[KalturaFacebookCaptionDistributionInfo] = NotImplemented): ...

    def getVideoAssetFilePath(self) -> str: ...
    def setVideoAssetFilePath(self, newVideoAssetFilePath: str) -> None: ...
    def getThumbAssetId(self) -> str: ...
    def setThumbAssetId(self, newThumbAssetId: str) -> None: ...
    def getCaptionsInfo(self) -> List[KalturaFacebookCaptionDistributionInfo]: ...
    def setCaptionsInfo(self, newCaptionsInfo: List[KalturaFacebookCaptionDistributionInfo]) -> None: ...

class KalturaFacebookDistributionProfile(KalturaConfigurableDistributionProfile):
    apiAuthorizeUrl: str
    pageId: str
    pageAccessToken: str
    userAccessToken: str
    state: str
    permissions: str
    reRequestPermissions: int
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
            apiAuthorizeUrl: str = NotImplemented,
            pageId: str = NotImplemented,
            pageAccessToken: str = NotImplemented,
            userAccessToken: str = NotImplemented,
            state: str = NotImplemented,
            permissions: str = NotImplemented,
            reRequestPermissions: int = NotImplemented): ...

    def getApiAuthorizeUrl(self) -> str: ...
    def setApiAuthorizeUrl(self, newApiAuthorizeUrl: str) -> None: ...
    def getPageId(self) -> str: ...
    def setPageId(self, newPageId: str) -> None: ...
    def getPageAccessToken(self) -> str: ...
    def setPageAccessToken(self, newPageAccessToken: str) -> None: ...
    def getUserAccessToken(self) -> str: ...
    def setUserAccessToken(self, newUserAccessToken: str) -> None: ...
    def getState(self) -> str: ...
    def setState(self, newState: str) -> None: ...
    def getPermissions(self) -> str: ...
    def setPermissions(self, newPermissions: str) -> None: ...
    def getReRequestPermissions(self) -> int: ...
    def setReRequestPermissions(self, newReRequestPermissions: int) -> None: ...

class KalturaFacebookDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaFacebookDistributionProviderFilter(KalturaFacebookDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaFacebookDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaFacebookDistributionProfileFilter(KalturaFacebookDistributionProfileBaseFilter):
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

class KalturaFacebookDistributionClientPluginServicesProxy: