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
from .EventNotification import *
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
class KalturaEntryVendorTaskCreationMode(object):
    MANUAL = 1
    AUTOMATIC = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskStatus(object):
    PENDING = 1
    READY = 2
    PROCESSING = 3
    PENDING_MODERATION = 4
    REJECTED = 5
    ERROR = 6
    ABORTED = 7
    PENDING_ENTRY_READY = 8

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaReachProfileContentDeletionPolicy(object):
    DO_NOTHING = 1
    DELETE_ONCE_PROCESSED = 2
    DELETE_AFTER_WEEK = 3
    DELETE_AFTER_MONTH = 4
    DELETE_AFTER_THREE_MONTHS = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaReachProfileStatus(object):
    DISABLED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaReachProfileType(object):
    FREE_TRIAL = 1
    PAID = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemOutputFormat(object):
    SRT = 1
    DFXP = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemStatus(object):
    DEPRECATED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorServiceFeature(object):
    CAPTIONS = 1
    TRANSLATION = 2
    ALIGNMENT = 3
    AUDIO_DESCRIPTION = 4

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorServiceTurnAroundTime(object):
    BEST_EFFORT = -1
    IMMEDIATE = 0
    THIRTY_MINUTES = 1800
    TWO_HOURS = 7200
    THREE_HOURS = 10800
    SIX_HOURS = 21600
    EIGHT_HOURS = 28800
    TWELVE_HOURS = 43200
    TWENTY_FOUR_HOURS = 86400
    FORTY_EIGHT_HOURS = 172800
    FOUR_DAYS = 345600
    TEN_DAYS = 864000

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorServiceType(object):
    HUMAN = 1
    MACHINE = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorTaskProcessingRegion(object):
    US = 1
    EU = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCatalogItemLanguage(object):
    AR = "Arabic"
    YUE = "Cantonese"
    ZH = "Chinese"
    DA = "Danish"
    NL = "Dutch"
    EN = "English"
    EN_US = "English (American)"
    EN_GB = "English (British)"
    FI = "Finnish"
    FR = "French"
    DE = "German"
    HE = "Hebrew"
    HI = "Hindi"
    IS = "Icelandic"
    IT = "Italian"
    JA = "Japanese"
    KO = "Korean"
    CMN = "Mandarin Chinese"
    NO = "Norwegian"
    PT = "Portuguese"
    RU = "Russian"
    ES = "Spanish"
    SV = "Swedish"
    TH = "Thai"
    TR = "Turkish"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    FINISH_TIME_ASC = "+finishTime"
    ID_ASC = "+id"
    PRICE_ASC = "+price"
    QUEUE_TIME_ASC = "+queueTime"
    STATUS_ASC = "+status"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    FINISH_TIME_DESC = "-finishTime"
    ID_DESC = "-id"
    PRICE_DESC = "-price"
    QUEUE_TIME_DESC = "-queueTime"
    STATUS_DESC = "-status"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaReachProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorCaptionsCatalogItemOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemPriceFunction(object):
    PRICE_PER_MINUTE = "kReachUtils::calcPricePerMinute"
    PRICE_PER_SECOND = "kReachUtils::calcPricePerSecond"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorCreditRecurrenceFrequency(object):
    DAILY = "day"
    MONTHLY = "month"
    WEEKLY = "week"
    YEARLY = "year"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorTranslationCatalogItemOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaBaseVendorCredit(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseVendorCredit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseVendorCredit")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaDictionary(KalturaObjectBase):
    def __init__(self,
            language=NotImplemented,
            data=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaCatalogItemLanguage
        self.language = language

        # @var string
        self.data = data


    PROPERTY_LOADERS = {
        'language': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDictionary.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDictionary")
        kparams.addStringEnumIfDefined("language", self.language)
        kparams.addStringIfDefined("data", self.data)
        return kparams

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


# @package Kaltura
# @subpackage Client
class KalturaVendorTaskData(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVendorTaskData")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTask(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            vendorPartnerId=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            queueTime=NotImplemented,
            finishTime=NotImplemented,
            entryId=NotImplemented,
            status=NotImplemented,
            reachProfileId=NotImplemented,
            catalogItemId=NotImplemented,
            price=NotImplemented,
            userId=NotImplemented,
            moderatingUser=NotImplemented,
            errDescription=NotImplemented,
            accessKey=NotImplemented,
            version=NotImplemented,
            notes=NotImplemented,
            dictionary=NotImplemented,
            context=NotImplemented,
            accuracy=NotImplemented,
            outputObjectId=NotImplemented,
            partnerData=NotImplemented,
            creationMode=NotImplemented,
            taskJobData=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var int
        # @readonly
        self.vendorPartnerId = vendorPartnerId

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var int
        # @readonly
        self.queueTime = queueTime

        # @var int
        # @readonly
        self.finishTime = finishTime

        # @var string
        # @insertonly
        self.entryId = entryId

        # @var KalturaEntryVendorTaskStatus
        self.status = status

        # The profile id from which this task base config is taken from
        # @var int
        # @insertonly
        self.reachProfileId = reachProfileId

        # The catalog item Id containing the task description
        # @var int
        # @insertonly
        self.catalogItemId = catalogItemId

        # The charged price to execute this task
        # @var float
        # @readonly
        self.price = price

        # The ID of the user who created this task
        # @var string
        # @readonly
        self.userId = userId

        # The user ID that approved this task for execution (in case moderation is requested)
        # @var string
        # @readonly
        self.moderatingUser = moderatingUser

        # Err description provided by provider in case job execution has failed
        # @var string
        self.errDescription = errDescription

        # Access key generated by Kaltura to allow vendors to ingest the end result to the destination
        # @var string
        # @readonly
        self.accessKey = accessKey

        # Vendor generated by Kaltura representing the entry vendor task version correlated to the entry version
        # @var string
        # @readonly
        self.version = version

        # User generated notes that should be taken into account by the vendor while executing the task
        # @var string
        self.notes = notes

        # @var string
        # @readonly
        self.dictionary = dictionary

        # Task context
        # @var string
        self.context = context

        # Task result accuracy percentage
        # @var int
        self.accuracy = accuracy

        # Task main object generated by executing the task
        # @var string
        self.outputObjectId = outputObjectId

        # Json object containing extra task data required by the requester
        # @var string
        self.partnerData = partnerData

        # Task creation mode
        # @var KalturaEntryVendorTaskCreationMode
        # @readonly
        self.creationMode = creationMode

        # @var KalturaVendorTaskData
        self.taskJobData = taskJobData


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'vendorPartnerId': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'queueTime': getXmlNodeInt, 
        'finishTime': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaEntryVendorTaskStatus"), 
        'reachProfileId': getXmlNodeInt, 
        'catalogItemId': getXmlNodeInt, 
        'price': getXmlNodeFloat, 
        'userId': getXmlNodeText, 
        'moderatingUser': getXmlNodeText, 
        'errDescription': getXmlNodeText, 
        'accessKey': getXmlNodeText, 
        'version': getXmlNodeText, 
        'notes': getXmlNodeText, 
        'dictionary': getXmlNodeText, 
        'context': getXmlNodeText, 
        'accuracy': getXmlNodeInt, 
        'outputObjectId': getXmlNodeText, 
        'partnerData': getXmlNodeText, 
        'creationMode': (KalturaEnumsFactory.createInt, "KalturaEntryVendorTaskCreationMode"), 
        'taskJobData': (KalturaObjectFactory.create, 'KalturaVendorTaskData'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryVendorTask.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntryVendorTask")
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addIntIfDefined("reachProfileId", self.reachProfileId)
        kparams.addIntIfDefined("catalogItemId", self.catalogItemId)
        kparams.addStringIfDefined("errDescription", self.errDescription)
        kparams.addStringIfDefined("notes", self.notes)
        kparams.addStringIfDefined("context", self.context)
        kparams.addIntIfDefined("accuracy", self.accuracy)
        kparams.addStringIfDefined("outputObjectId", self.outputObjectId)
        kparams.addStringIfDefined("partnerData", self.partnerData)
        kparams.addObjectIfDefined("taskJobData", self.taskJobData)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getVendorPartnerId(self):
        return self.vendorPartnerId

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getQueueTime(self):
        return self.queueTime

    def getFinishTime(self):
        return self.finishTime

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getReachProfileId(self):
        return self.reachProfileId

    def setReachProfileId(self, newReachProfileId):
        self.reachProfileId = newReachProfileId

    def getCatalogItemId(self):
        return self.catalogItemId

    def setCatalogItemId(self, newCatalogItemId):
        self.catalogItemId = newCatalogItemId

    def getPrice(self):
        return self.price

    def getUserId(self):
        return self.userId

    def getModeratingUser(self):
        return self.moderatingUser

    def getErrDescription(self):
        return self.errDescription

    def setErrDescription(self, newErrDescription):
        self.errDescription = newErrDescription

    def getAccessKey(self):
        return self.accessKey

    def getVersion(self):
        return self.version

    def getNotes(self):
        return self.notes

    def setNotes(self, newNotes):
        self.notes = newNotes

    def getDictionary(self):
        return self.dictionary

    def getContext(self):
        return self.context

    def setContext(self, newContext):
        self.context = newContext

    def getAccuracy(self):
        return self.accuracy

    def setAccuracy(self, newAccuracy):
        self.accuracy = newAccuracy

    def getOutputObjectId(self):
        return self.outputObjectId

    def setOutputObjectId(self, newOutputObjectId):
        self.outputObjectId = newOutputObjectId

    def getPartnerData(self):
        return self.partnerData

    def setPartnerData(self, newPartnerData):
        self.partnerData = newPartnerData

    def getCreationMode(self):
        return self.creationMode

    def getTaskJobData(self):
        return self.taskJobData

    def setTaskJobData(self, newTaskJobData):
        self.taskJobData = newTaskJobData


# @package Kaltura
# @subpackage Client
class KalturaReachProfile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            partnerId=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            profileType=NotImplemented,
            defaultOutputFormat=NotImplemented,
            enableMachineModeration=NotImplemented,
            enableHumanModeration=NotImplemented,
            autoDisplayMachineCaptionsOnPlayer=NotImplemented,
            autoDisplayHumanCaptionsOnPlayer=NotImplemented,
            enableMetadataExtraction=NotImplemented,
            enableSpeakerChangeIndication=NotImplemented,
            enableAudioTags=NotImplemented,
            enableProfanityRemoval=NotImplemented,
            maxCharactersPerCaptionLine=NotImplemented,
            contentDeletionPolicy=NotImplemented,
            rules=NotImplemented,
            credit=NotImplemented,
            usedCredit=NotImplemented,
            dictionaries=NotImplemented,
            flavorParamsIds=NotImplemented,
            vendorTaskProcessingRegion=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # The name of the profile
        # @var string
        self.name = name

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var KalturaReachProfileStatus
        # @readonly
        self.status = status

        # @var KalturaReachProfileType
        self.profileType = profileType

        # @var KalturaVendorCatalogItemOutputFormat
        self.defaultOutputFormat = defaultOutputFormat

        # @var KalturaNullableBoolean
        self.enableMachineModeration = enableMachineModeration

        # @var KalturaNullableBoolean
        self.enableHumanModeration = enableHumanModeration

        # @var KalturaNullableBoolean
        self.autoDisplayMachineCaptionsOnPlayer = autoDisplayMachineCaptionsOnPlayer

        # @var KalturaNullableBoolean
        self.autoDisplayHumanCaptionsOnPlayer = autoDisplayHumanCaptionsOnPlayer

        # @var KalturaNullableBoolean
        self.enableMetadataExtraction = enableMetadataExtraction

        # @var KalturaNullableBoolean
        self.enableSpeakerChangeIndication = enableSpeakerChangeIndication

        # @var KalturaNullableBoolean
        self.enableAudioTags = enableAudioTags

        # @var KalturaNullableBoolean
        self.enableProfanityRemoval = enableProfanityRemoval

        # @var int
        self.maxCharactersPerCaptionLine = maxCharactersPerCaptionLine

        # @var KalturaReachProfileContentDeletionPolicy
        self.contentDeletionPolicy = contentDeletionPolicy

        # @var array of KalturaRule
        self.rules = rules

        # @var KalturaBaseVendorCredit
        self.credit = credit

        # @var float
        # @readonly
        self.usedCredit = usedCredit

        # @var array of KalturaDictionary
        self.dictionaries = dictionaries

        # Comma separated flavorParamsIds that the vendor should look for it matching asset when trying to download the asset
        # @var string
        self.flavorParamsIds = flavorParamsIds

        # Indicates in which region the task processing should task place
        # @var KalturaVendorTaskProcessingRegion
        self.vendorTaskProcessingRegion = vendorTaskProcessingRegion


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaReachProfileStatus"), 
        'profileType': (KalturaEnumsFactory.createInt, "KalturaReachProfileType"), 
        'defaultOutputFormat': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemOutputFormat"), 
        'enableMachineModeration': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableHumanModeration': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'autoDisplayMachineCaptionsOnPlayer': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'autoDisplayHumanCaptionsOnPlayer': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableMetadataExtraction': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableSpeakerChangeIndication': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableAudioTags': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'enableProfanityRemoval': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'maxCharactersPerCaptionLine': getXmlNodeInt, 
        'contentDeletionPolicy': (KalturaEnumsFactory.createInt, "KalturaReachProfileContentDeletionPolicy"), 
        'rules': (KalturaObjectFactory.createArray, 'KalturaRule'), 
        'credit': (KalturaObjectFactory.create, 'KalturaBaseVendorCredit'), 
        'usedCredit': getXmlNodeFloat, 
        'dictionaries': (KalturaObjectFactory.createArray, 'KalturaDictionary'), 
        'flavorParamsIds': getXmlNodeText, 
        'vendorTaskProcessingRegion': (KalturaEnumsFactory.createInt, "KalturaVendorTaskProcessingRegion"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReachProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReachProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntEnumIfDefined("profileType", self.profileType)
        kparams.addIntEnumIfDefined("defaultOutputFormat", self.defaultOutputFormat)
        kparams.addIntEnumIfDefined("enableMachineModeration", self.enableMachineModeration)
        kparams.addIntEnumIfDefined("enableHumanModeration", self.enableHumanModeration)
        kparams.addIntEnumIfDefined("autoDisplayMachineCaptionsOnPlayer", self.autoDisplayMachineCaptionsOnPlayer)
        kparams.addIntEnumIfDefined("autoDisplayHumanCaptionsOnPlayer", self.autoDisplayHumanCaptionsOnPlayer)
        kparams.addIntEnumIfDefined("enableMetadataExtraction", self.enableMetadataExtraction)
        kparams.addIntEnumIfDefined("enableSpeakerChangeIndication", self.enableSpeakerChangeIndication)
        kparams.addIntEnumIfDefined("enableAudioTags", self.enableAudioTags)
        kparams.addIntEnumIfDefined("enableProfanityRemoval", self.enableProfanityRemoval)
        kparams.addIntIfDefined("maxCharactersPerCaptionLine", self.maxCharactersPerCaptionLine)
        kparams.addIntEnumIfDefined("contentDeletionPolicy", self.contentDeletionPolicy)
        kparams.addArrayIfDefined("rules", self.rules)
        kparams.addObjectIfDefined("credit", self.credit)
        kparams.addArrayIfDefined("dictionaries", self.dictionaries)
        kparams.addStringIfDefined("flavorParamsIds", self.flavorParamsIds)
        kparams.addIntEnumIfDefined("vendorTaskProcessingRegion", self.vendorTaskProcessingRegion)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPartnerId(self):
        return self.partnerId

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getStatus(self):
        return self.status

    def getProfileType(self):
        return self.profileType

    def setProfileType(self, newProfileType):
        self.profileType = newProfileType

    def getDefaultOutputFormat(self):
        return self.defaultOutputFormat

    def setDefaultOutputFormat(self, newDefaultOutputFormat):
        self.defaultOutputFormat = newDefaultOutputFormat

    def getEnableMachineModeration(self):
        return self.enableMachineModeration

    def setEnableMachineModeration(self, newEnableMachineModeration):
        self.enableMachineModeration = newEnableMachineModeration

    def getEnableHumanModeration(self):
        return self.enableHumanModeration

    def setEnableHumanModeration(self, newEnableHumanModeration):
        self.enableHumanModeration = newEnableHumanModeration

    def getAutoDisplayMachineCaptionsOnPlayer(self):
        return self.autoDisplayMachineCaptionsOnPlayer

    def setAutoDisplayMachineCaptionsOnPlayer(self, newAutoDisplayMachineCaptionsOnPlayer):
        self.autoDisplayMachineCaptionsOnPlayer = newAutoDisplayMachineCaptionsOnPlayer

    def getAutoDisplayHumanCaptionsOnPlayer(self):
        return self.autoDisplayHumanCaptionsOnPlayer

    def setAutoDisplayHumanCaptionsOnPlayer(self, newAutoDisplayHumanCaptionsOnPlayer):
        self.autoDisplayHumanCaptionsOnPlayer = newAutoDisplayHumanCaptionsOnPlayer

    def getEnableMetadataExtraction(self):
        return self.enableMetadataExtraction

    def setEnableMetadataExtraction(self, newEnableMetadataExtraction):
        self.enableMetadataExtraction = newEnableMetadataExtraction

    def getEnableSpeakerChangeIndication(self):
        return self.enableSpeakerChangeIndication

    def setEnableSpeakerChangeIndication(self, newEnableSpeakerChangeIndication):
        self.enableSpeakerChangeIndication = newEnableSpeakerChangeIndication

    def getEnableAudioTags(self):
        return self.enableAudioTags

    def setEnableAudioTags(self, newEnableAudioTags):
        self.enableAudioTags = newEnableAudioTags

    def getEnableProfanityRemoval(self):
        return self.enableProfanityRemoval

    def setEnableProfanityRemoval(self, newEnableProfanityRemoval):
        self.enableProfanityRemoval = newEnableProfanityRemoval

    def getMaxCharactersPerCaptionLine(self):
        return self.maxCharactersPerCaptionLine

    def setMaxCharactersPerCaptionLine(self, newMaxCharactersPerCaptionLine):
        self.maxCharactersPerCaptionLine = newMaxCharactersPerCaptionLine

    def getContentDeletionPolicy(self):
        return self.contentDeletionPolicy

    def setContentDeletionPolicy(self, newContentDeletionPolicy):
        self.contentDeletionPolicy = newContentDeletionPolicy

    def getRules(self):
        return self.rules

    def setRules(self, newRules):
        self.rules = newRules

    def getCredit(self):
        return self.credit

    def setCredit(self, newCredit):
        self.credit = newCredit

    def getUsedCredit(self):
        return self.usedCredit

    def getDictionaries(self):
        return self.dictionaries

    def setDictionaries(self, newDictionaries):
        self.dictionaries = newDictionaries

    def getFlavorParamsIds(self):
        return self.flavorParamsIds

    def setFlavorParamsIds(self, newFlavorParamsIds):
        self.flavorParamsIds = newFlavorParamsIds

    def getVendorTaskProcessingRegion(self):
        return self.vendorTaskProcessingRegion

    def setVendorTaskProcessingRegion(self, newVendorTaskProcessingRegion):
        self.vendorTaskProcessingRegion = newVendorTaskProcessingRegion


# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemPricing(KalturaObjectBase):
    def __init__(self,
            pricePerUnit=NotImplemented,
            priceFunction=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var float
        self.pricePerUnit = pricePerUnit

        # @var KalturaVendorCatalogItemPriceFunction
        self.priceFunction = priceFunction


    PROPERTY_LOADERS = {
        'pricePerUnit': getXmlNodeFloat, 
        'priceFunction': (KalturaEnumsFactory.createString, "KalturaVendorCatalogItemPriceFunction"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCatalogItemPricing.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVendorCatalogItemPricing")
        kparams.addFloatIfDefined("pricePerUnit", self.pricePerUnit)
        kparams.addStringEnumIfDefined("priceFunction", self.priceFunction)
        return kparams

    def getPricePerUnit(self):
        return self.pricePerUnit

    def setPricePerUnit(self, newPricePerUnit):
        self.pricePerUnit = newPricePerUnit

    def getPriceFunction(self):
        return self.priceFunction

    def setPriceFunction(self, newPriceFunction):
        self.priceFunction = newPriceFunction


# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItem(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            vendorPartnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            serviceType=NotImplemented,
            serviceFeature=NotImplemented,
            turnAroundTime=NotImplemented,
            pricing=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        self.vendorPartnerId = vendorPartnerId

        # @var string
        self.name = name

        # @var string
        self.systemName = systemName

        # @var int
        # @readonly
        self.createdAt = createdAt

        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # @var KalturaVendorCatalogItemStatus
        # @readonly
        self.status = status

        # @var KalturaVendorServiceType
        self.serviceType = serviceType

        # @var KalturaVendorServiceFeature
        # @readonly
        self.serviceFeature = serviceFeature

        # @var KalturaVendorServiceTurnAroundTime
        self.turnAroundTime = turnAroundTime

        # @var KalturaVendorCatalogItemPricing
        self.pricing = pricing


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'vendorPartnerId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemStatus"), 
        'serviceType': (KalturaEnumsFactory.createInt, "KalturaVendorServiceType"), 
        'serviceFeature': (KalturaEnumsFactory.createInt, "KalturaVendorServiceFeature"), 
        'turnAroundTime': (KalturaEnumsFactory.createInt, "KalturaVendorServiceTurnAroundTime"), 
        'pricing': (KalturaObjectFactory.create, 'KalturaVendorCatalogItemPricing'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVendorCatalogItem")
        kparams.addIntIfDefined("vendorPartnerId", self.vendorPartnerId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addIntEnumIfDefined("serviceType", self.serviceType)
        kparams.addIntEnumIfDefined("turnAroundTime", self.turnAroundTime)
        kparams.addObjectIfDefined("pricing", self.pricing)
        return kparams

    def getId(self):
        return self.id

    def getVendorPartnerId(self):
        return self.vendorPartnerId

    def setVendorPartnerId(self, newVendorPartnerId):
        self.vendorPartnerId = newVendorPartnerId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getStatus(self):
        return self.status

    def getServiceType(self):
        return self.serviceType

    def setServiceType(self, newServiceType):
        self.serviceType = newServiceType

    def getServiceFeature(self):
        return self.serviceFeature

    def getTurnAroundTime(self):
        return self.turnAroundTime

    def setTurnAroundTime(self, newTurnAroundTime):
        self.turnAroundTime = newTurnAroundTime

    def getPricing(self):
        return self.pricing

    def setPricing(self, newPricing):
        self.pricing = newPricing


# @package Kaltura
# @subpackage Client
class KalturaAddEntryVendorTaskAction(KalturaRuleAction):
    def __init__(self,
            type=NotImplemented,
            catalogItemIds=NotImplemented):
        KalturaRuleAction.__init__(self,
            type)

        # Catalog Item Id
        # @var string
        self.catalogItemIds = catalogItemIds


    PROPERTY_LOADERS = {
        'catalogItemIds': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRuleAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAddEntryVendorTaskAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRuleAction.toParams(self)
        kparams.put("objectType", "KalturaAddEntryVendorTaskAction")
        kparams.addStringIfDefined("catalogItemIds", self.catalogItemIds)
        return kparams

    def getCatalogItemIds(self):
        return self.catalogItemIds

    def setCatalogItemIds(self, newCatalogItemIds):
        self.catalogItemIds = newCatalogItemIds


# @package Kaltura
# @subpackage Client
class KalturaAlignmentVendorTaskData(KalturaVendorTaskData):
    def __init__(self,
            textTranscriptAssetId=NotImplemented,
            jsonTranscriptAssetId=NotImplemented,
            captionAssetId=NotImplemented):
        KalturaVendorTaskData.__init__(self)

        # The id of the text transcript object the vendor should use while runing the alignment task
        # @var string
        self.textTranscriptAssetId = textTranscriptAssetId

        # Optional - The id of the json transcript object the vendor should update once alignment task processing is done
        # @var string
        # @insertonly
        self.jsonTranscriptAssetId = jsonTranscriptAssetId

        # Optional - The id of the caption asset object the vendor should update once alignment task processing is done
        # @var string
        # @insertonly
        self.captionAssetId = captionAssetId


    PROPERTY_LOADERS = {
        'textTranscriptAssetId': getXmlNodeText, 
        'jsonTranscriptAssetId': getXmlNodeText, 
        'captionAssetId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAlignmentVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaAlignmentVendorTaskData")
        kparams.addStringIfDefined("textTranscriptAssetId", self.textTranscriptAssetId)
        kparams.addStringIfDefined("jsonTranscriptAssetId", self.jsonTranscriptAssetId)
        kparams.addStringIfDefined("captionAssetId", self.captionAssetId)
        return kparams

    def getTextTranscriptAssetId(self):
        return self.textTranscriptAssetId

    def setTextTranscriptAssetId(self, newTextTranscriptAssetId):
        self.textTranscriptAssetId = newTextTranscriptAssetId

    def getJsonTranscriptAssetId(self):
        return self.jsonTranscriptAssetId

    def setJsonTranscriptAssetId(self, newJsonTranscriptAssetId):
        self.jsonTranscriptAssetId = newJsonTranscriptAssetId

    def getCaptionAssetId(self):
        return self.captionAssetId

    def setCaptionAssetId(self, newCaptionAssetId):
        self.captionAssetId = newCaptionAssetId


# @package Kaltura
# @subpackage Client
class KalturaCatalogItemAdvancedFilter(KalturaSearchItem):
    def __init__(self,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented,
            sourceLanguageEqual=NotImplemented,
            targetLanguageEqual=NotImplemented):
        KalturaSearchItem.__init__(self)

        # @var KalturaVendorServiceType
        self.serviceTypeEqual = serviceTypeEqual

        # @var string
        self.serviceTypeIn = serviceTypeIn

        # @var KalturaVendorServiceFeature
        self.serviceFeatureEqual = serviceFeatureEqual

        # @var string
        self.serviceFeatureIn = serviceFeatureIn

        # @var KalturaVendorServiceTurnAroundTime
        self.turnAroundTimeEqual = turnAroundTimeEqual

        # @var string
        self.turnAroundTimeIn = turnAroundTimeIn

        # @var KalturaCatalogItemLanguage
        self.sourceLanguageEqual = sourceLanguageEqual

        # @var KalturaCatalogItemLanguage
        self.targetLanguageEqual = targetLanguageEqual


    PROPERTY_LOADERS = {
        'serviceTypeEqual': (KalturaEnumsFactory.createInt, "KalturaVendorServiceType"), 
        'serviceTypeIn': getXmlNodeText, 
        'serviceFeatureEqual': (KalturaEnumsFactory.createInt, "KalturaVendorServiceFeature"), 
        'serviceFeatureIn': getXmlNodeText, 
        'turnAroundTimeEqual': (KalturaEnumsFactory.createInt, "KalturaVendorServiceTurnAroundTime"), 
        'turnAroundTimeIn': getXmlNodeText, 
        'sourceLanguageEqual': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'targetLanguageEqual': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
    }

    def fromXml(self, node):
        KalturaSearchItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCatalogItemAdvancedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchItem.toParams(self)
        kparams.put("objectType", "KalturaCatalogItemAdvancedFilter")
        kparams.addIntEnumIfDefined("serviceTypeEqual", self.serviceTypeEqual)
        kparams.addStringIfDefined("serviceTypeIn", self.serviceTypeIn)
        kparams.addIntEnumIfDefined("serviceFeatureEqual", self.serviceFeatureEqual)
        kparams.addStringIfDefined("serviceFeatureIn", self.serviceFeatureIn)
        kparams.addIntEnumIfDefined("turnAroundTimeEqual", self.turnAroundTimeEqual)
        kparams.addStringIfDefined("turnAroundTimeIn", self.turnAroundTimeIn)
        kparams.addStringEnumIfDefined("sourceLanguageEqual", self.sourceLanguageEqual)
        kparams.addStringEnumIfDefined("targetLanguageEqual", self.targetLanguageEqual)
        return kparams

    def getServiceTypeEqual(self):
        return self.serviceTypeEqual

    def setServiceTypeEqual(self, newServiceTypeEqual):
        self.serviceTypeEqual = newServiceTypeEqual

    def getServiceTypeIn(self):
        return self.serviceTypeIn

    def setServiceTypeIn(self, newServiceTypeIn):
        self.serviceTypeIn = newServiceTypeIn

    def getServiceFeatureEqual(self):
        return self.serviceFeatureEqual

    def setServiceFeatureEqual(self, newServiceFeatureEqual):
        self.serviceFeatureEqual = newServiceFeatureEqual

    def getServiceFeatureIn(self):
        return self.serviceFeatureIn

    def setServiceFeatureIn(self, newServiceFeatureIn):
        self.serviceFeatureIn = newServiceFeatureIn

    def getTurnAroundTimeEqual(self):
        return self.turnAroundTimeEqual

    def setTurnAroundTimeEqual(self, newTurnAroundTimeEqual):
        self.turnAroundTimeEqual = newTurnAroundTimeEqual

    def getTurnAroundTimeIn(self):
        return self.turnAroundTimeIn

    def setTurnAroundTimeIn(self, newTurnAroundTimeIn):
        self.turnAroundTimeIn = newTurnAroundTimeIn

    def getSourceLanguageEqual(self):
        return self.sourceLanguageEqual

    def setSourceLanguageEqual(self, newSourceLanguageEqual):
        self.sourceLanguageEqual = newSourceLanguageEqual

    def getTargetLanguageEqual(self):
        return self.targetLanguageEqual

    def setTargetLanguageEqual(self, newTargetLanguageEqual):
        self.targetLanguageEqual = newTargetLanguageEqual


# @package Kaltura
# @subpackage Client
class KalturaCategoryEntryCondition(KalturaCondition):
    def __init__(self,
            type=NotImplemented,
            description=NotImplemented,
            not_=NotImplemented,
            categoryId=NotImplemented,
            categoryUserPermission=NotImplemented,
            comparison=NotImplemented):
        KalturaCondition.__init__(self,
            type,
            description,
            not_)

        # Category id to check condition for
        # @var int
        self.categoryId = categoryId

        # Minimum category user level permission to validate
        # @var KalturaCategoryUserPermissionLevel
        self.categoryUserPermission = categoryUserPermission

        # Comparing operator
        # @var KalturaSearchConditionComparison
        self.comparison = comparison


    PROPERTY_LOADERS = {
        'categoryId': getXmlNodeInt, 
        'categoryUserPermission': (KalturaEnumsFactory.createInt, "KalturaCategoryUserPermissionLevel"), 
        'comparison': (KalturaEnumsFactory.createString, "KalturaSearchConditionComparison"), 
    }

    def fromXml(self, node):
        KalturaCondition.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCategoryEntryCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCondition.toParams(self)
        kparams.put("objectType", "KalturaCategoryEntryCondition")
        kparams.addIntIfDefined("categoryId", self.categoryId)
        kparams.addIntEnumIfDefined("categoryUserPermission", self.categoryUserPermission)
        kparams.addStringEnumIfDefined("comparison", self.comparison)
        return kparams

    def getCategoryId(self):
        return self.categoryId

    def setCategoryId(self, newCategoryId):
        self.categoryId = newCategoryId

    def getCategoryUserPermission(self):
        return self.categoryUserPermission

    def setCategoryUserPermission(self, newCategoryUserPermission):
        self.categoryUserPermission = newCategoryUserPermission

    def getComparison(self):
        return self.comparison

    def setComparison(self, newComparison):
        self.comparison = newComparison


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaEntryVendorTask
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaEntryVendorTask'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryVendorTaskListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaEntryVendorTaskListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaReachProfileListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaReachProfile
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaReachProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReachProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaReachProfileListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaUnlimitedVendorCredit(KalturaBaseVendorCredit):
    def __init__(self,
            credit=NotImplemented,
            fromDate=NotImplemented,
            toDate=NotImplemented):
        KalturaBaseVendorCredit.__init__(self)

        # @var int
        # @readonly
        self.credit = credit

        # @var int
        self.fromDate = fromDate

        # @var int
        self.toDate = toDate


    PROPERTY_LOADERS = {
        'credit': getXmlNodeInt, 
        'fromDate': getXmlNodeInt, 
        'toDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBaseVendorCredit.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUnlimitedVendorCredit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseVendorCredit.toParams(self)
        kparams.put("objectType", "KalturaUnlimitedVendorCredit")
        kparams.addIntIfDefined("fromDate", self.fromDate)
        kparams.addIntIfDefined("toDate", self.toDate)
        return kparams

    def getCredit(self):
        return self.credit

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate

    def getToDate(self):
        return self.toDate

    def setToDate(self, newToDate):
        self.toDate = newToDate


# @package Kaltura
# @subpackage Client
class KalturaVendorAlignmentCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id=NotImplemented,
            vendorPartnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            serviceType=NotImplemented,
            serviceFeature=NotImplemented,
            turnAroundTime=NotImplemented,
            pricing=NotImplemented,
            sourceLanguage=NotImplemented,
            outputFormat=NotImplemented):
        KalturaVendorCatalogItem.__init__(self,
            id,
            vendorPartnerId,
            name,
            systemName,
            createdAt,
            updatedAt,
            status,
            serviceType,
            serviceFeature,
            turnAroundTime,
            pricing)

        # @var KalturaCatalogItemLanguage
        self.sourceLanguage = sourceLanguage

        # @var KalturaVendorCatalogItemOutputFormat
        self.outputFormat = outputFormat


    PROPERTY_LOADERS = {
        'sourceLanguage': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'outputFormat': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemOutputFormat"), 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorAlignmentCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorAlignmentCatalogItem")
        kparams.addStringEnumIfDefined("sourceLanguage", self.sourceLanguage)
        kparams.addIntEnumIfDefined("outputFormat", self.outputFormat)
        return kparams

    def getSourceLanguage(self):
        return self.sourceLanguage

    def setSourceLanguage(self, newSourceLanguage):
        self.sourceLanguage = newSourceLanguage

    def getOutputFormat(self):
        return self.outputFormat

    def setOutputFormat(self, newOutputFormat):
        self.outputFormat = newOutputFormat


# @package Kaltura
# @subpackage Client
class KalturaVendorAudioDescriptionCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id=NotImplemented,
            vendorPartnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            serviceType=NotImplemented,
            serviceFeature=NotImplemented,
            turnAroundTime=NotImplemented,
            pricing=NotImplemented,
            sourceLanguage=NotImplemented,
            flavorParamsId=NotImplemented):
        KalturaVendorCatalogItem.__init__(self,
            id,
            vendorPartnerId,
            name,
            systemName,
            createdAt,
            updatedAt,
            status,
            serviceType,
            serviceFeature,
            turnAroundTime,
            pricing)

        # @var KalturaCatalogItemLanguage
        self.sourceLanguage = sourceLanguage

        # @var int
        self.flavorParamsId = flavorParamsId


    PROPERTY_LOADERS = {
        'sourceLanguage': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'flavorParamsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorAudioDescriptionCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorAudioDescriptionCatalogItem")
        kparams.addStringEnumIfDefined("sourceLanguage", self.sourceLanguage)
        kparams.addIntIfDefined("flavorParamsId", self.flavorParamsId)
        return kparams

    def getSourceLanguage(self):
        return self.sourceLanguage

    def setSourceLanguage(self, newSourceLanguage):
        self.sourceLanguage = newSourceLanguage

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId


# @package Kaltura
# @subpackage Client
class KalturaVendorCaptionsCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id=NotImplemented,
            vendorPartnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            serviceType=NotImplemented,
            serviceFeature=NotImplemented,
            turnAroundTime=NotImplemented,
            pricing=NotImplemented,
            sourceLanguage=NotImplemented,
            outputFormat=NotImplemented,
            enableSpeakerId=NotImplemented,
            fixedPriceAddons=NotImplemented):
        KalturaVendorCatalogItem.__init__(self,
            id,
            vendorPartnerId,
            name,
            systemName,
            createdAt,
            updatedAt,
            status,
            serviceType,
            serviceFeature,
            turnAroundTime,
            pricing)

        # @var KalturaCatalogItemLanguage
        self.sourceLanguage = sourceLanguage

        # @var KalturaVendorCatalogItemOutputFormat
        self.outputFormat = outputFormat

        # @var KalturaNullableBoolean
        self.enableSpeakerId = enableSpeakerId

        # @var int
        self.fixedPriceAddons = fixedPriceAddons


    PROPERTY_LOADERS = {
        'sourceLanguage': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'outputFormat': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemOutputFormat"), 
        'enableSpeakerId': (KalturaEnumsFactory.createInt, "KalturaNullableBoolean"), 
        'fixedPriceAddons': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCaptionsCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorCaptionsCatalogItem")
        kparams.addStringEnumIfDefined("sourceLanguage", self.sourceLanguage)
        kparams.addIntEnumIfDefined("outputFormat", self.outputFormat)
        kparams.addIntEnumIfDefined("enableSpeakerId", self.enableSpeakerId)
        kparams.addIntIfDefined("fixedPriceAddons", self.fixedPriceAddons)
        return kparams

    def getSourceLanguage(self):
        return self.sourceLanguage

    def setSourceLanguage(self, newSourceLanguage):
        self.sourceLanguage = newSourceLanguage

    def getOutputFormat(self):
        return self.outputFormat

    def setOutputFormat(self, newOutputFormat):
        self.outputFormat = newOutputFormat

    def getEnableSpeakerId(self):
        return self.enableSpeakerId

    def setEnableSpeakerId(self, newEnableSpeakerId):
        self.enableSpeakerId = newEnableSpeakerId

    def getFixedPriceAddons(self):
        return self.fixedPriceAddons

    def setFixedPriceAddons(self, newFixedPriceAddons):
        self.fixedPriceAddons = newFixedPriceAddons


# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaVendorCatalogItem
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaVendorCatalogItem'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCatalogItemListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaVendorCatalogItemListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaVendorCredit(KalturaBaseVendorCredit):
    def __init__(self,
            credit=NotImplemented,
            fromDate=NotImplemented,
            overageCredit=NotImplemented,
            addOn=NotImplemented):
        KalturaBaseVendorCredit.__init__(self)

        # @var int
        self.credit = credit

        # @var int
        self.fromDate = fromDate

        # @var int
        self.overageCredit = overageCredit

        # @var int
        self.addOn = addOn


    PROPERTY_LOADERS = {
        'credit': getXmlNodeInt, 
        'fromDate': getXmlNodeInt, 
        'overageCredit': getXmlNodeInt, 
        'addOn': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBaseVendorCredit.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCredit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseVendorCredit.toParams(self)
        kparams.put("objectType", "KalturaVendorCredit")
        kparams.addIntIfDefined("credit", self.credit)
        kparams.addIntIfDefined("fromDate", self.fromDate)
        kparams.addIntIfDefined("overageCredit", self.overageCredit)
        kparams.addIntIfDefined("addOn", self.addOn)
        return kparams

    def getCredit(self):
        return self.credit

    def setCredit(self, newCredit):
        self.credit = newCredit

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate

    def getOverageCredit(self):
        return self.overageCredit

    def setOverageCredit(self, newOverageCredit):
        self.overageCredit = newOverageCredit

    def getAddOn(self):
        return self.addOn

    def setAddOn(self, newAddOn):
        self.addOn = newAddOn


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            queueTimeGreaterThanOrEqual=NotImplemented,
            queueTimeLessThanOrEqual=NotImplemented,
            finishTimeGreaterThanOrEqual=NotImplemented,
            finishTimeLessThanOrEqual=NotImplemented,
            entryIdEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            reachProfileIdEqual=NotImplemented,
            reachProfileIdIn=NotImplemented,
            catalogItemIdEqual=NotImplemented,
            catalogItemIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            contextEqual=NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.vendorPartnerIdEqual = vendorPartnerIdEqual

        # @var string
        self.vendorPartnerIdIn = vendorPartnerIdIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var int
        self.queueTimeGreaterThanOrEqual = queueTimeGreaterThanOrEqual

        # @var int
        self.queueTimeLessThanOrEqual = queueTimeLessThanOrEqual

        # @var int
        self.finishTimeGreaterThanOrEqual = finishTimeGreaterThanOrEqual

        # @var int
        self.finishTimeLessThanOrEqual = finishTimeLessThanOrEqual

        # @var string
        self.entryIdEqual = entryIdEqual

        # @var KalturaEntryVendorTaskStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.reachProfileIdEqual = reachProfileIdEqual

        # @var string
        self.reachProfileIdIn = reachProfileIdIn

        # @var int
        self.catalogItemIdEqual = catalogItemIdEqual

        # @var string
        self.catalogItemIdIn = catalogItemIdIn

        # @var string
        self.userIdEqual = userIdEqual

        # @var string
        self.contextEqual = contextEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'vendorPartnerIdEqual': getXmlNodeInt, 
        'vendorPartnerIdIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'queueTimeGreaterThanOrEqual': getXmlNodeInt, 
        'queueTimeLessThanOrEqual': getXmlNodeInt, 
        'finishTimeGreaterThanOrEqual': getXmlNodeInt, 
        'finishTimeLessThanOrEqual': getXmlNodeInt, 
        'entryIdEqual': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaEntryVendorTaskStatus"), 
        'statusIn': getXmlNodeText, 
        'reachProfileIdEqual': getXmlNodeInt, 
        'reachProfileIdIn': getXmlNodeText, 
        'catalogItemIdEqual': getXmlNodeInt, 
        'catalogItemIdIn': getXmlNodeText, 
        'userIdEqual': getXmlNodeText, 
        'contextEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRelatedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryVendorTaskBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedFilter.toParams(self)
        kparams.put("objectType", "KalturaEntryVendorTaskBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("vendorPartnerIdEqual", self.vendorPartnerIdEqual)
        kparams.addStringIfDefined("vendorPartnerIdIn", self.vendorPartnerIdIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntIfDefined("queueTimeGreaterThanOrEqual", self.queueTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("queueTimeLessThanOrEqual", self.queueTimeLessThanOrEqual)
        kparams.addIntIfDefined("finishTimeGreaterThanOrEqual", self.finishTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("finishTimeLessThanOrEqual", self.finishTimeLessThanOrEqual)
        kparams.addStringIfDefined("entryIdEqual", self.entryIdEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("reachProfileIdEqual", self.reachProfileIdEqual)
        kparams.addStringIfDefined("reachProfileIdIn", self.reachProfileIdIn)
        kparams.addIntIfDefined("catalogItemIdEqual", self.catalogItemIdEqual)
        kparams.addStringIfDefined("catalogItemIdIn", self.catalogItemIdIn)
        kparams.addStringIfDefined("userIdEqual", self.userIdEqual)
        kparams.addStringIfDefined("contextEqual", self.contextEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getVendorPartnerIdEqual(self):
        return self.vendorPartnerIdEqual

    def setVendorPartnerIdEqual(self, newVendorPartnerIdEqual):
        self.vendorPartnerIdEqual = newVendorPartnerIdEqual

    def getVendorPartnerIdIn(self):
        return self.vendorPartnerIdIn

    def setVendorPartnerIdIn(self, newVendorPartnerIdIn):
        self.vendorPartnerIdIn = newVendorPartnerIdIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getQueueTimeGreaterThanOrEqual(self):
        return self.queueTimeGreaterThanOrEqual

    def setQueueTimeGreaterThanOrEqual(self, newQueueTimeGreaterThanOrEqual):
        self.queueTimeGreaterThanOrEqual = newQueueTimeGreaterThanOrEqual

    def getQueueTimeLessThanOrEqual(self):
        return self.queueTimeLessThanOrEqual

    def setQueueTimeLessThanOrEqual(self, newQueueTimeLessThanOrEqual):
        self.queueTimeLessThanOrEqual = newQueueTimeLessThanOrEqual

    def getFinishTimeGreaterThanOrEqual(self):
        return self.finishTimeGreaterThanOrEqual

    def setFinishTimeGreaterThanOrEqual(self, newFinishTimeGreaterThanOrEqual):
        self.finishTimeGreaterThanOrEqual = newFinishTimeGreaterThanOrEqual

    def getFinishTimeLessThanOrEqual(self):
        return self.finishTimeLessThanOrEqual

    def setFinishTimeLessThanOrEqual(self, newFinishTimeLessThanOrEqual):
        self.finishTimeLessThanOrEqual = newFinishTimeLessThanOrEqual

    def getEntryIdEqual(self):
        return self.entryIdEqual

    def setEntryIdEqual(self, newEntryIdEqual):
        self.entryIdEqual = newEntryIdEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getReachProfileIdEqual(self):
        return self.reachProfileIdEqual

    def setReachProfileIdEqual(self, newReachProfileIdEqual):
        self.reachProfileIdEqual = newReachProfileIdEqual

    def getReachProfileIdIn(self):
        return self.reachProfileIdIn

    def setReachProfileIdIn(self, newReachProfileIdIn):
        self.reachProfileIdIn = newReachProfileIdIn

    def getCatalogItemIdEqual(self):
        return self.catalogItemIdEqual

    def setCatalogItemIdEqual(self, newCatalogItemIdEqual):
        self.catalogItemIdEqual = newCatalogItemIdEqual

    def getCatalogItemIdIn(self):
        return self.catalogItemIdIn

    def setCatalogItemIdIn(self, newCatalogItemIdIn):
        self.catalogItemIdIn = newCatalogItemIdIn

    def getUserIdEqual(self):
        return self.userIdEqual

    def setUserIdEqual(self, newUserIdEqual):
        self.userIdEqual = newUserIdEqual

    def getContextEqual(self):
        return self.contextEqual

    def setContextEqual(self, newContextEqual):
        self.contextEqual = newContextEqual


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskFilter(KalturaEntryVendorTaskBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            queueTimeGreaterThanOrEqual=NotImplemented,
            queueTimeLessThanOrEqual=NotImplemented,
            finishTimeGreaterThanOrEqual=NotImplemented,
            finishTimeLessThanOrEqual=NotImplemented,
            entryIdEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            reachProfileIdEqual=NotImplemented,
            reachProfileIdIn=NotImplemented,
            catalogItemIdEqual=NotImplemented,
            catalogItemIdIn=NotImplemented,
            userIdEqual=NotImplemented,
            contextEqual=NotImplemented,
            freeText=NotImplemented):
        KalturaEntryVendorTaskBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            vendorPartnerIdEqual,
            vendorPartnerIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            queueTimeGreaterThanOrEqual,
            queueTimeLessThanOrEqual,
            finishTimeGreaterThanOrEqual,
            finishTimeLessThanOrEqual,
            entryIdEqual,
            statusEqual,
            statusIn,
            reachProfileIdEqual,
            reachProfileIdIn,
            catalogItemIdEqual,
            catalogItemIdIn,
            userIdEqual,
            contextEqual)

        # @var string
        self.freeText = freeText


    PROPERTY_LOADERS = {
        'freeText': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaEntryVendorTaskBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryVendorTaskFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntryVendorTaskBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaEntryVendorTaskFilter")
        kparams.addStringIfDefined("freeText", self.freeText)
        return kparams

    def getFreeText(self):
        return self.freeText

    def setFreeText(self, newFreeText):
        self.freeText = newFreeText


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskCsvJobData(KalturaExportCsvJobData):
    def __init__(self,
            userName=NotImplemented,
            userMail=NotImplemented,
            outputPath=NotImplemented,
            filter=NotImplemented):
        KalturaExportCsvJobData.__init__(self,
            userName,
            userMail,
            outputPath)

        # The filter should return the list of users that need to be specified in the csv.
        # @var KalturaEntryVendorTaskFilter
        self.filter = filter


    PROPERTY_LOADERS = {
        'filter': (KalturaObjectFactory.create, 'KalturaEntryVendorTaskFilter'), 
    }

    def fromXml(self, node):
        KalturaExportCsvJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryVendorTaskCsvJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaExportCsvJobData.toParams(self)
        kparams.put("objectType", "KalturaEntryVendorTaskCsvJobData")
        kparams.addObjectIfDefined("filter", self.filter)
        return kparams

    def getFilter(self):
        return self.filter

    def setFilter(self, newFilter):
        self.filter = newFilter


# @package Kaltura
# @subpackage Client
class KalturaReachProfileBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            profileTypeEqual=NotImplemented,
            profileTypeIn=NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var KalturaReachProfileStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var KalturaReachProfileType
        self.profileTypeEqual = profileTypeEqual

        # @var string
        self.profileTypeIn = profileTypeIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaReachProfileStatus"), 
        'statusIn': getXmlNodeText, 
        'profileTypeEqual': (KalturaEnumsFactory.createInt, "KalturaReachProfileType"), 
        'profileTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRelatedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReachProfileBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedFilter.toParams(self)
        kparams.put("objectType", "KalturaReachProfileBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntEnumIfDefined("profileTypeEqual", self.profileTypeEqual)
        kparams.addStringIfDefined("profileTypeIn", self.profileTypeIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getProfileTypeEqual(self):
        return self.profileTypeEqual

    def setProfileTypeEqual(self, newProfileTypeEqual):
        self.profileTypeEqual = newProfileTypeEqual

    def getProfileTypeIn(self):
        return self.profileTypeIn

    def setProfileTypeIn(self, newProfileTypeIn):
        self.profileTypeIn = newProfileTypeIn


# @package Kaltura
# @subpackage Client
class KalturaReachReportInputFilter(KalturaReportInputFilter):
    def __init__(self,
            fromDate=NotImplemented,
            toDate=NotImplemented,
            fromDay=NotImplemented,
            toDay=NotImplemented,
            keywords=NotImplemented,
            searchInTags=NotImplemented,
            searchInAdminTags=NotImplemented,
            categories=NotImplemented,
            categoriesIdsIn=NotImplemented,
            customVar1In=NotImplemented,
            customVar2In=NotImplemented,
            customVar3In=NotImplemented,
            deviceIn=NotImplemented,
            countryIn=NotImplemented,
            regionIn=NotImplemented,
            citiesIn=NotImplemented,
            operatingSystemFamilyIn=NotImplemented,
            browserFamilyIn=NotImplemented,
            timeZoneOffset=NotImplemented,
            interval=NotImplemented,
            mediaTypeIn=NotImplemented,
            sourceTypeIn=NotImplemented,
            ownerIdsIn=NotImplemented,
            entryOperator=NotImplemented,
            entryCreatedAtGreaterThanOrEqual=NotImplemented,
            entryCreatedAtLessThanOrEqual=NotImplemented,
            entryIdIn=NotImplemented,
            serviceType=NotImplemented,
            serviceFeature=NotImplemented,
            turnAroundTime=NotImplemented):
        KalturaReportInputFilter.__init__(self,
            fromDate,
            toDate,
            fromDay,
            toDay,
            keywords,
            searchInTags,
            searchInAdminTags,
            categories,
            categoriesIdsIn,
            customVar1In,
            customVar2In,
            customVar3In,
            deviceIn,
            countryIn,
            regionIn,
            citiesIn,
            operatingSystemFamilyIn,
            browserFamilyIn,
            timeZoneOffset,
            interval,
            mediaTypeIn,
            sourceTypeIn,
            ownerIdsIn,
            entryOperator,
            entryCreatedAtGreaterThanOrEqual,
            entryCreatedAtLessThanOrEqual,
            entryIdIn)

        # @var KalturaVendorServiceType
        self.serviceType = serviceType

        # @var KalturaVendorServiceFeature
        self.serviceFeature = serviceFeature

        # @var KalturaVendorServiceTurnAroundTime
        self.turnAroundTime = turnAroundTime


    PROPERTY_LOADERS = {
        'serviceType': (KalturaEnumsFactory.createInt, "KalturaVendorServiceType"), 
        'serviceFeature': (KalturaEnumsFactory.createInt, "KalturaVendorServiceFeature"), 
        'turnAroundTime': (KalturaEnumsFactory.createInt, "KalturaVendorServiceTurnAroundTime"), 
    }

    def fromXml(self, node):
        KalturaReportInputFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReachReportInputFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReportInputFilter.toParams(self)
        kparams.put("objectType", "KalturaReachReportInputFilter")
        kparams.addIntEnumIfDefined("serviceType", self.serviceType)
        kparams.addIntEnumIfDefined("serviceFeature", self.serviceFeature)
        kparams.addIntEnumIfDefined("turnAroundTime", self.turnAroundTime)
        return kparams

    def getServiceType(self):
        return self.serviceType

    def setServiceType(self, newServiceType):
        self.serviceType = newServiceType

    def getServiceFeature(self):
        return self.serviceFeature

    def setServiceFeature(self, newServiceFeature):
        self.serviceFeature = newServiceFeature

    def getTurnAroundTime(self):
        return self.turnAroundTime

    def setTurnAroundTime(self, newTurnAroundTime):
        self.turnAroundTime = newTurnAroundTime


# @package Kaltura
# @subpackage Client
class KalturaTimeRangeVendorCredit(KalturaVendorCredit):
    def __init__(self,
            credit=NotImplemented,
            fromDate=NotImplemented,
            overageCredit=NotImplemented,
            addOn=NotImplemented,
            toDate=NotImplemented):
        KalturaVendorCredit.__init__(self,
            credit,
            fromDate,
            overageCredit,
            addOn)

        # @var int
        self.toDate = toDate


    PROPERTY_LOADERS = {
        'toDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorCredit.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTimeRangeVendorCredit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCredit.toParams(self)
        kparams.put("objectType", "KalturaTimeRangeVendorCredit")
        kparams.addIntIfDefined("toDate", self.toDate)
        return kparams

    def getToDate(self):
        return self.toDate

    def setToDate(self, newToDate):
        self.toDate = newToDate


# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.idNotIn = idNotIn

        # @var int
        self.vendorPartnerIdEqual = vendorPartnerIdEqual

        # @var string
        self.vendorPartnerIdIn = vendorPartnerIdIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual

        # @var KalturaVendorCatalogItemStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var KalturaVendorServiceType
        self.serviceTypeEqual = serviceTypeEqual

        # @var string
        self.serviceTypeIn = serviceTypeIn

        # @var KalturaVendorServiceFeature
        self.serviceFeatureEqual = serviceFeatureEqual

        # @var string
        self.serviceFeatureIn = serviceFeatureIn

        # @var KalturaVendorServiceTurnAroundTime
        self.turnAroundTimeEqual = turnAroundTimeEqual

        # @var string
        self.turnAroundTimeIn = turnAroundTimeIn


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'idNotIn': getXmlNodeText, 
        'vendorPartnerIdEqual': getXmlNodeInt, 
        'vendorPartnerIdIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemStatus"), 
        'statusIn': getXmlNodeText, 
        'serviceTypeEqual': (KalturaEnumsFactory.createInt, "KalturaVendorServiceType"), 
        'serviceTypeIn': getXmlNodeText, 
        'serviceFeatureEqual': (KalturaEnumsFactory.createInt, "KalturaVendorServiceFeature"), 
        'serviceFeatureIn': getXmlNodeText, 
        'turnAroundTimeEqual': (KalturaEnumsFactory.createInt, "KalturaVendorServiceTurnAroundTime"), 
        'turnAroundTimeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRelatedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCatalogItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorCatalogItemBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("idNotIn", self.idNotIn)
        kparams.addIntIfDefined("vendorPartnerIdEqual", self.vendorPartnerIdEqual)
        kparams.addStringIfDefined("vendorPartnerIdIn", self.vendorPartnerIdIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntEnumIfDefined("serviceTypeEqual", self.serviceTypeEqual)
        kparams.addStringIfDefined("serviceTypeIn", self.serviceTypeIn)
        kparams.addIntEnumIfDefined("serviceFeatureEqual", self.serviceFeatureEqual)
        kparams.addStringIfDefined("serviceFeatureIn", self.serviceFeatureIn)
        kparams.addIntEnumIfDefined("turnAroundTimeEqual", self.turnAroundTimeEqual)
        kparams.addStringIfDefined("turnAroundTimeIn", self.turnAroundTimeIn)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getIdNotIn(self):
        return self.idNotIn

    def setIdNotIn(self, newIdNotIn):
        self.idNotIn = newIdNotIn

    def getVendorPartnerIdEqual(self):
        return self.vendorPartnerIdEqual

    def setVendorPartnerIdEqual(self, newVendorPartnerIdEqual):
        self.vendorPartnerIdEqual = newVendorPartnerIdEqual

    def getVendorPartnerIdIn(self):
        return self.vendorPartnerIdIn

    def setVendorPartnerIdIn(self, newVendorPartnerIdIn):
        self.vendorPartnerIdIn = newVendorPartnerIdIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getServiceTypeEqual(self):
        return self.serviceTypeEqual

    def setServiceTypeEqual(self, newServiceTypeEqual):
        self.serviceTypeEqual = newServiceTypeEqual

    def getServiceTypeIn(self):
        return self.serviceTypeIn

    def setServiceTypeIn(self, newServiceTypeIn):
        self.serviceTypeIn = newServiceTypeIn

    def getServiceFeatureEqual(self):
        return self.serviceFeatureEqual

    def setServiceFeatureEqual(self, newServiceFeatureEqual):
        self.serviceFeatureEqual = newServiceFeatureEqual

    def getServiceFeatureIn(self):
        return self.serviceFeatureIn

    def setServiceFeatureIn(self, newServiceFeatureIn):
        self.serviceFeatureIn = newServiceFeatureIn

    def getTurnAroundTimeEqual(self):
        return self.turnAroundTimeEqual

    def setTurnAroundTimeEqual(self, newTurnAroundTimeEqual):
        self.turnAroundTimeEqual = newTurnAroundTimeEqual

    def getTurnAroundTimeIn(self):
        return self.turnAroundTimeIn

    def setTurnAroundTimeIn(self, newTurnAroundTimeIn):
        self.turnAroundTimeIn = newTurnAroundTimeIn


# @package Kaltura
# @subpackage Client
class KalturaVendorTranslationCatalogItem(KalturaVendorCaptionsCatalogItem):
    def __init__(self,
            id=NotImplemented,
            vendorPartnerId=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            status=NotImplemented,
            serviceType=NotImplemented,
            serviceFeature=NotImplemented,
            turnAroundTime=NotImplemented,
            pricing=NotImplemented,
            sourceLanguage=NotImplemented,
            outputFormat=NotImplemented,
            enableSpeakerId=NotImplemented,
            fixedPriceAddons=NotImplemented,
            targetLanguage=NotImplemented):
        KalturaVendorCaptionsCatalogItem.__init__(self,
            id,
            vendorPartnerId,
            name,
            systemName,
            createdAt,
            updatedAt,
            status,
            serviceType,
            serviceFeature,
            turnAroundTime,
            pricing,
            sourceLanguage,
            outputFormat,
            enableSpeakerId,
            fixedPriceAddons)

        # @var KalturaCatalogItemLanguage
        self.targetLanguage = targetLanguage


    PROPERTY_LOADERS = {
        'targetLanguage': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorTranslationCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorTranslationCatalogItem")
        kparams.addStringEnumIfDefined("targetLanguage", self.targetLanguage)
        return kparams

    def getTargetLanguage(self):
        return self.targetLanguage

    def setTargetLanguage(self, newTargetLanguage):
        self.targetLanguage = newTargetLanguage


# @package Kaltura
# @subpackage Client
class KalturaReachProfileFilter(KalturaReachProfileBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            profileTypeEqual=NotImplemented,
            profileTypeIn=NotImplemented):
        KalturaReachProfileBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            profileTypeEqual,
            profileTypeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaReachProfileBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReachProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReachProfileBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaReachProfileFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaReoccurringVendorCredit(KalturaTimeRangeVendorCredit):
    def __init__(self,
            credit=NotImplemented,
            fromDate=NotImplemented,
            overageCredit=NotImplemented,
            addOn=NotImplemented,
            toDate=NotImplemented,
            frequency=NotImplemented):
        KalturaTimeRangeVendorCredit.__init__(self,
            credit,
            fromDate,
            overageCredit,
            addOn,
            toDate)

        # @var KalturaVendorCreditRecurrenceFrequency
        self.frequency = frequency


    PROPERTY_LOADERS = {
        'frequency': (KalturaEnumsFactory.createString, "KalturaVendorCreditRecurrenceFrequency"), 
    }

    def fromXml(self, node):
        KalturaTimeRangeVendorCredit.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReoccurringVendorCredit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaTimeRangeVendorCredit.toParams(self)
        kparams.put("objectType", "KalturaReoccurringVendorCredit")
        kparams.addStringEnumIfDefined("frequency", self.frequency)
        return kparams

    def getFrequency(self):
        return self.frequency

    def setFrequency(self, newFrequency):
        self.frequency = newFrequency


# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemFilter(KalturaVendorCatalogItemBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented,
            partnerIdEqual=NotImplemented):
        KalturaVendorCatalogItemBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            vendorPartnerIdEqual,
            vendorPartnerIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serviceTypeEqual,
            serviceTypeIn,
            serviceFeatureEqual,
            serviceFeatureIn,
            turnAroundTimeEqual,
            turnAroundTimeIn)

        # @var int
        self.partnerIdEqual = partnerIdEqual


    PROPERTY_LOADERS = {
        'partnerIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorCatalogItemFilter")
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        return kparams

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual


# @package Kaltura
# @subpackage Client
class KalturaVendorCaptionsCatalogItemBaseFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            sourceLanguageEqual=NotImplemented,
            sourceLanguageIn=NotImplemented,
            outputFormatEqual=NotImplemented,
            outputFormatIn=NotImplemented):
        KalturaVendorCatalogItemFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            vendorPartnerIdEqual,
            vendorPartnerIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serviceTypeEqual,
            serviceTypeIn,
            serviceFeatureEqual,
            serviceFeatureIn,
            turnAroundTimeEqual,
            turnAroundTimeIn,
            partnerIdEqual)

        # @var KalturaCatalogItemLanguage
        self.sourceLanguageEqual = sourceLanguageEqual

        # @var string
        self.sourceLanguageIn = sourceLanguageIn

        # @var KalturaVendorCatalogItemOutputFormat
        self.outputFormatEqual = outputFormatEqual

        # @var string
        self.outputFormatIn = outputFormatIn


    PROPERTY_LOADERS = {
        'sourceLanguageEqual': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'sourceLanguageIn': getXmlNodeText, 
        'outputFormatEqual': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemOutputFormat"), 
        'outputFormatIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCaptionsCatalogItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorCaptionsCatalogItemBaseFilter")
        kparams.addStringEnumIfDefined("sourceLanguageEqual", self.sourceLanguageEqual)
        kparams.addStringIfDefined("sourceLanguageIn", self.sourceLanguageIn)
        kparams.addIntEnumIfDefined("outputFormatEqual", self.outputFormatEqual)
        kparams.addStringIfDefined("outputFormatIn", self.outputFormatIn)
        return kparams

    def getSourceLanguageEqual(self):
        return self.sourceLanguageEqual

    def setSourceLanguageEqual(self, newSourceLanguageEqual):
        self.sourceLanguageEqual = newSourceLanguageEqual

    def getSourceLanguageIn(self):
        return self.sourceLanguageIn

    def setSourceLanguageIn(self, newSourceLanguageIn):
        self.sourceLanguageIn = newSourceLanguageIn

    def getOutputFormatEqual(self):
        return self.outputFormatEqual

    def setOutputFormatEqual(self, newOutputFormatEqual):
        self.outputFormatEqual = newOutputFormatEqual

    def getOutputFormatIn(self):
        return self.outputFormatIn

    def setOutputFormatIn(self, newOutputFormatIn):
        self.outputFormatIn = newOutputFormatIn


# @package Kaltura
# @subpackage Client
class KalturaVendorAlignmentCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            sourceLanguageEqual=NotImplemented,
            sourceLanguageIn=NotImplemented,
            outputFormatEqual=NotImplemented,
            outputFormatIn=NotImplemented):
        KalturaVendorCaptionsCatalogItemBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            vendorPartnerIdEqual,
            vendorPartnerIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serviceTypeEqual,
            serviceTypeIn,
            serviceFeatureEqual,
            serviceFeatureIn,
            turnAroundTimeEqual,
            turnAroundTimeIn,
            partnerIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorAlignmentCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorAlignmentCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorAudioDescriptionCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            sourceLanguageEqual=NotImplemented,
            sourceLanguageIn=NotImplemented,
            outputFormatEqual=NotImplemented,
            outputFormatIn=NotImplemented):
        KalturaVendorCaptionsCatalogItemBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            vendorPartnerIdEqual,
            vendorPartnerIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serviceTypeEqual,
            serviceTypeIn,
            serviceFeatureEqual,
            serviceFeatureIn,
            turnAroundTimeEqual,
            turnAroundTimeIn,
            partnerIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorAudioDescriptionCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorAudioDescriptionCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorCaptionsCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            sourceLanguageEqual=NotImplemented,
            sourceLanguageIn=NotImplemented,
            outputFormatEqual=NotImplemented,
            outputFormatIn=NotImplemented):
        KalturaVendorCaptionsCatalogItemBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            vendorPartnerIdEqual,
            vendorPartnerIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serviceTypeEqual,
            serviceTypeIn,
            serviceFeatureEqual,
            serviceFeatureIn,
            turnAroundTimeEqual,
            turnAroundTimeIn,
            partnerIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCaptionsCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorCaptionsCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorTranslationCatalogItemBaseFilter(KalturaVendorCaptionsCatalogItemFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            sourceLanguageEqual=NotImplemented,
            sourceLanguageIn=NotImplemented,
            outputFormatEqual=NotImplemented,
            outputFormatIn=NotImplemented,
            targetLanguageEqual=NotImplemented,
            targetLanguageIn=NotImplemented):
        KalturaVendorCaptionsCatalogItemFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            vendorPartnerIdEqual,
            vendorPartnerIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serviceTypeEqual,
            serviceTypeIn,
            serviceFeatureEqual,
            serviceFeatureIn,
            turnAroundTimeEqual,
            turnAroundTimeIn,
            partnerIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn)

        # @var KalturaCatalogItemLanguage
        self.targetLanguageEqual = targetLanguageEqual

        # @var string
        self.targetLanguageIn = targetLanguageIn


    PROPERTY_LOADERS = {
        'targetLanguageEqual': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'targetLanguageIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorTranslationCatalogItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorTranslationCatalogItemBaseFilter")
        kparams.addStringEnumIfDefined("targetLanguageEqual", self.targetLanguageEqual)
        kparams.addStringIfDefined("targetLanguageIn", self.targetLanguageIn)
        return kparams

    def getTargetLanguageEqual(self):
        return self.targetLanguageEqual

    def setTargetLanguageEqual(self, newTargetLanguageEqual):
        self.targetLanguageEqual = newTargetLanguageEqual

    def getTargetLanguageIn(self):
        return self.targetLanguageIn

    def setTargetLanguageIn(self, newTargetLanguageIn):
        self.targetLanguageIn = newTargetLanguageIn


# @package Kaltura
# @subpackage Client
class KalturaVendorTranslationCatalogItemFilter(KalturaVendorTranslationCatalogItemBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            idNotIn=NotImplemented,
            vendorPartnerIdEqual=NotImplemented,
            vendorPartnerIdIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            serviceTypeEqual=NotImplemented,
            serviceTypeIn=NotImplemented,
            serviceFeatureEqual=NotImplemented,
            serviceFeatureIn=NotImplemented,
            turnAroundTimeEqual=NotImplemented,
            turnAroundTimeIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            sourceLanguageEqual=NotImplemented,
            sourceLanguageIn=NotImplemented,
            outputFormatEqual=NotImplemented,
            outputFormatIn=NotImplemented,
            targetLanguageEqual=NotImplemented,
            targetLanguageIn=NotImplemented):
        KalturaVendorTranslationCatalogItemBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            idNotIn,
            vendorPartnerIdEqual,
            vendorPartnerIdIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            statusEqual,
            statusIn,
            serviceTypeEqual,
            serviceTypeIn,
            serviceFeatureEqual,
            serviceFeatureIn,
            turnAroundTimeEqual,
            turnAroundTimeIn,
            partnerIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn,
            targetLanguageEqual,
            targetLanguageIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorTranslationCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorTranslationCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTranslationCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorTranslationCatalogItemFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemService(KalturaServiceBase):
    """Vendor Catalog Item Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, vendorCatalogItem):
        """Allows you to add an service catalog item"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("vendorCatalogItem", vendorCatalogItem)
        self.client.queueServiceActionCall("reach_vendorcatalogitem", "add", "KalturaVendorCatalogItem", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVendorCatalogItem')

    def delete(self, id):
        """Delete vedor catalog item object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_vendorcatalogitem", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, id):
        """Retrieve specific catalog item by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_vendorcatalogitem", "get", "KalturaVendorCatalogItem", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVendorCatalogItem')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List KalturaVendorCatalogItem objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("reach_vendorcatalogitem", "list", "KalturaVendorCatalogItemListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVendorCatalogItemListResponse')

    def update(self, id, vendorCatalogItem):
        """Update an existing vedor catalog item object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("vendorCatalogItem", vendorCatalogItem)
        self.client.queueServiceActionCall("reach_vendorcatalogitem", "update", "KalturaVendorCatalogItem", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVendorCatalogItem')

    def updateStatus(self, id, status):
        """Update vendor catalog item status by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("status", status);
        self.client.queueServiceActionCall("reach_vendorcatalogitem", "updateStatus", "KalturaVendorCatalogItem", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVendorCatalogItem')


# @package Kaltura
# @subpackage Client
class KalturaReachProfileService(KalturaServiceBase):
    """Reach Profile Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, reachProfile):
        """Allows you to add a partner specific reach profile"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("reachProfile", reachProfile)
        self.client.queueServiceActionCall("reach_reachprofile", "add", "KalturaReachProfile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaReachProfile')

    def delete(self, id):
        """Delete vednor profile by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_reachprofile", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def get(self, id):
        """Retrieve specific reach profile by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_reachprofile", "get", "KalturaReachProfile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaReachProfile')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List KalturaReachProfile objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("reach_reachprofile", "list", "KalturaReachProfileListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaReachProfileListResponse')

    def syncCredit(self, reachProfileId):
        """sync vednor profile credit"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("reachProfileId", reachProfileId);
        self.client.queueServiceActionCall("reach_reachprofile", "syncCredit", "KalturaReachProfile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaReachProfile')

    def update(self, id, reachProfile):
        """Update an existing reach profile object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("reachProfile", reachProfile)
        self.client.queueServiceActionCall("reach_reachprofile", "update", "KalturaReachProfile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaReachProfile')

    def updateStatus(self, id, status):
        """Update reach profile status by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("status", status);
        self.client.queueServiceActionCall("reach_reachprofile", "updateStatus", "KalturaReachProfile", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaReachProfile')


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskService(KalturaServiceBase):
    """Entry Vendor Task Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def abort(self, id, abortReason = NotImplemented):
        """Cancel entry task. will only occur for task in PENDING or PENDING_MODERATION status"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addStringIfDefined("abortReason", abortReason)
        self.client.queueServiceActionCall("reach_entryvendortask", "abort", "KalturaEntryVendorTask", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTask')

    def add(self, entryVendorTask):
        """Allows you to add a entry vendor task"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("entryVendorTask", entryVendorTask)
        self.client.queueServiceActionCall("reach_entryvendortask", "add", "KalturaEntryVendorTask", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTask')

    def approve(self, id):
        """Approve entry vendor task for execution."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_entryvendortask", "approve", "KalturaEntryVendorTask", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTask')

    def exportToCsv(self, filter):
        """add batch job that sends an email with a link to download an updated CSV that contains list of users"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("reach_entryvendortask", "exportToCsv", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def extendAccessKey(self, id):
        """Extend access key in case the existing one has expired."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_entryvendortask", "extendAccessKey", "KalturaEntryVendorTask", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTask')

    def get(self, id):
        """Retrieve specific entry vendor task by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_entryvendortask", "get", "KalturaEntryVendorTask", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTask')

    def getJobs(self, filter = NotImplemented, pager = NotImplemented):
        """get KalturaEntryVendorTask objects for specific vendor partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("reach_entryvendortask", "getJobs", "KalturaEntryVendorTaskListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTaskListResponse')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List KalturaEntryVendorTask objects"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("reach_entryvendortask", "list", "KalturaEntryVendorTaskListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTaskListResponse')

    def reject(self, id, rejectReason = NotImplemented):
        """Reject entry vendor task for execution."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addStringIfDefined("rejectReason", rejectReason)
        self.client.queueServiceActionCall("reach_entryvendortask", "reject", "KalturaEntryVendorTask", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTask')

    def serveCsv(self, id):
        """Will serve a requested csv"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("reach_entryvendortask", "serveCsv", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def update(self, id, entryVendorTask):
        """Update entry vendor task. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("entryVendorTask", entryVendorTask)
        self.client.queueServiceActionCall("reach_entryvendortask", "update", "KalturaEntryVendorTask", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTask')

    def updateJob(self, id, entryVendorTask):
        """Update entry vendor task. Only the properties that were set will be updated."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("entryVendorTask", entryVendorTask)
        self.client.queueServiceActionCall("reach_entryvendortask", "updateJob", "KalturaEntryVendorTask", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaEntryVendorTask')


# @package Kaltura
# @subpackage Client
class KalturaPartnerCatalogItemService(KalturaServiceBase):
    """Partner Catalog Item Service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, id):
        """Assign existing catalogItem to specific account"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_partnercatalogitem", "add", "KalturaVendorCatalogItem", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaVendorCatalogItem')

    def delete(self, id):
        """Remove existing catalogItem from specific account"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("reach_partnercatalogitem", "delete", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

########## main ##########
class KalturaReachClientPlugin(KalturaClientPlugin):
    # KalturaReachClientPlugin
    instance = None

    # @return KalturaReachClientPlugin
    @staticmethod
    def get():
        if KalturaReachClientPlugin.instance == None:
            KalturaReachClientPlugin.instance = KalturaReachClientPlugin()
        return KalturaReachClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'vendorCatalogItem': KalturaVendorCatalogItemService,
            'reachProfile': KalturaReachProfileService,
            'entryVendorTask': KalturaEntryVendorTaskService,
            'PartnerCatalogItem': KalturaPartnerCatalogItemService,
        }

    def getEnums(self):
        return {
            'KalturaEntryVendorTaskCreationMode': KalturaEntryVendorTaskCreationMode,
            'KalturaEntryVendorTaskStatus': KalturaEntryVendorTaskStatus,
            'KalturaReachProfileContentDeletionPolicy': KalturaReachProfileContentDeletionPolicy,
            'KalturaReachProfileStatus': KalturaReachProfileStatus,
            'KalturaReachProfileType': KalturaReachProfileType,
            'KalturaVendorCatalogItemOutputFormat': KalturaVendorCatalogItemOutputFormat,
            'KalturaVendorCatalogItemStatus': KalturaVendorCatalogItemStatus,
            'KalturaVendorServiceFeature': KalturaVendorServiceFeature,
            'KalturaVendorServiceTurnAroundTime': KalturaVendorServiceTurnAroundTime,
            'KalturaVendorServiceType': KalturaVendorServiceType,
            'KalturaVendorTaskProcessingRegion': KalturaVendorTaskProcessingRegion,
            'KalturaCatalogItemLanguage': KalturaCatalogItemLanguage,
            'KalturaEntryVendorTaskOrderBy': KalturaEntryVendorTaskOrderBy,
            'KalturaReachProfileOrderBy': KalturaReachProfileOrderBy,
            'KalturaVendorCaptionsCatalogItemOrderBy': KalturaVendorCaptionsCatalogItemOrderBy,
            'KalturaVendorCatalogItemOrderBy': KalturaVendorCatalogItemOrderBy,
            'KalturaVendorCatalogItemPriceFunction': KalturaVendorCatalogItemPriceFunction,
            'KalturaVendorCreditRecurrenceFrequency': KalturaVendorCreditRecurrenceFrequency,
            'KalturaVendorTranslationCatalogItemOrderBy': KalturaVendorTranslationCatalogItemOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaBaseVendorCredit': KalturaBaseVendorCredit,
            'KalturaDictionary': KalturaDictionary,
            'KalturaVendorTaskData': KalturaVendorTaskData,
            'KalturaEntryVendorTask': KalturaEntryVendorTask,
            'KalturaReachProfile': KalturaReachProfile,
            'KalturaVendorCatalogItemPricing': KalturaVendorCatalogItemPricing,
            'KalturaVendorCatalogItem': KalturaVendorCatalogItem,
            'KalturaAddEntryVendorTaskAction': KalturaAddEntryVendorTaskAction,
            'KalturaAlignmentVendorTaskData': KalturaAlignmentVendorTaskData,
            'KalturaCatalogItemAdvancedFilter': KalturaCatalogItemAdvancedFilter,
            'KalturaCategoryEntryCondition': KalturaCategoryEntryCondition,
            'KalturaEntryVendorTaskListResponse': KalturaEntryVendorTaskListResponse,
            'KalturaReachProfileListResponse': KalturaReachProfileListResponse,
            'KalturaUnlimitedVendorCredit': KalturaUnlimitedVendorCredit,
            'KalturaVendorAlignmentCatalogItem': KalturaVendorAlignmentCatalogItem,
            'KalturaVendorAudioDescriptionCatalogItem': KalturaVendorAudioDescriptionCatalogItem,
            'KalturaVendorCaptionsCatalogItem': KalturaVendorCaptionsCatalogItem,
            'KalturaVendorCatalogItemListResponse': KalturaVendorCatalogItemListResponse,
            'KalturaVendorCredit': KalturaVendorCredit,
            'KalturaEntryVendorTaskBaseFilter': KalturaEntryVendorTaskBaseFilter,
            'KalturaEntryVendorTaskFilter': KalturaEntryVendorTaskFilter,
            'KalturaEntryVendorTaskCsvJobData': KalturaEntryVendorTaskCsvJobData,
            'KalturaReachProfileBaseFilter': KalturaReachProfileBaseFilter,
            'KalturaReachReportInputFilter': KalturaReachReportInputFilter,
            'KalturaTimeRangeVendorCredit': KalturaTimeRangeVendorCredit,
            'KalturaVendorCatalogItemBaseFilter': KalturaVendorCatalogItemBaseFilter,
            'KalturaVendorTranslationCatalogItem': KalturaVendorTranslationCatalogItem,
            'KalturaReachProfileFilter': KalturaReachProfileFilter,
            'KalturaReoccurringVendorCredit': KalturaReoccurringVendorCredit,
            'KalturaVendorCatalogItemFilter': KalturaVendorCatalogItemFilter,
            'KalturaVendorCaptionsCatalogItemBaseFilter': KalturaVendorCaptionsCatalogItemBaseFilter,
            'KalturaVendorAlignmentCatalogItemFilter': KalturaVendorAlignmentCatalogItemFilter,
            'KalturaVendorAudioDescriptionCatalogItemFilter': KalturaVendorAudioDescriptionCatalogItemFilter,
            'KalturaVendorCaptionsCatalogItemFilter': KalturaVendorCaptionsCatalogItemFilter,
            'KalturaVendorTranslationCatalogItemBaseFilter': KalturaVendorTranslationCatalogItemBaseFilter,
            'KalturaVendorTranslationCatalogItemFilter': KalturaVendorTranslationCatalogItemFilter,
        }

    # @return string
    def getName(self):
        return 'reach'

