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
# @package Kaltura
# @subpackage Client
class KalturaWebexAPIGroupParticipationType(object):
    NO_CLASSIFICATION = 0
    OPT_IN = 1
    OPT_OUT = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaWebexAPIUsersMatching(object):
    DO_NOT_MODIFY = 0
    ADD_POSTFIX = 1
    REMOVE_POSTFIX = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaWebexAPIIntegrationSetting(KalturaIntegrationSetting):
    def __init__(self,
            id = NotImplemented,
            status = NotImplemented,
            defaultUserId = NotImplemented,
            accountId = NotImplemented,
            createUserIfNotExist = NotImplemented,
            conversionProfileId = NotImplemented,
            handleParticipantsMode = NotImplemented,
            deletionPolicy = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            partnerId = NotImplemented,
            enableMeetingUpload = NotImplemented,
            enableMeetingChat = NotImplemented,
            webexCategory = NotImplemented,
            enableRecordingUpload = NotImplemented,
            enableTranscription = NotImplemented,
            userMatchingMode = NotImplemented,
            userPostfix = NotImplemented,
            webexAccountDescription = NotImplemented,
            groupParticipationType = NotImplemented,
            optOutGroupNames = NotImplemented,
            optInGroupNames = NotImplemented,
            siteUrl = NotImplemented):
        KalturaIntegrationSetting.__init__(self,
            id,
            status,
            defaultUserId,
            accountId,
            createUserIfNotExist,
            conversionProfileId,
            handleParticipantsMode,
            deletionPolicy,
            createdAt,
            updatedAt,
            partnerId,
            enableMeetingUpload,
            enableMeetingChat)

        # @var str
        self.webexCategory = webexCategory

        # @var KalturaNullableBoolean
        self.enableRecordingUpload = enableRecordingUpload

        # @var KalturaNullableBoolean
        self.enableTranscription = enableTranscription

        # @var KalturaWebexAPIUsersMatching
        self.userMatchingMode = userMatchingMode

        # @var str
        self.userPostfix = userPostfix

        # @var str
        self.webexAccountDescription = webexAccountDescription

        # @var KalturaWebexAPIGroupParticipationType
        self.groupParticipationType = groupParticipationType

        # @var str
        self.optOutGroupNames = optOutGroupNames

        # @var str
        self.optInGroupNames = optInGroupNames

        # @var str
        self.siteUrl = siteUrl


    PROPERTY_LOADERS = {
        'webexCategory': getXmlNodeText, 
        'enableRecordingUpload': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableTranscription': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'userMatchingMode': (KalturaEnumsFactory.createInt, "KalturaWebexAPIUsersMatching"), 
        'userPostfix': getXmlNodeText, 
        'webexAccountDescription': getXmlNodeText, 
        'groupParticipationType': (KalturaEnumsFactory.createInt, "KalturaWebexAPIGroupParticipationType"), 
        'optOutGroupNames': getXmlNodeText, 
        'optInGroupNames': getXmlNodeText, 
        'siteUrl': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaIntegrationSetting.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWebexAPIIntegrationSetting.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaIntegrationSetting.toParams(self)
        kparams.put("objectType", "KalturaWebexAPIIntegrationSetting")
        kparams.addStringIfDefined("webexCategory", self.webexCategory)
        kparams.addIntEnumIfDefined("enableRecordingUpload", self.enableRecordingUpload)
        kparams.addIntEnumIfDefined("enableTranscription", self.enableTranscription)
        kparams.addIntEnumIfDefined("userMatchingMode", self.userMatchingMode)
        kparams.addStringIfDefined("userPostfix", self.userPostfix)
        kparams.addStringIfDefined("webexAccountDescription", self.webexAccountDescription)
        kparams.addIntEnumIfDefined("groupParticipationType", self.groupParticipationType)
        kparams.addStringIfDefined("optOutGroupNames", self.optOutGroupNames)
        kparams.addStringIfDefined("optInGroupNames", self.optInGroupNames)
        kparams.addStringIfDefined("siteUrl", self.siteUrl)
        return kparams

    def getWebexCategory(self):
        return self.webexCategory

    def setWebexCategory(self, newWebexCategory):
        self.webexCategory = newWebexCategory

    def getEnableRecordingUpload(self):
        return self.enableRecordingUpload

    def setEnableRecordingUpload(self, newEnableRecordingUpload):
        self.enableRecordingUpload = newEnableRecordingUpload

    def getEnableTranscription(self):
        return self.enableTranscription

    def setEnableTranscription(self, newEnableTranscription):
        self.enableTranscription = newEnableTranscription

    def getUserMatchingMode(self):
        return self.userMatchingMode

    def setUserMatchingMode(self, newUserMatchingMode):
        self.userMatchingMode = newUserMatchingMode

    def getUserPostfix(self):
        return self.userPostfix

    def setUserPostfix(self, newUserPostfix):
        self.userPostfix = newUserPostfix

    def getWebexAccountDescription(self):
        return self.webexAccountDescription

    def setWebexAccountDescription(self, newWebexAccountDescription):
        self.webexAccountDescription = newWebexAccountDescription

    def getGroupParticipationType(self):
        return self.groupParticipationType

    def setGroupParticipationType(self, newGroupParticipationType):
        self.groupParticipationType = newGroupParticipationType

    def getOptOutGroupNames(self):
        return self.optOutGroupNames

    def setOptOutGroupNames(self, newOptOutGroupNames):
        self.optOutGroupNames = newOptOutGroupNames

    def getOptInGroupNames(self):
        return self.optInGroupNames

    def setOptInGroupNames(self, newOptInGroupNames):
        self.optInGroupNames = newOptInGroupNames

    def getSiteUrl(self):
        return self.siteUrl

    def setSiteUrl(self, newSiteUrl):
        self.siteUrl = newSiteUrl


# @package Kaltura
# @subpackage Client
class KalturaWebexAPIDropFolder(KalturaDropFolder):
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
            webexAPIVendorIntegrationId = NotImplemented,
            webexAPIVendorIntegration = NotImplemented):
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
        self.webexAPIVendorIntegrationId = webexAPIVendorIntegrationId

        # @var KalturaWebexAPIIntegrationSetting
        # @readonly
        self.webexAPIVendorIntegration = webexAPIVendorIntegration


    PROPERTY_LOADERS = {
        'webexAPIVendorIntegrationId': getXmlNodeInt, 
        'webexAPIVendorIntegration': (KalturaObjectFactory.create, 'KalturaWebexAPIIntegrationSetting'), 
    }

    def fromXml(self, node):
        KalturaDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWebexAPIDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolder.toParams(self)
        kparams.put("objectType", "KalturaWebexAPIDropFolder")
        return kparams

    def getWebexAPIVendorIntegrationId(self):
        return self.webexAPIVendorIntegrationId

    def getWebexAPIVendorIntegration(self):
        return self.webexAPIVendorIntegration


# @package Kaltura
# @subpackage Client
class KalturaWebexAPIDropFolderFile(KalturaDropFolderFile):
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
            recordingId = NotImplemented,
            description = NotImplemented,
            contentUrl = NotImplemented,
            urlExpiry = NotImplemented,
            fileExtension = NotImplemented,
            meetingId = NotImplemented,
            recordingStartTime = NotImplemented,
            hostEmail = NotImplemented):
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

        # @var str
        self.recordingId = recordingId

        # @var str
        self.description = description

        # @var str
        self.contentUrl = contentUrl

        # @var int
        self.urlExpiry = urlExpiry

        # @var str
        self.fileExtension = fileExtension

        # @var str
        self.meetingId = meetingId

        # @var int
        self.recordingStartTime = recordingStartTime

        # @var str
        self.hostEmail = hostEmail


    PROPERTY_LOADERS = {
        'recordingId': getXmlNodeText, 
        'description': getXmlNodeText, 
        'contentUrl': getXmlNodeText, 
        'urlExpiry': getXmlNodeInt, 
        'fileExtension': getXmlNodeText, 
        'meetingId': getXmlNodeText, 
        'recordingStartTime': getXmlNodeInt, 
        'hostEmail': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDropFolderFile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWebexAPIDropFolderFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFile.toParams(self)
        kparams.put("objectType", "KalturaWebexAPIDropFolderFile")
        kparams.addStringIfDefined("recordingId", self.recordingId)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("contentUrl", self.contentUrl)
        kparams.addIntIfDefined("urlExpiry", self.urlExpiry)
        kparams.addStringIfDefined("fileExtension", self.fileExtension)
        kparams.addStringIfDefined("meetingId", self.meetingId)
        kparams.addIntIfDefined("recordingStartTime", self.recordingStartTime)
        kparams.addStringIfDefined("hostEmail", self.hostEmail)
        return kparams

    def getRecordingId(self):
        return self.recordingId

    def setRecordingId(self, newRecordingId):
        self.recordingId = newRecordingId

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getContentUrl(self):
        return self.contentUrl

    def setContentUrl(self, newContentUrl):
        self.contentUrl = newContentUrl

    def getUrlExpiry(self):
        return self.urlExpiry

    def setUrlExpiry(self, newUrlExpiry):
        self.urlExpiry = newUrlExpiry

    def getFileExtension(self):
        return self.fileExtension

    def setFileExtension(self, newFileExtension):
        self.fileExtension = newFileExtension

    def getMeetingId(self):
        return self.meetingId

    def setMeetingId(self, newMeetingId):
        self.meetingId = newMeetingId

    def getRecordingStartTime(self):
        return self.recordingStartTime

    def setRecordingStartTime(self, newRecordingStartTime):
        self.recordingStartTime = newRecordingStartTime

    def getHostEmail(self):
        return self.hostEmail

    def setHostEmail(self, newHostEmail):
        self.hostEmail = newHostEmail


# @package Kaltura
# @subpackage Client
class KalturaWebexAPIIntegrationSettingResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaWebexAPIIntegrationSetting]
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaWebexAPIIntegrationSetting'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWebexAPIIntegrationSettingResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaWebexAPIIntegrationSettingResponse")
        return kparams

    def getObjects(self):
        return self.objects


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaWebexVendorService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def fetchRegistrationPage(self, tokensData, iv):
        kparams = KalturaParams()
        kparams.addStringIfDefined("tokensData", tokensData)
        kparams.addStringIfDefined("iv", iv)
        self.client.queueServiceActionCall("webexapidropfolder_webexvendor", "fetchRegistrationPage", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, pager = NotImplemented):
        """List KalturaWebexAPIIntegrationSetting objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("webexapidropfolder_webexvendor", "list", "KalturaWebexAPIIntegrationSettingResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaWebexAPIIntegrationSettingResponse')

    def oauthValidation(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("webexapidropfolder_webexvendor", "oauthValidation", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def preOauthValidation(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("webexapidropfolder_webexvendor", "preOauthValidation", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def submitRegistration(self, accountId, integrationSetting):
        kparams = KalturaParams()
        kparams.addStringIfDefined("accountId", accountId)
        kparams.addObjectIfDefined("integrationSetting", integrationSetting)
        self.client.queueServiceActionCall("webexapidropfolder_webexvendor", "submitRegistration", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaWebexAPIDropFolderClientPlugin(KalturaClientPlugin):
    # KalturaWebexAPIDropFolderClientPlugin
    instance = None

    # @return KalturaWebexAPIDropFolderClientPlugin
    @staticmethod
    def get():
        if KalturaWebexAPIDropFolderClientPlugin.instance == None:
            KalturaWebexAPIDropFolderClientPlugin.instance = KalturaWebexAPIDropFolderClientPlugin()
        return KalturaWebexAPIDropFolderClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'webexVendor': KalturaWebexVendorService,
        }

    def getEnums(self):
        return {
            'KalturaWebexAPIGroupParticipationType': KalturaWebexAPIGroupParticipationType,
            'KalturaWebexAPIUsersMatching': KalturaWebexAPIUsersMatching,
        }

    def getTypes(self):
        return {
            'KalturaWebexAPIIntegrationSetting': KalturaWebexAPIIntegrationSetting,
            'KalturaWebexAPIDropFolder': KalturaWebexAPIDropFolder,
            'KalturaWebexAPIDropFolderFile': KalturaWebexAPIDropFolderFile,
            'KalturaWebexAPIIntegrationSettingResponse': KalturaWebexAPIIntegrationSettingResponse,
        }

    # @return string
    def getName(self):
        return 'WebexAPIDropFolder'

