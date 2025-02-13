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
from .Metadata import *
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
class KalturaMicrosoftTeamsDropFolderFile(KalturaDropFolderFile):
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
            remoteId = NotImplemented,
            ownerId = NotImplemented,
            additionalUserIds = NotImplemented,
            description = NotImplemented,
            targetCategoryIds = NotImplemented,
            name = NotImplemented,
            contentUrl = NotImplemented):
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
        self.remoteId = remoteId

        # @var str
        self.ownerId = ownerId

        # @var str
        self.additionalUserIds = additionalUserIds

        # @var str
        self.description = description

        # @var str
        self.targetCategoryIds = targetCategoryIds

        # @var str
        self.name = name

        # @var str
        self.contentUrl = contentUrl


    PROPERTY_LOADERS = {
        'remoteId': getXmlNodeText, 
        'ownerId': getXmlNodeText, 
        'additionalUserIds': getXmlNodeText, 
        'description': getXmlNodeText, 
        'targetCategoryIds': getXmlNodeText, 
        'name': getXmlNodeText, 
        'contentUrl': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDropFolderFile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMicrosoftTeamsDropFolderFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFile.toParams(self)
        kparams.put("objectType", "KalturaMicrosoftTeamsDropFolderFile")
        kparams.addStringIfDefined("remoteId", self.remoteId)
        kparams.addStringIfDefined("ownerId", self.ownerId)
        kparams.addStringIfDefined("additionalUserIds", self.additionalUserIds)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("targetCategoryIds", self.targetCategoryIds)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("contentUrl", self.contentUrl)
        return kparams

    def getRemoteId(self):
        return self.remoteId

    def setRemoteId(self, newRemoteId):
        self.remoteId = newRemoteId

    def getOwnerId(self):
        return self.ownerId

    def setOwnerId(self, newOwnerId):
        self.ownerId = newOwnerId

    def getAdditionalUserIds(self):
        return self.additionalUserIds

    def setAdditionalUserIds(self, newAdditionalUserIds):
        self.additionalUserIds = newAdditionalUserIds

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTargetCategoryIds(self):
        return self.targetCategoryIds

    def setTargetCategoryIds(self, newTargetCategoryIds):
        self.targetCategoryIds = newTargetCategoryIds

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getContentUrl(self):
        return self.contentUrl

    def setContentUrl(self, newContentUrl):
        self.contentUrl = newContentUrl


# @package Kaltura
# @subpackage Client
class KalturaMicrosoftTeamsIntegrationSetting(KalturaIntegrationSetting):
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
            clientSecret = NotImplemented,
            clientId = NotImplemented,
            userMetadataProfileId = NotImplemented,
            scopes = NotImplemented,
            encryptionKey = NotImplemented):
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
        self.clientSecret = clientSecret

        # @var str
        self.clientId = clientId

        # User-level custom metadata profile ID which will contain encrypted user-level Graph access data.
        # @var int
        self.userMetadataProfileId = userMetadataProfileId

        # MS Graph permission scopes for delegate auth
        # @var str
        self.scopes = scopes

        # Encryption key used for encrypting/decrypting user auth data.
        # @var str
        # @readonly
        self.encryptionKey = encryptionKey


    PROPERTY_LOADERS = {
        'clientSecret': getXmlNodeText, 
        'clientId': getXmlNodeText, 
        'userMetadataProfileId': getXmlNodeInt, 
        'scopes': getXmlNodeText, 
        'encryptionKey': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaIntegrationSetting.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMicrosoftTeamsIntegrationSetting.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaIntegrationSetting.toParams(self)
        kparams.put("objectType", "KalturaMicrosoftTeamsIntegrationSetting")
        kparams.addStringIfDefined("clientSecret", self.clientSecret)
        kparams.addStringIfDefined("clientId", self.clientId)
        kparams.addIntIfDefined("userMetadataProfileId", self.userMetadataProfileId)
        kparams.addStringIfDefined("scopes", self.scopes)
        return kparams

    def getClientSecret(self):
        return self.clientSecret

    def setClientSecret(self, newClientSecret):
        self.clientSecret = newClientSecret

    def getClientId(self):
        return self.clientId

    def setClientId(self, newClientId):
        self.clientId = newClientId

    def getUserMetadataProfileId(self):
        return self.userMetadataProfileId

    def setUserMetadataProfileId(self, newUserMetadataProfileId):
        self.userMetadataProfileId = newUserMetadataProfileId

    def getScopes(self):
        return self.scopes

    def setScopes(self, newScopes):
        self.scopes = newScopes

    def getEncryptionKey(self):
        return self.encryptionKey


# @package Kaltura
# @subpackage Client
class KalturaMicrosoftTeamsDropFolder(KalturaRemoteDropFolder):
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
            integrationId = NotImplemented,
            tenantId = NotImplemented,
            clientSecret = NotImplemented,
            clientId = NotImplemented):
        KalturaRemoteDropFolder.__init__(self,
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

        # ID of the integration being fulfilled by the drop folder
        # @var int
        self.integrationId = integrationId

        # @var str
        # @readonly
        self.tenantId = tenantId

        # @var str
        # @readonly
        self.clientSecret = clientSecret

        # @var str
        # @readonly
        self.clientId = clientId


    PROPERTY_LOADERS = {
        'integrationId': getXmlNodeInt, 
        'tenantId': getXmlNodeText, 
        'clientSecret': getXmlNodeText, 
        'clientId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRemoteDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMicrosoftTeamsDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRemoteDropFolder.toParams(self)
        kparams.put("objectType", "KalturaMicrosoftTeamsDropFolder")
        kparams.addIntIfDefined("integrationId", self.integrationId)
        return kparams

    def getIntegrationId(self):
        return self.integrationId

    def setIntegrationId(self, newIntegrationId):
        self.integrationId = newIntegrationId

    def getTenantId(self):
        return self.tenantId

    def getClientSecret(self):
        return self.clientSecret

    def getClientId(self):
        return self.clientId


########## services ##########
########## main ##########
class KalturaMicrosoftTeamsDropFolderClientPlugin(KalturaClientPlugin):
    # KalturaMicrosoftTeamsDropFolderClientPlugin
    instance = None

    # @return KalturaMicrosoftTeamsDropFolderClientPlugin
    @staticmethod
    def get():
        if KalturaMicrosoftTeamsDropFolderClientPlugin.instance == None:
            KalturaMicrosoftTeamsDropFolderClientPlugin.instance = KalturaMicrosoftTeamsDropFolderClientPlugin()
        return KalturaMicrosoftTeamsDropFolderClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaMicrosoftTeamsDropFolderFile': KalturaMicrosoftTeamsDropFolderFile,
            'KalturaMicrosoftTeamsIntegrationSetting': KalturaMicrosoftTeamsIntegrationSetting,
            'KalturaMicrosoftTeamsDropFolder': KalturaMicrosoftTeamsDropFolder,
        }

    # @return string
    def getName(self):
        return 'MicrosoftTeamsDropFolder'

