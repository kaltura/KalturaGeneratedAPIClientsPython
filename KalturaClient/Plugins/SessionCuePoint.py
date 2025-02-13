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
from .CuePoint import *
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
class KalturaSessionCuePointOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    END_TIME_ASC = "+endTime"
    INT_ID_ASC = "+intId"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    START_TIME_ASC = "+startTime"
    TRIGGERED_AT_ASC = "+triggeredAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    END_TIME_DESC = "-endTime"
    INT_ID_DESC = "-intId"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"
    START_TIME_DESC = "-startTime"
    TRIGGERED_AT_DESC = "-triggeredAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaSessionCuePoint(KalturaCuePoint):
    def __init__(self,
            id = NotImplemented,
            intId = NotImplemented,
            cuePointType = NotImplemented,
            status = NotImplemented,
            entryId = NotImplemented,
            partnerId = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            triggeredAt = NotImplemented,
            tags = NotImplemented,
            startTime = NotImplemented,
            userId = NotImplemented,
            partnerData = NotImplemented,
            partnerSortValue = NotImplemented,
            forceStop = NotImplemented,
            thumbOffset = NotImplemented,
            systemName = NotImplemented,
            isMomentary = NotImplemented,
            copiedFrom = NotImplemented,
            name = NotImplemented,
            endTime = NotImplemented,
            duration = NotImplemented,
            sessionOwner = NotImplemented):
        KalturaCuePoint.__init__(self,
            id,
            intId,
            cuePointType,
            status,
            entryId,
            partnerId,
            createdAt,
            updatedAt,
            triggeredAt,
            tags,
            startTime,
            userId,
            partnerData,
            partnerSortValue,
            forceStop,
            thumbOffset,
            systemName,
            isMomentary,
            copiedFrom)

        # @var str
        self.name = name

        # @var int
        self.endTime = endTime

        # Duration in milliseconds
        # @var int
        # @readonly
        self.duration = duration

        # @var str
        self.sessionOwner = sessionOwner


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'endTime': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'sessionOwner': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaCuePoint.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSessionCuePoint.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCuePoint.toParams(self)
        kparams.put("objectType", "KalturaSessionCuePoint")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("endTime", self.endTime)
        kparams.addStringIfDefined("sessionOwner", self.sessionOwner)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, newEndTime):
        self.endTime = newEndTime

    def getDuration(self):
        return self.duration

    def getSessionOwner(self):
        return self.sessionOwner

    def setSessionOwner(self, newSessionOwner):
        self.sessionOwner = newSessionOwner


# @package Kaltura
# @subpackage Client
class KalturaSessionCuePointBaseFilter(KalturaCuePointFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            cuePointTypeEqual = NotImplemented,
            cuePointTypeIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            entryIdEqual = NotImplemented,
            entryIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            triggeredAtGreaterThanOrEqual = NotImplemented,
            triggeredAtLessThanOrEqual = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            startTimeGreaterThanOrEqual = NotImplemented,
            startTimeLessThanOrEqual = NotImplemented,
            userIdEqual = NotImplemented,
            userIdIn = NotImplemented,
            partnerSortValueEqual = NotImplemented,
            partnerSortValueIn = NotImplemented,
            partnerSortValueGreaterThanOrEqual = NotImplemented,
            partnerSortValueLessThanOrEqual = NotImplemented,
            forceStopEqual = NotImplemented,
            systemNameEqual = NotImplemented,
            systemNameIn = NotImplemented,
            freeText = NotImplemented,
            userIdEqualCurrent = NotImplemented,
            userIdCurrent = NotImplemented,
            endTimeGreaterThanOrEqual = NotImplemented,
            endTimeLessThanOrEqual = NotImplemented,
            durationGreaterThanOrEqual = NotImplemented,
            durationLessThanOrEqual = NotImplemented):
        KalturaCuePointFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            cuePointTypeEqual,
            cuePointTypeIn,
            statusEqual,
            statusIn,
            entryIdEqual,
            entryIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            triggeredAtGreaterThanOrEqual,
            triggeredAtLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            startTimeGreaterThanOrEqual,
            startTimeLessThanOrEqual,
            userIdEqual,
            userIdIn,
            partnerSortValueEqual,
            partnerSortValueIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            forceStopEqual,
            systemNameEqual,
            systemNameIn,
            freeText,
            userIdEqualCurrent,
            userIdCurrent)

        # @var int
        self.endTimeGreaterThanOrEqual = endTimeGreaterThanOrEqual

        # @var int
        self.endTimeLessThanOrEqual = endTimeLessThanOrEqual

        # @var int
        self.durationGreaterThanOrEqual = durationGreaterThanOrEqual

        # @var int
        self.durationLessThanOrEqual = durationLessThanOrEqual


    PROPERTY_LOADERS = {
        'endTimeGreaterThanOrEqual': getXmlNodeInt, 
        'endTimeLessThanOrEqual': getXmlNodeInt, 
        'durationGreaterThanOrEqual': getXmlNodeInt, 
        'durationLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaCuePointFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSessionCuePointBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCuePointFilter.toParams(self)
        kparams.put("objectType", "KalturaSessionCuePointBaseFilter")
        kparams.addIntIfDefined("endTimeGreaterThanOrEqual", self.endTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("endTimeLessThanOrEqual", self.endTimeLessThanOrEqual)
        kparams.addIntIfDefined("durationGreaterThanOrEqual", self.durationGreaterThanOrEqual)
        kparams.addIntIfDefined("durationLessThanOrEqual", self.durationLessThanOrEqual)
        return kparams

    def getEndTimeGreaterThanOrEqual(self):
        return self.endTimeGreaterThanOrEqual

    def setEndTimeGreaterThanOrEqual(self, newEndTimeGreaterThanOrEqual):
        self.endTimeGreaterThanOrEqual = newEndTimeGreaterThanOrEqual

    def getEndTimeLessThanOrEqual(self):
        return self.endTimeLessThanOrEqual

    def setEndTimeLessThanOrEqual(self, newEndTimeLessThanOrEqual):
        self.endTimeLessThanOrEqual = newEndTimeLessThanOrEqual

    def getDurationGreaterThanOrEqual(self):
        return self.durationGreaterThanOrEqual

    def setDurationGreaterThanOrEqual(self, newDurationGreaterThanOrEqual):
        self.durationGreaterThanOrEqual = newDurationGreaterThanOrEqual

    def getDurationLessThanOrEqual(self):
        return self.durationLessThanOrEqual

    def setDurationLessThanOrEqual(self, newDurationLessThanOrEqual):
        self.durationLessThanOrEqual = newDurationLessThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaSessionCuePointFilter(KalturaSessionCuePointBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            cuePointTypeEqual = NotImplemented,
            cuePointTypeIn = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            entryIdEqual = NotImplemented,
            entryIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            triggeredAtGreaterThanOrEqual = NotImplemented,
            triggeredAtLessThanOrEqual = NotImplemented,
            tagsLike = NotImplemented,
            tagsMultiLikeOr = NotImplemented,
            tagsMultiLikeAnd = NotImplemented,
            startTimeGreaterThanOrEqual = NotImplemented,
            startTimeLessThanOrEqual = NotImplemented,
            userIdEqual = NotImplemented,
            userIdIn = NotImplemented,
            partnerSortValueEqual = NotImplemented,
            partnerSortValueIn = NotImplemented,
            partnerSortValueGreaterThanOrEqual = NotImplemented,
            partnerSortValueLessThanOrEqual = NotImplemented,
            forceStopEqual = NotImplemented,
            systemNameEqual = NotImplemented,
            systemNameIn = NotImplemented,
            freeText = NotImplemented,
            userIdEqualCurrent = NotImplemented,
            userIdCurrent = NotImplemented,
            endTimeGreaterThanOrEqual = NotImplemented,
            endTimeLessThanOrEqual = NotImplemented,
            durationGreaterThanOrEqual = NotImplemented,
            durationLessThanOrEqual = NotImplemented):
        KalturaSessionCuePointBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            cuePointTypeEqual,
            cuePointTypeIn,
            statusEqual,
            statusIn,
            entryIdEqual,
            entryIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            triggeredAtGreaterThanOrEqual,
            triggeredAtLessThanOrEqual,
            tagsLike,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            startTimeGreaterThanOrEqual,
            startTimeLessThanOrEqual,
            userIdEqual,
            userIdIn,
            partnerSortValueEqual,
            partnerSortValueIn,
            partnerSortValueGreaterThanOrEqual,
            partnerSortValueLessThanOrEqual,
            forceStopEqual,
            systemNameEqual,
            systemNameIn,
            freeText,
            userIdEqualCurrent,
            userIdCurrent,
            endTimeGreaterThanOrEqual,
            endTimeLessThanOrEqual,
            durationGreaterThanOrEqual,
            durationLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSessionCuePointBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSessionCuePointFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSessionCuePointBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaSessionCuePointFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaSessionCuePointClientPlugin(KalturaClientPlugin):
    # KalturaSessionCuePointClientPlugin
    instance = None

    # @return KalturaSessionCuePointClientPlugin
    @staticmethod
    def get():
        if KalturaSessionCuePointClientPlugin.instance == None:
            KalturaSessionCuePointClientPlugin.instance = KalturaSessionCuePointClientPlugin()
        return KalturaSessionCuePointClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaSessionCuePointOrderBy': KalturaSessionCuePointOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaSessionCuePoint': KalturaSessionCuePoint,
            'KalturaSessionCuePointBaseFilter': KalturaSessionCuePointBaseFilter,
            'KalturaSessionCuePointFilter': KalturaSessionCuePointFilter,
        }

    # @return string
    def getName(self):
        return 'sessionCuePoint'

