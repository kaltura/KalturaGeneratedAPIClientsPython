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
from .EventNotification import *
from .BulkUpload import *
from .Caption import *
from .Schedule import *
from .Transcript import *
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
class KalturaEntryObjectType(object):
    ENTRY = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

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
    SCHEDULED = 9

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
    VTT = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemStage(object):
    PRODUCTION = 1
    QA = 2

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
    CHAPTERING = 5
    INTELLIGENT_TAGGING = 6
    DUBBING = 7
    LIVE_CAPTION = 8
    EXTENDED_AUDIO_DESCRIPTION = 9
    CLIPS = 10
    LIVE_TRANSLATION = 11
    QUIZ = 12
    SUMMARY = 13
    VIDEO_ANALYSIS = 14
    MODERATION = 15
    METADATA_ENRICHMENT = 16

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorServiceTurnAroundTime(object):
    BEST_EFFORT = -1
    IMMEDIATE = 0
    ONE_BUSINESS_DAY = 1
    TWO_BUSINESS_DAYS = 2
    THREE_BUSINESS_DAYS = 3
    FOUR_BUSINESS_DAYS = 4
    FIVE_BUSINESS_DAYS = 5
    SIX_BUSINESS_DAYS = 6
    SEVEN_BUSINESS_DAYS = 7
    THIRTY_MINUTES = 1800
    TWO_HOURS = 7200
    THREE_HOURS = 10800
    SIX_HOURS = 21600
    EIGHT_HOURS = 28800
    TWELVE_HOURS = 43200
    TWENTY_FOUR_HOURS = 86400
    FORTY_EIGHT_HOURS = 172800
    FOUR_DAYS = 345600
    FIVE_DAYS = 432000
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
    CA = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaVendorVideoAnalysisType(object):
    OCR = 1

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCatalogItemLanguage(object):
    AF = "Afrikaans"
    AR = "Arabic"
    AUTO_DETECT = "Auto Detect"
    AZ = "Azerbaijani"
    BA = "Bashkir"
    EU = "Basque"
    BN = "Bengali (Bangla)"
    BS = "Bosnian"
    BG = "Bulgarian"
    MY = "Burmese"
    BE = "Byelorussian (Belarusian)"
    KM = "Cambodian"
    YUE = "Cantonese"
    CA = "Catalan"
    ZH = "Chinese"
    HR = "Croatian"
    CS = "Czech"
    DA = "Danish"
    NL = "Dutch"
    EN = "English"
    EN_US = "English (American)"
    EN_AU = "English (Australian)"
    EN_GB = "English (British)"
    EO = "Esperanto"
    ET = "Estonian"
    FA = "Farsi"
    FI = "Finnish"
    FR = "French"
    FR_CA = "French (Canada)"
    GD = "Gaelic (Scottish)"
    GL = "Galician"
    KA = "Georgian"
    DE = "German"
    EL = "Greek"
    GU = "Gujarati"
    HE = "Hebrew"
    HI = "Hindi"
    HU = "Hungarian"
    IS = "Icelandic"
    IN = "Indonesian"
    IA = "Interlingua"
    GA = "Irish"
    IT = "Italian"
    JA = "Japanese"
    JV = "Javanese"
    KN = "Kannada"
    KK = "Kazakh"
    KO = "Korean"
    LO = "Laothian"
    LV = "Latvian (Lettish)"
    LT = "Lithuanian"
    MK = "Macedonian"
    MS = "Malay"
    ML = "Malayalam"
    CMN = "Mandarin Chinese"
    MR = "Marathi"
    MN = "Mongolian"
    NE = "Nepali"
    NO = "Norwegian"
    FA_IR = "Persian (Iran)"
    PL = "Polish"
    PT = "Portuguese"
    PT_BR = "Portuguese (Brazil)"
    PA = "Punjabi"
    RO = "Romanian"
    RU = "Russian"
    SR = "Serbian"
    ZH_CN = "Simplified Chinese"
    SI = "Sinhalese"
    SK = "Slovak"
    SK_SK = "Slovakian"
    SL = "Slovenian"
    ES = "Spanish"
    ES_XL = "Spanish (Latin America)"
    SU = "Sundanese"
    SW = "Swahili (Kiswahili)"
    SV = "Swedish"
    TL = "Tagalog"
    ZH_TW = "Taiwanese Mandarin"
    TA = "Tamil"
    TE = "Telugu"
    TH = "Thai"
    ZH_HK = "Traditional Chinese"
    TR = "Turkish"
    UG = "Uighur"
    UK = "Ukrainian"
    UR = "Urdu"
    UZ = "Uzbek"
    VI = "Vietnamese"
    CY = "Welsh"
    XH = "Xhosa"
    ZU = "Zulu"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    EXPECTED_FINISH_TIME_ASC = "+expectedFinishTime"
    FINISH_TIME_ASC = "+finishTime"
    ID_ASC = "+id"
    PRICE_ASC = "+price"
    QUEUE_TIME_ASC = "+queueTime"
    STATUS_ASC = "+status"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    EXPECTED_FINISH_TIME_DESC = "-expectedFinishTime"
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
class KalturaReachVendorEngineType(object):
    OPEN_CALAIS = "OpenCalaisReachVendor.OPEN_CALAIS"
    HELLO_WORLD = "ReachInternal.HELLO_WORLD"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSummaryWritingStyleTaskData(object):
    CASUAL = "casual"
    FORMAL = "formal"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTypeOfSummaryTaskData(object):
    CONCISE = "concise"
    DETAILED = "detailed"
    EXTENSIVE = "extensive"

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
    PRICE_PER_HOUR = "kReachUtils::calcPricePerHour"
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
            language = NotImplemented,
            data = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaCatalogItemLanguage
        self.language = language

        # @var str
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
    def __init__(self,
            entryDuration = NotImplemented):
        KalturaObjectBase.__init__(self)

        # The duration of the entry for which the task was created for in milliseconds
        # @var int
        # @readonly
        self.entryDuration = entryDuration


    PROPERTY_LOADERS = {
        'entryDuration': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaVendorTaskData")
        return kparams

    def getEntryDuration(self):
        return self.entryDuration


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTask(KalturaObjectBase):
    def __init__(self,
            id = NotImplemented,
            partnerId = NotImplemented,
            vendorPartnerId = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            queueTime = NotImplemented,
            finishTime = NotImplemented,
            entryId = NotImplemented,
            status = NotImplemented,
            reachProfileId = NotImplemented,
            catalogItemId = NotImplemented,
            price = NotImplemented,
            userId = NotImplemented,
            entryObjectType = NotImplemented,
            moderatingUser = NotImplemented,
            errDescription = NotImplemented,
            accessKey = NotImplemented,
            version = NotImplemented,
            notes = NotImplemented,
            dictionary = NotImplemented,
            context = NotImplemented,
            accuracy = NotImplemented,
            outputObjectId = NotImplemented,
            partnerData = NotImplemented,
            creationMode = NotImplemented,
            taskJobData = NotImplemented,
            expectedFinishTime = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            externalTaskId = NotImplemented):
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

        # @var str
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
        # @var str
        # @readonly
        self.userId = userId

        # @var KalturaEntryObjectType
        # @insertonly
        self.entryObjectType = entryObjectType

        # The user ID that approved this task for execution (in case moderation is requested)
        # @var str
        # @readonly
        self.moderatingUser = moderatingUser

        # Err description provided by provider in case job execution has failed
        # @var str
        self.errDescription = errDescription

        # Access key generated by Kaltura to allow vendors to ingest the end result to the destination
        # @var str
        # @readonly
        self.accessKey = accessKey

        # Vendor generated by Kaltura representing the entry vendor task version correlated to the entry version
        # @var str
        # @readonly
        self.version = version

        # User generated notes that should be taken into account by the vendor while executing the task
        # @var str
        self.notes = notes

        # @var str
        # @readonly
        self.dictionary = dictionary

        # Task context
        # @var str
        self.context = context

        # Task result accuracy percentage
        # @var int
        self.accuracy = accuracy

        # Task main object generated by executing the task
        # @var str
        self.outputObjectId = outputObjectId

        # Json object containing extra task data required by the requester
        # @var str
        self.partnerData = partnerData

        # Task creation mode
        # @var KalturaEntryVendorTaskCreationMode
        # @readonly
        self.creationMode = creationMode

        # @var KalturaVendorTaskData
        self.taskJobData = taskJobData

        # @var int
        # @readonly
        self.expectedFinishTime = expectedFinishTime

        # @var KalturaVendorServiceType
        # @readonly
        self.serviceType = serviceType

        # @var KalturaVendorServiceFeature
        # @readonly
        self.serviceFeature = serviceFeature

        # @var KalturaVendorServiceTurnAroundTime
        # @readonly
        self.turnAroundTime = turnAroundTime

        # The vendor's task internal Id
        # @var str
        self.externalTaskId = externalTaskId


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
        'entryObjectType': (KalturaEnumsFactory.createInt, "KalturaEntryObjectType"), 
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
        'expectedFinishTime': getXmlNodeInt, 
        'serviceType': (KalturaEnumsFactory.createInt, "KalturaVendorServiceType"), 
        'serviceFeature': (KalturaEnumsFactory.createInt, "KalturaVendorServiceFeature"), 
        'turnAroundTime': (KalturaEnumsFactory.createInt, "KalturaVendorServiceTurnAroundTime"), 
        'externalTaskId': getXmlNodeText, 
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
        kparams.addIntEnumIfDefined("entryObjectType", self.entryObjectType)
        kparams.addStringIfDefined("errDescription", self.errDescription)
        kparams.addStringIfDefined("notes", self.notes)
        kparams.addStringIfDefined("context", self.context)
        kparams.addIntIfDefined("accuracy", self.accuracy)
        kparams.addStringIfDefined("outputObjectId", self.outputObjectId)
        kparams.addStringIfDefined("partnerData", self.partnerData)
        kparams.addObjectIfDefined("taskJobData", self.taskJobData)
        kparams.addStringIfDefined("externalTaskId", self.externalTaskId)
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

    def getEntryObjectType(self):
        return self.entryObjectType

    def setEntryObjectType(self, newEntryObjectType):
        self.entryObjectType = newEntryObjectType

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

    def getExpectedFinishTime(self):
        return self.expectedFinishTime

    def getServiceType(self):
        return self.serviceType

    def getServiceFeature(self):
        return self.serviceFeature

    def getTurnAroundTime(self):
        return self.turnAroundTime

    def getExternalTaskId(self):
        return self.externalTaskId

    def setExternalTaskId(self, newExternalTaskId):
        self.externalTaskId = newExternalTaskId


# @package Kaltura
# @subpackage Client
class KalturaReachProfile(KalturaObjectBase):
    def __init__(self,
            id = NotImplemented,
            name = NotImplemented,
            partnerId = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            profileType = NotImplemented,
            defaultOutputFormat = NotImplemented,
            enableMachineModeration = NotImplemented,
            enableHumanModeration = NotImplemented,
            autoDisplayMachineCaptionsOnPlayer = NotImplemented,
            autoDisplayHumanCaptionsOnPlayer = NotImplemented,
            enableMetadataExtraction = NotImplemented,
            enableSpeakerChangeIndication = NotImplemented,
            enableAudioTags = NotImplemented,
            enableProfanityRemoval = NotImplemented,
            maxCharactersPerCaptionLine = NotImplemented,
            labelAdditionForMachineServiceType = NotImplemented,
            labelAdditionForHumanServiceType = NotImplemented,
            contentDeletionPolicy = NotImplemented,
            rules = NotImplemented,
            credit = NotImplemented,
            usedCredit = NotImplemented,
            dictionaries = NotImplemented,
            flavorParamsIds = NotImplemented,
            vendorTaskProcessingRegion = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # The name of the profile
        # @var str
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

        # @var str
        self.labelAdditionForMachineServiceType = labelAdditionForMachineServiceType

        # @var str
        self.labelAdditionForHumanServiceType = labelAdditionForHumanServiceType

        # @var KalturaReachProfileContentDeletionPolicy
        self.contentDeletionPolicy = contentDeletionPolicy

        # @var List[KalturaRule]
        self.rules = rules

        # @var KalturaBaseVendorCredit
        self.credit = credit

        # @var float
        # @readonly
        self.usedCredit = usedCredit

        # @var List[KalturaDictionary]
        self.dictionaries = dictionaries

        # Comma separated flavorParamsIds that the vendor should look for it matching asset when trying to download the asset
        # @var str
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
        'labelAdditionForMachineServiceType': getXmlNodeText, 
        'labelAdditionForHumanServiceType': getXmlNodeText, 
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
        kparams.addStringIfDefined("labelAdditionForMachineServiceType", self.labelAdditionForMachineServiceType)
        kparams.addStringIfDefined("labelAdditionForHumanServiceType", self.labelAdditionForHumanServiceType)
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

    def getLabelAdditionForMachineServiceType(self):
        return self.labelAdditionForMachineServiceType

    def setLabelAdditionForMachineServiceType(self, newLabelAdditionForMachineServiceType):
        self.labelAdditionForMachineServiceType = newLabelAdditionForMachineServiceType

    def getLabelAdditionForHumanServiceType(self):
        return self.labelAdditionForHumanServiceType

    def setLabelAdditionForHumanServiceType(self, newLabelAdditionForHumanServiceType):
        self.labelAdditionForHumanServiceType = newLabelAdditionForHumanServiceType

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
            pricePerUnit = NotImplemented,
            priceFunction = NotImplemented):
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
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var int
        self.vendorPartnerId = vendorPartnerId

        # @var str
        self.name = name

        # @var str
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

        # Property showing the catalog item's engine type, in case a vendor can offer the same service via different engines.
        # @var KalturaReachVendorEngineType
        self.engineType = engineType

        # @var KalturaCatalogItemLanguage
        self.sourceLanguage = sourceLanguage

        # @var bool
        self.allowResubmission = allowResubmission

        # @var bool
        self.requiresOverages = requiresOverages

        # @var str
        self.vendorData = vendorData

        # @var KalturaVendorCatalogItemStage
        self.stage = stage

        # @var int
        self.lastBulkUpdateId = lastBulkUpdateId

        # @var str
        self.contract = contract

        # @var str
        self.createdBy = createdBy

        # @var str
        self.notes = notes

        # @var int
        self.partnerId = partnerId

        # @var int
        self.defaultReachProfileId = defaultReachProfileId

        # @var str
        self.adminTagsToExclude = adminTagsToExclude


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
        'engineType': (KalturaEnumsFactory.createString, "KalturaReachVendorEngineType"), 
        'sourceLanguage': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'allowResubmission': getXmlNodeBool, 
        'requiresOverages': getXmlNodeBool, 
        'vendorData': getXmlNodeText, 
        'stage': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemStage"), 
        'lastBulkUpdateId': getXmlNodeInt, 
        'contract': getXmlNodeText, 
        'createdBy': getXmlNodeText, 
        'notes': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'defaultReachProfileId': getXmlNodeInt, 
        'adminTagsToExclude': getXmlNodeText, 
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
        kparams.addStringEnumIfDefined("engineType", self.engineType)
        kparams.addStringEnumIfDefined("sourceLanguage", self.sourceLanguage)
        kparams.addBoolIfDefined("allowResubmission", self.allowResubmission)
        kparams.addBoolIfDefined("requiresOverages", self.requiresOverages)
        kparams.addStringIfDefined("vendorData", self.vendorData)
        kparams.addIntEnumIfDefined("stage", self.stage)
        kparams.addIntIfDefined("lastBulkUpdateId", self.lastBulkUpdateId)
        kparams.addStringIfDefined("contract", self.contract)
        kparams.addStringIfDefined("createdBy", self.createdBy)
        kparams.addStringIfDefined("notes", self.notes)
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addIntIfDefined("defaultReachProfileId", self.defaultReachProfileId)
        kparams.addStringIfDefined("adminTagsToExclude", self.adminTagsToExclude)
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

    def getEngineType(self):
        return self.engineType

    def setEngineType(self, newEngineType):
        self.engineType = newEngineType

    def getSourceLanguage(self):
        return self.sourceLanguage

    def setSourceLanguage(self, newSourceLanguage):
        self.sourceLanguage = newSourceLanguage

    def getAllowResubmission(self):
        return self.allowResubmission

    def setAllowResubmission(self, newAllowResubmission):
        self.allowResubmission = newAllowResubmission

    def getRequiresOverages(self):
        return self.requiresOverages

    def setRequiresOverages(self, newRequiresOverages):
        self.requiresOverages = newRequiresOverages

    def getVendorData(self):
        return self.vendorData

    def setVendorData(self, newVendorData):
        self.vendorData = newVendorData

    def getStage(self):
        return self.stage

    def setStage(self, newStage):
        self.stage = newStage

    def getLastBulkUpdateId(self):
        return self.lastBulkUpdateId

    def setLastBulkUpdateId(self, newLastBulkUpdateId):
        self.lastBulkUpdateId = newLastBulkUpdateId

    def getContract(self):
        return self.contract

    def setContract(self, newContract):
        self.contract = newContract

    def getCreatedBy(self):
        return self.createdBy

    def setCreatedBy(self, newCreatedBy):
        self.createdBy = newCreatedBy

    def getNotes(self):
        return self.notes

    def setNotes(self, newNotes):
        self.notes = newNotes

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getDefaultReachProfileId(self):
        return self.defaultReachProfileId

    def setDefaultReachProfileId(self, newDefaultReachProfileId):
        self.defaultReachProfileId = newDefaultReachProfileId

    def getAdminTagsToExclude(self):
        return self.adminTagsToExclude

    def setAdminTagsToExclude(self, newAdminTagsToExclude):
        self.adminTagsToExclude = newAdminTagsToExclude


# @package Kaltura
# @subpackage Client
class KalturaAddEntryVendorTaskAction(KalturaRuleAction):
    def __init__(self,
            type = NotImplemented,
            catalogItemIds = NotImplemented):
        KalturaRuleAction.__init__(self,
            type)

        # Catalog Item Id
        # @var str
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
class KalturaCatalogItemAdvancedFilter(KalturaSearchItem):
    def __init__(self,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            targetLanguageEqual = NotImplemented):
        KalturaSearchItem.__init__(self)

        # @var KalturaVendorServiceType
        self.serviceTypeEqual = serviceTypeEqual

        # @var str
        self.serviceTypeIn = serviceTypeIn

        # @var KalturaVendorServiceFeature
        self.serviceFeatureEqual = serviceFeatureEqual

        # @var str
        self.serviceFeatureIn = serviceFeatureIn

        # @var KalturaVendorServiceTurnAroundTime
        self.turnAroundTimeEqual = turnAroundTimeEqual

        # @var str
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
            type = NotImplemented,
            description = NotImplemented,
            not_ = NotImplemented,
            categoryId = NotImplemented,
            categoryIds = NotImplemented,
            categoryUserPermission = NotImplemented,
            comparison = NotImplemented):
        KalturaCondition.__init__(self,
            type,
            description,
            not_)

        # Category id to check condition for
        # @var int
        self.categoryId = categoryId

        # Category id's to check condition for
        # @var str
        self.categoryIds = categoryIds

        # Minimum category user level permission to validate
        # @var KalturaCategoryUserPermissionLevel
        self.categoryUserPermission = categoryUserPermission

        # Comparing operator
        # @var KalturaSearchConditionComparison
        self.comparison = comparison


    PROPERTY_LOADERS = {
        'categoryId': getXmlNodeInt, 
        'categoryIds': getXmlNodeText, 
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
        kparams.addStringIfDefined("categoryIds", self.categoryIds)
        kparams.addIntEnumIfDefined("categoryUserPermission", self.categoryUserPermission)
        kparams.addStringEnumIfDefined("comparison", self.comparison)
        return kparams

    def getCategoryId(self):
        return self.categoryId

    def setCategoryId(self, newCategoryId):
        self.categoryId = newCategoryId

    def getCategoryIds(self):
        return self.categoryIds

    def setCategoryIds(self, newCategoryIds):
        self.categoryIds = newCategoryIds

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
class KalturaClipsVendorTaskData(KalturaVendorTaskData):
    def __init__(self,
            entryDuration = NotImplemented,
            clipsDuration = NotImplemented,
            eventSessionContextId = NotImplemented,
            instruction = NotImplemented,
            clipsOutputJson = NotImplemented):
        KalturaVendorTaskData.__init__(self,
            entryDuration)

        # Estimated duration of the clips, in seconds.
        # @var int
        # @insertonly
        self.clipsDuration = clipsDuration

        # Event session context ID used to enhance clip results.
        # @var str
        # @insertonly
        self.eventSessionContextId = eventSessionContextId

        # Instruction describing the moments to capture or the objectives to achieve with the clips.
        # @var str
        # @insertonly
        self.instruction = instruction

        # List of clips as JSON string.
        # 	 For example: [{"title": "Title of the first clip", "description": "Description of the first clip", "tags": "Tagged-Example", "start": 127, "duration": 30}]
        # @var str
        self.clipsOutputJson = clipsOutputJson


    PROPERTY_LOADERS = {
        'clipsDuration': getXmlNodeInt, 
        'eventSessionContextId': getXmlNodeText, 
        'instruction': getXmlNodeText, 
        'clipsOutputJson': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaClipsVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaClipsVendorTaskData")
        kparams.addIntIfDefined("clipsDuration", self.clipsDuration)
        kparams.addStringIfDefined("eventSessionContextId", self.eventSessionContextId)
        kparams.addStringIfDefined("instruction", self.instruction)
        kparams.addStringIfDefined("clipsOutputJson", self.clipsOutputJson)
        return kparams

    def getClipsDuration(self):
        return self.clipsDuration

    def setClipsDuration(self, newClipsDuration):
        self.clipsDuration = newClipsDuration

    def getEventSessionContextId(self):
        return self.eventSessionContextId

    def setEventSessionContextId(self, newEventSessionContextId):
        self.eventSessionContextId = newEventSessionContextId

    def getInstruction(self):
        return self.instruction

    def setInstruction(self, newInstruction):
        self.instruction = newInstruction

    def getClipsOutputJson(self):
        return self.clipsOutputJson

    def setClipsOutputJson(self, newClipsOutputJson):
        self.clipsOutputJson = newClipsOutputJson


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskListResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaEntryVendorTask]
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
class KalturaIntelligentTaggingVendorTaskData(KalturaVendorTaskData):
    def __init__(self,
            entryDuration = NotImplemented,
            assetId = NotImplemented):
        KalturaVendorTaskData.__init__(self,
            entryDuration)

        # Optional - The id of the caption asset object
        # @var str
        # @insertonly
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaIntelligentTaggingVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaIntelligentTaggingVendorTaskData")
        kparams.addStringIfDefined("assetId", self.assetId)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId


# @package Kaltura
# @subpackage Client
class KalturaMetadataEnrichmentVendorTaskData(KalturaVendorTaskData):
    def __init__(self,
            entryDuration = NotImplemented,
            detailLevel = NotImplemented,
            instruction = NotImplemented,
            outputJson = NotImplemented):
        KalturaVendorTaskData.__init__(self,
            entryDuration)

        # The level of detail for the metadata enrichment process.
        # @var str
        # @insertonly
        self.detailLevel = detailLevel

        # Instructions describing what should be taken into account during the metadata enrichment process.
        # @var str
        # @insertonly
        self.instruction = instruction

        # Metadata enrichment result as JSON string.
        # 	 For example: {"titles": ["The first title", "The second title"], "descriptions": ["The first description"], "tags": ["Tag1", "Tag2"]}
        # @var str
        self.outputJson = outputJson


    PROPERTY_LOADERS = {
        'detailLevel': getXmlNodeText, 
        'instruction': getXmlNodeText, 
        'outputJson': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetadataEnrichmentVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaMetadataEnrichmentVendorTaskData")
        kparams.addStringIfDefined("detailLevel", self.detailLevel)
        kparams.addStringIfDefined("instruction", self.instruction)
        kparams.addStringIfDefined("outputJson", self.outputJson)
        return kparams

    def getDetailLevel(self):
        return self.detailLevel

    def setDetailLevel(self, newDetailLevel):
        self.detailLevel = newDetailLevel

    def getInstruction(self):
        return self.instruction

    def setInstruction(self, newInstruction):
        self.instruction = newInstruction

    def getOutputJson(self):
        return self.outputJson

    def setOutputJson(self, newOutputJson):
        self.outputJson = newOutputJson


# @package Kaltura
# @subpackage Client
class KalturaModerationVendorTaskData(KalturaVendorTaskData):
    def __init__(self,
            entryDuration = NotImplemented,
            ruleIds = NotImplemented,
            policyIds = NotImplemented,
            moderationOutputJson = NotImplemented):
        KalturaVendorTaskData.__init__(self,
            entryDuration)

        # A comma seperated string of rule IDs.
        # @var str
        self.ruleIds = ruleIds

        # A comma seperated string of policy IDs.
        # @var str
        self.policyIds = policyIds

        # JSON string containing the moderation output.
        # @var str
        self.moderationOutputJson = moderationOutputJson


    PROPERTY_LOADERS = {
        'ruleIds': getXmlNodeText, 
        'policyIds': getXmlNodeText, 
        'moderationOutputJson': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaModerationVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaModerationVendorTaskData")
        kparams.addStringIfDefined("ruleIds", self.ruleIds)
        kparams.addStringIfDefined("policyIds", self.policyIds)
        kparams.addStringIfDefined("moderationOutputJson", self.moderationOutputJson)
        return kparams

    def getRuleIds(self):
        return self.ruleIds

    def setRuleIds(self, newRuleIds):
        self.ruleIds = newRuleIds

    def getPolicyIds(self):
        return self.policyIds

    def setPolicyIds(self, newPolicyIds):
        self.policyIds = newPolicyIds

    def getModerationOutputJson(self):
        return self.moderationOutputJson

    def setModerationOutputJson(self, newModerationOutputJson):
        self.moderationOutputJson = newModerationOutputJson


# @package Kaltura
# @subpackage Client
class KalturaQuizVendorTaskData(KalturaVendorTaskData):
    def __init__(self,
            entryDuration = NotImplemented,
            numberOfQuestions = NotImplemented,
            questionsType = NotImplemented,
            context = NotImplemented,
            formalStyle = NotImplemented,
            createQuiz = NotImplemented,
            quizOutput = NotImplemented):
        KalturaVendorTaskData.__init__(self,
            entryDuration)

        # Number Of Questions.
        # @var int
        self.numberOfQuestions = numberOfQuestions

        # Questions Type.
        # @var str
        self.questionsType = questionsType

        # Quiz Context.
        # @var str
        self.context = context

        # Formal Style.
        # @var str
        self.formalStyle = formalStyle

        # Create quiz flag.
        # @var bool
        self.createQuiz = createQuiz

        # Quiz entry Id
        # @var str
        self.quizOutput = quizOutput


    PROPERTY_LOADERS = {
        'numberOfQuestions': getXmlNodeInt, 
        'questionsType': getXmlNodeText, 
        'context': getXmlNodeText, 
        'formalStyle': getXmlNodeText, 
        'createQuiz': getXmlNodeBool, 
        'quizOutput': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaQuizVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaQuizVendorTaskData")
        kparams.addIntIfDefined("numberOfQuestions", self.numberOfQuestions)
        kparams.addStringIfDefined("questionsType", self.questionsType)
        kparams.addStringIfDefined("context", self.context)
        kparams.addStringIfDefined("formalStyle", self.formalStyle)
        kparams.addBoolIfDefined("createQuiz", self.createQuiz)
        kparams.addStringIfDefined("quizOutput", self.quizOutput)
        return kparams

    def getNumberOfQuestions(self):
        return self.numberOfQuestions

    def setNumberOfQuestions(self, newNumberOfQuestions):
        self.numberOfQuestions = newNumberOfQuestions

    def getQuestionsType(self):
        return self.questionsType

    def setQuestionsType(self, newQuestionsType):
        self.questionsType = newQuestionsType

    def getContext(self):
        return self.context

    def setContext(self, newContext):
        self.context = newContext

    def getFormalStyle(self):
        return self.formalStyle

    def setFormalStyle(self, newFormalStyle):
        self.formalStyle = newFormalStyle

    def getCreateQuiz(self):
        return self.createQuiz

    def setCreateQuiz(self, newCreateQuiz):
        self.createQuiz = newCreateQuiz

    def getQuizOutput(self):
        return self.quizOutput

    def setQuizOutput(self, newQuizOutput):
        self.quizOutput = newQuizOutput


# @package Kaltura
# @subpackage Client
class KalturaReachProfileListResponse(KalturaListResponse):
    def __init__(self,
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaReachProfile]
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
class KalturaScheduledVendorTaskData(KalturaVendorTaskData):
    def __init__(self,
            entryDuration = NotImplemented,
            startDate = NotImplemented,
            endDate = NotImplemented,
            scheduledEventId = NotImplemented):
        KalturaVendorTaskData.__init__(self,
            entryDuration)

        # @var int
        # @insertonly
        self.startDate = startDate

        # @var int
        # @insertonly
        self.endDate = endDate

        # @var int
        # @insertonly
        self.scheduledEventId = scheduledEventId


    PROPERTY_LOADERS = {
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'scheduledEventId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaScheduledVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaScheduledVendorTaskData")
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addIntIfDefined("scheduledEventId", self.scheduledEventId)
        return kparams

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getScheduledEventId(self):
        return self.scheduledEventId

    def setScheduledEventId(self, newScheduledEventId):
        self.scheduledEventId = newScheduledEventId


# @package Kaltura
# @subpackage Client
class KalturaSummaryVendorTaskData(KalturaVendorTaskData):
    def __init__(self,
            entryDuration = NotImplemented,
            typeOfSummary = NotImplemented,
            writingStyle = NotImplemented,
            language = NotImplemented,
            summaryOutputJson = NotImplemented):
        KalturaVendorTaskData.__init__(self,
            entryDuration)

        # Type of summary.
        # @var KalturaTypeOfSummaryTaskData
        self.typeOfSummary = typeOfSummary

        # Writing style of the summary.
        # @var KalturaSummaryWritingStyleTaskData
        self.writingStyle = writingStyle

        # Language code
        # @var KalturaLanguageCode
        self.language = language

        # JSON string containing the summary output.
        # @var str
        self.summaryOutputJson = summaryOutputJson


    PROPERTY_LOADERS = {
        'typeOfSummary': (KalturaEnumsFactory.createString, "KalturaTypeOfSummaryTaskData"), 
        'writingStyle': (KalturaEnumsFactory.createString, "KalturaSummaryWritingStyleTaskData"), 
        'language': (KalturaEnumsFactory.createString, "KalturaLanguageCode"), 
        'summaryOutputJson': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSummaryVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaSummaryVendorTaskData")
        kparams.addStringEnumIfDefined("typeOfSummary", self.typeOfSummary)
        kparams.addStringEnumIfDefined("writingStyle", self.writingStyle)
        kparams.addStringEnumIfDefined("language", self.language)
        kparams.addStringIfDefined("summaryOutputJson", self.summaryOutputJson)
        return kparams

    def getTypeOfSummary(self):
        return self.typeOfSummary

    def setTypeOfSummary(self, newTypeOfSummary):
        self.typeOfSummary = newTypeOfSummary

    def getWritingStyle(self):
        return self.writingStyle

    def setWritingStyle(self, newWritingStyle):
        self.writingStyle = newWritingStyle

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getSummaryOutputJson(self):
        return self.summaryOutputJson

    def setSummaryOutputJson(self, newSummaryOutputJson):
        self.summaryOutputJson = newSummaryOutputJson


# @package Kaltura
# @subpackage Client
class KalturaUnlimitedVendorCredit(KalturaBaseVendorCredit):
    def __init__(self,
            credit = NotImplemented,
            fromDate = NotImplemented):
        KalturaBaseVendorCredit.__init__(self)

        # @var int
        # @readonly
        self.credit = credit

        # @var int
        self.fromDate = fromDate


    PROPERTY_LOADERS = {
        'credit': getXmlNodeInt, 
        'fromDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBaseVendorCredit.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUnlimitedVendorCredit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseVendorCredit.toParams(self)
        kparams.put("objectType", "KalturaUnlimitedVendorCredit")
        kparams.addIntIfDefined("fromDate", self.fromDate)
        return kparams

    def getCredit(self):
        return self.credit

    def getFromDate(self):
        return self.fromDate

    def setFromDate(self, newFromDate):
        self.fromDate = newFromDate


# @package Kaltura
# @subpackage Client
class KalturaVendorAlignmentCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            outputFormat = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)

        # @var KalturaVendorCatalogItemOutputFormat
        self.outputFormat = outputFormat


    PROPERTY_LOADERS = {
        'outputFormat': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemOutputFormat"), 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorAlignmentCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorAlignmentCatalogItem")
        kparams.addIntEnumIfDefined("outputFormat", self.outputFormat)
        return kparams

    def getOutputFormat(self):
        return self.outputFormat

    def setOutputFormat(self, newOutputFormat):
        self.outputFormat = newOutputFormat


# @package Kaltura
# @subpackage Client
class KalturaVendorAudioDescriptionCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            flavorParamsId = NotImplemented,
            clearAudioFlavorParamsId = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)

        # @var int
        self.flavorParamsId = flavorParamsId

        # @var int
        self.clearAudioFlavorParamsId = clearAudioFlavorParamsId


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'clearAudioFlavorParamsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorAudioDescriptionCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorAudioDescriptionCatalogItem")
        kparams.addIntIfDefined("flavorParamsId", self.flavorParamsId)
        kparams.addIntIfDefined("clearAudioFlavorParamsId", self.clearAudioFlavorParamsId)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getClearAudioFlavorParamsId(self):
        return self.clearAudioFlavorParamsId

    def setClearAudioFlavorParamsId(self, newClearAudioFlavorParamsId):
        self.clearAudioFlavorParamsId = newClearAudioFlavorParamsId


# @package Kaltura
# @subpackage Client
class KalturaVendorCaptionsCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            outputFormat = NotImplemented,
            enableSpeakerId = NotImplemented,
            fixedPriceAddons = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)

        # @var KalturaVendorCatalogItemOutputFormat
        self.outputFormat = outputFormat

        # @var KalturaNullableBoolean
        self.enableSpeakerId = enableSpeakerId

        # @var int
        self.fixedPriceAddons = fixedPriceAddons


    PROPERTY_LOADERS = {
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
        kparams.addIntEnumIfDefined("outputFormat", self.outputFormat)
        kparams.addIntEnumIfDefined("enableSpeakerId", self.enableSpeakerId)
        kparams.addIntIfDefined("fixedPriceAddons", self.fixedPriceAddons)
        return kparams

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
            totalCount = NotImplemented,
            objects = NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var List[KalturaVendorCatalogItem]
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
class KalturaVendorChapteringCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorChapteringCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorChapteringCatalogItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorClipsCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorClipsCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorClipsCatalogItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorCredit(KalturaBaseVendorCredit):
    def __init__(self,
            credit = NotImplemented,
            fromDate = NotImplemented,
            overageCredit = NotImplemented,
            addOn = NotImplemented,
            allowNegativeOverageCredit = NotImplemented):
        KalturaBaseVendorCredit.__init__(self)

        # @var int
        self.credit = credit

        # @var int
        self.fromDate = fromDate

        # @var int
        self.overageCredit = overageCredit

        # @var int
        self.addOn = addOn

        # @var bool
        self.allowNegativeOverageCredit = allowNegativeOverageCredit


    PROPERTY_LOADERS = {
        'credit': getXmlNodeInt, 
        'fromDate': getXmlNodeInt, 
        'overageCredit': getXmlNodeInt, 
        'addOn': getXmlNodeInt, 
        'allowNegativeOverageCredit': getXmlNodeBool, 
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
        kparams.addBoolIfDefined("allowNegativeOverageCredit", self.allowNegativeOverageCredit)
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

    def getAllowNegativeOverageCredit(self):
        return self.allowNegativeOverageCredit

    def setAllowNegativeOverageCredit(self, newAllowNegativeOverageCredit):
        self.allowNegativeOverageCredit = newAllowNegativeOverageCredit


# @package Kaltura
# @subpackage Client
class KalturaVendorDubbingCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            flavorParamsId = NotImplemented,
            clearAudioFlavorParamsId = NotImplemented,
            targetLanguage = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)

        # @var int
        self.flavorParamsId = flavorParamsId

        # @var int
        self.clearAudioFlavorParamsId = clearAudioFlavorParamsId

        # @var KalturaCatalogItemLanguage
        self.targetLanguage = targetLanguage


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'clearAudioFlavorParamsId': getXmlNodeInt, 
        'targetLanguage': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorDubbingCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorDubbingCatalogItem")
        kparams.addIntIfDefined("flavorParamsId", self.flavorParamsId)
        kparams.addIntIfDefined("clearAudioFlavorParamsId", self.clearAudioFlavorParamsId)
        kparams.addStringEnumIfDefined("targetLanguage", self.targetLanguage)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getClearAudioFlavorParamsId(self):
        return self.clearAudioFlavorParamsId

    def setClearAudioFlavorParamsId(self, newClearAudioFlavorParamsId):
        self.clearAudioFlavorParamsId = newClearAudioFlavorParamsId

    def getTargetLanguage(self):
        return self.targetLanguage

    def setTargetLanguage(self, newTargetLanguage):
        self.targetLanguage = newTargetLanguage


# @package Kaltura
# @subpackage Client
class KalturaVendorExtendedAudioDescriptionCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            flavorParamsId = NotImplemented,
            clearAudioFlavorParamsId = NotImplemented,
            outputFormat = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)

        # @var int
        self.flavorParamsId = flavorParamsId

        # @var int
        self.clearAudioFlavorParamsId = clearAudioFlavorParamsId

        # @var KalturaVendorCatalogItemOutputFormat
        self.outputFormat = outputFormat


    PROPERTY_LOADERS = {
        'flavorParamsId': getXmlNodeInt, 
        'clearAudioFlavorParamsId': getXmlNodeInt, 
        'outputFormat': (KalturaEnumsFactory.createInt, "KalturaVendorCatalogItemOutputFormat"), 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorExtendedAudioDescriptionCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorExtendedAudioDescriptionCatalogItem")
        kparams.addIntIfDefined("flavorParamsId", self.flavorParamsId)
        kparams.addIntIfDefined("clearAudioFlavorParamsId", self.clearAudioFlavorParamsId)
        kparams.addIntEnumIfDefined("outputFormat", self.outputFormat)
        return kparams

    def getFlavorParamsId(self):
        return self.flavorParamsId

    def setFlavorParamsId(self, newFlavorParamsId):
        self.flavorParamsId = newFlavorParamsId

    def getClearAudioFlavorParamsId(self):
        return self.clearAudioFlavorParamsId

    def setClearAudioFlavorParamsId(self, newClearAudioFlavorParamsId):
        self.clearAudioFlavorParamsId = newClearAudioFlavorParamsId

    def getOutputFormat(self):
        return self.outputFormat

    def setOutputFormat(self, newOutputFormat):
        self.outputFormat = newOutputFormat


# @package Kaltura
# @subpackage Client
class KalturaVendorIntelligentTaggingCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorIntelligentTaggingCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorIntelligentTaggingCatalogItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorMetadataEnrichmentCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorMetadataEnrichmentCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorMetadataEnrichmentCatalogItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorModerationCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorModerationCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorModerationCatalogItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorQuizCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorQuizCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorQuizCatalogItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorSummaryCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorSummaryCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorSummaryCatalogItem")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorTaskDataCaptionAsset(KalturaVendorTaskData):
    def __init__(self,
            entryDuration = NotImplemented,
            captionAssetId = NotImplemented):
        KalturaVendorTaskData.__init__(self,
            entryDuration)

        # Optional - The id of the caption asset object
        # @var str
        # @insertonly
        self.captionAssetId = captionAssetId


    PROPERTY_LOADERS = {
        'captionAssetId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorTaskDataCaptionAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskData.toParams(self)
        kparams.put("objectType", "KalturaVendorTaskDataCaptionAsset")
        kparams.addStringIfDefined("captionAssetId", self.captionAssetId)
        return kparams

    def getCaptionAssetId(self):
        return self.captionAssetId

    def setCaptionAssetId(self, newCaptionAssetId):
        self.captionAssetId = newCaptionAssetId


# @package Kaltura
# @subpackage Client
class KalturaVendorVideoAnalysisCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            videoAnalysisType = NotImplemented,
            maxVideoDuration = NotImplemented):
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
            pricing,
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude)

        # @var KalturaVendorVideoAnalysisType
        self.videoAnalysisType = videoAnalysisType

        # @var int
        self.maxVideoDuration = maxVideoDuration


    PROPERTY_LOADERS = {
        'videoAnalysisType': (KalturaEnumsFactory.createInt, "KalturaVendorVideoAnalysisType"), 
        'maxVideoDuration': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorVideoAnalysisCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorVideoAnalysisCatalogItem")
        kparams.addIntEnumIfDefined("videoAnalysisType", self.videoAnalysisType)
        kparams.addIntIfDefined("maxVideoDuration", self.maxVideoDuration)
        return kparams

    def getVideoAnalysisType(self):
        return self.videoAnalysisType

    def setVideoAnalysisType(self, newVideoAnalysisType):
        self.videoAnalysisType = newVideoAnalysisType

    def getMaxVideoDuration(self):
        return self.maxVideoDuration

    def setMaxVideoDuration(self, newMaxVideoDuration):
        self.maxVideoDuration = newMaxVideoDuration


# @package Kaltura
# @subpackage Client
class KalturaAlignmentVendorTaskData(KalturaVendorTaskDataCaptionAsset):
    def __init__(self,
            entryDuration = NotImplemented,
            captionAssetId = NotImplemented,
            textTranscriptAssetId = NotImplemented,
            jsonTranscriptAssetId = NotImplemented):
        KalturaVendorTaskDataCaptionAsset.__init__(self,
            entryDuration,
            captionAssetId)

        # The id of the text transcript object the vendor should use while runing the alignment task
        # @var str
        self.textTranscriptAssetId = textTranscriptAssetId

        # Optional - The id of the json transcript object the vendor should update once alignment task processing is done
        # @var str
        # @insertonly
        self.jsonTranscriptAssetId = jsonTranscriptAssetId


    PROPERTY_LOADERS = {
        'textTranscriptAssetId': getXmlNodeText, 
        'jsonTranscriptAssetId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorTaskDataCaptionAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAlignmentVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskDataCaptionAsset.toParams(self)
        kparams.put("objectType", "KalturaAlignmentVendorTaskData")
        kparams.addStringIfDefined("textTranscriptAssetId", self.textTranscriptAssetId)
        kparams.addStringIfDefined("jsonTranscriptAssetId", self.jsonTranscriptAssetId)
        return kparams

    def getTextTranscriptAssetId(self):
        return self.textTranscriptAssetId

    def setTextTranscriptAssetId(self, newTextTranscriptAssetId):
        self.textTranscriptAssetId = newTextTranscriptAssetId

    def getJsonTranscriptAssetId(self):
        return self.jsonTranscriptAssetId

    def setJsonTranscriptAssetId(self, newJsonTranscriptAssetId):
        self.jsonTranscriptAssetId = newJsonTranscriptAssetId


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            queueTimeGreaterThanOrEqual = NotImplemented,
            queueTimeLessThanOrEqual = NotImplemented,
            finishTimeGreaterThanOrEqual = NotImplemented,
            finishTimeLessThanOrEqual = NotImplemented,
            entryIdEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            reachProfileIdEqual = NotImplemented,
            reachProfileIdIn = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            catalogItemIdIn = NotImplemented,
            userIdEqual = NotImplemented,
            contextEqual = NotImplemented,
            expectedFinishTimeGreaterThanOrEqual = NotImplemented,
            expectedFinishTimeLessThanOrEqual = NotImplemented,
            entryObjectTypeEqual = NotImplemented,
            entryObjectTypeIn = NotImplemented,
            entryObjectTypeNotIn = NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var str
        self.idIn = idIn

        # @var str
        self.idNotIn = idNotIn

        # @var int
        self.vendorPartnerIdEqual = vendorPartnerIdEqual

        # @var str
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

        # @var str
        self.entryIdEqual = entryIdEqual

        # @var KalturaEntryVendorTaskStatus
        self.statusEqual = statusEqual

        # @var str
        self.statusIn = statusIn

        # @var int
        self.reachProfileIdEqual = reachProfileIdEqual

        # @var str
        self.reachProfileIdIn = reachProfileIdIn

        # @var int
        self.catalogItemIdEqual = catalogItemIdEqual

        # @var str
        self.catalogItemIdIn = catalogItemIdIn

        # @var str
        self.userIdEqual = userIdEqual

        # @var str
        self.contextEqual = contextEqual

        # @var int
        self.expectedFinishTimeGreaterThanOrEqual = expectedFinishTimeGreaterThanOrEqual

        # @var int
        self.expectedFinishTimeLessThanOrEqual = expectedFinishTimeLessThanOrEqual

        # @var KalturaEntryObjectType
        self.entryObjectTypeEqual = entryObjectTypeEqual

        # @var str
        self.entryObjectTypeIn = entryObjectTypeIn

        # @var str
        self.entryObjectTypeNotIn = entryObjectTypeNotIn


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
        'expectedFinishTimeGreaterThanOrEqual': getXmlNodeInt, 
        'expectedFinishTimeLessThanOrEqual': getXmlNodeInt, 
        'entryObjectTypeEqual': (KalturaEnumsFactory.createInt, "KalturaEntryObjectType"), 
        'entryObjectTypeIn': getXmlNodeText, 
        'entryObjectTypeNotIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRelatedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntryVendorTaskBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedFilter.toParams(self)
        kparams.put("objectType", "KalturaEntryVendorTaskBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("idNotIn", self.idNotIn)
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
        kparams.addIntIfDefined("expectedFinishTimeGreaterThanOrEqual", self.expectedFinishTimeGreaterThanOrEqual)
        kparams.addIntIfDefined("expectedFinishTimeLessThanOrEqual", self.expectedFinishTimeLessThanOrEqual)
        kparams.addIntEnumIfDefined("entryObjectTypeEqual", self.entryObjectTypeEqual)
        kparams.addStringIfDefined("entryObjectTypeIn", self.entryObjectTypeIn)
        kparams.addStringIfDefined("entryObjectTypeNotIn", self.entryObjectTypeNotIn)
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

    def getExpectedFinishTimeGreaterThanOrEqual(self):
        return self.expectedFinishTimeGreaterThanOrEqual

    def setExpectedFinishTimeGreaterThanOrEqual(self, newExpectedFinishTimeGreaterThanOrEqual):
        self.expectedFinishTimeGreaterThanOrEqual = newExpectedFinishTimeGreaterThanOrEqual

    def getExpectedFinishTimeLessThanOrEqual(self):
        return self.expectedFinishTimeLessThanOrEqual

    def setExpectedFinishTimeLessThanOrEqual(self, newExpectedFinishTimeLessThanOrEqual):
        self.expectedFinishTimeLessThanOrEqual = newExpectedFinishTimeLessThanOrEqual

    def getEntryObjectTypeEqual(self):
        return self.entryObjectTypeEqual

    def setEntryObjectTypeEqual(self, newEntryObjectTypeEqual):
        self.entryObjectTypeEqual = newEntryObjectTypeEqual

    def getEntryObjectTypeIn(self):
        return self.entryObjectTypeIn

    def setEntryObjectTypeIn(self, newEntryObjectTypeIn):
        self.entryObjectTypeIn = newEntryObjectTypeIn

    def getEntryObjectTypeNotIn(self):
        return self.entryObjectTypeNotIn

    def setEntryObjectTypeNotIn(self, newEntryObjectTypeNotIn):
        self.entryObjectTypeNotIn = newEntryObjectTypeNotIn


# @package Kaltura
# @subpackage Client
class KalturaEntryVendorTaskFilter(KalturaEntryVendorTaskBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            queueTimeGreaterThanOrEqual = NotImplemented,
            queueTimeLessThanOrEqual = NotImplemented,
            finishTimeGreaterThanOrEqual = NotImplemented,
            finishTimeLessThanOrEqual = NotImplemented,
            entryIdEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            reachProfileIdEqual = NotImplemented,
            reachProfileIdIn = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            catalogItemIdIn = NotImplemented,
            userIdEqual = NotImplemented,
            contextEqual = NotImplemented,
            expectedFinishTimeGreaterThanOrEqual = NotImplemented,
            expectedFinishTimeLessThanOrEqual = NotImplemented,
            entryObjectTypeEqual = NotImplemented,
            entryObjectTypeIn = NotImplemented,
            entryObjectTypeNotIn = NotImplemented,
            freeText = NotImplemented):
        KalturaEntryVendorTaskBaseFilter.__init__(self,
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
            contextEqual,
            expectedFinishTimeGreaterThanOrEqual,
            expectedFinishTimeLessThanOrEqual,
            entryObjectTypeEqual,
            entryObjectTypeIn,
            entryObjectTypeNotIn)

        # @var str
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
            userName = NotImplemented,
            userMail = NotImplemented,
            outputPath = NotImplemented,
            sharedOutputPath = NotImplemented,
            filter = NotImplemented):
        KalturaExportCsvJobData.__init__(self,
            userName,
            userMail,
            outputPath,
            sharedOutputPath)

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
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            profileTypeEqual = NotImplemented,
            profileTypeIn = NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var str
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

        # @var str
        self.statusIn = statusIn

        # @var KalturaReachProfileType
        self.profileTypeEqual = profileTypeEqual

        # @var str
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
            fromDate = NotImplemented,
            toDate = NotImplemented,
            fromDay = NotImplemented,
            toDay = NotImplemented,
            keywords = NotImplemented,
            searchInTags = NotImplemented,
            searchInAdminTags = NotImplemented,
            categories = NotImplemented,
            categoriesIdsIn = NotImplemented,
            customVar1In = NotImplemented,
            customVar2In = NotImplemented,
            customVar3In = NotImplemented,
            deviceIn = NotImplemented,
            countryIn = NotImplemented,
            regionIn = NotImplemented,
            citiesIn = NotImplemented,
            operatingSystemFamilyIn = NotImplemented,
            operatingSystemIn = NotImplemented,
            browserFamilyIn = NotImplemented,
            browserIn = NotImplemented,
            timeZoneOffset = NotImplemented,
            interval = NotImplemented,
            mediaTypeIn = NotImplemented,
            sourceTypeIn = NotImplemented,
            ownerIdsIn = NotImplemented,
            entryOperator = NotImplemented,
            entryCreatedAtGreaterThanOrEqual = NotImplemented,
            entryCreatedAtLessThanOrEqual = NotImplemented,
            entryIdIn = NotImplemented,
            playbackTypeIn = NotImplemented,
            playbackContextIdsIn = NotImplemented,
            rootEntryIdIn = NotImplemented,
            errorCodeIn = NotImplemented,
            playerVersionIn = NotImplemented,
            ispIn = NotImplemented,
            applicationVersionIn = NotImplemented,
            nodeIdsIn = NotImplemented,
            categoriesAncestorIdIn = NotImplemented,
            hotspotIdIn = NotImplemented,
            crmIdIn = NotImplemented,
            playlistIdIn = NotImplemented,
            domainIn = NotImplemented,
            canonicalUrlIn = NotImplemented,
            virtualEventIdIn = NotImplemented,
            originIn = NotImplemented,
            uiConfIdIn = NotImplemented,
            cuePointIdIn = NotImplemented,
            contextIdIn = NotImplemented,
            roleIn = NotImplemented,
            industryIn = NotImplemented,
            playbackModeIn = NotImplemented,
            companyIn = NotImplemented,
            eventSessionContextIdIn = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented):
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
            operatingSystemIn,
            browserFamilyIn,
            browserIn,
            timeZoneOffset,
            interval,
            mediaTypeIn,
            sourceTypeIn,
            ownerIdsIn,
            entryOperator,
            entryCreatedAtGreaterThanOrEqual,
            entryCreatedAtLessThanOrEqual,
            entryIdIn,
            playbackTypeIn,
            playbackContextIdsIn,
            rootEntryIdIn,
            errorCodeIn,
            playerVersionIn,
            ispIn,
            applicationVersionIn,
            nodeIdsIn,
            categoriesAncestorIdIn,
            hotspotIdIn,
            crmIdIn,
            playlistIdIn,
            domainIn,
            canonicalUrlIn,
            virtualEventIdIn,
            originIn,
            uiConfIdIn,
            cuePointIdIn,
            contextIdIn,
            roleIn,
            industryIn,
            playbackModeIn,
            companyIn,
            eventSessionContextIdIn)

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
            credit = NotImplemented,
            fromDate = NotImplemented,
            overageCredit = NotImplemented,
            addOn = NotImplemented,
            allowNegativeOverageCredit = NotImplemented,
            toDate = NotImplemented):
        KalturaVendorCredit.__init__(self,
            credit,
            fromDate,
            overageCredit,
            addOn,
            allowNegativeOverageCredit)

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
class KalturaTranslationVendorTaskData(KalturaVendorTaskDataCaptionAsset):
    def __init__(self,
            entryDuration = NotImplemented,
            captionAssetId = NotImplemented):
        KalturaVendorTaskDataCaptionAsset.__init__(self,
            entryDuration,
            captionAssetId)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorTaskDataCaptionAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTranslationVendorTaskData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTaskDataCaptionAsset.toParams(self)
        kparams.put("objectType", "KalturaTranslationVendorTaskData")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorCatalogItemBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var str
        self.idIn = idIn

        # @var str
        self.idNotIn = idNotIn

        # @var int
        self.vendorPartnerIdEqual = vendorPartnerIdEqual

        # @var str
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

        # @var str
        self.statusIn = statusIn

        # @var KalturaVendorServiceType
        self.serviceTypeEqual = serviceTypeEqual

        # @var str
        self.serviceTypeIn = serviceTypeIn

        # @var KalturaVendorServiceFeature
        self.serviceFeatureEqual = serviceFeatureEqual

        # @var str
        self.serviceFeatureIn = serviceFeatureIn

        # @var KalturaVendorServiceTurnAroundTime
        self.turnAroundTimeEqual = turnAroundTimeEqual

        # @var str
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
class KalturaVendorLiveCatalogItem(KalturaVendorCaptionsCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            outputFormat = NotImplemented,
            enableSpeakerId = NotImplemented,
            fixedPriceAddons = NotImplemented,
            minimalRefundTime = NotImplemented,
            minimalOrderTime = NotImplemented,
            durationLimit = NotImplemented):
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
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude,
            outputFormat,
            enableSpeakerId,
            fixedPriceAddons)

        # @var int
        self.minimalRefundTime = minimalRefundTime

        # @var int
        self.minimalOrderTime = minimalOrderTime

        # @var int
        self.durationLimit = durationLimit


    PROPERTY_LOADERS = {
        'minimalRefundTime': getXmlNodeInt, 
        'minimalOrderTime': getXmlNodeInt, 
        'durationLimit': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorLiveCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorLiveCatalogItem")
        kparams.addIntIfDefined("minimalRefundTime", self.minimalRefundTime)
        kparams.addIntIfDefined("minimalOrderTime", self.minimalOrderTime)
        kparams.addIntIfDefined("durationLimit", self.durationLimit)
        return kparams

    def getMinimalRefundTime(self):
        return self.minimalRefundTime

    def setMinimalRefundTime(self, newMinimalRefundTime):
        self.minimalRefundTime = newMinimalRefundTime

    def getMinimalOrderTime(self):
        return self.minimalOrderTime

    def setMinimalOrderTime(self, newMinimalOrderTime):
        self.minimalOrderTime = newMinimalOrderTime

    def getDurationLimit(self):
        return self.durationLimit

    def setDurationLimit(self, newDurationLimit):
        self.durationLimit = newDurationLimit


# @package Kaltura
# @subpackage Client
class KalturaVendorTranslationCatalogItem(KalturaVendorCaptionsCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            outputFormat = NotImplemented,
            enableSpeakerId = NotImplemented,
            fixedPriceAddons = NotImplemented,
            targetLanguage = NotImplemented,
            requireSource = NotImplemented):
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
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude,
            outputFormat,
            enableSpeakerId,
            fixedPriceAddons)

        # @var KalturaCatalogItemLanguage
        self.targetLanguage = targetLanguage

        # @var bool
        self.requireSource = requireSource


    PROPERTY_LOADERS = {
        'targetLanguage': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'requireSource': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorTranslationCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorTranslationCatalogItem")
        kparams.addStringEnumIfDefined("targetLanguage", self.targetLanguage)
        kparams.addBoolIfDefined("requireSource", self.requireSource)
        return kparams

    def getTargetLanguage(self):
        return self.targetLanguage

    def setTargetLanguage(self, newTargetLanguage):
        self.targetLanguage = newTargetLanguage

    def getRequireSource(self):
        return self.requireSource

    def setRequireSource(self, newRequireSource):
        self.requireSource = newRequireSource


# @package Kaltura
# @subpackage Client
class KalturaReachProfileFilter(KalturaReachProfileBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            profileTypeEqual = NotImplemented,
            profileTypeIn = NotImplemented):
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
            credit = NotImplemented,
            fromDate = NotImplemented,
            overageCredit = NotImplemented,
            addOn = NotImplemented,
            allowNegativeOverageCredit = NotImplemented,
            toDate = NotImplemented,
            frequency = NotImplemented):
        KalturaTimeRangeVendorCredit.__init__(self,
            credit,
            fromDate,
            overageCredit,
            addOn,
            allowNegativeOverageCredit,
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
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented):
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

        # @var int
        self.catalogItemIdEqual = catalogItemIdEqual


    PROPERTY_LOADERS = {
        'partnerIdEqual': getXmlNodeInt, 
        'catalogItemIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorCatalogItemFilter")
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addIntIfDefined("catalogItemIdEqual", self.catalogItemIdEqual)
        return kparams

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getCatalogItemIdEqual(self):
        return self.catalogItemIdEqual

    def setCatalogItemIdEqual(self, newCatalogItemIdEqual):
        self.catalogItemIdEqual = newCatalogItemIdEqual


# @package Kaltura
# @subpackage Client
class KalturaVendorLiveCaptionCatalogItem(KalturaVendorLiveCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            outputFormat = NotImplemented,
            enableSpeakerId = NotImplemented,
            fixedPriceAddons = NotImplemented,
            minimalRefundTime = NotImplemented,
            minimalOrderTime = NotImplemented,
            durationLimit = NotImplemented,
            startTimeBuffer = NotImplemented,
            endTimeBuffer = NotImplemented):
        KalturaVendorLiveCatalogItem.__init__(self,
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
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude,
            outputFormat,
            enableSpeakerId,
            fixedPriceAddons,
            minimalRefundTime,
            minimalOrderTime,
            durationLimit)

        # How long before the live stream start should service activate? (in secs)
        # @var int
        # @insertonly
        self.startTimeBuffer = startTimeBuffer

        # How long after the live stream end should service de-activate? (in secs)
        # @var int
        # @insertonly
        self.endTimeBuffer = endTimeBuffer


    PROPERTY_LOADERS = {
        'startTimeBuffer': getXmlNodeInt, 
        'endTimeBuffer': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaVendorLiveCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorLiveCaptionCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorLiveCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorLiveCaptionCatalogItem")
        kparams.addIntIfDefined("startTimeBuffer", self.startTimeBuffer)
        kparams.addIntIfDefined("endTimeBuffer", self.endTimeBuffer)
        return kparams

    def getStartTimeBuffer(self):
        return self.startTimeBuffer

    def setStartTimeBuffer(self, newStartTimeBuffer):
        self.startTimeBuffer = newStartTimeBuffer

    def getEndTimeBuffer(self):
        return self.endTimeBuffer

    def setEndTimeBuffer(self, newEndTimeBuffer):
        self.endTimeBuffer = newEndTimeBuffer


# @package Kaltura
# @subpackage Client
class KalturaVendorLiveTranslationCatalogItem(KalturaVendorLiveCatalogItem):
    def __init__(self,
            id = NotImplemented,
            vendorPartnerId = NotImplemented,
            name = NotImplemented,
            systemName = NotImplemented,
            createdAt = NotImplemented,
            updatedAt = NotImplemented,
            status = NotImplemented,
            serviceType = NotImplemented,
            serviceFeature = NotImplemented,
            turnAroundTime = NotImplemented,
            pricing = NotImplemented,
            engineType = NotImplemented,
            sourceLanguage = NotImplemented,
            allowResubmission = NotImplemented,
            requiresOverages = NotImplemented,
            vendorData = NotImplemented,
            stage = NotImplemented,
            lastBulkUpdateId = NotImplemented,
            contract = NotImplemented,
            createdBy = NotImplemented,
            notes = NotImplemented,
            partnerId = NotImplemented,
            defaultReachProfileId = NotImplemented,
            adminTagsToExclude = NotImplemented,
            outputFormat = NotImplemented,
            enableSpeakerId = NotImplemented,
            fixedPriceAddons = NotImplemented,
            minimalRefundTime = NotImplemented,
            minimalOrderTime = NotImplemented,
            durationLimit = NotImplemented,
            targetLanguage = NotImplemented):
        KalturaVendorLiveCatalogItem.__init__(self,
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
            engineType,
            sourceLanguage,
            allowResubmission,
            requiresOverages,
            vendorData,
            stage,
            lastBulkUpdateId,
            contract,
            createdBy,
            notes,
            partnerId,
            defaultReachProfileId,
            adminTagsToExclude,
            outputFormat,
            enableSpeakerId,
            fixedPriceAddons,
            minimalRefundTime,
            minimalOrderTime,
            durationLimit)

        # @var KalturaCatalogItemLanguage
        self.targetLanguage = targetLanguage


    PROPERTY_LOADERS = {
        'targetLanguage': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
    }

    def fromXml(self, node):
        KalturaVendorLiveCatalogItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorLiveTranslationCatalogItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorLiveCatalogItem.toParams(self)
        kparams.put("objectType", "KalturaVendorLiveTranslationCatalogItem")
        kparams.addStringEnumIfDefined("targetLanguage", self.targetLanguage)
        return kparams

    def getTargetLanguage(self):
        return self.targetLanguage

    def setTargetLanguage(self, newTargetLanguage):
        self.targetLanguage = newTargetLanguage


# @package Kaltura
# @subpackage Client
class KalturaVendorCaptionsCatalogItemBaseFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)

        # @var KalturaCatalogItemLanguage
        self.sourceLanguageEqual = sourceLanguageEqual

        # @var str
        self.sourceLanguageIn = sourceLanguageIn

        # @var KalturaVendorCatalogItemOutputFormat
        self.outputFormatEqual = outputFormatEqual

        # @var str
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
class KalturaVendorClipsCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorClipsCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorClipsCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorDubbingCatalogItemBaseFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            targetLanguageEqual = NotImplemented,
            targetLanguageIn = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)

        # @var KalturaCatalogItemLanguage
        self.targetLanguageEqual = targetLanguageEqual

        # @var str
        self.targetLanguageIn = targetLanguageIn


    PROPERTY_LOADERS = {
        'targetLanguageEqual': (KalturaEnumsFactory.createString, "KalturaCatalogItemLanguage"), 
        'targetLanguageIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorDubbingCatalogItemBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorDubbingCatalogItemBaseFilter")
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
class KalturaVendorIntelligentTaggingCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorIntelligentTaggingCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorIntelligentTaggingCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorMetadataEnrichmentCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorMetadataEnrichmentCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorMetadataEnrichmentCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorModerationCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorModerationCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorModerationCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorQuizCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorQuizCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorQuizCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorSummaryCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorSummaryCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorSummaryCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorVideoAnalysisCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented):
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
            partnerIdEqual,
            catalogItemIdEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCatalogItemFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorVideoAnalysisCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCatalogItemFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorVideoAnalysisCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorAlignmentCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented):
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
            catalogItemIdEqual,
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
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented):
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
            catalogItemIdEqual,
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
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented):
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
            catalogItemIdEqual,
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
class KalturaVendorChapteringCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented):
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
            catalogItemIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorChapteringCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorChapteringCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorDubbingCatalogItemFilter(KalturaVendorDubbingCatalogItemBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            targetLanguageEqual = NotImplemented,
            targetLanguageIn = NotImplemented):
        KalturaVendorDubbingCatalogItemBaseFilter.__init__(self,
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
            catalogItemIdEqual,
            targetLanguageEqual,
            targetLanguageIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorDubbingCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorDubbingCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorDubbingCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorDubbingCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorExtendedAudioDescriptionCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented):
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
            catalogItemIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorExtendedAudioDescriptionCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorExtendedAudioDescriptionCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorLiveCaptionCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented):
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
            catalogItemIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaVendorCaptionsCatalogItemBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaVendorLiveCaptionCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorCaptionsCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorLiveCaptionCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorTranslationCatalogItemBaseFilter(KalturaVendorCaptionsCatalogItemFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented,
            targetLanguageEqual = NotImplemented,
            targetLanguageIn = NotImplemented):
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
            catalogItemIdEqual,
            sourceLanguageEqual,
            sourceLanguageIn,
            outputFormatEqual,
            outputFormatIn)

        # @var KalturaCatalogItemLanguage
        self.targetLanguageEqual = targetLanguageEqual

        # @var str
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
class KalturaVendorLiveTranslationCatalogItemFilter(KalturaVendorTranslationCatalogItemBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented,
            targetLanguageEqual = NotImplemented,
            targetLanguageIn = NotImplemented):
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
            catalogItemIdEqual,
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
        self.fromXmlImpl(node, KalturaVendorLiveTranslationCatalogItemFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaVendorTranslationCatalogItemBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaVendorLiveTranslationCatalogItemFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaVendorTranslationCatalogItemFilter(KalturaVendorTranslationCatalogItemBaseFilter):
    def __init__(self,
            orderBy = NotImplemented,
            advancedSearch = NotImplemented,
            idEqual = NotImplemented,
            idIn = NotImplemented,
            idNotIn = NotImplemented,
            vendorPartnerIdEqual = NotImplemented,
            vendorPartnerIdIn = NotImplemented,
            createdAtGreaterThanOrEqual = NotImplemented,
            createdAtLessThanOrEqual = NotImplemented,
            updatedAtGreaterThanOrEqual = NotImplemented,
            updatedAtLessThanOrEqual = NotImplemented,
            statusEqual = NotImplemented,
            statusIn = NotImplemented,
            serviceTypeEqual = NotImplemented,
            serviceTypeIn = NotImplemented,
            serviceFeatureEqual = NotImplemented,
            serviceFeatureIn = NotImplemented,
            turnAroundTimeEqual = NotImplemented,
            turnAroundTimeIn = NotImplemented,
            partnerIdEqual = NotImplemented,
            catalogItemIdEqual = NotImplemented,
            sourceLanguageEqual = NotImplemented,
            sourceLanguageIn = NotImplemented,
            outputFormatEqual = NotImplemented,
            outputFormatIn = NotImplemented,
            targetLanguageEqual = NotImplemented,
            targetLanguageIn = NotImplemented):
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
            catalogItemIdEqual,
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

    def addFromBulkUpload(self, fileData, bulkUploadData = NotImplemented, bulkUploadVendorCatalogItemData = NotImplemented):
        kparams = KalturaParams()
        kfiles = {"fileData": fileData}
        kparams.addObjectIfDefined("bulkUploadData", bulkUploadData)
        kparams.addObjectIfDefined("bulkUploadVendorCatalogItemData", bulkUploadVendorCatalogItemData)
        self.client.queueServiceActionCall("reach_vendorcatalogitem", "addFromBulkUpload", "KalturaBulkUpload", kparams, kfiles)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaBulkUpload')

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

    def getServeUrl(self, vendorPartnerId = NotImplemented):
        kparams = KalturaParams()
        kparams.addIntIfDefined("vendorPartnerId", vendorPartnerId);
        self.client.queueServiceActionCall("reach_vendorcatalogitem", "getServeUrl", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

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

    def serve(self, vendorPartnerId = NotImplemented):
        kparams = KalturaParams()
        kparams.addIntIfDefined("vendorPartnerId", vendorPartnerId);
        self.client.queueServiceActionCall('reach_vendorcatalogitem', 'serve', None ,kparams)
        return self.client.getServeUrl()

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
        """sync vendor profile credit"""

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

    def getServeUrl(self, filterType = NotImplemented, filterInput = NotImplemented, status = NotImplemented, dueDate = NotImplemented):
        kparams = KalturaParams()
        kparams.addStringIfDefined("filterType", filterType)
        kparams.addIntIfDefined("filterInput", filterInput);
        kparams.addIntIfDefined("status", status);
        kparams.addStringIfDefined("dueDate", dueDate)
        self.client.queueServiceActionCall("reach_entryvendortask", "getServeUrl", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

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

    def serve(self, vendorPartnerId = NotImplemented, partnerId = NotImplemented, status = NotImplemented, dueDate = NotImplemented):
        kparams = KalturaParams()
        kparams.addIntIfDefined("vendorPartnerId", vendorPartnerId);
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addIntIfDefined("status", status);
        kparams.addStringIfDefined("dueDate", dueDate)
        self.client.queueServiceActionCall('reach_entryvendortask', 'serve', None ,kparams)
        return self.client.getServeUrl()

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

    def add(self, id, defaultReachProfileId = NotImplemented):
        """Assign existing catalogItem to specific account"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("defaultReachProfileId", defaultReachProfileId);
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
            'KalturaEntryObjectType': KalturaEntryObjectType,
            'KalturaEntryVendorTaskCreationMode': KalturaEntryVendorTaskCreationMode,
            'KalturaEntryVendorTaskStatus': KalturaEntryVendorTaskStatus,
            'KalturaReachProfileContentDeletionPolicy': KalturaReachProfileContentDeletionPolicy,
            'KalturaReachProfileStatus': KalturaReachProfileStatus,
            'KalturaReachProfileType': KalturaReachProfileType,
            'KalturaVendorCatalogItemOutputFormat': KalturaVendorCatalogItemOutputFormat,
            'KalturaVendorCatalogItemStage': KalturaVendorCatalogItemStage,
            'KalturaVendorCatalogItemStatus': KalturaVendorCatalogItemStatus,
            'KalturaVendorServiceFeature': KalturaVendorServiceFeature,
            'KalturaVendorServiceTurnAroundTime': KalturaVendorServiceTurnAroundTime,
            'KalturaVendorServiceType': KalturaVendorServiceType,
            'KalturaVendorTaskProcessingRegion': KalturaVendorTaskProcessingRegion,
            'KalturaVendorVideoAnalysisType': KalturaVendorVideoAnalysisType,
            'KalturaCatalogItemLanguage': KalturaCatalogItemLanguage,
            'KalturaEntryVendorTaskOrderBy': KalturaEntryVendorTaskOrderBy,
            'KalturaReachProfileOrderBy': KalturaReachProfileOrderBy,
            'KalturaReachVendorEngineType': KalturaReachVendorEngineType,
            'KalturaSummaryWritingStyleTaskData': KalturaSummaryWritingStyleTaskData,
            'KalturaTypeOfSummaryTaskData': KalturaTypeOfSummaryTaskData,
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
            'KalturaCatalogItemAdvancedFilter': KalturaCatalogItemAdvancedFilter,
            'KalturaCategoryEntryCondition': KalturaCategoryEntryCondition,
            'KalturaClipsVendorTaskData': KalturaClipsVendorTaskData,
            'KalturaEntryVendorTaskListResponse': KalturaEntryVendorTaskListResponse,
            'KalturaIntelligentTaggingVendorTaskData': KalturaIntelligentTaggingVendorTaskData,
            'KalturaMetadataEnrichmentVendorTaskData': KalturaMetadataEnrichmentVendorTaskData,
            'KalturaModerationVendorTaskData': KalturaModerationVendorTaskData,
            'KalturaQuizVendorTaskData': KalturaQuizVendorTaskData,
            'KalturaReachProfileListResponse': KalturaReachProfileListResponse,
            'KalturaScheduledVendorTaskData': KalturaScheduledVendorTaskData,
            'KalturaSummaryVendorTaskData': KalturaSummaryVendorTaskData,
            'KalturaUnlimitedVendorCredit': KalturaUnlimitedVendorCredit,
            'KalturaVendorAlignmentCatalogItem': KalturaVendorAlignmentCatalogItem,
            'KalturaVendorAudioDescriptionCatalogItem': KalturaVendorAudioDescriptionCatalogItem,
            'KalturaVendorCaptionsCatalogItem': KalturaVendorCaptionsCatalogItem,
            'KalturaVendorCatalogItemListResponse': KalturaVendorCatalogItemListResponse,
            'KalturaVendorChapteringCatalogItem': KalturaVendorChapteringCatalogItem,
            'KalturaVendorClipsCatalogItem': KalturaVendorClipsCatalogItem,
            'KalturaVendorCredit': KalturaVendorCredit,
            'KalturaVendorDubbingCatalogItem': KalturaVendorDubbingCatalogItem,
            'KalturaVendorExtendedAudioDescriptionCatalogItem': KalturaVendorExtendedAudioDescriptionCatalogItem,
            'KalturaVendorIntelligentTaggingCatalogItem': KalturaVendorIntelligentTaggingCatalogItem,
            'KalturaVendorMetadataEnrichmentCatalogItem': KalturaVendorMetadataEnrichmentCatalogItem,
            'KalturaVendorModerationCatalogItem': KalturaVendorModerationCatalogItem,
            'KalturaVendorQuizCatalogItem': KalturaVendorQuizCatalogItem,
            'KalturaVendorSummaryCatalogItem': KalturaVendorSummaryCatalogItem,
            'KalturaVendorTaskDataCaptionAsset': KalturaVendorTaskDataCaptionAsset,
            'KalturaVendorVideoAnalysisCatalogItem': KalturaVendorVideoAnalysisCatalogItem,
            'KalturaAlignmentVendorTaskData': KalturaAlignmentVendorTaskData,
            'KalturaEntryVendorTaskBaseFilter': KalturaEntryVendorTaskBaseFilter,
            'KalturaEntryVendorTaskFilter': KalturaEntryVendorTaskFilter,
            'KalturaEntryVendorTaskCsvJobData': KalturaEntryVendorTaskCsvJobData,
            'KalturaReachProfileBaseFilter': KalturaReachProfileBaseFilter,
            'KalturaReachReportInputFilter': KalturaReachReportInputFilter,
            'KalturaTimeRangeVendorCredit': KalturaTimeRangeVendorCredit,
            'KalturaTranslationVendorTaskData': KalturaTranslationVendorTaskData,
            'KalturaVendorCatalogItemBaseFilter': KalturaVendorCatalogItemBaseFilter,
            'KalturaVendorLiveCatalogItem': KalturaVendorLiveCatalogItem,
            'KalturaVendorTranslationCatalogItem': KalturaVendorTranslationCatalogItem,
            'KalturaReachProfileFilter': KalturaReachProfileFilter,
            'KalturaReoccurringVendorCredit': KalturaReoccurringVendorCredit,
            'KalturaVendorCatalogItemFilter': KalturaVendorCatalogItemFilter,
            'KalturaVendorLiveCaptionCatalogItem': KalturaVendorLiveCaptionCatalogItem,
            'KalturaVendorLiveTranslationCatalogItem': KalturaVendorLiveTranslationCatalogItem,
            'KalturaVendorCaptionsCatalogItemBaseFilter': KalturaVendorCaptionsCatalogItemBaseFilter,
            'KalturaVendorClipsCatalogItemFilter': KalturaVendorClipsCatalogItemFilter,
            'KalturaVendorDubbingCatalogItemBaseFilter': KalturaVendorDubbingCatalogItemBaseFilter,
            'KalturaVendorIntelligentTaggingCatalogItemFilter': KalturaVendorIntelligentTaggingCatalogItemFilter,
            'KalturaVendorMetadataEnrichmentCatalogItemFilter': KalturaVendorMetadataEnrichmentCatalogItemFilter,
            'KalturaVendorModerationCatalogItemFilter': KalturaVendorModerationCatalogItemFilter,
            'KalturaVendorQuizCatalogItemFilter': KalturaVendorQuizCatalogItemFilter,
            'KalturaVendorSummaryCatalogItemFilter': KalturaVendorSummaryCatalogItemFilter,
            'KalturaVendorVideoAnalysisCatalogItemFilter': KalturaVendorVideoAnalysisCatalogItemFilter,
            'KalturaVendorAlignmentCatalogItemFilter': KalturaVendorAlignmentCatalogItemFilter,
            'KalturaVendorAudioDescriptionCatalogItemFilter': KalturaVendorAudioDescriptionCatalogItemFilter,
            'KalturaVendorCaptionsCatalogItemFilter': KalturaVendorCaptionsCatalogItemFilter,
            'KalturaVendorChapteringCatalogItemFilter': KalturaVendorChapteringCatalogItemFilter,
            'KalturaVendorDubbingCatalogItemFilter': KalturaVendorDubbingCatalogItemFilter,
            'KalturaVendorExtendedAudioDescriptionCatalogItemFilter': KalturaVendorExtendedAudioDescriptionCatalogItemFilter,
            'KalturaVendorLiveCaptionCatalogItemFilter': KalturaVendorLiveCaptionCatalogItemFilter,
            'KalturaVendorTranslationCatalogItemBaseFilter': KalturaVendorTranslationCatalogItemBaseFilter,
            'KalturaVendorLiveTranslationCatalogItemFilter': KalturaVendorLiveTranslationCatalogItemFilter,
            'KalturaVendorTranslationCatalogItemFilter': KalturaVendorTranslationCatalogItemFilter,
        }

    # @return string
    def getName(self):
        return 'reach'

