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

class KalturaYouTubeApiDistributionCaptionAction(object):
    UPDATE_ACTION = 1
    SUBMIT_ACTION = 2
    DELETE_ACTION = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaYoutubeApiDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaYoutubeApiDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaYouTubeApiCaptionDistributionInfo(KalturaObjectBase):
    language: str
    label: str
    filePath: str
    remoteId: str
    action: KalturaYouTubeApiDistributionCaptionAction
    version: str
    assetId: str
    def __init__(self,
            language: str = NotImplemented,
            label: str = NotImplemented,
            filePath: str = NotImplemented,
            remoteId: str = NotImplemented,
            action: KalturaYouTubeApiDistributionCaptionAction = NotImplemented,
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
    def getAction(self) -> KalturaYouTubeApiDistributionCaptionAction: ...
    def setAction(self, newAction: KalturaYouTubeApiDistributionCaptionAction) -> None: ...
    def getVersion(self) -> str: ...
    def setVersion(self, newVersion: str) -> None: ...
    def getAssetId(self) -> str: ...
    def setAssetId(self, newAssetId: str) -> None: ...

class KalturaYoutubeApiDistributionProvider(KalturaDistributionProvider):
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

class KalturaYoutubeApiDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    videoAssetFilePath: str
    thumbAssetFilePath: str
    captionsInfo: List[KalturaYouTubeApiCaptionDistributionInfo]
    def __init__(self,
            fieldValues: str = NotImplemented,
            videoAssetFilePath: str = NotImplemented,
            thumbAssetFilePath: str = NotImplemented,
            captionsInfo: List[KalturaYouTubeApiCaptionDistributionInfo] = NotImplemented): ...

    def getVideoAssetFilePath(self) -> str: ...
    def setVideoAssetFilePath(self, newVideoAssetFilePath: str) -> None: ...
    def getThumbAssetFilePath(self) -> str: ...
    def setThumbAssetFilePath(self, newThumbAssetFilePath: str) -> None: ...
    def getCaptionsInfo(self) -> List[KalturaYouTubeApiCaptionDistributionInfo]: ...
    def setCaptionsInfo(self, newCaptionsInfo: List[KalturaYouTubeApiCaptionDistributionInfo]) -> None: ...

class KalturaYoutubeApiDistributionProfile(KalturaConfigurableDistributionProfile):
    username: str
    defaultCategory: int
    allowComments: str
    allowEmbedding: str
    allowRatings: str
    allowResponses: str
    apiAuthorizeUrl: str
    googleClientId: str
    googleClientSecret: str
    googleTokenData: str
    assumeSuccess: bool
    privacyStatus: str
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
            defaultCategory: int = NotImplemented,
            allowComments: str = NotImplemented,
            allowEmbedding: str = NotImplemented,
            allowRatings: str = NotImplemented,
            allowResponses: str = NotImplemented,
            apiAuthorizeUrl: str = NotImplemented,
            googleClientId: str = NotImplemented,
            googleClientSecret: str = NotImplemented,
            googleTokenData: str = NotImplemented,
            assumeSuccess: bool = NotImplemented,
            privacyStatus: str = NotImplemented): ...

    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getDefaultCategory(self) -> int: ...
    def setDefaultCategory(self, newDefaultCategory: int) -> None: ...
    def getAllowComments(self) -> str: ...
    def setAllowComments(self, newAllowComments: str) -> None: ...
    def getAllowEmbedding(self) -> str: ...
    def setAllowEmbedding(self, newAllowEmbedding: str) -> None: ...
    def getAllowRatings(self) -> str: ...
    def setAllowRatings(self, newAllowRatings: str) -> None: ...
    def getAllowResponses(self) -> str: ...
    def setAllowResponses(self, newAllowResponses: str) -> None: ...
    def getApiAuthorizeUrl(self) -> str: ...
    def setApiAuthorizeUrl(self, newApiAuthorizeUrl: str) -> None: ...
    def getGoogleClientId(self) -> str: ...
    def setGoogleClientId(self, newGoogleClientId: str) -> None: ...
    def getGoogleClientSecret(self) -> str: ...
    def setGoogleClientSecret(self, newGoogleClientSecret: str) -> None: ...
    def getGoogleTokenData(self) -> str: ...
    def setGoogleTokenData(self, newGoogleTokenData: str) -> None: ...
    def getAssumeSuccess(self) -> bool: ...
    def setAssumeSuccess(self, newAssumeSuccess: bool) -> None: ...
    def getPrivacyStatus(self) -> str: ...
    def setPrivacyStatus(self, newPrivacyStatus: str) -> None: ...

class KalturaYoutubeApiDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaYoutubeApiDistributionProviderFilter(KalturaYoutubeApiDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaYoutubeApiDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaYoutubeApiDistributionProfileFilter(KalturaYoutubeApiDistributionProfileBaseFilter):
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

class KalturaYoutubeApiDistributionClientPluginServicesProxy: