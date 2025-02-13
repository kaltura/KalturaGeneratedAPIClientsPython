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
from .DropFolder import *
from .Vendor import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaZoomMeetingMetadata(KalturaObjectBase):
    uuid: str
    meetingId: str
    accountId: str
    hostId: str
    topic: str
    meetingStartTime: str
    type: KalturaRecordingType
    def __init__(self,
            uuid: str = NotImplemented,
            meetingId: str = NotImplemented,
            accountId: str = NotImplemented,
            hostId: str = NotImplemented,
            topic: str = NotImplemented,
            meetingStartTime: str = NotImplemented,
            type: KalturaRecordingType = NotImplemented): ...

    def getUuid(self) -> str: ...
    def setUuid(self, newUuid: str) -> None: ...
    def getMeetingId(self) -> str: ...
    def setMeetingId(self, newMeetingId: str) -> None: ...
    def getAccountId(self) -> str: ...
    def setAccountId(self, newAccountId: str) -> None: ...
    def getHostId(self) -> str: ...
    def setHostId(self, newHostId: str) -> None: ...
    def getTopic(self) -> str: ...
    def setTopic(self, newTopic: str) -> None: ...
    def getMeetingStartTime(self) -> str: ...
    def setMeetingStartTime(self, newMeetingStartTime: str) -> None: ...
    def getType(self) -> KalturaRecordingType: ...
    def setType(self, newType: KalturaRecordingType) -> None: ...

class KalturaZoomRecordingFile(KalturaObjectBase):
    id: str
    recordingStart: str
    fileType: KalturaRecordingFileType
    downloadUrl: str
    fileExtension: str
    downloadToken: str
    def __init__(self,
            id: str = NotImplemented,
            recordingStart: str = NotImplemented,
            fileType: KalturaRecordingFileType = NotImplemented,
            downloadUrl: str = NotImplemented,
            fileExtension: str = NotImplemented,
            downloadToken: str = NotImplemented): ...

    def getId(self) -> str: ...
    def setId(self, newId: str) -> None: ...
    def getRecordingStart(self) -> str: ...
    def setRecordingStart(self, newRecordingStart: str) -> None: ...
    def getFileType(self) -> KalturaRecordingFileType: ...
    def setFileType(self, newFileType: KalturaRecordingFileType) -> None: ...
    def getDownloadUrl(self) -> str: ...
    def setDownloadUrl(self, newDownloadUrl: str) -> None: ...
    def getFileExtension(self) -> str: ...
    def setFileExtension(self, newFileExtension: str) -> None: ...
    def getDownloadToken(self) -> str: ...
    def setDownloadToken(self, newDownloadToken: str) -> None: ...

class KalturaZoomDropFolder(KalturaDropFolder):
    zoomVendorIntegrationId: int
    zoomVendorIntegration: KalturaZoomIntegrationSetting
    lastHandledMeetingTime: int
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            description: str = NotImplemented,
            type: KalturaDropFolderType = NotImplemented,
            status: KalturaDropFolderStatus = NotImplemented,
            conversionProfileId: int = NotImplemented,
            dc: int = NotImplemented,
            path: str = NotImplemented,
            fileSizeCheckInterval: int = NotImplemented,
            fileDeletePolicy: KalturaDropFolderFileDeletePolicy = NotImplemented,
            fileDeleteRegex: str = NotImplemented,
            autoFileDeleteDays: int = NotImplemented,
            fileHandlerType: KalturaDropFolderFileHandlerType = NotImplemented,
            fileNamePatterns: str = NotImplemented,
            fileHandlerConfig: KalturaDropFolderFileHandlerConfig = NotImplemented,
            tags: str = NotImplemented,
            errorCode: KalturaDropFolderErrorCode = NotImplemented,
            errorDescription: str = NotImplemented,
            ignoreFileNamePatterns: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            lastAccessedAt: int = NotImplemented,
            incremental: bool = NotImplemented,
            lastFileTimestamp: int = NotImplemented,
            metadataProfileId: int = NotImplemented,
            categoriesMetadataFieldName: str = NotImplemented,
            enforceEntitlement: bool = NotImplemented,
            shouldValidateKS: bool = NotImplemented,
            zoomVendorIntegrationId: int = NotImplemented,
            zoomVendorIntegration: KalturaZoomIntegrationSetting = NotImplemented,
            lastHandledMeetingTime: int = NotImplemented): ...

    def getZoomVendorIntegrationId(self) -> int: ...
    def getZoomVendorIntegration(self) -> KalturaZoomIntegrationSetting: ...
    def getLastHandledMeetingTime(self) -> int: ...
    def setLastHandledMeetingTime(self, newLastHandledMeetingTime: int) -> None: ...

class KalturaZoomDropFolderFile(KalturaDropFolderFile):
    meetingMetadata: KalturaZoomMeetingMetadata
    recordingFile: KalturaZoomRecordingFile
    parentEntryId: str
    isParentEntry: bool
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            dropFolderId: int = NotImplemented,
            fileName: str = NotImplemented,
            fileSize: float = NotImplemented,
            fileSizeLastSetAt: int = NotImplemented,
            status: KalturaDropFolderFileStatus = NotImplemented,
            type: KalturaDropFolderType = NotImplemented,
            parsedSlug: str = NotImplemented,
            parsedFlavor: str = NotImplemented,
            parsedUserId: str = NotImplemented,
            leadDropFolderFileId: int = NotImplemented,
            deletedDropFolderFileId: int = NotImplemented,
            entryId: str = NotImplemented,
            errorCode: KalturaDropFolderFileErrorCode = NotImplemented,
            errorDescription: str = NotImplemented,
            lastModificationTime: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            uploadStartDetectedAt: int = NotImplemented,
            uploadEndDetectedAt: int = NotImplemented,
            importStartedAt: int = NotImplemented,
            importEndedAt: int = NotImplemented,
            batchJobId: int = NotImplemented,
            meetingMetadata: KalturaZoomMeetingMetadata = NotImplemented,
            recordingFile: KalturaZoomRecordingFile = NotImplemented,
            parentEntryId: str = NotImplemented,
            isParentEntry: bool = NotImplemented): ...

    def getMeetingMetadata(self) -> KalturaZoomMeetingMetadata: ...
    def setMeetingMetadata(self, newMeetingMetadata: KalturaZoomMeetingMetadata) -> None: ...
    def getRecordingFile(self) -> KalturaZoomRecordingFile: ...
    def setRecordingFile(self, newRecordingFile: KalturaZoomRecordingFile) -> None: ...
    def getParentEntryId(self) -> str: ...
    def setParentEntryId(self, newParentEntryId: str) -> None: ...
    def getIsParentEntry(self) -> bool: ...
    def setIsParentEntry(self, newIsParentEntry: bool) -> None: ...

class KalturaZoomDropFolderBaseFilter(KalturaDropFolderFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            typeEqual: KalturaDropFolderType = NotImplemented,
            typeIn: str = NotImplemented,
            statusEqual: KalturaDropFolderStatus = NotImplemented,
            statusIn: str = NotImplemented,
            conversionProfileIdEqual: int = NotImplemented,
            conversionProfileIdIn: str = NotImplemented,
            dcEqual: int = NotImplemented,
            dcIn: str = NotImplemented,
            pathEqual: str = NotImplemented,
            pathLike: str = NotImplemented,
            fileHandlerTypeEqual: KalturaDropFolderFileHandlerType = NotImplemented,
            fileHandlerTypeIn: str = NotImplemented,
            fileNamePatternsLike: str = NotImplemented,
            fileNamePatternsMultiLikeOr: str = NotImplemented,
            fileNamePatternsMultiLikeAnd: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            errorCodeEqual: KalturaDropFolderErrorCode = NotImplemented,
            errorCodeIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            currentDc: KalturaNullableBoolean = NotImplemented): ...
        pass

class KalturaZoomDropFolderFilter(KalturaZoomDropFolderBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            typeEqual: KalturaDropFolderType = NotImplemented,
            typeIn: str = NotImplemented,
            statusEqual: KalturaDropFolderStatus = NotImplemented,
            statusIn: str = NotImplemented,
            conversionProfileIdEqual: int = NotImplemented,
            conversionProfileIdIn: str = NotImplemented,
            dcEqual: int = NotImplemented,
            dcIn: str = NotImplemented,
            pathEqual: str = NotImplemented,
            pathLike: str = NotImplemented,
            fileHandlerTypeEqual: KalturaDropFolderFileHandlerType = NotImplemented,
            fileHandlerTypeIn: str = NotImplemented,
            fileNamePatternsLike: str = NotImplemented,
            fileNamePatternsMultiLikeOr: str = NotImplemented,
            fileNamePatternsMultiLikeAnd: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            errorCodeEqual: KalturaDropFolderErrorCode = NotImplemented,
            errorCodeIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            currentDc: KalturaNullableBoolean = NotImplemented): ...
        pass

class KalturaZoomDropFolderClientPluginServicesProxy: