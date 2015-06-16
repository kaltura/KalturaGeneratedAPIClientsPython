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
# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerLimitType(object):
    ACCESS_CONTROLS = "ACCESS_CONTROLS"
    ADMIN_LOGIN_USERS = "ADMIN_LOGIN_USERS"
    BULK_SIZE = "BULK_SIZE"
    END_USERS = "END_USERS"
    ENTRIES = "ENTRIES"
    LIVE_STREAM_INPUTS = "LIVE_STREAM_INPUTS"
    LIVE_STREAM_OUTPUTS = "LIVE_STREAM_OUTPUTS"
    LOGIN_USERS = "LOGIN_USERS"
    MONTHLY_BANDWIDTH = "MONTHLY_BANDWIDTH"
    MONTHLY_STORAGE = "MONTHLY_STORAGE"
    MONTHLY_STORAGE_AND_BANDWIDTH = "MONTHLY_STORAGE_AND_BANDWIDTH"
    MONTHLY_STREAM_ENTRIES = "MONTHLY_STREAM_ENTRIES"
    PUBLISHERS = "PUBLISHERS"
    USER_LOGIN_ATTEMPTS = "USER_LOGIN_ATTEMPTS"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerLimit(KalturaObjectBase):
    def __init__(self,
            type=NotImplemented,
            max=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaSystemPartnerLimitType
        self.type = type

        # @var float
        self.max = max


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createString, "KalturaSystemPartnerLimitType"), 
        'max': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerLimit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerLimit")
        kparams.addStringEnumIfDefined("type", self.type)
        kparams.addFloatIfDefined("max", self.max)
        return kparams

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getMax(self):
        return self.max

    def setMax(self, newMax):
        self.max = newMax


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerConfiguration(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerName=NotImplemented,
            description=NotImplemented,
            adminName=NotImplemented,
            adminEmail=NotImplemented,
            host=NotImplemented,
            cdnHost=NotImplemented,
            cdnHostWhiteList=NotImplemented,
            thumbnailHost=NotImplemented,
            partnerPackage=NotImplemented,
            monitorUsage=NotImplemented,
            moderateContent=NotImplemented,
            storageDeleteFromKaltura=NotImplemented,
            storageServePriority=NotImplemented,
            kmcVersion=NotImplemented,
            restrictThumbnailByKs=NotImplemented,
            supportAnimatedThumbnails=NotImplemented,
            defThumbOffset=NotImplemented,
            defThumbDensity=NotImplemented,
            userSessionRoleId=NotImplemented,
            adminSessionRoleId=NotImplemented,
            alwaysAllowedPermissionNames=NotImplemented,
            importRemoteSourceForConvert=NotImplemented,
            permissions=NotImplemented,
            notificationsConfig=NotImplemented,
            allowMultiNotification=NotImplemented,
            loginBlockPeriod=NotImplemented,
            numPrevPassToKeep=NotImplemented,
            passReplaceFreq=NotImplemented,
            isFirstLogin=NotImplemented,
            partnerGroupType=NotImplemented,
            partnerParentId=NotImplemented,
            limits=NotImplemented,
            streamerType=NotImplemented,
            mediaProtocol=NotImplemented,
            extendedFreeTrailExpiryReason=NotImplemented,
            extendedFreeTrailExpiryDate=NotImplemented,
            extendedFreeTrail=NotImplemented,
            crmId=NotImplemented,
            referenceId=NotImplemented,
            crmLink=NotImplemented,
            verticalClasiffication=NotImplemented,
            partnerPackageClassOfService=NotImplemented,
            enableBulkUploadNotificationsEmails=NotImplemented,
            deliveryProfileIds=NotImplemented,
            enforceDelivery=NotImplemented,
            bulkUploadNotificationsEmail=NotImplemented,
            internalUse=NotImplemented,
            defaultLiveStreamEntrySourceType=NotImplemented,
            liveStreamProvisionParams=NotImplemented,
            autoModerateEntryFilter=NotImplemented,
            logoutUrl=NotImplemented,
            defaultEntitlementEnforcement=NotImplemented,
            cacheFlavorVersion=NotImplemented,
            apiAccessControlId=NotImplemented,
            defaultDeliveryType=NotImplemented,
            defaultEmbedCodeType=NotImplemented,
            customDeliveryTypes=NotImplemented,
            restrictEntryByMetadata=NotImplemented,
            language=NotImplemented,
            audioThumbEntryId=NotImplemented,
            liveThumbEntryId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var string
        self.partnerName = partnerName

        # @var string
        self.description = description

        # @var string
        self.adminName = adminName

        # @var string
        self.adminEmail = adminEmail

        # @var string
        self.host = host

        # @var string
        self.cdnHost = cdnHost

        # @var string
        self.cdnHostWhiteList = cdnHostWhiteList

        # @var string
        self.thumbnailHost = thumbnailHost

        # @var int
        self.partnerPackage = partnerPackage

        # @var int
        self.monitorUsage = monitorUsage

        # @var bool
        self.moderateContent = moderateContent

        # @var bool
        self.storageDeleteFromKaltura = storageDeleteFromKaltura

        # @var KalturaStorageServePriority
        self.storageServePriority = storageServePriority

        # @var int
        self.kmcVersion = kmcVersion

        # @var int
        self.restrictThumbnailByKs = restrictThumbnailByKs

        # @var bool
        self.supportAnimatedThumbnails = supportAnimatedThumbnails

        # @var int
        self.defThumbOffset = defThumbOffset

        # @var int
        self.defThumbDensity = defThumbDensity

        # @var int
        self.userSessionRoleId = userSessionRoleId

        # @var int
        self.adminSessionRoleId = adminSessionRoleId

        # @var string
        self.alwaysAllowedPermissionNames = alwaysAllowedPermissionNames

        # @var bool
        self.importRemoteSourceForConvert = importRemoteSourceForConvert

        # @var array of KalturaPermission
        self.permissions = permissions

        # @var string
        self.notificationsConfig = notificationsConfig

        # @var bool
        self.allowMultiNotification = allowMultiNotification

        # @var int
        self.loginBlockPeriod = loginBlockPeriod

        # @var int
        self.numPrevPassToKeep = numPrevPassToKeep

        # @var int
        self.passReplaceFreq = passReplaceFreq

        # @var bool
        self.isFirstLogin = isFirstLogin

        # @var KalturaPartnerGroupType
        self.partnerGroupType = partnerGroupType

        # @var int
        self.partnerParentId = partnerParentId

        # @var array of KalturaSystemPartnerLimit
        self.limits = limits

        # http/rtmp/hdnetwork
        # @var string
        self.streamerType = streamerType

        # http/https, rtmp/rtmpe
        # @var string
        self.mediaProtocol = mediaProtocol

        # @var string
        self.extendedFreeTrailExpiryReason = extendedFreeTrailExpiryReason

        # Unix timestamp (In seconds)
        # @var int
        self.extendedFreeTrailExpiryDate = extendedFreeTrailExpiryDate

        # @var int
        self.extendedFreeTrail = extendedFreeTrail

        # @var string
        self.crmId = crmId

        # @var string
        self.referenceId = referenceId

        # @var string
        self.crmLink = crmLink

        # @var string
        self.verticalClasiffication = verticalClasiffication

        # @var string
        self.partnerPackageClassOfService = partnerPackageClassOfService

        # @var bool
        self.enableBulkUploadNotificationsEmails = enableBulkUploadNotificationsEmails

        # @var string
        self.deliveryProfileIds = deliveryProfileIds

        # @var bool
        self.enforceDelivery = enforceDelivery

        # @var string
        self.bulkUploadNotificationsEmail = bulkUploadNotificationsEmail

        # @var bool
        self.internalUse = internalUse

        # @var KalturaSourceType
        self.defaultLiveStreamEntrySourceType = defaultLiveStreamEntrySourceType

        # @var string
        self.liveStreamProvisionParams = liveStreamProvisionParams

        # @var KalturaBaseEntryFilter
        self.autoModerateEntryFilter = autoModerateEntryFilter

        # @var string
        self.logoutUrl = logoutUrl

        # @var bool
        self.defaultEntitlementEnforcement = defaultEntitlementEnforcement

        # @var int
        self.cacheFlavorVersion = cacheFlavorVersion

        # @var int
        self.apiAccessControlId = apiAccessControlId

        # @var string
        self.defaultDeliveryType = defaultDeliveryType

        # @var string
        self.defaultEmbedCodeType = defaultEmbedCodeType

        # @var array of KalturaKeyBooleanValue
        self.customDeliveryTypes = customDeliveryTypes

        # @var bool
        self.restrictEntryByMetadata = restrictEntryByMetadata

        # @var KalturaLanguageCode
        self.language = language

        # @var string
        self.audioThumbEntryId = audioThumbEntryId

        # @var string
        self.liveThumbEntryId = liveThumbEntryId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'adminName': getXmlNodeText, 
        'adminEmail': getXmlNodeText, 
        'host': getXmlNodeText, 
        'cdnHost': getXmlNodeText, 
        'cdnHostWhiteList': getXmlNodeText, 
        'thumbnailHost': getXmlNodeText, 
        'partnerPackage': getXmlNodeInt, 
        'monitorUsage': getXmlNodeInt, 
        'moderateContent': getXmlNodeBool, 
        'storageDeleteFromKaltura': getXmlNodeBool, 
        'storageServePriority': (KalturaEnumsFactory.createInt, "KalturaStorageServePriority"), 
        'kmcVersion': getXmlNodeInt, 
        'restrictThumbnailByKs': getXmlNodeInt, 
        'supportAnimatedThumbnails': getXmlNodeBool, 
        'defThumbOffset': getXmlNodeInt, 
        'defThumbDensity': getXmlNodeInt, 
        'userSessionRoleId': getXmlNodeInt, 
        'adminSessionRoleId': getXmlNodeInt, 
        'alwaysAllowedPermissionNames': getXmlNodeText, 
        'importRemoteSourceForConvert': getXmlNodeBool, 
        'permissions': (KalturaObjectFactory.createArray, KalturaPermission), 
        'notificationsConfig': getXmlNodeText, 
        'allowMultiNotification': getXmlNodeBool, 
        'loginBlockPeriod': getXmlNodeInt, 
        'numPrevPassToKeep': getXmlNodeInt, 
        'passReplaceFreq': getXmlNodeInt, 
        'isFirstLogin': getXmlNodeBool, 
        'partnerGroupType': (KalturaEnumsFactory.createInt, "KalturaPartnerGroupType"), 
        'partnerParentId': getXmlNodeInt, 
        'limits': (KalturaObjectFactory.createArray, KalturaSystemPartnerLimit), 
        'streamerType': getXmlNodeText, 
        'mediaProtocol': getXmlNodeText, 
        'extendedFreeTrailExpiryReason': getXmlNodeText, 
        'extendedFreeTrailExpiryDate': getXmlNodeInt, 
        'extendedFreeTrail': getXmlNodeInt, 
        'crmId': getXmlNodeText, 
        'referenceId': getXmlNodeText, 
        'crmLink': getXmlNodeText, 
        'verticalClasiffication': getXmlNodeText, 
        'partnerPackageClassOfService': getXmlNodeText, 
        'enableBulkUploadNotificationsEmails': getXmlNodeBool, 
        'deliveryProfileIds': getXmlNodeText, 
        'enforceDelivery': getXmlNodeBool, 
        'bulkUploadNotificationsEmail': getXmlNodeText, 
        'internalUse': getXmlNodeBool, 
        'defaultLiveStreamEntrySourceType': (KalturaEnumsFactory.createString, "KalturaSourceType"), 
        'liveStreamProvisionParams': getXmlNodeText, 
        'autoModerateEntryFilter': (KalturaObjectFactory.create, KalturaBaseEntryFilter), 
        'logoutUrl': getXmlNodeText, 
        'defaultEntitlementEnforcement': getXmlNodeBool, 
        'cacheFlavorVersion': getXmlNodeInt, 
        'apiAccessControlId': getXmlNodeInt, 
        'defaultDeliveryType': getXmlNodeText, 
        'defaultEmbedCodeType': getXmlNodeText, 
        'customDeliveryTypes': (KalturaObjectFactory.createArray, KalturaKeyBooleanValue), 
        'restrictEntryByMetadata': getXmlNodeBool, 
        'language': (KalturaEnumsFactory.createString, "KalturaLanguageCode"), 
        'audioThumbEntryId': getXmlNodeText, 
        'liveThumbEntryId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerConfiguration.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerConfiguration")
        kparams.addStringIfDefined("partnerName", self.partnerName)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("adminName", self.adminName)
        kparams.addStringIfDefined("adminEmail", self.adminEmail)
        kparams.addStringIfDefined("host", self.host)
        kparams.addStringIfDefined("cdnHost", self.cdnHost)
        kparams.addStringIfDefined("cdnHostWhiteList", self.cdnHostWhiteList)
        kparams.addStringIfDefined("thumbnailHost", self.thumbnailHost)
        kparams.addIntIfDefined("partnerPackage", self.partnerPackage)
        kparams.addIntIfDefined("monitorUsage", self.monitorUsage)
        kparams.addBoolIfDefined("moderateContent", self.moderateContent)
        kparams.addBoolIfDefined("storageDeleteFromKaltura", self.storageDeleteFromKaltura)
        kparams.addIntEnumIfDefined("storageServePriority", self.storageServePriority)
        kparams.addIntIfDefined("kmcVersion", self.kmcVersion)
        kparams.addIntIfDefined("restrictThumbnailByKs", self.restrictThumbnailByKs)
        kparams.addBoolIfDefined("supportAnimatedThumbnails", self.supportAnimatedThumbnails)
        kparams.addIntIfDefined("defThumbOffset", self.defThumbOffset)
        kparams.addIntIfDefined("defThumbDensity", self.defThumbDensity)
        kparams.addIntIfDefined("userSessionRoleId", self.userSessionRoleId)
        kparams.addIntIfDefined("adminSessionRoleId", self.adminSessionRoleId)
        kparams.addStringIfDefined("alwaysAllowedPermissionNames", self.alwaysAllowedPermissionNames)
        kparams.addBoolIfDefined("importRemoteSourceForConvert", self.importRemoteSourceForConvert)
        kparams.addArrayIfDefined("permissions", self.permissions)
        kparams.addStringIfDefined("notificationsConfig", self.notificationsConfig)
        kparams.addBoolIfDefined("allowMultiNotification", self.allowMultiNotification)
        kparams.addIntIfDefined("loginBlockPeriod", self.loginBlockPeriod)
        kparams.addIntIfDefined("numPrevPassToKeep", self.numPrevPassToKeep)
        kparams.addIntIfDefined("passReplaceFreq", self.passReplaceFreq)
        kparams.addBoolIfDefined("isFirstLogin", self.isFirstLogin)
        kparams.addIntEnumIfDefined("partnerGroupType", self.partnerGroupType)
        kparams.addIntIfDefined("partnerParentId", self.partnerParentId)
        kparams.addArrayIfDefined("limits", self.limits)
        kparams.addStringIfDefined("streamerType", self.streamerType)
        kparams.addStringIfDefined("mediaProtocol", self.mediaProtocol)
        kparams.addStringIfDefined("extendedFreeTrailExpiryReason", self.extendedFreeTrailExpiryReason)
        kparams.addIntIfDefined("extendedFreeTrailExpiryDate", self.extendedFreeTrailExpiryDate)
        kparams.addIntIfDefined("extendedFreeTrail", self.extendedFreeTrail)
        kparams.addStringIfDefined("crmId", self.crmId)
        kparams.addStringIfDefined("referenceId", self.referenceId)
        kparams.addStringIfDefined("crmLink", self.crmLink)
        kparams.addStringIfDefined("verticalClasiffication", self.verticalClasiffication)
        kparams.addStringIfDefined("partnerPackageClassOfService", self.partnerPackageClassOfService)
        kparams.addBoolIfDefined("enableBulkUploadNotificationsEmails", self.enableBulkUploadNotificationsEmails)
        kparams.addStringIfDefined("deliveryProfileIds", self.deliveryProfileIds)
        kparams.addBoolIfDefined("enforceDelivery", self.enforceDelivery)
        kparams.addStringIfDefined("bulkUploadNotificationsEmail", self.bulkUploadNotificationsEmail)
        kparams.addBoolIfDefined("internalUse", self.internalUse)
        kparams.addStringEnumIfDefined("defaultLiveStreamEntrySourceType", self.defaultLiveStreamEntrySourceType)
        kparams.addStringIfDefined("liveStreamProvisionParams", self.liveStreamProvisionParams)
        kparams.addObjectIfDefined("autoModerateEntryFilter", self.autoModerateEntryFilter)
        kparams.addStringIfDefined("logoutUrl", self.logoutUrl)
        kparams.addBoolIfDefined("defaultEntitlementEnforcement", self.defaultEntitlementEnforcement)
        kparams.addIntIfDefined("cacheFlavorVersion", self.cacheFlavorVersion)
        kparams.addIntIfDefined("apiAccessControlId", self.apiAccessControlId)
        kparams.addStringIfDefined("defaultDeliveryType", self.defaultDeliveryType)
        kparams.addStringIfDefined("defaultEmbedCodeType", self.defaultEmbedCodeType)
        kparams.addArrayIfDefined("customDeliveryTypes", self.customDeliveryTypes)
        kparams.addBoolIfDefined("restrictEntryByMetadata", self.restrictEntryByMetadata)
        kparams.addStringEnumIfDefined("language", self.language)
        kparams.addStringIfDefined("audioThumbEntryId", self.audioThumbEntryId)
        kparams.addStringIfDefined("liveThumbEntryId", self.liveThumbEntryId)
        return kparams

    def getId(self):
        return self.id

    def getPartnerName(self):
        return self.partnerName

    def setPartnerName(self, newPartnerName):
        self.partnerName = newPartnerName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getAdminName(self):
        return self.adminName

    def setAdminName(self, newAdminName):
        self.adminName = newAdminName

    def getAdminEmail(self):
        return self.adminEmail

    def setAdminEmail(self, newAdminEmail):
        self.adminEmail = newAdminEmail

    def getHost(self):
        return self.host

    def setHost(self, newHost):
        self.host = newHost

    def getCdnHost(self):
        return self.cdnHost

    def setCdnHost(self, newCdnHost):
        self.cdnHost = newCdnHost

    def getCdnHostWhiteList(self):
        return self.cdnHostWhiteList

    def setCdnHostWhiteList(self, newCdnHostWhiteList):
        self.cdnHostWhiteList = newCdnHostWhiteList

    def getThumbnailHost(self):
        return self.thumbnailHost

    def setThumbnailHost(self, newThumbnailHost):
        self.thumbnailHost = newThumbnailHost

    def getPartnerPackage(self):
        return self.partnerPackage

    def setPartnerPackage(self, newPartnerPackage):
        self.partnerPackage = newPartnerPackage

    def getMonitorUsage(self):
        return self.monitorUsage

    def setMonitorUsage(self, newMonitorUsage):
        self.monitorUsage = newMonitorUsage

    def getModerateContent(self):
        return self.moderateContent

    def setModerateContent(self, newModerateContent):
        self.moderateContent = newModerateContent

    def getStorageDeleteFromKaltura(self):
        return self.storageDeleteFromKaltura

    def setStorageDeleteFromKaltura(self, newStorageDeleteFromKaltura):
        self.storageDeleteFromKaltura = newStorageDeleteFromKaltura

    def getStorageServePriority(self):
        return self.storageServePriority

    def setStorageServePriority(self, newStorageServePriority):
        self.storageServePriority = newStorageServePriority

    def getKmcVersion(self):
        return self.kmcVersion

    def setKmcVersion(self, newKmcVersion):
        self.kmcVersion = newKmcVersion

    def getRestrictThumbnailByKs(self):
        return self.restrictThumbnailByKs

    def setRestrictThumbnailByKs(self, newRestrictThumbnailByKs):
        self.restrictThumbnailByKs = newRestrictThumbnailByKs

    def getSupportAnimatedThumbnails(self):
        return self.supportAnimatedThumbnails

    def setSupportAnimatedThumbnails(self, newSupportAnimatedThumbnails):
        self.supportAnimatedThumbnails = newSupportAnimatedThumbnails

    def getDefThumbOffset(self):
        return self.defThumbOffset

    def setDefThumbOffset(self, newDefThumbOffset):
        self.defThumbOffset = newDefThumbOffset

    def getDefThumbDensity(self):
        return self.defThumbDensity

    def setDefThumbDensity(self, newDefThumbDensity):
        self.defThumbDensity = newDefThumbDensity

    def getUserSessionRoleId(self):
        return self.userSessionRoleId

    def setUserSessionRoleId(self, newUserSessionRoleId):
        self.userSessionRoleId = newUserSessionRoleId

    def getAdminSessionRoleId(self):
        return self.adminSessionRoleId

    def setAdminSessionRoleId(self, newAdminSessionRoleId):
        self.adminSessionRoleId = newAdminSessionRoleId

    def getAlwaysAllowedPermissionNames(self):
        return self.alwaysAllowedPermissionNames

    def setAlwaysAllowedPermissionNames(self, newAlwaysAllowedPermissionNames):
        self.alwaysAllowedPermissionNames = newAlwaysAllowedPermissionNames

    def getImportRemoteSourceForConvert(self):
        return self.importRemoteSourceForConvert

    def setImportRemoteSourceForConvert(self, newImportRemoteSourceForConvert):
        self.importRemoteSourceForConvert = newImportRemoteSourceForConvert

    def getPermissions(self):
        return self.permissions

    def setPermissions(self, newPermissions):
        self.permissions = newPermissions

    def getNotificationsConfig(self):
        return self.notificationsConfig

    def setNotificationsConfig(self, newNotificationsConfig):
        self.notificationsConfig = newNotificationsConfig

    def getAllowMultiNotification(self):
        return self.allowMultiNotification

    def setAllowMultiNotification(self, newAllowMultiNotification):
        self.allowMultiNotification = newAllowMultiNotification

    def getLoginBlockPeriod(self):
        return self.loginBlockPeriod

    def setLoginBlockPeriod(self, newLoginBlockPeriod):
        self.loginBlockPeriod = newLoginBlockPeriod

    def getNumPrevPassToKeep(self):
        return self.numPrevPassToKeep

    def setNumPrevPassToKeep(self, newNumPrevPassToKeep):
        self.numPrevPassToKeep = newNumPrevPassToKeep

    def getPassReplaceFreq(self):
        return self.passReplaceFreq

    def setPassReplaceFreq(self, newPassReplaceFreq):
        self.passReplaceFreq = newPassReplaceFreq

    def getIsFirstLogin(self):
        return self.isFirstLogin

    def setIsFirstLogin(self, newIsFirstLogin):
        self.isFirstLogin = newIsFirstLogin

    def getPartnerGroupType(self):
        return self.partnerGroupType

    def setPartnerGroupType(self, newPartnerGroupType):
        self.partnerGroupType = newPartnerGroupType

    def getPartnerParentId(self):
        return self.partnerParentId

    def setPartnerParentId(self, newPartnerParentId):
        self.partnerParentId = newPartnerParentId

    def getLimits(self):
        return self.limits

    def setLimits(self, newLimits):
        self.limits = newLimits

    def getStreamerType(self):
        return self.streamerType

    def setStreamerType(self, newStreamerType):
        self.streamerType = newStreamerType

    def getMediaProtocol(self):
        return self.mediaProtocol

    def setMediaProtocol(self, newMediaProtocol):
        self.mediaProtocol = newMediaProtocol

    def getExtendedFreeTrailExpiryReason(self):
        return self.extendedFreeTrailExpiryReason

    def setExtendedFreeTrailExpiryReason(self, newExtendedFreeTrailExpiryReason):
        self.extendedFreeTrailExpiryReason = newExtendedFreeTrailExpiryReason

    def getExtendedFreeTrailExpiryDate(self):
        return self.extendedFreeTrailExpiryDate

    def setExtendedFreeTrailExpiryDate(self, newExtendedFreeTrailExpiryDate):
        self.extendedFreeTrailExpiryDate = newExtendedFreeTrailExpiryDate

    def getExtendedFreeTrail(self):
        return self.extendedFreeTrail

    def setExtendedFreeTrail(self, newExtendedFreeTrail):
        self.extendedFreeTrail = newExtendedFreeTrail

    def getCrmId(self):
        return self.crmId

    def setCrmId(self, newCrmId):
        self.crmId = newCrmId

    def getReferenceId(self):
        return self.referenceId

    def setReferenceId(self, newReferenceId):
        self.referenceId = newReferenceId

    def getCrmLink(self):
        return self.crmLink

    def setCrmLink(self, newCrmLink):
        self.crmLink = newCrmLink

    def getVerticalClasiffication(self):
        return self.verticalClasiffication

    def setVerticalClasiffication(self, newVerticalClasiffication):
        self.verticalClasiffication = newVerticalClasiffication

    def getPartnerPackageClassOfService(self):
        return self.partnerPackageClassOfService

    def setPartnerPackageClassOfService(self, newPartnerPackageClassOfService):
        self.partnerPackageClassOfService = newPartnerPackageClassOfService

    def getEnableBulkUploadNotificationsEmails(self):
        return self.enableBulkUploadNotificationsEmails

    def setEnableBulkUploadNotificationsEmails(self, newEnableBulkUploadNotificationsEmails):
        self.enableBulkUploadNotificationsEmails = newEnableBulkUploadNotificationsEmails

    def getDeliveryProfileIds(self):
        return self.deliveryProfileIds

    def setDeliveryProfileIds(self, newDeliveryProfileIds):
        self.deliveryProfileIds = newDeliveryProfileIds

    def getEnforceDelivery(self):
        return self.enforceDelivery

    def setEnforceDelivery(self, newEnforceDelivery):
        self.enforceDelivery = newEnforceDelivery

    def getBulkUploadNotificationsEmail(self):
        return self.bulkUploadNotificationsEmail

    def setBulkUploadNotificationsEmail(self, newBulkUploadNotificationsEmail):
        self.bulkUploadNotificationsEmail = newBulkUploadNotificationsEmail

    def getInternalUse(self):
        return self.internalUse

    def setInternalUse(self, newInternalUse):
        self.internalUse = newInternalUse

    def getDefaultLiveStreamEntrySourceType(self):
        return self.defaultLiveStreamEntrySourceType

    def setDefaultLiveStreamEntrySourceType(self, newDefaultLiveStreamEntrySourceType):
        self.defaultLiveStreamEntrySourceType = newDefaultLiveStreamEntrySourceType

    def getLiveStreamProvisionParams(self):
        return self.liveStreamProvisionParams

    def setLiveStreamProvisionParams(self, newLiveStreamProvisionParams):
        self.liveStreamProvisionParams = newLiveStreamProvisionParams

    def getAutoModerateEntryFilter(self):
        return self.autoModerateEntryFilter

    def setAutoModerateEntryFilter(self, newAutoModerateEntryFilter):
        self.autoModerateEntryFilter = newAutoModerateEntryFilter

    def getLogoutUrl(self):
        return self.logoutUrl

    def setLogoutUrl(self, newLogoutUrl):
        self.logoutUrl = newLogoutUrl

    def getDefaultEntitlementEnforcement(self):
        return self.defaultEntitlementEnforcement

    def setDefaultEntitlementEnforcement(self, newDefaultEntitlementEnforcement):
        self.defaultEntitlementEnforcement = newDefaultEntitlementEnforcement

    def getCacheFlavorVersion(self):
        return self.cacheFlavorVersion

    def setCacheFlavorVersion(self, newCacheFlavorVersion):
        self.cacheFlavorVersion = newCacheFlavorVersion

    def getApiAccessControlId(self):
        return self.apiAccessControlId

    def setApiAccessControlId(self, newApiAccessControlId):
        self.apiAccessControlId = newApiAccessControlId

    def getDefaultDeliveryType(self):
        return self.defaultDeliveryType

    def setDefaultDeliveryType(self, newDefaultDeliveryType):
        self.defaultDeliveryType = newDefaultDeliveryType

    def getDefaultEmbedCodeType(self):
        return self.defaultEmbedCodeType

    def setDefaultEmbedCodeType(self, newDefaultEmbedCodeType):
        self.defaultEmbedCodeType = newDefaultEmbedCodeType

    def getCustomDeliveryTypes(self):
        return self.customDeliveryTypes

    def setCustomDeliveryTypes(self, newCustomDeliveryTypes):
        self.customDeliveryTypes = newCustomDeliveryTypes

    def getRestrictEntryByMetadata(self):
        return self.restrictEntryByMetadata

    def setRestrictEntryByMetadata(self, newRestrictEntryByMetadata):
        self.restrictEntryByMetadata = newRestrictEntryByMetadata

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getAudioThumbEntryId(self):
        return self.audioThumbEntryId

    def setAudioThumbEntryId(self, newAudioThumbEntryId):
        self.audioThumbEntryId = newAudioThumbEntryId

    def getLiveThumbEntryId(self):
        return self.liveThumbEntryId

    def setLiveThumbEntryId(self, newLiveThumbEntryId):
        self.liveThumbEntryId = newLiveThumbEntryId


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerPackage(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.id = id

        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerPackage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerPackage")
        kparams.addIntIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerUsageItem(KalturaObjectBase):
    def __init__(self,
            partnerId=NotImplemented,
            partnerName=NotImplemented,
            partnerStatus=NotImplemented,
            partnerPackage=NotImplemented,
            partnerCreatedAt=NotImplemented,
            views=NotImplemented,
            plays=NotImplemented,
            entriesCount=NotImplemented,
            totalEntriesCount=NotImplemented,
            videoEntriesCount=NotImplemented,
            imageEntriesCount=NotImplemented,
            audioEntriesCount=NotImplemented,
            mixEntriesCount=NotImplemented,
            bandwidth=NotImplemented,
            totalStorage=NotImplemented,
            storage=NotImplemented,
            peakStorage=NotImplemented,
            avgStorage=NotImplemented,
            combinedBandwidthStorage=NotImplemented,
            deletedStorage=NotImplemented,
            transcodingUsage=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Partner ID
        # @var int
        self.partnerId = partnerId

        # Partner name
        # @var string
        self.partnerName = partnerName

        # Partner status
        # @var KalturaPartnerStatus
        self.partnerStatus = partnerStatus

        # Partner package
        # @var int
        self.partnerPackage = partnerPackage

        # Partner creation date (Unix timestamp)
        # @var int
        self.partnerCreatedAt = partnerCreatedAt

        # Number of player loads in the specific date range
        # @var int
        self.views = views

        # Number of plays in the specific date range
        # @var int
        self.plays = plays

        # Number of new entries created during specific date range
        # @var int
        self.entriesCount = entriesCount

        # Total number of entries
        # @var int
        self.totalEntriesCount = totalEntriesCount

        # Number of new video entries created during specific date range
        # @var int
        self.videoEntriesCount = videoEntriesCount

        # Number of new image entries created during specific date range
        # @var int
        self.imageEntriesCount = imageEntriesCount

        # Number of new audio entries created during specific date range
        # @var int
        self.audioEntriesCount = audioEntriesCount

        # Number of new mix entries created during specific date range
        # @var int
        self.mixEntriesCount = mixEntriesCount

        # The total bandwidth usage during the given date range (in MB)
        # @var float
        self.bandwidth = bandwidth

        # The total storage consumption (in MB)
        # @var float
        self.totalStorage = totalStorage

        # The change in storage consumption (new uploads) during the given date range (in MB)
        # @var float
        self.storage = storage

        # The peak amount of storage consumption during the given date range for the specific publisher
        # @var float
        self.peakStorage = peakStorage

        # The average amount of storage consumption during the given date range for the specific publisher
        # @var float
        self.avgStorage = avgStorage

        # The combined amount of bandwidth and storage consumed during the given date range for the specific publisher
        # @var float
        self.combinedBandwidthStorage = combinedBandwidthStorage

        # Amount of deleted storage in MB
        # @var float
        self.deletedStorage = deletedStorage

        # Amount of transcoding usage in MB
        # @var float
        self.transcodingUsage = transcodingUsage


    PROPERTY_LOADERS = {
        'partnerId': getXmlNodeInt, 
        'partnerName': getXmlNodeText, 
        'partnerStatus': (KalturaEnumsFactory.createInt, "KalturaPartnerStatus"), 
        'partnerPackage': getXmlNodeInt, 
        'partnerCreatedAt': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'plays': getXmlNodeInt, 
        'entriesCount': getXmlNodeInt, 
        'totalEntriesCount': getXmlNodeInt, 
        'videoEntriesCount': getXmlNodeInt, 
        'imageEntriesCount': getXmlNodeInt, 
        'audioEntriesCount': getXmlNodeInt, 
        'mixEntriesCount': getXmlNodeInt, 
        'bandwidth': getXmlNodeFloat, 
        'totalStorage': getXmlNodeFloat, 
        'storage': getXmlNodeFloat, 
        'peakStorage': getXmlNodeFloat, 
        'avgStorage': getXmlNodeFloat, 
        'combinedBandwidthStorage': getXmlNodeFloat, 
        'deletedStorage': getXmlNodeFloat, 
        'transcodingUsage': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageItem")
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("partnerName", self.partnerName)
        kparams.addIntEnumIfDefined("partnerStatus", self.partnerStatus)
        kparams.addIntIfDefined("partnerPackage", self.partnerPackage)
        kparams.addIntIfDefined("partnerCreatedAt", self.partnerCreatedAt)
        kparams.addIntIfDefined("views", self.views)
        kparams.addIntIfDefined("plays", self.plays)
        kparams.addIntIfDefined("entriesCount", self.entriesCount)
        kparams.addIntIfDefined("totalEntriesCount", self.totalEntriesCount)
        kparams.addIntIfDefined("videoEntriesCount", self.videoEntriesCount)
        kparams.addIntIfDefined("imageEntriesCount", self.imageEntriesCount)
        kparams.addIntIfDefined("audioEntriesCount", self.audioEntriesCount)
        kparams.addIntIfDefined("mixEntriesCount", self.mixEntriesCount)
        kparams.addFloatIfDefined("bandwidth", self.bandwidth)
        kparams.addFloatIfDefined("totalStorage", self.totalStorage)
        kparams.addFloatIfDefined("storage", self.storage)
        kparams.addFloatIfDefined("peakStorage", self.peakStorage)
        kparams.addFloatIfDefined("avgStorage", self.avgStorage)
        kparams.addFloatIfDefined("combinedBandwidthStorage", self.combinedBandwidthStorage)
        kparams.addFloatIfDefined("deletedStorage", self.deletedStorage)
        kparams.addFloatIfDefined("transcodingUsage", self.transcodingUsage)
        return kparams

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getPartnerName(self):
        return self.partnerName

    def setPartnerName(self, newPartnerName):
        self.partnerName = newPartnerName

    def getPartnerStatus(self):
        return self.partnerStatus

    def setPartnerStatus(self, newPartnerStatus):
        self.partnerStatus = newPartnerStatus

    def getPartnerPackage(self):
        return self.partnerPackage

    def setPartnerPackage(self, newPartnerPackage):
        self.partnerPackage = newPartnerPackage

    def getPartnerCreatedAt(self):
        return self.partnerCreatedAt

    def setPartnerCreatedAt(self, newPartnerCreatedAt):
        self.partnerCreatedAt = newPartnerCreatedAt

    def getViews(self):
        return self.views

    def setViews(self, newViews):
        self.views = newViews

    def getPlays(self):
        return self.plays

    def setPlays(self, newPlays):
        self.plays = newPlays

    def getEntriesCount(self):
        return self.entriesCount

    def setEntriesCount(self, newEntriesCount):
        self.entriesCount = newEntriesCount

    def getTotalEntriesCount(self):
        return self.totalEntriesCount

    def setTotalEntriesCount(self, newTotalEntriesCount):
        self.totalEntriesCount = newTotalEntriesCount

    def getVideoEntriesCount(self):
        return self.videoEntriesCount

    def setVideoEntriesCount(self, newVideoEntriesCount):
        self.videoEntriesCount = newVideoEntriesCount

    def getImageEntriesCount(self):
        return self.imageEntriesCount

    def setImageEntriesCount(self, newImageEntriesCount):
        self.imageEntriesCount = newImageEntriesCount

    def getAudioEntriesCount(self):
        return self.audioEntriesCount

    def setAudioEntriesCount(self, newAudioEntriesCount):
        self.audioEntriesCount = newAudioEntriesCount

    def getMixEntriesCount(self):
        return self.mixEntriesCount

    def setMixEntriesCount(self, newMixEntriesCount):
        self.mixEntriesCount = newMixEntriesCount

    def getBandwidth(self):
        return self.bandwidth

    def setBandwidth(self, newBandwidth):
        self.bandwidth = newBandwidth

    def getTotalStorage(self):
        return self.totalStorage

    def setTotalStorage(self, newTotalStorage):
        self.totalStorage = newTotalStorage

    def getStorage(self):
        return self.storage

    def setStorage(self, newStorage):
        self.storage = newStorage

    def getPeakStorage(self):
        return self.peakStorage

    def setPeakStorage(self, newPeakStorage):
        self.peakStorage = newPeakStorage

    def getAvgStorage(self):
        return self.avgStorage

    def setAvgStorage(self, newAvgStorage):
        self.avgStorage = newAvgStorage

    def getCombinedBandwidthStorage(self):
        return self.combinedBandwidthStorage

    def setCombinedBandwidthStorage(self, newCombinedBandwidthStorage):
        self.combinedBandwidthStorage = newCombinedBandwidthStorage

    def getDeletedStorage(self):
        return self.deletedStorage

    def setDeletedStorage(self, newDeletedStorage):
        self.deletedStorage = newDeletedStorage

    def getTranscodingUsage(self):
        return self.transcodingUsage

    def setTranscodingUsage(self, newTranscodingUsage):
        self.transcodingUsage = newTranscodingUsage


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerOveragedLimit(KalturaSystemPartnerLimit):
    def __init__(self,
            type=NotImplemented,
            max=NotImplemented,
            overagePrice=NotImplemented,
            overageUnit=NotImplemented):
        KalturaSystemPartnerLimit.__init__(self,
            type,
            max)

        # @var float
        self.overagePrice = overagePrice

        # @var float
        self.overageUnit = overageUnit


    PROPERTY_LOADERS = {
        'overagePrice': getXmlNodeFloat, 
        'overageUnit': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaSystemPartnerLimit.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerOveragedLimit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSystemPartnerLimit.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerOveragedLimit")
        kparams.addFloatIfDefined("overagePrice", self.overagePrice)
        kparams.addFloatIfDefined("overageUnit", self.overageUnit)
        return kparams

    def getOveragePrice(self):
        return self.overagePrice

    def setOveragePrice(self, newOveragePrice):
        self.overagePrice = newOveragePrice

    def getOverageUnit(self):
        return self.overageUnit

    def setOverageUnit(self, newOverageUnit):
        self.overageUnit = newOverageUnit


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerUsageFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            fromDate=NotImplemented,
            toDate=NotImplemented,
            timezoneOffset=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # Date range from
        # @var int
        self.fromDate = fromDate

        # Date range to
        # @var int
        self.toDate = toDate

        # Time zone offset
        # @var int
        self.timezoneOffset = timezoneOffset


    PROPERTY_LOADERS = {
        'fromDate': getXmlNodeInt, 
        'toDate': getXmlNodeInt, 
        'timezoneOffset': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageFilter")
        kparams.addIntIfDefined("fromDate", self.fromDate)
        kparams.addIntIfDefined("toDate", self.toDate)
        kparams.addIntIfDefined("timezoneOffset", self.timezoneOffset)
        return kparams

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate

    def getToDate(self):
        return self.toDate

    def setToDate(self, newToDate):
        self.toDate = newToDate

    def getTimezoneOffset(self):
        return self.timezoneOffset

    def setTimezoneOffset(self, newTimezoneOffset):
        self.timezoneOffset = newTimezoneOffset


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerUsageListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaSystemPartnerUsageItem
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaSystemPartnerUsageItem), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerUsageListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerUsageListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerFilter(KalturaPartnerFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            nameLike=NotImplemented,
            nameMultiLikeOr=NotImplemented,
            nameMultiLikeAnd=NotImplemented,
            nameEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            partnerPackageEqual=NotImplemented,
            partnerPackageGreaterThanOrEqual=NotImplemented,
            partnerPackageLessThanOrEqual=NotImplemented,
            partnerGroupTypeEqual=NotImplemented,
            partnerNameDescriptionWebsiteAdminNameAdminEmailLike=NotImplemented,
            partnerParentIdEqual=NotImplemented,
            partnerParentIdIn=NotImplemented):
        KalturaPartnerFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            nameLike,
            nameMultiLikeOr,
            nameMultiLikeAnd,
            nameEqual,
            statusEqual,
            statusIn,
            partnerPackageEqual,
            partnerPackageGreaterThanOrEqual,
            partnerPackageLessThanOrEqual,
            partnerGroupTypeEqual,
            partnerNameDescriptionWebsiteAdminNameAdminEmailLike)

        # @var int
        self.partnerParentIdEqual = partnerParentIdEqual

        # @var string
        self.partnerParentIdIn = partnerParentIdIn


    PROPERTY_LOADERS = {
        'partnerParentIdEqual': getXmlNodeInt, 
        'partnerParentIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPartnerFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSystemPartnerFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPartnerFilter.toParams(self)
        kparams.put("objectType", "KalturaSystemPartnerFilter")
        kparams.addIntIfDefined("partnerParentIdEqual", self.partnerParentIdEqual)
        kparams.addStringIfDefined("partnerParentIdIn", self.partnerParentIdIn)
        return kparams

    def getPartnerParentIdEqual(self):
        return self.partnerParentIdEqual

    def setPartnerParentIdEqual(self, newPartnerParentIdEqual):
        self.partnerParentIdEqual = newPartnerParentIdEqual

    def getPartnerParentIdIn(self):
        return self.partnerParentIdIn

    def setPartnerParentIdIn(self, newPartnerParentIdIn):
        self.partnerParentIdIn = newPartnerParentIdIn


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaSystemPartnerService(KalturaServiceBase):
    """System partner service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, partnerId):
        """Retrieve all info about partner
        	 This service gets partner id as parameter and accessable to the admin console partner only"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        self.client.queueServiceActionCall("systempartner_systempartner", "get", KalturaPartner, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartner)

    def getUsage(self, partnerFilter = NotImplemented, usageFilter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("partnerFilter", partnerFilter)
        kparams.addObjectIfDefined("usageFilter", usageFilter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("systempartner_systempartner", "getUsage", KalturaSystemPartnerUsageListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSystemPartnerUsageListResponse)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("systempartner_systempartner", "list", KalturaPartnerListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPartnerListResponse)

    def updateStatus(self, partnerId, status, reason):
        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addIntIfDefined("status", status);
        kparams.addStringIfDefined("reason", reason)
        self.client.queueServiceActionCall("systempartner_systempartner", "updateStatus", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getAdminSession(self, partnerId, userId = NotImplemented):
        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("systempartner_systempartner", "getAdminSession", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def updateConfiguration(self, partnerId, configuration):
        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addObjectIfDefined("configuration", configuration)
        self.client.queueServiceActionCall("systempartner_systempartner", "updateConfiguration", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def getConfiguration(self, partnerId):
        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        self.client.queueServiceActionCall("systempartner_systempartner", "getConfiguration", KalturaSystemPartnerConfiguration, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSystemPartnerConfiguration)

    def getPackages(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPackages", KalturaSystemPartnerPackage, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaSystemPartnerPackage)

    def getPackagesClassOfService(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPackagesClassOfService", KalturaSystemPartnerPackage, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaSystemPartnerPackage)

    def getPackagesVertical(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPackagesVertical", KalturaSystemPartnerPackage, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaSystemPartnerPackage)

    def getPlayerEmbedCodeTypes(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPlayerEmbedCodeTypes", KalturaPlayerEmbedCodeType, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaPlayerEmbedCodeType)

    def getPlayerDeliveryTypes(self):
        kparams = KalturaParams()
        self.client.queueServiceActionCall("systempartner_systempartner", "getPlayerDeliveryTypes", KalturaPlayerDeliveryType, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaPlayerDeliveryType)

    def resetUserPassword(self, userId, partnerId, newPassword):
        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("newPassword", newPassword)
        self.client.queueServiceActionCall("systempartner_systempartner", "resetUserPassword", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def listUserLoginData(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("systempartner_systempartner", "listUserLoginData", KalturaUserLoginDataListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserLoginDataListResponse)

########## main ##########
class KalturaSystemPartnerClientPlugin(KalturaClientPlugin):
    # KalturaSystemPartnerClientPlugin
    instance = None

    # @return KalturaSystemPartnerClientPlugin
    @staticmethod
    def get():
        if KalturaSystemPartnerClientPlugin.instance == None:
            KalturaSystemPartnerClientPlugin.instance = KalturaSystemPartnerClientPlugin()
        return KalturaSystemPartnerClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'systemPartner': KalturaSystemPartnerService,
        }

    def getEnums(self):
        return {
            'KalturaSystemPartnerLimitType': KalturaSystemPartnerLimitType,
        }

    def getTypes(self):
        return {
            'KalturaSystemPartnerLimit': KalturaSystemPartnerLimit,
            'KalturaSystemPartnerConfiguration': KalturaSystemPartnerConfiguration,
            'KalturaSystemPartnerPackage': KalturaSystemPartnerPackage,
            'KalturaSystemPartnerUsageItem': KalturaSystemPartnerUsageItem,
            'KalturaSystemPartnerOveragedLimit': KalturaSystemPartnerOveragedLimit,
            'KalturaSystemPartnerUsageFilter': KalturaSystemPartnerUsageFilter,
            'KalturaSystemPartnerUsageListResponse': KalturaSystemPartnerUsageListResponse,
            'KalturaSystemPartnerFilter': KalturaSystemPartnerFilter,
        }

    # @return string
    def getName(self):
        return 'systemPartner'

