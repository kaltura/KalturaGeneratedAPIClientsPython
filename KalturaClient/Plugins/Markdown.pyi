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
from .Attachment import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaMarkdownAssetOrderBy(object):
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

class KalturaMarkdownProviderType(object):
    KAI = "0"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaMarkdownAsset(KalturaAttachmentAsset):
    accuracy: int
    providerType: KalturaMarkdownProviderType
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
            status: KalturaAttachmentAssetStatus = NotImplemented,
            accuracy: int = NotImplemented,
            providerType: KalturaMarkdownProviderType = NotImplemented): ...

    def getAccuracy(self) -> int: ...
    def setAccuracy(self, newAccuracy: int) -> None: ...
    def getProviderType(self) -> KalturaMarkdownProviderType: ...
    def setProviderType(self, newProviderType: KalturaMarkdownProviderType) -> None: ...

class KalturaMarkdownAssetListResponse(KalturaListResponse):
    objects: List[KalturaMarkdownAsset]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaMarkdownAsset] = NotImplemented): ...

    def getObjects(self) -> List[KalturaMarkdownAsset]: ...

class KalturaMarkdownAssetBaseFilter(KalturaTextualAttachmentAssetFilter):
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

class KalturaMarkdownAssetFilter(KalturaMarkdownAssetBaseFilter):
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

class KalturaMarkdownClientPluginServicesProxy: