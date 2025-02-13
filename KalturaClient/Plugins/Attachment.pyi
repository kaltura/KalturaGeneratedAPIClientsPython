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

class KalturaAttachmentAssetStatus(object):
    ERROR = -1
    QUEUED = 0
    READY = 2
    DELETED = 3
    IMPORTING = 7
    EXPORTING = 9

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaAttachmentAssetOrderBy(object):
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

class KalturaAttachmentType(object):
    TEXT = "1"
    MEDIA = "2"
    DOCUMENT = "3"
    JSON = "4"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaAttachmentAsset(KalturaAsset):
    filename: str
    title: str
    format: KalturaAttachmentType
    status: KalturaAttachmentAssetStatus
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
            filename: str = NotImplemented,
            title: str = NotImplemented,
            format: KalturaAttachmentType = NotImplemented,
            status: KalturaAttachmentAssetStatus = NotImplemented): ...

    def getFilename(self) -> str: ...
    def setFilename(self, newFilename: str) -> None: ...
    def getTitle(self) -> str: ...
    def setTitle(self, newTitle: str) -> None: ...
    def getFormat(self) -> KalturaAttachmentType: ...
    def setFormat(self, newFormat: KalturaAttachmentType) -> None: ...
    def getStatus(self) -> KalturaAttachmentAssetStatus: ...

class KalturaAttachmentAssetListResponse(KalturaListResponse):
    objects: List[KalturaAttachmentAsset]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaAttachmentAsset] = NotImplemented): ...

    def getObjects(self) -> List[KalturaAttachmentAsset]: ...

class KalturaAttachmentServeOptions(KalturaAssetServeOptions):
    def __init__(self,
            download: bool = NotImplemented,
            referrer: str = NotImplemented): ...
        pass

class KalturaAttachmentAssetBaseFilter(KalturaAssetFilter):
    formatEqual: KalturaAttachmentType
    formatIn: str
    statusEqual: KalturaAttachmentAssetStatus
    statusIn: str
    statusNotIn: str
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
            formatEqual: KalturaAttachmentType = NotImplemented,
            formatIn: str = NotImplemented,
            statusEqual: KalturaAttachmentAssetStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented): ...

    def getFormatEqual(self) -> KalturaAttachmentType: ...
    def setFormatEqual(self, newFormatEqual: KalturaAttachmentType) -> None: ...
    def getFormatIn(self) -> str: ...
    def setFormatIn(self, newFormatIn: str) -> None: ...
    def getStatusEqual(self) -> KalturaAttachmentAssetStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaAttachmentAssetStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getStatusNotIn(self) -> str: ...
    def setStatusNotIn(self, newStatusNotIn: str) -> None: ...

class KalturaAttachmentAssetFilter(KalturaAttachmentAssetBaseFilter):
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
            formatEqual: KalturaAttachmentType = NotImplemented,
            formatIn: str = NotImplemented,
            statusEqual: KalturaAttachmentAssetStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented): ...
        pass

class KalturaAttachmentAssetService(KalturaServiceBase):
    def add(self, entryId: str, attachmentAsset: KalturaAttachmentAsset) -> KalturaAttachmentAsset: ...
    def delete(self, attachmentAssetId: str) -> None: ...
    def get(self, attachmentAssetId: str) -> KalturaAttachmentAsset: ...
    def getRemotePaths(self, id: str) -> KalturaRemotePathListResponse: ...
    def getUrl(self, id: str, storageId: int = NotImplemented) -> str: ...
    def list(self, filter: KalturaAssetFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaAttachmentAssetListResponse: ...
    def serve(self, attachmentAssetId: str, serveOptions: KalturaAttachmentServeOptions = NotImplemented) -> IO[Any]: ...
    def setContent(self, id: str, contentResource: KalturaContentResource) -> KalturaAttachmentAsset: ...
    def update(self, id: str, attachmentAsset: KalturaAttachmentAsset) -> KalturaAttachmentAsset: ...

class KalturaAttachmentClientPluginServicesProxy:
    attachmentAsset: KalturaAttachmentAssetService