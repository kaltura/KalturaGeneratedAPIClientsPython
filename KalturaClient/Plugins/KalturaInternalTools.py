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
# @package Kaltura
# @subpackage Client
class KalturaInternalToolsSession(KalturaObjectBase):
    def __init__(self,
            partner_id=NotImplemented,
            valid_until=NotImplemented,
            partner_pattern=NotImplemented,
            type=NotImplemented,
            error=NotImplemented,
            rand=NotImplemented,
            user=NotImplemented,
            privileges=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.partner_id = partner_id

        # @var int
        self.valid_until = valid_until

        # @var string
        self.partner_pattern = partner_pattern

        # @var KalturaSessionType
        self.type = type

        # @var string
        self.error = error

        # @var int
        self.rand = rand

        # @var string
        self.user = user

        # @var string
        self.privileges = privileges


    PROPERTY_LOADERS = {
        'partner_id': getXmlNodeInt, 
        'valid_until': getXmlNodeInt, 
        'partner_pattern': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createInt, "KalturaSessionType"), 
        'error': getXmlNodeText, 
        'rand': getXmlNodeInt, 
        'user': getXmlNodeText, 
        'privileges': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInternalToolsSession.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaInternalToolsSession")
        kparams.addIntIfDefined("partner_id", self.partner_id)
        kparams.addIntIfDefined("valid_until", self.valid_until)
        kparams.addStringIfDefined("partner_pattern", self.partner_pattern)
        kparams.addIntEnumIfDefined("type", self.type)
        kparams.addStringIfDefined("error", self.error)
        kparams.addIntIfDefined("rand", self.rand)
        kparams.addStringIfDefined("user", self.user)
        kparams.addStringIfDefined("privileges", self.privileges)
        return kparams

    def getPartner_id(self):
        return self.partner_id

    def setPartner_id(self, newPartner_id):
        self.partner_id = newPartner_id

    def getValid_until(self):
        return self.valid_until

    def setValid_until(self, newValid_until):
        self.valid_until = newValid_until

    def getPartner_pattern(self):
        return self.partner_pattern

    def setPartner_pattern(self, newPartner_pattern):
        self.partner_pattern = newPartner_pattern

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getError(self):
        return self.error

    def setError(self, newError):
        self.error = newError

    def getRand(self):
        return self.rand

    def setRand(self, newRand):
        self.rand = newRand

    def getUser(self):
        return self.user

    def setUser(self, newUser):
        self.user = newUser

    def getPrivileges(self):
        return self.privileges

    def setPrivileges(self, newPrivileges):
        self.privileges = newPrivileges


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaKalturaInternalToolsSystemHelperService(KalturaServiceBase):
    """Internal Tools Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def fromSecureString(self, str):
        """KS from Secure String"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("str", str)
        self.client.queueServiceActionCall("kalturainternaltools_kalturainternaltoolssystemhelper", "fromSecureString", KalturaInternalToolsSession, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaInternalToolsSession)

    def iptocountry(self, remote_addr):
        """from ip to country"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("remote_addr", remote_addr)
        self.client.queueServiceActionCall("kalturainternaltools_kalturainternaltoolssystemhelper", "iptocountry", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def getRemoteAddress(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("kalturainternaltools_kalturainternaltoolssystemhelper", "getRemoteAddress", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaKalturaInternalToolsClientPlugin(KalturaClientPlugin):
    # KalturaKalturaInternalToolsClientPlugin
    instance = None

    # @return KalturaKalturaInternalToolsClientPlugin
    @staticmethod
    def get():
        if KalturaKalturaInternalToolsClientPlugin.instance == None:
            KalturaKalturaInternalToolsClientPlugin.instance = KalturaKalturaInternalToolsClientPlugin()
        return KalturaKalturaInternalToolsClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'KalturaInternalToolsSystemHelper': KalturaKalturaInternalToolsSystemHelperService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaInternalToolsSession': KalturaInternalToolsSession,
        }

    # @return string
    def getName(self):
        return 'KalturaInternalTools'

