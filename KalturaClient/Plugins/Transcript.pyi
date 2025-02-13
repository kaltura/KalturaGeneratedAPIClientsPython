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

class KalturaTranscriptAssetOrderBy(object):
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

class KalturaTranscriptProviderType(object):
    CIELO24 = "cielo24.Cielo24"
    VOICEBASE = "voicebase.Voicebase"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaTranscriptAsset(KalturaAttachmentAsset):
    accuracy: float
    humanVerified: KalturaNullableBoolean
    language: KalturaLanguage
    providerType: KalturaTranscriptProviderType
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
            accuracy: float = NotImplemented,
            humanVerified: KalturaNullableBoolean = NotImplemented,
            language: KalturaLanguage = NotImplemented,
            providerType: KalturaTranscriptProviderType = NotImplemented): ...

    def getAccuracy(self) -> float: ...
    def setAccuracy(self, newAccuracy: float) -> None: ...
    def getHumanVerified(self) -> KalturaNullableBoolean: ...
    def setHumanVerified(self, newHumanVerified: KalturaNullableBoolean) -> None: ...
    def getLanguage(self) -> KalturaLanguage: ...
    def setLanguage(self, newLanguage: KalturaLanguage) -> None: ...
    def getProviderType(self) -> KalturaTranscriptProviderType: ...
    def setProviderType(self, newProviderType: KalturaTranscriptProviderType) -> None: ...

class KalturaEntryTranscriptAssetSearchItem(KalturaSearchItem):
    contentLike: str
    contentMultiLikeOr: str
    contentMultiLikeAnd: str
    def __init__(self,
            contentLike: str = NotImplemented,
            contentMultiLikeOr: str = NotImplemented,
            contentMultiLikeAnd: str = NotImplemented): ...

    def getContentLike(self) -> str: ...
    def setContentLike(self, newContentLike: str) -> None: ...
    def getContentMultiLikeOr(self) -> str: ...
    def setContentMultiLikeOr(self, newContentMultiLikeOr: str) -> None: ...
    def getContentMultiLikeAnd(self) -> str: ...
    def setContentMultiLikeAnd(self, newContentMultiLikeAnd: str) -> None: ...

class KalturaTranscriptAssetListResponse(KalturaListResponse):
    objects: List[KalturaTranscriptAsset]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaTranscriptAsset] = NotImplemented): ...

    def getObjects(self) -> List[KalturaTranscriptAsset]: ...

class KalturaTranscriptAssetBaseFilter(KalturaAttachmentAssetFilter):
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

class KalturaTranscriptAssetFilter(KalturaTranscriptAssetBaseFilter):
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

class KalturaTranscriptClientPluginServicesProxy: