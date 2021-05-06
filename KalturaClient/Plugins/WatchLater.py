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
# Copyright (C) 2006-2021  Kaltura Inc.
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
########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaWatchLaterUserEntry(KalturaUserEntry):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            userId=NotImplemented,
            partnerId=NotImplemented,
            status=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            type=NotImplemented,
            extendedStatus=NotImplemented):
        KalturaUserEntry.__init__(self,
            id,
            entryId,
            userId,
            partnerId,
            status,
            createdAt,
            updatedAt,
            type,
            extendedStatus)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUserEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWatchLaterUserEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserEntry.toParams(self)
        kparams.put("objectType", "KalturaWatchLaterUserEntry")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaWatchLaterUserEntryAdvancedFilter(KalturaSearchItem):
    def __init__(self,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            userIdEqual=NotImplemented,
            userIdIn=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            extendedStatusEqual=NotImplemented,
            extendedStatusIn=NotImplemented):
        KalturaSearchItem.__init__(self)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.userIdEqual = userIdEqual

        # @var string
        self.userIdIn = userIdIn

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var KalturaUserEntryExtendedStatus
        self.extendedStatusEqual = extendedStatusEqual

        # @var string
        self.extendedStatusIn = extendedStatusIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'userIdIn': getXmlNodeText, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'extendedStatusEqual': (KalturaEnumsFactory.createString, "KalturaUserEntryExtendedStatus"), 
        'extendedStatusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWatchLaterUserEntryAdvancedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchItem.toParams(self)
        kparams.put("objectType", "KalturaWatchLaterUserEntryAdvancedFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("userIdEqual", self.userIdEqual)
        kparams.addStringIfDefined("userIdIn", self.userIdIn)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addStringEnumIfDefined("extendedStatusEqual", self.extendedStatusEqual)
        kparams.addStringIfDefined("extendedStatusIn", self.extendedStatusIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getUserIdIn(self):
        return self.userIdIn

    def setUserIdIn(self, newUserIdIn):
        self.userIdIn = newUserIdIn

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getExtendedStatusEqual(self):
        return self.extendedStatusEqual

    def setExtendedStatusEqual(self, newExtendedStatusEqual):
        self.extendedStatusEqual = newExtendedStatusEqual

    def getExtendedStatusIn(self):
        return self.extendedStatusIn

    def setExtendedStatusIn(self, newExtendedStatusIn):
        self.extendedStatusIn = newExtendedStatusIn


# @package Kaltura
# @subpackage Client
class KalturaWatchLaterUserEntryFilter(KalturaUserEntryFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            entryIdEqual=NotImplemented,
            entryIdIn=NotImplemented,
            entryIdNotIn=NotImplemented,
            userIdEqual=NotImplemented,
            userIdIn=NotImplemented,
            userIdNotIn=NotImplemented,
            statusEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            typeEqual=NotImplemented,
            extendedStatusEqual=NotImplemented,
            extendedStatusIn=NotImplemented,
            extendedStatusNotIn=NotImplemented,
            userIdEqualCurrent=NotImplemented,
            isAnonymous=NotImplemented,
            privacyContextEqual=NotImplemented,
            privacyContextIn=NotImplemented,
            partnerId=NotImplemented):
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
            extendedStatusEqual,
            extendedStatusIn,
            extendedStatusNotIn,
            userIdEqualCurrent,
            isAnonymous,
            privacyContextEqual,
            privacyContextIn,
            partnerId)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUserEntryFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaWatchLaterUserEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaWatchLaterUserEntryFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaWatchLaterClientPlugin(KalturaClientPlugin):
    # KalturaWatchLaterClientPlugin
    instance = None

    # @return KalturaWatchLaterClientPlugin
    @staticmethod
    def get():
        if KalturaWatchLaterClientPlugin.instance == None:
            KalturaWatchLaterClientPlugin.instance = KalturaWatchLaterClientPlugin()
        return KalturaWatchLaterClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaWatchLaterUserEntry': KalturaWatchLaterUserEntry,
            'KalturaWatchLaterUserEntryAdvancedFilter': KalturaWatchLaterUserEntryAdvancedFilter,
            'KalturaWatchLaterUserEntryFilter': KalturaWatchLaterUserEntryFilter,
        }

    # @return string
    def getName(self):
        return 'watchLater'

