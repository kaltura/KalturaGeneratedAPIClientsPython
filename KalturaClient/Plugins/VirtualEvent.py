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
# @package Kaltura
# @subpackage Client
class KalturaVirtualEventStatus(object):
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVirtualScheduleEventSubType(object):
    AGENDA = 1
    REGISTRATION = 2
    MAIN_EVENT = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVirtualEventOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaVirtualEvent(KalturaObjectBase):
    def __init__(self,
            id = NotImplemented,
            partnerId = NotImplemented,
            name = NotImplemented,
            description = NotImplemented,
            status = NotImplemented,
            tags = NotImplemented,
            attendeesGroupIds = NotImplemented,
            adminsGroupIds = NotImplemented,
            registrationScheduleEventId = NotImplemented,
            agendaScheduleEventId = NotImplemented,
            mainEventScheduleEventId = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            deletionDueDate = NotImplemented,
            registrationFormSchema = NotImplemented,
            eventUrl = NotImplemented,
            webhookRegistrationToken = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var str
        self.name = name

        # @var str
        self.description = description

        # @var KalturaVirtualEventStatus
        # @readonly
        self.status = status

        # @var str
        self.tags = tags

        # @var str
        self.attendeesGroupIds = attendeesGroupIds

        # @var str
        self.adminsGroupIds = adminsGroupIds

        # @var int
        self.registrationScheduleEventId = registrationScheduleEventId

        # @var int
        self.agendaScheduleEventId = agendaScheduleEventId

        # @var int
        self.mainEventScheduleEventId = mainEventScheduleEventId

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var int
        self.deletionDueDate = deletionDueDate

        # JSON-Schema of the Registration Form
        # @var str
        self.registrationFormSchema = registrationFormSchema

        # The Virtual Event Url
        # @var str
        self.eventUrl = eventUrl

        # The Virtual Event WebHook registration token
        # @var str
        self.webhookRegistrationToken = webhookRegistrationToken


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaVirtualEventStatus"), 
        'tags': getXmlNodeText, 
        'attendeesGroupIds': getXmlNodeText, 
        'adminsGroupIds': getXmlNodeText, 
        'registrationScheduleEventId': getXmlNodeInt, 
        'agendaScheduleEventId': getXmlNodeInt, 
        'mainEventScheduleEventId': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'deletionDueDate': getXmlNodeInt, 
        'registrationFormSchema': getXmlNodeText, 
        'eventUrl': getXmlNodeText, 
        'webhookRegistrationToken': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirtualEvent.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVirtualEvent")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("tags", self.tags)
        kparams.addStringIfDefined("attendeesGroupIds", self.attendeesGroupIds)
        kparams.addStringIfDefined("adminsGroupIds", self.adminsGroupIds)
        kparams.addIntIfDefined("registrationScheduleEventId", self.registrationScheduleEventId)
        kparams.addIntIfDefined("agendaScheduleEventId", self.agendaScheduleEventId)
        kparams.addIntIfDefined("mainEventScheduleEventId", self.mainEventScheduleEventId)
        kparams.addIntIfDefined("deletionDueDate", self.deletionDueDate)
        kparams.addStringIfDefined("registrationFormSchema", self.registrationFormSchema)
        kparams.addStringIfDefined("eventUrl", self.eventUrl)
        kparams.addStringIfDefined("webhookRegistrationToken", self.webhookRegistrationToken)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getStatus(self):
        return self.status

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getAttendeesGroupIds(self):
        return self.attendeesGroupIds

    def setAttendeesGroupIds(self, newAttendeesGroupIds):
        self.attendeesGroupIds = newAttendeesGroupIds

    def getAdminsGroupIds(self):
        return self.adminsGroupIds

    def setAdminsGroupIds(self, newAdminsGroupIds):
        self.adminsGroupIds = newAdminsGroupIds

    def getRegistrationScheduleEventId(self):
        return self.registrationScheduleEventId

    def setRegistrationScheduleEventId(self, newRegistrationScheduleEventId):
        self.registrationScheduleEventId = newRegistrationScheduleEventId

    def getAgendaScheduleEventId(self):
        return self.agendaScheduleEventId

    def setAgendaScheduleEventId(self, newAgendaScheduleEventId):
        self.agendaScheduleEventId = newAgendaScheduleEventId

    def getMainEventScheduleEventId(self):
        return self.mainEventScheduleEventId

    def setMainEventScheduleEventId(self, newMainEventScheduleEventId):
        self.mainEventScheduleEventId = newMainEventScheduleEventId

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getDeletionDueDate(self):
        return self.deletionDueDate

    def setDeletionDueDate(self, newDeletionDueDate):
        self.deletionDueDate = newDeletionDueDate

    def getRegistrationFormSchema(self):
        return self.registrationFormSchema

    def setRegistrationFormSchema(self, newRegistrationFormSchema):
        self.registrationFormSchema = newRegistrationFormSchema

    def getEventUrl(self):
        return self.eventUrl

    def setEventUrl(self, newEventUrl):
        self.eventUrl = newEventUrl

    def getWebhookRegistrationToken(self):
        return self.webhookRegistrationToken

    def setWebhookRegistrationToken(self, newWebhookRegistrationToken):
        self.webhookRegistrationToken = newWebhookRegistrationToken


# @package Kaltura
# @subpackage Client
class KalturaVirtualEventBaseFilter(KalturaFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var str
        self.idIn = idIn

        # @var str
        self.idNotIn = idNotIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var str
        self.partnerIdIn = partnerIdIn

        # @var KalturaVirtualEventStatus
        self.statusEqual = statusEqual

        # @var str
        self.statusIn = statusIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'idNotIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaVirtualEventStatus"), 
        'statusIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirtualEventBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaVirtualEventBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("idNotIn", self.idNotIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getIdNotIn(self):
        return self.idNotIn

    def setIdNotIn(self, newIdNotIn):
        self.idNotIn = newIdNotIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaVirtualEventListResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaVirtualEvent]
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaVirtualEvent'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirtualEventListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaVirtualEventListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaVirtualScheduleEvent(KalturaScheduleEvent):
    def __init__(self,
            id = NotImplemented,
            partnerId = NotImplemented,
            parentId = NotImplemented,
            summary = NotImplemented,
            description = NotImplemented,
            status = NotImplemented,
            startDate = NotImplemented,
            endDate = NotImplemented,
            referenceId = NotImplemented,
            linkedTo = NotImplemented,
            linkedBy = NotImplemented,
            classificationType = NotImplemented,
            geoLatitude = NotImplemented,
            geoLongitude = NotImplemented,
            location = NotImplemented,
            organizer = NotImplemented,
            ownerId = NotImplemented,
            priority = NotImplemented,
            sequence = NotImplemented,
            recurrenceType = NotImplemented,
            duration = NotImplemented,
            contact = NotImplemented,
            comment = NotImplemented,
            tags = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            recurrence = NotImplemented,
            virtualEventId = NotImplemented,
            virtualScheduleEventSubType = NotImplemented):
        KalturaScheduleEvent.__init__(self,
            id,
            partnerId,
            parentId,
            summary,
            description,
            status,
            startDate,
            endDate,
            referenceId,
            linkedTo,
            linkedBy,
            classificationType,
            geoLatitude,
            geoLongitude,
            location,
            organizer,
            ownerId,
            priority,
            sequence,
            recurrenceType,
            duration,
            contact,
            comment,
            tags,
            createdAt,
            updatedAt,
            recurrence)

        # The ID of the virtual event connected to this Schedule Event
        # @var int
        self.virtualEventId = virtualEventId

        # The type of the Virtual Schedule Event
        # @var KalturaVirtualScheduleEventSubType
        # @insertonly
        self.virtualScheduleEventSubType = virtualScheduleEventSubType


    PROPERTY_LOADERS = {
        'virtualEventId': getXmlNodeInt, 
        'virtualScheduleEventSubType': (KalturaEnumsFactory.createInt, "KalturaVirtualScheduleEventSubType"), 
    }

    def fromXml(self, node):
        KalturaScheduleEvent.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirtualScheduleEvent.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaScheduleEvent.toParams(self)
        kparams.put("objectType", "KalturaVirtualScheduleEvent")
        kparams.addIntIfDefined("virtualEventId", self.virtualEventId)
        kparams.addIntEnumIfDefined("virtualScheduleEventSubType", self.virtualScheduleEventSubType)
        return kparams

    def getVirtualEventId(self):
        return self.virtualEventId

    def setVirtualEventId(self, newVirtualEventId):
        self.virtualEventId = newVirtualEventId

    def getVirtualScheduleEventSubType(self):
        return self.virtualScheduleEventSubType

    def setVirtualScheduleEventSubType(self, newVirtualScheduleEventSubType):
        self.virtualScheduleEventSubType = newVirtualScheduleEventSubType


# @package Kaltura
# @subpackage Client
class KalturaVirtualEventFilter(KalturaVirtualEventBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented):
        KalturaVirtualEventBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            partnerIdEqual,
            partnerIdIn,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVirtualEventBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirtualEventFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVirtualEventBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVirtualEventFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVirtualScheduleEventBaseFilter(KalturaScheduleEventFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            parentIdEqual = NotImplemented,
            parentIdIn = NotImplemented,
            parentIdNotIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            startDateGreaterThanOrEqual = NotImplemented,
            startDateLessThanOrEqual = NotImplemented,
            endDateGreaterThanOrEqual = NotImplemented,
            endDateLessThanOrEqual = NotImplemented,
            referenceIdEqual = NotImplemented,
            referenceIdIn = NotImplemented,
            ownerIdEqual = NotImplemented,
            ownerIdIn = NotImplemented,
            priorityEqual = NotImplemented,
            priorityIn = NotImplemented,
            priorityGreaterThanOrEqual = NotImplemented,
            priorityLessThanOrEqual = NotImplemented,
            recurrenceTypeEqual = NotImplemented,
            recurrenceTypeIn = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            resourceIdsLike = NotImplemented,
            resourceIdsMultiLikeOr = NotImplemented,
            resourceIdsMultiLikeAnd = NotImplemented,
            parentResourceIdsLike = NotImplemented,
            parentResourceIdsMultiLikeOr = NotImplemented,
            parentResourceIdsMultiLikeAnd = NotImplemented,
            templateEntryCategoriesIdsMultiLikeAnd = NotImplemented,
            templateEntryCategoriesIdsMultiLikeOr = NotImplemented,
            resourceSystemNamesMultiLikeOr = NotImplemented,
            templateEntryCategoriesIdsLike = NotImplemented,
            resourceSystemNamesMultiLikeAnd = NotImplemented,
            resourceSystemNamesLike = NotImplemented,
            resourceIdEqual = NotImplemented):
        KalturaScheduleEventFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            parentIdEqual,
            parentIdIn,
            parentIdNotIn,
            statusEqual,
            statusIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            referenceIdEqual,
            referenceIdIn,
            ownerIdEqual,
            ownerIdIn,
            priorityEqual,
            priorityIn,
            priorityGreaterThanOrEqual,
            priorityLessThanOrEqual,
            recurrenceTypeEqual,
            recurrenceTypeIn,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            resourceIdsLike,
            resourceIdsMultiLikeOr,
            resourceIdsMultiLikeAnd,
            parentResourceIdsLike,
            parentResourceIdsMultiLikeOr,
            parentResourceIdsMultiLikeAnd,
            templateEntryCategoriesIdsMultiLikeAnd,
            templateEntryCategoriesIdsMultiLikeOr,
            resourceSystemNamesMultiLikeOr,
            templateEntryCategoriesIdsLike,
            resourceSystemNamesMultiLikeAnd,
            resourceSystemNamesLike,
            resourceIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaScheduleEventFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirtualScheduleEventBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaScheduleEventFilter.toParams(self)
        kparams.put("objectType", "KalturaVirtualScheduleEventBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVirtualScheduleEventFilter(KalturaVirtualScheduleEventBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            parentIdEqual = NotImplemented,
            parentIdIn = NotImplemented,
            parentIdNotIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            startDateGreaterThanOrEqual = NotImplemented,
            startDateLessThanOrEqual = NotImplemented,
            endDateGreaterThanOrEqual = NotImplemented,
            endDateLessThanOrEqual = NotImplemented,
            referenceIdEqual = NotImplemented,
            referenceIdIn = NotImplemented,
            ownerIdEqual = NotImplemented,
            ownerIdIn = NotImplemented,
            priorityEqual = NotImplemented,
            priorityIn = NotImplemented,
            priorityGreaterThanOrEqual = NotImplemented,
            priorityLessThanOrEqual = NotImplemented,
            recurrenceTypeEqual = NotImplemented,
            recurrenceTypeIn = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            resourceIdsLike = NotImplemented,
            resourceIdsMultiLikeOr = NotImplemented,
            resourceIdsMultiLikeAnd = NotImplemented,
            parentResourceIdsLike = NotImplemented,
            parentResourceIdsMultiLikeOr = NotImplemented,
            parentResourceIdsMultiLikeAnd = NotImplemented,
            templateEntryCategoriesIdsMultiLikeAnd = NotImplemented,
            templateEntryCategoriesIdsMultiLikeOr = NotImplemented,
            resourceSystemNamesMultiLikeOr = NotImplemented,
            templateEntryCategoriesIdsLike = NotImplemented,
            resourceSystemNamesMultiLikeAnd = NotImplemented,
            resourceSystemNamesLike = NotImplemented,
            resourceIdEqual = NotImplemented):
        KalturaVirtualScheduleEventBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            parentIdEqual,
            parentIdIn,
            parentIdNotIn,
            statusEqual,
            statusIn,
            startDateGreaterThanOrEqual,
            startDateLessThanOrEqual,
            endDateGreaterThanOrEqual,
            endDateLessThanOrEqual,
            referenceIdEqual,
            referenceIdIn,
            ownerIdEqual,
            ownerIdIn,
            priorityEqual,
            priorityIn,
            priorityGreaterThanOrEqual,
            priorityLessThanOrEqual,
            recurrenceTypeEqual,
            recurrenceTypeIn,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            resourceIdsLike,
            resourceIdsMultiLikeOr,
            resourceIdsMultiLikeAnd,
            parentResourceIdsLike,
            parentResourceIdsMultiLikeOr,
            parentResourceIdsMultiLikeAnd,
            templateEntryCategoriesIdsMultiLikeAnd,
            templateEntryCategoriesIdsMultiLikeOr,
            resourceSystemNamesMultiLikeOr,
            templateEntryCategoriesIdsLike,
            resourceSystemNamesMultiLikeAnd,
            resourceSystemNamesLike,
            resourceIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVirtualScheduleEventBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVirtualScheduleEventFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVirtualScheduleEventBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVirtualScheduleEventFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaVirtualEventService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, virtualEvent):
        """Add a new virtual event"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("virtualEvent", virtualEvent)
        self.client.queueServiceActionCall("virtualevent_virtualevent", "add", "KalturaVirtualEvent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVirtualEvent')

    def delete(self, id):
        """Delete a virtual event"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("virtualevent_virtualevent", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, id):
        """Retrieve a virtual event by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("virtualevent_virtualevent", "get", "KalturaVirtualEvent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVirtualEvent')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List virtual events"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("virtualevent_virtualevent", "list", "KalturaVirtualEventListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVirtualEventListResponse')

    def update(self, id, virtualEvent):
        """Update an existing virtual event"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("virtualEvent", virtualEvent)
        self.client.queueServiceActionCall("virtualevent_virtualevent", "update", "KalturaVirtualEvent", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVirtualEvent')

########## main ##########
class KalturaVirtualEventClientPlugin(KalturaClientPlugin):
    # KalturaVirtualEventClientPlugin
    instance = None

    # @return KalturaVirtualEventClientPlugin
    @staticmethod
    def get():
        if KalturaVirtualEventClientPlugin.instance == None:
            KalturaVirtualEventClientPlugin.instance = KalturaVirtualEventClientPlugin()
        return KalturaVirtualEventClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'virtualEvent': KalturaVirtualEventService,
        }

    def getEnums(self):
        return {
            'KalturaVirtualEventStatus': KalturaVirtualEventStatus,
            'KalturaVirtualScheduleEventSubType': KalturaVirtualScheduleEventSubType,
            'KalturaVirtualEventOrderBy': KalturaVirtualEventOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaVirtualEvent': KalturaVirtualEvent,
            'KalturaVirtualEventBaseFilter': KalturaVirtualEventBaseFilter,
            'KalturaVirtualEventListResponse': KalturaVirtualEventListResponse,
            'KalturaVirtualScheduleEvent': KalturaVirtualScheduleEvent,
            'KalturaVirtualEventFilter': KalturaVirtualEventFilter,
            'KalturaVirtualScheduleEventBaseFilter': KalturaVirtualScheduleEventBaseFilter,
            'KalturaVirtualScheduleEventFilter': KalturaVirtualScheduleEventFilter,
        }

    # @return string
    def getName(self):
        return 'virtualEvent'

