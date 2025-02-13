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
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaDocumentType(object):
    DOCUMENT = 11
    SWF = 12
    PDF = 13

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaDocumentEntryOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    END_DATE_ASC = "+endDate"
    MODERATION_COUNT_ASC = "+moderationCount"
    NAME_ASC = "+name"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    RANK_ASC = "+rank"
    RECENT_ASC = "+recent"
    START_DATE_ASC = "+startDate"
    TOTAL_RANK_ASC = "+totalRank"
    UPDATED_AT_ASC = "+updatedAt"
    WEIGHT_ASC = "+weight"
    CREATED_AT_DESC = "-createdAt"
    END_DATE_DESC = "-endDate"
    MODERATION_COUNT_DESC = "-moderationCount"
    NAME_DESC = "-name"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"
    RANK_DESC = "-rank"
    RECENT_DESC = "-recent"
    START_DATE_DESC = "-startDate"
    TOTAL_RANK_DESC = "-totalRank"
    UPDATED_AT_DESC = "-updatedAt"
    WEIGHT_DESC = "-weight"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDocumentFlavorParamsOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDocumentFlavorParamsOutputOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaImageFlavorParamsOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaImageFlavorParamsOutputOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPdfFlavorParamsOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPdfFlavorParamsOutputOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaSwfFlavorParamsOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaSwfFlavorParamsOutputOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDocumentEntry(KalturaBaseEntry):
    documentType: KalturaDocumentType
    assetParamsIds: str
    def __init__(self,
            id: str = NotImplemented,
            name: str = NotImplemented,
            multiLingual_name: List[KalturaMultiLingualString] = NotImplemented,
            description: str = NotImplemented,
            multiLingual_description: List[KalturaMultiLingualString] = NotImplemented,
            partnerId: int = NotImplemented,
            userId: str = NotImplemented,
            creatorId: str = NotImplemented,
            tags: str = NotImplemented,
            multiLingual_tags: List[KalturaMultiLingualString] = NotImplemented,
            adminTags: str = NotImplemented,
            categories: str = NotImplemented,
            categoriesIds: str = NotImplemented,
            status: KalturaEntryStatus = NotImplemented,
            moderationStatus: KalturaEntryModerationStatus = NotImplemented,
            moderationCount: int = NotImplemented,
            type: KalturaEntryType = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            rank: float = NotImplemented,
            totalRank: int = NotImplemented,
            votes: int = NotImplemented,
            groupId: int = NotImplemented,
            partnerData: str = NotImplemented,
            downloadUrl: str = NotImplemented,
            searchText: str = NotImplemented,
            licenseType: KalturaLicenseType = NotImplemented,
            version: int = NotImplemented,
            thumbnailUrl: str = NotImplemented,
            accessControlId: int = NotImplemented,
            startDate: int = NotImplemented,
            endDate: int = NotImplemented,
            referenceId: str = NotImplemented,
            replacingEntryId: str = NotImplemented,
            replacedEntryId: str = NotImplemented,
            replacementStatus: KalturaEntryReplacementStatus = NotImplemented,
            partnerSortValue: int = NotImplemented,
            conversionProfileId: int = NotImplemented,
            redirectEntryId: str = NotImplemented,
            rootEntryId: str = NotImplemented,
            parentEntryId: str = NotImplemented,
            operationAttributes: List[KalturaOperationAttributes] = NotImplemented,
            entitledUsersEdit: str = NotImplemented,
            entitledUsersPublish: str = NotImplemented,
            entitledUsersView: str = NotImplemented,
            capabilities: str = NotImplemented,
            templateEntryId: str = NotImplemented,
            displayInSearch: KalturaEntryDisplayInSearchType = NotImplemented,
            application: KalturaEntryApplication = NotImplemented,
            applicationVersion: str = NotImplemented,
            blockAutoTranscript: bool = NotImplemented,
            defaultLanguage: str = NotImplemented,
            responseLanguage: str = NotImplemented,
            documentType: KalturaDocumentType = NotImplemented,
            assetParamsIds: str = NotImplemented): ...

    def getDocumentType(self) -> KalturaDocumentType: ...
    def setDocumentType(self, newDocumentType: KalturaDocumentType) -> None: ...
    def getAssetParamsIds(self) -> str: ...

class KalturaDocumentListResponse(KalturaListResponse):
    objects: List[KalturaDocumentEntry]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaDocumentEntry] = NotImplemented): ...

    def getObjects(self) -> List[KalturaDocumentEntry]: ...

class KalturaDocumentFlavorParams(KalturaFlavorParams):
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

class KalturaImageFlavorParams(KalturaFlavorParams):
    densityWidth: int
    densityHeight: int
    sizeWidth: int
    sizeHeight: int
    depth: int
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
            densityWidth: int = NotImplemented,
            densityHeight: int = NotImplemented,
            sizeWidth: int = NotImplemented,
            sizeHeight: int = NotImplemented,
            depth: int = NotImplemented): ...

    def getDensityWidth(self) -> int: ...
    def setDensityWidth(self, newDensityWidth: int) -> None: ...
    def getDensityHeight(self) -> int: ...
    def setDensityHeight(self, newDensityHeight: int) -> None: ...
    def getSizeWidth(self) -> int: ...
    def setSizeWidth(self, newSizeWidth: int) -> None: ...
    def getSizeHeight(self) -> int: ...
    def setSizeHeight(self, newSizeHeight: int) -> None: ...
    def getDepth(self) -> int: ...
    def setDepth(self, newDepth: int) -> None: ...

class KalturaPdfFlavorParams(KalturaFlavorParams):
    readonly: bool
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
            readonly: bool = NotImplemented): ...

    def getReadonly(self) -> bool: ...
    def setReadonly(self, newReadonly: bool) -> None: ...

class KalturaSwfFlavorParams(KalturaFlavorParams):
    flashVersion: int
    poly2Bitmap: bool
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
            flashVersion: int = NotImplemented,
            poly2Bitmap: bool = NotImplemented): ...

    def getFlashVersion(self) -> int: ...
    def setFlashVersion(self, newFlashVersion: int) -> None: ...
    def getPoly2Bitmap(self) -> bool: ...
    def setPoly2Bitmap(self, newPoly2Bitmap: bool) -> None: ...

class KalturaDocumentFlavorParamsOutput(KalturaFlavorParamsOutput):
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
            readyBehavior: int = NotImplemented): ...
        pass

class KalturaImageFlavorParamsOutput(KalturaFlavorParamsOutput):
    densityWidth: int
    densityHeight: int
    sizeWidth: int
    sizeHeight: int
    depth: int
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
            densityWidth: int = NotImplemented,
            densityHeight: int = NotImplemented,
            sizeWidth: int = NotImplemented,
            sizeHeight: int = NotImplemented,
            depth: int = NotImplemented): ...

    def getDensityWidth(self) -> int: ...
    def setDensityWidth(self, newDensityWidth: int) -> None: ...
    def getDensityHeight(self) -> int: ...
    def setDensityHeight(self, newDensityHeight: int) -> None: ...
    def getSizeWidth(self) -> int: ...
    def setSizeWidth(self, newSizeWidth: int) -> None: ...
    def getSizeHeight(self) -> int: ...
    def setSizeHeight(self, newSizeHeight: int) -> None: ...
    def getDepth(self) -> int: ...
    def setDepth(self, newDepth: int) -> None: ...

class KalturaPdfFlavorParamsOutput(KalturaFlavorParamsOutput):
    readonly: bool
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
            readonly: bool = NotImplemented): ...

    def getReadonly(self) -> bool: ...
    def setReadonly(self, newReadonly: bool) -> None: ...

class KalturaSwfFlavorParamsOutput(KalturaFlavorParamsOutput):
    flashVersion: int
    poly2Bitmap: bool
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
            flashVersion: int = NotImplemented,
            poly2Bitmap: bool = NotImplemented): ...

    def getFlashVersion(self) -> int: ...
    def setFlashVersion(self, newFlashVersion: int) -> None: ...
    def getPoly2Bitmap(self) -> bool: ...
    def setPoly2Bitmap(self, newPoly2Bitmap: bool) -> None: ...

class KalturaDocumentEntryBaseFilter(KalturaBaseEntryFilter):
    documentTypeEqual: KalturaDocumentType
    documentTypeIn: str
    assetParamsIdsMatchOr: str
    assetParamsIdsMatchAnd: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            nameMultiLikeOr: str = NotImplemented,
            nameMultiLikeAnd: str = NotImplemented,
            nameEqual: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            userIdNotIn: str = NotImplemented,
            creatorIdEqual: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            adminTagsLike: str = NotImplemented,
            adminTagsMultiLikeOr: str = NotImplemented,
            adminTagsMultiLikeAnd: str = NotImplemented,
            categoriesMatchAnd: str = NotImplemented,
            categoriesMatchOr: str = NotImplemented,
            categoriesNotContains: str = NotImplemented,
            categoriesIdsMatchAnd: str = NotImplemented,
            categoriesIdsMatchOr: str = NotImplemented,
            categoriesIdsNotContains: str = NotImplemented,
            categoriesIdsEmpty: KalturaNullableBoolean = NotImplemented,
            statusEqual: KalturaEntryStatus = NotImplemented,
            statusNotEqual: KalturaEntryStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            moderationStatusEqual: KalturaEntryModerationStatus = NotImplemented,
            moderationStatusNotEqual: KalturaEntryModerationStatus = NotImplemented,
            moderationStatusIn: str = NotImplemented,
            moderationStatusNotIn: str = NotImplemented,
            typeEqual: KalturaEntryType = NotImplemented,
            typeIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            rankLessThanOrEqual: float = NotImplemented,
            rankGreaterThanOrEqual: float = NotImplemented,
            totalRankLessThanOrEqual: int = NotImplemented,
            totalRankGreaterThanOrEqual: int = NotImplemented,
            groupIdEqual: int = NotImplemented,
            searchTextMatchAnd: str = NotImplemented,
            searchTextMatchOr: str = NotImplemented,
            accessControlIdEqual: int = NotImplemented,
            accessControlIdIn: str = NotImplemented,
            startDateGreaterThanOrEqual: int = NotImplemented,
            startDateLessThanOrEqual: int = NotImplemented,
            startDateGreaterThanOrEqualOrNull: int = NotImplemented,
            startDateLessThanOrEqualOrNull: int = NotImplemented,
            endDateGreaterThanOrEqual: int = NotImplemented,
            endDateLessThanOrEqual: int = NotImplemented,
            endDateGreaterThanOrEqualOrNull: int = NotImplemented,
            endDateLessThanOrEqualOrNull: int = NotImplemented,
            referenceIdEqual: str = NotImplemented,
            referenceIdIn: str = NotImplemented,
            replacingEntryIdEqual: str = NotImplemented,
            replacingEntryIdIn: str = NotImplemented,
            replacedEntryIdEqual: str = NotImplemented,
            replacedEntryIdIn: str = NotImplemented,
            replacementStatusEqual: KalturaEntryReplacementStatus = NotImplemented,
            replacementStatusIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            rootEntryIdEqual: str = NotImplemented,
            rootEntryIdIn: str = NotImplemented,
            parentEntryIdEqual: str = NotImplemented,
            entitledUsersEditMatchAnd: str = NotImplemented,
            entitledUsersEditMatchOr: str = NotImplemented,
            entitledUsersPublishMatchAnd: str = NotImplemented,
            entitledUsersPublishMatchOr: str = NotImplemented,
            entitledUsersViewMatchAnd: str = NotImplemented,
            entitledUsersViewMatchOr: str = NotImplemented,
            tagsNameMultiLikeOr: str = NotImplemented,
            tagsAdminTagsMultiLikeOr: str = NotImplemented,
            tagsAdminTagsNameMultiLikeOr: str = NotImplemented,
            tagsNameMultiLikeAnd: str = NotImplemented,
            tagsAdminTagsMultiLikeAnd: str = NotImplemented,
            tagsAdminTagsNameMultiLikeAnd: str = NotImplemented,
            displayInSearchEqual: KalturaEntryDisplayInSearchType = NotImplemented,
            displayInSearchIn: str = NotImplemented,
            freeText: str = NotImplemented,
            excludedFreeTextGroups: str = NotImplemented,
            descriptionLike: str = NotImplemented,
            isRoot: KalturaNullableBoolean = NotImplemented,
            categoriesFullNameIn: str = NotImplemented,
            categoryAncestorIdIn: str = NotImplemented,
            redirectFromEntryId: str = NotImplemented,
            conversionProfileIdEqual: int = NotImplemented,
            documentTypeEqual: KalturaDocumentType = NotImplemented,
            documentTypeIn: str = NotImplemented,
            assetParamsIdsMatchOr: str = NotImplemented,
            assetParamsIdsMatchAnd: str = NotImplemented): ...

    def getDocumentTypeEqual(self) -> KalturaDocumentType: ...
    def setDocumentTypeEqual(self, newDocumentTypeEqual: KalturaDocumentType) -> None: ...
    def getDocumentTypeIn(self) -> str: ...
    def setDocumentTypeIn(self, newDocumentTypeIn: str) -> None: ...
    def getAssetParamsIdsMatchOr(self) -> str: ...
    def setAssetParamsIdsMatchOr(self, newAssetParamsIdsMatchOr: str) -> None: ...
    def getAssetParamsIdsMatchAnd(self) -> str: ...
    def setAssetParamsIdsMatchAnd(self, newAssetParamsIdsMatchAnd: str) -> None: ...

class KalturaDocumentEntryFilter(KalturaDocumentEntryBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            nameMultiLikeOr: str = NotImplemented,
            nameMultiLikeAnd: str = NotImplemented,
            nameEqual: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            userIdNotIn: str = NotImplemented,
            creatorIdEqual: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            adminTagsLike: str = NotImplemented,
            adminTagsMultiLikeOr: str = NotImplemented,
            adminTagsMultiLikeAnd: str = NotImplemented,
            categoriesMatchAnd: str = NotImplemented,
            categoriesMatchOr: str = NotImplemented,
            categoriesNotContains: str = NotImplemented,
            categoriesIdsMatchAnd: str = NotImplemented,
            categoriesIdsMatchOr: str = NotImplemented,
            categoriesIdsNotContains: str = NotImplemented,
            categoriesIdsEmpty: KalturaNullableBoolean = NotImplemented,
            statusEqual: KalturaEntryStatus = NotImplemented,
            statusNotEqual: KalturaEntryStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            moderationStatusEqual: KalturaEntryModerationStatus = NotImplemented,
            moderationStatusNotEqual: KalturaEntryModerationStatus = NotImplemented,
            moderationStatusIn: str = NotImplemented,
            moderationStatusNotIn: str = NotImplemented,
            typeEqual: KalturaEntryType = NotImplemented,
            typeIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            rankLessThanOrEqual: float = NotImplemented,
            rankGreaterThanOrEqual: float = NotImplemented,
            totalRankLessThanOrEqual: int = NotImplemented,
            totalRankGreaterThanOrEqual: int = NotImplemented,
            groupIdEqual: int = NotImplemented,
            searchTextMatchAnd: str = NotImplemented,
            searchTextMatchOr: str = NotImplemented,
            accessControlIdEqual: int = NotImplemented,
            accessControlIdIn: str = NotImplemented,
            startDateGreaterThanOrEqual: int = NotImplemented,
            startDateLessThanOrEqual: int = NotImplemented,
            startDateGreaterThanOrEqualOrNull: int = NotImplemented,
            startDateLessThanOrEqualOrNull: int = NotImplemented,
            endDateGreaterThanOrEqual: int = NotImplemented,
            endDateLessThanOrEqual: int = NotImplemented,
            endDateGreaterThanOrEqualOrNull: int = NotImplemented,
            endDateLessThanOrEqualOrNull: int = NotImplemented,
            referenceIdEqual: str = NotImplemented,
            referenceIdIn: str = NotImplemented,
            replacingEntryIdEqual: str = NotImplemented,
            replacingEntryIdIn: str = NotImplemented,
            replacedEntryIdEqual: str = NotImplemented,
            replacedEntryIdIn: str = NotImplemented,
            replacementStatusEqual: KalturaEntryReplacementStatus = NotImplemented,
            replacementStatusIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            rootEntryIdEqual: str = NotImplemented,
            rootEntryIdIn: str = NotImplemented,
            parentEntryIdEqual: str = NotImplemented,
            entitledUsersEditMatchAnd: str = NotImplemented,
            entitledUsersEditMatchOr: str = NotImplemented,
            entitledUsersPublishMatchAnd: str = NotImplemented,
            entitledUsersPublishMatchOr: str = NotImplemented,
            entitledUsersViewMatchAnd: str = NotImplemented,
            entitledUsersViewMatchOr: str = NotImplemented,
            tagsNameMultiLikeOr: str = NotImplemented,
            tagsAdminTagsMultiLikeOr: str = NotImplemented,
            tagsAdminTagsNameMultiLikeOr: str = NotImplemented,
            tagsNameMultiLikeAnd: str = NotImplemented,
            tagsAdminTagsMultiLikeAnd: str = NotImplemented,
            tagsAdminTagsNameMultiLikeAnd: str = NotImplemented,
            displayInSearchEqual: KalturaEntryDisplayInSearchType = NotImplemented,
            displayInSearchIn: str = NotImplemented,
            freeText: str = NotImplemented,
            excludedFreeTextGroups: str = NotImplemented,
            descriptionLike: str = NotImplemented,
            isRoot: KalturaNullableBoolean = NotImplemented,
            categoriesFullNameIn: str = NotImplemented,
            categoryAncestorIdIn: str = NotImplemented,
            redirectFromEntryId: str = NotImplemented,
            conversionProfileIdEqual: int = NotImplemented,
            documentTypeEqual: KalturaDocumentType = NotImplemented,
            documentTypeIn: str = NotImplemented,
            assetParamsIdsMatchOr: str = NotImplemented,
            assetParamsIdsMatchAnd: str = NotImplemented): ...
        pass

class KalturaDocumentFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
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

class KalturaImageFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
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

class KalturaPdfFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
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

class KalturaSwfFlavorParamsBaseFilter(KalturaFlavorParamsFilter):
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

class KalturaDocumentFlavorParamsFilter(KalturaDocumentFlavorParamsBaseFilter):
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

class KalturaImageFlavorParamsFilter(KalturaImageFlavorParamsBaseFilter):
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

class KalturaPdfFlavorParamsFilter(KalturaPdfFlavorParamsBaseFilter):
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

class KalturaSwfFlavorParamsFilter(KalturaSwfFlavorParamsBaseFilter):
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

class KalturaDocumentFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
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

class KalturaImageFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
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

class KalturaPdfFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
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

class KalturaSwfFlavorParamsOutputBaseFilter(KalturaFlavorParamsOutputFilter):
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

class KalturaDocumentFlavorParamsOutputFilter(KalturaDocumentFlavorParamsOutputBaseFilter):
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

class KalturaImageFlavorParamsOutputFilter(KalturaImageFlavorParamsOutputBaseFilter):
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

class KalturaPdfFlavorParamsOutputFilter(KalturaPdfFlavorParamsOutputBaseFilter):
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

class KalturaSwfFlavorParamsOutputFilter(KalturaSwfFlavorParamsOutputBaseFilter):
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

class KalturaDocumentsService(KalturaServiceBase):
    def addContent(self, entryId: str, resource: KalturaResource = NotImplemented) -> KalturaDocumentEntry: ...
    def addFromEntry(self, sourceEntryId: str, documentEntry: KalturaDocumentEntry = NotImplemented, sourceFlavorParamsId: int = NotImplemented) -> KalturaDocumentEntry: ...
    def addFromFlavorAsset(self, sourceFlavorAssetId: str, documentEntry: KalturaDocumentEntry = NotImplemented) -> KalturaDocumentEntry: ...
    def addFromUploadedFile(self, documentEntry: KalturaDocumentEntry, uploadTokenId: str) -> KalturaDocumentEntry: ...
    def approveReplace(self, entryId: str) -> KalturaDocumentEntry: ...
    def cancelReplace(self, entryId: str) -> KalturaDocumentEntry: ...
    def convert(self, entryId: str, conversionProfileId: int = NotImplemented, dynamicConversionAttributes: List[None] = NotImplemented) -> int: ...
    def convertPptToSwf(self, entryId: str) -> str: ...
    def delete(self, entryId: str) -> None: ...
    def get(self, entryId: str, version: int = -1) -> KalturaDocumentEntry: ...
    def list(self, filter: KalturaDocumentEntryFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaDocumentListResponse: ...
    def serve(self, entryId: str, flavorAssetId: str = NotImplemented, forceProxy: bool = False) -> IO[Any]: ...
    def serveByFlavorParamsId(self, entryId: str, flavorParamsId: str = NotImplemented, forceProxy: bool = False) -> IO[Any]: ...
    def update(self, entryId: str, documentEntry: KalturaDocumentEntry) -> KalturaDocumentEntry: ...
    def updateContent(self, entryId: str, resource: KalturaResource, conversionProfileId: int = NotImplemented) -> KalturaDocumentEntry: ...
    def upload(self, fileData: IO[Any]) -> str: ...

class KalturaDocumentClientPluginServicesProxy:
    documents: KalturaDocumentsService