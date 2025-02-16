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
class KalturaHandleParticipantsMode(object):
    ADD_AS_CO_PUBLISHERS = 0
    ADD_AS_CO_VIEWERS = 1
    IGNORE = 2
    ADD_AS_CO_EDITORS = 3
    ADD_AS_CO_EDITORS_CO_PUBLISHERS = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingFileType(object):
    UNDEFINED = 0
    VIDEO = 1
    CHAT = 2
    TRANSCRIPT = 3
    AUDIO = 4
    CC = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingType(object):
    MEETING = 0
    WEBINAR = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorIntegrationStatus(object):
    DISABLED = 1
    ACTIVE = 2
    DELETED = 3

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
class KalturaEndpointValidationResponse(KalturaObjectBase):
    def __init__(self,
            plainToken = NotImplemented,
            encryptedToken = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var str
        self.plainToken = plainToken

        # @var str
        self.encryptedToken = encryptedToken


    PROPERTY_LOADERS = {
        'plainToken': getXmlNodeText, 
        'encryptedToken': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEndpointValidationResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEndpointValidationResponse")
        kparams.addStringIfDefined("plainToken", self.plainToken)
        kparams.addStringIfDefined("encryptedToken", self.encryptedToken)
        return kparams

    def getPlainToken(self):
        return self.plainToken

    def setPlainToken(self, newPlainToken):
        self.plainToken = newPlainToken

    def getEncryptedToken(self):
        return self.encryptedToken

    def setEncryptedToken(self, newEncryptedToken):
        self.encryptedToken = newEncryptedToken


# @package Kaltura
# @subpackage Client
class KalturaIntegrationSetting(KalturaObjectBase):
    def __init__(self,
            id = NotImplemented,
            status = NotImplemented,
            defaultUserId = NotImplemented,
            accountId = NotImplemented,
            createUserIfNotExist = NotImplemented,
            conversionProfileId = NotImplemented,
            handleParticipantsMode = NotImplemented,
            deletionPolicy = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            partnerId = NotImplemented,
            enableMeetingUpload = NotImplemented,
            enableMeetingChat = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var KalturaVendorIntegrationStatus
        # @readonly
        self.status = status

        # @var str
        self.defaultUserId = defaultUserId

        # @var str
        # @readonly
        self.accountId = accountId

        # @var KalturaNullableBoolean
        self.createUserIfNotExist = createUserIfNotExist

        # @var int
        self.conversionProfileId = conversionProfileId

        # @var KalturaHandleParticipantsMode
        self.handleParticipantsMode = handleParticipantsMode

        # @var KalturaNullableBoolean
        self.deletionPolicy = deletionPolicy

        # @var str
        # @readonly
        self.createdAt = createdAt

        # @var str
        # @readonly
        self.updatedAt = updatedAt

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var KalturaNullableBoolean
        self.enableMeetingUpload = enableMeetingUpload

        # @var KalturaNullableBoolean
        self.enableMeetingChat = enableMeetingChat


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaVendorIntegrationStatus"), 
        'defaultUserId': getXmlNodeText, 
        'accountId': getXmlNodeText, 
        'createUserIfNotExist': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'conversionProfileId': getXmlNodeInt, 
        'handleParticipantsMode': (KalturaEnumsFactory.createInt, "KalturaHandleParticipantsMode"), 
        'deletionPolicy': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'createdAt': getXmlNodeText, 
        'updatedAt': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'enableMeetingUpload': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableMeetingChat': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaIntegrationSetting.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaIntegrationSetting")
        kparams.addStringIfDefined("defaultUserId", self.defaultUserId)
        kparams.addIntEnumIfDefined("createUserIfNotExist", self.createUserIfNotExist)
        kparams.addIntIfDefined("conversionProfileId", self.conversionProfileId)
        kparams.addIntEnumIfDefined("handleParticipantsMode", self.handleParticipantsMode)
        kparams.addIntEnumIfDefined("deletionPolicy", self.deletionPolicy)
        kparams.addIntEnumIfDefined("enableMeetingUpload", self.enableMeetingUpload)
        kparams.addIntEnumIfDefined("enableMeetingChat", self.enableMeetingChat)
        return kparams

    def getId(self):
        return self.id

    def getStatus(self):
        return self.status

    def getDefaultUserId(self):
        return self.defaultUserId

    def setDefaultUserId(self, newDefaultUserId):
        self.defaultUserId = newDefaultUserId

    def getAccountId(self):
        return self.accountId

    def getCreateUserIfNotExist(self):
        return self.createUserIfNotExist

    def setCreateUserIfNotExist(self, newCreateUserIfNotExist):
        self.createUserIfNotExist = newCreateUserIfNotExist

    def getConversionProfileId(self):
        return self.conversionProfileId

    def setConversionProfileId(self, newConversionProfileId):
        self.conversionProfileId = newConversionProfileId

    def getHandleParticipantsMode(self):
        return self.handleParticipantsMode

    def setHandleParticipantsMode(self, newHandleParticipantsMode):
        self.handleParticipantsMode = newHandleParticipantsMode

    def getDeletionPolicy(self):
        return self.deletionPolicy

    def setDeletionPolicy(self, newDeletionPolicy):
        self.deletionPolicy = newDeletionPolicy

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getPartnerId(self):
        return self.partnerId

    def getEnableMeetingUpload(self):
        return self.enableMeetingUpload

    def setEnableMeetingUpload(self, newEnableMeetingUpload):
        self.enableMeetingUpload = newEnableMeetingUpload

    def getEnableMeetingChat(self):
        return self.enableMeetingChat

    def setEnableMeetingChat(self, newEnableMeetingChat):
        self.enableMeetingChat = newEnableMeetingChat


# @package Kaltura
# @subpackage Client
class KalturaZoomIntegrationSetting(KalturaIntegrationSetting):
    def __init__(self,
            id = NotImplemented,
            status = NotImplemented,
            defaultUserId = NotImplemented,
            accountId = NotImplemented,
            createUserIfNotExist = NotImplemented,
            conversionProfileId = NotImplemented,
            handleParticipantsMode = NotImplemented,
            deletionPolicy = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            partnerId = NotImplemented,
            enableMeetingUpload = NotImplemented,
            enableMeetingChat = NotImplemented,
            zoomCategory = NotImplemented,
            enableRecordingUpload = NotImplemented,
            zoomUserMatchingMode = NotImplemented,
            zoomUserPostfix = NotImplemented,
            zoomWebinarCategory = NotImplemented,
            enableWebinarUploads = NotImplemented,
            enableZoomTranscription = NotImplemented,
            zoomAccountDescription = NotImplemented,
            optOutGroupNames = NotImplemented,
            optInGroupNames = NotImplemented,
            groupParticipationType = NotImplemented,
            handleCohostsMode = NotImplemented,
            handleAlternativeHostsMode = NotImplemented):
        KalturaIntegrationSetting.__init__(self,
            id,
            status,
            defaultUserId,
            accountId,
            createUserIfNotExist,
            conversionProfileId,
            handleParticipantsMode,
            deletionPolicy,
            createdAt,
            updatedAt,
            partnerId,
            enableMeetingUpload,
            enableMeetingChat)

        # @var str
        self.zoomCategory = zoomCategory

        # @var KalturaNullableBoolean
        self.enableRecordingUpload = enableRecordingUpload

        # @var KalturaZoomUsersMatching
        self.zoomUserMatchingMode = zoomUserMatchingMode

        # @var str
        self.zoomUserPostfix = zoomUserPostfix

        # @var str
        self.zoomWebinarCategory = zoomWebinarCategory

        # @var KalturaNullableBoolean
        self.enableWebinarUploads = enableWebinarUploads

        # @var KalturaNullableBoolean
        self.enableZoomTranscription = enableZoomTranscription

        # @var str
        self.zoomAccountDescription = zoomAccountDescription

        # @var str
        self.optOutGroupNames = optOutGroupNames

        # @var str
        self.optInGroupNames = optInGroupNames

        # @var KalturaZoomGroupParticipationType
        self.groupParticipationType = groupParticipationType

        # @var KalturaHandleParticipantsMode
        self.handleCohostsMode = handleCohostsMode

        # @var KalturaHandleParticipantsMode
        self.handleAlternativeHostsMode = handleAlternativeHostsMode


    PROPERTY_LOADERS = {
        'zoomCategory': getXmlNodeText, 
        'enableRecordingUpload': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'zoomUserMatchingMode': (KalturaEnumsFactory.createInt, "KalturaZoomUsersMatching"), 
        'zoomUserPostfix': getXmlNodeText, 
        'zoomWebinarCategory': getXmlNodeText, 
        'enableWebinarUploads': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableZoomTranscription': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'zoomAccountDescription': getXmlNodeText, 
        'optOutGroupNames': getXmlNodeText, 
        'optInGroupNames': getXmlNodeText, 
        'groupParticipationType': (KalturaEnumsFactory.createInt, "KalturaZoomGroupParticipationType"), 
        'handleCohostsMode': (KalturaEnumsFactory.createInt, "KalturaHandleParticipantsMode"), 
        'handleAlternativeHostsMode': (KalturaEnumsFactory.createInt, "KalturaHandleParticipantsMode"), 
    }

    def fromXml(self, node):
        KalturaIntegrationSetting.fromXml(self, node)
        self.fromXmlImpl(node, KalturaZoomIntegrationSetting.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaIntegrationSetting.toParams(self)
        kparams.put("objectType", "KalturaZoomIntegrationSetting")
        kparams.addStringIfDefined("zoomCategory", self.zoomCategory)
        kparams.addIntEnumIfDefined("enableRecordingUpload", self.enableRecordingUpload)
        kparams.addIntEnumIfDefined("zoomUserMatchingMode", self.zoomUserMatchingMode)
        kparams.addStringIfDefined("zoomUserPostfix", self.zoomUserPostfix)
        kparams.addStringIfDefined("zoomWebinarCategory", self.zoomWebinarCategory)
        kparams.addIntEnumIfDefined("enableWebinarUploads", self.enableWebinarUploads)
        kparams.addIntEnumIfDefined("enableZoomTranscription", self.enableZoomTranscription)
        kparams.addStringIfDefined("zoomAccountDescription", self.zoomAccountDescription)
        kparams.addStringIfDefined("optOutGroupNames", self.optOutGroupNames)
        kparams.addStringIfDefined("optInGroupNames", self.optInGroupNames)
        kparams.addIntEnumIfDefined("groupParticipationType", self.groupParticipationType)
        kparams.addIntEnumIfDefined("handleCohostsMode", self.handleCohostsMode)
        kparams.addIntEnumIfDefined("handleAlternativeHostsMode", self.handleAlternativeHostsMode)
        return kparams

    def getZoomCategory(self):
        return self.zoomCategory

    def setZoomCategory(self, newZoomCategory):
        self.zoomCategory = newZoomCategory

    def getEnableRecordingUpload(self):
        return self.enableRecordingUpload

    def setEnableRecordingUpload(self, newEnableRecordingUpload):
        self.enableRecordingUpload = newEnableRecordingUpload

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

    def getEnableZoomTranscription(self):
        return self.enableZoomTranscription

    def setEnableZoomTranscription(self, newEnableZoomTranscription):
        self.enableZoomTranscription = newEnableZoomTranscription

    def getZoomAccountDescription(self):
        return self.zoomAccountDescription

    def setZoomAccountDescription(self, newZoomAccountDescription):
        self.zoomAccountDescription = newZoomAccountDescription

    def getOptOutGroupNames(self):
        return self.optOutGroupNames

    def setOptOutGroupNames(self, newOptOutGroupNames):
        self.optOutGroupNames = newOptOutGroupNames

    def getOptInGroupNames(self):
        return self.optInGroupNames

    def setOptInGroupNames(self, newOptInGroupNames):
        self.optInGroupNames = newOptInGroupNames

    def getGroupParticipationType(self):
        return self.groupParticipationType

    def setGroupParticipationType(self, newGroupParticipationType):
        self.groupParticipationType = newGroupParticipationType

    def getHandleCohostsMode(self):
        return self.handleCohostsMode

    def setHandleCohostsMode(self, newHandleCohostsMode):
        self.handleCohostsMode = newHandleCohostsMode

    def getHandleAlternativeHostsMode(self):
        return self.handleAlternativeHostsMode

    def setHandleAlternativeHostsMode(self, newHandleAlternativeHostsMode):
        self.handleAlternativeHostsMode = newHandleAlternativeHostsMode


# @package Kaltura
# @subpackage Client
class KalturaZoomIntegrationSettingResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaZoomIntegrationSetting]
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

    def localRegistrationPage(self, zoomAccountId):
        kparams = KalturaParams()
        kparams.addStringIfDefined("zoomAccountId", zoomAccountId)
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
        self.client.queueServiceActionCall("vendor_zoomvendor", "recordingComplete", "KalturaEndpointValidationResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEndpointValidationResponse')

    def submitRegistration(self, accountId, integrationSetting):
        kparams = KalturaParams()
        kparams.addStringIfDefined("accountId", accountId)
        kparams.addObjectIfDefined("integrationSetting", integrationSetting)
        self.client.queueServiceActionCall("vendor_zoomvendor", "submitRegistration", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaVendorIntegrationService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, integration, remoteId):
        """Add new integration setting object"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("integration", integration)
        kparams.addStringIfDefined("remoteId", remoteId)
        self.client.queueServiceActionCall("vendor_vendorintegration", "add", "KalturaIntegrationSetting", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaIntegrationSetting')

    def delete(self, integrationId):
        """Delete integration object by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("integrationId", integrationId);
        self.client.queueServiceActionCall("vendor_vendorintegration", "delete", "KalturaIntegrationSetting", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaIntegrationSetting')

    def get(self, integrationId):
        """Retrieve integration setting object by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("integrationId", integrationId);
        self.client.queueServiceActionCall("vendor_vendorintegration", "get", "KalturaIntegrationSetting", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaIntegrationSetting')

    def update(self, id, integrationSetting):
        """Update an existing vedor catalog item object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("integrationSetting", integrationSetting)
        self.client.queueServiceActionCall("vendor_vendorintegration", "update", "KalturaIntegrationSetting", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaIntegrationSetting')

    def updateStatus(self, id, status):
        """Update vendor catalog item status by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("status", status);
        self.client.queueServiceActionCall("vendor_vendorintegration", "updateStatus", "KalturaIntegrationSetting", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaIntegrationSetting')

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
            'vendorIntegration': KalturaVendorIntegrationService,
        }

    def getEnums(self):
        return {
            'KalturaHandleParticipantsMode': KalturaHandleParticipantsMode,
            'KalturaRecordingFileType': KalturaRecordingFileType,
            'KalturaRecordingType': KalturaRecordingType,
            'KalturaVendorIntegrationStatus': KalturaVendorIntegrationStatus,
            'KalturaZoomUsersMatching': KalturaZoomUsersMatching,
        }

    def getTypes(self):
        return {
            'KalturaEndpointValidationResponse': KalturaEndpointValidationResponse,
            'KalturaIntegrationSetting': KalturaIntegrationSetting,
            'KalturaZoomIntegrationSetting': KalturaZoomIntegrationSetting,
            'KalturaZoomIntegrationSettingResponse': KalturaZoomIntegrationSettingResponse,
        }

    # @return string
    def getName(self):
        return 'vendor'

