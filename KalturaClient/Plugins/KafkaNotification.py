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
class KalturaKafkaNotificationFormat(object):
    JSON = 1
    AVRO = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaKafkaNotificationTemplateOrderBy(object):
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
class KalturaKafkaNotificationTemplate(KalturaEventNotificationTemplate):
    def __init__(self,
            id = NotImplemented,
            partnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            description = NotImplemented,
            type = NotImplemented,
            status = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            manualDispatchEnabled = NotImplemented,
            automaticDispatchEnabled = NotImplemented,
            eventType = NotImplemented,
            eventObjectType = NotImplemented,
            eventConditions = NotImplemented,
            contentParameters = NotImplemented,
            userParameters = NotImplemented,
            eventDelayedCondition = NotImplemented,
            topicName = NotImplemented,
            partitionKey = NotImplemented,
            messageFormat = NotImplemented,
            apiObjectType = NotImplemented,
            responseProfileSystemName = NotImplemented,
            requiresPermissions = NotImplemented):
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
            userParameters,
            eventDelayedCondition)

        # Define the content dynamic parameters
        # @var str
        self.topicName = topicName

        # Define the content dynamic parameters
        # @var str
        self.partitionKey = partitionKey

        # Define the content dynamic parameters
        # @var KalturaKafkaNotificationFormat
        self.messageFormat = messageFormat

        # Kaltura API object type
        # @var str
        self.apiObjectType = apiObjectType

        # Kaltura response-profile system name
        # @var str
        self.responseProfileSystemName = responseProfileSystemName

        # Partner permissions needed to trigger the notification (comma seperated list of permissions)
        # @var str
        self.requiresPermissions = requiresPermissions


    PROPERTY_LOADERS = {
        'topicName': getXmlNodeText, 
        'partitionKey': getXmlNodeText, 
        'messageFormat': (KalturaEnumsFactory.createInt, "KalturaKafkaNotificationFormat"), 
        'apiObjectType': getXmlNodeText, 
        'responseProfileSystemName': getXmlNodeText, 
        'requiresPermissions': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaEventNotificationTemplate.fromXml(self, node)
        self.fromXmlImpl(node, KalturaKafkaNotificationTemplate.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationTemplate.toParams(self)
        kparams.put("objectType", "KalturaKafkaNotificationTemplate")
        kparams.addStringIfDefined("topicName", self.topicName)
        kparams.addStringIfDefined("partitionKey", self.partitionKey)
        kparams.addIntEnumIfDefined("messageFormat", self.messageFormat)
        kparams.addStringIfDefined("apiObjectType", self.apiObjectType)
        kparams.addStringIfDefined("responseProfileSystemName", self.responseProfileSystemName)
        kparams.addStringIfDefined("requiresPermissions", self.requiresPermissions)
        return kparams

    def getTopicName(self):
        return self.topicName

    def setTopicName(self, newTopicName):
        self.topicName = newTopicName

    def getPartitionKey(self):
        return self.partitionKey

    def setPartitionKey(self, newPartitionKey):
        self.partitionKey = newPartitionKey

    def getMessageFormat(self):
        return self.messageFormat

    def setMessageFormat(self, newMessageFormat):
        self.messageFormat = newMessageFormat

    def getApiObjectType(self):
        return self.apiObjectType

    def setApiObjectType(self, newApiObjectType):
        self.apiObjectType = newApiObjectType

    def getResponseProfileSystemName(self):
        return self.responseProfileSystemName

    def setResponseProfileSystemName(self, newResponseProfileSystemName):
        self.responseProfileSystemName = newResponseProfileSystemName

    def getRequiresPermissions(self):
        return self.requiresPermissions

    def setRequiresPermissions(self, newRequiresPermissions):
        self.requiresPermissions = newRequiresPermissions


# @package Kaltura
# @subpackage Client
class KalturaKafkaNotificationTemplateBaseFilter(KalturaEventNotificationTemplateFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            systemNameEqual = NotImplemented,
            systemNameIn = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented):
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
        self.fromXmlImpl(node, KalturaKafkaNotificationTemplateBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationTemplateFilter.toParams(self)
        kparams.put("objectType", "KalturaKafkaNotificationTemplateBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaKafkaNotificationTemplateFilter(KalturaKafkaNotificationTemplateBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            partnerIdIn = NotImplemented,
            systemNameEqual = NotImplemented,
            systemNameIn = NotImplemented,
            typeEqual = NotImplemented,
            typeIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented):
        KalturaKafkaNotificationTemplateBaseFilter.__init__(self,
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
        KalturaKafkaNotificationTemplateBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaKafkaNotificationTemplateFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaKafkaNotificationTemplateBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaKafkaNotificationTemplateFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaKafkaNotificationClientPlugin(KalturaClientPlugin):
    # KalturaKafkaNotificationClientPlugin
    instance = None

    # @return KalturaKafkaNotificationClientPlugin
    @staticmethod
    def get():
        if KalturaKafkaNotificationClientPlugin.instance == None:
            KalturaKafkaNotificationClientPlugin.instance = KalturaKafkaNotificationClientPlugin()
        return KalturaKafkaNotificationClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaKafkaNotificationFormat': KalturaKafkaNotificationFormat,
            'KalturaKafkaNotificationTemplateOrderBy': KalturaKafkaNotificationTemplateOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaKafkaNotificationTemplate': KalturaKafkaNotificationTemplate,
            'KalturaKafkaNotificationTemplateBaseFilter': KalturaKafkaNotificationTemplateBaseFilter,
            'KalturaKafkaNotificationTemplateFilter': KalturaKafkaNotificationTemplateFilter,
        }

    # @return string
    def getName(self):
        return 'kafkaNotification'

