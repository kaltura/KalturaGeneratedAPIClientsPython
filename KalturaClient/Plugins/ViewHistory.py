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
class KalturaViewHistoryUserEntry(KalturaUserEntry):
    def __init__(self,
            id=NotImplemented,
            entryId=NotImplemented,
            userId=NotImplemented,
            partnerId=NotImplemented,
            status=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            type=NotImplemented,
            extendedStatus=NotImplemented,
            playbackContext=NotImplemented,
            lastTimeReached=NotImplemented,
            lastUpdateTime=NotImplemented):
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

        # Playback context
        # @var string
        self.playbackContext = playbackContext

        # Last playback time reached by user
        # @var int
        self.lastTimeReached = lastTimeReached

        # @var int
        self.lastUpdateTime = lastUpdateTime


    PROPERTY_LOADERS = {
        'playbackContext': getXmlNodeText, 
        'lastTimeReached': getXmlNodeInt, 
        'lastUpdateTime': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaUserEntry.fromXml(self, node)
        self.fromXmlImpl(node, KalturaViewHistoryUserEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserEntry.toParams(self)
        kparams.put("objectType", "KalturaViewHistoryUserEntry")
        kparams.addStringIfDefined("playbackContext", self.playbackContext)
        kparams.addIntIfDefined("lastTimeReached", self.lastTimeReached)
        kparams.addIntIfDefined("lastUpdateTime", self.lastUpdateTime)
        return kparams

    def getPlaybackContext(self):
        return self.playbackContext

    def setPlaybackContext(self, newPlaybackContext):
        self.playbackContext = newPlaybackContext

    def getLastTimeReached(self):
        return self.lastTimeReached

    def setLastTimeReached(self, newLastTimeReached):
        self.lastTimeReached = newLastTimeReached

    def getLastUpdateTime(self):
        return self.lastUpdateTime

    def setLastUpdateTime(self, newLastUpdateTime):
        self.lastUpdateTime = newLastUpdateTime


# @package Kaltura
# @subpackage Client
class KalturaViewHistoryUserEntryAdvancedFilter(KalturaSearchItem):
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

        # @var string
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.userIdEqual = userIdEqual

        # @var string
        self.userIdIn = userIdIn

        # @var string
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var string
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var KalturaUserEntryExtendedStatus
        self.extendedStatusEqual = extendedStatusEqual

        # @var string
        self.extendedStatusIn = extendedStatusIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'userIdIn': getXmlNodeText, 
        'updatedAtGreaterThanOrEqual': getXmlNodeText, 
        'updatedAtLessThanOrEqual': getXmlNodeText, 
        'extendedStatusEqual': (KalturaEnumsFactory.createString, "KalturaUserEntryExtendedStatus"), 
        'extendedStatusIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaViewHistoryUserEntryAdvancedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchItem.toParams(self)
        kparams.put("objectType", "KalturaViewHistoryUserEntryAdvancedFilter")
        kparams.addStringIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("userIdEqual", self.userIdEqual)
        kparams.addStringIfDefined("userIdIn", self.userIdIn)
        kparams.addStringIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addStringIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
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
class KalturaViewHistoryUserEntryFilter(KalturaUserEntryFilter):
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
        self.fromXmlImpl(node, KalturaViewHistoryUserEntryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserEntryFilter.toParams(self)
        kparams.put("objectType", "KalturaViewHistoryUserEntryFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaViewHistoryClientPlugin(KalturaClientPlugin):
    # KalturaViewHistoryClientPlugin
    instance = None

    # @return KalturaViewHistoryClientPlugin
    @staticmethod
    def get():
        if KalturaViewHistoryClientPlugin.instance == None:
            KalturaViewHistoryClientPlugin.instance = KalturaViewHistoryClientPlugin()
        return KalturaViewHistoryClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaViewHistoryUserEntry': KalturaViewHistoryUserEntry,
            'KalturaViewHistoryUserEntryAdvancedFilter': KalturaViewHistoryUserEntryAdvancedFilter,
            'KalturaViewHistoryUserEntryFilter': KalturaViewHistoryUserEntryFilter,
        }

    # @return string
    def getName(self):
        return 'viewHistory'

