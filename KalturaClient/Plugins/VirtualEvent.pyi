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
from .Schedule import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaVirtualEventStatus(object):
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVirtualScheduleEventSubType(object):
    AGENDA = 1
    REGISTRATION = 2
    MAIN_EVENT = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVirtualEventOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVirtualEvent(KalturaObjectBase):
    id: int
    partnerId: int
    name: str
    description: str
    status: KalturaVirtualEventStatus
    tags: str
    attendeesGroupIds: str
    adminsGroupIds: str
    registrationScheduleEventId: int
    agendaScheduleEventId: int
    mainEventScheduleEventId: int
    createdAt: int
    updatedAt: int
    deletionDueDate: int
    registrationFormSchema: str
    eventUrl: str
    webhookRegistrationToken: str
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            description: str = NotImplemented,
            status: KalturaVirtualEventStatus = NotImplemented,
            tags: str = NotImplemented,
            attendeesGroupIds: str = NotImplemented,
            adminsGroupIds: str = NotImplemented,
            registrationScheduleEventId: int = NotImplemented,
            agendaScheduleEventId: int = NotImplemented,
            mainEventScheduleEventId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            deletionDueDate: int = NotImplemented,
            registrationFormSchema: str = NotImplemented,
            eventUrl: str = NotImplemented,
            webhookRegistrationToken: str = NotImplemented): ...

    def getId(self) -> int: ...
    def getPartnerId(self) -> int: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getStatus(self) -> KalturaVirtualEventStatus: ...
    def getTags(self) -> str: ...
    def setTags(self, newTags: str) -> None: ...
    def getAttendeesGroupIds(self) -> str: ...
    def setAttendeesGroupIds(self, newAttendeesGroupIds: str) -> None: ...
    def getAdminsGroupIds(self) -> str: ...
    def setAdminsGroupIds(self, newAdminsGroupIds: str) -> None: ...
    def getRegistrationScheduleEventId(self) -> int: ...
    def setRegistrationScheduleEventId(self, newRegistrationScheduleEventId: int) -> None: ...
    def getAgendaScheduleEventId(self) -> int: ...
    def setAgendaScheduleEventId(self, newAgendaScheduleEventId: int) -> None: ...
    def getMainEventScheduleEventId(self) -> int: ...
    def setMainEventScheduleEventId(self, newMainEventScheduleEventId: int) -> None: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getDeletionDueDate(self) -> int: ...
    def setDeletionDueDate(self, newDeletionDueDate: int) -> None: ...
    def getRegistrationFormSchema(self) -> str: ...
    def setRegistrationFormSchema(self, newRegistrationFormSchema: str) -> None: ...
    def getEventUrl(self) -> str: ...
    def setEventUrl(self, newEventUrl: str) -> None: ...
    def getWebhookRegistrationToken(self) -> str: ...
    def setWebhookRegistrationToken(self, newWebhookRegistrationToken: str) -> None: ...

class KalturaVirtualEventBaseFilter(KalturaFilter):
    idEqual: int
    idIn: str
    idNotIn: str
    partnerIdEqual: int
    partnerIdIn: str
    statusEqual: KalturaVirtualEventStatus
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
            idNotIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            statusEqual: KalturaVirtualEventStatus = NotImplemented,
            statusIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getIdNotIn(self) -> str: ...
    def setIdNotIn(self, newIdNotIn: str) -> None: ...
    def getPartnerIdEqual(self) -> int: ...
    def setPartnerIdEqual(self, newPartnerIdEqual: int) -> None: ...
    def getPartnerIdIn(self) -> str: ...
    def setPartnerIdIn(self, newPartnerIdIn: str) -> None: ...
    def getStatusEqual(self) -> KalturaVirtualEventStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaVirtualEventStatus) -> None: ...
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

class KalturaVirtualEventListResponse(KalturaListResponse):
    objects: List[KalturaVirtualEvent]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaVirtualEvent] = NotImplemented): ...

    def getObjects(self) -> List[KalturaVirtualEvent]: ...
    def setObjects(self, newObjects: List[KalturaVirtualEvent]) -> None: ...

class KalturaVirtualScheduleEvent(KalturaScheduleEvent):
    virtualEventId: int
    virtualScheduleEventSubType: KalturaVirtualScheduleEventSubType
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            parentId: int = NotImplemented,
            summary: str = NotImplemented,
            description: str = NotImplemented,
            status: KalturaScheduleEventStatus = NotImplemented,
            startDate: int = NotImplemented,
            endDate: int = NotImplemented,
            referenceId: str = NotImplemented,
            linkedTo: KalturaLinkedScheduleEvent = NotImplemented,
            linkedBy: str = NotImplemented,
            classificationType: KalturaScheduleEventClassificationType = NotImplemented,
            geoLatitude: float = NotImplemented,
            geoLongitude: float = NotImplemented,
            location: str = NotImplemented,
            organizer: str = NotImplemented,
            ownerId: str = NotImplemented,
            priority: int = NotImplemented,
            sequence: int = NotImplemented,
            recurrenceType: KalturaScheduleEventRecurrenceType = NotImplemented,
            duration: int = NotImplemented,
            contact: str = NotImplemented,
            comment: str = NotImplemented,
            tags: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            recurrence: KalturaScheduleEventRecurrence = NotImplemented,
            virtualEventId: int = NotImplemented,
            virtualScheduleEventSubType: KalturaVirtualScheduleEventSubType = NotImplemented): ...

    def getVirtualEventId(self) -> int: ...
    def setVirtualEventId(self, newVirtualEventId: int) -> None: ...
    def getVirtualScheduleEventSubType(self) -> KalturaVirtualScheduleEventSubType: ...
    def setVirtualScheduleEventSubType(self, newVirtualScheduleEventSubType: KalturaVirtualScheduleEventSubType) -> None: ...

class KalturaVirtualEventFilter(KalturaVirtualEventBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            statusEqual: KalturaVirtualEventStatus = NotImplemented,
            statusIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaVirtualScheduleEventBaseFilter(KalturaScheduleEventFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            parentIdNotIn: str = NotImplemented,
            statusEqual: KalturaScheduleEventStatus = NotImplemented,
            statusIn: str = NotImplemented,
            startDateGreaterThanOrEqual: int = NotImplemented,
            startDateLessThanOrEqual: int = NotImplemented,
            endDateGreaterThanOrEqual: int = NotImplemented,
            endDateLessThanOrEqual: int = NotImplemented,
            referenceIdEqual: str = NotImplemented,
            referenceIdIn: str = NotImplemented,
            ownerIdEqual: str = NotImplemented,
            ownerIdIn: str = NotImplemented,
            priorityEqual: int = NotImplemented,
            priorityIn: str = NotImplemented,
            priorityGreaterThanOrEqual: int = NotImplemented,
            priorityLessThanOrEqual: int = NotImplemented,
            recurrenceTypeEqual: KalturaScheduleEventRecurrenceType = NotImplemented,
            recurrenceTypeIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            resourceIdsLike: str = NotImplemented,
            resourceIdsMultiLikeOr: str = NotImplemented,
            resourceIdsMultiLikeAnd: str = NotImplemented,
            parentResourceIdsLike: str = NotImplemented,
            parentResourceIdsMultiLikeOr: str = NotImplemented,
            parentResourceIdsMultiLikeAnd: str = NotImplemented,
            templateEntryCategoriesIdsMultiLikeAnd: str = NotImplemented,
            templateEntryCategoriesIdsMultiLikeOr: str = NotImplemented,
            resourceSystemNamesMultiLikeOr: str = NotImplemented,
            templateEntryCategoriesIdsLike: str = NotImplemented,
            resourceSystemNamesMultiLikeAnd: str = NotImplemented,
            resourceSystemNamesLike: str = NotImplemented,
            resourceIdEqual: str = NotImplemented): ...
        pass

class KalturaVirtualScheduleEventFilter(KalturaVirtualScheduleEventBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            parentIdNotIn: str = NotImplemented,
            statusEqual: KalturaScheduleEventStatus = NotImplemented,
            statusIn: str = NotImplemented,
            startDateGreaterThanOrEqual: int = NotImplemented,
            startDateLessThanOrEqual: int = NotImplemented,
            endDateGreaterThanOrEqual: int = NotImplemented,
            endDateLessThanOrEqual: int = NotImplemented,
            referenceIdEqual: str = NotImplemented,
            referenceIdIn: str = NotImplemented,
            ownerIdEqual: str = NotImplemented,
            ownerIdIn: str = NotImplemented,
            priorityEqual: int = NotImplemented,
            priorityIn: str = NotImplemented,
            priorityGreaterThanOrEqual: int = NotImplemented,
            priorityLessThanOrEqual: int = NotImplemented,
            recurrenceTypeEqual: KalturaScheduleEventRecurrenceType = NotImplemented,
            recurrenceTypeIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            resourceIdsLike: str = NotImplemented,
            resourceIdsMultiLikeOr: str = NotImplemented,
            resourceIdsMultiLikeAnd: str = NotImplemented,
            parentResourceIdsLike: str = NotImplemented,
            parentResourceIdsMultiLikeOr: str = NotImplemented,
            parentResourceIdsMultiLikeAnd: str = NotImplemented,
            templateEntryCategoriesIdsMultiLikeAnd: str = NotImplemented,
            templateEntryCategoriesIdsMultiLikeOr: str = NotImplemented,
            resourceSystemNamesMultiLikeOr: str = NotImplemented,
            templateEntryCategoriesIdsLike: str = NotImplemented,
            resourceSystemNamesMultiLikeAnd: str = NotImplemented,
            resourceSystemNamesLike: str = NotImplemented,
            resourceIdEqual: str = NotImplemented): ...
        pass

class KalturaVirtualEventService(KalturaServiceBase):
    def add(self, virtualEvent: KalturaVirtualEvent) -> KalturaVirtualEvent: ...
    def delete(self, id: int) -> None: ...
    def get(self, id: int) -> KalturaVirtualEvent: ...
    def list(self, filter: KalturaVirtualEventFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaVirtualEventListResponse: ...
    def update(self, id: int, virtualEvent: KalturaVirtualEvent) -> KalturaVirtualEvent: ...

class KalturaVirtualEventClientPluginServicesProxy:
    virtualEvent: KalturaVirtualEventService