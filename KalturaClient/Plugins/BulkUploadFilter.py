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
from .BulkUpload import *
from .BulkUploadXml import *
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
class KalturaBulkServiceFilterDataBase(KalturaBulkServiceData):
    """Represents the Bulk service input for filter bulk upload"""

    def __init__(self,
            filter=NotImplemented):
        KalturaBulkServiceData.__init__(self)

        # Filter for extracting the objects list to upload
        # @var KalturaFilter
        self.filter = filter


    PROPERTY_LOADERS = {
        'filter': (KalturaObjectFactory.create, 'KalturaFilter'), 
    }

    def fromXml(self, node):
        KalturaBulkServiceData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkServiceFilterDataBase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkServiceData.toParams(self)
        kparams.put("objectType", "KalturaBulkServiceFilterDataBase")
        kparams.addObjectIfDefined("filter", self.filter)
        return kparams

    def getFilter(self):
        return self.filter

    def setFilter(self, newFilter):
        self.filter = newFilter


# @package Kaltura
# @subpackage Client
class KalturaBulkUploadResultJob(KalturaBulkUploadResult):
    def __init__(self,
            id=NotImplemented,
            bulkUploadJobId=NotImplemented,
            lineIndex=NotImplemented,
            partnerId=NotImplemented,
            status=NotImplemented,
            action=NotImplemented,
            objectId=NotImplemented,
            objectStatus=NotImplemented,
            bulkUploadResultObjectType=NotImplemented,
            rowData=NotImplemented,
            partnerData=NotImplemented,
            objectErrorDescription=NotImplemented,
            pluginsData=NotImplemented,
            errorDescription=NotImplemented,
            errorCode=NotImplemented,
            errorType=NotImplemented,
            jobObjectId=NotImplemented):
        KalturaBulkUploadResult.__init__(self,
            id,
            bulkUploadJobId,
            lineIndex,
            partnerId,
            status,
            action,
            objectId,
            objectStatus,
            bulkUploadResultObjectType,
            rowData,
            partnerData,
            objectErrorDescription,
            pluginsData,
            errorDescription,
            errorCode,
            errorType)

        # ID of object being processed by the job
        # @var int
        self.jobObjectId = jobObjectId


    PROPERTY_LOADERS = {
        'jobObjectId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBulkUploadResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadResultJob.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadResult.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadResultJob")
        kparams.addIntIfDefined("jobObjectId", self.jobObjectId)
        return kparams

    def getJobObjectId(self):
        return self.jobObjectId

    def setJobObjectId(self, newJobObjectId):
        self.jobObjectId = newJobObjectId


# @package Kaltura
# @subpackage Client
class KalturaBulkServiceFilterData(KalturaBulkServiceFilterDataBase):
    """Represents the Bulk service input for filter bulk upload"""

    def __init__(self,
            filter=NotImplemented,
            templateObject=NotImplemented):
        KalturaBulkServiceFilterDataBase.__init__(self,
            filter)

        # Template object for new object creation
        # @var KalturaObjectBase
        self.templateObject = templateObject


    PROPERTY_LOADERS = {
        'templateObject': (KalturaObjectFactory.create, 'KalturaObjectBase'), 
    }

    def fromXml(self, node):
        KalturaBulkServiceFilterDataBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkServiceFilterData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkServiceFilterDataBase.toParams(self)
        kparams.put("objectType", "KalturaBulkServiceFilterData")
        kparams.addObjectIfDefined("templateObject", self.templateObject)
        return kparams

    def getTemplateObject(self):
        return self.templateObject

    def setTemplateObject(self, newTemplateObject):
        self.templateObject = newTemplateObject


# @package Kaltura
# @subpackage Client
class KalturaBulkUploadFilterJobData(KalturaBulkUploadJobData):
    """Represents the Bulk upload job data for filter bulk upload"""

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
            filter=NotImplemented,
            templateObject=NotImplemented):
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

        # Filter for extracting the objects list to upload
        # @var KalturaFilter
        self.filter = filter

        # Template object for new object creation
        # @var KalturaObjectBase
        self.templateObject = templateObject


    PROPERTY_LOADERS = {
        'filter': (KalturaObjectFactory.create, 'KalturaFilter'), 
        'templateObject': (KalturaObjectFactory.create, 'KalturaObjectBase'), 
    }

    def fromXml(self, node):
        KalturaBulkUploadJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadFilterJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadJobData.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadFilterJobData")
        kparams.addObjectIfDefined("filter", self.filter)
        kparams.addObjectIfDefined("templateObject", self.templateObject)
        return kparams

    def getFilter(self):
        return self.filter

    def setFilter(self, newFilter):
        self.filter = newFilter

    def getTemplateObject(self):
        return self.templateObject

    def setTemplateObject(self, newTemplateObject):
        self.templateObject = newTemplateObject


########## services ##########
########## main ##########
class KalturaBulkUploadFilterClientPlugin(KalturaClientPlugin):
    # KalturaBulkUploadFilterClientPlugin
    instance = None

    # @return KalturaBulkUploadFilterClientPlugin
    @staticmethod
    def get():
        if KalturaBulkUploadFilterClientPlugin.instance == None:
            KalturaBulkUploadFilterClientPlugin.instance = KalturaBulkUploadFilterClientPlugin()
        return KalturaBulkUploadFilterClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaBulkServiceFilterDataBase': KalturaBulkServiceFilterDataBase,
            'KalturaBulkUploadResultJob': KalturaBulkUploadResultJob,
            'KalturaBulkServiceFilterData': KalturaBulkServiceFilterData,
            'KalturaBulkUploadFilterJobData': KalturaBulkUploadFilterJobData,
        }

    # @return string
    def getName(self):
        return 'bulkUploadFilter'

