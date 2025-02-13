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
class KalturaUserEntryPermissionLevel(object):
    SPEAKER = 1
    ROOM_MODERATOR = 2
    ATTENDEE = 3
    ADMIN = 4
    PREVIEW_ONLY = 5
    CHAT_MODERATOR = 6
    PANELIST = 7

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaPermissionLevel(KalturaObjectBase):
    def __init__(self,
            permissionLevel = NotImplemented):
        KalturaObjectBase.__init__(self)

        # Permission Level
        # @var KalturaUserEntryPermissionLevel
        self.permissionLevel = permissionLevel


    PROPERTY_LOADERS = {
        'permissionLevel': (KalturaEnumsFactory.createInt, "KalturaUserEntryPermissionLevel"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionLevel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermissionLevel")
        kparams.addIntEnumIfDefined("permissionLevel", self.permissionLevel)
        return kparams

    def getPermissionLevel(self):
        return self.permissionLevel

    def setPermissionLevel(self, newPermissionLevel):
        self.permissionLevel = newPermissionLevel


# @package Kaltura
# @subpackage Client
class KalturaPermissionLevelUserEntry(KalturaUserEntry):
    def __init__(self,
            id = NotImplemented,
            entryId = NotImplemented,
            userId = NotImplemented,
            partnerId = NotImplemented,
            status = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            type = NotImplemented,
            permissionLevels = NotImplemented,
            permissionOrder = NotImplemented):
        KalturaUserEntry.__init__(self,
            id,
            entryId,
            userId,
            partnerId,
            status,
            createdAt,
            updatedAt,
            type)

        # Playback context
        # @var List[KalturaPermissionLevel]
        self.permissionLevels = permissionLevels

        # @var int
        self.permissionOrder = permissionOrder


    PROPERTY_LOADERS = {
        'permissionLevels': (KalturaObjectFactory.createArray, 'KalturaPermissionLevel'), 
        'permissionOrder': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaUserEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionLevelUserEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserEntry.toParams(self)
        kparams.put("objectType", "KalturaPermissionLevelUserEntry")
        kparams.addArrayIfDefined("permissionLevels", self.permissionLevels)
        kparams.addIntIfDefined("permissionOrder", self.permissionOrder)
        return kparams

    def getPermissionLevels(self):
        return self.permissionLevels

    def setPermissionLevels(self, newPermissionLevels):
        self.permissionLevels = newPermissionLevels

    def getPermissionOrder(self):
        return self.permissionOrder

    def setPermissionOrder(self, newPermissionOrder):
        self.permissionOrder = newPermissionOrder


# @package Kaltura
# @subpackage Client
class KalturaPermissionLevelUserEntryFilter(KalturaUserEntryFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            entryIdEqual = NotImplemented,
            entryIdIn = NotImplemented,
            entryIdNotIn = NotImplemented,
            userIdEqual = NotImplemented,
            userIdIn = NotImplemented,
            userIdNotIn = NotImplemented,
            statusEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            typeEqual = NotImplemented,
            userIdEqualCurrent = NotImplemented,
            isAnonymous = NotImplemented,
            privacyContextEqual = NotImplemented,
            privacyContextIn = NotImplemented,
            partnerId = NotImplemented,
            permissionLevels = NotImplemented):
        KalturaUserEntryFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            entryIdEqual,
            entryIdIn,
            entryIdNotIn,
            userIdEqual,
            userIdIn,
            userIdNotIn,
            statusEqual,
            createdAtLessThanOrEqual,
            createdAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            typeEqual,
            userIdEqualCurrent,
            isAnonymous,
            privacyContextEqual,
            privacyContextIn,
            partnerId)

        # @var List[KalturaPermissionLevel]
        self.permissionLevels = permissionLevels


    PROPERTY_LOADERS = {
        'permissionLevels': (KalturaObjectFactory.createArray, 'KalturaPermissionLevel'), 
    }

    def fromXml(self, node):
        KalturaUserEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionLevelUserEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaPermissionLevelUserEntryFilter")
        kparams.addArrayIfDefined("permissionLevels", self.permissionLevels)
        return kparams

    def getPermissionLevels(self):
        return self.permissionLevels

    def setPermissionLevels(self, newPermissionLevels):
        self.permissionLevels = newPermissionLevels


########## services ##########
########## main ##########
class KalturaEntryPermissionLevelClientPlugin(KalturaClientPlugin):
    # KalturaEntryPermissionLevelClientPlugin
    instance = None

    # @return KalturaEntryPermissionLevelClientPlugin
    @staticmethod
    def get():
        if KalturaEntryPermissionLevelClientPlugin.instance == None:
            KalturaEntryPermissionLevelClientPlugin.instance = KalturaEntryPermissionLevelClientPlugin()
        return KalturaEntryPermissionLevelClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaUserEntryPermissionLevel': KalturaUserEntryPermissionLevel,
        }

    def getTypes(self):
        return {
            'KalturaPermissionLevel': KalturaPermissionLevel,
            'KalturaPermissionLevelUserEntry': KalturaPermissionLevelUserEntry,
            'KalturaPermissionLevelUserEntryFilter': KalturaPermissionLevelUserEntryFilter,
        }

    # @return string
    def getName(self):
        return 'entryPermissionLevel'

