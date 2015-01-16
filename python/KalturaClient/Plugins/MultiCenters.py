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
# Copyright (C) 2006-2011  Kaltura Inc.
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
from Core import *
from ..Base import *

########## enums ##########
########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaFileSyncImportJobData(KalturaJobData):
    def __init__(self,
            sourceUrl=NotImplemented,
            filesyncId=NotImplemented,
            tmpFilePath=NotImplemented,
            destFilePath=NotImplemented,
            fileSize=NotImplemented):
        KalturaJobData.__init__(self)

        # @var string
        self.sourceUrl = sourceUrl

        # @var string
        self.filesyncId = filesyncId

        # @var string
        self.tmpFilePath = tmpFilePath

        # @var string
        self.destFilePath = destFilePath

        # @var int
        self.fileSize = fileSize


    PROPERTY_LOADERS = {
        'sourceUrl': getXmlNodeText, 
        'filesyncId': getXmlNodeText, 
        'tmpFilePath': getXmlNodeText, 
        'destFilePath': getXmlNodeText, 
        'fileSize': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFileSyncImportJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaJobData.toParams(self)
        kparams.put("objectType", "KalturaFileSyncImportJobData")
        kparams.addStringIfDefined("sourceUrl", self.sourceUrl)
        kparams.addStringIfDefined("filesyncId", self.filesyncId)
        kparams.addStringIfDefined("tmpFilePath", self.tmpFilePath)
        kparams.addStringIfDefined("destFilePath", self.destFilePath)
        kparams.addIntIfDefined("fileSize", self.fileSize)
        return kparams

    def getSourceUrl(self):
        return self.sourceUrl

    def setSourceUrl(self, newSourceUrl):
        self.sourceUrl = newSourceUrl

    def getFilesyncId(self):
        return self.filesyncId

    def setFilesyncId(self, newFilesyncId):
        self.filesyncId = newFilesyncId

    def getTmpFilePath(self):
        return self.tmpFilePath

    def setTmpFilePath(self, newTmpFilePath):
        self.tmpFilePath = newTmpFilePath

    def getDestFilePath(self):
        return self.destFilePath

    def setDestFilePath(self, newDestFilePath):
        self.destFilePath = newDestFilePath

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize


########## services ##########
########## main ##########
class KalturaMultiCentersClientPlugin(KalturaClientPlugin):
    # KalturaMultiCentersClientPlugin
    instance = None

    # @return KalturaMultiCentersClientPlugin
    @staticmethod
    def get():
        if KalturaMultiCentersClientPlugin.instance == None:
            KalturaMultiCentersClientPlugin.instance = KalturaMultiCentersClientPlugin()
        return KalturaMultiCentersClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaFileSyncImportJobData': KalturaFileSyncImportJobData,
        }

    # @return string
    def getName(self):
        return 'multiCenters'

