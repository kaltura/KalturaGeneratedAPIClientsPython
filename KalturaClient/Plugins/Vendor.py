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
# Copyright (C) 2006-2021  Kaltura Inc.
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
    CMS_MATCHING = 3

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
            handleParticipantsMode=NotImplemented,
            zoomUserMatchingMode=NotImplemented,
            zoomUserPostfix=NotImplemented,
            zoomWebinarCategory=NotImplemented,
            enableWebinarUploads=NotImplemented,
            conversionProfileId=NotImplemented,
            jwtToken=NotImplemented,
            deletionPolicy=NotImplemented,
            enableZoomTranscription=NotImplemented,
            zoomAccountDescription=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            enableMeetingUpload=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.defaultUserId = defaultUserId

        # @var string
        self.zoomCategory = zoomCategory

        # @var string
        # @readonly
        self.accountId = accountId

        # @var KalturaNullableBoolean
        self.enableRecordingUpload = enableRecordingUpload

        # @var KalturaNullableBoolean
        self.createUserIfNotExist = createUserIfNotExist

        # @var KalturaHandleParticipantsMode
        self.handleParticipantsMode = handleParticipantsMode

        # @var KalturaZoomUsersMatching
        self.zoomUserMatchingMode = zoomUserMatchingMode

        # @var string
        self.zoomUserPostfix = zoomUserPostfix

        # @var string
        self.zoomWebinarCategory = zoomWebinarCategory

        # @var KalturaNullableBoolean
        self.enableWebinarUploads = enableWebinarUploads

        # @var int
        self.conversionProfileId = conversionProfileId

        # @var string
        self.jwtToken = jwtToken

        # @var KalturaNullableBoolean
        self.deletionPolicy = deletionPolicy

        # @var KalturaNullableBoolean
        self.enableZoomTranscription = enableZoomTranscription

        # @var string
        self.zoomAccountDescription = zoomAccountDescription

        # @var string
        self.createdAt = createdAt

        # @var string
        self.updatedAt = updatedAt

        # @var KalturaNullableBoolean
        self.enableMeetingUpload = enableMeetingUpload


    PROPERTY_LOADERS = {
        'defaultUserId': getXmlNodeText, 
        'zoomCategory': getXmlNodeText, 
        'accountId': getXmlNodeText, 
        'enableRecordingUpload': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'createUserIfNotExist': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'handleParticipantsMode': (KalturaEnumsFactory.createInt, "KalturaHandleParticipantsMode"), 
        'zoomUserMatchingMode': (KalturaEnumsFactory.createInt, "KalturaZoomUsersMatching"), 
        'zoomUserPostfix': getXmlNodeText, 
        'zoomWebinarCategory': getXmlNodeText, 
        'enableWebinarUploads': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'conversionProfileId': getXmlNodeInt, 
        'jwtToken': getXmlNodeText, 
        'deletionPolicy': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableZoomTranscription': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'zoomAccountDescription': getXmlNodeText, 
        'createdAt': getXmlNodeText, 
        'updatedAt': getXmlNodeText, 
        'enableMeetingUpload': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomIntegrationSetting.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaZoomIntegrationSetting")
        kparams.addStringIfDefined("defaultUserId", self.defaultUserId)
        kparams.addStringIfDefined("zoomCategory", self.zoomCategory)
        kparams.addIntEnumIfDefined("enableRecordingUpload", self.enableRecordingUpload)
        kparams.addIntEnumIfDefined("createUserIfNotExist", self.createUserIfNotExist)
        kparams.addIntEnumIfDefined("handleParticipantsMode", self.handleParticipantsMode)
        kparams.addIntEnumIfDefined("zoomUserMatchingMode", self.zoomUserMatchingMode)
        kparams.addStringIfDefined("zoomUserPostfix", self.zoomUserPostfix)
        kparams.addStringIfDefined("zoomWebinarCategory", self.zoomWebinarCategory)
        kparams.addIntEnumIfDefined("enableWebinarUploads", self.enableWebinarUploads)
        kparams.addIntIfDefined("conversionProfileId", self.conversionProfileId)
        kparams.addStringIfDefined("jwtToken", self.jwtToken)
        kparams.addIntEnumIfDefined("deletionPolicy", self.deletionPolicy)
        kparams.addIntEnumIfDefined("enableZoomTranscription", self.enableZoomTranscription)
        kparams.addStringIfDefined("zoomAccountDescription", self.zoomAccountDescription)
        kparams.addStringIfDefined("createdAt", self.createdAt)
        kparams.addStringIfDefined("updatedAt", self.updatedAt)
        kparams.addIntEnumIfDefined("enableMeetingUpload", self.enableMeetingUpload)
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

    def getEnableRecordingUpload(self):
        return self.enableRecordingUpload

    def setEnableRecordingUpload(self, newEnableRecordingUpload):
        self.enableRecordingUpload = newEnableRecordingUpload

    def getCreateUserIfNotExist(self):
        return self.createUserIfNotExist

    def setCreateUserIfNotExist(self, newCreateUserIfNotExist):
        self.createUserIfNotExist = newCreateUserIfNotExist

    def getHandleParticipantsMode(self):
        return self.handleParticipantsMode

    def setHandleParticipantsMode(self, newHandleParticipantsMode):
        self.handleParticipantsMode = newHandleParticipantsMode

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

    def getConversionProfileId(self):
        return self.conversionProfileId

    def setConversionProfileId(self, newConversionProfileId):
        self.conversionProfileId = newConversionProfileId

    def getJwtToken(self):
        return self.jwtToken

    def setJwtToken(self, newJwtToken):
        self.jwtToken = newJwtToken

    def getDeletionPolicy(self):
        return self.deletionPolicy

    def setDeletionPolicy(self, newDeletionPolicy):
        self.deletionPolicy = newDeletionPolicy

    def getEnableZoomTranscription(self):
        return self.enableZoomTranscription

    def setEnableZoomTranscription(self, newEnableZoomTranscription):
        self.enableZoomTranscription = newEnableZoomTranscription

    def getZoomAccountDescription(self):
        return self.zoomAccountDescription

    def setZoomAccountDescription(self, newZoomAccountDescription):
        self.zoomAccountDescription = newZoomAccountDescription

    def getCreatedAt(self):
        return self.createdAt

    def setCreatedAt(self, newCreatedAt):
        self.createdAt = newCreatedAt

    def getUpdatedAt(self):
        return self.updatedAt

    def setUpdatedAt(self, newUpdatedAt):
        self.updatedAt = newUpdatedAt

    def getEnableMeetingUpload(self):
        return self.enableMeetingUpload

    def setEnableMeetingUpload(self, newEnableMeetingUpload):
        self.enableMeetingUpload = newEnableMeetingUpload


# @package Kaltura
# @subpackage Client
class KalturaZoomIntegrationSettingResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaZoomIntegrationSetting
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaZoomIntegrationSetting'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomIntegrationSettingResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaZoomIntegrationSettingResponse")
        return kparams

    def getObjects(self):
        return self.objects


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

    def get(self, partnerId):
        """Retrieve zoom integration setting object by partner id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        self.client.queueServiceActionCall("vendor_zoomvendor", "get", "KalturaZoomIntegrationSetting", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaZoomIntegrationSetting')

    def list(self, pager = NotImplemented):
        """List KalturaZoomIntegrationSetting objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("vendor_zoomvendor", "list", "KalturaZoomIntegrationSettingResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaZoomIntegrationSettingResponse')

    def localRegistrationPage(self, jwt):
        kparams = KalturaParams()
        kparams.addStringIfDefined("jwt", jwt)
        self.client.queueServiceActionCall("vendor_zoomvendor", "localRegistrationPage", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def oauthValidation(self):
        """load html page the that will ask the user for its KMC URL, derive the region of the user from it,
        	 and redirect to the registration page in the correct region, while forwarding the necessary code for registration"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("vendor_zoomvendor", "oauthValidation", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def preOauthValidation(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("vendor_zoomvendor", "preOauthValidation", "None", kparams)
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
            'KalturaZoomIntegrationSettingResponse': KalturaZoomIntegrationSettingResponse,
        }

    # @return string
    def getName(self):
        return 'vendor'

