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
class KalturaHandleParticipantsMode(object):
    ADD_AS_CO_PUBLISHERS = 0
    ADD_AS_CO_VIEWERS = 1
    IGNORE = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaZoomUsersMatching(object):
    DO_NOT_MODIFY = 0
    ADD_POSTFIX = 1
    REMOVE_POSTFIX = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaZoomIntegrationSetting(KalturaObjectBase):
    def __init__(self,
            defaultUserId=NotImplemented,
            zoomCategory=NotImplemented,
            accountId=NotImplemented,
            enableRecordingUpload=NotImplemented,
            createUserIfNotExist=NotImplemented,
            handleParticipantMode=NotImplemented,
            zoomUserMatchingMode=NotImplemented,
            zoomUserPostfix=NotImplemented,
            zoomWebinarCategory=NotImplemented,
            enableWebinarUploads=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.defaultUserId = defaultUserId

        # @var string
        self.zoomCategory = zoomCategory

        # @var string
        self.accountId = accountId

        # @var KalturaNullableBoolean
        self.enableRecordingUpload = enableRecordingUpload

        # @var KalturaNullableBoolean
        self.createUserIfNotExist = createUserIfNotExist

        # @var KalturaHandleParticipantsMode
        self.handleParticipantMode = handleParticipantMode

        # @var KalturaZoomUsersMatching
        self.zoomUserMatchingMode = zoomUserMatchingMode

        # @var string
        self.zoomUserPostfix = zoomUserPostfix

        # @var string
        self.zoomWebinarCategory = zoomWebinarCategory

        # @var KalturaNullableBoolean
        self.enableWebinarUploads = enableWebinarUploads


    PROPERTY_LOADERS = {
        'defaultUserId': getXmlNodeText, 
        'zoomCategory': getXmlNodeText, 
        'accountId': getXmlNodeText, 
        'enableRecordingUpload': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'createUserIfNotExist': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'handleParticipantMode': (KalturaEnumsFactory.createInt, "KalturaHandleParticipantsMode"), 
        'zoomUserMatchingMode': (KalturaEnumsFactory.createInt, "KalturaZoomUsersMatching"), 
        'zoomUserPostfix': getXmlNodeText, 
        'zoomWebinarCategory': getXmlNodeText, 
        'enableWebinarUploads': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomIntegrationSetting.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaZoomIntegrationSetting")
        kparams.addStringIfDefined("defaultUserId", self.defaultUserId)
        kparams.addStringIfDefined("zoomCategory", self.zoomCategory)
        kparams.addStringIfDefined("accountId", self.accountId)
        kparams.addIntEnumIfDefined("enableRecordingUpload", self.enableRecordingUpload)
        kparams.addIntEnumIfDefined("createUserIfNotExist", self.createUserIfNotExist)
        kparams.addIntEnumIfDefined("handleParticipantMode", self.handleParticipantMode)
        kparams.addIntEnumIfDefined("zoomUserMatchingMode", self.zoomUserMatchingMode)
        kparams.addStringIfDefined("zoomUserPostfix", self.zoomUserPostfix)
        kparams.addStringIfDefined("zoomWebinarCategory", self.zoomWebinarCategory)
        kparams.addIntEnumIfDefined("enableWebinarUploads", self.enableWebinarUploads)
        return kparams

    def getDefaultUserId(self):
        return self.defaultUserId

    def setDefaultUserId(self, newDefaultUserId):
        self.defaultUserId = newDefaultUserId

    def getZoomCategory(self):
        return self.zoomCategory

    def setZoomCategory(self, newZoomCategory):
        self.zoomCategory = newZoomCategory

    def getAccountId(self):
        return self.accountId

    def setAccountId(self, newAccountId):
        self.accountId = newAccountId

    def getEnableRecordingUpload(self):
        return self.enableRecordingUpload

    def setEnableRecordingUpload(self, newEnableRecordingUpload):
        self.enableRecordingUpload = newEnableRecordingUpload

    def getCreateUserIfNotExist(self):
        return self.createUserIfNotExist

    def setCreateUserIfNotExist(self, newCreateUserIfNotExist):
        self.createUserIfNotExist = newCreateUserIfNotExist

    def getHandleParticipantMode(self):
        return self.handleParticipantMode

    def setHandleParticipantMode(self, newHandleParticipantMode):
        self.handleParticipantMode = newHandleParticipantMode

    def getZoomUserMatchingMode(self):
        return self.zoomUserMatchingMode

    def setZoomUserMatchingMode(self, newZoomUserMatchingMode):
        self.zoomUserMatchingMode = newZoomUserMatchingMode

    def getZoomUserPostfix(self):
        return self.zoomUserPostfix

    def setZoomUserPostfix(self, newZoomUserPostfix):
        self.zoomUserPostfix = newZoomUserPostfix

    def getZoomWebinarCategory(self):
        return self.zoomWebinarCategory

    def setZoomWebinarCategory(self, newZoomWebinarCategory):
        self.zoomWebinarCategory = newZoomWebinarCategory

    def getEnableWebinarUploads(self):
        return self.enableWebinarUploads

    def setEnableWebinarUploads(self, newEnableWebinarUploads):
        self.enableWebinarUploads = newEnableWebinarUploads


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaZoomVendorService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def deAuthorization(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("vendor_zoomvendor", "deAuthorization", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def fetchRegistrationPage(self, tokensData, iv):
        kparams = KalturaParams()
        kparams.addStringIfDefined("tokensData", tokensData)
        kparams.addStringIfDefined("iv", iv)
        self.client.queueServiceActionCall("vendor_zoomvendor", "fetchRegistrationPage", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def oauthValidation(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("vendor_zoomvendor", "oauthValidation", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def recordingComplete(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("vendor_zoomvendor", "recordingComplete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def submitRegistration(self, accountId, integrationSetting):
        kparams = KalturaParams()
        kparams.addStringIfDefined("accountId", accountId)
        kparams.addObjectIfDefined("integrationSetting", integrationSetting)
        self.client.queueServiceActionCall("vendor_zoomvendor", "submitRegistration", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaVendorClientPlugin(KalturaClientPlugin):
    # KalturaVendorClientPlugin
    instance = None

    # @return KalturaVendorClientPlugin
    @staticmethod
    def get():
        if KalturaVendorClientPlugin.instance == None:
            KalturaVendorClientPlugin.instance = KalturaVendorClientPlugin()
        return KalturaVendorClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'zoomVendor': KalturaZoomVendorService,
        }

    def getEnums(self):
        return {
            'KalturaHandleParticipantsMode': KalturaHandleParticipantsMode,
            'KalturaZoomUsersMatching': KalturaZoomUsersMatching,
        }

    def getTypes(self):
        return {
            'KalturaZoomIntegrationSetting': KalturaZoomIntegrationSetting,
        }

    # @return string
    def getName(self):
        return 'vendor'

