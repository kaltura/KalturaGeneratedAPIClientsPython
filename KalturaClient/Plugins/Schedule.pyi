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

class KalturaScheduleEventClassificationType(object):
    PUBLIC_EVENT = 1
    PRIVATE_EVENT = 2
    CONFIDENTIAL_EVENT = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaScheduleEventConflictType(object):
    RESOURCE_CONFLICT = 1
    BLACKOUT_CONFLICT = 2
    BOTH = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaScheduleEventRecurrenceType(object):
    NONE = 0
    RECURRING = 1
    RECURRENCE = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaScheduleEventStatus(object):
    CANCELLED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaScheduleEventType(object):
    RECORD = 1
    LIVE_STREAM = 2
    BLACKOUT = 3
    MEETING = 4
    LIVE_REDIRECT = 5
    VOD = 6

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaScheduleResourceStatus(object):
    DISABLED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaCameraScheduleResourceOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEntryScheduleEventOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    END_DATE_ASC = "+endDate"
    PRIORITY_ASC = "+priority"
    START_DATE_ASC = "+startDate"
    SUMMARY_ASC = "+summary"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    END_DATE_DESC = "-endDate"
    PRIORITY_DESC = "-priority"
    START_DATE_DESC = "-startDate"
    SUMMARY_DESC = "-summary"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaLiveEntryScheduleResourceOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaLiveStreamScheduleEventOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    END_DATE_ASC = "+endDate"
    PRIORITY_ASC = "+priority"
    START_DATE_ASC = "+startDate"
    SUMMARY_ASC = "+summary"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    END_DATE_DESC = "-endDate"
    PRIORITY_DESC = "-priority"
    START_DATE_DESC = "-startDate"
    SUMMARY_DESC = "-summary"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaLocationScheduleResourceOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaRecordScheduleEventOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    END_DATE_ASC = "+endDate"
    PRIORITY_ASC = "+priority"
    START_DATE_ASC = "+startDate"
    SUMMARY_ASC = "+summary"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    END_DATE_DESC = "-endDate"
    PRIORITY_DESC = "-priority"
    START_DATE_DESC = "-startDate"
    SUMMARY_DESC = "-summary"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaScheduleEventOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    END_DATE_ASC = "+endDate"
    PRIORITY_ASC = "+priority"
    START_DATE_ASC = "+startDate"
    SUMMARY_ASC = "+summary"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    END_DATE_DESC = "-endDate"
    PRIORITY_DESC = "-priority"
    START_DATE_DESC = "-startDate"
    SUMMARY_DESC = "-summary"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaScheduleEventRecurrenceDay(object):
    FRIDAY = "FR"
    MONDAY = "MO"
    SATURDAY = "SA"
    SUNDAY = "SU"
    THURSDAY = "TH"
    TUESDAY = "TU"
    WEDNESDAY = "WE"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaScheduleEventRecurrenceFrequency(object):
    DAILY = "days"
    HOURLY = "hours"
    MINUTELY = "minutes"
    MONTHLY = "months"
    SECONDLY = "seconds"
    WEEKLY = "weeks"
    YEARLY = "years"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaScheduleEventResourceOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaScheduleResourceOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaLinkedScheduleEvent(KalturaObjectBase):
    offset: int
    eventId: int
    def __init__(self,
            offset: int = NotImplemented,
            eventId: int = NotImplemented): ...

    def getOffset(self) -> int: ...
    def setOffset(self, newOffset: int) -> None: ...
    def getEventId(self) -> int: ...
    def setEventId(self, newEventId: int) -> None: ...

class KalturaLiveFeature(KalturaObjectBase):
    systemName: str
    preStartTime: int
    postEndTime: int
    def __init__(self,
            systemName: str = NotImplemented,
            preStartTime: int = NotImplemented,
            postEndTime: int = NotImplemented): ...

    def getSystemName(self) -> str: ...
    def setSystemName(self, newSystemName: str) -> None: ...
    def getPreStartTime(self) -> int: ...
    def setPreStartTime(self, newPreStartTime: int) -> None: ...
    def getPostEndTime(self) -> int: ...
    def setPostEndTime(self, newPostEndTime: int) -> None: ...

class KalturaScheduleEventRecurrence(KalturaObjectBase):
    name: str
    frequency: KalturaScheduleEventRecurrenceFrequency
    until: int
    timeZone: str
    count: int
    interval: int
    bySecond: str
    byMinute: str
    byHour: str
    byDay: str
    byMonthDay: str
    byYearDay: str
    byWeekNumber: str
    byMonth: str
    byOffset: str
    weekStartDay: KalturaScheduleEventRecurrenceDay
    def __init__(self,
            name: str = NotImplemented,
            frequency: KalturaScheduleEventRecurrenceFrequency = NotImplemented,
            until: int = NotImplemented,
            timeZone: str = NotImplemented,
            count: int = NotImplemented,
            interval: int = NotImplemented,
            bySecond: str = NotImplemented,
            byMinute: str = NotImplemented,
            byHour: str = NotImplemented,
            byDay: str = NotImplemented,
            byMonthDay: str = NotImplemented,
            byYearDay: str = NotImplemented,
            byWeekNumber: str = NotImplemented,
            byMonth: str = NotImplemented,
            byOffset: str = NotImplemented,
            weekStartDay: KalturaScheduleEventRecurrenceDay = NotImplemented): ...

    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getFrequency(self) -> KalturaScheduleEventRecurrenceFrequency: ...
    def setFrequency(self, newFrequency: KalturaScheduleEventRecurrenceFrequency) -> None: ...
    def getUntil(self) -> int: ...
    def setUntil(self, newUntil: int) -> None: ...
    def getTimeZone(self) -> str: ...
    def setTimeZone(self, newTimeZone: str) -> None: ...
    def getCount(self) -> int: ...
    def setCount(self, newCount: int) -> None: ...
    def getInterval(self) -> int: ...
    def setInterval(self, newInterval: int) -> None: ...
    def getBySecond(self) -> str: ...
    def setBySecond(self, newBySecond: str) -> None: ...
    def getByMinute(self) -> str: ...
    def setByMinute(self, newByMinute: str) -> None: ...
    def getByHour(self) -> str: ...
    def setByHour(self, newByHour: str) -> None: ...
    def getByDay(self) -> str: ...
    def setByDay(self, newByDay: str) -> None: ...
    def getByMonthDay(self) -> str: ...
    def setByMonthDay(self, newByMonthDay: str) -> None: ...
    def getByYearDay(self) -> str: ...
    def setByYearDay(self, newByYearDay: str) -> None: ...
    def getByWeekNumber(self) -> str: ...
    def setByWeekNumber(self, newByWeekNumber: str) -> None: ...
    def getByMonth(self) -> str: ...
    def setByMonth(self, newByMonth: str) -> None: ...
    def getByOffset(self) -> str: ...
    def setByOffset(self, newByOffset: str) -> None: ...
    def getWeekStartDay(self) -> KalturaScheduleEventRecurrenceDay: ...
    def setWeekStartDay(self, newWeekStartDay: KalturaScheduleEventRecurrenceDay) -> None: ...

class KalturaScheduleEvent(KalturaObjectBase):
    id: int
    partnerId: int
    parentId: int
    summary: str
    description: str
    status: KalturaScheduleEventStatus
    startDate: int
    endDate: int
    referenceId: str
    linkedTo: KalturaLinkedScheduleEvent
    linkedBy: str
    classificationType: KalturaScheduleEventClassificationType
    geoLatitude: float
    geoLongitude: float
    location: str
    organizer: str
    ownerId: str
    priority: int
    sequence: int
    recurrenceType: KalturaScheduleEventRecurrenceType
    duration: int
    contact: str
    comment: str
    tags: str
    createdAt: int
    updatedAt: int
    recurrence: KalturaScheduleEventRecurrence
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
            recurrence: KalturaScheduleEventRecurrence = NotImplemented): ...

    def getId(self) -> int: ...
    def getPartnerId(self) -> int: ...
    def getParentId(self) -> int: ...
    def getSummary(self) -> str: ...
    def setSummary(self, newSummary: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getStatus(self) -> KalturaScheduleEventStatus: ...
    def getStartDate(self) -> int: ...
    def setStartDate(self, newStartDate: int) -> None: ...
    def getEndDate(self) -> int: ...
    def setEndDate(self, newEndDate: int) -> None: ...
    def getReferenceId(self) -> str: ...
    def setReferenceId(self, newReferenceId: str) -> None: ...
    def getLinkedTo(self) -> KalturaLinkedScheduleEvent: ...
    def setLinkedTo(self, newLinkedTo: KalturaLinkedScheduleEvent) -> None: ...
    def getLinkedBy(self) -> str: ...
    def setLinkedBy(self, newLinkedBy: str) -> None: ...
    def getClassificationType(self) -> KalturaScheduleEventClassificationType: ...
    def setClassificationType(self, newClassificationType: KalturaScheduleEventClassificationType) -> None: ...
    def getGeoLatitude(self) -> float: ...
    def setGeoLatitude(self, newGeoLatitude: float) -> None: ...
    def getGeoLongitude(self) -> float: ...
    def setGeoLongitude(self, newGeoLongitude: float) -> None: ...
    def getLocation(self) -> str: ...
    def setLocation(self, newLocation: str) -> None: ...
    def getOrganizer(self) -> str: ...
    def setOrganizer(self, newOrganizer: str) -> None: ...
    def getOwnerId(self) -> str: ...
    def setOwnerId(self, newOwnerId: str) -> None: ...
    def getPriority(self) -> int: ...
    def setPriority(self, newPriority: int) -> None: ...
    def getSequence(self) -> int: ...
    def setSequence(self, newSequence: int) -> None: ...
    def getRecurrenceType(self) -> KalturaScheduleEventRecurrenceType: ...
    def setRecurrenceType(self, newRecurrenceType: KalturaScheduleEventRecurrenceType) -> None: ...
    def getDuration(self) -> int: ...
    def setDuration(self, newDuration: int) -> None: ...
    def getContact(self) -> str: ...
    def setContact(self, newContact: str) -> None: ...
    def getComment(self) -> str: ...
    def setComment(self, newComment: str) -> None: ...
    def getTags(self) -> str: ...
    def setTags(self, newTags: str) -> None: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getRecurrence(self) -> KalturaScheduleEventRecurrence: ...
    def setRecurrence(self, newRecurrence: KalturaScheduleEventRecurrence) -> None: ...

class KalturaScheduleEventResource(KalturaObjectBase):
    eventId: int
    resourceId: int
    partnerId: int
    createdAt: int
    updatedAt: int
    def __init__(self,
            eventId: int = NotImplemented,
            resourceId: int = NotImplemented,
            partnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented): ...

    def getEventId(self) -> int: ...
    def setEventId(self, newEventId: int) -> None: ...
    def getResourceId(self) -> int: ...
    def setResourceId(self, newResourceId: int) -> None: ...
    def getPartnerId(self) -> int: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...

class KalturaScheduleResource(KalturaObjectBase):
    id: int
    parentId: int
    partnerId: int
    name: str
    systemName: str
    description: str
    status: KalturaScheduleResourceStatus
    tags: str
    createdAt: int
    updatedAt: int
    def __init__(self,
            id: int = NotImplemented,
            parentId: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            status: KalturaScheduleResourceStatus = NotImplemented,
            tags: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented): ...

    def getId(self) -> int: ...
    def getParentId(self) -> int: ...
    def setParentId(self, newParentId: int) -> None: ...
    def getPartnerId(self) -> int: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getSystemName(self) -> str: ...
    def setSystemName(self, newSystemName: str) -> None: ...
    def getDescription(self) -> str: ...
    def setDescription(self, newDescription: str) -> None: ...
    def getStatus(self) -> KalturaScheduleResourceStatus: ...
    def getTags(self) -> str: ...
    def setTags(self, newTags: str) -> None: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...

class KalturaBlackoutScheduleEvent(KalturaScheduleEvent):
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
            recurrence: KalturaScheduleEventRecurrence = NotImplemented): ...
        pass

class KalturaCameraScheduleResource(KalturaScheduleResource):
    streamUrl: str
    def __init__(self,
            id: int = NotImplemented,
            parentId: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            status: KalturaScheduleResourceStatus = NotImplemented,
            tags: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            streamUrl: str = NotImplemented): ...

    def getStreamUrl(self) -> str: ...
    def setStreamUrl(self, newStreamUrl: str) -> None: ...

class KalturaEntryScheduleEvent(KalturaScheduleEvent):
    templateEntryId: str
    entryIds: str
    categoryIds: str
    blackoutConflicts: List[KalturaScheduleEvent]
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
            templateEntryId: str = NotImplemented,
            entryIds: str = NotImplemented,
            categoryIds: str = NotImplemented,
            blackoutConflicts: List[KalturaScheduleEvent] = NotImplemented): ...

    def getTemplateEntryId(self) -> str: ...
    def setTemplateEntryId(self, newTemplateEntryId: str) -> None: ...
    def getEntryIds(self) -> str: ...
    def setEntryIds(self, newEntryIds: str) -> None: ...
    def getCategoryIds(self) -> str: ...
    def setCategoryIds(self, newCategoryIds: str) -> None: ...
    def getBlackoutConflicts(self) -> List[KalturaScheduleEvent]: ...

class KalturaLiveCaptionFeature(KalturaLiveFeature):
    mediaUrl: str
    mediaKey: str
    captionUrl: str
    captionToken: str
    inputDelay: int
    captionFormat: str
    language: str
    def __init__(self,
            systemName: str = NotImplemented,
            preStartTime: int = NotImplemented,
            postEndTime: int = NotImplemented,
            mediaUrl: str = NotImplemented,
            mediaKey: str = NotImplemented,
            captionUrl: str = NotImplemented,
            captionToken: str = NotImplemented,
            inputDelay: int = NotImplemented,
            captionFormat: str = NotImplemented,
            language: str = NotImplemented): ...

    def getMediaUrl(self) -> str: ...
    def setMediaUrl(self, newMediaUrl: str) -> None: ...
    def getMediaKey(self) -> str: ...
    def setMediaKey(self, newMediaKey: str) -> None: ...
    def getCaptionUrl(self) -> str: ...
    def setCaptionUrl(self, newCaptionUrl: str) -> None: ...
    def getCaptionToken(self) -> str: ...
    def setCaptionToken(self, newCaptionToken: str) -> None: ...
    def getInputDelay(self) -> int: ...
    def setInputDelay(self, newInputDelay: int) -> None: ...
    def getCaptionFormat(self) -> str: ...
    def setCaptionFormat(self, newCaptionFormat: str) -> None: ...
    def getLanguage(self) -> str: ...
    def setLanguage(self, newLanguage: str) -> None: ...

class KalturaLiveEntryScheduleResource(KalturaScheduleResource):
    entryId: str
    def __init__(self,
            id: int = NotImplemented,
            parentId: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            status: KalturaScheduleResourceStatus = NotImplemented,
            tags: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            entryId: str = NotImplemented): ...

    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...

class KalturaLiveRestreamFeature(KalturaLiveFeature):
    primaryUrl: str
    secondaryUrl: str
    playbackUrl: str
    streamKey: str
    def __init__(self,
            systemName: str = NotImplemented,
            preStartTime: int = NotImplemented,
            postEndTime: int = NotImplemented,
            primaryUrl: str = NotImplemented,
            secondaryUrl: str = NotImplemented,
            playbackUrl: str = NotImplemented,
            streamKey: str = NotImplemented): ...

    def getPrimaryUrl(self) -> str: ...
    def setPrimaryUrl(self, newPrimaryUrl: str) -> None: ...
    def getSecondaryUrl(self) -> str: ...
    def setSecondaryUrl(self, newSecondaryUrl: str) -> None: ...
    def getPlaybackUrl(self) -> str: ...
    def setPlaybackUrl(self, newPlaybackUrl: str) -> None: ...
    def getStreamKey(self) -> str: ...
    def setStreamKey(self, newStreamKey: str) -> None: ...

class KalturaLocationScheduleResource(KalturaScheduleResource):
    def __init__(self,
            id: int = NotImplemented,
            parentId: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            status: KalturaScheduleResourceStatus = NotImplemented,
            tags: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented): ...
        pass

class KalturaScheduleEventListResponse(KalturaListResponse):
    objects: List[KalturaScheduleEvent]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaScheduleEvent] = NotImplemented): ...

    def getObjects(self) -> List[KalturaScheduleEvent]: ...

class KalturaScheduleEventResourceListResponse(KalturaListResponse):
    objects: List[KalturaScheduleEventResource]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaScheduleEventResource] = NotImplemented): ...

    def getObjects(self) -> List[KalturaScheduleEventResource]: ...

class KalturaScheduleResourceListResponse(KalturaListResponse):
    objects: List[KalturaScheduleResource]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaScheduleResource] = NotImplemented): ...

    def getObjects(self) -> List[KalturaScheduleResource]: ...

class KalturaBaseLiveScheduleEvent(KalturaEntryScheduleEvent):
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
            templateEntryId: str = NotImplemented,
            entryIds: str = NotImplemented,
            categoryIds: str = NotImplemented,
            blackoutConflicts: List[KalturaScheduleEvent] = NotImplemented): ...
        pass

class KalturaMeetingScheduleEvent(KalturaEntryScheduleEvent):
    preStartTime: int
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
            templateEntryId: str = NotImplemented,
            entryIds: str = NotImplemented,
            categoryIds: str = NotImplemented,
            blackoutConflicts: List[KalturaScheduleEvent] = NotImplemented,
            preStartTime: int = NotImplemented): ...

    def getPreStartTime(self) -> int: ...
    def setPreStartTime(self, newPreStartTime: int) -> None: ...

class KalturaRecordScheduleEvent(KalturaEntryScheduleEvent):
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
            templateEntryId: str = NotImplemented,
            entryIds: str = NotImplemented,
            categoryIds: str = NotImplemented,
            blackoutConflicts: List[KalturaScheduleEvent] = NotImplemented): ...
        pass

class KalturaScheduleEventBaseFilter(KalturaRelatedFilter):
    idEqual: int
    idIn: str
    idNotIn: str
    parentIdEqual: int
    parentIdIn: str
    parentIdNotIn: str
    statusEqual: KalturaScheduleEventStatus
    statusIn: str
    startDateGreaterThanOrEqual: int
    startDateLessThanOrEqual: int
    endDateGreaterThanOrEqual: int
    endDateLessThanOrEqual: int
    referenceIdEqual: str
    referenceIdIn: str
    ownerIdEqual: str
    ownerIdIn: str
    priorityEqual: int
    priorityIn: str
    priorityGreaterThanOrEqual: int
    priorityLessThanOrEqual: int
    recurrenceTypeEqual: KalturaScheduleEventRecurrenceType
    recurrenceTypeIn: str
    tagsLike: str
    tagsMultiLikeOr: str
    tagsMultiLikeAnd: str
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
            updatedAtLessThanOrEqual: int = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getIdNotIn(self) -> str: ...
    def setIdNotIn(self, newIdNotIn: str) -> None: ...
    def getParentIdEqual(self) -> int: ...
    def setParentIdEqual(self, newParentIdEqual: int) -> None: ...
    def getParentIdIn(self) -> str: ...
    def setParentIdIn(self, newParentIdIn: str) -> None: ...
    def getParentIdNotIn(self) -> str: ...
    def setParentIdNotIn(self, newParentIdNotIn: str) -> None: ...
    def getStatusEqual(self) -> KalturaScheduleEventStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaScheduleEventStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getStartDateGreaterThanOrEqual(self) -> int: ...
    def setStartDateGreaterThanOrEqual(self, newStartDateGreaterThanOrEqual: int) -> None: ...
    def getStartDateLessThanOrEqual(self) -> int: ...
    def setStartDateLessThanOrEqual(self, newStartDateLessThanOrEqual: int) -> None: ...
    def getEndDateGreaterThanOrEqual(self) -> int: ...
    def setEndDateGreaterThanOrEqual(self, newEndDateGreaterThanOrEqual: int) -> None: ...
    def getEndDateLessThanOrEqual(self) -> int: ...
    def setEndDateLessThanOrEqual(self, newEndDateLessThanOrEqual: int) -> None: ...
    def getReferenceIdEqual(self) -> str: ...
    def setReferenceIdEqual(self, newReferenceIdEqual: str) -> None: ...
    def getReferenceIdIn(self) -> str: ...
    def setReferenceIdIn(self, newReferenceIdIn: str) -> None: ...
    def getOwnerIdEqual(self) -> str: ...
    def setOwnerIdEqual(self, newOwnerIdEqual: str) -> None: ...
    def getOwnerIdIn(self) -> str: ...
    def setOwnerIdIn(self, newOwnerIdIn: str) -> None: ...
    def getPriorityEqual(self) -> int: ...
    def setPriorityEqual(self, newPriorityEqual: int) -> None: ...
    def getPriorityIn(self) -> str: ...
    def setPriorityIn(self, newPriorityIn: str) -> None: ...
    def getPriorityGreaterThanOrEqual(self) -> int: ...
    def setPriorityGreaterThanOrEqual(self, newPriorityGreaterThanOrEqual: int) -> None: ...
    def getPriorityLessThanOrEqual(self) -> int: ...
    def setPriorityLessThanOrEqual(self, newPriorityLessThanOrEqual: int) -> None: ...
    def getRecurrenceTypeEqual(self) -> KalturaScheduleEventRecurrenceType: ...
    def setRecurrenceTypeEqual(self, newRecurrenceTypeEqual: KalturaScheduleEventRecurrenceType) -> None: ...
    def getRecurrenceTypeIn(self) -> str: ...
    def setRecurrenceTypeIn(self, newRecurrenceTypeIn: str) -> None: ...
    def getTagsLike(self) -> str: ...
    def setTagsLike(self, newTagsLike: str) -> None: ...
    def getTagsMultiLikeOr(self) -> str: ...
    def setTagsMultiLikeOr(self, newTagsMultiLikeOr: str) -> None: ...
    def getTagsMultiLikeAnd(self) -> str: ...
    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...

class KalturaScheduleEventResourceBaseFilter(KalturaRelatedFilter):
    eventIdEqual: int
    eventIdIn: str
    resourceIdEqual: int
    resourceIdIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            eventIdEqual: int = NotImplemented,
            eventIdIn: str = NotImplemented,
            resourceIdEqual: int = NotImplemented,
            resourceIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...

    def getEventIdEqual(self) -> int: ...
    def setEventIdEqual(self, newEventIdEqual: int) -> None: ...
    def getEventIdIn(self) -> str: ...
    def setEventIdIn(self, newEventIdIn: str) -> None: ...
    def getResourceIdEqual(self) -> int: ...
    def setResourceIdEqual(self, newResourceIdEqual: int) -> None: ...
    def getResourceIdIn(self) -> str: ...
    def setResourceIdIn(self, newResourceIdIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...

class KalturaScheduleResourceBaseFilter(KalturaRelatedFilter):
    idEqual: int
    idIn: str
    idNotIn: str
    parentIdEqual: int
    parentIdIn: str
    nameEqual: str
    systemNameEqual: str
    systemNameIn: str
    statusEqual: KalturaScheduleResourceStatus
    statusIn: str
    tagsLike: str
    tagsMultiLikeOr: str
    tagsMultiLikeAnd: str
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
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaScheduleResourceStatus = NotImplemented,
            statusIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
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
    def getParentIdEqual(self) -> int: ...
    def setParentIdEqual(self, newParentIdEqual: int) -> None: ...
    def getParentIdIn(self) -> str: ...
    def setParentIdIn(self, newParentIdIn: str) -> None: ...
    def getNameEqual(self) -> str: ...
    def setNameEqual(self, newNameEqual: str) -> None: ...
    def getSystemNameEqual(self) -> str: ...
    def setSystemNameEqual(self, newSystemNameEqual: str) -> None: ...
    def getSystemNameIn(self) -> str: ...
    def setSystemNameIn(self, newSystemNameIn: str) -> None: ...
    def getStatusEqual(self) -> KalturaScheduleResourceStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaScheduleResourceStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getTagsLike(self) -> str: ...
    def setTagsLike(self, newTagsLike: str) -> None: ...
    def getTagsMultiLikeOr(self) -> str: ...
    def setTagsMultiLikeOr(self, newTagsMultiLikeOr: str) -> None: ...
    def getTagsMultiLikeAnd(self) -> str: ...
    def setTagsMultiLikeAnd(self, newTagsMultiLikeAnd: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...

class KalturaVodScheduleEvent(KalturaEntryScheduleEvent):
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
            templateEntryId: str = NotImplemented,
            entryIds: str = NotImplemented,
            categoryIds: str = NotImplemented,
            blackoutConflicts: List[KalturaScheduleEvent] = NotImplemented): ...
        pass

class KalturaLiveRedirectScheduleEvent(KalturaBaseLiveScheduleEvent):
    redirectEntryId: str
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
            templateEntryId: str = NotImplemented,
            entryIds: str = NotImplemented,
            categoryIds: str = NotImplemented,
            blackoutConflicts: List[KalturaScheduleEvent] = NotImplemented,
            redirectEntryId: str = NotImplemented): ...

    def getRedirectEntryId(self) -> str: ...
    def setRedirectEntryId(self, newRedirectEntryId: str) -> None: ...

class KalturaLiveStreamScheduleEvent(KalturaBaseLiveScheduleEvent):
    sourceEntryId: str
    projectedAudience: int
    preStartTime: int
    postEndTime: int
    preStartEntryId: str
    postEndEntryId: str
    isContentInterruptible: bool
    liveFeatures: List[KalturaLiveFeature]
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
            templateEntryId: str = NotImplemented,
            entryIds: str = NotImplemented,
            categoryIds: str = NotImplemented,
            blackoutConflicts: List[KalturaScheduleEvent] = NotImplemented,
            sourceEntryId: str = NotImplemented,
            projectedAudience: int = NotImplemented,
            preStartTime: int = NotImplemented,
            postEndTime: int = NotImplemented,
            preStartEntryId: str = NotImplemented,
            postEndEntryId: str = NotImplemented,
            isContentInterruptible: bool = NotImplemented,
            liveFeatures: List[KalturaLiveFeature] = NotImplemented): ...

    def getSourceEntryId(self) -> str: ...
    def setSourceEntryId(self, newSourceEntryId: str) -> None: ...
    def getProjectedAudience(self) -> int: ...
    def setProjectedAudience(self, newProjectedAudience: int) -> None: ...
    def getPreStartTime(self) -> int: ...
    def setPreStartTime(self, newPreStartTime: int) -> None: ...
    def getPostEndTime(self) -> int: ...
    def setPostEndTime(self, newPostEndTime: int) -> None: ...
    def getPreStartEntryId(self) -> str: ...
    def setPreStartEntryId(self, newPreStartEntryId: str) -> None: ...
    def getPostEndEntryId(self) -> str: ...
    def setPostEndEntryId(self, newPostEndEntryId: str) -> None: ...
    def getIsContentInterruptible(self) -> bool: ...
    def setIsContentInterruptible(self, newIsContentInterruptible: bool) -> None: ...
    def getLiveFeatures(self) -> List[KalturaLiveFeature]: ...
    def setLiveFeatures(self, newLiveFeatures: List[KalturaLiveFeature]) -> None: ...

class KalturaScheduleEventFilter(KalturaScheduleEventBaseFilter):
    resourceIdsLike: str
    resourceIdsMultiLikeOr: str
    resourceIdsMultiLikeAnd: str
    parentResourceIdsLike: str
    parentResourceIdsMultiLikeOr: str
    parentResourceIdsMultiLikeAnd: str
    templateEntryCategoriesIdsMultiLikeAnd: str
    templateEntryCategoriesIdsMultiLikeOr: str
    resourceSystemNamesMultiLikeOr: str
    templateEntryCategoriesIdsLike: str
    resourceSystemNamesMultiLikeAnd: str
    resourceSystemNamesLike: str
    resourceIdEqual: str
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

    def getResourceIdsLike(self) -> str: ...
    def setResourceIdsLike(self, newResourceIdsLike: str) -> None: ...
    def getResourceIdsMultiLikeOr(self) -> str: ...
    def setResourceIdsMultiLikeOr(self, newResourceIdsMultiLikeOr: str) -> None: ...
    def getResourceIdsMultiLikeAnd(self) -> str: ...
    def setResourceIdsMultiLikeAnd(self, newResourceIdsMultiLikeAnd: str) -> None: ...
    def getParentResourceIdsLike(self) -> str: ...
    def setParentResourceIdsLike(self, newParentResourceIdsLike: str) -> None: ...
    def getParentResourceIdsMultiLikeOr(self) -> str: ...
    def setParentResourceIdsMultiLikeOr(self, newParentResourceIdsMultiLikeOr: str) -> None: ...
    def getParentResourceIdsMultiLikeAnd(self) -> str: ...
    def setParentResourceIdsMultiLikeAnd(self, newParentResourceIdsMultiLikeAnd: str) -> None: ...
    def getTemplateEntryCategoriesIdsMultiLikeAnd(self) -> str: ...
    def setTemplateEntryCategoriesIdsMultiLikeAnd(self, newTemplateEntryCategoriesIdsMultiLikeAnd: str) -> None: ...
    def getTemplateEntryCategoriesIdsMultiLikeOr(self) -> str: ...
    def setTemplateEntryCategoriesIdsMultiLikeOr(self, newTemplateEntryCategoriesIdsMultiLikeOr: str) -> None: ...
    def getResourceSystemNamesMultiLikeOr(self) -> str: ...
    def setResourceSystemNamesMultiLikeOr(self, newResourceSystemNamesMultiLikeOr: str) -> None: ...
    def getTemplateEntryCategoriesIdsLike(self) -> str: ...
    def setTemplateEntryCategoriesIdsLike(self, newTemplateEntryCategoriesIdsLike: str) -> None: ...
    def getResourceSystemNamesMultiLikeAnd(self) -> str: ...
    def setResourceSystemNamesMultiLikeAnd(self, newResourceSystemNamesMultiLikeAnd: str) -> None: ...
    def getResourceSystemNamesLike(self) -> str: ...
    def setResourceSystemNamesLike(self, newResourceSystemNamesLike: str) -> None: ...
    def getResourceIdEqual(self) -> str: ...
    def setResourceIdEqual(self, newResourceIdEqual: str) -> None: ...

class KalturaScheduleEventResourceFilter(KalturaScheduleEventResourceBaseFilter):
    eventIdOrItsParentIdEqual: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            eventIdEqual: int = NotImplemented,
            eventIdIn: str = NotImplemented,
            resourceIdEqual: int = NotImplemented,
            resourceIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            eventIdOrItsParentIdEqual: int = NotImplemented): ...

    def getEventIdOrItsParentIdEqual(self) -> int: ...
    def setEventIdOrItsParentIdEqual(self, newEventIdOrItsParentIdEqual: int) -> None: ...

class KalturaScheduleResourceFilter(KalturaScheduleResourceBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaScheduleResourceStatus = NotImplemented,
            statusIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaCameraScheduleResourceBaseFilter(KalturaScheduleResourceFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaScheduleResourceStatus = NotImplemented,
            statusIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaEntryScheduleEventBaseFilter(KalturaScheduleEventFilter):
    templateEntryIdEqual: str
    entryIdsLike: str
    entryIdsMultiLikeOr: str
    entryIdsMultiLikeAnd: str
    categoryIdsLike: str
    categoryIdsMultiLikeOr: str
    categoryIdsMultiLikeAnd: str
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented): ...

    def getTemplateEntryIdEqual(self) -> str: ...
    def setTemplateEntryIdEqual(self, newTemplateEntryIdEqual: str) -> None: ...
    def getEntryIdsLike(self) -> str: ...
    def setEntryIdsLike(self, newEntryIdsLike: str) -> None: ...
    def getEntryIdsMultiLikeOr(self) -> str: ...
    def setEntryIdsMultiLikeOr(self, newEntryIdsMultiLikeOr: str) -> None: ...
    def getEntryIdsMultiLikeAnd(self) -> str: ...
    def setEntryIdsMultiLikeAnd(self, newEntryIdsMultiLikeAnd: str) -> None: ...
    def getCategoryIdsLike(self) -> str: ...
    def setCategoryIdsLike(self, newCategoryIdsLike: str) -> None: ...
    def getCategoryIdsMultiLikeOr(self) -> str: ...
    def setCategoryIdsMultiLikeOr(self, newCategoryIdsMultiLikeOr: str) -> None: ...
    def getCategoryIdsMultiLikeAnd(self) -> str: ...
    def setCategoryIdsMultiLikeAnd(self, newCategoryIdsMultiLikeAnd: str) -> None: ...

class KalturaLiveEntryScheduleResourceBaseFilter(KalturaScheduleResourceFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaScheduleResourceStatus = NotImplemented,
            statusIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaLocationScheduleResourceBaseFilter(KalturaScheduleResourceFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaScheduleResourceStatus = NotImplemented,
            statusIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaCameraScheduleResourceFilter(KalturaCameraScheduleResourceBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaScheduleResourceStatus = NotImplemented,
            statusIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaEntryScheduleEventFilter(KalturaEntryScheduleEventBaseFilter):
    parentCategoryIdsLike: str
    parentCategoryIdsMultiLikeOr: str
    parentCategoryIdsMultiLikeAnd: str
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...

    def getParentCategoryIdsLike(self) -> str: ...
    def setParentCategoryIdsLike(self, newParentCategoryIdsLike: str) -> None: ...
    def getParentCategoryIdsMultiLikeOr(self) -> str: ...
    def setParentCategoryIdsMultiLikeOr(self, newParentCategoryIdsMultiLikeOr: str) -> None: ...
    def getParentCategoryIdsMultiLikeAnd(self) -> str: ...
    def setParentCategoryIdsMultiLikeAnd(self, newParentCategoryIdsMultiLikeAnd: str) -> None: ...

class KalturaLiveEntryScheduleResourceFilter(KalturaLiveEntryScheduleResourceBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaScheduleResourceStatus = NotImplemented,
            statusIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaLocationScheduleResourceFilter(KalturaLocationScheduleResourceBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            parentIdEqual: int = NotImplemented,
            parentIdIn: str = NotImplemented,
            nameEqual: str = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            statusEqual: KalturaScheduleResourceStatus = NotImplemented,
            statusIn: str = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented): ...
        pass

class KalturaLiveRedirectScheduleEventFilter(KalturaEntryScheduleEventFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaLiveStreamScheduleEventBaseFilter(KalturaEntryScheduleEventFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaMeetingScheduleEventBaseFilter(KalturaEntryScheduleEventFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaRecordScheduleEventBaseFilter(KalturaEntryScheduleEventFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaVodScheduleEventBaseFilter(KalturaEntryScheduleEventFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaBlackoutScheduleEventFilter(KalturaRecordScheduleEventBaseFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaLiveStreamScheduleEventFilter(KalturaLiveStreamScheduleEventBaseFilter):
    sourceEntryIdEqual: str
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented,
            sourceEntryIdEqual: str = NotImplemented): ...

    def getSourceEntryIdEqual(self) -> str: ...
    def setSourceEntryIdEqual(self, newSourceEntryIdEqual: str) -> None: ...

class KalturaMeetingScheduleEventFilter(KalturaMeetingScheduleEventBaseFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaRecordScheduleEventFilter(KalturaRecordScheduleEventBaseFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaVodScheduleEventFilter(KalturaVodScheduleEventBaseFilter):
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
            resourceIdEqual: str = NotImplemented,
            templateEntryIdEqual: str = NotImplemented,
            entryIdsLike: str = NotImplemented,
            entryIdsMultiLikeOr: str = NotImplemented,
            entryIdsMultiLikeAnd: str = NotImplemented,
            categoryIdsLike: str = NotImplemented,
            categoryIdsMultiLikeOr: str = NotImplemented,
            categoryIdsMultiLikeAnd: str = NotImplemented,
            parentCategoryIdsLike: str = NotImplemented,
            parentCategoryIdsMultiLikeOr: str = NotImplemented,
            parentCategoryIdsMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaScheduleEventService(KalturaServiceBase):
    def add(self, scheduleEvent: KalturaScheduleEvent) -> KalturaScheduleEvent: ...
    def addFromBulkUpload(self, fileData: IO[Any], bulkUploadData: KalturaBulkUploadScheduleEventJobData = NotImplemented) -> KalturaBulkUpload: ...
    def cancel(self, scheduleEventId: int) -> KalturaScheduleEvent: ...
    def delete(self, scheduleEventId: int) -> KalturaScheduleEvent: ...
    def get(self, scheduleEventId: int) -> KalturaScheduleEvent: ...
    def getConflicts(self, resourceIds: str, scheduleEvent: KalturaScheduleEvent, scheduleEventIdToIgnore: str = NotImplemented, scheduleEventConflictType: int = 1) -> KalturaScheduleEventListResponse: ...
    def list(self, filter: KalturaScheduleEventFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaScheduleEventListResponse: ...
    def update(self, scheduleEventId: int, scheduleEvent: KalturaScheduleEvent) -> KalturaScheduleEvent: ...
    def updateLiveFeature(self, scheduledEventId: int, featureName: str, liveFeature: KalturaLiveFeature) -> KalturaLiveStreamScheduleEvent: ...

class KalturaScheduleResourceService(KalturaServiceBase):
    def add(self, scheduleResource: KalturaScheduleResource) -> KalturaScheduleResource: ...
    def addFromBulkUpload(self, fileData: IO[Any], bulkUploadData: KalturaBulkUploadCsvJobData = NotImplemented) -> KalturaBulkUpload: ...
    def delete(self, scheduleResourceId: int) -> KalturaScheduleResource: ...
    def get(self, scheduleResourceId: int) -> KalturaScheduleResource: ...
    def list(self, filter: KalturaScheduleResourceFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaScheduleResourceListResponse: ...
    def update(self, scheduleResourceId: int, scheduleResource: KalturaScheduleResource) -> KalturaScheduleResource: ...

class KalturaScheduleEventResourceService(KalturaServiceBase):
    def add(self, scheduleEventResource: KalturaScheduleEventResource) -> KalturaScheduleEventResource: ...
    def delete(self, scheduleEventId: int, scheduleResourceId: int) -> None: ...
    def get(self, scheduleEventId: int, scheduleResourceId: int) -> KalturaScheduleEventResource: ...
    def list(self, filter: KalturaScheduleEventResourceFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented, filterBlackoutConflicts: bool = True) -> KalturaScheduleEventResourceListResponse: ...
    def update(self, scheduleEventId: int, scheduleResourceId: int, scheduleEventResource: KalturaScheduleEventResource) -> KalturaScheduleEventResource: ...

class KalturaScheduleClientPluginServicesProxy:
    scheduleEvent: KalturaScheduleEventService
    scheduleResource: KalturaScheduleResourceService
    scheduleEventResource: KalturaScheduleEventResourceService