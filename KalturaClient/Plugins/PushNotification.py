# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2019  Kaltura Inc.
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
from .EventNotification import *
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
class KalturaPushNotificationCommandType(object):
    CLEAR_QUEUE = "CLEAR_QUEUE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPushNotificationTemplateOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaPushEventNotificationParameter(KalturaEventNotificationParameter):
    def __init__(self,
            key=NotImplemented,
            description=NotImplemented,
            value=NotImplemented,
            queueKeyToken=NotImplemented):
        KalturaEventNotificationParameter.__init__(self,
            key,
            description,
            value)

        # @var string
        self.queueKeyToken = queueKeyToken


    PROPERTY_LOADERS = {
        'queueKeyToken': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaEventNotificationParameter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushEventNotificationParameter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationParameter.toParams(self)
        kparams.put("objectType", "KalturaPushEventNotificationParameter")
        kparams.addStringIfDefined("queueKeyToken", self.queueKeyToken)
        return kparams

    def getQueueKeyToken(self):
        return self.queueKeyToken

    def setQueueKeyToken(self, newQueueKeyToken):
        self.queueKeyToken = newQueueKeyToken


# @package Kaltura
# @subpackage Client
class KalturaPushNotificationData(KalturaObjectBase):
    def __init__(self,
            queueName=NotImplemented,
            queueKey=NotImplemented,
            url=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        # @readonly
        self.queueName = queueName

        # @var string
        # @readonly
        self.queueKey = queueKey

        # @var string
        # @readonly
        self.url = url


    PROPERTY_LOADERS = {
        'queueName': getXmlNodeText, 
        'queueKey': getXmlNodeText, 
        'url': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushNotificationData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPushNotificationData")
        return kparams

    def getQueueName(self):
        return self.queueName

    def getQueueKey(self):
        return self.queueKey

    def getUrl(self):
        return self.url


# @package Kaltura
# @subpackage Client
class KalturaPushNotificationParams(KalturaObjectBase):
    """Object which contains contextual entry-related data."""

    def __init__(self,
            userParams=NotImplemented):
        KalturaObjectBase.__init__(self)

        # User params
        # @var array of KalturaPushEventNotificationParameter
        self.userParams = userParams


    PROPERTY_LOADERS = {
        'userParams': (KalturaObjectFactory.createArray, 'KalturaPushEventNotificationParameter'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushNotificationParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPushNotificationParams")
        kparams.addArrayIfDefined("userParams", self.userParams)
        return kparams

    def getUserParams(self):
        return self.userParams

    def setUserParams(self, newUserParams):
        self.userParams = newUserParams


# @package Kaltura
# @subpackage Client
class KalturaPushNotificationTemplate(KalturaEventNotificationTemplate):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            type=NotImplemented,
            status=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            manualDispatchEnabled=NotImplemented,
            automaticDispatchEnabled=NotImplemented,
            eventType=NotImplemented,
            eventObjectType=NotImplemented,
            eventConditions=NotImplemented,
            contentParameters=NotImplemented,
            userParameters=NotImplemented,
            queueNameParameters=NotImplemented,
            queueKeyParameters=NotImplemented,
            apiObjectType=NotImplemented,
            objectFormat=NotImplemented,
            responseProfileId=NotImplemented):
        KalturaEventNotificationTemplate.__init__(self,
            id,
            partnerId,
            name,
            systemName,
            description,
            type,
            status,
            createdAt,
            updatedAt,
            manualDispatchEnabled,
            automaticDispatchEnabled,
            eventType,
            eventObjectType,
            eventConditions,
            contentParameters,
            userParameters)

        # Define the content dynamic parameters
        # @var array of KalturaPushEventNotificationParameter
        self.queueNameParameters = queueNameParameters

        # Define the content dynamic parameters
        # @var array of KalturaPushEventNotificationParameter
        self.queueKeyParameters = queueKeyParameters

        # Kaltura API object type
        # @var string
        self.apiObjectType = apiObjectType

        # Kaltura Object format
        # @var KalturaResponseType
        self.objectFormat = objectFormat

        # Kaltura response-profile id
        # @var int
        self.responseProfileId = responseProfileId


    PROPERTY_LOADERS = {
        'queueNameParameters': (KalturaObjectFactory.createArray, 'KalturaPushEventNotificationParameter'), 
        'queueKeyParameters': (KalturaObjectFactory.createArray, 'KalturaPushEventNotificationParameter'), 
        'apiObjectType': getXmlNodeText, 
        'objectFormat': (KalturaEnumsFactory.createInt, "KalturaResponseType"), 
        'responseProfileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaEventNotificationTemplate.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushNotificationTemplate.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationTemplate.toParams(self)
        kparams.put("objectType", "KalturaPushNotificationTemplate")
        kparams.addArrayIfDefined("queueNameParameters", self.queueNameParameters)
        kparams.addArrayIfDefined("queueKeyParameters", self.queueKeyParameters)
        kparams.addStringIfDefined("apiObjectType", self.apiObjectType)
        kparams.addIntEnumIfDefined("objectFormat", self.objectFormat)
        kparams.addIntIfDefined("responseProfileId", self.responseProfileId)
        return kparams

    def getQueueNameParameters(self):
        return self.queueNameParameters

    def setQueueNameParameters(self, newQueueNameParameters):
        self.queueNameParameters = newQueueNameParameters

    def getQueueKeyParameters(self):
        return self.queueKeyParameters

    def setQueueKeyParameters(self, newQueueKeyParameters):
        self.queueKeyParameters = newQueueKeyParameters

    def getApiObjectType(self):
        return self.apiObjectType

    def setApiObjectType(self, newApiObjectType):
        self.apiObjectType = newApiObjectType

    def getObjectFormat(self):
        return self.objectFormat

    def setObjectFormat(self, newObjectFormat):
        self.objectFormat = newObjectFormat

    def getResponseProfileId(self):
        return self.responseProfileId

    def setResponseProfileId(self, newResponseProfileId):
        self.responseProfileId = newResponseProfileId


# @package Kaltura
# @subpackage Client
class KalturaPushNotificationTemplateBaseFilter(KalturaEventNotificationTemplateFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaEventNotificationTemplateFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            systemNameEqual,
            systemNameIn,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaEventNotificationTemplateFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushNotificationTemplateBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationTemplateFilter.toParams(self)
        kparams.put("objectType", "KalturaPushNotificationTemplateBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPushNotificationTemplateFilter(KalturaPushNotificationTemplateBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            systemNameEqual=NotImplemented,
            systemNameIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaPushNotificationTemplateBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            systemNameEqual,
            systemNameIn,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPushNotificationTemplateBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushNotificationTemplateFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPushNotificationTemplateBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaPushNotificationTemplateFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaPushNotificationClientPlugin(KalturaClientPlugin):
    # KalturaPushNotificationClientPlugin
    instance = None

    # @return KalturaPushNotificationClientPlugin
    @staticmethod
    def get():
        if KalturaPushNotificationClientPlugin.instance == None:
            KalturaPushNotificationClientPlugin.instance = KalturaPushNotificationClientPlugin()
        return KalturaPushNotificationClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaPushNotificationCommandType': KalturaPushNotificationCommandType,
            'KalturaPushNotificationTemplateOrderBy': KalturaPushNotificationTemplateOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaPushEventNotificationParameter': KalturaPushEventNotificationParameter,
            'KalturaPushNotificationData': KalturaPushNotificationData,
            'KalturaPushNotificationParams': KalturaPushNotificationParams,
            'KalturaPushNotificationTemplate': KalturaPushNotificationTemplate,
            'KalturaPushNotificationTemplateBaseFilter': KalturaPushNotificationTemplateBaseFilter,
            'KalturaPushNotificationTemplateFilter': KalturaPushNotificationTemplateFilter,
        }

    # @return string
    def getName(self):
        return 'pushNotification'

