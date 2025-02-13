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
from .DropFolder import *
from .Vendor import *
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
########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaZoomMeetingMetadata(KalturaObjectBase):
    def __init__(self,
            uuid = NotImplemented,
            meetingId = NotImplemented,
            accountId = NotImplemented,
            hostId = NotImplemented,
            topic = NotImplemented,
            meetingStartTime = NotImplemented,
            type = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var str
        self.uuid = uuid

        # @var str
        self.meetingId = meetingId

        # @var str
        self.accountId = accountId

        # @var str
        self.hostId = hostId

        # @var str
        self.topic = topic

        # @var str
        self.meetingStartTime = meetingStartTime

        # @var KalturaRecordingType
        self.type = type


    PROPERTY_LOADERS = {
        'uuid': getXmlNodeText, 
        'meetingId': getXmlNodeText, 
        'accountId': getXmlNodeText, 
        'hostId': getXmlNodeText, 
        'topic': getXmlNodeText, 
        'meetingStartTime': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createInt, "KalturaRecordingType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomMeetingMetadata.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaZoomMeetingMetadata")
        kparams.addStringIfDefined("uuid", self.uuid)
        kparams.addStringIfDefined("meetingId", self.meetingId)
        kparams.addStringIfDefined("accountId", self.accountId)
        kparams.addStringIfDefined("hostId", self.hostId)
        kparams.addStringIfDefined("topic", self.topic)
        kparams.addStringIfDefined("meetingStartTime", self.meetingStartTime)
        kparams.addIntEnumIfDefined("type", self.type)
        return kparams

    def getUuid(self):
        return self.uuid

    def setUuid(self, newUuid):
        self.uuid = newUuid

    def getMeetingId(self):
        return self.meetingId

    def setMeetingId(self, newMeetingId):
        self.meetingId = newMeetingId

    def getAccountId(self):
        return self.accountId

    def setAccountId(self, newAccountId):
        self.accountId = newAccountId

    def getHostId(self):
        return self.hostId

    def setHostId(self, newHostId):
        self.hostId = newHostId

    def getTopic(self):
        return self.topic

    def setTopic(self, newTopic):
        self.topic = newTopic

    def getMeetingStartTime(self):
        return self.meetingStartTime

    def setMeetingStartTime(self, newMeetingStartTime):
        self.meetingStartTime = newMeetingStartTime

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaZoomRecordingFile(KalturaObjectBase):
    def __init__(self,
            id = NotImplemented,
            recordingStart = NotImplemented,
            fileType = NotImplemented,
            downloadUrl = NotImplemented,
            fileExtension = NotImplemented,
            downloadToken = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var str
        self.id = id

        # @var str
        self.recordingStart = recordingStart

        # @var KalturaRecordingFileType
        self.fileType = fileType

        # @var str
        self.downloadUrl = downloadUrl

        # @var str
        self.fileExtension = fileExtension

        # @var str
        self.downloadToken = downloadToken


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'recordingStart': getXmlNodeText, 
        'fileType': (KalturaEnumsFactory.createInt, "KalturaRecordingFileType"), 
        'downloadUrl': getXmlNodeText, 
        'fileExtension': getXmlNodeText, 
        'downloadToken': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomRecordingFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaZoomRecordingFile")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("recordingStart", self.recordingStart)
        kparams.addIntEnumIfDefined("fileType", self.fileType)
        kparams.addStringIfDefined("downloadUrl", self.downloadUrl)
        kparams.addStringIfDefined("fileExtension", self.fileExtension)
        kparams.addStringIfDefined("downloadToken", self.downloadToken)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getRecordingStart(self):
        return self.recordingStart

    def setRecordingStart(self, newRecordingStart):
        self.recordingStart = newRecordingStart

    def getFileType(self):
        return self.fileType

    def setFileType(self, newFileType):
        self.fileType = newFileType

    def getDownloadUrl(self):
        return self.downloadUrl

    def setDownloadUrl(self, newDownloadUrl):
        self.downloadUrl = newDownloadUrl

    def getFileExtension(self):
        return self.fileExtension

    def setFileExtension(self, newFileExtension):
        self.fileExtension = newFileExtension

    def getDownloadToken(self):
        return self.downloadToken

    def setDownloadToken(self, newDownloadToken):
        self.downloadToken = newDownloadToken


# @package Kaltura
# @subpackage Client
class KalturaZoomDropFolder(KalturaDropFolder):
    def __init__(self,
            id = NotImplemented,
            partnerId = NotImplemented,
            name = NotImplemented,
            description = NotImplemented,
            type = NotImplemented,
            status = NotImplemented,
            conversionProfileId = NotImplemented,
            dc = NotImplemented,
            path = NotImplemented,
            fileSizeCheckInterval = NotImplemented,
            fileDeletePolicy = NotImplemented,
            fileDeleteRegex = NotImplemented,
            autoFileDeleteDays = NotImplemented,
            fileHandlerType = NotImplemented,
            fileNamePatterns = NotImplemented,
            fileHandlerConfig = NotImplemented,
            tags = NotImplemented,
            errorCode = NotImplemented,
            errorDescription = NotImplemented,
            ignoreFileNamePatterns = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            lastAccessedAt = NotImplemented,
            incremental = NotImplemented,
            lastFileTimestamp = NotImplemented,
            metadataProfileId = NotImplemented,
            categoriesMetadataFieldName = NotImplemented,
            enforceEntitlement = NotImplemented,
            shouldValidateKS = NotImplemented,
            zoomVendorIntegrationId = NotImplemented,
            zoomVendorIntegration = NotImplemented,
            lastHandledMeetingTime = NotImplemented):
        KalturaDropFolder.__init__(self,
            id,
            partnerId,
            name,
            description,
            type,
            status,
            conversionProfileId,
            dc,
            path,
            fileSizeCheckInterval,
            fileDeletePolicy,
            fileDeleteRegex,
            autoFileDeleteDays,
            fileHandlerType,
            fileNamePatterns,
            fileHandlerConfig,
            tags,
            errorCode,
            errorDescription,
            ignoreFileNamePatterns,
            createdAt,
            updatedAt,
            lastAccessedAt,
            incremental,
            lastFileTimestamp,
            metadataProfileId,
            categoriesMetadataFieldName,
            enforceEntitlement,
            shouldValidateKS)

        # @var int
        # @readonly
        self.zoomVendorIntegrationId = zoomVendorIntegrationId

        # @var KalturaZoomIntegrationSetting
        # @readonly
        self.zoomVendorIntegration = zoomVendorIntegration

        # @var int
        self.lastHandledMeetingTime = lastHandledMeetingTime


    PROPERTY_LOADERS = {
        'zoomVendorIntegrationId': getXmlNodeInt, 
        'zoomVendorIntegration': (KalturaObjectFactory.create, 'KalturaZoomIntegrationSetting'), 
        'lastHandledMeetingTime': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolder.toParams(self)
        kparams.put("objectType", "KalturaZoomDropFolder")
        kparams.addIntIfDefined("lastHandledMeetingTime", self.lastHandledMeetingTime)
        return kparams

    def getZoomVendorIntegrationId(self):
        return self.zoomVendorIntegrationId

    def getZoomVendorIntegration(self):
        return self.zoomVendorIntegration

    def getLastHandledMeetingTime(self):
        return self.lastHandledMeetingTime

    def setLastHandledMeetingTime(self, newLastHandledMeetingTime):
        self.lastHandledMeetingTime = newLastHandledMeetingTime


# @package Kaltura
# @subpackage Client
class KalturaZoomDropFolderFile(KalturaDropFolderFile):
    def __init__(self,
            id = NotImplemented,
            partnerId = NotImplemented,
            dropFolderId = NotImplemented,
            fileName = NotImplemented,
            fileSize = NotImplemented,
            fileSizeLastSetAt = NotImplemented,
            status = NotImplemented,
            type = NotImplemented,
            parsedSlug = NotImplemented,
            parsedFlavor = NotImplemented,
            parsedUserId = NotImplemented,
            leadDropFolderFileId = NotImplemented,
            deletedDropFolderFileId = NotImplemented,
            entryId = NotImplemented,
            errorCode = NotImplemented,
            errorDescription = NotImplemented,
            lastModificationTime = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            uploadStartDetectedAt = NotImplemented,
            uploadEndDetectedAt = NotImplemented,
            importStartedAt = NotImplemented,
            importEndedAt = NotImplemented,
            batchJobId = NotImplemented,
            meetingMetadata = NotImplemented,
            recordingFile = NotImplemented,
            parentEntryId = NotImplemented,
            isParentEntry = NotImplemented):
        KalturaDropFolderFile.__init__(self,
            id,
            partnerId,
            dropFolderId,
            fileName,
            fileSize,
            fileSizeLastSetAt,
            status,
            type,
            parsedSlug,
            parsedFlavor,
            parsedUserId,
            leadDropFolderFileId,
            deletedDropFolderFileId,
            entryId,
            errorCode,
            errorDescription,
            lastModificationTime,
            createdAt,
            updatedAt,
            uploadStartDetectedAt,
            uploadEndDetectedAt,
            importStartedAt,
            importEndedAt,
            batchJobId)

        # @var KalturaZoomMeetingMetadata
        self.meetingMetadata = meetingMetadata

        # @var KalturaZoomRecordingFile
        self.recordingFile = recordingFile

        # @var str
        self.parentEntryId = parentEntryId

        # @var bool
        self.isParentEntry = isParentEntry


    PROPERTY_LOADERS = {
        'meetingMetadata': (KalturaObjectFactory.create, 'KalturaZoomMeetingMetadata'), 
        'recordingFile': (KalturaObjectFactory.create, 'KalturaZoomRecordingFile'), 
        'parentEntryId': getXmlNodeText, 
        'isParentEntry': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaDropFolderFile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomDropFolderFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFile.toParams(self)
        kparams.put("objectType", "KalturaZoomDropFolderFile")
        kparams.addObjectIfDefined("meetingMetadata", self.meetingMetadata)
        kparams.addObjectIfDefined("recordingFile", self.recordingFile)
        kparams.addStringIfDefined("parentEntryId", self.parentEntryId)
        kparams.addBoolIfDefined("isParentEntry", self.isParentEntry)
        return kparams

    def getMeetingMetadata(self):
        return self.meetingMetadata

    def setMeetingMetadata(self, newMeetingMetadata):
        self.meetingMetadata = newMeetingMetadata

    def getRecordingFile(self):
        return self.recordingFile

    def setRecordingFile(self, newRecordingFile):
        self.recordingFile = newRecordingFile

    def getParentEntryId(self):
        return self.parentEntryId

    def setParentEntryId(self, newParentEntryId):
        self.parentEntryId = newParentEntryId

    def getIsParentEntry(self):
        return self.isParentEntry

    def setIsParentEntry(self, newIsParentEntry):
        self.isParentEntry = newIsParentEntry


# @package Kaltura
# @subpackage Client
class KalturaZoomDropFolderBaseFilter(KalturaDropFolderFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            nameLike = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            conversionProfileIdEqual = NotImplemented,
            conversionProfileIdIn = NotImplemented,
            dcEqual = NotImplemented,
            dcIn = NotImplemented,
            pathEqual = NotImplemented,
            pathLike = NotImplemented,
            fileHandlerTypeEqual = NotImplemented,
            fileHandlerTypeIn = NotImplemented,
            fileNamePatternsLike = NotImplemented,
            fileNamePatternsMultiLikeOr = NotImplemented,
            fileNamePatternsMultiLikeAnd = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            errorCodeEqual = NotImplemented,
            errorCodeIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            currentDc = NotImplemented):
        KalturaDropFolderFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathEqual,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            errorCodeEqual,
            errorCodeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            currentDc)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDropFolderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomDropFolderBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFilter.toParams(self)
        kparams.put("objectType", "KalturaZoomDropFolderBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaZoomDropFolderFilter(KalturaZoomDropFolderBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            nameLike = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            conversionProfileIdEqual = NotImplemented,
            conversionProfileIdIn = NotImplemented,
            dcEqual = NotImplemented,
            dcIn = NotImplemented,
            pathEqual = NotImplemented,
            pathLike = NotImplemented,
            fileHandlerTypeEqual = NotImplemented,
            fileHandlerTypeIn = NotImplemented,
            fileNamePatternsLike = NotImplemented,
            fileNamePatternsMultiLikeOr = NotImplemented,
            fileNamePatternsMultiLikeAnd = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            errorCodeEqual = NotImplemented,
            errorCodeIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            currentDc = NotImplemented):
        KalturaZoomDropFolderBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            nameLike,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            conversionProfileIdEqual,
            conversionProfileIdIn,
            dcEqual,
            dcIn,
            pathEqual,
            pathLike,
            fileHandlerTypeEqual,
            fileHandlerTypeIn,
            fileNamePatternsLike,
            fileNamePatternsMultiLikeOr,
            fileNamePatternsMultiLikeAnd,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            errorCodeEqual,
            errorCodeIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            currentDc)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaZoomDropFolderBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomDropFolderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaZoomDropFolderBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaZoomDropFolderFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaZoomDropFolderClientPlugin(KalturaClientPlugin):
    # KalturaZoomDropFolderClientPlugin
    instance = None

    # @return KalturaZoomDropFolderClientPlugin
    @staticmethod
    def get():
        if KalturaZoomDropFolderClientPlugin.instance == None:
            KalturaZoomDropFolderClientPlugin.instance = KalturaZoomDropFolderClientPlugin()
        return KalturaZoomDropFolderClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaZoomMeetingMetadata': KalturaZoomMeetingMetadata,
            'KalturaZoomRecordingFile': KalturaZoomRecordingFile,
            'KalturaZoomDropFolder': KalturaZoomDropFolder,
            'KalturaZoomDropFolderFile': KalturaZoomDropFolderFile,
            'KalturaZoomDropFolderBaseFilter': KalturaZoomDropFolderBaseFilter,
            'KalturaZoomDropFolderFilter': KalturaZoomDropFolderFilter,
        }

    # @return string
    def getName(self):
        return 'ZoomDropFolder'

