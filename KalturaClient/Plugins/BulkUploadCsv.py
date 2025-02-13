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
from .BulkUpload import *
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
class KalturaBulkUploadCsvVersion(object):
    V1 = 1
    V2 = 2
    V3 = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaBulkUploadCsvJobData(KalturaBulkUploadJobData):
    """Represents the Bulk upload job data for xml bulk upload"""

    def __init__(self,
            userId = NotImplemented,
            uploadedBy = NotImplemented,
            conversionProfileId = NotImplemented,
            resultsFileLocalPath = NotImplemented,
            resultsFileUrl = NotImplemented,
            numOfEntries = NotImplemented,
            numOfObjects = NotImplemented,
            filePath = NotImplemented,
            bulkUploadObjectType = NotImplemented,
            fileName = NotImplemented,
            objectData = NotImplemented,
            type = NotImplemented,
            emailRecipients = NotImplemented,
            numOfErrorObjects = NotImplemented,
            privileges = NotImplemented,
            csvVersion = NotImplemented,
            columns = NotImplemented,
            processObjectId = NotImplemented,
            processObjectType = NotImplemented):
        KalturaBulkUploadJobData.__init__(self,
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

        # The version of the csv file
        # @var KalturaBulkUploadCsvVersion
        # @readonly
        self.csvVersion = csvVersion

        # Array containing CSV headers
        # @var List[KalturaString]
        self.columns = columns

        # The object in process
        # @var str
        self.processObjectId = processObjectId

        # The type of the object in process
        # @var str
        self.processObjectType = processObjectType


    PROPERTY_LOADERS = {
        'csvVersion': (KalturaEnumsFactory.createInt, "KalturaBulkUploadCsvVersion"), 
        'columns': (KalturaObjectFactory.createArray, 'KalturaString'), 
        'processObjectId': getXmlNodeText, 
        'processObjectType': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBulkUploadJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadCsvJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadJobData.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadCsvJobData")
        kparams.addArrayIfDefined("columns", self.columns)
        kparams.addStringIfDefined("processObjectId", self.processObjectId)
        kparams.addStringIfDefined("processObjectType", self.processObjectType)
        return kparams

    def getCsvVersion(self):
        return self.csvVersion

    def getColumns(self):
        return self.columns

    def setColumns(self, newColumns):
        self.columns = newColumns

    def getProcessObjectId(self):
        return self.processObjectId

    def setProcessObjectId(self, newProcessObjectId):
        self.processObjectId = newProcessObjectId

    def getProcessObjectType(self):
        return self.processObjectType

    def setProcessObjectType(self, newProcessObjectType):
        self.processObjectType = newProcessObjectType


########## services ##########
########## main ##########
class KalturaBulkUploadCsvClientPlugin(KalturaClientPlugin):
    # KalturaBulkUploadCsvClientPlugin
    instance = None

    # @return KalturaBulkUploadCsvClientPlugin
    @staticmethod
    def get():
        if KalturaBulkUploadCsvClientPlugin.instance == None:
            KalturaBulkUploadCsvClientPlugin.instance = KalturaBulkUploadCsvClientPlugin()
        return KalturaBulkUploadCsvClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaBulkUploadCsvVersion': KalturaBulkUploadCsvVersion,
        }

    def getTypes(self):
        return {
            'KalturaBulkUploadCsvJobData': KalturaBulkUploadCsvJobData,
        }

    # @return string
    def getName(self):
        return 'bulkUploadCsv'

