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
########## classes ##########
########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaSharepointExtensionService(KalturaServiceBase):
    """Kaltura Sharepoint Extension Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def isVersionSupported(self, serverMajor, serverMinor, serverBuild):
        """Is this Kaltura-Sharepoint-Server-Plugin supports minimum version of $major.$minor.$build (which is required by the extension)"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("serverMajor", serverMajor);
        kparams.addIntIfDefined("serverMinor", serverMinor);
        kparams.addIntIfDefined("serverBuild", serverBuild);
        self.client.queueServiceActionCall("kalturasharepointextension_sharepointextension", "isVersionSupported", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def listUiconfs(self):
        """list uiconfs for sharepoint extension"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("kalturasharepointextension_sharepointextension", "listUiconfs", "KalturaUiConfListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaUiConfListResponse')

########## main ##########
class KalturaKalturaSharepointExtensionClientPlugin(KalturaClientPlugin):
    # KalturaKalturaSharepointExtensionClientPlugin
    instance = None

    # @return KalturaKalturaSharepointExtensionClientPlugin
    @staticmethod
    def get():
        if KalturaKalturaSharepointExtensionClientPlugin.instance == None:
            KalturaKalturaSharepointExtensionClientPlugin.instance = KalturaKalturaSharepointExtensionClientPlugin()
        return KalturaKalturaSharepointExtensionClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'sharepointExtension': KalturaSharepointExtensionService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
        }

    # @return string
    def getName(self):
        return 'KalturaSharepointExtension'

