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
class KalturaFeedItemInfo(KalturaObjectBase):
    def __init__(self,
            itemXPath=NotImplemented,
            itemPublishDateXPath=NotImplemented,
            itemUniqueIdentifierXPath=NotImplemented,
            itemContentFileSizeXPath=NotImplemented,
            itemContentUrlXPath=NotImplemented,
            itemContentBitrateXPath=NotImplemented,
            itemHashXPath=NotImplemented,
            itemContentXpath=NotImplemented,
            contentBitrateAttributeName=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.itemXPath = itemXPath

        # @var string
        self.itemPublishDateXPath = itemPublishDateXPath

        # @var string
        self.itemUniqueIdentifierXPath = itemUniqueIdentifierXPath

        # @var string
        self.itemContentFileSizeXPath = itemContentFileSizeXPath

        # @var string
        self.itemContentUrlXPath = itemContentUrlXPath

        # @var string
        self.itemContentBitrateXPath = itemContentBitrateXPath

        # @var string
        self.itemHashXPath = itemHashXPath

        # @var string
        self.itemContentXpath = itemContentXpath

        # @var string
        self.contentBitrateAttributeName = contentBitrateAttributeName


    PROPERTY_LOADERS = {
        'itemXPath': getXmlNodeText, 
        'itemPublishDateXPath': getXmlNodeText, 
        'itemUniqueIdentifierXPath': getXmlNodeText, 
        'itemContentFileSizeXPath': getXmlNodeText, 
        'itemContentUrlXPath': getXmlNodeText, 
        'itemContentBitrateXPath': getXmlNodeText, 
        'itemHashXPath': getXmlNodeText, 
        'itemContentXpath': getXmlNodeText, 
        'contentBitrateAttributeName': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFeedItemInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFeedItemInfo")
        kparams.addStringIfDefined("itemXPath", self.itemXPath)
        kparams.addStringIfDefined("itemPublishDateXPath", self.itemPublishDateXPath)
        kparams.addStringIfDefined("itemUniqueIdentifierXPath", self.itemUniqueIdentifierXPath)
        kparams.addStringIfDefined("itemContentFileSizeXPath", self.itemContentFileSizeXPath)
        kparams.addStringIfDefined("itemContentUrlXPath", self.itemContentUrlXPath)
        kparams.addStringIfDefined("itemContentBitrateXPath", self.itemContentBitrateXPath)
        kparams.addStringIfDefined("itemHashXPath", self.itemHashXPath)
        kparams.addStringIfDefined("itemContentXpath", self.itemContentXpath)
        kparams.addStringIfDefined("contentBitrateAttributeName", self.contentBitrateAttributeName)
        return kparams

    def getItemXPath(self):
        return self.itemXPath

    def setItemXPath(self, newItemXPath):
        self.itemXPath = newItemXPath

    def getItemPublishDateXPath(self):
        return self.itemPublishDateXPath

    def setItemPublishDateXPath(self, newItemPublishDateXPath):
        self.itemPublishDateXPath = newItemPublishDateXPath

    def getItemUniqueIdentifierXPath(self):
        return self.itemUniqueIdentifierXPath

    def setItemUniqueIdentifierXPath(self, newItemUniqueIdentifierXPath):
        self.itemUniqueIdentifierXPath = newItemUniqueIdentifierXPath

    def getItemContentFileSizeXPath(self):
        return self.itemContentFileSizeXPath

    def setItemContentFileSizeXPath(self, newItemContentFileSizeXPath):
        self.itemContentFileSizeXPath = newItemContentFileSizeXPath

    def getItemContentUrlXPath(self):
        return self.itemContentUrlXPath

    def setItemContentUrlXPath(self, newItemContentUrlXPath):
        self.itemContentUrlXPath = newItemContentUrlXPath

    def getItemContentBitrateXPath(self):
        return self.itemContentBitrateXPath

    def setItemContentBitrateXPath(self, newItemContentBitrateXPath):
        self.itemContentBitrateXPath = newItemContentBitrateXPath

    def getItemHashXPath(self):
        return self.itemHashXPath

    def setItemHashXPath(self, newItemHashXPath):
        self.itemHashXPath = newItemHashXPath

    def getItemContentXpath(self):
        return self.itemContentXpath

    def setItemContentXpath(self, newItemContentXpath):
        self.itemContentXpath = newItemContentXpath

    def getContentBitrateAttributeName(self):
        return self.contentBitrateAttributeName

    def setContentBitrateAttributeName(self, newContentBitrateAttributeName):
        self.contentBitrateAttributeName = newContentBitrateAttributeName


# @package Kaltura
# @subpackage Client
class KalturaFeedDropFolder(KalturaDropFolder):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            type=NotImplemented,
            status=NotImplemented,
            conversionProfileId=NotImplemented,
            dc=NotImplemented,
            path=NotImplemented,
            fileSizeCheckInterval=NotImplemented,
            fileDeletePolicy=NotImplemented,
            autoFileDeleteDays=NotImplemented,
            fileHandlerType=NotImplemented,
            fileNamePatterns=NotImplemented,
            fileHandlerConfig=NotImplemented,
            tags=NotImplemented,
            errorCode=NotImplemented,
            errorDescription=NotImplemented,
            ignoreFileNamePatterns=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            lastAccessedAt=NotImplemented,
            incremental=NotImplemented,
            lastFileTimestamp=NotImplemented,
            metadataProfileId=NotImplemented,
            categoriesMetadataFieldName=NotImplemented,
            enforceEntitlement=NotImplemented,
            shouldValidateKS=NotImplemented,
            itemHandlingLimit=NotImplemented,
            feedItemInfo=NotImplemented):
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
        self.itemHandlingLimit = itemHandlingLimit

        # @var KalturaFeedItemInfo
        self.feedItemInfo = feedItemInfo


    PROPERTY_LOADERS = {
        'itemHandlingLimit': getXmlNodeInt, 
        'feedItemInfo': (KalturaObjectFactory.create, 'KalturaFeedItemInfo'), 
    }

    def fromXml(self, node):
        KalturaDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFeedDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolder.toParams(self)
        kparams.put("objectType", "KalturaFeedDropFolder")
        kparams.addIntIfDefined("itemHandlingLimit", self.itemHandlingLimit)
        kparams.addObjectIfDefined("feedItemInfo", self.feedItemInfo)
        return kparams

    def getItemHandlingLimit(self):
        return self.itemHandlingLimit

    def setItemHandlingLimit(self, newItemHandlingLimit):
        self.itemHandlingLimit = newItemHandlingLimit

    def getFeedItemInfo(self):
        return self.feedItemInfo

    def setFeedItemInfo(self, newFeedItemInfo):
        self.feedItemInfo = newFeedItemInfo


# @package Kaltura
# @subpackage Client
class KalturaFeedDropFolderFile(KalturaDropFolderFile):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            dropFolderId=NotImplemented,
            fileName=NotImplemented,
            fileSize=NotImplemented,
            fileSizeLastSetAt=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            parsedSlug=NotImplemented,
            parsedFlavor=NotImplemented,
            parsedUserId=NotImplemented,
            leadDropFolderFileId=NotImplemented,
            deletedDropFolderFileId=NotImplemented,
            entryId=NotImplemented,
            errorCode=NotImplemented,
            errorDescription=NotImplemented,
            lastModificationTime=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            uploadStartDetectedAt=NotImplemented,
            uploadEndDetectedAt=NotImplemented,
            importStartedAt=NotImplemented,
            importEndedAt=NotImplemented,
            batchJobId=NotImplemented,
            hash=NotImplemented,
            feedXmlPath=NotImplemented):
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

        # MD5 or Sha1 encrypted string
        # @var string
        self.hash = hash

        # Path of the original Feed content XML
        # @var string
        self.feedXmlPath = feedXmlPath


    PROPERTY_LOADERS = {
        'hash': getXmlNodeText, 
        'feedXmlPath': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDropFolderFile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFeedDropFolderFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFile.toParams(self)
        kparams.put("objectType", "KalturaFeedDropFolderFile")
        kparams.addStringIfDefined("hash", self.hash)
        kparams.addStringIfDefined("feedXmlPath", self.feedXmlPath)
        return kparams

    def getHash(self):
        return self.hash

    def setHash(self, newHash):
        self.hash = newHash

    def getFeedXmlPath(self):
        return self.feedXmlPath

    def setFeedXmlPath(self, newFeedXmlPath):
        self.feedXmlPath = newFeedXmlPath


########## services ##########
########## main ##########
class KalturaFeedDropFolderClientPlugin(KalturaClientPlugin):
    # KalturaFeedDropFolderClientPlugin
    instance = None

    # @return KalturaFeedDropFolderClientPlugin
    @staticmethod
    def get():
        if KalturaFeedDropFolderClientPlugin.instance == None:
            KalturaFeedDropFolderClientPlugin.instance = KalturaFeedDropFolderClientPlugin()
        return KalturaFeedDropFolderClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaFeedItemInfo': KalturaFeedItemInfo,
            'KalturaFeedDropFolder': KalturaFeedDropFolder,
            'KalturaFeedDropFolderFile': KalturaFeedDropFolderFile,
        }

    # @return string
    def getName(self):
        return 'FeedDropFolder'

