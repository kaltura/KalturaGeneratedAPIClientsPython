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
from .Metadata import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaDropFolderContentFileHandlerMatchPolicy(object):
    ADD_AS_NEW = 1
    MATCH_EXISTING_OR_ADD_AS_NEW = 2
    MATCH_EXISTING_OR_KEEP_IN_FOLDER = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaDropFolderFileDeletePolicy(object):
    MANUAL_DELETE = 1
    AUTO_DELETE = 2
    AUTO_DELETE_WHEN_ENTRY_IS_READY = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaDropFolderFileStatus(object):
    UPLOADING = 1
    PENDING = 2
    WAITING = 3
    HANDLED = 4
    IGNORE = 5
    DELETED = 6
    PURGED = 7
    NO_MATCH = 8
    ERROR_HANDLING = 9
    ERROR_DELETING = 10
    DOWNLOADING = 11
    ERROR_DOWNLOADING = 12
    PROCESSING = 13
    PARSED = 14
    DETECTED = 15

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaDropFolderStatus(object):
    DISABLED = 0
    ENABLED = 1
    DELETED = 2
    ERROR = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaDropFolderErrorCode(object):
    ERROR_CONNECT = "1"
    ERROR_AUTENTICATE = "2"
    ERROR_GET_PHISICAL_FILE_LIST = "3"
    ERROR_GET_DB_FILE_LIST = "4"
    DROP_FOLDER_APP_ERROR = "5"
    CONTENT_MATCH_POLICY_UNDEFINED = "6"
    MISSING_CONFIG = "7"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDropFolderFileErrorCode(object):
    ERROR_ADDING_BULK_UPLOAD = "dropFolderXmlBulkUpload.ERROR_ADDING_BULK_UPLOAD"
    ERROR_ADD_CONTENT_RESOURCE = "dropFolderXmlBulkUpload.ERROR_ADD_CONTENT_RESOURCE"
    ERROR_IN_BULK_UPLOAD = "dropFolderXmlBulkUpload.ERROR_IN_BULK_UPLOAD"
    ERROR_WRITING_TEMP_FILE = "dropFolderXmlBulkUpload.ERROR_WRITING_TEMP_FILE"
    LOCAL_FILE_WRONG_CHECKSUM = "dropFolderXmlBulkUpload.LOCAL_FILE_WRONG_CHECKSUM"
    LOCAL_FILE_WRONG_SIZE = "dropFolderXmlBulkUpload.LOCAL_FILE_WRONG_SIZE"
    MALFORMED_XML_FILE = "dropFolderXmlBulkUpload.MALFORMED_XML_FILE"
    XML_FILE_SIZE_EXCEED_LIMIT = "dropFolderXmlBulkUpload.XML_FILE_SIZE_EXCEED_LIMIT"
    ERROR_UPDATE_ENTRY = "1"
    ERROR_ADD_ENTRY = "2"
    FLAVOR_NOT_FOUND = "3"
    FLAVOR_MISSING_IN_FILE_NAME = "4"
    SLUG_REGEX_NO_MATCH = "5"
    ERROR_READING_FILE = "6"
    ERROR_DOWNLOADING_FILE = "7"
    ERROR_UPDATE_FILE = "8"
    ERROR_ADDING_CONTENT_PROCESSOR = "10"
    ERROR_IN_CONTENT_PROCESSOR = "11"
    ERROR_DELETING_FILE = "12"
    FILE_NO_MATCH = "13"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDropFolderFileHandlerType(object):
    TR_RDS = "TrRdsSyncDropFolder.TR_RDS"
    XML = "dropFolderXmlBulkUpload.XML"
    ICAL = "scheduleDropFolder.ICAL"
    CONTENT = "1"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDropFolderFileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    FILE_NAME_ASC = "+fileName"
    FILE_SIZE_ASC = "+fileSize"
    FILE_SIZE_LAST_SET_AT_ASC = "+fileSizeLastSetAt"
    ID_ASC = "+id"
    PARSED_FLAVOR_ASC = "+parsedFlavor"
    PARSED_SLUG_ASC = "+parsedSlug"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    FILE_NAME_DESC = "-fileName"
    FILE_SIZE_DESC = "-fileSize"
    FILE_SIZE_LAST_SET_AT_DESC = "-fileSizeLastSetAt"
    ID_DESC = "-id"
    PARSED_FLAVOR_DESC = "-parsedFlavor"
    PARSED_SLUG_DESC = "-parsedSlug"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDropFolderOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    NAME_ASC = "+name"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    NAME_DESC = "-name"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDropFolderType(object):
    AP_FEED = "ApFeedDropFolder.AP_FEED"
    FEED = "FeedDropFolder.FEED"
    MS_TEAMS = "MicrosoftTeamsDropFolder.MS_TEAMS"
    S3DROPFOLDER = "S3DropFolder.S3DROPFOLDER"
    TR_RDS_COMPANY = "TrRdsSyncDropFolder.TR_RDS_COMPANY"
    TR_RDS_TMCTERM = "TrRdsSyncDropFolder.TR_RDS_TMCTERM"
    WEBEX_API = "WebexAPIDropFolder.WEBEX_API"
    WEBEX = "WebexDropFolder.WEBEX"
    ZOOM = "ZoomDropFolder.ZOOM"
    LOCAL = "1"
    FTP = "2"
    SCP = "3"
    SFTP = "4"
    S3 = "6"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaFtpDropFolderOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    NAME_ASC = "+name"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    NAME_DESC = "-name"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaRemoteDropFolderOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    NAME_ASC = "+name"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    NAME_DESC = "-name"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaScpDropFolderOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    NAME_ASC = "+name"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    NAME_DESC = "-name"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaSftpDropFolderOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    NAME_ASC = "+name"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    NAME_DESC = "-name"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaSshDropFolderOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    NAME_ASC = "+name"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    NAME_DESC = "-name"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaDropFolderFileHandlerConfig(KalturaObjectBase):
    handlerType: KalturaDropFolderFileHandlerType
    def __init__(self,
            handlerType: KalturaDropFolderFileHandlerType = NotImplemented): ...

    def getHandlerType(self) -> KalturaDropFolderFileHandlerType: ...

class KalturaDropFolder(KalturaObjectBase):
    id: int
    partnerId: int
    name: str
    description: str
    type: KalturaDropFolderType
    status: KalturaDropFolderStatus
    conversionProfileId: int
    dc: int
    path: str
    fileSizeCheckInterval: int
    fileDeletePolicy: KalturaDropFolderFileDeletePolicy
    fileDeleteRegex: str
    autoFileDeleteDays: int
    fileHandlerType: KalturaDropFolderFileHandlerType
    fileNamePatterns: str
    fileHandlerConfig: KalturaDropFolderFileHandlerConfig
    tags: str
    errorCode: KalturaDropFolderErrorCode
    errorDescription: str
    ignoreFileNamePatterns: str
    createdAt: int
    updatedAt: int
    lastAccessedAt: int
    incremental: bool
    lastFileTimestamp: int
    metadataProfileId: int
    categoriesMetadataFieldName: str
    enforceEntitlement: bool
    shouldValidateKS: bool
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
            shouldValidateKS: bool = NotImplemented): ...

    def getId(self) -> int: ...
    def getPartnerId(self) -> int: ...
    def setPartnerId(self, newPartnerId: int) -> None: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getType(self) -> KalturaDropFolderType: ...
    def setType(self, newType: KalturaDropFolderType) -> None: ...
    def getStatus(self) -> KalturaDropFolderStatus: ...
    def setStatus(self, newStatus: KalturaDropFolderStatus) -> None: ...
    def getConversionProfileId(self) -> int: ...
    def setConversionProfileId(self, newConversionProfileId: int) -> None: ...
    def getDc(self) -> int: ...
    def setDc(self, newDc: int) -> None: ...
    def getPath(self) -> str: ...
    def setPath(self, newPath: str) -> None: ...
    def getFileSizeCheckInterval(self) -> int: ...
    def setFileSizeCheckInterval(self, newFileSizeCheckInterval: int) -> None: ...
    def getFileDeletePolicy(self) -> KalturaDropFolderFileDeletePolicy: ...
    def setFileDeletePolicy(self, newFileDeletePolicy: KalturaDropFolderFileDeletePolicy) -> None: ...
    def getFileDeleteRegex(self) -> str: ...
    def setFileDeleteRegex(self, newFileDeleteRegex: str) -> None: ...
    def getAutoFileDeleteDays(self) -> int: ...
    def setAutoFileDeleteDays(self, newAutoFileDeleteDays: int) -> None: ...
    def getFileHandlerType(self) -> KalturaDropFolderFileHandlerType: ...
    def setFileHandlerType(self, newFileHandlerType: KalturaDropFolderFileHandlerType) -> None: ...
    def getFileNamePatterns(self) -> str: ...
    def setFileNamePatterns(self, newFileNamePatterns: str) -> None: ...
    def getFileHandlerConfig(self) -> KalturaDropFolderFileHandlerConfig: ...
    def setFileHandlerConfig(self, newFileHandlerConfig: KalturaDropFolderFileHandlerConfig) -> None: ...
    def getTags(self) -> str: ...
    def setTags(self, newTags: str) -> None: ...
    def getErrorCode(self) -> KalturaDropFolderErrorCode: ...
    def setErrorCode(self, newErrorCode: KalturaDropFolderErrorCode) -> None: ...
    def getErrorDescription(self) -> str: ...
    def setErrorDescription(self, newErrorDescription: str) -> None: ...
    def getIgnoreFileNamePatterns(self) -> str: ...
    def setIgnoreFileNamePatterns(self, newIgnoreFileNamePatterns: str) -> None: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getLastAccessedAt(self) -> int: ...
    def setLastAccessedAt(self, newLastAccessedAt: int) -> None: ...
    def getIncremental(self) -> bool: ...
    def setIncremental(self, newIncremental: bool) -> None: ...
    def getLastFileTimestamp(self) -> int: ...
    def setLastFileTimestamp(self, newLastFileTimestamp: int) -> None: ...
    def getMetadataProfileId(self) -> int: ...
    def setMetadataProfileId(self, newMetadataProfileId: int) -> None: ...
    def getCategoriesMetadataFieldName(self) -> str: ...
    def setCategoriesMetadataFieldName(self, newCategoriesMetadataFieldName: str) -> None: ...
    def getEnforceEntitlement(self) -> bool: ...
    def setEnforceEntitlement(self, newEnforceEntitlement: bool) -> None: ...
    def getShouldValidateKS(self) -> bool: ...
    def setShouldValidateKS(self, newShouldValidateKS: bool) -> None: ...

class KalturaDropFolderFile(KalturaObjectBase):
    id: int
    partnerId: int
    dropFolderId: int
    fileName: str
    fileSize: float
    fileSizeLastSetAt: int
    status: KalturaDropFolderFileStatus
    type: KalturaDropFolderType
    parsedSlug: str
    parsedFlavor: str
    parsedUserId: str
    leadDropFolderFileId: int
    deletedDropFolderFileId: int
    entryId: str
    errorCode: KalturaDropFolderFileErrorCode
    errorDescription: str
    lastModificationTime: str
    createdAt: int
    updatedAt: int
    uploadStartDetectedAt: int
    uploadEndDetectedAt: int
    importStartedAt: int
    importEndedAt: int
    batchJobId: int
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
            batchJobId: int = NotImplemented): ...

    def getId(self) -> int: ...
    def getPartnerId(self) -> int: ...
    def getDropFolderId(self) -> int: ...
    def setDropFolderId(self, newDropFolderId: int) -> None: ...
    def getFileName(self) -> str: ...
    def setFileName(self, newFileName: str) -> None: ...
    def getFileSize(self) -> float: ...
    def setFileSize(self, newFileSize: float) -> None: ...
    def getFileSizeLastSetAt(self) -> int: ...
    def getStatus(self) -> KalturaDropFolderFileStatus: ...
    def getType(self) -> KalturaDropFolderType: ...
    def getParsedSlug(self) -> str: ...
    def setParsedSlug(self, newParsedSlug: str) -> None: ...
    def getParsedFlavor(self) -> str: ...
    def setParsedFlavor(self, newParsedFlavor: str) -> None: ...
    def getParsedUserId(self) -> str: ...
    def setParsedUserId(self, newParsedUserId: str) -> None: ...
    def getLeadDropFolderFileId(self) -> int: ...
    def setLeadDropFolderFileId(self, newLeadDropFolderFileId: int) -> None: ...
    def getDeletedDropFolderFileId(self) -> int: ...
    def setDeletedDropFolderFileId(self, newDeletedDropFolderFileId: int) -> None: ...
    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...
    def getErrorCode(self) -> KalturaDropFolderFileErrorCode: ...
    def setErrorCode(self, newErrorCode: KalturaDropFolderFileErrorCode) -> None: ...
    def getErrorDescription(self) -> str: ...
    def setErrorDescription(self, newErrorDescription: str) -> None: ...
    def getLastModificationTime(self) -> str: ...
    def setLastModificationTime(self, newLastModificationTime: str) -> None: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getUploadStartDetectedAt(self) -> int: ...
    def setUploadStartDetectedAt(self, newUploadStartDetectedAt: int) -> None: ...
    def getUploadEndDetectedAt(self) -> int: ...
    def setUploadEndDetectedAt(self, newUploadEndDetectedAt: int) -> None: ...
    def getImportStartedAt(self) -> int: ...
    def setImportStartedAt(self, newImportStartedAt: int) -> None: ...
    def getImportEndedAt(self) -> int: ...
    def setImportEndedAt(self, newImportEndedAt: int) -> None: ...
    def getBatchJobId(self) -> int: ...

class KalturaDropFolderBaseFilter(KalturaFilter):
    idEqual: int
    idIn: str
    partnerIdEqual: int
    partnerIdIn: str
    nameLike: str
    typeEqual: KalturaDropFolderType
    typeIn: str
    statusEqual: KalturaDropFolderStatus
    statusIn: str
    conversionProfileIdEqual: int
    conversionProfileIdIn: str
    dcEqual: int
    dcIn: str
    pathEqual: str
    pathLike: str
    fileHandlerTypeEqual: KalturaDropFolderFileHandlerType
    fileHandlerTypeIn: str
    fileNamePatternsLike: str
    fileNamePatternsMultiLikeOr: str
    fileNamePatternsMultiLikeAnd: str
    tagsLike: str
    tagsMultiLikeOr: str
    tagsMultiLikeAnd: str
    errorCodeEqual: KalturaDropFolderErrorCode
    errorCodeIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
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
            updatedAtLessThanOrEqual: int = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getPartnerIdEqual(self) -> int: ...
    def setPartnerIdEqual(self, newPartnerIdEqual: int) -> None: ...
    def getPartnerIdIn(self) -> str: ...
    def setPartnerIdIn(self, newPartnerIdIn: str) -> None: ...
    def getNameLike(self) -> str: ...
    def setNameLike(self, newNameLike: str) -> None: ...
    def getTypeEqual(self) -> KalturaDropFolderType: ...
    def setTypeEqual(self, newTypeEqual: KalturaDropFolderType) -> None: ...
    def getTypeIn(self) -> str: ...
    def setTypeIn(self, newTypeIn: str) -> None: ...
    def getStatusEqual(self) -> KalturaDropFolderStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaDropFolderStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getConversionProfileIdEqual(self) -> int: ...
    def setConversionProfileIdEqual(self, newConversionProfileIdEqual: int) -> None: ...
    def getConversionProfileIdIn(self) -> str: ...
    def setConversionProfileIdIn(self, newConversionProfileIdIn: str) -> None: ...
    def getDcEqual(self) -> int: ...
    def setDcEqual(self, newDcEqual: int) -> None: ...
    def getDcIn(self) -> str: ...
    def setDcIn(self, newDcIn: str) -> None: ...
    def getPathEqual(self) -> str: ...
    def setPathEqual(self, newPathEqual: str) -> None: ...
    def getPathLike(self) -> str: ...
    def setPathLike(self, newPathLike: str) -> None: ...
    def getFileHandlerTypeEqual(self) -> KalturaDropFolderFileHandlerType: ...
    def setFileHandlerTypeEqual(self, newFileHandlerTypeEqual: KalturaDropFolderFileHandlerType) -> None: ...
    def getFileHandlerTypeIn(self) -> str: ...
    def setFileHandlerTypeIn(self, newFileHandlerTypeIn: str) -> None: ...
    def getFileNamePatternsLike(self) -> str: ...
    def setFileNamePatternsLike(self, newFileNamePatternsLike: str) -> None: ...
    def getFileNamePatternsMultiLikeOr(self) -> str: ...
    def setFileNamePatternsMultiLikeOr(self, newFileNamePatternsMultiLikeOr: str) -> None: ...
    def getFileNamePatternsMultiLikeAnd(self) -> str: ...
    def setFileNamePatternsMultiLikeAnd(self, newFileNamePatternsMultiLikeAnd: str) -> None: ...
    def getTagsLike(self) -> str: ...
    def setTagsLike(self, newTagsLike: str) -> None: ...
    def getTagsMultiLikeOr(self) -> str: ...
    def setTagsMultiLikeOr(self, newTagsMultiLikeOr: str) -> None: ...
    def getTagsMultiLikeAnd(self) -> str: ...
    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd: str) -> None: ...
    def getErrorCodeEqual(self) -> KalturaDropFolderErrorCode: ...
    def setErrorCodeEqual(self, newErrorCodeEqual: KalturaDropFolderErrorCode) -> None: ...
    def getErrorCodeIn(self) -> str: ...
    def setErrorCodeIn(self, newErrorCodeIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...

class KalturaDropFolderContentFileHandlerConfig(KalturaDropFolderFileHandlerConfig):
    contentMatchPolicy: KalturaDropFolderContentFileHandlerMatchPolicy
    slugRegex: str
    def __init__(self,
            handlerType: KalturaDropFolderFileHandlerType = NotImplemented,
            contentMatchPolicy: KalturaDropFolderContentFileHandlerMatchPolicy = NotImplemented,
            slugRegex: str = NotImplemented): ...

    def getContentMatchPolicy(self) -> KalturaDropFolderContentFileHandlerMatchPolicy: ...
    def setContentMatchPolicy(self, newContentMatchPolicy: KalturaDropFolderContentFileHandlerMatchPolicy) -> None: ...
    def getSlugRegex(self) -> str: ...
    def setSlugRegex(self, newSlugRegex: str) -> None: ...

class KalturaDropFolderContentProcessorJobData(KalturaJobData):
    dropFolderId: int
    dropFolderFileIds: str
    parsedSlug: str
    contentMatchPolicy: KalturaDropFolderContentFileHandlerMatchPolicy
    conversionProfileId: int
    parsedUserId: str
    def __init__(self,
            dropFolderId: int = NotImplemented,
            dropFolderFileIds: str = NotImplemented,
            parsedSlug: str = NotImplemented,
            contentMatchPolicy: KalturaDropFolderContentFileHandlerMatchPolicy = NotImplemented,
            conversionProfileId: int = NotImplemented,
            parsedUserId: str = NotImplemented): ...

    def getDropFolderId(self) -> int: ...
    def setDropFolderId(self, newDropFolderId: int) -> None: ...
    def getDropFolderFileIds(self) -> str: ...
    def setDropFolderFileIds(self, newDropFolderFileIds: str) -> None: ...
    def getParsedSlug(self) -> str: ...
    def setParsedSlug(self, newParsedSlug: str) -> None: ...
    def getContentMatchPolicy(self) -> KalturaDropFolderContentFileHandlerMatchPolicy: ...
    def setContentMatchPolicy(self, newContentMatchPolicy: KalturaDropFolderContentFileHandlerMatchPolicy) -> None: ...
    def getConversionProfileId(self) -> int: ...
    def setConversionProfileId(self, newConversionProfileId: int) -> None: ...
    def getParsedUserId(self) -> str: ...
    def setParsedUserId(self, newParsedUserId: str) -> None: ...

class KalturaDropFolderFileBaseFilter(KalturaFilter):
    idEqual: int
    idIn: str
    idGreaterThanOrEqual: int
    partnerIdEqual: int
    partnerIdIn: str
    dropFolderIdEqual: int
    dropFolderIdIn: str
    fileNameEqual: str
    fileNameIn: str
    fileNameLike: str
    statusEqual: KalturaDropFolderFileStatus
    statusIn: str
    statusNotIn: str
    parsedSlugEqual: str
    parsedSlugIn: str
    parsedSlugLike: str
    parsedFlavorEqual: str
    parsedFlavorIn: str
    parsedFlavorLike: str
    leadDropFolderFileIdEqual: int
    deletedDropFolderFileIdEqual: int
    entryIdEqual: str
    errorCodeEqual: KalturaDropFolderFileErrorCode
    errorCodeIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idGreaterThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            dropFolderIdEqual: int = NotImplemented,
            dropFolderIdIn: str = NotImplemented,
            fileNameEqual: str = NotImplemented,
            fileNameIn: str = NotImplemented,
            fileNameLike: str = NotImplemented,
            statusEqual: KalturaDropFolderFileStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            parsedSlugEqual: str = NotImplemented,
            parsedSlugIn: str = NotImplemented,
            parsedSlugLike: str = NotImplemented,
            parsedFlavorEqual: str = NotImplemented,
            parsedFlavorIn: str = NotImplemented,
            parsedFlavorLike: str = NotImplemented,
            leadDropFolderFileIdEqual: int = NotImplemented,
            deletedDropFolderFileIdEqual: int = NotImplemented,
            entryIdEqual: str = NotImplemented,
            errorCodeEqual: KalturaDropFolderFileErrorCode = NotImplemented,
            errorCodeIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getIdGreaterThanOrEqual(self) -> int: ...
    def setIdGreaterThanOrEqual(self, newIdGreaterThanOrEqual: int) -> None: ...
    def getPartnerIdEqual(self) -> int: ...
    def setPartnerIdEqual(self, newPartnerIdEqual: int) -> None: ...
    def getPartnerIdIn(self) -> str: ...
    def setPartnerIdIn(self, newPartnerIdIn: str) -> None: ...
    def getDropFolderIdEqual(self) -> int: ...
    def setDropFolderIdEqual(self, newDropFolderIdEqual: int) -> None: ...
    def getDropFolderIdIn(self) -> str: ...
    def setDropFolderIdIn(self, newDropFolderIdIn: str) -> None: ...
    def getFileNameEqual(self) -> str: ...
    def setFileNameEqual(self, newFileNameEqual: str) -> None: ...
    def getFileNameIn(self) -> str: ...
    def setFileNameIn(self, newFileNameIn: str) -> None: ...
    def getFileNameLike(self) -> str: ...
    def setFileNameLike(self, newFileNameLike: str) -> None: ...
    def getStatusEqual(self) -> KalturaDropFolderFileStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaDropFolderFileStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getStatusNotIn(self) -> str: ...
    def setStatusNotIn(self, newStatusNotIn: str) -> None: ...
    def getParsedSlugEqual(self) -> str: ...
    def setParsedSlugEqual(self, newParsedSlugEqual: str) -> None: ...
    def getParsedSlugIn(self) -> str: ...
    def setParsedSlugIn(self, newParsedSlugIn: str) -> None: ...
    def getParsedSlugLike(self) -> str: ...
    def setParsedSlugLike(self, newParsedSlugLike: str) -> None: ...
    def getParsedFlavorEqual(self) -> str: ...
    def setParsedFlavorEqual(self, newParsedFlavorEqual: str) -> None: ...
    def getParsedFlavorIn(self) -> str: ...
    def setParsedFlavorIn(self, newParsedFlavorIn: str) -> None: ...
    def getParsedFlavorLike(self) -> str: ...
    def setParsedFlavorLike(self, newParsedFlavorLike: str) -> None: ...
    def getLeadDropFolderFileIdEqual(self) -> int: ...
    def setLeadDropFolderFileIdEqual(self, newLeadDropFolderFileIdEqual: int) -> None: ...
    def getDeletedDropFolderFileIdEqual(self) -> int: ...
    def setDeletedDropFolderFileIdEqual(self, newDeletedDropFolderFileIdEqual: int) -> None: ...
    def getEntryIdEqual(self) -> str: ...
    def setEntryIdEqual(self, newEntryIdEqual: str) -> None: ...
    def getErrorCodeEqual(self) -> KalturaDropFolderFileErrorCode: ...
    def setErrorCodeEqual(self, newErrorCodeEqual: KalturaDropFolderFileErrorCode) -> None: ...
    def getErrorCodeIn(self) -> str: ...
    def setErrorCodeIn(self, newErrorCodeIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...

class KalturaDropFolderFileListResponse(KalturaListResponse):
    objects: List[KalturaDropFolderFile]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaDropFolderFile] = NotImplemented): ...

    def getObjects(self) -> List[KalturaDropFolderFile]: ...

class KalturaDropFolderListResponse(KalturaListResponse):
    objects: List[KalturaDropFolder]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaDropFolder] = NotImplemented): ...

    def getObjects(self) -> List[KalturaDropFolder]: ...

class KalturaRemoteDropFolder(KalturaDropFolder):
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
            shouldValidateKS: bool = NotImplemented): ...
        pass

class KalturaDropFolderFileFilter(KalturaDropFolderFileBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idGreaterThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            dropFolderIdEqual: int = NotImplemented,
            dropFolderIdIn: str = NotImplemented,
            fileNameEqual: str = NotImplemented,
            fileNameIn: str = NotImplemented,
            fileNameLike: str = NotImplemented,
            statusEqual: KalturaDropFolderFileStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            parsedSlugEqual: str = NotImplemented,
            parsedSlugIn: str = NotImplemented,
            parsedSlugLike: str = NotImplemented,
            parsedFlavorEqual: str = NotImplemented,
            parsedFlavorIn: str = NotImplemented,
            parsedFlavorLike: str = NotImplemented,
            leadDropFolderFileIdEqual: int = NotImplemented,
            deletedDropFolderFileIdEqual: int = NotImplemented,
            entryIdEqual: str = NotImplemented,
            errorCodeEqual: KalturaDropFolderFileErrorCode = NotImplemented,
            errorCodeIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaDropFolderFilter(KalturaDropFolderBaseFilter):
    currentDc: KalturaNullableBoolean
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

    def getCurrentDc(self) -> KalturaNullableBoolean: ...
    def setCurrentDc(self, newCurrentDc: KalturaNullableBoolean) -> None: ...

class KalturaFtpDropFolder(KalturaRemoteDropFolder):
    host: str
    port: int
    username: str
    password: str
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
            host: str = NotImplemented,
            port: int = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented): ...

    def getHost(self) -> str: ...
    def setHost(self, newHost: str) -> None: ...
    def getPort(self) -> int: ...
    def setPort(self, newPort: int) -> None: ...
    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...

class KalturaSshDropFolder(KalturaRemoteDropFolder):
    host: str
    port: int
    username: str
    password: str
    privateKey: str
    publicKey: str
    passPhrase: str
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
            host: str = NotImplemented,
            port: int = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented,
            privateKey: str = NotImplemented,
            publicKey: str = NotImplemented,
            passPhrase: str = NotImplemented): ...

    def getHost(self) -> str: ...
    def setHost(self, newHost: str) -> None: ...
    def getPort(self) -> int: ...
    def setPort(self, newPort: int) -> None: ...
    def getUsername(self) -> str: ...
    def setUsername(self, newUsername: str) -> None: ...
    def getPassword(self) -> str: ...
    def setPassword(self, newPassword: str) -> None: ...
    def getPrivateKey(self) -> str: ...
    def setPrivateKey(self, newPrivateKey: str) -> None: ...
    def getPublicKey(self) -> str: ...
    def setPublicKey(self, newPublicKey: str) -> None: ...
    def getPassPhrase(self) -> str: ...
    def setPassPhrase(self, newPassPhrase: str) -> None: ...

class KalturaDropFolderImportJobData(KalturaSshImportJobData):
    dropFolderFileId: int
    def __init__(self,
            srcFileUrl: str = NotImplemented,
            destFileLocalPath: str = NotImplemented,
            flavorAssetId: str = NotImplemented,
            fileSize: int = NotImplemented,
            destFileSharedPath: str = NotImplemented,
            urlHeaders: List[KalturaString] = NotImplemented,
            shouldRedirect: bool = NotImplemented,
            privateKey: str = NotImplemented,
            publicKey: str = NotImplemented,
            passPhrase: str = NotImplemented,
            dropFolderFileId: int = NotImplemented): ...

    def getDropFolderFileId(self) -> int: ...
    def setDropFolderFileId(self, newDropFolderFileId: int) -> None: ...

class KalturaRemoteDropFolderBaseFilter(KalturaDropFolderFilter):
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

class KalturaScpDropFolder(KalturaSshDropFolder):
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
            host: str = NotImplemented,
            port: int = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented,
            privateKey: str = NotImplemented,
            publicKey: str = NotImplemented,
            passPhrase: str = NotImplemented): ...
        pass

class KalturaSftpDropFolder(KalturaSshDropFolder):
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
            host: str = NotImplemented,
            port: int = NotImplemented,
            username: str = NotImplemented,
            password: str = NotImplemented,
            privateKey: str = NotImplemented,
            publicKey: str = NotImplemented,
            passPhrase: str = NotImplemented): ...
        pass

class KalturaDropFolderFileResource(KalturaGenericDataCenterContentResource):
    dropFolderFileId: int
    def __init__(self,
            dropFolderFileId: int = NotImplemented): ...

    def getDropFolderFileId(self) -> int: ...
    def setDropFolderFileId(self, newDropFolderFileId: int) -> None: ...

class KalturaRemoteDropFolderFilter(KalturaRemoteDropFolderBaseFilter):
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

class KalturaFtpDropFolderBaseFilter(KalturaRemoteDropFolderFilter):
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

class KalturaSshDropFolderBaseFilter(KalturaRemoteDropFolderFilter):
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

class KalturaFtpDropFolderFilter(KalturaFtpDropFolderBaseFilter):
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

class KalturaSshDropFolderFilter(KalturaSshDropFolderBaseFilter):
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

class KalturaScpDropFolderBaseFilter(KalturaSshDropFolderFilter):
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

class KalturaSftpDropFolderBaseFilter(KalturaSshDropFolderFilter):
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

class KalturaScpDropFolderFilter(KalturaScpDropFolderBaseFilter):
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

class KalturaSftpDropFolderFilter(KalturaSftpDropFolderBaseFilter):
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

class KalturaDropFolderService(KalturaServiceBase):
    def add(self, dropFolder: KalturaDropFolder) -> KalturaDropFolder: ...
    def delete(self, dropFolderId: int) -> KalturaDropFolder: ...
    def freeExclusiveDropFolder(self, dropFolderId: int, errorCode: str = NotImplemented, errorDescription: str = NotImplemented) -> KalturaDropFolder: ...
    def get(self, dropFolderId: int) -> KalturaDropFolder: ...
    def getExclusiveDropFolder(self, tag: str, maxTime: int) -> KalturaDropFolder: ...
    def list(self, filter: KalturaDropFolderFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaDropFolderListResponse: ...
    def update(self, dropFolderId: int, dropFolder: KalturaDropFolder) -> KalturaDropFolder: ...
    def updateStatus(self, dropFolderId: int, status: int) -> None: ...

class KalturaDropFolderFileService(KalturaServiceBase):
    def add(self, dropFolderFile: KalturaDropFolderFile) -> KalturaDropFolderFile: ...
    def delete(self, dropFolderFileId: int) -> KalturaDropFolderFile: ...
    def get(self, dropFolderFileId: int) -> KalturaDropFolderFile: ...
    def ignore(self, dropFolderFileId: int) -> KalturaDropFolderFile: ...
    def list(self, filter: KalturaDropFolderFileFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaDropFolderFileListResponse: ...
    def update(self, dropFolderFileId: int, dropFolderFile: KalturaDropFolderFile) -> KalturaDropFolderFile: ...
    def updateStatus(self, dropFolderFileId: int, status: int) -> KalturaDropFolderFile: ...

class KalturaDropFolderClientPluginServicesProxy:
    dropFolder: KalturaDropFolderService
    dropFolderFile: KalturaDropFolderFileService