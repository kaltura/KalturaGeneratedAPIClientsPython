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
class KalturaS3DropFolder(KalturaDropFolder):
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
            s3Host = NotImplemented,
            s3Region = NotImplemented,
            s3UserId = NotImplemented,
            s3Password = NotImplemented,
            useS3Arn = NotImplemented,
            s3Arn = NotImplemented):
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

        # @var str
        self.s3Host = s3Host

        # @var str
        self.s3Region = s3Region

        # @var str
        self.s3UserId = s3UserId

        # @var str
        self.s3Password = s3Password

        # @var bool
        self.useS3Arn = useS3Arn

        # @var str
        # @readonly
        self.s3Arn = s3Arn


    PROPERTY_LOADERS = {
        's3Host': getXmlNodeText, 
        's3Region': getXmlNodeText, 
        's3UserId': getXmlNodeText, 
        's3Password': getXmlNodeText, 
        'useS3Arn': getXmlNodeBool, 
        's3Arn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaS3DropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolder.toParams(self)
        kparams.put("objectType", "KalturaS3DropFolder")
        kparams.addStringIfDefined("s3Host", self.s3Host)
        kparams.addStringIfDefined("s3Region", self.s3Region)
        kparams.addStringIfDefined("s3UserId", self.s3UserId)
        kparams.addStringIfDefined("s3Password", self.s3Password)
        kparams.addBoolIfDefined("useS3Arn", self.useS3Arn)
        return kparams

    def getS3Host(self):
        return self.s3Host

    def setS3Host(self, newS3Host):
        self.s3Host = newS3Host

    def getS3Region(self):
        return self.s3Region

    def setS3Region(self, newS3Region):
        self.s3Region = newS3Region

    def getS3UserId(self):
        return self.s3UserId

    def setS3UserId(self, newS3UserId):
        self.s3UserId = newS3UserId

    def getS3Password(self):
        return self.s3Password

    def setS3Password(self, newS3Password):
        self.s3Password = newS3Password

    def getUseS3Arn(self):
        return self.useS3Arn

    def setUseS3Arn(self, newUseS3Arn):
        self.useS3Arn = newUseS3Arn

    def getS3Arn(self):
        return self.s3Arn


# @package Kaltura
# @subpackage Client
class KalturaS3DropFolderFile(KalturaDropFolderFile):
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
            batchJobId = NotImplemented):
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


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDropFolderFile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaS3DropFolderFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFile.toParams(self)
        kparams.put("objectType", "KalturaS3DropFolderFile")
        return kparams


########## services ##########
########## main ##########
class KalturaS3DropFolderClientPlugin(KalturaClientPlugin):
    # KalturaS3DropFolderClientPlugin
    instance = None

    # @return KalturaS3DropFolderClientPlugin
    @staticmethod
    def get():
        if KalturaS3DropFolderClientPlugin.instance == None:
            KalturaS3DropFolderClientPlugin.instance = KalturaS3DropFolderClientPlugin()
        return KalturaS3DropFolderClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaS3DropFolder': KalturaS3DropFolder,
            'KalturaS3DropFolderFile': KalturaS3DropFolderFile,
        }

    # @return string
    def getName(self):
        return 'S3DropFolder'

