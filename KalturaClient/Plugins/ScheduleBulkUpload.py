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
# Copyright (C) 2006-2021  Kaltura Inc.
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
from .BulkUploadCsv import *
from .Schedule import *
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
class KalturaBulkUploadResultScheduleEvent(KalturaBulkUploadResult):
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
            referenceId=NotImplemented,
            templateEntryId=NotImplemented,
            eventType=NotImplemented,
            title=NotImplemented,
            description=NotImplemented,
            tags=NotImplemented,
            categoryIds=NotImplemented,
            resourceId=NotImplemented,
            startTime=NotImplemented,
            duration=NotImplemented,
            endTime=NotImplemented,
            recurrence=NotImplemented,
            coEditors=NotImplemented,
            coPublishers=NotImplemented,
            eventOrganizerId=NotImplemented,
            contentOwnerId=NotImplemented,
            templateEntryType=NotImplemented):
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

        # @var string
        self.referenceId = referenceId

        # @var string
        self.templateEntryId = templateEntryId

        # @var int
        self.eventType = eventType

        # @var string
        self.title = title

        # @var string
        self.description = description

        # @var string
        self.tags = tags

        # @var string
        self.categoryIds = categoryIds

        # ID of the resource specified for the new event.
        # @var string
        self.resourceId = resourceId

        # @var int
        self.startTime = startTime

        # @var int
        self.duration = duration

        # @var int
        self.endTime = endTime

        # @var string
        self.recurrence = recurrence

        # @var string
        self.coEditors = coEditors

        # @var string
        self.coPublishers = coPublishers

        # @var string
        self.eventOrganizerId = eventOrganizerId

        # @var string
        self.contentOwnerId = contentOwnerId

        # @var string
        self.templateEntryType = templateEntryType


    PROPERTY_LOADERS = {
        'referenceId': getXmlNodeText, 
        'templateEntryId': getXmlNodeText, 
        'eventType': getXmlNodeInt, 
        'title': getXmlNodeText, 
        'description': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'categoryIds': getXmlNodeText, 
        'resourceId': getXmlNodeText, 
        'startTime': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'endTime': getXmlNodeInt, 
        'recurrence': getXmlNodeText, 
        'coEditors': getXmlNodeText, 
        'coPublishers': getXmlNodeText, 
        'eventOrganizerId': getXmlNodeText, 
        'contentOwnerId': getXmlNodeText, 
        'templateEntryType': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBulkUploadResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadResultScheduleEvent.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadResult.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadResultScheduleEvent")
        kparams.addStringIfDefined("referenceId", self.referenceId)
        kparams.addStringIfDefined("templateEntryId", self.templateEntryId)
        kparams.addIntIfDefined("eventType", self.eventType)
        kparams.addStringIfDefined("title", self.title)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("categoryIds", self.categoryIds)
        kparams.addStringIfDefined("resourceId", self.resourceId)
        kparams.addIntIfDefined("startTime", self.startTime)
        kparams.addIntIfDefined("duration", self.duration)
        kparams.addIntIfDefined("endTime", self.endTime)
        kparams.addStringIfDefined("recurrence", self.recurrence)
        kparams.addStringIfDefined("coEditors", self.coEditors)
        kparams.addStringIfDefined("coPublishers", self.coPublishers)
        kparams.addStringIfDefined("eventOrganizerId", self.eventOrganizerId)
        kparams.addStringIfDefined("contentOwnerId", self.contentOwnerId)
        kparams.addStringIfDefined("templateEntryType", self.templateEntryType)
        return kparams

    def getReferenceId(self):
        return self.referenceId

    def setReferenceId(self, newReferenceId):
        self.referenceId = newReferenceId

    def getTemplateEntryId(self):
        return self.templateEntryId

    def setTemplateEntryId(self, newTemplateEntryId):
        self.templateEntryId = newTemplateEntryId

    def getEventType(self):
        return self.eventType

    def setEventType(self, newEventType):
        self.eventType = newEventType

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getCategoryIds(self):
        return self.categoryIds

    def setCategoryIds(self, newCategoryIds):
        self.categoryIds = newCategoryIds

    def getResourceId(self):
        return self.resourceId

    def setResourceId(self, newResourceId):
        self.resourceId = newResourceId

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, newStartTime):
        self.startTime = newStartTime

    def getDuration(self):
        return self.duration

    def setDuration(self, newDuration):
        self.duration = newDuration

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, newEndTime):
        self.endTime = newEndTime

    def getRecurrence(self):
        return self.recurrence

    def setRecurrence(self, newRecurrence):
        self.recurrence = newRecurrence

    def getCoEditors(self):
        return self.coEditors

    def setCoEditors(self, newCoEditors):
        self.coEditors = newCoEditors

    def getCoPublishers(self):
        return self.coPublishers

    def setCoPublishers(self, newCoPublishers):
        self.coPublishers = newCoPublishers

    def getEventOrganizerId(self):
        return self.eventOrganizerId

    def setEventOrganizerId(self, newEventOrganizerId):
        self.eventOrganizerId = newEventOrganizerId

    def getContentOwnerId(self):
        return self.contentOwnerId

    def setContentOwnerId(self, newContentOwnerId):
        self.contentOwnerId = newContentOwnerId

    def getTemplateEntryType(self):
        return self.templateEntryType

    def setTemplateEntryType(self, newTemplateEntryType):
        self.templateEntryType = newTemplateEntryType


# @package Kaltura
# @subpackage Client
class KalturaBulkUploadResultScheduleResource(KalturaBulkUploadResult):
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
            resourceId=NotImplemented,
            name=NotImplemented,
            type=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            tags=NotImplemented,
            parentType=NotImplemented,
            parentSystemName=NotImplemented):
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

        # @var string
        self.resourceId = resourceId

        # @var string
        self.name = name

        # @var string
        self.type = type

        # @var string
        self.systemName = systemName

        # @var string
        self.description = description

        # @var string
        self.tags = tags

        # @var string
        self.parentType = parentType

        # @var string
        self.parentSystemName = parentSystemName


    PROPERTY_LOADERS = {
        'resourceId': getXmlNodeText, 
        'name': getXmlNodeText, 
        'type': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'tags': getXmlNodeText, 
        'parentType': getXmlNodeText, 
        'parentSystemName': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBulkUploadResult.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadResultScheduleResource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadResult.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadResultScheduleResource")
        kparams.addStringIfDefined("resourceId", self.resourceId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("type", self.type)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("parentType", self.parentType)
        kparams.addStringIfDefined("parentSystemName", self.parentSystemName)
        return kparams

    def getResourceId(self):
        return self.resourceId

    def setResourceId(self, newResourceId):
        self.resourceId = newResourceId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getParentType(self):
        return self.parentType

    def setParentType(self, newParentType):
        self.parentType = newParentType

    def getParentSystemName(self):
        return self.parentSystemName

    def setParentSystemName(self, newParentSystemName):
        self.parentSystemName = newParentSystemName


# @package Kaltura
# @subpackage Client
class KalturaBulkUploadScheduleEventJobData(KalturaBulkUploadJobData):
    """Represents the abstract Bulk upload job data for general bulk upload"""

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
            privileges=NotImplemented):
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


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaBulkUploadJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadScheduleEventJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadJobData.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadScheduleEventJobData")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaBulkUploadICalJobData(KalturaBulkUploadScheduleEventJobData):
    """Represents the Bulk upload job data for iCal bulk upload"""

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
            eventsType=NotImplemented):
        KalturaBulkUploadScheduleEventJobData.__init__(self,
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

        # The type of the events that ill be created by this upload
        # @var KalturaScheduleEventType
        self.eventsType = eventsType


    PROPERTY_LOADERS = {
        'eventsType': (KalturaEnumsFactory.createInt, "KalturaScheduleEventType"), 
    }

    def fromXml(self, node):
        KalturaBulkUploadScheduleEventJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadICalJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadScheduleEventJobData.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadICalJobData")
        kparams.addIntEnumIfDefined("eventsType", self.eventsType)
        return kparams

    def getEventsType(self):
        return self.eventsType

    def setEventsType(self, newEventsType):
        self.eventsType = newEventsType


# @package Kaltura
# @subpackage Client
class KalturaBulkUploadScheduleEventCsvJobData(KalturaBulkUploadScheduleEventJobData):
    """Represents the Bulk upload job data for CSV bulk upload"""

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
            csvVersion=NotImplemented,
            columns=NotImplemented):
        KalturaBulkUploadScheduleEventJobData.__init__(self,
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
        # @var array of KalturaString
        self.columns = columns


    PROPERTY_LOADERS = {
        'csvVersion': (KalturaEnumsFactory.createInt, "KalturaBulkUploadCsvVersion"), 
        'columns': (KalturaObjectFactory.createArray, 'KalturaString'), 
    }

    def fromXml(self, node):
        KalturaBulkUploadScheduleEventJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkUploadScheduleEventCsvJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBulkUploadScheduleEventJobData.toParams(self)
        kparams.put("objectType", "KalturaBulkUploadScheduleEventCsvJobData")
        kparams.addArrayIfDefined("columns", self.columns)
        return kparams

    def getCsvVersion(self):
        return self.csvVersion

    def getColumns(self):
        return self.columns

    def setColumns(self, newColumns):
        self.columns = newColumns


########## services ##########
########## main ##########
class KalturaScheduleBulkUploadClientPlugin(KalturaClientPlugin):
    # KalturaScheduleBulkUploadClientPlugin
    instance = None

    # @return KalturaScheduleBulkUploadClientPlugin
    @staticmethod
    def get():
        if KalturaScheduleBulkUploadClientPlugin.instance == None:
            KalturaScheduleBulkUploadClientPlugin.instance = KalturaScheduleBulkUploadClientPlugin()
        return KalturaScheduleBulkUploadClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaBulkUploadResultScheduleEvent': KalturaBulkUploadResultScheduleEvent,
            'KalturaBulkUploadResultScheduleResource': KalturaBulkUploadResultScheduleResource,
            'KalturaBulkUploadScheduleEventJobData': KalturaBulkUploadScheduleEventJobData,
            'KalturaBulkUploadICalJobData': KalturaBulkUploadICalJobData,
            'KalturaBulkUploadScheduleEventCsvJobData': KalturaBulkUploadScheduleEventCsvJobData,
        }

    # @return string
    def getName(self):
        return 'scheduleBulkUpload'

