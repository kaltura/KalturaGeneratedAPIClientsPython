# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2019  Kaltura Inc.
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
class KalturaCaptionAssetStatus(object):
    ERROR = -1
    QUEUED = 0
    READY = 2
    DELETED = 3
    IMPORTING = 7
    EXPORTING = 9

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCaptionAssetOrderBy(object):
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
class KalturaCaptionParamsOrderBy(object):

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCaptionType(object):
    SRT = "1"
    DFXP = "2"
    WEBVTT = "3"
    CAP = "4"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaCaptionAsset(KalturaAsset):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            partnerId=NotImplemented,
            version=NotImplemented,
            size=NotImplemented,
            tags=NotImplemented,
            fileExt=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            deletedAt=NotImplemented,
            description=NotImplemented,
            partnerData=NotImplemented,
            partnerDescription=NotImplemented,
            actualSourceAssetParamsIds=NotImplemented,
            captionParamsId=NotImplemented,
            language=NotImplemented,
            languageCode=NotImplemented,
            isDefault=NotImplemented,
            label=NotImplemented,
            format=NotImplemented,
            status=NotImplemented,
            parentId=NotImplemented,
            accuracy=NotImplemented,
            displayOnPlayer=NotImplemented):
        KalturaAsset.__init__(self,
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
            actualSourceAssetParamsIds)

        # The Caption Params used to create this Caption Asset
        # @var int
        # @insertonly
        self.captionParamsId = captionParamsId

        # The language of the caption asset content
        # @var KalturaLanguage
        self.language = language

        # The language of the caption asset content
        # @var KalturaLanguageCode
        # @readonly
        self.languageCode = languageCode

        # Is default caption asset of the entry
        # @var KalturaNullableBoolean
        self.isDefault = isDefault

        # Friendly label
        # @var string
        self.label = label

        # The caption format
        # @var KalturaCaptionType
        # @insertonly
        self.format = format

        # The status of the asset
        # @var KalturaCaptionAssetStatus
        # @readonly
        self.status = status

        # The parent id of the asset
        # @var string
        # @insertonly
        self.parentId = parentId

        # The Accuracy of the caption content
        # @var int
        self.accuracy = accuracy

        # The Accuracy of the caption content
        # @var bool
        self.displayOnPlayer = displayOnPlayer


    PROPERTY_LOADERS = {
        'captionParamsId': getXmlNodeInt, 
        'language': (KalturaEnumsFactory.createString, "KalturaLanguage"), 
        'languageCode': (KalturaEnumsFactory.createString, "KalturaLanguageCode"), 
        'isDefault': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'label': getXmlNodeText, 
        'format': (KalturaEnumsFactory.createString, "KalturaCaptionType"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaCaptionAssetStatus"), 
        'parentId': getXmlNodeText, 
        'accuracy': getXmlNodeInt, 
        'displayOnPlayer': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaCaptionAsset")
        kparams.addIntIfDefined("captionParamsId", self.captionParamsId)
        kparams.addStringEnumIfDefined("language", self.language)
        kparams.addIntEnumIfDefined("isDefault", self.isDefault)
        kparams.addStringIfDefined("label", self.label)
        kparams.addStringEnumIfDefined("format", self.format)
        kparams.addStringIfDefined("parentId", self.parentId)
        kparams.addIntIfDefined("accuracy", self.accuracy)
        kparams.addBoolIfDefined("displayOnPlayer", self.displayOnPlayer)
        return kparams

    def getCaptionParamsId(self):
        return self.captionParamsId

    def setCaptionParamsId(self, newCaptionParamsId):
        self.captionParamsId = newCaptionParamsId

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getLanguageCode(self):
        return self.languageCode

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getLabel(self):
        return self.label

    def setLabel(self, newLabel):
        self.label = newLabel

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getStatus(self):
        return self.status

    def getParentId(self):
        return self.parentId

    def setParentId(self, newParentId):
        self.parentId = newParentId

    def getAccuracy(self):
        return self.accuracy

    def setAccuracy(self, newAccuracy):
        self.accuracy = newAccuracy

    def getDisplayOnPlayer(self):
        return self.displayOnPlayer

    def setDisplayOnPlayer(self, newDisplayOnPlayer):
        self.displayOnPlayer = newDisplayOnPlayer


# @package Kaltura
# @subpackage Client
class KalturaCaptionParams(KalturaAssetParams):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            isSystemDefault=NotImplemented,
            tags=NotImplemented,
            requiredPermissions=NotImplemented,
            sourceRemoteStorageProfileId=NotImplemented,
            remoteStorageProfileIds=NotImplemented,
            mediaParserType=NotImplemented,
            sourceAssetParamsIds=NotImplemented,
            language=NotImplemented,
            isDefault=NotImplemented,
            label=NotImplemented,
            format=NotImplemented,
            sourceParamsId=NotImplemented):
        KalturaAssetParams.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            createdAt,
            isSystemDefault,
            tags,
            requiredPermissions,
            sourceRemoteStorageProfileId,
            remoteStorageProfileIds,
            mediaParserType,
            sourceAssetParamsIds)

        # The language of the caption content
        # @var KalturaLanguage
        # @insertonly
        self.language = language

        # Is default caption asset of the entry
        # @var KalturaNullableBoolean
        self.isDefault = isDefault

        # Friendly label
        # @var string
        self.label = label

        # The caption format
        # @var KalturaCaptionType
        # @insertonly
        self.format = format

        # Id of the caption params or the flavor params to be used as source for the caption creation
        # @var int
        self.sourceParamsId = sourceParamsId


    PROPERTY_LOADERS = {
        'language': (KalturaEnumsFactory.createString, "KalturaLanguage"), 
        'isDefault': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'label': getXmlNodeText, 
        'format': (KalturaEnumsFactory.createString, "KalturaCaptionType"), 
        'sourceParamsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAssetParams.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParams.toParams(self)
        kparams.put("objectType", "KalturaCaptionParams")
        kparams.addStringEnumIfDefined("language", self.language)
        kparams.addIntEnumIfDefined("isDefault", self.isDefault)
        kparams.addStringIfDefined("label", self.label)
        kparams.addStringEnumIfDefined("format", self.format)
        kparams.addIntIfDefined("sourceParamsId", self.sourceParamsId)
        return kparams

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getLabel(self):
        return self.label

    def setLabel(self, newLabel):
        self.label = newLabel

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getSourceParamsId(self):
        return self.sourceParamsId

    def setSourceParamsId(self, newSourceParamsId):
        self.sourceParamsId = newSourceParamsId


# @package Kaltura
# @subpackage Client
class KalturaCaptionPlaybackPluginData(KalturaObjectBase):
    def __init__(self,
            label=NotImplemented,
            format=NotImplemented,
            language=NotImplemented,
            webVttUrl=NotImplemented,
            url=NotImplemented,
            isDefault=NotImplemented,
            languageCode=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.label = label

        # @var string
        self.format = format

        # @var string
        self.language = language

        # @var string
        self.webVttUrl = webVttUrl

        # @var string
        self.url = url

        # @var bool
        self.isDefault = isDefault

        # @var string
        self.languageCode = languageCode


    PROPERTY_LOADERS = {
        'label': getXmlNodeText, 
        'format': getXmlNodeText, 
        'language': getXmlNodeText, 
        'webVttUrl': getXmlNodeText, 
        'url': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
        'languageCode': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionPlaybackPluginData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCaptionPlaybackPluginData")
        kparams.addStringIfDefined("label", self.label)
        kparams.addStringIfDefined("format", self.format)
        kparams.addStringIfDefined("language", self.language)
        kparams.addStringIfDefined("webVttUrl", self.webVttUrl)
        kparams.addStringIfDefined("url", self.url)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        kparams.addStringIfDefined("languageCode", self.languageCode)
        return kparams

    def getLabel(self):
        return self.label

    def setLabel(self, newLabel):
        self.label = newLabel

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getWebVttUrl(self):
        return self.webVttUrl

    def setWebVttUrl(self, newWebVttUrl):
        self.webVttUrl = newWebVttUrl

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getLanguageCode(self):
        return self.languageCode

    def setLanguageCode(self, newLanguageCode):
        self.languageCode = newLanguageCode


# @package Kaltura
# @subpackage Client
class KalturaCaptionAssetListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaCaptionAsset
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaCaptionAsset'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCaptionAssetListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaCaptionParamsListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaCaptionParams
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaCaptionParams'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionParamsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCaptionParamsListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaCopyCaptionsJobData(KalturaJobData):
    def __init__(self,
            entryId=NotImplemented,
            clipsDescriptionArray=NotImplemented,
            fullCopy=NotImplemented):
        KalturaJobData.__init__(self)

        # entry Id
        # @var string
        self.entryId = entryId

        # an array of source start time and duration
        # @var array of KalturaClipDescription
        self.clipsDescriptionArray = clipsDescriptionArray

        # @var bool
        self.fullCopy = fullCopy


    PROPERTY_LOADERS = {
        'entryId': getXmlNodeText, 
        'clipsDescriptionArray': (KalturaObjectFactory.createArray, 'KalturaClipDescription'), 
        'fullCopy': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCopyCaptionsJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaJobData.toParams(self)
        kparams.put("objectType", "KalturaCopyCaptionsJobData")
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addArrayIfDefined("clipsDescriptionArray", self.clipsDescriptionArray)
        kparams.addBoolIfDefined("fullCopy", self.fullCopy)
        return kparams

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getClipsDescriptionArray(self):
        return self.clipsDescriptionArray

    def setClipsDescriptionArray(self, newClipsDescriptionArray):
        self.clipsDescriptionArray = newClipsDescriptionArray

    def getFullCopy(self):
        return self.fullCopy

    def setFullCopy(self, newFullCopy):
        self.fullCopy = newFullCopy


# @package Kaltura
# @subpackage Client
class KalturaParseMultiLanguageCaptionAssetJobData(KalturaJobData):
    def __init__(self,
            multiLanaguageCaptionAssetId=NotImplemented,
            entryId=NotImplemented,
            fileLocation=NotImplemented,
            fileEncryptionKey=NotImplemented):
        KalturaJobData.__init__(self)

        # @var string
        self.multiLanaguageCaptionAssetId = multiLanaguageCaptionAssetId

        # @var string
        self.entryId = entryId

        # @var string
        self.fileLocation = fileLocation

        # @var string
        self.fileEncryptionKey = fileEncryptionKey


    PROPERTY_LOADERS = {
        'multiLanaguageCaptionAssetId': getXmlNodeText, 
        'entryId': getXmlNodeText, 
        'fileLocation': getXmlNodeText, 
        'fileEncryptionKey': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaParseMultiLanguageCaptionAssetJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaJobData.toParams(self)
        kparams.put("objectType", "KalturaParseMultiLanguageCaptionAssetJobData")
        kparams.addStringIfDefined("multiLanaguageCaptionAssetId", self.multiLanaguageCaptionAssetId)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addStringIfDefined("fileLocation", self.fileLocation)
        kparams.addStringIfDefined("fileEncryptionKey", self.fileEncryptionKey)
        return kparams

    def getMultiLanaguageCaptionAssetId(self):
        return self.multiLanaguageCaptionAssetId

    def setMultiLanaguageCaptionAssetId(self, newMultiLanaguageCaptionAssetId):
        self.multiLanaguageCaptionAssetId = newMultiLanaguageCaptionAssetId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getFileLocation(self):
        return self.fileLocation

    def setFileLocation(self, newFileLocation):
        self.fileLocation = newFileLocation

    def getFileEncryptionKey(self):
        return self.fileEncryptionKey

    def setFileEncryptionKey(self, newFileEncryptionKey):
        self.fileEncryptionKey = newFileEncryptionKey


# @package Kaltura
# @subpackage Client
class KalturaCaptionAssetBaseFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            sizeGreaterThanOrEqual=NotImplemented,
            sizeLessThanOrEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            typeIn=NotImplemented,
            captionParamsIdEqual=NotImplemented,
            captionParamsIdIn=NotImplemented,
            formatEqual=NotImplemented,
            formatIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaAssetFilter.__init__(self,
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
            typeIn)

        # @var int
        self.captionParamsIdEqual = captionParamsIdEqual

        # @var string
        self.captionParamsIdIn = captionParamsIdIn

        # @var KalturaCaptionType
        self.formatEqual = formatEqual

        # @var string
        self.formatIn = formatIn

        # @var KalturaCaptionAssetStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var string
        self.statusNotIn = statusNotIn


    PROPERTY_LOADERS = {
        'captionParamsIdEqual': getXmlNodeInt, 
        'captionParamsIdIn': getXmlNodeText, 
        'formatEqual': (KalturaEnumsFactory.createString, "KalturaCaptionType"), 
        'formatIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaCaptionAssetStatus"), 
        'statusIn': getXmlNodeText, 
        'statusNotIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionAssetBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaCaptionAssetBaseFilter")
        kparams.addIntIfDefined("captionParamsIdEqual", self.captionParamsIdEqual)
        kparams.addStringIfDefined("captionParamsIdIn", self.captionParamsIdIn)
        kparams.addStringEnumIfDefined("formatEqual", self.formatEqual)
        kparams.addStringIfDefined("formatIn", self.formatIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("statusNotIn", self.statusNotIn)
        return kparams

    def getCaptionParamsIdEqual(self):
        return self.captionParamsIdEqual

    def setCaptionParamsIdEqual(self, newCaptionParamsIdEqual):
        self.captionParamsIdEqual = newCaptionParamsIdEqual

    def getCaptionParamsIdIn(self):
        return self.captionParamsIdIn

    def setCaptionParamsIdIn(self, newCaptionParamsIdIn):
        self.captionParamsIdIn = newCaptionParamsIdIn

    def getFormatEqual(self):
        return self.formatEqual

    def setFormatEqual(self, newFormatEqual):
        self.formatEqual = newFormatEqual

    def getFormatIn(self):
        return self.formatIn

    def setFormatIn(self, newFormatIn):
        self.formatIn = newFormatIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getStatusNotIn(self):
        return self.statusNotIn

    def setStatusNotIn(self, newStatusNotIn):
        self.statusNotIn = newStatusNotIn


# @package Kaltura
# @subpackage Client
class KalturaCaptionParamsBaseFilter(KalturaAssetParamsFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            formatIn=NotImplemented):
        KalturaAssetParamsFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual)

        # @var KalturaCaptionType
        self.formatEqual = formatEqual

        # @var string
        self.formatIn = formatIn


    PROPERTY_LOADERS = {
        'formatEqual': (KalturaEnumsFactory.createString, "KalturaCaptionType"), 
        'formatIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetParamsFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionParamsBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetParamsFilter.toParams(self)
        kparams.put("objectType", "KalturaCaptionParamsBaseFilter")
        kparams.addStringEnumIfDefined("formatEqual", self.formatEqual)
        kparams.addStringIfDefined("formatIn", self.formatIn)
        return kparams

    def getFormatEqual(self):
        return self.formatEqual

    def setFormatEqual(self, newFormatEqual):
        self.formatEqual = newFormatEqual

    def getFormatIn(self):
        return self.formatIn

    def setFormatIn(self, newFormatIn):
        self.formatIn = newFormatIn


# @package Kaltura
# @subpackage Client
class KalturaCaptionAssetFilter(KalturaCaptionAssetBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            sizeGreaterThanOrEqual=NotImplemented,
            sizeLessThanOrEqual=NotImplemented,
            tagsLike=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            deletedAtGreaterThanOrEqual=NotImplemented,
            deletedAtLessThanOrEqual=NotImplemented,
            typeIn=NotImplemented,
            captionParamsIdEqual=NotImplemented,
            captionParamsIdIn=NotImplemented,
            formatEqual=NotImplemented,
            formatIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            statusNotIn=NotImplemented):
        KalturaCaptionAssetBaseFilter.__init__(self,
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
            captionParamsIdEqual,
            captionParamsIdIn,
            formatEqual,
            formatIn,
            statusEqual,
            statusIn,
            statusNotIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaCaptionAssetBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCaptionAssetBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaCaptionAssetFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaCaptionParamsFilter(KalturaCaptionParamsBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            isSystemDefaultEqual=NotImplemented,
            tagsEqual=NotImplemented,
            formatEqual=NotImplemented,
            formatIn=NotImplemented):
        KalturaCaptionParamsBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            systemNameEqual,
            systemNameIn,
            isSystemDefaultEqual,
            tagsEqual,
            formatEqual,
            formatIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaCaptionParamsBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCaptionParamsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCaptionParamsBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaCaptionParamsFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaCaptionAssetService(KalturaServiceBase):
    """Retrieve information and invoke actions on caption Asset"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, entryId, captionAsset):
        """Add caption asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addObjectIfDefined("captionAsset", captionAsset)
        self.client.queueServiceActionCall("caption_captionasset", "add", "KalturaCaptionAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionAsset')

    def delete(self, captionAssetId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("captionAssetId", captionAssetId)
        self.client.queueServiceActionCall("caption_captionasset", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, captionAssetId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("captionAssetId", captionAssetId)
        self.client.queueServiceActionCall("caption_captionasset", "get", "KalturaCaptionAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionAsset')

    def getRemotePaths(self, id):
        """Get remote storage existing paths for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("caption_captionasset", "getRemotePaths", "KalturaRemotePathListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaRemotePathListResponse')

    def getUrl(self, id, storageId = NotImplemented):
        """Get download URL for the asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addIntIfDefined("storageId", storageId);
        self.client.queueServiceActionCall("caption_captionasset", "getUrl", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List caption Assets by filter and pager"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("caption_captionasset", "list", "KalturaCaptionAssetListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionAssetListResponse')

    def serve(self, captionAssetId):
        """Serves caption by its id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("captionAssetId", captionAssetId)
        self.client.queueServiceActionCall('caption_captionasset', 'serve', None ,kparams)
        return self.client.getServeUrl()

    def serveByEntryId(self, entryId, captionParamId = NotImplemented):
        """Serves caption by entry id and thumnail params id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("captionParamId", captionParamId);
        self.client.queueServiceActionCall('caption_captionasset', 'serveByEntryId', None ,kparams)
        return self.client.getServeUrl()

    def serveWebVTT(self, captionAssetId, segmentDuration = 30, segmentIndex = NotImplemented, localTimestamp = 10000):
        """Serves caption by its id converting it to segmented WebVTT"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("captionAssetId", captionAssetId)
        kparams.addIntIfDefined("segmentDuration", segmentDuration);
        kparams.addIntIfDefined("segmentIndex", segmentIndex);
        kparams.addIntIfDefined("localTimestamp", localTimestamp);
        self.client.queueServiceActionCall('caption_captionasset', 'serveWebVTT', None ,kparams)
        return self.client.getServeUrl()

    def setAsDefault(self, captionAssetId):
        """Markss the caption as default and removes that mark from all other caption assets of the entry."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("captionAssetId", captionAssetId)
        self.client.queueServiceActionCall("caption_captionasset", "setAsDefault", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def setContent(self, id, contentResource):
        """Update content of caption asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("contentResource", contentResource)
        self.client.queueServiceActionCall("caption_captionasset", "setContent", "KalturaCaptionAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionAsset')

    def update(self, id, captionAsset):
        """Update caption asset"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addObjectIfDefined("captionAsset", captionAsset)
        self.client.queueServiceActionCall("caption_captionasset", "update", "KalturaCaptionAsset", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionAsset')


# @package Kaltura
# @subpackage Client
class KalturaCaptionParamsService(KalturaServiceBase):
    """Add & Manage Caption Params"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, captionParams):
        """Add new Caption Params"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("captionParams", captionParams)
        self.client.queueServiceActionCall("caption_captionparams", "add", "KalturaCaptionParams", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionParams')

    def delete(self, id):
        """Delete Caption Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("caption_captionparams", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, id):
        """Get Caption Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("caption_captionparams", "get", "KalturaCaptionParams", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionParams')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List Caption Params by filter with paging support (By default - all system default params will be listed too)"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("caption_captionparams", "list", "KalturaCaptionParamsListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionParamsListResponse')

    def update(self, id, captionParams):
        """Update Caption Params by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("captionParams", captionParams)
        self.client.queueServiceActionCall("caption_captionparams", "update", "KalturaCaptionParams", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaCaptionParams')

########## main ##########
class KalturaCaptionClientPlugin(KalturaClientPlugin):
    # KalturaCaptionClientPlugin
    instance = None

    # @return KalturaCaptionClientPlugin
    @staticmethod
    def get():
        if KalturaCaptionClientPlugin.instance == None:
            KalturaCaptionClientPlugin.instance = KalturaCaptionClientPlugin()
        return KalturaCaptionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'captionAsset': KalturaCaptionAssetService,
            'captionParams': KalturaCaptionParamsService,
        }

    def getEnums(self):
        return {
            'KalturaCaptionAssetStatus': KalturaCaptionAssetStatus,
            'KalturaCaptionAssetOrderBy': KalturaCaptionAssetOrderBy,
            'KalturaCaptionParamsOrderBy': KalturaCaptionParamsOrderBy,
            'KalturaCaptionType': KalturaCaptionType,
        }

    def getTypes(self):
        return {
            'KalturaCaptionAsset': KalturaCaptionAsset,
            'KalturaCaptionParams': KalturaCaptionParams,
            'KalturaCaptionPlaybackPluginData': KalturaCaptionPlaybackPluginData,
            'KalturaCaptionAssetListResponse': KalturaCaptionAssetListResponse,
            'KalturaCaptionParamsListResponse': KalturaCaptionParamsListResponse,
            'KalturaCopyCaptionsJobData': KalturaCopyCaptionsJobData,
            'KalturaParseMultiLanguageCaptionAssetJobData': KalturaParseMultiLanguageCaptionAssetJobData,
            'KalturaCaptionAssetBaseFilter': KalturaCaptionAssetBaseFilter,
            'KalturaCaptionParamsBaseFilter': KalturaCaptionParamsBaseFilter,
            'KalturaCaptionAssetFilter': KalturaCaptionAssetFilter,
            'KalturaCaptionParamsFilter': KalturaCaptionParamsFilter,
        }

    # @return string
    def getName(self):
        return 'caption'

