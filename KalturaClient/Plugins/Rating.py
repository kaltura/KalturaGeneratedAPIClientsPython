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
# Copyright (C) 2006-2020  Kaltura Inc.
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
class KalturaRatingCountOrderBy(object):

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaRatingCount(KalturaObjectBase):
    def __init__(self,
            entryId=NotImplemented,
            rank=NotImplemented,
            count=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.entryId = entryId

        # @var int
        self.rank = rank

        # @var int
        self.count = count


    PROPERTY_LOADERS = {
        'entryId': getXmlNodeText, 
        'rank': getXmlNodeInt, 
        'count': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRatingCount.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRatingCount")
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addIntIfDefined("rank", self.rank)
        kparams.addIntIfDefined("count", self.count)
        return kparams

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getRank(self):
        return self.rank

    def setRank(self, newRank):
        self.rank = newRank

    def getCount(self):
        return self.count

    def setCount(self, newCount):
        self.count = newCount


# @package Kaltura
# @subpackage Client
class KalturaRatingCountListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaRatingCount
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaRatingCount'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRatingCountListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRatingCountListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaRatingCountBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            entryIdEqual=NotImplemented,
            rankIn=NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var string
        self.entryIdEqual = entryIdEqual

        # @var string
        self.rankIn = rankIn


    PROPERTY_LOADERS = {
        'entryIdEqual': getXmlNodeText, 
        'rankIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRelatedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRatingCountBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedFilter.toParams(self)
        kparams.put("objectType", "KalturaRatingCountBaseFilter")
        kparams.addStringIfDefined("entryIdEqual", self.entryIdEqual)
        kparams.addStringIfDefined("rankIn", self.rankIn)
        return kparams

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getRankIn(self):
        return self.rankIn

    def setRankIn(self, newRankIn):
        self.rankIn = newRankIn


# @package Kaltura
# @subpackage Client
class KalturaRatingCountFilter(KalturaRatingCountBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            entryIdEqual=NotImplemented,
            rankIn=NotImplemented):
        KalturaRatingCountBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            entryIdEqual,
            rankIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRatingCountBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRatingCountFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRatingCountBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaRatingCountFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaRatingService(KalturaServiceBase):
    """Allows user to manipulate their entry rating"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def checkRating(self, entryId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("rating_rating", "checkRating", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def getRatingCounts(self, filter):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("rating_rating", "getRatingCounts", "KalturaRatingCountListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaRatingCountListResponse')

    def rate(self, entryId, rank):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("rank", rank);
        self.client.queueServiceActionCall("rating_rating", "rate", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def removeRating(self, entryId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("rating_rating", "removeRating", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

########## main ##########
class KalturaRatingClientPlugin(KalturaClientPlugin):
    # KalturaRatingClientPlugin
    instance = None

    # @return KalturaRatingClientPlugin
    @staticmethod
    def get():
        if KalturaRatingClientPlugin.instance == None:
            KalturaRatingClientPlugin.instance = KalturaRatingClientPlugin()
        return KalturaRatingClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'rating': KalturaRatingService,
        }

    def getEnums(self):
        return {
            'KalturaRatingCountOrderBy': KalturaRatingCountOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaRatingCount': KalturaRatingCount,
            'KalturaRatingCountListResponse': KalturaRatingCountListResponse,
            'KalturaRatingCountBaseFilter': KalturaRatingCountBaseFilter,
            'KalturaRatingCountFilter': KalturaRatingCountFilter,
        }

    # @return string
    def getName(self):
        return 'rating'

