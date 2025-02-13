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

class KalturaKafkaNotificationFormat(object):
    JSON = 1
    AVRO = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaKafkaNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaKafkaNotificationTemplate(KalturaEventNotificationTemplate):
    topicName: str
    partitionKey: str
    messageFormat: KalturaKafkaNotificationFormat
    apiObjectType: str
    responseProfileSystemName: str
    requiresPermissions: str
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
            topicName: str = NotImplemented,
            partitionKey: str = NotImplemented,
            messageFormat: KalturaKafkaNotificationFormat = NotImplemented,
            apiObjectType: str = NotImplemented,
            responseProfileSystemName: str = NotImplemented,
            requiresPermissions: str = NotImplemented): ...

    def getTopicName(self) -> str: ...
    def setTopicName(self, newTopicName: str) -> None: ...
    def getPartitionKey(self) -> str: ...
    def setPartitionKey(self, newPartitionKey: str) -> None: ...
    def getMessageFormat(self) -> KalturaKafkaNotificationFormat: ...
    def setMessageFormat(self, newMessageFormat: KalturaKafkaNotificationFormat) -> None: ...
    def getApiObjectType(self) -> str: ...
    def setApiObjectType(self, newApiObjectType: str) -> None: ...
    def getResponseProfileSystemName(self) -> str: ...
    def setResponseProfileSystemName(self, newResponseProfileSystemName: str) -> None: ...
    def getRequiresPermissions(self) -> str: ...
    def setRequiresPermissions(self, newRequiresPermissions: str) -> None: ...

class KalturaKafkaNotificationTemplateBaseFilter(KalturaEventNotificationTemplateFilter):
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

class KalturaKafkaNotificationTemplateFilter(KalturaKafkaNotificationTemplateBaseFilter):
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

class KalturaKafkaNotificationClientPluginServicesProxy: