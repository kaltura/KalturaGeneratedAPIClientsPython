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
class KalturaGameObjectType(object):
    LEADERBOARD = "1"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaUserScoreProperties(KalturaObjectBase):
    def __init__(self,
            rank = NotImplemented,
            userId = NotImplemented,
            score = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.rank = rank

        # @var str
        self.userId = userId

        # @var int
        self.score = score


    PROPERTY_LOADERS = {
        'rank': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'score': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserScoreProperties.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserScoreProperties")
        kparams.addIntIfDefined("rank", self.rank)
        kparams.addStringIfDefined("userId", self.userId)
        kparams.addIntIfDefined("score", self.score)
        return kparams

    def getRank(self):
        return self.rank

    def setRank(self, newRank):
        self.rank = newRank

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getScore(self):
        return self.score

    def setScore(self, newScore):
        self.score = newScore


# @package Kaltura
# @subpackage Client
class KalturaUserScorePropertiesResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaUserScoreProperties]
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaUserScoreProperties'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserScorePropertiesResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaUserScorePropertiesResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaUserScorePropertiesBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRelatedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserScorePropertiesBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedFilter.toParams(self)
        kparams.put("objectType", "KalturaUserScorePropertiesBaseFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaUserScorePropertiesFilter(KalturaUserScorePropertiesBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            gameObjectId = NotImplemented,
            gameObjectType = NotImplemented,
            userIdEqual = NotImplemented,
            placesAboveUser = NotImplemented,
            placesBelowUser = NotImplemented):
        KalturaUserScorePropertiesBaseFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var str
        self.gameObjectId = gameObjectId

        # @var KalturaGameObjectType
        self.gameObjectType = gameObjectType

        # @var str
        self.userIdEqual = userIdEqual

        # @var int
        self.placesAboveUser = placesAboveUser

        # @var int
        self.placesBelowUser = placesBelowUser


    PROPERTY_LOADERS = {
        'gameObjectId': getXmlNodeText, 
        'gameObjectType': (KalturaEnumsFactory.createString, "KalturaGameObjectType"), 
        'userIdEqual': getXmlNodeText, 
        'placesAboveUser': getXmlNodeInt, 
        'placesBelowUser': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaUserScorePropertiesBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserScorePropertiesFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUserScorePropertiesBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUserScorePropertiesFilter")
        kparams.addStringIfDefined("gameObjectId", self.gameObjectId)
        kparams.addStringEnumIfDefined("gameObjectType", self.gameObjectType)
        kparams.addStringIfDefined("userIdEqual", self.userIdEqual)
        kparams.addIntIfDefined("placesAboveUser", self.placesAboveUser)
        kparams.addIntIfDefined("placesBelowUser", self.placesBelowUser)
        return kparams

    def getGameObjectId(self):
        return self.gameObjectId

    def setGameObjectId(self, newGameObjectId):
        self.gameObjectId = newGameObjectId

    def getGameObjectType(self):
        return self.gameObjectType

    def setGameObjectType(self, newGameObjectType):
        self.gameObjectType = newGameObjectType

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getPlacesAboveUser(self):
        return self.placesAboveUser

    def setPlacesAboveUser(self, newPlacesAboveUser):
        self.placesAboveUser = newPlacesAboveUser

    def getPlacesBelowUser(self):
        return self.placesBelowUser

    def setPlacesBelowUser(self, newPlacesBelowUser):
        self.placesBelowUser = newPlacesBelowUser


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaUserScoreService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def delete(self, gameObjectId, gameObjectType, userId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("gameObjectId", gameObjectId)
        kparams.addStringIfDefined("gameObjectType", gameObjectType)
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("game_userscore", "delete", "KalturaUserScorePropertiesResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaUserScorePropertiesResponse')

    def list(self, filter, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("game_userscore", "list", "KalturaUserScorePropertiesResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaUserScorePropertiesResponse')

    def update(self, gameObjectId, gameObjectType, userId, score):
        kparams = KalturaParams()
        kparams.addStringIfDefined("gameObjectId", gameObjectId)
        kparams.addStringIfDefined("gameObjectType", gameObjectType)
        kparams.addStringIfDefined("userId", userId)
        kparams.addIntIfDefined("score", score);
        self.client.queueServiceActionCall("game_userscore", "update", "KalturaUserScorePropertiesResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaUserScorePropertiesResponse')

########## main ##########
class KalturaGameClientPlugin(KalturaClientPlugin):
    # KalturaGameClientPlugin
    instance = None

    # @return KalturaGameClientPlugin
    @staticmethod
    def get():
        if KalturaGameClientPlugin.instance == None:
            KalturaGameClientPlugin.instance = KalturaGameClientPlugin()
        return KalturaGameClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'userScore': KalturaUserScoreService,
        }

    def getEnums(self):
        return {
            'KalturaGameObjectType': KalturaGameObjectType,
        }

    def getTypes(self):
        return {
            'KalturaUserScoreProperties': KalturaUserScoreProperties,
            'KalturaUserScorePropertiesResponse': KalturaUserScorePropertiesResponse,
            'KalturaUserScorePropertiesBaseFilter': KalturaUserScorePropertiesBaseFilter,
            'KalturaUserScorePropertiesFilter': KalturaUserScorePropertiesFilter,
        }

    # @return string
    def getName(self):
        return 'game'

