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
from .BulkUploadXml import *
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
class KalturaDropFolderXmlBulkUploadFileHandlerConfig(KalturaDropFolderFileHandlerConfig):
    def __init__(self,
            handlerType=NotImplemented):
        KalturaDropFolderFileHandlerConfig.__init__(self,
            handlerType)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDropFolderFileHandlerConfig.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderXmlBulkUploadFileHandlerConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDropFolderFileHandlerConfig.toParams(self)
        kparams.put("objectType", "KalturaDropFolderXmlBulkUploadFileHandlerConfig")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaDropFolderXmlBulkUploadJobData(KalturaBulkUploadXmlJobData):
    """Represents the Bulk upload job data for drop folder xml bulk upload"""

    def __init__(self,
            userId=NotImplemented,
            uploadedBy=NotImplemented,
            conversionProfileId=NotImplemented,
            resultsFileLocalPath=NotImplemented,
            resultsFileUrl=NotImplemented,
            numOfEntries=NotImplemented,
            numOfObjects=NotImplemented,
            filePath=NotImplemented,
            bulkUploadObjectType=NotImplemented,
            fileName=NotImplemented,
            objectData=NotImplemented,
            type=NotImplemented,
            emailRecipients=NotImplemented,
            numOfErrorObjects=NotImplemented,
            privileges=NotImplemented,
            dropFolderId=NotImplemented):
        KalturaBulkUploadXmlJobData.__init__(self,
            userId,
            uploadedBy,
            conversionProfileId,
            resultsFileLocalPath,
            resultsFileUrl,
            numOfEntries,
            numOfObjects,
            filePath,
            bulkUploadObjectType,
            fileName,
            objectData,
            type,
            emailRecipients,
            numOfErrorObjects,
            privileges)

        # the job drop folder id
        # @var int
        self.dropFolderId = dropFolderId


    PROPERTY_LOADERS = {
        'dropFolderId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBulkUploadXmlJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDropFolderXmlBulkUploadJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadXmlJobData.toParams(self)
        kparams.put("objectType", "KalturaDropFolderXmlBulkUploadJobData")
        kparams.addIntIfDefined("dropFolderId", self.dropFolderId)
        return kparams

    def getDropFolderId(self):
        return self.dropFolderId

    def setDropFolderId(self, newDropFolderId):
        self.dropFolderId = newDropFolderId


########## services ##########
########## main ##########
class KalturaDropFolderXmlBulkUploadClientPlugin(KalturaClientPlugin):
    # KalturaDropFolderXmlBulkUploadClientPlugin
    instance = None

    # @return KalturaDropFolderXmlBulkUploadClientPlugin
    @staticmethod
    def get():
        if KalturaDropFolderXmlBulkUploadClientPlugin.instance == None:
            KalturaDropFolderXmlBulkUploadClientPlugin.instance = KalturaDropFolderXmlBulkUploadClientPlugin()
        return KalturaDropFolderXmlBulkUploadClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaDropFolderXmlBulkUploadFileHandlerConfig': KalturaDropFolderXmlBulkUploadFileHandlerConfig,
            'KalturaDropFolderXmlBulkUploadJobData': KalturaDropFolderXmlBulkUploadJobData,
        }

    # @return string
    def getName(self):
        return 'dropFolderXmlBulkUpload'

