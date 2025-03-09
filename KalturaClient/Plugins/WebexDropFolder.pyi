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
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaWebexDropFolderFileOrderBy(object):
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

class KalturaWebexDropFolderOrderBy(object):
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

class KalturaWebexDropFolder(KalturaDropFolder):
    webexUserId: str
    webexPassword: str
    webexSiteId: int
    webexPartnerId: str
    webexServiceUrl: str
    webexHostIdMetadataFieldName: str
    deleteFromRecycleBin: bool
    webexServiceType: str
    webexSiteName: str
    deleteFromTimestamp: int
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
            webexUserId: str = NotImplemented,
            webexPassword: str = NotImplemented,
            webexSiteId: int = NotImplemented,
            webexPartnerId: str = NotImplemented,
            webexServiceUrl: str = NotImplemented,
            webexHostIdMetadataFieldName: str = NotImplemented,
            deleteFromRecycleBin: bool = NotImplemented,
            webexServiceType: str = NotImplemented,
            webexSiteName: str = NotImplemented,
            deleteFromTimestamp: int = NotImplemented): ...

    def getWebexUserId(self) -> str: ...
    def setWebexUserId(self, newWebexUserId: str) -> None: ...
    def getWebexPassword(self) -> str: ...
    def setWebexPassword(self, newWebexPassword: str) -> None: ...
    def getWebexSiteId(self) -> int: ...
    def setWebexSiteId(self, newWebexSiteId: int) -> None: ...
    def getWebexPartnerId(self) -> str: ...
    def setWebexPartnerId(self, newWebexPartnerId: str) -> None: ...
    def getWebexServiceUrl(self) -> str: ...
    def setWebexServiceUrl(self, newWebexServiceUrl: str) -> None: ...
    def getWebexHostIdMetadataFieldName(self) -> str: ...
    def setWebexHostIdMetadataFieldName(self, newWebexHostIdMetadataFieldName: str) -> None: ...
    def getDeleteFromRecycleBin(self) -> bool: ...
    def setDeleteFromRecycleBin(self, newDeleteFromRecycleBin: bool) -> None: ...
    def getWebexServiceType(self) -> str: ...
    def setWebexServiceType(self, newWebexServiceType: str) -> None: ...
    def getWebexSiteName(self) -> str: ...
    def setWebexSiteName(self, newWebexSiteName: str) -> None: ...
    def getDeleteFromTimestamp(self) -> int: ...
    def setDeleteFromTimestamp(self, newDeleteFromTimestamp: int) -> None: ...

class KalturaWebexDropFolderFile(KalturaDropFolderFile):
    recordingId: int
    webexHostId: str
    description: str
    confId: str
    contentUrl: str
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
            recordingId: int = NotImplemented,
            webexHostId: str = NotImplemented,
            description: str = NotImplemented,
            confId: str = NotImplemented,
            contentUrl: str = NotImplemented): ...

    def getRecordingId(self) -> int: ...
    def setRecordingId(self, newRecordingId: int) -> None: ...
    def getWebexHostId(self) -> str: ...
    def setWebexHostId(self, newWebexHostId: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getConfId(self) -> str: ...
    def setConfId(self, newConfId: str) -> None: ...
    def getContentUrl(self) -> str: ...
    def setContentUrl(self, newContentUrl: str) -> None: ...

class KalturaWebexDropFolderContentProcessorJobData(KalturaDropFolderContentProcessorJobData):
    description: str
    webexHostId: str
    def __init__(self,
            dropFolderId: int = NotImplemented,
            dropFolderFileIds: str = NotImplemented,
            parsedSlug: str = NotImplemented,
            contentMatchPolicy: KalturaDropFolderContentFileHandlerMatchPolicy = NotImplemented,
            conversionProfileId: int = NotImplemented,
            parsedUserId: str = NotImplemented,
            description: str = NotImplemented,
            webexHostId: str = NotImplemented): ...

    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getWebexHostId(self) -> str: ...
    def setWebexHostId(self, newWebexHostId: str) -> None: ...

class KalturaWebexDropFolderBaseFilter(KalturaDropFolderFilter):
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

class KalturaWebexDropFolderFileBaseFilter(KalturaDropFolderFileFilter):
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

class KalturaWebexDropFolderFileFilter(KalturaWebexDropFolderFileBaseFilter):
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

class KalturaWebexDropFolderFilter(KalturaWebexDropFolderBaseFilter):
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

class KalturaWebexDropFolderClientPluginServicesProxy: