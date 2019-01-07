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
########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaPollService(KalturaServiceBase):
    """Poll service
     The poll service works against the cache entirely no DB instance should be used here"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, pollType = "SINGLE_ANONYMOUS"):
        """Add Action"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pollType", pollType)
        self.client.queueServiceActionCall("poll_poll", "add", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getVote(self, pollId, userId):
        """Vote Action"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pollId", pollId)
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("poll_poll", "getVote", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getVotes(self, pollId, answerIds):
        """Get Votes Action"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pollId", pollId)
        kparams.addStringIfDefined("answerIds", answerIds)
        self.client.queueServiceActionCall("poll_poll", "getVotes", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def resetVotes(self, pollId):
        """Get resetVotes Action"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pollId", pollId)
        self.client.queueServiceActionCall("poll_poll", "resetVotes", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def vote(self, pollId, userId, answerIds):
        """Vote Action"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pollId", pollId)
        kparams.addStringIfDefined("userId", userId)
        kparams.addStringIfDefined("answerIds", answerIds)
        self.client.queueServiceActionCall("poll_poll", "vote", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaPollClientPlugin(KalturaClientPlugin):
    # KalturaPollClientPlugin
    instance = None

    # @return KalturaPollClientPlugin
    @staticmethod
    def get():
        if KalturaPollClientPlugin.instance == None:
            KalturaPollClientPlugin.instance = KalturaPollClientPlugin()
        return KalturaPollClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'poll': KalturaPollService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
        }

    # @return string
    def getName(self):
        return 'poll'

