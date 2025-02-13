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
class KalturaDropFolderTrRdsFileHandlerConfig(KalturaDropFolderFileHandlerConfig):
    def __init__(self,
            handlerType = NotImplemented,
            leadPattern = NotImplemented,
            additionalPatterns = NotImplemented):
        KalturaDropFolderFileHandlerConfig.__init__(self,
            handlerType)

        # @var str
        self.leadPattern = leadPattern

        # @var str
        self.additionalPatterns = additionalPatterns


    PROPERTY_LOADERS = {
        'leadPattern': getXmlNodeText, 
        'additionalPatterns': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDropFolderFileHandlerConfig.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderTrRdsFileHandlerConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFileHandlerConfig.toParams(self)
        kparams.put("objectType", "KalturaDropFolderTrRdsFileHandlerConfig")
        kparams.addStringIfDefined("leadPattern", self.leadPattern)
        kparams.addStringIfDefined("additionalPatterns", self.additionalPatterns)
        return kparams

    def getLeadPattern(self):
        return self.leadPattern

    def setLeadPattern(self, newLeadPattern):
        self.leadPattern = newLeadPattern

    def getAdditionalPatterns(self):
        return self.additionalPatterns

    def setAdditionalPatterns(self, newAdditionalPatterns):
        self.additionalPatterns = newAdditionalPatterns


# @package Kaltura
# @subpackage Client
class KalturaTrRdsDropFolder(KalturaSftpDropFolder):
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
            host = NotImplemented,
            port = NotImplemented,
            username = NotImplemented,
            password = NotImplemented,
            privateKey = NotImplemented,
            publicKey = NotImplemented,
            passPhrase = NotImplemented,
            syncMetadataProfile = NotImplemented,
            targetMetadataProfile = NotImplemented):
        KalturaSftpDropFolder.__init__(self,
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
            shouldValidateKS,
            host,
            port,
            username,
            password,
            privateKey,
            publicKey,
            passPhrase)

        # @var int
        self.syncMetadataProfile = syncMetadataProfile

        # @var int
        self.targetMetadataProfile = targetMetadataProfile


    PROPERTY_LOADERS = {
        'syncMetadataProfile': getXmlNodeInt, 
        'targetMetadataProfile': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaSftpDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTrRdsDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSftpDropFolder.toParams(self)
        kparams.put("objectType", "KalturaTrRdsDropFolder")
        kparams.addIntIfDefined("syncMetadataProfile", self.syncMetadataProfile)
        kparams.addIntIfDefined("targetMetadataProfile", self.targetMetadataProfile)
        return kparams

    def getSyncMetadataProfile(self):
        return self.syncMetadataProfile

    def setSyncMetadataProfile(self, newSyncMetadataProfile):
        self.syncMetadataProfile = newSyncMetadataProfile

    def getTargetMetadataProfile(self):
        return self.targetMetadataProfile

    def setTargetMetadataProfile(self, newTargetMetadataProfile):
        self.targetMetadataProfile = newTargetMetadataProfile


########## services ##########
########## main ##########
class KalturaTrRdsSyncDropFolderClientPlugin(KalturaClientPlugin):
    # KalturaTrRdsSyncDropFolderClientPlugin
    instance = None

    # @return KalturaTrRdsSyncDropFolderClientPlugin
    @staticmethod
    def get():
        if KalturaTrRdsSyncDropFolderClientPlugin.instance == None:
            KalturaTrRdsSyncDropFolderClientPlugin.instance = KalturaTrRdsSyncDropFolderClientPlugin()
        return KalturaTrRdsSyncDropFolderClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaDropFolderTrRdsFileHandlerConfig': KalturaDropFolderTrRdsFileHandlerConfig,
            'KalturaTrRdsDropFolder': KalturaTrRdsDropFolder,
        }

    # @return string
    def getName(self):
        return 'TrRdsSyncDropFolder'

