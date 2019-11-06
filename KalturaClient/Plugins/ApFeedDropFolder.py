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
class KalturaApFeedDropFolder(KalturaFeedDropFolder):
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
            feedItemInfo=NotImplemented,
            apApiKey=NotImplemented):
        KalturaFeedDropFolder.__init__(self,
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
            shouldValidateKS,
            itemHandlingLimit,
            feedItemInfo)

        # @var string
        self.apApiKey = apApiKey


    PROPERTY_LOADERS = {
        'apApiKey': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFeedDropFolder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApFeedDropFolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFeedDropFolder.toParams(self)
        kparams.put("objectType", "KalturaApFeedDropFolder")
        kparams.addStringIfDefined("apApiKey", self.apApiKey)
        return kparams

    def getApApiKey(self):
        return self.apApiKey

    def setApApiKey(self, newApApiKey):
        self.apApiKey = newApApiKey


########## services ##########
########## main ##########
class KalturaApFeedDropFolderClientPlugin(KalturaClientPlugin):
    # KalturaApFeedDropFolderClientPlugin
    instance = None

    # @return KalturaApFeedDropFolderClientPlugin
    @staticmethod
    def get():
        if KalturaApFeedDropFolderClientPlugin.instance == None:
            KalturaApFeedDropFolderClientPlugin.instance = KalturaApFeedDropFolderClientPlugin()
        return KalturaApFeedDropFolderClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaApFeedDropFolder': KalturaApFeedDropFolder,
        }

    # @return string
    def getName(self):
        return 'ApFeedDropFolder'

