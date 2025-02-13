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
from .Drm import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaWidevineRepositorySyncMode(object):
    MODIFY = 0

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaWidevineFlavorAssetOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    DELETED_AT_ASC = "+deletedAt"
    SIZE_ASC = "+size"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    DELETED_AT_DESC = "-deletedAt"
    SIZE_DESC = "-size"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaWidevineFlavorParamsOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaWidevineFlavorParamsOutputOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaWidevineProfileOrderBy(object):
    ID_ASC = "+id"
    NAME_ASC = "+name"
    ID_DESC = "-id"
    NAME_DESC = "-name"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaWidevineProfile(KalturaDrmProfile):
    key: str
    iv: str
    owner: str
    portal: str
    maxGop: int
    regServerHost: str
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            description: str = NotImplemented,
            provider: KalturaDrmProviderType = NotImplemented,
            status: KalturaDrmProfileStatus = NotImplemented,
            licenseServerUrl: str = NotImplemented,
            defaultPolicy: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            signingKey: str = NotImplemented,
            key: str = NotImplemented,
            iv: str = NotImplemented,
            owner: str = NotImplemented,
            portal: str = NotImplemented,
            maxGop: int = NotImplemented,
            regServerHost: str = NotImplemented): ...

    def getKey(self) -> str: ...
    def setKey(self, newKey: str) -> None: ...
    def getIv(self) -> str: ...
    def setIv(self, newIv: str) -> None: ...
    def getOwner(self) -> str: ...
    def setOwner(self, newOwner: str) -> None: ...
    def getPortal(self) -> str: ...
    def setPortal(self, newPortal: str) -> None: ...
    def getMaxGop(self) -> int: ...
    def setMaxGop(self, newMaxGop: int) -> None: ...
    def getRegServerHost(self) -> str: ...
    def setRegServerHost(self, newRegServerHost: str) -> None: ...

class KalturaWidevineRepositorySyncJobData(KalturaJobData):
    syncMode: KalturaWidevineRepositorySyncMode
    wvAssetIds: str
    modifiedAttributes: str
    monitorSyncCompletion: int
    def __init__(self,
            syncMode: KalturaWidevineRepositorySyncMode = NotImplemented,
            wvAssetIds: str = NotImplemented,
            modifiedAttributes: str = NotImplemented,
            monitorSyncCompletion: int = NotImplemented): ...

    def getSyncMode(self) -> KalturaWidevineRepositorySyncMode: ...
    def setSyncMode(self, newSyncMode: KalturaWidevineRepositorySyncMode) -> None: ...
    def getWvAssetIds(self) -> str: ...
    def setWvAssetIds(self, newWvAssetIds: str) -> None: ...
    def getModifiedAttributes(self) -> str: ...
    def setModifiedAttributes(self, newModifiedAttributes: str) -> None: ...
    def getMonitorSyncCompletion(self) -> int: ...
    def setMonitorSyncCompletion(self, newMonitorSyncCompletion: int) -> None: ...

class KalturaWidevineFlavorAsset(KalturaFlavorAsset):
    widevineDistributionStartDate: int
    widevineDistributionEndDate: int
    widevineAssetId: int
    def __init__(self,
            id: str = NotImplemented,
            entryId: str = NotImplemented,
            partnerId: int = NotImplemented,
            version: int = NotImplemented,
            size: int = NotImplemented,
            tags: str = NotImplemented,
            fileExt: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            deletedAt: int = NotImplemented,
            description: str = NotImplemented,
            partnerData: str = NotImplemented,
            partnerDescription: str = NotImplemented,
            actualSourceAssetParamsIds: str = NotImplemented,
            sizeInBytes: int = NotImplemented,
            flavorParamsId: int = NotImplemented,
            width: int = NotImplemented,
            height: int = NotImplemented,
            bitrate: int = NotImplemented,
            frameRate: float = NotImplemented,
            isOriginal: bool = NotImplemented,
            isWeb: bool = NotImplemented,
            containerFormat: str = NotImplemented,
            videoCodecId: str = NotImplemented,
            status: KalturaFlavorAssetStatus = NotImplemented,
            language: KalturaLanguage = NotImplemented,
            label: str = NotImplemented,
            isDefault: KalturaNullableBoolean = NotImplemented,
            widevineDistributionStartDate: int = NotImplemented,
            widevineDistributionEndDate: int = NotImplemented,
            widevineAssetId: int = NotImplemented): ...

    def getWidevineDistributionStartDate(self) -> int: ...
    def setWidevineDistributionStartDate(self, newWidevineDistributionStartDate: int) -> None: ...
    def getWidevineDistributionEndDate(self) -> int: ...
    def setWidevineDistributionEndDate(self, newWidevineDistributionEndDate: int) -> None: ...
    def getWidevineAssetId(self) -> int: ...
    def setWidevineAssetId(self, newWidevineAssetId: int) -> None: ...

class KalturaWidevineFlavorParams(KalturaFlavorParams):
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            createdAt: int = NotImplemented,
            isSystemDefault: KalturaNullableBoolean = NotImplemented,
            tags: str = NotImplemented,
            requiredPermissions: List[KalturaString] = NotImplemented,
            sourceRemoteStorageProfileId: int = NotImplemented,
            remoteStorageProfileIds: int = NotImplemented,
            mediaParserType: KalturaMediaParserType = NotImplemented,
            sourceAssetParamsIds: str = NotImplemented,
            videoCodec: KalturaVideoCodec = NotImplemented,
            videoBitrate: int = NotImplemented,
            audioCodec: KalturaAudioCodec = NotImplemented,
            audioBitrate: int = NotImplemented,
            audioChannels: int = NotImplemented,
            audioSampleRate: int = NotImplemented,
            width: int = NotImplemented,
            height: int = NotImplemented,
            frameRate: float = NotImplemented,
            gopSize: int = NotImplemented,
            conversionEngines: str = NotImplemented,
            conversionEnginesExtraParams: str = NotImplemented,
            twoPass: bool = NotImplemented,
            deinterlice: int = NotImplemented,
            rotate: int = NotImplemented,
            operators: str = NotImplemented,
            engineVersion: int = NotImplemented,
            format: KalturaContainerFormat = NotImplemented,
            aspectRatioProcessingMode: int = NotImplemented,
            forceFrameToMultiplication16: int = NotImplemented,
            isGopInSec: int = NotImplemented,
            isAvoidVideoShrinkFramesizeToSource: int = NotImplemented,
            isAvoidVideoShrinkBitrateToSource: int = NotImplemented,
            isVideoFrameRateForLowBrAppleHls: int = NotImplemented,
            multiStream: str = NotImplemented,
            anamorphicPixels: float = NotImplemented,
            isAvoidForcedKeyFrames: int = NotImplemented,
            forcedKeyFramesMode: int = NotImplemented,
            isCropIMX: int = NotImplemented,
            optimizationPolicy: int = NotImplemented,
            maxFrameRate: int = NotImplemented,
            videoConstantBitrate: int = NotImplemented,
            videoBitrateTolerance: int = NotImplemented,
            watermarkData: str = NotImplemented,
            subtitlesData: str = NotImplemented,
            cropData: str = NotImplemented,
            isEncrypted: int = NotImplemented,
            contentAwareness: float = NotImplemented,
            chunkedEncodeMode: int = NotImplemented,
            clipOffset: int = NotImplemented,
            clipDuration: int = NotImplemented): ...
        pass

class KalturaWidevineFlavorParamsOutput(KalturaFlavorParamsOutput):
    widevineDistributionStartDate: int
    widevineDistributionEndDate: int
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            createdAt: int = NotImplemented,
            isSystemDefault: KalturaNullableBoolean = NotImplemented,
            tags: str = NotImplemented,
            requiredPermissions: List[KalturaString] = NotImplemented,
            sourceRemoteStorageProfileId: int = NotImplemented,
            remoteStorageProfileIds: int = NotImplemented,
            mediaParserType: KalturaMediaParserType = NotImplemented,
            sourceAssetParamsIds: str = NotImplemented,
            videoCodec: KalturaVideoCodec = NotImplemented,
            videoBitrate: int = NotImplemented,
            audioCodec: KalturaAudioCodec = NotImplemented,
            audioBitrate: int = NotImplemented,
            audioChannels: int = NotImplemented,
            audioSampleRate: int = NotImplemented,
            width: int = NotImplemented,
            height: int = NotImplemented,
            frameRate: float = NotImplemented,
            gopSize: int = NotImplemented,
            conversionEngines: str = NotImplemented,
            conversionEnginesExtraParams: str = NotImplemented,
            twoPass: bool = NotImplemented,
            deinterlice: int = NotImplemented,
            rotate: int = NotImplemented,
            operators: str = NotImplemented,
            engineVersion: int = NotImplemented,
            format: KalturaContainerFormat = NotImplemented,
            aspectRatioProcessingMode: int = NotImplemented,
            forceFrameToMultiplication16: int = NotImplemented,
            isGopInSec: int = NotImplemented,
            isAvoidVideoShrinkFramesizeToSource: int = NotImplemented,
            isAvoidVideoShrinkBitrateToSource: int = NotImplemented,
            isVideoFrameRateForLowBrAppleHls: int = NotImplemented,
            multiStream: str = NotImplemented,
            anamorphicPixels: float = NotImplemented,
            isAvoidForcedKeyFrames: int = NotImplemented,
            forcedKeyFramesMode: int = NotImplemented,
            isCropIMX: int = NotImplemented,
            optimizationPolicy: int = NotImplemented,
            maxFrameRate: int = NotImplemented,
            videoConstantBitrate: int = NotImplemented,
            videoBitrateTolerance: int = NotImplemented,
            watermarkData: str = NotImplemented,
            subtitlesData: str = NotImplemented,
            cropData: str = NotImplemented,
            isEncrypted: int = NotImplemented,
            contentAwareness: float = NotImplemented,
            chunkedEncodeMode: int = NotImplemented,
            clipOffset: int = NotImplemented,
            clipDuration: int = NotImplemented,
            flavorParamsId: int = NotImplemented,
            commandLinesStr: str = NotImplemented,
            flavorParamsVersion: str = NotImplemented,
            flavorAssetId: str = NotImplemented,
            flavorAssetVersion: str = NotImplemented,
            readyBehavior: int = NotImplemented,
            widevineDistributionStartDate: int = NotImplemented,
            widevineDistributionEndDate: int = NotImplemented): ...

    def getWidevineDistributionStartDate(self) -> int: ...
    def setWidevineDistributionStartDate(self, newWidevineDistributionStartDate: int) -> None: ...
    def getWidevineDistributionEndDate(self) -> int: ...
    def setWidevineDistributionEndDate(self, newWidevineDistributionEndDate: int) -> None: ...

class KalturaWidevineProfileBaseFilter(KalturaDrmProfileFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            providerEqual: KalturaDrmProviderType = NotImplemented,
            providerIn: str = NotImplemented,
            statusEqual: KalturaDrmProfileStatus = NotImplemented,
            statusIn: str = NotImplemented): ...
        pass

class KalturaWidevineProfileFilter(KalturaWidevineProfileBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            providerEqual: KalturaDrmProviderType = NotImplemented,
            providerIn: str = NotImplemented,
            statusEqual: KalturaDrmProfileStatus = NotImplemented,
            statusIn: str = NotImplemented): ...
        pass

class KalturaWidevineFlavorAssetBaseFilter(KalturaFlavorAssetFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            sizeGreaterThanOrEqual: int = NotImplemented,
            sizeLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            deletedAtGreaterThanOrEqual: int = NotImplemented,
            deletedAtLessThanOrEqual: int = NotImplemented,
            typeIn: str = NotImplemented,
            flavorParamsIdEqual: int = NotImplemented,
            flavorParamsIdIn: str = NotImplemented,
            statusEqual: KalturaFlavorAssetStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented): ...
        pass

class KalturaWidevineFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            isSystemDefaultEqual: KalturaNullableBoolean = NotImplemented,
            tagsEqual: str = NotImplemented,
            formatEqual: KalturaContainerFormat = NotImplemented): ...
        pass

class KalturaWidevineFlavorAssetFilter(KalturaWidevineFlavorAssetBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            sizeGreaterThanOrEqual: int = NotImplemented,
            sizeLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            deletedAtGreaterThanOrEqual: int = NotImplemented,
            deletedAtLessThanOrEqual: int = NotImplemented,
            typeIn: str = NotImplemented,
            flavorParamsIdEqual: int = NotImplemented,
            flavorParamsIdIn: str = NotImplemented,
            statusEqual: KalturaFlavorAssetStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented): ...
        pass

class KalturaWidevineFlavorParamsFilter(KalturaWidevineFlavorParamsBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            isSystemDefaultEqual: KalturaNullableBoolean = NotImplemented,
            tagsEqual: str = NotImplemented,
            formatEqual: KalturaContainerFormat = NotImplemented): ...
        pass

class KalturaWidevineFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            isSystemDefaultEqual: KalturaNullableBoolean = NotImplemented,
            tagsEqual: str = NotImplemented,
            formatEqual: KalturaContainerFormat = NotImplemented,
            flavorParamsIdEqual: int = NotImplemented,
            flavorParamsVersionEqual: str = NotImplemented,
            flavorAssetIdEqual: str = NotImplemented,
            flavorAssetVersionEqual: str = NotImplemented): ...
        pass

class KalturaWidevineFlavorParamsOutputFilter(KalturaWidevineFlavorParamsOutputBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            isSystemDefaultEqual: KalturaNullableBoolean = NotImplemented,
            tagsEqual: str = NotImplemented,
            formatEqual: KalturaContainerFormat = NotImplemented,
            flavorParamsIdEqual: int = NotImplemented,
            flavorParamsVersionEqual: str = NotImplemented,
            flavorAssetIdEqual: str = NotImplemented,
            flavorAssetVersionEqual: str = NotImplemented): ...
        pass

class KalturaWidevineDrmService(KalturaServiceBase):
    def getLicense(self, flavorAssetId: str, referrer: str = NotImplemented) -> str: ...

class KalturaWidevineClientPluginServicesProxy:
    widevineDrm: KalturaWidevineDrmService