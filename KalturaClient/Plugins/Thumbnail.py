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
from .FileSync import *
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
class KalturaThumbnailService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def transform(self, transformString):
        """Retrieves a thumbnail according to the required transformation"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("transformString", transformString)
        self.client.queueServiceActionCall("thumbnail_thumbnail", "transform", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

########## main ##########
class KalturaThumbnailClientPlugin(KalturaClientPlugin):
    # KalturaThumbnailClientPlugin
    instance = None

    # @return KalturaThumbnailClientPlugin
    @staticmethod
    def get():
        if KalturaThumbnailClientPlugin.instance == None:
            KalturaThumbnailClientPlugin.instance = KalturaThumbnailClientPlugin()
        return KalturaThumbnailClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'thumbnail': KalturaThumbnailService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
        }

    # @return string
    def getName(self):
        return 'thumbnail'

