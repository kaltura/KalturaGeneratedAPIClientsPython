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
########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaBooleanNotificationTemplate(KalturaEventNotificationTemplate):
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
            eventDelayedCondition = NotImplemented):
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


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaEventNotificationTemplate.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBooleanNotificationTemplate.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationTemplate.toParams(self)
        kparams.put("objectType", "KalturaBooleanNotificationTemplate")
        return kparams


########## services ##########
########## main ##########
class KalturaBooleanNotificationClientPlugin(KalturaClientPlugin):
    # KalturaBooleanNotificationClientPlugin
    instance = None

    # @return KalturaBooleanNotificationClientPlugin
    @staticmethod
    def get():
        if KalturaBooleanNotificationClientPlugin.instance == None:
            KalturaBooleanNotificationClientPlugin.instance = KalturaBooleanNotificationClientPlugin()
        return KalturaBooleanNotificationClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaBooleanNotificationTemplate': KalturaBooleanNotificationTemplate,
        }

    # @return string
    def getName(self):
        return 'booleanNotification'

