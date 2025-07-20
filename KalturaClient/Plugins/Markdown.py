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
# @package Kaltura
# @subpackage Client
from __future__ import absolute_import

from .Core import *
from .Attachment import *
from ..Base import (
    getXmlNodeBool,
    getXmlNodeFloat,
    getXmlNodeInt,
    getXmlNodeText,
    KalturaClientPlugin,
    KalturaEnumsFactory,
    KalturaObjectBase,
    KalturaObjectFactory,
    KalturaParams,
    KalturaServiceBase,
)

########## enums ##########
# @package Kaltura
# @subpackage Client
class KalturaMarkdownAssetOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    DELETED_AT_ASC = "+deletedAt"
    SIZE_ASC = "+size"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    DELETED_AT_DESC = "-deletedAt"
    SIZE_DESC = "-size"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaMarkdownProviderType(object):
    KAI = "0"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaMarkdownAsset(KalturaAttachmentAsset):
    def __init__(self,
            id = NotImplemented,
            entryId = NotImplemented,
            partnerId = NotImplemented,
            version = NotImplemented,
            size = NotImplemented,
            tags = NotImplemented,
            fileExt = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            deletedAt = NotImplemented,
            description = NotImplemented,
            partnerData = NotImplemented,
            partnerDescription = NotImplemented,
            actualSourceAssetParamsIds = NotImplemented,
            sizeInBytes = NotImplemented,
            filename = NotImplemented,
            title = NotImplemented,
            format = NotImplemented,
            status = NotImplemented,
            accuracy = NotImplemented,
            providerType = NotImplemented):
        KalturaAttachmentAsset.__init__(self,
            id,
            entryId,
            partnerId,
            version,
            size,
            tags,
            fileExt,
            createdAt,
            updatedAt,
            deletedAt,
            description,
            partnerData,
            partnerDescription,
            actualSourceAssetParamsIds,
            sizeInBytes,
            filename,
            title,
            format,
            status)

        # The percentage accuracy of the markdown - values between 0 and 100
        # @var int
        self.accuracy = accuracy

        # The provider of the markdown
        # @var KalturaMarkdownProviderType
        self.providerType = providerType


    PROPERTY_LOADERS = {
        'accuracy': getXmlNodeInt, 
        'providerType': (KalturaEnumsFactory.createString, "KalturaMarkdownProviderType"), 
    }

    def fromXml(self, node):
        KalturaAttachmentAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMarkdownAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAttachmentAsset.toParams(self)
        kparams.put("objectType", "KalturaMarkdownAsset")
        kparams.addIntIfDefined("accuracy", self.accuracy)
        kparams.addStringEnumIfDefined("providerType", self.providerType)
        return kparams

    def getAccuracy(self):
        return self.accuracy

    def setAccuracy(self, newAccuracy):
        self.accuracy = newAccuracy

    def getProviderType(self):
        return self.providerType

    def setProviderType(self, newProviderType):
        self.providerType = newProviderType


# @package Kaltura
# @subpackage Client
class KalturaMarkdownAssetListResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaMarkdownAsset]
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaMarkdownAsset'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMarkdownAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaMarkdownAssetListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaMarkdownAssetBaseFilter(KalturaTextualAttachmentAssetFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            entryIdEqual = NotImplemented,
            entryIdIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            sizeGreaterThanOrEqual = NotImplemented,
            sizeLessThanOrEqual = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            deletedAtGreaterThanOrEqual = NotImplemented,
            deletedAtLessThanOrEqual = NotImplemented,
            typeIn = NotImplemented,
            formatEqual = NotImplemented,
            formatIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            statusNotIn = NotImplemented):
        KalturaTextualAttachmentAssetFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            entryIdEqual,
            entryIdIn,
            partnerIdEqual,
            partnerIdIn,
            sizeGreaterThanOrEqual,
            sizeLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            deletedAtGreaterThanOrEqual,
            deletedAtLessThanOrEqual,
            typeIn,
            formatEqual,
            formatIn,
            statusEqual,
            statusIn,
            statusNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaTextualAttachmentAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMarkdownAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaTextualAttachmentAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaMarkdownAssetBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaMarkdownAssetFilter(KalturaMarkdownAssetBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            entryIdEqual = NotImplemented,
            entryIdIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            sizeGreaterThanOrEqual = NotImplemented,
            sizeLessThanOrEqual = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            deletedAtGreaterThanOrEqual = NotImplemented,
            deletedAtLessThanOrEqual = NotImplemented,
            typeIn = NotImplemented,
            formatEqual = NotImplemented,
            formatIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            statusNotIn = NotImplemented):
        KalturaMarkdownAssetBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            entryIdEqual,
            entryIdIn,
            partnerIdEqual,
            partnerIdIn,
            sizeGreaterThanOrEqual,
            sizeLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            deletedAtGreaterThanOrEqual,
            deletedAtLessThanOrEqual,
            typeIn,
            formatEqual,
            formatIn,
            statusEqual,
            statusIn,
            statusNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaMarkdownAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMarkdownAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMarkdownAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaMarkdownAssetFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaMarkdownClientPlugin(KalturaClientPlugin):
    # KalturaMarkdownClientPlugin
    instance = None

    # @return KalturaMarkdownClientPlugin
    @staticmethod
    def get():
        if KalturaMarkdownClientPlugin.instance == None:
            KalturaMarkdownClientPlugin.instance = KalturaMarkdownClientPlugin()
        return KalturaMarkdownClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaMarkdownAssetOrderBy': KalturaMarkdownAssetOrderBy,
            'KalturaMarkdownProviderType': KalturaMarkdownProviderType,
        }

    def getTypes(self):
        return {
            'KalturaMarkdownAsset': KalturaMarkdownAsset,
            'KalturaMarkdownAssetListResponse': KalturaMarkdownAssetListResponse,
            'KalturaMarkdownAssetBaseFilter': KalturaMarkdownAssetBaseFilter,
            'KalturaMarkdownAssetFilter': KalturaMarkdownAssetFilter,
        }

    # @return string
    def getName(self):
        return 'markdown'

