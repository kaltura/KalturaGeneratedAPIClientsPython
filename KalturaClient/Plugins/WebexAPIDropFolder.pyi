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

class KalturaWebexAPIGroupParticipationType(object):
    NO_CLASSIFICATION = 0
    OPT_IN = 1
    OPT_OUT = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaWebexAPIUsersMatching(object):
    DO_NOT_MODIFY = 0
    ADD_POSTFIX = 1
    REMOVE_POSTFIX = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaWebexAPIIntegrationSetting(KalturaIntegrationSetting):
    webexCategory: str
    enableRecordingUpload: KalturaNullableBoolean
    enableTranscription: KalturaNullableBoolean
    userMatchingMode: KalturaWebexAPIUsersMatching
    userPostfix: str
    webexAccountDescription: str
    groupParticipationType: KalturaWebexAPIGroupParticipationType
    optOutGroupNames: str
    optInGroupNames: str
    siteUrl: str
    def __init__(self,
            id: int = NotImplemented,
            status: KalturaVendorIntegrationStatus = NotImplemented,
            defaultUserId: str = NotImplemented,
            accountId: str = NotImplemented,
            createUserIfNotExist: KalturaNullableBoolean = NotImplemented,
            conversionProfileId: int = NotImplemented,
            handleParticipantsMode: KalturaHandleParticipantsMode = NotImplemented,
            deletionPolicy: KalturaNullableBoolean = NotImplemented,
            createdAt: str = NotImplemented,
            updatedAt: str = NotImplemented,
            partnerId: int = NotImplemented,
            enableMeetingUpload: KalturaNullableBoolean = NotImplemented,
            enableMeetingChat: KalturaNullableBoolean = NotImplemented,
            webexCategory: str = NotImplemented,
            enableRecordingUpload: KalturaNullableBoolean = NotImplemented,
            enableTranscription: KalturaNullableBoolean = NotImplemented,
            userMatchingMode: KalturaWebexAPIUsersMatching = NotImplemented,
            userPostfix: str = NotImplemented,
            webexAccountDescription: str = NotImplemented,
            groupParticipationType: KalturaWebexAPIGroupParticipationType = NotImplemented,
            optOutGroupNames: str = NotImplemented,
            optInGroupNames: str = NotImplemented,
            siteUrl: str = NotImplemented): ...

    def getWebexCategory(self) -> str: ...
    def setWebexCategory(self, newWebexCategory: str) -> None: ...
    def getEnableRecordingUpload(self) -> KalturaNullableBoolean: ...
    def setEnableRecordingUpload(self, newEnableRecordingUpload: KalturaNullableBoolean) -> None: ...
    def getEnableTranscription(self) -> KalturaNullableBoolean: ...
    def setEnableTranscription(self, newEnableTranscription: KalturaNullableBoolean) -> None: ...
    def getUserMatchingMode(self) -> KalturaWebexAPIUsersMatching: ...
    def setUserMatchingMode(self, newUserMatchingMode: KalturaWebexAPIUsersMatching) -> None: ...
    def getUserPostfix(self) -> str: ...
    def setUserPostfix(self, newUserPostfix: str) -> None: ...
    def getWebexAccountDescription(self) -> str: ...
    def setWebexAccountDescription(self, newWebexAccountDescription: str) -> None: ...
    def getGroupParticipationType(self) -> KalturaWebexAPIGroupParticipationType: ...
    def setGroupParticipationType(self, newGroupParticipationType: KalturaWebexAPIGroupParticipationType) -> None: ...
    def getOptOutGroupNames(self) -> str: ...
    def setOptOutGroupNames(self, newOptOutGroupNames: str) -> None: ...
    def getOptInGroupNames(self) -> str: ...
    def setOptInGroupNames(self, newOptInGroupNames: str) -> None: ...
    def getSiteUrl(self) -> str: ...
    def setSiteUrl(self, newSiteUrl: str) -> None: ...

class KalturaWebexAPIDropFolder(KalturaDropFolder):
    webexAPIVendorIntegrationId: int
    webexAPIVendorIntegration: KalturaWebexAPIIntegrationSetting
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
            webexAPIVendorIntegrationId: int = NotImplemented,
            webexAPIVendorIntegration: KalturaWebexAPIIntegrationSetting = NotImplemented): ...

    def getWebexAPIVendorIntegrationId(self) -> int: ...
    def getWebexAPIVendorIntegration(self) -> KalturaWebexAPIIntegrationSetting: ...

class KalturaWebexAPIDropFolderFile(KalturaDropFolderFile):
    recordingId: str
    description: str
    contentUrl: str
    urlExpiry: int
    fileExtension: str
    meetingId: str
    recordingStartTime: int
    hostEmail: str
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
            recordingId: str = NotImplemented,
            description: str = NotImplemented,
            contentUrl: str = NotImplemented,
            urlExpiry: int = NotImplemented,
            fileExtension: str = NotImplemented,
            meetingId: str = NotImplemented,
            recordingStartTime: int = NotImplemented,
            hostEmail: str = NotImplemented): ...

    def getRecordingId(self) -> str: ...
    def setRecordingId(self, newRecordingId: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getContentUrl(self) -> str: ...
    def setContentUrl(self, newContentUrl: str) -> None: ...
    def getUrlExpiry(self) -> int: ...
    def setUrlExpiry(self, newUrlExpiry: int) -> None: ...
    def getFileExtension(self) -> str: ...
    def setFileExtension(self, newFileExtension: str) -> None: ...
    def getMeetingId(self) -> str: ...
    def setMeetingId(self, newMeetingId: str) -> None: ...
    def getRecordingStartTime(self) -> int: ...
    def setRecordingStartTime(self, newRecordingStartTime: int) -> None: ...
    def getHostEmail(self) -> str: ...
    def setHostEmail(self, newHostEmail: str) -> None: ...

class KalturaWebexAPIIntegrationSettingResponse(KalturaListResponse):
    objects: List[KalturaWebexAPIIntegrationSetting]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaWebexAPIIntegrationSetting] = NotImplemented): ...

    def getObjects(self) -> List[KalturaWebexAPIIntegrationSetting]: ...

class KalturaWebexVendorService(KalturaServiceBase):
    def fetchRegistrationPage(self, tokensData: str, iv: str) -> None: ...
    def list(self, pager: KalturaFilterPager = NotImplemented) -> KalturaWebexAPIIntegrationSettingResponse: ...
    def oauthValidation(self) -> str: ...
    def preOauthValidation(self) -> None: ...
    def submitRegistration(self, accountId: str, integrationSetting: KalturaWebexAPIIntegrationSetting) -> str: ...

class KalturaWebexAPIDropFolderClientPluginServicesProxy:
    webexVendor: KalturaWebexVendorService