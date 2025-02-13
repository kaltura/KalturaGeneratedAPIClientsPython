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

class KalturaPushNotificationCommandType(object):
    CLEAR_QUEUE = "CLEAR_QUEUE"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPushNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPushEventNotificationParameter(KalturaEventNotificationParameter):
    queueKeyToken: str
    def __init__(self,
            key: str = NotImplemented,
            description: str = NotImplemented,
            value: KalturaStringValue = NotImplemented,
            queueKeyToken: str = NotImplemented): ...

    def getQueueKeyToken(self) -> str: ...
    def setQueueKeyToken(self, newQueueKeyToken: str) -> None: ...

class KalturaPushNotificationData(KalturaObjectBase):
    queueName: str
    queueKey: str
    url: str
    def __init__(self,
            queueName: str = NotImplemented,
            queueKey: str = NotImplemented,
            url: str = NotImplemented): ...

    def getQueueName(self) -> str: ...
    def getQueueKey(self) -> str: ...
    def getUrl(self) -> str: ...

class KalturaPushNotificationParams(KalturaObjectBase):
    userParams: List[KalturaPushEventNotificationParameter]
    def __init__(self,
            userParams: List[KalturaPushEventNotificationParameter] = NotImplemented): ...

    def getUserParams(self) -> List[KalturaPushEventNotificationParameter]: ...
    def setUserParams(self, newUserParams: List[KalturaPushEventNotificationParameter]) -> None: ...

class KalturaPushNotificationTemplate(KalturaEventNotificationTemplate):
    queueNameParameters: List[KalturaPushEventNotificationParameter]
    queueKeyParameters: List[KalturaPushEventNotificationParameter]
    apiObjectType: str
    objectFormat: KalturaResponseType
    responseProfileId: int
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
            queueNameParameters: List[KalturaPushEventNotificationParameter] = NotImplemented,
            queueKeyParameters: List[KalturaPushEventNotificationParameter] = NotImplemented,
            apiObjectType: str = NotImplemented,
            objectFormat: KalturaResponseType = NotImplemented,
            responseProfileId: int = NotImplemented): ...

    def getQueueNameParameters(self) -> List[KalturaPushEventNotificationParameter]: ...
    def setQueueNameParameters(self, newQueueNameParameters: List[KalturaPushEventNotificationParameter]) -> None: ...
    def getQueueKeyParameters(self) -> List[KalturaPushEventNotificationParameter]: ...
    def setQueueKeyParameters(self, newQueueKeyParameters: List[KalturaPushEventNotificationParameter]) -> None: ...
    def getApiObjectType(self) -> str: ...
    def setApiObjectType(self, newApiObjectType: str) -> None: ...
    def getObjectFormat(self) -> KalturaResponseType: ...
    def setObjectFormat(self, newObjectFormat: KalturaResponseType) -> None: ...
    def getResponseProfileId(self) -> int: ...
    def setResponseProfileId(self, newResponseProfileId: int) -> None: ...

class KalturaPushNotificationTemplateBaseFilter(KalturaEventNotificationTemplateFilter):
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

class KalturaPushNotificationTemplateFilter(KalturaPushNotificationTemplateBaseFilter):
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

class KalturaPushNotificationClientPluginServicesProxy: