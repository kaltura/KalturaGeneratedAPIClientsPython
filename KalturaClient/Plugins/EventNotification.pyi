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
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaEventNotificationDelayedCondition(object):
    NONE = 0
    PENDING_ENTRY_READY = 1

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaEventNotificationTemplateStatus(object):
    DISABLED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaEventNotificationEventObjectType(object):
    AD_CUE_POINT = "adCuePointEventNotifications.AdCuePoint"
    ANNOTATION = "annotationEventNotifications.Annotation"
    ATTACHMENT_ASSET = "attachmentAssetEventNotifications.AttachmentAsset"
    CAPTION_ASSET = "captionAssetEventNotifications.CaptionAsset"
    CODE_CUE_POINT = "codeCuePointEventNotifications.CodeCuePoint"
    DISTRIBUTION_PROFILE = "contentDistributionEventNotifications.DistributionProfile"
    ENTRY_DISTRIBUTION = "contentDistributionEventNotifications.EntryDistribution"
    CUE_POINT = "cuePointEventNotifications.CuePoint"
    DROP_FOLDER = "dropFolderEventNotifications.DropFolder"
    DROP_FOLDER_FILE = "dropFolderEventNotifications.DropFolderFile"
    METADATA = "metadataEventNotifications.Metadata"
    SCHEDULE_EVENT = "scheduleEventNotifications.ScheduleEvent"
    SCHEDULE_EVENT_RESOURCE = "scheduleEventNotifications.ScheduleEventResource"
    SCHEDULE_RESOURCE = "scheduleEventNotifications.ScheduleResource"
    TRANSCRIPT_ASSET = "transcriptAssetEventNotifications.TranscriptAsset"
    VIRTUAL_EVENT = "virtualEventEventNotifications.VirtualEvent"
    ENTRY = "1"
    CATEGORY = "2"
    ASSET = "3"
    FLAVORASSET = "4"
    THUMBASSET = "5"
    KUSER = "8"
    ACCESSCONTROL = "9"
    BATCHJOB = "10"
    BULKUPLOADRESULT = "11"
    CATEGORYKUSER = "12"
    CONVERSIONPROFILE2 = "14"
    FLAVORPARAMS = "15"
    FLAVORPARAMSCONVERSIONPROFILE = "16"
    FLAVORPARAMSOUTPUT = "17"
    GENERICSYNDICATIONFEED = "18"
    KUSERTOUSERROLE = "19"
    PARTNER = "20"
    PERMISSION = "21"
    PERMISSIONITEM = "22"
    PERMISSIONTOPERMISSIONITEM = "23"
    SCHEDULER = "24"
    SCHEDULERCONFIG = "25"
    SCHEDULERSTATUS = "26"
    SCHEDULERWORKER = "27"
    STORAGEPROFILE = "28"
    SYNDICATIONFEED = "29"
    THUMBPARAMS = "31"
    THUMBPARAMSOUTPUT = "32"
    UPLOADTOKEN = "33"
    USERLOGINDATA = "34"
    USERROLE = "35"
    WIDGET = "36"
    CATEGORYENTRY = "37"
    LIVE_STREAM = "38"
    SERVER_NODE = "39"
    ENTRY_SERVER_NODE = "40"
    REACH_PROFILE = "41"
    ENTRY_VENDOR_TASK = "42"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEventNotificationEventType(object):
    INTEGRATION_JOB_CLOSED = "integrationEventNotifications.INTEGRATION_JOB_CLOSED"
    BATCH_JOB_STATUS = "1"
    OBJECT_ADDED = "2"
    OBJECT_CHANGED = "3"
    OBJECT_COPIED = "4"
    OBJECT_CREATED = "5"
    OBJECT_DATA_CHANGED = "6"
    OBJECT_DELETED = "7"
    OBJECT_ERASED = "8"
    OBJECT_READY_FOR_REPLACMENT = "9"
    OBJECT_SAVED = "10"
    OBJECT_UPDATED = "11"
    OBJECT_REPLACED = "12"
    OBJECT_READY_FOR_INDEX = "13"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEventNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEventNotificationTemplateType(object):
    BOOLEAN = "booleanNotification.Boolean"
    BPM_ABORT = "businessProcessNotification.BusinessProcessAbort"
    BPM_SIGNAL = "businessProcessNotification.BusinessProcessSignal"
    BPM_START = "businessProcessNotification.BusinessProcessStart"
    EMAIL = "emailNotification.Email"
    HTTP = "httpNotification.Http"
    KAFKA = "kafkaNotification.Kafka"
    PUSH = "pushNotification.Push"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEventNotificationParameter(KalturaObjectBase):
    key: str
    description: str
    value: KalturaStringValue
    def __init__(self,
            key: str = NotImplemented,
            description: str = NotImplemented,
            value: KalturaStringValue = NotImplemented): ...

    def getKey(self) -> str: ...
    def setKey(self, newKey: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getValue(self) -> KalturaStringValue: ...
    def setValue(self, newValue: KalturaStringValue) -> None: ...

class KalturaEventNotificationTemplate(KalturaObjectBase):
    id: int
    partnerId: int
    name: str
    systemName: str
    description: str
    type: KalturaEventNotificationTemplateType
    status: KalturaEventNotificationTemplateStatus
    createdAt: int
    updatedAt: int
    manualDispatchEnabled: bool
    automaticDispatchEnabled: bool
    eventType: KalturaEventNotificationEventType
    eventObjectType: KalturaEventNotificationEventObjectType
    eventConditions: List[KalturaCondition]
    contentParameters: List[KalturaEventNotificationParameter]
    userParameters: List[KalturaEventNotificationParameter]
    eventDelayedCondition: KalturaEventNotificationDelayedCondition
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            type: KalturaEventNotificationTemplateType = NotImplemented,
            status: KalturaEventNotificationTemplateStatus = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            manualDispatchEnabled: bool = NotImplemented,
            automaticDispatchEnabled: bool = NotImplemented,
            eventType: KalturaEventNotificationEventType = NotImplemented,
            eventObjectType: KalturaEventNotificationEventObjectType = NotImplemented,
            eventConditions: List[KalturaCondition] = NotImplemented,
            contentParameters: List[KalturaEventNotificationParameter] = NotImplemented,
            userParameters: List[KalturaEventNotificationParameter] = NotImplemented,
            eventDelayedCondition: KalturaEventNotificationDelayedCondition = NotImplemented): ...

    def getId(self) -> int: ...
    def getPartnerId(self) -> int: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getSystemName(self) -> str: ...
    def setSystemName(self, newSystemName: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getType(self) -> KalturaEventNotificationTemplateType: ...
    def setType(self, newType: KalturaEventNotificationTemplateType) -> None: ...
    def getStatus(self) -> KalturaEventNotificationTemplateStatus: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getManualDispatchEnabled(self) -> bool: ...
    def setManualDispatchEnabled(self, newManualDispatchEnabled: bool) -> None: ...
    def getAutomaticDispatchEnabled(self) -> bool: ...
    def setAutomaticDispatchEnabled(self, newAutomaticDispatchEnabled: bool) -> None: ...
    def getEventType(self) -> KalturaEventNotificationEventType: ...
    def setEventType(self, newEventType: KalturaEventNotificationEventType) -> None: ...
    def getEventObjectType(self) -> KalturaEventNotificationEventObjectType: ...
    def setEventObjectType(self, newEventObjectType: KalturaEventNotificationEventObjectType) -> None: ...
    def getEventConditions(self) -> List[KalturaCondition]: ...
    def setEventConditions(self, newEventConditions: List[KalturaCondition]) -> None: ...
    def getContentParameters(self) -> List[KalturaEventNotificationParameter]: ...
    def setContentParameters(self, newContentParameters: List[KalturaEventNotificationParameter]) -> None: ...
    def getUserParameters(self) -> List[KalturaEventNotificationParameter]: ...
    def setUserParameters(self, newUserParameters: List[KalturaEventNotificationParameter]) -> None: ...
    def getEventDelayedCondition(self) -> KalturaEventNotificationDelayedCondition: ...
    def setEventDelayedCondition(self, newEventDelayedCondition: KalturaEventNotificationDelayedCondition) -> None: ...

class KalturaEventFieldCondition(KalturaCondition):
    field: KalturaBooleanField
    def __init__(self,
            type: KalturaConditionType = NotImplemented,
            description: str = NotImplemented,
            not_: bool = NotImplemented,
            field: KalturaBooleanField = NotImplemented): ...

    def getField(self) -> KalturaBooleanField: ...
    def setField(self, newField: KalturaBooleanField) -> None: ...

class KalturaEventNotificationArrayParameter(KalturaEventNotificationParameter):
    values: List[KalturaString]
    allowedValues: List[KalturaStringValue]
    def __init__(self,
            key: str = NotImplemented,
            description: str = NotImplemented,
            value: KalturaStringValue = NotImplemented,
            values: List[KalturaString] = NotImplemented,
            allowedValues: List[KalturaStringValue] = NotImplemented): ...

    def getValues(self) -> List[KalturaString]: ...
    def setValues(self, newValues: List[KalturaString]) -> None: ...
    def getAllowedValues(self) -> List[KalturaStringValue]: ...
    def setAllowedValues(self, newAllowedValues: List[KalturaStringValue]) -> None: ...

class KalturaEventNotificationDispatchJobData(KalturaJobData):
    templateId: int
    contentParameters: List[KalturaKeyValue]
    def __init__(self,
            templateId: int = NotImplemented,
            contentParameters: List[KalturaKeyValue] = NotImplemented): ...

    def getTemplateId(self) -> int: ...
    def setTemplateId(self, newTemplateId: int) -> None: ...
    def getContentParameters(self) -> List[KalturaKeyValue]: ...
    def setContentParameters(self, newContentParameters: List[KalturaKeyValue]) -> None: ...

class KalturaEventNotificationScope(KalturaScope):
    objectId: str
    scopeObjectType: KalturaEventNotificationEventObjectType
    def __init__(self,
            objectId: str = NotImplemented,
            scopeObjectType: KalturaEventNotificationEventObjectType = NotImplemented): ...

    def getObjectId(self) -> str: ...
    def setObjectId(self, newObjectId: str) -> None: ...
    def getScopeObjectType(self) -> KalturaEventNotificationEventObjectType: ...
    def setScopeObjectType(self, newScopeObjectType: KalturaEventNotificationEventObjectType) -> None: ...

class KalturaEventNotificationTemplateBaseFilter(KalturaFilter):
    idEqual: int
    idIn: str
    partnerIdEqual: int
    partnerIdIn: str
    systemNameEqual: str
    systemNameIn: str
    typeEqual: KalturaEventNotificationTemplateType
    typeIn: str
    statusEqual: KalturaEventNotificationTemplateStatus
    statusIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            typeEqual: KalturaEventNotificationTemplateType = NotImplemented,
            typeIn: str = NotImplemented,
            statusEqual: KalturaEventNotificationTemplateStatus = NotImplemented,
            statusIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getPartnerIdEqual(self) -> int: ...
    def setPartnerIdEqual(self, newPartnerIdEqual: int) -> None: ...
    def getPartnerIdIn(self) -> str: ...
    def setPartnerIdIn(self, newPartnerIdIn: str) -> None: ...
    def getSystemNameEqual(self) -> str: ...
    def setSystemNameEqual(self, newSystemNameEqual: str) -> None: ...
    def getSystemNameIn(self) -> str: ...
    def setSystemNameIn(self, newSystemNameIn: str) -> None: ...
    def getTypeEqual(self) -> KalturaEventNotificationTemplateType: ...
    def setTypeEqual(self, newTypeEqual: KalturaEventNotificationTemplateType) -> None: ...
    def getTypeIn(self) -> str: ...
    def setTypeIn(self, newTypeIn: str) -> None: ...
    def getStatusEqual(self) -> KalturaEventNotificationTemplateStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaEventNotificationTemplateStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...

class KalturaEventNotificationTemplateListResponse(KalturaListResponse):
    objects: List[KalturaEventNotificationTemplate]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaEventNotificationTemplate] = NotImplemented): ...

    def getObjects(self) -> List[KalturaEventNotificationTemplate]: ...

class KalturaEventObjectChangedCondition(KalturaCondition):
    modifiedColumns: str
    def __init__(self,
            type: KalturaConditionType = NotImplemented,
            description: str = NotImplemented,
            not_: bool = NotImplemented,
            modifiedColumns: str = NotImplemented): ...

    def getModifiedColumns(self) -> str: ...
    def setModifiedColumns(self, newModifiedColumns: str) -> None: ...

class KalturaEventNotificationDispatchScope(KalturaEventNotificationScope):
    dynamicValues: List[KalturaKeyValue]
    def __init__(self,
            objectId: str = NotImplemented,
            scopeObjectType: KalturaEventNotificationEventObjectType = NotImplemented,
            dynamicValues: List[KalturaKeyValue] = NotImplemented): ...

    def getDynamicValues(self) -> List[KalturaKeyValue]: ...
    def setDynamicValues(self, newDynamicValues: List[KalturaKeyValue]) -> None: ...

class KalturaEventNotificationTemplateFilter(KalturaEventNotificationTemplateBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            typeEqual: KalturaEventNotificationTemplateType = NotImplemented,
            typeIn: str = NotImplemented,
            statusEqual: KalturaEventNotificationTemplateStatus = NotImplemented,
            statusIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaEventNotificationTemplateService(KalturaServiceBase):
    def add(self, eventNotificationTemplate: KalturaEventNotificationTemplate) -> KalturaEventNotificationTemplate: ...
    def clone(self, id: int, eventNotificationTemplate: KalturaEventNotificationTemplate = NotImplemented) -> KalturaEventNotificationTemplate: ...
    def delete(self, id: int) -> None: ...
    def dispatch(self, id: int, scope: KalturaEventNotificationScope) -> int: ...
    def get(self, id: int) -> KalturaEventNotificationTemplate: ...
    def list(self, filter: KalturaEventNotificationTemplateFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaEventNotificationTemplateListResponse: ...
    def listByPartner(self, filter: KalturaPartnerFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaEventNotificationTemplateListResponse: ...
    def listTemplates(self, filter: KalturaEventNotificationTemplateFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaEventNotificationTemplateListResponse: ...
    def register(self, notificationTemplateSystemName: str, pushNotificationParams: KalturaPushNotificationParams) -> KalturaPushNotificationData: ...
    def sendCommand(self, notificationTemplateSystemName: str, pushNotificationParams: KalturaPushNotificationParams, command: str) -> None: ...
    def update(self, id: int, eventNotificationTemplate: KalturaEventNotificationTemplate) -> KalturaEventNotificationTemplate: ...
    def updateStatus(self, id: int, status: int) -> KalturaEventNotificationTemplate: ...

class KalturaEventNotificationClientPluginServicesProxy:
    eventNotificationTemplate: KalturaEventNotificationTemplateService