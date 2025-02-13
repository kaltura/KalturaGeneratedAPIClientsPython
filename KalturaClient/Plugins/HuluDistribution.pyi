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

class KalturaHuluDistributionProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaHuluDistributionProviderOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaHuluDistributionProvider(KalturaDistributionProvider):
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

class KalturaHuluDistributionJobProviderData(KalturaConfigurableDistributionJobProviderData):
    videoAssetFilePath: str
    thumbAssetFilePath: str
    cuePoints: List[KalturaCuePoint]
    fileBaseName: str
    captionLocalPaths: List[KalturaString]
    def __init__(self,
            fieldValues: str = NotImplemented,
            videoAssetFilePath: str = NotImplemented,
            thumbAssetFilePath: str = NotImplemented,
            cuePoints: List[KalturaCuePoint] = NotImplemented,
            fileBaseName: str = NotImplemented,
            captionLocalPaths: List[KalturaString] = NotImplemented): ...

    def getVideoAssetFilePath(self) -> str: ...
    def setVideoAssetFilePath(self, newVideoAssetFilePath: str) -> None: ...
    def getThumbAssetFilePath(self) -> str: ...
    def setThumbAssetFilePath(self, newThumbAssetFilePath: str) -> None: ...
    def getCuePoints(self) -> List[KalturaCuePoint]: ...
    def setCuePoints(self, newCuePoints: List[KalturaCuePoint]) -> None: ...
    def getFileBaseName(self) -> str: ...
    def setFileBaseName(self, newFileBaseName: str) -> None: ...
    def getCaptionLocalPaths(self) -> List[KalturaString]: ...
    def setCaptionLocalPaths(self, newCaptionLocalPaths: List[KalturaString]) -> None: ...

class KalturaHuluDistributionProfile(KalturaConfigurableDistributionProfile):
    sftpHost: str
    sftpLogin: str
    sftpPass: str
    seriesChannel: str
    seriesPrimaryCategory: str
    seriesAdditionalCategories: List[KalturaString]
    seasonNumber: str
    seasonSynopsis: str
    seasonTuneInInformation: str
    videoMediaType: str
    disableEpisodeNumberCustomValidation: bool
    protocol: KalturaDistributionProtocol
    asperaHost: str
    asperaLogin: str
    asperaPass: str
    port: int
    passphrase: str
    asperaPublicKey: str
    asperaPrivateKey: str
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
            sftpHost: str = NotImplemented,
            sftpLogin: str = NotImplemented,
            sftpPass: str = NotImplemented,
            seriesChannel: str = NotImplemented,
            seriesPrimaryCategory: str = NotImplemented,
            seriesAdditionalCategories: List[KalturaString] = NotImplemented,
            seasonNumber: str = NotImplemented,
            seasonSynopsis: str = NotImplemented,
            seasonTuneInInformation: str = NotImplemented,
            videoMediaType: str = NotImplemented,
            disableEpisodeNumberCustomValidation: bool = NotImplemented,
            protocol: KalturaDistributionProtocol = NotImplemented,
            asperaHost: str = NotImplemented,
            asperaLogin: str = NotImplemented,
            asperaPass: str = NotImplemented,
            port: int = NotImplemented,
            passphrase: str = NotImplemented,
            asperaPublicKey: str = NotImplemented,
            asperaPrivateKey: str = NotImplemented): ...

    def getSftpHost(self) -> str: ...
    def setSftpHost(self, newSftpHost: str) -> None: ...
    def getSftpLogin(self) -> str: ...
    def setSftpLogin(self, newSftpLogin: str) -> None: ...
    def getSftpPass(self) -> str: ...
    def setSftpPass(self, newSftpPass: str) -> None: ...
    def getSeriesChannel(self) -> str: ...
    def setSeriesChannel(self, newSeriesChannel: str) -> None: ...
    def getSeriesPrimaryCategory(self) -> str: ...
    def setSeriesPrimaryCategory(self, newSeriesPrimaryCategory: str) -> None: ...
    def getSeriesAdditionalCategories(self) -> List[KalturaString]: ...
    def setSeriesAdditionalCategories(self, newSeriesAdditionalCategories: List[KalturaString]) -> None: ...
    def getSeasonNumber(self) -> str: ...
    def setSeasonNumber(self, newSeasonNumber: str) -> None: ...
    def getSeasonSynopsis(self) -> str: ...
    def setSeasonSynopsis(self, newSeasonSynopsis: str) -> None: ...
    def getSeasonTuneInInformation(self) -> str: ...
    def setSeasonTuneInInformation(self, newSeasonTuneInInformation: str) -> None: ...
    def getVideoMediaType(self) -> str: ...
    def setVideoMediaType(self, newVideoMediaType: str) -> None: ...
    def getDisableEpisodeNumberCustomValidation(self) -> bool: ...
    def setDisableEpisodeNumberCustomValidation(self, newDisableEpisodeNumberCustomValidation: bool) -> None: ...
    def getProtocol(self) -> KalturaDistributionProtocol: ...
    def setProtocol(self, newProtocol: KalturaDistributionProtocol) -> None: ...
    def getAsperaHost(self) -> str: ...
    def setAsperaHost(self, newAsperaHost: str) -> None: ...
    def getAsperaLogin(self) -> str: ...
    def setAsperaLogin(self, newAsperaLogin: str) -> None: ...
    def getAsperaPass(self) -> str: ...
    def setAsperaPass(self, newAsperaPass: str) -> None: ...
    def getPort(self) -> int: ...
    def setPort(self, newPort: int) -> None: ...
    def getPassphrase(self) -> str: ...
    def setPassphrase(self, newPassphrase: str) -> None: ...
    def getAsperaPublicKey(self) -> str: ...
    def setAsperaPublicKey(self, newAsperaPublicKey: str) -> None: ...
    def getAsperaPrivateKey(self) -> str: ...
    def setAsperaPrivateKey(self, newAsperaPrivateKey: str) -> None: ...

class KalturaHuluDistributionProviderBaseFilter(KalturaDistributionProviderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaHuluDistributionProviderFilter(KalturaHuluDistributionProviderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            typeEqual: KalturaDistributionProviderType = NotImplemented,
            typeIn: str = NotImplemented): ...
        pass

class KalturaHuluDistributionProfileBaseFilter(KalturaConfigurableDistributionProfileFilter):
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

class KalturaHuluDistributionProfileFilter(KalturaHuluDistributionProfileBaseFilter):
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

class KalturaHuluDistributionClientPluginServicesProxy: