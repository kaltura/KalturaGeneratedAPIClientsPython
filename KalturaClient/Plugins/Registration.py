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
class KalturaRegistrationUserEntry(KalturaUserEntry):
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
        self.fromXmlImpl(node, KalturaRegistrationUserEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserEntry.toParams(self)
        kparams.put("objectType", "KalturaRegistrationUserEntry")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaRegistrationUserEntryFilter(KalturaUserEntryFilter):
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
        self.fromXmlImpl(node, KalturaRegistrationUserEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaRegistrationUserEntryFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaRegistrationClientPlugin(KalturaClientPlugin):
    # KalturaRegistrationClientPlugin
    instance = None

    # @return KalturaRegistrationClientPlugin
    @staticmethod
    def get():
        if KalturaRegistrationClientPlugin.instance == None:
            KalturaRegistrationClientPlugin.instance = KalturaRegistrationClientPlugin()
        return KalturaRegistrationClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaRegistrationUserEntry': KalturaRegistrationUserEntry,
            'KalturaRegistrationUserEntryFilter': KalturaRegistrationUserEntryFilter,
        }

    # @return string
    def getName(self):
        return 'registration'

