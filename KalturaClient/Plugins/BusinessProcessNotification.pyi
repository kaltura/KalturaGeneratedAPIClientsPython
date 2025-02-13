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
from .EventNotification import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaBusinessProcessAbortNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBusinessProcessNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBusinessProcessProvider(object):
    ACTIVITI = "activitiBusinessProcessNotification.Activiti"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBusinessProcessServerOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBusinessProcessServerStatus(object):
    DISABLED = "1"
    ENABLED = "2"
    DELETED = "3"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBusinessProcessSignalNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBusinessProcessStartNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBusinessProcessCase(KalturaObjectBase):
    id: str
    businessProcessId: str
    businessProcessStartNotificationTemplateId: int
    suspended: bool
    activityId: str
    def __init__(self,
            id: str = NotImplemented,
            businessProcessId: str = NotImplemented,
            businessProcessStartNotificationTemplateId: int = NotImplemented,
            suspended: bool = NotImplemented,
            activityId: str = NotImplemented): ...

    def getId(self) -> str: ...
    def setId(self, newId: str) -> None: ...
    def getBusinessProcessId(self) -> str: ...
    def setBusinessProcessId(self, newBusinessProcessId: str) -> None: ...
    def getBusinessProcessStartNotificationTemplateId(self) -> int: ...
    def setBusinessProcessStartNotificationTemplateId(self, newBusinessProcessStartNotificationTemplateId: int) -> None: ...
    def getSuspended(self) -> bool: ...
    def setSuspended(self, newSuspended: bool) -> None: ...
    def getActivityId(self) -> str: ...
    def setActivityId(self, newActivityId: str) -> None: ...

class KalturaBusinessProcessServer(KalturaObjectBase):
    id: int
    createdAt: int
    updatedAt: int
    partnerId: int
    name: str
    systemName: str
    description: str
    status: KalturaBusinessProcessServerStatus
    type: KalturaBusinessProcessProvider
    dc: int
    def __init__(self,
            id: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            status: KalturaBusinessProcessServerStatus = NotImplemented,
            type: KalturaBusinessProcessProvider = NotImplemented,
            dc: int = NotImplemented): ...

    def getId(self) -> int: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getPartnerId(self) -> int: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getSystemName(self) -> str: ...
    def setSystemName(self, newSystemName: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getStatus(self) -> KalturaBusinessProcessServerStatus: ...
    def getType(self) -> KalturaBusinessProcessProvider: ...
    def getDc(self) -> int: ...
    def setDc(self, newDc: int) -> None: ...

class KalturaBusinessProcessNotificationTemplate(KalturaEventNotificationTemplate):
    serverId: int
    processId: str
    mainObjectCode: str
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
            eventDelayedCondition: KalturaEventNotificationDelayedCondition = NotImplemented,
            serverId: int = NotImplemented,
            processId: str = NotImplemented,
            mainObjectCode: str = NotImplemented): ...

    def getServerId(self) -> int: ...
    def setServerId(self, newServerId: int) -> None: ...
    def getProcessId(self) -> str: ...
    def setProcessId(self, newProcessId: str) -> None: ...
    def getMainObjectCode(self) -> str: ...
    def setMainObjectCode(self, newMainObjectCode: str) -> None: ...

class KalturaBusinessProcessServerBaseFilter(KalturaFilter):
    idEqual: int
    idIn: str
    idNotIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    partnerIdEqual: int
    partnerIdIn: str
    statusEqual: KalturaBusinessProcessServerStatus
    statusNotEqual: KalturaBusinessProcessServerStatus
    statusIn: str
    statusNotIn: str
    typeEqual: KalturaBusinessProcessProvider
    typeIn: str
    dcEqual: int
    dcEqOrNull: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            statusEqual: KalturaBusinessProcessServerStatus = NotImplemented,
            statusNotEqual: KalturaBusinessProcessServerStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            typeEqual: KalturaBusinessProcessProvider = NotImplemented,
            typeIn: str = NotImplemented,
            dcEqual: int = NotImplemented,
            dcEqOrNull: int = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getIdNotIn(self) -> str: ...
    def setIdNotIn(self, newIdNotIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...
    def getPartnerIdEqual(self) -> int: ...
    def setPartnerIdEqual(self, newPartnerIdEqual: int) -> None: ...
    def getPartnerIdIn(self) -> str: ...
    def setPartnerIdIn(self, newPartnerIdIn: str) -> None: ...
    def getStatusEqual(self) -> KalturaBusinessProcessServerStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaBusinessProcessServerStatus) -> None: ...
    def getStatusNotEqual(self) -> KalturaBusinessProcessServerStatus: ...
    def setStatusNotEqual(self, newStatusNotEqual: KalturaBusinessProcessServerStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getStatusNotIn(self) -> str: ...
    def setStatusNotIn(self, newStatusNotIn: str) -> None: ...
    def getTypeEqual(self) -> KalturaBusinessProcessProvider: ...
    def setTypeEqual(self, newTypeEqual: KalturaBusinessProcessProvider) -> None: ...
    def getTypeIn(self) -> str: ...
    def setTypeIn(self, newTypeIn: str) -> None: ...
    def getDcEqual(self) -> int: ...
    def setDcEqual(self, newDcEqual: int) -> None: ...
    def getDcEqOrNull(self) -> int: ...
    def setDcEqOrNull(self, newDcEqOrNull: int) -> None: ...

class KalturaBusinessProcessServerListResponse(KalturaListResponse):
    objects: List[KalturaBusinessProcessServer]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaBusinessProcessServer] = NotImplemented): ...

    def getObjects(self) -> List[KalturaBusinessProcessServer]: ...

class KalturaBusinessProcessAbortNotificationTemplate(KalturaBusinessProcessNotificationTemplate):
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
            eventDelayedCondition: KalturaEventNotificationDelayedCondition = NotImplemented,
            serverId: int = NotImplemented,
            processId: str = NotImplemented,
            mainObjectCode: str = NotImplemented): ...
        pass

class KalturaBusinessProcessNotificationDispatchJobData(KalturaEventNotificationDispatchJobData):
    server: KalturaBusinessProcessServer
    caseId: str
    def __init__(self,
            templateId: int = NotImplemented,
            contentParameters: List[KalturaKeyValue] = NotImplemented,
            server: KalturaBusinessProcessServer = NotImplemented,
            caseId: str = NotImplemented): ...

    def getServer(self) -> KalturaBusinessProcessServer: ...
    def setServer(self, newServer: KalturaBusinessProcessServer) -> None: ...
    def getCaseId(self) -> str: ...
    def setCaseId(self, newCaseId: str) -> None: ...

class KalturaBusinessProcessServerFilter(KalturaBusinessProcessServerBaseFilter):
    currentDcOrExternal: KalturaNullableBoolean
    currentDc: KalturaNullableBoolean
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            statusEqual: KalturaBusinessProcessServerStatus = NotImplemented,
            statusNotEqual: KalturaBusinessProcessServerStatus = NotImplemented,
            statusIn: str = NotImplemented,
            statusNotIn: str = NotImplemented,
            typeEqual: KalturaBusinessProcessProvider = NotImplemented,
            typeIn: str = NotImplemented,
            dcEqual: int = NotImplemented,
            dcEqOrNull: int = NotImplemented,
            currentDcOrExternal: KalturaNullableBoolean = NotImplemented,
            currentDc: KalturaNullableBoolean = NotImplemented): ...

    def getCurrentDcOrExternal(self) -> KalturaNullableBoolean: ...
    def setCurrentDcOrExternal(self, newCurrentDcOrExternal: KalturaNullableBoolean) -> None: ...
    def getCurrentDc(self) -> KalturaNullableBoolean: ...
    def setCurrentDc(self, newCurrentDc: KalturaNullableBoolean) -> None: ...

class KalturaBusinessProcessSignalNotificationTemplate(KalturaBusinessProcessNotificationTemplate):
    message: str
    eventId: str
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
            eventDelayedCondition: KalturaEventNotificationDelayedCondition = NotImplemented,
            serverId: int = NotImplemented,
            processId: str = NotImplemented,
            mainObjectCode: str = NotImplemented,
            message: str = NotImplemented,
            eventId: str = NotImplemented): ...

    def getMessage(self) -> str: ...
    def setMessage(self, newMessage: str) -> None: ...
    def getEventId(self) -> str: ...
    def setEventId(self, newEventId: str) -> None: ...

class KalturaBusinessProcessStartNotificationTemplate(KalturaBusinessProcessNotificationTemplate):
    abortOnDeletion: bool
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
            eventDelayedCondition: KalturaEventNotificationDelayedCondition = NotImplemented,
            serverId: int = NotImplemented,
            processId: str = NotImplemented,
            mainObjectCode: str = NotImplemented,
            abortOnDeletion: bool = NotImplemented): ...

    def getAbortOnDeletion(self) -> bool: ...
    def setAbortOnDeletion(self, newAbortOnDeletion: bool) -> None: ...

class KalturaBusinessProcessNotificationTemplateBaseFilter(KalturaEventNotificationTemplateFilter):
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

class KalturaBusinessProcessNotificationTemplateFilter(KalturaBusinessProcessNotificationTemplateBaseFilter):
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

class KalturaBusinessProcessAbortNotificationTemplateBaseFilter(KalturaBusinessProcessNotificationTemplateFilter):
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

class KalturaBusinessProcessSignalNotificationTemplateBaseFilter(KalturaBusinessProcessNotificationTemplateFilter):
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

class KalturaBusinessProcessStartNotificationTemplateBaseFilter(KalturaBusinessProcessNotificationTemplateFilter):
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

class KalturaBusinessProcessAbortNotificationTemplateFilter(KalturaBusinessProcessAbortNotificationTemplateBaseFilter):
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

class KalturaBusinessProcessSignalNotificationTemplateFilter(KalturaBusinessProcessSignalNotificationTemplateBaseFilter):
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

class KalturaBusinessProcessStartNotificationTemplateFilter(KalturaBusinessProcessStartNotificationTemplateBaseFilter):
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

class KalturaBusinessProcessCaseService(KalturaServiceBase):
    def abort(self, objectType: str, objectId: str, businessProcessStartNotificationTemplateId: int) -> None: ...
    def list(self, objectType: str, objectId: str) -> List[KalturaBusinessProcessCase]: ...
    def serveDiagram(self, objectType: str, objectId: str, businessProcessStartNotificationTemplateId: int) -> IO[Any]: ...

class KalturaBusinessProcessNotificationClientPluginServicesProxy:
    businessProcessCase: KalturaBusinessProcessCaseService