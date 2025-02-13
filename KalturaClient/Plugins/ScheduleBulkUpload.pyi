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
from typing import List, IO, Any
from .Core import *
from .BulkUploadCsv import *
from .Schedule import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaBulkUploadResultScheduleEvent(KalturaBulkUploadResult):
    referenceId: str
    templateEntryId: str
    eventType: int
    title: str
    description: str
    tags: str
    categoryIds: str
    resourceId: str
    startTime: int
    duration: int
    endTime: int
    recurrence: str
    coEditors: str
    coPublishers: str
    eventOrganizerId: str
    contentOwnerId: str
    templateEntryType: str
    def __init__(self,
            id: int = NotImplemented,
            bulkUploadJobId: int = NotImplemented,
            lineIndex: int = NotImplemented,
            partnerId: int = NotImplemented,
            status: KalturaBulkUploadResultStatus = NotImplemented,
            action: KalturaBulkUploadAction = NotImplemented,
            objectId: str = NotImplemented,
            objectStatus: int = NotImplemented,
            bulkUploadResultObjectType: KalturaBulkUploadObjectType = NotImplemented,
            rowData: str = NotImplemented,
            partnerData: str = NotImplemented,
            objectErrorDescription: str = NotImplemented,
            pluginsData: List[KalturaBulkUploadPluginData] = NotImplemented,
            errorDescription: str = NotImplemented,
            errorCode: str = NotImplemented,
            errorType: int = NotImplemented,
            referenceId: str = NotImplemented,
            templateEntryId: str = NotImplemented,
            eventType: int = NotImplemented,
            title: str = NotImplemented,
            description: str = NotImplemented,
            tags: str = NotImplemented,
            categoryIds: str = NotImplemented,
            resourceId: str = NotImplemented,
            startTime: int = NotImplemented,
            duration: int = NotImplemented,
            endTime: int = NotImplemented,
            recurrence: str = NotImplemented,
            coEditors: str = NotImplemented,
            coPublishers: str = NotImplemented,
            eventOrganizerId: str = NotImplemented,
            contentOwnerId: str = NotImplemented,
            templateEntryType: str = NotImplemented): ...

    def getReferenceId(self) -> str: ...
    def setReferenceId(self, newReferenceId: str) -> None: ...
    def getTemplateEntryId(self) -> str: ...
    def setTemplateEntryId(self, newTemplateEntryId: str) -> None: ...
    def getEventType(self) -> int: ...
    def setEventType(self, newEventType: int) -> None: ...
    def getTitle(self) -> str: ...
    def setTitle(self, newTitle: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getTags(self) -> str: ...
    def setTags(self, newTags: str) -> None: ...
    def getCategoryIds(self) -> str: ...
    def setCategoryIds(self, newCategoryIds: str) -> None: ...
    def getResourceId(self) -> str: ...
    def setResourceId(self, newResourceId: str) -> None: ...
    def getStartTime(self) -> int: ...
    def setStartTime(self, newStartTime: int) -> None: ...
    def getDuration(self) -> int: ...
    def setDuration(self, newDuration: int) -> None: ...
    def getEndTime(self) -> int: ...
    def setEndTime(self, newEndTime: int) -> None: ...
    def getRecurrence(self) -> str: ...
    def setRecurrence(self, newRecurrence: str) -> None: ...
    def getCoEditors(self) -> str: ...
    def setCoEditors(self, newCoEditors: str) -> None: ...
    def getCoPublishers(self) -> str: ...
    def setCoPublishers(self, newCoPublishers: str) -> None: ...
    def getEventOrganizerId(self) -> str: ...
    def setEventOrganizerId(self, newEventOrganizerId: str) -> None: ...
    def getContentOwnerId(self) -> str: ...
    def setContentOwnerId(self, newContentOwnerId: str) -> None: ...
    def getTemplateEntryType(self) -> str: ...
    def setTemplateEntryType(self, newTemplateEntryType: str) -> None: ...

class KalturaBulkUploadResultScheduleResource(KalturaBulkUploadResult):
    resourceId: str
    name: str
    type: str
    systemName: str
    description: str
    tags: str
    parentType: str
    parentSystemName: str
    def __init__(self,
            id: int = NotImplemented,
            bulkUploadJobId: int = NotImplemented,
            lineIndex: int = NotImplemented,
            partnerId: int = NotImplemented,
            status: KalturaBulkUploadResultStatus = NotImplemented,
            action: KalturaBulkUploadAction = NotImplemented,
            objectId: str = NotImplemented,
            objectStatus: int = NotImplemented,
            bulkUploadResultObjectType: KalturaBulkUploadObjectType = NotImplemented,
            rowData: str = NotImplemented,
            partnerData: str = NotImplemented,
            objectErrorDescription: str = NotImplemented,
            pluginsData: List[KalturaBulkUploadPluginData] = NotImplemented,
            errorDescription: str = NotImplemented,
            errorCode: str = NotImplemented,
            errorType: int = NotImplemented,
            resourceId: str = NotImplemented,
            name: str = NotImplemented,
            type: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            tags: str = NotImplemented,
            parentType: str = NotImplemented,
            parentSystemName: str = NotImplemented): ...

    def getResourceId(self) -> str: ...
    def setResourceId(self, newResourceId: str) -> None: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getType(self) -> str: ...
    def setType(self, newType: str) -> None: ...
    def getSystemName(self) -> str: ...
    def setSystemName(self, newSystemName: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getTags(self) -> str: ...
    def setTags(self, newTags: str) -> None: ...
    def getParentType(self) -> str: ...
    def setParentType(self, newParentType: str) -> None: ...
    def getParentSystemName(self) -> str: ...
    def setParentSystemName(self, newParentSystemName: str) -> None: ...

class KalturaBulkUploadScheduleEventJobData(KalturaBulkUploadJobData):
    def __init__(self,
            userId: str = NotImplemented,
            uploadedBy: str = NotImplemented,
            conversionProfileId: int = NotImplemented,
            resultsFileLocalPath: str = NotImplemented,
            resultsFileUrl: str = NotImplemented,
            numOfEntries: int = NotImplemented,
            numOfObjects: int = NotImplemented,
            filePath: str = NotImplemented,
            bulkUploadObjectType: KalturaBulkUploadObjectType = NotImplemented,
            fileName: str = NotImplemented,
            objectData: KalturaBulkUploadObjectData = NotImplemented,
            type: KalturaBulkUploadType = NotImplemented,
            emailRecipients: str = NotImplemented,
            numOfErrorObjects: int = NotImplemented,
            privileges: str = NotImplemented): ...
        pass

class KalturaBulkUploadICalJobData(KalturaBulkUploadScheduleEventJobData):
    eventsType: KalturaScheduleEventType
    def __init__(self,
            userId: str = NotImplemented,
            uploadedBy: str = NotImplemented,
            conversionProfileId: int = NotImplemented,
            resultsFileLocalPath: str = NotImplemented,
            resultsFileUrl: str = NotImplemented,
            numOfEntries: int = NotImplemented,
            numOfObjects: int = NotImplemented,
            filePath: str = NotImplemented,
            bulkUploadObjectType: KalturaBulkUploadObjectType = NotImplemented,
            fileName: str = NotImplemented,
            objectData: KalturaBulkUploadObjectData = NotImplemented,
            type: KalturaBulkUploadType = NotImplemented,
            emailRecipients: str = NotImplemented,
            numOfErrorObjects: int = NotImplemented,
            privileges: str = NotImplemented,
            eventsType: KalturaScheduleEventType = NotImplemented): ...

    def getEventsType(self) -> KalturaScheduleEventType: ...
    def setEventsType(self, newEventsType: KalturaScheduleEventType) -> None: ...

class KalturaBulkUploadScheduleEventCsvJobData(KalturaBulkUploadScheduleEventJobData):
    csvVersion: KalturaBulkUploadCsvVersion
    columns: List[KalturaString]
    def __init__(self,
            userId: str = NotImplemented,
            uploadedBy: str = NotImplemented,
            conversionProfileId: int = NotImplemented,
            resultsFileLocalPath: str = NotImplemented,
            resultsFileUrl: str = NotImplemented,
            numOfEntries: int = NotImplemented,
            numOfObjects: int = NotImplemented,
            filePath: str = NotImplemented,
            bulkUploadObjectType: KalturaBulkUploadObjectType = NotImplemented,
            fileName: str = NotImplemented,
            objectData: KalturaBulkUploadObjectData = NotImplemented,
            type: KalturaBulkUploadType = NotImplemented,
            emailRecipients: str = NotImplemented,
            numOfErrorObjects: int = NotImplemented,
            privileges: str = NotImplemented,
            csvVersion: KalturaBulkUploadCsvVersion = NotImplemented,
            columns: List[KalturaString] = NotImplemented): ...

    def getCsvVersion(self) -> KalturaBulkUploadCsvVersion: ...
    def getColumns(self) -> List[KalturaString]: ...
    def setColumns(self, newColumns: List[KalturaString]) -> None: ...

class KalturaScheduleBulkUploadClientPluginServicesProxy: