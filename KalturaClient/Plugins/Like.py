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
# Copyright (C) 2006-2015  Kaltura Inc.
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
from Core import *
from ..Base import *

########## enums ##########
########## classes ##########
########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaLikeService(KalturaServiceBase):
    """Allows user to 'like' or 'unlike' and entry"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def like(self, entryId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("like_like", "like", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def unlike(self, entryId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("like_like", "unlike", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def checkLikeExists(self, entryId, userId = NotImplemented):
        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("like_like", "checkLikeExists", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

########## main ##########
class KalturaLikeClientPlugin(KalturaClientPlugin):
    # KalturaLikeClientPlugin
    instance = None

    # @return KalturaLikeClientPlugin
    @staticmethod
    def get():
        if KalturaLikeClientPlugin.instance == None:
            KalturaLikeClientPlugin.instance = KalturaLikeClientPlugin()
        return KalturaLikeClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'like': KalturaLikeService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
        }

    # @return string
    def getName(self):
        return 'like'

