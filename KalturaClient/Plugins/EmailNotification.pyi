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

class KalturaEmailNotificationTemplatePriority(object):
    HIGH = 1
    NORMAL = 3
    LOW = 5

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaEmailNotificationFormat(object):
    HTML = "1"
    TEXT = "2"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEmailNotificationRecipientProviderType(object):
    STATIC_LIST = "1"
    CATEGORY = "2"
    USER = "3"
    GROUP = "4"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEmailNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaEmailNotificationRecipient(KalturaObjectBase):
    email: KalturaStringValue
    name: KalturaStringValue
    def __init__(self,
            email: KalturaStringValue = NotImplemented,
            name: KalturaStringValue = NotImplemented): ...

    def getEmail(self) -> KalturaStringValue: ...
    def setEmail(self, newEmail: KalturaStringValue) -> None: ...
    def getName(self) -> KalturaStringValue: ...
    def setName(self, newName: KalturaStringValue) -> None: ...

class KalturaEmailNotificationRecipientJobData(KalturaObjectBase):
    providerType: KalturaEmailNotificationRecipientProviderType
    def __init__(self,
            providerType: KalturaEmailNotificationRecipientProviderType = NotImplemented): ...

    def getProviderType(self) -> KalturaEmailNotificationRecipientProviderType: ...

class KalturaEmailNotificationRecipientProvider(KalturaObjectBase):
    def __init__(self): ...
        pass

class KalturaCategoryUserProviderFilter(KalturaFilter):
    userIdEqual: str
    userIdIn: str
    statusEqual: KalturaCategoryUserStatus
    statusIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    updateMethodEqual: KalturaUpdateMethodType
    updateMethodIn: str
    permissionNamesMatchAnd: str
    permissionNamesMatchOr: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            statusEqual: KalturaCategoryUserStatus = NotImplemented,
            statusIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            updateMethodEqual: KalturaUpdateMethodType = NotImplemented,
            updateMethodIn: str = NotImplemented,
            permissionNamesMatchAnd: str = NotImplemented,
            permissionNamesMatchOr: str = NotImplemented): ...

    def getUserIdEqual(self) -> str: ...
    def setUserIdEqual(self, newUserIdEqual: str) -> None: ...
    def getUserIdIn(self) -> str: ...
    def setUserIdIn(self, newUserIdIn: str) -> None: ...
    def getStatusEqual(self) -> KalturaCategoryUserStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaCategoryUserStatus) -> None: ...
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
    def getUpdateMethodEqual(self) -> KalturaUpdateMethodType: ...
    def setUpdateMethodEqual(self, newUpdateMethodEqual: KalturaUpdateMethodType) -> None: ...
    def getUpdateMethodIn(self) -> str: ...
    def setUpdateMethodIn(self, newUpdateMethodIn: str) -> None: ...
    def getPermissionNamesMatchAnd(self) -> str: ...
    def setPermissionNamesMatchAnd(self, newPermissionNamesMatchAnd: str) -> None: ...
    def getPermissionNamesMatchOr(self) -> str: ...
    def setPermissionNamesMatchOr(self, newPermissionNamesMatchOr: str) -> None: ...

class KalturaEmailNotificationCategoryRecipientJobData(KalturaEmailNotificationRecipientJobData):
    categoryUserFilter: KalturaCategoryUserFilter
    def __init__(self,
            providerType: KalturaEmailNotificationRecipientProviderType = NotImplemented,
            categoryUserFilter: KalturaCategoryUserFilter = NotImplemented): ...

    def getCategoryUserFilter(self) -> KalturaCategoryUserFilter: ...
    def setCategoryUserFilter(self, newCategoryUserFilter: KalturaCategoryUserFilter) -> None: ...

class KalturaEmailNotificationCategoryRecipientProvider(KalturaEmailNotificationRecipientProvider):
    categoryId: KalturaStringValue
    categoryIds: KalturaStringValue
    categoryUserFilter: KalturaCategoryUserProviderFilter
    def __init__(self,
            categoryId: KalturaStringValue = NotImplemented,
            categoryIds: KalturaStringValue = NotImplemented,
            categoryUserFilter: KalturaCategoryUserProviderFilter = NotImplemented): ...

    def getCategoryId(self) -> KalturaStringValue: ...
    def setCategoryId(self, newCategoryId: KalturaStringValue) -> None: ...
    def getCategoryIds(self) -> KalturaStringValue: ...
    def setCategoryIds(self, newCategoryIds: KalturaStringValue) -> None: ...
    def getCategoryUserFilter(self) -> KalturaCategoryUserProviderFilter: ...
    def setCategoryUserFilter(self, newCategoryUserFilter: KalturaCategoryUserProviderFilter) -> None: ...

class KalturaEmailNotificationGroupRecipientJobData(KalturaEmailNotificationRecipientJobData):
    groupId: str
    def __init__(self,
            providerType: KalturaEmailNotificationRecipientProviderType = NotImplemented,
            groupId: str = NotImplemented): ...

    def getGroupId(self) -> str: ...
    def setGroupId(self, newGroupId: str) -> None: ...

class KalturaEmailNotificationGroupRecipientProvider(KalturaEmailNotificationRecipientProvider):
    groupId: str
    def __init__(self,
            groupId: str = NotImplemented): ...

    def getGroupId(self) -> str: ...
    def setGroupId(self, newGroupId: str) -> None: ...

class KalturaEmailNotificationParameter(KalturaEventNotificationParameter):
    def __init__(self,
            key: str = NotImplemented,
            description: str = NotImplemented,
            value: KalturaStringValue = NotImplemented): ...
        pass

class KalturaEmailNotificationStaticRecipientJobData(KalturaEmailNotificationRecipientJobData):
    emailRecipients: List[KalturaKeyValue]
    def __init__(self,
            providerType: KalturaEmailNotificationRecipientProviderType = NotImplemented,
            emailRecipients: List[KalturaKeyValue] = NotImplemented): ...

    def getEmailRecipients(self) -> List[KalturaKeyValue]: ...
    def setEmailRecipients(self, newEmailRecipients: List[KalturaKeyValue]) -> None: ...

class KalturaEmailNotificationStaticRecipientProvider(KalturaEmailNotificationRecipientProvider):
    emailRecipients: List[KalturaEmailNotificationRecipient]
    def __init__(self,
            emailRecipients: List[KalturaEmailNotificationRecipient] = NotImplemented): ...

    def getEmailRecipients(self) -> List[KalturaEmailNotificationRecipient]: ...
    def setEmailRecipients(self, newEmailRecipients: List[KalturaEmailNotificationRecipient]) -> None: ...

class KalturaEmailNotificationTemplate(KalturaEventNotificationTemplate):
    format: KalturaEmailNotificationFormat
    subject: str
    body: str
    fromEmail: str
    fromName: str
    to: KalturaEmailNotificationRecipientProvider
    cc: KalturaEmailNotificationRecipientProvider
    bcc: KalturaEmailNotificationRecipientProvider
    replyTo: KalturaEmailNotificationRecipientProvider
    priority: KalturaEmailNotificationTemplatePriority
    confirmReadingTo: str
    hostname: str
    messageID: str
    customHeaders: List[KalturaKeyValue]
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
            format: KalturaEmailNotificationFormat = NotImplemented,
            subject: str = NotImplemented,
            body: str = NotImplemented,
            fromEmail: str = NotImplemented,
            fromName: str = NotImplemented,
            to: KalturaEmailNotificationRecipientProvider = NotImplemented,
            cc: KalturaEmailNotificationRecipientProvider = NotImplemented,
            bcc: KalturaEmailNotificationRecipientProvider = NotImplemented,
            replyTo: KalturaEmailNotificationRecipientProvider = NotImplemented,
            priority: KalturaEmailNotificationTemplatePriority = NotImplemented,
            confirmReadingTo: str = NotImplemented,
            hostname: str = NotImplemented,
            messageID: str = NotImplemented,
            customHeaders: List[KalturaKeyValue] = NotImplemented): ...

    def getFormat(self) -> KalturaEmailNotificationFormat: ...
    def setFormat(self, newFormat: KalturaEmailNotificationFormat) -> None: ...
    def getSubject(self) -> str: ...
    def setSubject(self, newSubject: str) -> None: ...
    def getBody(self) -> str: ...
    def setBody(self, newBody: str) -> None: ...
    def getFromEmail(self) -> str: ...
    def setFromEmail(self, newFromEmail: str) -> None: ...
    def getFromName(self) -> str: ...
    def setFromName(self, newFromName: str) -> None: ...
    def getTo(self) -> KalturaEmailNotificationRecipientProvider: ...
    def setTo(self, newTo: KalturaEmailNotificationRecipientProvider) -> None: ...
    def getCc(self) -> KalturaEmailNotificationRecipientProvider: ...
    def setCc(self, newCc: KalturaEmailNotificationRecipientProvider) -> None: ...
    def getBcc(self) -> KalturaEmailNotificationRecipientProvider: ...
    def setBcc(self, newBcc: KalturaEmailNotificationRecipientProvider) -> None: ...
    def getReplyTo(self) -> KalturaEmailNotificationRecipientProvider: ...
    def setReplyTo(self, newReplyTo: KalturaEmailNotificationRecipientProvider) -> None: ...
    def getPriority(self) -> KalturaEmailNotificationTemplatePriority: ...
    def setPriority(self, newPriority: KalturaEmailNotificationTemplatePriority) -> None: ...
    def getConfirmReadingTo(self) -> str: ...
    def setConfirmReadingTo(self, newConfirmReadingTo: str) -> None: ...
    def getHostname(self) -> str: ...
    def setHostname(self, newHostname: str) -> None: ...
    def getMessageID(self) -> str: ...
    def setMessageID(self, newMessageID: str) -> None: ...
    def getCustomHeaders(self) -> List[KalturaKeyValue]: ...
    def setCustomHeaders(self, newCustomHeaders: List[KalturaKeyValue]) -> None: ...

class KalturaEmailNotificationUserRecipientJobData(KalturaEmailNotificationRecipientJobData):
    filter: KalturaUserFilter
    def __init__(self,
            providerType: KalturaEmailNotificationRecipientProviderType = NotImplemented,
            filter: KalturaUserFilter = NotImplemented): ...

    def getFilter(self) -> KalturaUserFilter: ...
    def setFilter(self, newFilter: KalturaUserFilter) -> None: ...

class KalturaEmailNotificationUserRecipientProvider(KalturaEmailNotificationRecipientProvider):
    filter: KalturaUserFilter
    def __init__(self,
            filter: KalturaUserFilter = NotImplemented): ...

    def getFilter(self) -> KalturaUserFilter: ...
    def setFilter(self, newFilter: KalturaUserFilter) -> None: ...

class KalturaEmailNotificationDispatchJobData(KalturaEventNotificationDispatchJobData):
    fromEmail: str
    fromName: str
    to: KalturaEmailNotificationRecipientJobData
    cc: KalturaEmailNotificationRecipientJobData
    bcc: KalturaEmailNotificationRecipientJobData
    replyTo: KalturaEmailNotificationRecipientJobData
    priority: KalturaEmailNotificationTemplatePriority
    confirmReadingTo: str
    hostname: str
    messageID: str
    customHeaders: List[KalturaKeyValue]
    def __init__(self,
            templateId: int = NotImplemented,
            contentParameters: List[KalturaKeyValue] = NotImplemented,
            fromEmail: str = NotImplemented,
            fromName: str = NotImplemented,
            to: KalturaEmailNotificationRecipientJobData = NotImplemented,
            cc: KalturaEmailNotificationRecipientJobData = NotImplemented,
            bcc: KalturaEmailNotificationRecipientJobData = NotImplemented,
            replyTo: KalturaEmailNotificationRecipientJobData = NotImplemented,
            priority: KalturaEmailNotificationTemplatePriority = NotImplemented,
            confirmReadingTo: str = NotImplemented,
            hostname: str = NotImplemented,
            messageID: str = NotImplemented,
            customHeaders: List[KalturaKeyValue] = NotImplemented): ...

    def getFromEmail(self) -> str: ...
    def setFromEmail(self, newFromEmail: str) -> None: ...
    def getFromName(self) -> str: ...
    def setFromName(self, newFromName: str) -> None: ...
    def getTo(self) -> KalturaEmailNotificationRecipientJobData: ...
    def setTo(self, newTo: KalturaEmailNotificationRecipientJobData) -> None: ...
    def getCc(self) -> KalturaEmailNotificationRecipientJobData: ...
    def setCc(self, newCc: KalturaEmailNotificationRecipientJobData) -> None: ...
    def getBcc(self) -> KalturaEmailNotificationRecipientJobData: ...
    def setBcc(self, newBcc: KalturaEmailNotificationRecipientJobData) -> None: ...
    def getReplyTo(self) -> KalturaEmailNotificationRecipientJobData: ...
    def setReplyTo(self, newReplyTo: KalturaEmailNotificationRecipientJobData) -> None: ...
    def getPriority(self) -> KalturaEmailNotificationTemplatePriority: ...
    def setPriority(self, newPriority: KalturaEmailNotificationTemplatePriority) -> None: ...
    def getConfirmReadingTo(self) -> str: ...
    def setConfirmReadingTo(self, newConfirmReadingTo: str) -> None: ...
    def getHostname(self) -> str: ...
    def setHostname(self, newHostname: str) -> None: ...
    def getMessageID(self) -> str: ...
    def setMessageID(self, newMessageID: str) -> None: ...
    def getCustomHeaders(self) -> List[KalturaKeyValue]: ...
    def setCustomHeaders(self, newCustomHeaders: List[KalturaKeyValue]) -> None: ...

class KalturaEmailNotificationTemplateBaseFilter(KalturaEventNotificationTemplateFilter):
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

class KalturaEmailNotificationTemplateFilter(KalturaEmailNotificationTemplateBaseFilter):
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

class KalturaEmailNotificationClientPluginServicesProxy: