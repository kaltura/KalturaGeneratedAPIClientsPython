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
from typing import List, IO, Any
from .Core import *
from .EventNotification import *
from .BulkUpload import *
from .Caption import *
from .Schedule import *
from .Transcript import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaEntryObjectType(object):
    ENTRY = 1

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaEntryVendorTaskCreationMode(object):
    MANUAL = 1
    AUTOMATIC = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

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

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaReachProfileContentDeletionPolicy(object):
    DO_NOTHING = 1
    DELETE_ONCE_PROCESSED = 2
    DELETE_AFTER_WEEK = 3
    DELETE_AFTER_MONTH = 4
    DELETE_AFTER_THREE_MONTHS = 5

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaReachProfileStatus(object):
    DISABLED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaReachProfileType(object):
    FREE_TRIAL = 1
    PAID = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVendorCatalogItemOutputFormat(object):
    SRT = 1
    DFXP = 2
    VTT = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVendorCatalogItemStage(object):
    PRODUCTION = 1
    QA = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVendorCatalogItemStatus(object):
    DEPRECATED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

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

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

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

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVendorServiceType(object):
    HUMAN = 1
    MACHINE = 2

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVendorTaskProcessingRegion(object):
    US = 1
    EU = 2
    CA = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaVendorVideoAnalysisType(object):
    OCR = 1

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

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

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

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

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaReachProfileOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaReachVendorEngineType(object):
    OPEN_CALAIS = "OpenCalaisReachVendor.OPEN_CALAIS"
    HELLO_WORLD = "ReachInternal.HELLO_WORLD"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaSummaryWritingStyleTaskData(object):
    CASUAL = "casual"
    FORMAL = "formal"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaTypeOfSummaryTaskData(object):
    CONCISE = "concise"
    DETAILED = "detailed"
    EXTENSIVE = "extensive"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVendorCaptionsCatalogItemOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVendorCatalogItemOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVendorCatalogItemPriceFunction(object):
    PRICE_PER_HOUR = "kReachUtils::calcPricePerHour"
    PRICE_PER_MINUTE = "kReachUtils::calcPricePerMinute"
    PRICE_PER_SECOND = "kReachUtils::calcPricePerSecond"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVendorCreditRecurrenceFrequency(object):
    DAILY = "day"
    MONTHLY = "month"
    WEEKLY = "week"
    YEARLY = "year"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaVendorTranslationCatalogItemOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    ID_ASC = "+id"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    ID_DESC = "-id"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaBaseVendorCredit(KalturaObjectBase):
    def __init__(self): ...
        pass

class KalturaDictionary(KalturaObjectBase):
    language: KalturaCatalogItemLanguage
    data: str
    def __init__(self,
            language: KalturaCatalogItemLanguage = NotImplemented,
            data: str = NotImplemented): ...

    def getLanguage(self) -> KalturaCatalogItemLanguage: ...
    def setLanguage(self, newLanguage: KalturaCatalogItemLanguage) -> None: ...
    def getData(self) -> str: ...
    def setData(self, newData: str) -> None: ...

class KalturaVendorTaskData(KalturaObjectBase):
    entryDuration: int
    def __init__(self,
            entryDuration: int = NotImplemented): ...

    def getEntryDuration(self) -> int: ...

class KalturaEntryVendorTask(KalturaObjectBase):
    id: int
    partnerId: int
    vendorPartnerId: int
    createdAt: int
    updatedAt: int
    queueTime: int
    finishTime: int
    entryId: str
    status: KalturaEntryVendorTaskStatus
    reachProfileId: int
    catalogItemId: int
    price: float
    userId: str
    entryObjectType: KalturaEntryObjectType
    moderatingUser: str
    errDescription: str
    accessKey: str
    version: str
    notes: str
    dictionary: str
    context: str
    accuracy: int
    outputObjectId: str
    partnerData: str
    creationMode: KalturaEntryVendorTaskCreationMode
    taskJobData: KalturaVendorTaskData
    expectedFinishTime: int
    serviceType: KalturaVendorServiceType
    serviceFeature: KalturaVendorServiceFeature
    turnAroundTime: KalturaVendorServiceTurnAroundTime
    externalTaskId: str
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            queueTime: int = NotImplemented,
            finishTime: int = NotImplemented,
            entryId: str = NotImplemented,
            status: KalturaEntryVendorTaskStatus = NotImplemented,
            reachProfileId: int = NotImplemented,
            catalogItemId: int = NotImplemented,
            price: float = NotImplemented,
            userId: str = NotImplemented,
            entryObjectType: KalturaEntryObjectType = NotImplemented,
            moderatingUser: str = NotImplemented,
            errDescription: str = NotImplemented,
            accessKey: str = NotImplemented,
            version: str = NotImplemented,
            notes: str = NotImplemented,
            dictionary: str = NotImplemented,
            context: str = NotImplemented,
            accuracy: int = NotImplemented,
            outputObjectId: str = NotImplemented,
            partnerData: str = NotImplemented,
            creationMode: KalturaEntryVendorTaskCreationMode = NotImplemented,
            taskJobData: KalturaVendorTaskData = NotImplemented,
            expectedFinishTime: int = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            externalTaskId: str = NotImplemented): ...

    def getId(self) -> int: ...
    def getPartnerId(self) -> int: ...
    def getVendorPartnerId(self) -> int: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getQueueTime(self) -> int: ...
    def getFinishTime(self) -> int: ...
    def getEntryId(self) -> str: ...
    def setEntryId(self, newEntryId: str) -> None: ...
    def getStatus(self) -> KalturaEntryVendorTaskStatus: ...
    def setStatus(self, newStatus: KalturaEntryVendorTaskStatus) -> None: ...
    def getReachProfileId(self) -> int: ...
    def setReachProfileId(self, newReachProfileId: int) -> None: ...
    def getCatalogItemId(self) -> int: ...
    def setCatalogItemId(self, newCatalogItemId: int) -> None: ...
    def getPrice(self) -> float: ...
    def getUserId(self) -> str: ...
    def getEntryObjectType(self) -> KalturaEntryObjectType: ...
    def setEntryObjectType(self, newEntryObjectType: KalturaEntryObjectType) -> None: ...
    def getModeratingUser(self) -> str: ...
    def getErrDescription(self) -> str: ...
    def setErrDescription(self, newErrDescription: str) -> None: ...
    def getAccessKey(self) -> str: ...
    def getVersion(self) -> str: ...
    def getNotes(self) -> str: ...
    def setNotes(self, newNotes: str) -> None: ...
    def getDictionary(self) -> str: ...
    def getContext(self) -> str: ...
    def setContext(self, newContext: str) -> None: ...
    def getAccuracy(self) -> int: ...
    def setAccuracy(self, newAccuracy: int) -> None: ...
    def getOutputObjectId(self) -> str: ...
    def setOutputObjectId(self, newOutputObjectId: str) -> None: ...
    def getPartnerData(self) -> str: ...
    def setPartnerData(self, newPartnerData: str) -> None: ...
    def getCreationMode(self) -> KalturaEntryVendorTaskCreationMode: ...
    def getTaskJobData(self) -> KalturaVendorTaskData: ...
    def setTaskJobData(self, newTaskJobData: KalturaVendorTaskData) -> None: ...
    def getExpectedFinishTime(self) -> int: ...
    def getServiceType(self) -> KalturaVendorServiceType: ...
    def getServiceFeature(self) -> KalturaVendorServiceFeature: ...
    def getTurnAroundTime(self) -> KalturaVendorServiceTurnAroundTime: ...
    def getExternalTaskId(self) -> str: ...
    def setExternalTaskId(self, newExternalTaskId: str) -> None: ...

class KalturaReachProfile(KalturaObjectBase):
    id: int
    name: str
    partnerId: int
    createdAt: int
    updatedAt: int
    status: KalturaReachProfileStatus
    profileType: KalturaReachProfileType
    defaultOutputFormat: KalturaVendorCatalogItemOutputFormat
    enableMachineModeration: KalturaNullableBoolean
    enableHumanModeration: KalturaNullableBoolean
    autoDisplayMachineCaptionsOnPlayer: KalturaNullableBoolean
    autoDisplayHumanCaptionsOnPlayer: KalturaNullableBoolean
    enableMetadataExtraction: KalturaNullableBoolean
    enableSpeakerChangeIndication: KalturaNullableBoolean
    enableAudioTags: KalturaNullableBoolean
    enableProfanityRemoval: KalturaNullableBoolean
    maxCharactersPerCaptionLine: int
    labelAdditionForMachineServiceType: str
    labelAdditionForHumanServiceType: str
    contentDeletionPolicy: KalturaReachProfileContentDeletionPolicy
    rules: List[KalturaRule]
    credit: KalturaBaseVendorCredit
    usedCredit: float
    dictionaries: List[KalturaDictionary]
    flavorParamsIds: str
    vendorTaskProcessingRegion: KalturaVendorTaskProcessingRegion
    def __init__(self,
            id: int = NotImplemented,
            name: str = NotImplemented,
            partnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaReachProfileStatus = NotImplemented,
            profileType: KalturaReachProfileType = NotImplemented,
            defaultOutputFormat: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            enableMachineModeration: KalturaNullableBoolean = NotImplemented,
            enableHumanModeration: KalturaNullableBoolean = NotImplemented,
            autoDisplayMachineCaptionsOnPlayer: KalturaNullableBoolean = NotImplemented,
            autoDisplayHumanCaptionsOnPlayer: KalturaNullableBoolean = NotImplemented,
            enableMetadataExtraction: KalturaNullableBoolean = NotImplemented,
            enableSpeakerChangeIndication: KalturaNullableBoolean = NotImplemented,
            enableAudioTags: KalturaNullableBoolean = NotImplemented,
            enableProfanityRemoval: KalturaNullableBoolean = NotImplemented,
            maxCharactersPerCaptionLine: int = NotImplemented,
            labelAdditionForMachineServiceType: str = NotImplemented,
            labelAdditionForHumanServiceType: str = NotImplemented,
            contentDeletionPolicy: KalturaReachProfileContentDeletionPolicy = NotImplemented,
            rules: List[KalturaRule] = NotImplemented,
            credit: KalturaBaseVendorCredit = NotImplemented,
            usedCredit: float = NotImplemented,
            dictionaries: List[KalturaDictionary] = NotImplemented,
            flavorParamsIds: str = NotImplemented,
            vendorTaskProcessingRegion: KalturaVendorTaskProcessingRegion = NotImplemented): ...

    def getId(self) -> int: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getPartnerId(self) -> int: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getStatus(self) -> KalturaReachProfileStatus: ...
    def getProfileType(self) -> KalturaReachProfileType: ...
    def setProfileType(self, newProfileType: KalturaReachProfileType) -> None: ...
    def getDefaultOutputFormat(self) -> KalturaVendorCatalogItemOutputFormat: ...
    def setDefaultOutputFormat(self, newDefaultOutputFormat: KalturaVendorCatalogItemOutputFormat) -> None: ...
    def getEnableMachineModeration(self) -> KalturaNullableBoolean: ...
    def setEnableMachineModeration(self, newEnableMachineModeration: KalturaNullableBoolean) -> None: ...
    def getEnableHumanModeration(self) -> KalturaNullableBoolean: ...
    def setEnableHumanModeration(self, newEnableHumanModeration: KalturaNullableBoolean) -> None: ...
    def getAutoDisplayMachineCaptionsOnPlayer(self) -> KalturaNullableBoolean: ...
    def setAutoDisplayMachineCaptionsOnPlayer(self, newAutoDisplayMachineCaptionsOnPlayer: KalturaNullableBoolean) -> None: ...
    def getAutoDisplayHumanCaptionsOnPlayer(self) -> KalturaNullableBoolean: ...
    def setAutoDisplayHumanCaptionsOnPlayer(self, newAutoDisplayHumanCaptionsOnPlayer: KalturaNullableBoolean) -> None: ...
    def getEnableMetadataExtraction(self) -> KalturaNullableBoolean: ...
    def setEnableMetadataExtraction(self, newEnableMetadataExtraction: KalturaNullableBoolean) -> None: ...
    def getEnableSpeakerChangeIndication(self) -> KalturaNullableBoolean: ...
    def setEnableSpeakerChangeIndication(self, newEnableSpeakerChangeIndication: KalturaNullableBoolean) -> None: ...
    def getEnableAudioTags(self) -> KalturaNullableBoolean: ...
    def setEnableAudioTags(self, newEnableAudioTags: KalturaNullableBoolean) -> None: ...
    def getEnableProfanityRemoval(self) -> KalturaNullableBoolean: ...
    def setEnableProfanityRemoval(self, newEnableProfanityRemoval: KalturaNullableBoolean) -> None: ...
    def getMaxCharactersPerCaptionLine(self) -> int: ...
    def setMaxCharactersPerCaptionLine(self, newMaxCharactersPerCaptionLine: int) -> None: ...
    def getLabelAdditionForMachineServiceType(self) -> str: ...
    def setLabelAdditionForMachineServiceType(self, newLabelAdditionForMachineServiceType: str) -> None: ...
    def getLabelAdditionForHumanServiceType(self) -> str: ...
    def setLabelAdditionForHumanServiceType(self, newLabelAdditionForHumanServiceType: str) -> None: ...
    def getContentDeletionPolicy(self) -> KalturaReachProfileContentDeletionPolicy: ...
    def setContentDeletionPolicy(self, newContentDeletionPolicy: KalturaReachProfileContentDeletionPolicy) -> None: ...
    def getRules(self) -> List[KalturaRule]: ...
    def setRules(self, newRules: List[KalturaRule]) -> None: ...
    def getCredit(self) -> KalturaBaseVendorCredit: ...
    def setCredit(self, newCredit: KalturaBaseVendorCredit) -> None: ...
    def getUsedCredit(self) -> float: ...
    def getDictionaries(self) -> List[KalturaDictionary]: ...
    def setDictionaries(self, newDictionaries: List[KalturaDictionary]) -> None: ...
    def getFlavorParamsIds(self) -> str: ...
    def setFlavorParamsIds(self, newFlavorParamsIds: str) -> None: ...
    def getVendorTaskProcessingRegion(self) -> KalturaVendorTaskProcessingRegion: ...
    def setVendorTaskProcessingRegion(self, newVendorTaskProcessingRegion: KalturaVendorTaskProcessingRegion) -> None: ...

class KalturaVendorCatalogItemPricing(KalturaObjectBase):
    pricePerUnit: float
    priceFunction: KalturaVendorCatalogItemPriceFunction
    def __init__(self,
            pricePerUnit: float = NotImplemented,
            priceFunction: KalturaVendorCatalogItemPriceFunction = NotImplemented): ...

    def getPricePerUnit(self) -> float: ...
    def setPricePerUnit(self, newPricePerUnit: float) -> None: ...
    def getPriceFunction(self) -> KalturaVendorCatalogItemPriceFunction: ...
    def setPriceFunction(self, newPriceFunction: KalturaVendorCatalogItemPriceFunction) -> None: ...

class KalturaVendorCatalogItem(KalturaObjectBase):
    id: int
    vendorPartnerId: int
    name: str
    systemName: str
    createdAt: int
    updatedAt: int
    status: KalturaVendorCatalogItemStatus
    serviceType: KalturaVendorServiceType
    serviceFeature: KalturaVendorServiceFeature
    turnAroundTime: KalturaVendorServiceTurnAroundTime
    pricing: KalturaVendorCatalogItemPricing
    engineType: KalturaReachVendorEngineType
    sourceLanguage: KalturaCatalogItemLanguage
    allowResubmission: bool
    requiresOverages: bool
    vendorData: str
    stage: KalturaVendorCatalogItemStage
    lastBulkUpdateId: int
    contract: str
    createdBy: str
    notes: str
    partnerId: int
    defaultReachProfileId: int
    adminTagsToExclude: str
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented): ...

    def getId(self) -> int: ...
    def getVendorPartnerId(self) -> int: ...
    def setVendorPartnerId(self, newVendorPartnerId: int) -> None: ...
    def getName(self) -> str: ...
    def setName(self, newName: str) -> None: ...
    def getSystemName(self) -> str: ...
    def setSystemName(self, newSystemName: str) -> None: ...
    def getCreatedAt(self) -> int: ...
    def getUpdatedAt(self) -> int: ...
    def getStatus(self) -> KalturaVendorCatalogItemStatus: ...
    def getServiceType(self) -> KalturaVendorServiceType: ...
    def setServiceType(self, newServiceType: KalturaVendorServiceType) -> None: ...
    def getServiceFeature(self) -> KalturaVendorServiceFeature: ...
    def getTurnAroundTime(self) -> KalturaVendorServiceTurnAroundTime: ...
    def setTurnAroundTime(self, newTurnAroundTime: KalturaVendorServiceTurnAroundTime) -> None: ...
    def getPricing(self) -> KalturaVendorCatalogItemPricing: ...
    def setPricing(self, newPricing: KalturaVendorCatalogItemPricing) -> None: ...
    def getEngineType(self) -> KalturaReachVendorEngineType: ...
    def setEngineType(self, newEngineType: KalturaReachVendorEngineType) -> None: ...
    def getSourceLanguage(self) -> KalturaCatalogItemLanguage: ...
    def setSourceLanguage(self, newSourceLanguage: KalturaCatalogItemLanguage) -> None: ...
    def getAllowResubmission(self) -> bool: ...
    def setAllowResubmission(self, newAllowResubmission: bool) -> None: ...
    def getRequiresOverages(self) -> bool: ...
    def setRequiresOverages(self, newRequiresOverages: bool) -> None: ...
    def getVendorData(self) -> str: ...
    def setVendorData(self, newVendorData: str) -> None: ...
    def getStage(self) -> KalturaVendorCatalogItemStage: ...
    def setStage(self, newStage: KalturaVendorCatalogItemStage) -> None: ...
    def getLastBulkUpdateId(self) -> int: ...
    def setLastBulkUpdateId(self, newLastBulkUpdateId: int) -> None: ...
    def getContract(self) -> str: ...
    def setContract(self, newContract: str) -> None: ...
    def getCreatedBy(self) -> str: ...
    def setCreatedBy(self, newCreatedBy: str) -> None: ...
    def getNotes(self) -> str: ...
    def setNotes(self, newNotes: str) -> None: ...
    def getPartnerId(self) -> int: ...
    def setPartnerId(self, newPartnerId: int) -> None: ...
    def getDefaultReachProfileId(self) -> int: ...
    def setDefaultReachProfileId(self, newDefaultReachProfileId: int) -> None: ...
    def getAdminTagsToExclude(self) -> str: ...
    def setAdminTagsToExclude(self, newAdminTagsToExclude: str) -> None: ...

class KalturaAddEntryVendorTaskAction(KalturaRuleAction):
    catalogItemIds: str
    def __init__(self,
            type: KalturaRuleActionType = NotImplemented,
            catalogItemIds: str = NotImplemented): ...

    def getCatalogItemIds(self) -> str: ...
    def setCatalogItemIds(self, newCatalogItemIds: str) -> None: ...

class KalturaCatalogItemAdvancedFilter(KalturaSearchItem):
    serviceTypeEqual: KalturaVendorServiceType
    serviceTypeIn: str
    serviceFeatureEqual: KalturaVendorServiceFeature
    serviceFeatureIn: str
    turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime
    turnAroundTimeIn: str
    sourceLanguageEqual: KalturaCatalogItemLanguage
    targetLanguageEqual: KalturaCatalogItemLanguage
    def __init__(self,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            targetLanguageEqual: KalturaCatalogItemLanguage = NotImplemented): ...

    def getServiceTypeEqual(self) -> KalturaVendorServiceType: ...
    def setServiceTypeEqual(self, newServiceTypeEqual: KalturaVendorServiceType) -> None: ...
    def getServiceTypeIn(self) -> str: ...
    def setServiceTypeIn(self, newServiceTypeIn: str) -> None: ...
    def getServiceFeatureEqual(self) -> KalturaVendorServiceFeature: ...
    def setServiceFeatureEqual(self, newServiceFeatureEqual: KalturaVendorServiceFeature) -> None: ...
    def getServiceFeatureIn(self) -> str: ...
    def setServiceFeatureIn(self, newServiceFeatureIn: str) -> None: ...
    def getTurnAroundTimeEqual(self) -> KalturaVendorServiceTurnAroundTime: ...
    def setTurnAroundTimeEqual(self, newTurnAroundTimeEqual: KalturaVendorServiceTurnAroundTime) -> None: ...
    def getTurnAroundTimeIn(self) -> str: ...
    def setTurnAroundTimeIn(self, newTurnAroundTimeIn: str) -> None: ...
    def getSourceLanguageEqual(self) -> KalturaCatalogItemLanguage: ...
    def setSourceLanguageEqual(self, newSourceLanguageEqual: KalturaCatalogItemLanguage) -> None: ...
    def getTargetLanguageEqual(self) -> KalturaCatalogItemLanguage: ...
    def setTargetLanguageEqual(self, newTargetLanguageEqual: KalturaCatalogItemLanguage) -> None: ...

class KalturaCategoryEntryCondition(KalturaCondition):
    categoryId: int
    categoryIds: str
    categoryUserPermission: KalturaCategoryUserPermissionLevel
    comparison: KalturaSearchConditionComparison
    def __init__(self,
            type: KalturaConditionType = NotImplemented,
            description: str = NotImplemented,
            not_: bool = NotImplemented,
            categoryId: int = NotImplemented,
            categoryIds: str = NotImplemented,
            categoryUserPermission: KalturaCategoryUserPermissionLevel = NotImplemented,
            comparison: KalturaSearchConditionComparison = NotImplemented): ...

    def getCategoryId(self) -> int: ...
    def setCategoryId(self, newCategoryId: int) -> None: ...
    def getCategoryIds(self) -> str: ...
    def setCategoryIds(self, newCategoryIds: str) -> None: ...
    def getCategoryUserPermission(self) -> KalturaCategoryUserPermissionLevel: ...
    def setCategoryUserPermission(self, newCategoryUserPermission: KalturaCategoryUserPermissionLevel) -> None: ...
    def getComparison(self) -> KalturaSearchConditionComparison: ...
    def setComparison(self, newComparison: KalturaSearchConditionComparison) -> None: ...

class KalturaClipsVendorTaskData(KalturaVendorTaskData):
    clipsDuration: int
    eventSessionContextId: str
    instruction: str
    clipsOutputJson: str
    def __init__(self,
            entryDuration: int = NotImplemented,
            clipsDuration: int = NotImplemented,
            eventSessionContextId: str = NotImplemented,
            instruction: str = NotImplemented,
            clipsOutputJson: str = NotImplemented): ...

    def getClipsDuration(self) -> int: ...
    def setClipsDuration(self, newClipsDuration: int) -> None: ...
    def getEventSessionContextId(self) -> str: ...
    def setEventSessionContextId(self, newEventSessionContextId: str) -> None: ...
    def getInstruction(self) -> str: ...
    def setInstruction(self, newInstruction: str) -> None: ...
    def getClipsOutputJson(self) -> str: ...
    def setClipsOutputJson(self, newClipsOutputJson: str) -> None: ...

class KalturaEntryVendorTaskListResponse(KalturaListResponse):
    objects: List[KalturaEntryVendorTask]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaEntryVendorTask] = NotImplemented): ...

    def getObjects(self) -> List[KalturaEntryVendorTask]: ...

class KalturaIntelligentTaggingVendorTaskData(KalturaVendorTaskData):
    assetId: str
    def __init__(self,
            entryDuration: int = NotImplemented,
            assetId: str = NotImplemented): ...

    def getAssetId(self) -> str: ...
    def setAssetId(self, newAssetId: str) -> None: ...

class KalturaMetadataEnrichmentVendorTaskData(KalturaVendorTaskData):
    detailLevel: str
    instruction: str
    outputJson: str
    def __init__(self,
            entryDuration: int = NotImplemented,
            detailLevel: str = NotImplemented,
            instruction: str = NotImplemented,
            outputJson: str = NotImplemented): ...

    def getDetailLevel(self) -> str: ...
    def setDetailLevel(self, newDetailLevel: str) -> None: ...
    def getInstruction(self) -> str: ...
    def setInstruction(self, newInstruction: str) -> None: ...
    def getOutputJson(self) -> str: ...
    def setOutputJson(self, newOutputJson: str) -> None: ...

class KalturaModerationVendorTaskData(KalturaVendorTaskData):
    ruleIds: str
    policyIds: str
    moderationOutputJson: str
    def __init__(self,
            entryDuration: int = NotImplemented,
            ruleIds: str = NotImplemented,
            policyIds: str = NotImplemented,
            moderationOutputJson: str = NotImplemented): ...

    def getRuleIds(self) -> str: ...
    def setRuleIds(self, newRuleIds: str) -> None: ...
    def getPolicyIds(self) -> str: ...
    def setPolicyIds(self, newPolicyIds: str) -> None: ...
    def getModerationOutputJson(self) -> str: ...
    def setModerationOutputJson(self, newModerationOutputJson: str) -> None: ...

class KalturaQuizVendorTaskData(KalturaVendorTaskData):
    numberOfQuestions: int
    questionsType: str
    context: str
    formalStyle: str
    createQuiz: bool
    quizOutput: str
    def __init__(self,
            entryDuration: int = NotImplemented,
            numberOfQuestions: int = NotImplemented,
            questionsType: str = NotImplemented,
            context: str = NotImplemented,
            formalStyle: str = NotImplemented,
            createQuiz: bool = NotImplemented,
            quizOutput: str = NotImplemented): ...

    def getNumberOfQuestions(self) -> int: ...
    def setNumberOfQuestions(self, newNumberOfQuestions: int) -> None: ...
    def getQuestionsType(self) -> str: ...
    def setQuestionsType(self, newQuestionsType: str) -> None: ...
    def getContext(self) -> str: ...
    def setContext(self, newContext: str) -> None: ...
    def getFormalStyle(self) -> str: ...
    def setFormalStyle(self, newFormalStyle: str) -> None: ...
    def getCreateQuiz(self) -> bool: ...
    def setCreateQuiz(self, newCreateQuiz: bool) -> None: ...
    def getQuizOutput(self) -> str: ...
    def setQuizOutput(self, newQuizOutput: str) -> None: ...

class KalturaReachProfileListResponse(KalturaListResponse):
    objects: List[KalturaReachProfile]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaReachProfile] = NotImplemented): ...

    def getObjects(self) -> List[KalturaReachProfile]: ...

class KalturaScheduledVendorTaskData(KalturaVendorTaskData):
    startDate: int
    endDate: int
    scheduledEventId: int
    def __init__(self,
            entryDuration: int = NotImplemented,
            startDate: int = NotImplemented,
            endDate: int = NotImplemented,
            scheduledEventId: int = NotImplemented): ...

    def getStartDate(self) -> int: ...
    def setStartDate(self, newStartDate: int) -> None: ...
    def getEndDate(self) -> int: ...
    def setEndDate(self, newEndDate: int) -> None: ...
    def getScheduledEventId(self) -> int: ...
    def setScheduledEventId(self, newScheduledEventId: int) -> None: ...

class KalturaSummaryVendorTaskData(KalturaVendorTaskData):
    typeOfSummary: KalturaTypeOfSummaryTaskData
    writingStyle: KalturaSummaryWritingStyleTaskData
    language: KalturaLanguageCode
    summaryOutputJson: str
    def __init__(self,
            entryDuration: int = NotImplemented,
            typeOfSummary: KalturaTypeOfSummaryTaskData = NotImplemented,
            writingStyle: KalturaSummaryWritingStyleTaskData = NotImplemented,
            language: KalturaLanguageCode = NotImplemented,
            summaryOutputJson: str = NotImplemented): ...

    def getTypeOfSummary(self) -> KalturaTypeOfSummaryTaskData: ...
    def setTypeOfSummary(self, newTypeOfSummary: KalturaTypeOfSummaryTaskData) -> None: ...
    def getWritingStyle(self) -> KalturaSummaryWritingStyleTaskData: ...
    def setWritingStyle(self, newWritingStyle: KalturaSummaryWritingStyleTaskData) -> None: ...
    def getLanguage(self) -> KalturaLanguageCode: ...
    def setLanguage(self, newLanguage: KalturaLanguageCode) -> None: ...
    def getSummaryOutputJson(self) -> str: ...
    def setSummaryOutputJson(self, newSummaryOutputJson: str) -> None: ...

class KalturaUnlimitedVendorCredit(KalturaBaseVendorCredit):
    credit: int
    fromDate: int
    def __init__(self,
            credit: int = NotImplemented,
            fromDate: int = NotImplemented): ...

    def getCredit(self) -> int: ...
    def getFromDate(self) -> int: ...
    def setFromDate(self, newFromDate: int) -> None: ...

class KalturaVendorAlignmentCatalogItem(KalturaVendorCatalogItem):
    outputFormat: KalturaVendorCatalogItemOutputFormat
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            outputFormat: KalturaVendorCatalogItemOutputFormat = NotImplemented): ...

    def getOutputFormat(self) -> KalturaVendorCatalogItemOutputFormat: ...
    def setOutputFormat(self, newOutputFormat: KalturaVendorCatalogItemOutputFormat) -> None: ...

class KalturaVendorAudioDescriptionCatalogItem(KalturaVendorCatalogItem):
    flavorParamsId: int
    clearAudioFlavorParamsId: int
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            flavorParamsId: int = NotImplemented,
            clearAudioFlavorParamsId: int = NotImplemented): ...

    def getFlavorParamsId(self) -> int: ...
    def setFlavorParamsId(self, newFlavorParamsId: int) -> None: ...
    def getClearAudioFlavorParamsId(self) -> int: ...
    def setClearAudioFlavorParamsId(self, newClearAudioFlavorParamsId: int) -> None: ...

class KalturaVendorCaptionsCatalogItem(KalturaVendorCatalogItem):
    outputFormat: KalturaVendorCatalogItemOutputFormat
    enableSpeakerId: KalturaNullableBoolean
    fixedPriceAddons: int
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            outputFormat: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            enableSpeakerId: KalturaNullableBoolean = NotImplemented,
            fixedPriceAddons: int = NotImplemented): ...

    def getOutputFormat(self) -> KalturaVendorCatalogItemOutputFormat: ...
    def setOutputFormat(self, newOutputFormat: KalturaVendorCatalogItemOutputFormat) -> None: ...
    def getEnableSpeakerId(self) -> KalturaNullableBoolean: ...
    def setEnableSpeakerId(self, newEnableSpeakerId: KalturaNullableBoolean) -> None: ...
    def getFixedPriceAddons(self) -> int: ...
    def setFixedPriceAddons(self, newFixedPriceAddons: int) -> None: ...

class KalturaVendorCatalogItemListResponse(KalturaListResponse):
    objects: List[KalturaVendorCatalogItem]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaVendorCatalogItem] = NotImplemented): ...

    def getObjects(self) -> List[KalturaVendorCatalogItem]: ...

class KalturaVendorChapteringCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented): ...
        pass

class KalturaVendorClipsCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented): ...
        pass

class KalturaVendorCredit(KalturaBaseVendorCredit):
    credit: int
    fromDate: int
    overageCredit: int
    addOn: int
    allowNegativeOverageCredit: bool
    def __init__(self,
            credit: int = NotImplemented,
            fromDate: int = NotImplemented,
            overageCredit: int = NotImplemented,
            addOn: int = NotImplemented,
            allowNegativeOverageCredit: bool = NotImplemented): ...

    def getCredit(self) -> int: ...
    def setCredit(self, newCredit: int) -> None: ...
    def getFromDate(self) -> int: ...
    def setFromDate(self, newFromDate: int) -> None: ...
    def getOverageCredit(self) -> int: ...
    def setOverageCredit(self, newOverageCredit: int) -> None: ...
    def getAddOn(self) -> int: ...
    def setAddOn(self, newAddOn: int) -> None: ...
    def getAllowNegativeOverageCredit(self) -> bool: ...
    def setAllowNegativeOverageCredit(self, newAllowNegativeOverageCredit: bool) -> None: ...

class KalturaVendorDubbingCatalogItem(KalturaVendorCatalogItem):
    flavorParamsId: int
    clearAudioFlavorParamsId: int
    targetLanguage: KalturaCatalogItemLanguage
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            flavorParamsId: int = NotImplemented,
            clearAudioFlavorParamsId: int = NotImplemented,
            targetLanguage: KalturaCatalogItemLanguage = NotImplemented): ...

    def getFlavorParamsId(self) -> int: ...
    def setFlavorParamsId(self, newFlavorParamsId: int) -> None: ...
    def getClearAudioFlavorParamsId(self) -> int: ...
    def setClearAudioFlavorParamsId(self, newClearAudioFlavorParamsId: int) -> None: ...
    def getTargetLanguage(self) -> KalturaCatalogItemLanguage: ...
    def setTargetLanguage(self, newTargetLanguage: KalturaCatalogItemLanguage) -> None: ...

class KalturaVendorExtendedAudioDescriptionCatalogItem(KalturaVendorCatalogItem):
    flavorParamsId: int
    clearAudioFlavorParamsId: int
    outputFormat: KalturaVendorCatalogItemOutputFormat
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            flavorParamsId: int = NotImplemented,
            clearAudioFlavorParamsId: int = NotImplemented,
            outputFormat: KalturaVendorCatalogItemOutputFormat = NotImplemented): ...

    def getFlavorParamsId(self) -> int: ...
    def setFlavorParamsId(self, newFlavorParamsId: int) -> None: ...
    def getClearAudioFlavorParamsId(self) -> int: ...
    def setClearAudioFlavorParamsId(self, newClearAudioFlavorParamsId: int) -> None: ...
    def getOutputFormat(self) -> KalturaVendorCatalogItemOutputFormat: ...
    def setOutputFormat(self, newOutputFormat: KalturaVendorCatalogItemOutputFormat) -> None: ...

class KalturaVendorIntelligentTaggingCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented): ...
        pass

class KalturaVendorMetadataEnrichmentCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented): ...
        pass

class KalturaVendorModerationCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented): ...
        pass

class KalturaVendorQuizCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented): ...
        pass

class KalturaVendorSummaryCatalogItem(KalturaVendorCatalogItem):
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented): ...
        pass

class KalturaVendorTaskDataCaptionAsset(KalturaVendorTaskData):
    captionAssetId: str
    def __init__(self,
            entryDuration: int = NotImplemented,
            captionAssetId: str = NotImplemented): ...

    def getCaptionAssetId(self) -> str: ...
    def setCaptionAssetId(self, newCaptionAssetId: str) -> None: ...

class KalturaVendorVideoAnalysisCatalogItem(KalturaVendorCatalogItem):
    videoAnalysisType: KalturaVendorVideoAnalysisType
    maxVideoDuration: int
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            videoAnalysisType: KalturaVendorVideoAnalysisType = NotImplemented,
            maxVideoDuration: int = NotImplemented): ...

    def getVideoAnalysisType(self) -> KalturaVendorVideoAnalysisType: ...
    def setVideoAnalysisType(self, newVideoAnalysisType: KalturaVendorVideoAnalysisType) -> None: ...
    def getMaxVideoDuration(self) -> int: ...
    def setMaxVideoDuration(self, newMaxVideoDuration: int) -> None: ...

class KalturaAlignmentVendorTaskData(KalturaVendorTaskDataCaptionAsset):
    textTranscriptAssetId: str
    jsonTranscriptAssetId: str
    def __init__(self,
            entryDuration: int = NotImplemented,
            captionAssetId: str = NotImplemented,
            textTranscriptAssetId: str = NotImplemented,
            jsonTranscriptAssetId: str = NotImplemented): ...

    def getTextTranscriptAssetId(self) -> str: ...
    def setTextTranscriptAssetId(self, newTextTranscriptAssetId: str) -> None: ...
    def getJsonTranscriptAssetId(self) -> str: ...
    def setJsonTranscriptAssetId(self, newJsonTranscriptAssetId: str) -> None: ...

class KalturaEntryVendorTaskBaseFilter(KalturaRelatedFilter):
    idEqual: int
    idIn: str
    idNotIn: str
    vendorPartnerIdEqual: int
    vendorPartnerIdIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    queueTimeGreaterThanOrEqual: int
    queueTimeLessThanOrEqual: int
    finishTimeGreaterThanOrEqual: int
    finishTimeLessThanOrEqual: int
    entryIdEqual: str
    statusEqual: KalturaEntryVendorTaskStatus
    statusIn: str
    reachProfileIdEqual: int
    reachProfileIdIn: str
    catalogItemIdEqual: int
    catalogItemIdIn: str
    userIdEqual: str
    contextEqual: str
    expectedFinishTimeGreaterThanOrEqual: int
    expectedFinishTimeLessThanOrEqual: int
    entryObjectTypeEqual: KalturaEntryObjectType
    entryObjectTypeIn: str
    entryObjectTypeNotIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            queueTimeGreaterThanOrEqual: int = NotImplemented,
            queueTimeLessThanOrEqual: int = NotImplemented,
            finishTimeGreaterThanOrEqual: int = NotImplemented,
            finishTimeLessThanOrEqual: int = NotImplemented,
            entryIdEqual: str = NotImplemented,
            statusEqual: KalturaEntryVendorTaskStatus = NotImplemented,
            statusIn: str = NotImplemented,
            reachProfileIdEqual: int = NotImplemented,
            reachProfileIdIn: str = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            catalogItemIdIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            contextEqual: str = NotImplemented,
            expectedFinishTimeGreaterThanOrEqual: int = NotImplemented,
            expectedFinishTimeLessThanOrEqual: int = NotImplemented,
            entryObjectTypeEqual: KalturaEntryObjectType = NotImplemented,
            entryObjectTypeIn: str = NotImplemented,
            entryObjectTypeNotIn: str = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getIdNotIn(self) -> str: ...
    def setIdNotIn(self, newIdNotIn: str) -> None: ...
    def getVendorPartnerIdEqual(self) -> int: ...
    def setVendorPartnerIdEqual(self, newVendorPartnerIdEqual: int) -> None: ...
    def getVendorPartnerIdIn(self) -> str: ...
    def setVendorPartnerIdIn(self, newVendorPartnerIdIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...
    def getQueueTimeGreaterThanOrEqual(self) -> int: ...
    def setQueueTimeGreaterThanOrEqual(self, newQueueTimeGreaterThanOrEqual: int) -> None: ...
    def getQueueTimeLessThanOrEqual(self) -> int: ...
    def setQueueTimeLessThanOrEqual(self, newQueueTimeLessThanOrEqual: int) -> None: ...
    def getFinishTimeGreaterThanOrEqual(self) -> int: ...
    def setFinishTimeGreaterThanOrEqual(self, newFinishTimeGreaterThanOrEqual: int) -> None: ...
    def getFinishTimeLessThanOrEqual(self) -> int: ...
    def setFinishTimeLessThanOrEqual(self, newFinishTimeLessThanOrEqual: int) -> None: ...
    def getEntryIdEqual(self) -> str: ...
    def setEntryIdEqual(self, newEntryIdEqual: str) -> None: ...
    def getStatusEqual(self) -> KalturaEntryVendorTaskStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaEntryVendorTaskStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getReachProfileIdEqual(self) -> int: ...
    def setReachProfileIdEqual(self, newReachProfileIdEqual: int) -> None: ...
    def getReachProfileIdIn(self) -> str: ...
    def setReachProfileIdIn(self, newReachProfileIdIn: str) -> None: ...
    def getCatalogItemIdEqual(self) -> int: ...
    def setCatalogItemIdEqual(self, newCatalogItemIdEqual: int) -> None: ...
    def getCatalogItemIdIn(self) -> str: ...
    def setCatalogItemIdIn(self, newCatalogItemIdIn: str) -> None: ...
    def getUserIdEqual(self) -> str: ...
    def setUserIdEqual(self, newUserIdEqual: str) -> None: ...
    def getContextEqual(self) -> str: ...
    def setContextEqual(self, newContextEqual: str) -> None: ...
    def getExpectedFinishTimeGreaterThanOrEqual(self) -> int: ...
    def setExpectedFinishTimeGreaterThanOrEqual(self, newExpectedFinishTimeGreaterThanOrEqual: int) -> None: ...
    def getExpectedFinishTimeLessThanOrEqual(self) -> int: ...
    def setExpectedFinishTimeLessThanOrEqual(self, newExpectedFinishTimeLessThanOrEqual: int) -> None: ...
    def getEntryObjectTypeEqual(self) -> KalturaEntryObjectType: ...
    def setEntryObjectTypeEqual(self, newEntryObjectTypeEqual: KalturaEntryObjectType) -> None: ...
    def getEntryObjectTypeIn(self) -> str: ...
    def setEntryObjectTypeIn(self, newEntryObjectTypeIn: str) -> None: ...
    def getEntryObjectTypeNotIn(self) -> str: ...
    def setEntryObjectTypeNotIn(self, newEntryObjectTypeNotIn: str) -> None: ...

class KalturaEntryVendorTaskFilter(KalturaEntryVendorTaskBaseFilter):
    freeText: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            queueTimeGreaterThanOrEqual: int = NotImplemented,
            queueTimeLessThanOrEqual: int = NotImplemented,
            finishTimeGreaterThanOrEqual: int = NotImplemented,
            finishTimeLessThanOrEqual: int = NotImplemented,
            entryIdEqual: str = NotImplemented,
            statusEqual: KalturaEntryVendorTaskStatus = NotImplemented,
            statusIn: str = NotImplemented,
            reachProfileIdEqual: int = NotImplemented,
            reachProfileIdIn: str = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            catalogItemIdIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            contextEqual: str = NotImplemented,
            expectedFinishTimeGreaterThanOrEqual: int = NotImplemented,
            expectedFinishTimeLessThanOrEqual: int = NotImplemented,
            entryObjectTypeEqual: KalturaEntryObjectType = NotImplemented,
            entryObjectTypeIn: str = NotImplemented,
            entryObjectTypeNotIn: str = NotImplemented,
            freeText: str = NotImplemented): ...

    def getFreeText(self) -> str: ...
    def setFreeText(self, newFreeText: str) -> None: ...

class KalturaEntryVendorTaskCsvJobData(KalturaExportCsvJobData):
    filter: KalturaEntryVendorTaskFilter
    def __init__(self,
            userName: str = NotImplemented,
            userMail: str = NotImplemented,
            outputPath: str = NotImplemented,
            sharedOutputPath: str = NotImplemented,
            filter: KalturaEntryVendorTaskFilter = NotImplemented): ...

    def getFilter(self) -> KalturaEntryVendorTaskFilter: ...
    def setFilter(self, newFilter: KalturaEntryVendorTaskFilter) -> None: ...

class KalturaReachProfileBaseFilter(KalturaRelatedFilter):
    idEqual: int
    idIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    statusEqual: KalturaReachProfileStatus
    statusIn: str
    profileTypeEqual: KalturaReachProfileType
    profileTypeIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaReachProfileStatus = NotImplemented,
            statusIn: str = NotImplemented,
            profileTypeEqual: KalturaReachProfileType = NotImplemented,
            profileTypeIn: str = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...
    def getStatusEqual(self) -> KalturaReachProfileStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaReachProfileStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getProfileTypeEqual(self) -> KalturaReachProfileType: ...
    def setProfileTypeEqual(self, newProfileTypeEqual: KalturaReachProfileType) -> None: ...
    def getProfileTypeIn(self) -> str: ...
    def setProfileTypeIn(self, newProfileTypeIn: str) -> None: ...

class KalturaReachReportInputFilter(KalturaReportInputFilter):
    serviceType: KalturaVendorServiceType
    serviceFeature: KalturaVendorServiceFeature
    turnAroundTime: KalturaVendorServiceTurnAroundTime
    def __init__(self,
            fromDate: int = NotImplemented,
            toDate: int = NotImplemented,
            fromDay: str = NotImplemented,
            toDay: str = NotImplemented,
            keywords: str = NotImplemented,
            searchInTags: bool = NotImplemented,
            searchInAdminTags: bool = NotImplemented,
            categories: str = NotImplemented,
            categoriesIdsIn: str = NotImplemented,
            customVar1In: str = NotImplemented,
            customVar2In: str = NotImplemented,
            customVar3In: str = NotImplemented,
            deviceIn: str = NotImplemented,
            countryIn: str = NotImplemented,
            regionIn: str = NotImplemented,
            citiesIn: str = NotImplemented,
            operatingSystemFamilyIn: str = NotImplemented,
            operatingSystemIn: str = NotImplemented,
            browserFamilyIn: str = NotImplemented,
            browserIn: str = NotImplemented,
            timeZoneOffset: int = NotImplemented,
            interval: KalturaReportInterval = NotImplemented,
            mediaTypeIn: str = NotImplemented,
            sourceTypeIn: str = NotImplemented,
            ownerIdsIn: str = NotImplemented,
            entryOperator: KalturaESearchEntryOperator = NotImplemented,
            entryCreatedAtGreaterThanOrEqual: int = NotImplemented,
            entryCreatedAtLessThanOrEqual: int = NotImplemented,
            entryIdIn: str = NotImplemented,
            playbackTypeIn: str = NotImplemented,
            playbackContextIdsIn: str = NotImplemented,
            rootEntryIdIn: str = NotImplemented,
            errorCodeIn: str = NotImplemented,
            playerVersionIn: str = NotImplemented,
            ispIn: str = NotImplemented,
            applicationVersionIn: str = NotImplemented,
            nodeIdsIn: str = NotImplemented,
            categoriesAncestorIdIn: str = NotImplemented,
            hotspotIdIn: str = NotImplemented,
            crmIdIn: str = NotImplemented,
            playlistIdIn: str = NotImplemented,
            domainIn: str = NotImplemented,
            canonicalUrlIn: str = NotImplemented,
            virtualEventIdIn: str = NotImplemented,
            originIn: str = NotImplemented,
            uiConfIdIn: str = NotImplemented,
            cuePointIdIn: str = NotImplemented,
            contextIdIn: str = NotImplemented,
            roleIn: str = NotImplemented,
            industryIn: str = NotImplemented,
            playbackModeIn: str = NotImplemented,
            companyIn: str = NotImplemented,
            eventSessionContextIdIn: str = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented): ...

    def getServiceType(self) -> KalturaVendorServiceType: ...
    def setServiceType(self, newServiceType: KalturaVendorServiceType) -> None: ...
    def getServiceFeature(self) -> KalturaVendorServiceFeature: ...
    def setServiceFeature(self, newServiceFeature: KalturaVendorServiceFeature) -> None: ...
    def getTurnAroundTime(self) -> KalturaVendorServiceTurnAroundTime: ...
    def setTurnAroundTime(self, newTurnAroundTime: KalturaVendorServiceTurnAroundTime) -> None: ...

class KalturaTimeRangeVendorCredit(KalturaVendorCredit):
    toDate: int
    def __init__(self,
            credit: int = NotImplemented,
            fromDate: int = NotImplemented,
            overageCredit: int = NotImplemented,
            addOn: int = NotImplemented,
            allowNegativeOverageCredit: bool = NotImplemented,
            toDate: int = NotImplemented): ...

    def getToDate(self) -> int: ...
    def setToDate(self, newToDate: int) -> None: ...

class KalturaTranslationVendorTaskData(KalturaVendorTaskDataCaptionAsset):
    def __init__(self,
            entryDuration: int = NotImplemented,
            captionAssetId: str = NotImplemented): ...
        pass

class KalturaVendorCatalogItemBaseFilter(KalturaRelatedFilter):
    idEqual: int
    idIn: str
    idNotIn: str
    vendorPartnerIdEqual: int
    vendorPartnerIdIn: str
    createdAtGreaterThanOrEqual: int
    createdAtLessThanOrEqual: int
    updatedAtGreaterThanOrEqual: int
    updatedAtLessThanOrEqual: int
    statusEqual: KalturaVendorCatalogItemStatus
    statusIn: str
    serviceTypeEqual: KalturaVendorServiceType
    serviceTypeIn: str
    serviceFeatureEqual: KalturaVendorServiceFeature
    serviceFeatureIn: str
    turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime
    turnAroundTimeIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented): ...

    def getIdEqual(self) -> int: ...
    def setIdEqual(self, newIdEqual: int) -> None: ...
    def getIdIn(self) -> str: ...
    def setIdIn(self, newIdIn: str) -> None: ...
    def getIdNotIn(self) -> str: ...
    def setIdNotIn(self, newIdNotIn: str) -> None: ...
    def getVendorPartnerIdEqual(self) -> int: ...
    def setVendorPartnerIdEqual(self, newVendorPartnerIdEqual: int) -> None: ...
    def getVendorPartnerIdIn(self) -> str: ...
    def setVendorPartnerIdIn(self, newVendorPartnerIdIn: str) -> None: ...
    def getCreatedAtGreaterThanOrEqual(self) -> int: ...
    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual: int) -> None: ...
    def getCreatedAtLessThanOrEqual(self) -> int: ...
    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual: int) -> None: ...
    def getUpdatedAtGreaterThanOrEqual(self) -> int: ...
    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual: int) -> None: ...
    def getUpdatedAtLessThanOrEqual(self) -> int: ...
    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual: int) -> None: ...
    def getStatusEqual(self) -> KalturaVendorCatalogItemStatus: ...
    def setStatusEqual(self, newStatusEqual: KalturaVendorCatalogItemStatus) -> None: ...
    def getStatusIn(self) -> str: ...
    def setStatusIn(self, newStatusIn: str) -> None: ...
    def getServiceTypeEqual(self) -> KalturaVendorServiceType: ...
    def setServiceTypeEqual(self, newServiceTypeEqual: KalturaVendorServiceType) -> None: ...
    def getServiceTypeIn(self) -> str: ...
    def setServiceTypeIn(self, newServiceTypeIn: str) -> None: ...
    def getServiceFeatureEqual(self) -> KalturaVendorServiceFeature: ...
    def setServiceFeatureEqual(self, newServiceFeatureEqual: KalturaVendorServiceFeature) -> None: ...
    def getServiceFeatureIn(self) -> str: ...
    def setServiceFeatureIn(self, newServiceFeatureIn: str) -> None: ...
    def getTurnAroundTimeEqual(self) -> KalturaVendorServiceTurnAroundTime: ...
    def setTurnAroundTimeEqual(self, newTurnAroundTimeEqual: KalturaVendorServiceTurnAroundTime) -> None: ...
    def getTurnAroundTimeIn(self) -> str: ...
    def setTurnAroundTimeIn(self, newTurnAroundTimeIn: str) -> None: ...

class KalturaVendorLiveCatalogItem(KalturaVendorCaptionsCatalogItem):
    minimalRefundTime: int
    minimalOrderTime: int
    durationLimit: int
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            outputFormat: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            enableSpeakerId: KalturaNullableBoolean = NotImplemented,
            fixedPriceAddons: int = NotImplemented,
            minimalRefundTime: int = NotImplemented,
            minimalOrderTime: int = NotImplemented,
            durationLimit: int = NotImplemented): ...

    def getMinimalRefundTime(self) -> int: ...
    def setMinimalRefundTime(self, newMinimalRefundTime: int) -> None: ...
    def getMinimalOrderTime(self) -> int: ...
    def setMinimalOrderTime(self, newMinimalOrderTime: int) -> None: ...
    def getDurationLimit(self) -> int: ...
    def setDurationLimit(self, newDurationLimit: int) -> None: ...

class KalturaVendorTranslationCatalogItem(KalturaVendorCaptionsCatalogItem):
    targetLanguage: KalturaCatalogItemLanguage
    requireSource: bool
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            outputFormat: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            enableSpeakerId: KalturaNullableBoolean = NotImplemented,
            fixedPriceAddons: int = NotImplemented,
            targetLanguage: KalturaCatalogItemLanguage = NotImplemented,
            requireSource: bool = NotImplemented): ...

    def getTargetLanguage(self) -> KalturaCatalogItemLanguage: ...
    def setTargetLanguage(self, newTargetLanguage: KalturaCatalogItemLanguage) -> None: ...
    def getRequireSource(self) -> bool: ...
    def setRequireSource(self, newRequireSource: bool) -> None: ...

class KalturaReachProfileFilter(KalturaReachProfileBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaReachProfileStatus = NotImplemented,
            statusIn: str = NotImplemented,
            profileTypeEqual: KalturaReachProfileType = NotImplemented,
            profileTypeIn: str = NotImplemented): ...
        pass

class KalturaReoccurringVendorCredit(KalturaTimeRangeVendorCredit):
    frequency: KalturaVendorCreditRecurrenceFrequency
    def __init__(self,
            credit: int = NotImplemented,
            fromDate: int = NotImplemented,
            overageCredit: int = NotImplemented,
            addOn: int = NotImplemented,
            allowNegativeOverageCredit: bool = NotImplemented,
            toDate: int = NotImplemented,
            frequency: KalturaVendorCreditRecurrenceFrequency = NotImplemented): ...

    def getFrequency(self) -> KalturaVendorCreditRecurrenceFrequency: ...
    def setFrequency(self, newFrequency: KalturaVendorCreditRecurrenceFrequency) -> None: ...

class KalturaVendorCatalogItemFilter(KalturaVendorCatalogItemBaseFilter):
    partnerIdEqual: int
    catalogItemIdEqual: int
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented): ...

    def getPartnerIdEqual(self) -> int: ...
    def setPartnerIdEqual(self, newPartnerIdEqual: int) -> None: ...
    def getCatalogItemIdEqual(self) -> int: ...
    def setCatalogItemIdEqual(self, newCatalogItemIdEqual: int) -> None: ...

class KalturaVendorLiveCaptionCatalogItem(KalturaVendorLiveCatalogItem):
    startTimeBuffer: int
    endTimeBuffer: int
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            outputFormat: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            enableSpeakerId: KalturaNullableBoolean = NotImplemented,
            fixedPriceAddons: int = NotImplemented,
            minimalRefundTime: int = NotImplemented,
            minimalOrderTime: int = NotImplemented,
            durationLimit: int = NotImplemented,
            startTimeBuffer: int = NotImplemented,
            endTimeBuffer: int = NotImplemented): ...

    def getStartTimeBuffer(self) -> int: ...
    def setStartTimeBuffer(self, newStartTimeBuffer: int) -> None: ...
    def getEndTimeBuffer(self) -> int: ...
    def setEndTimeBuffer(self, newEndTimeBuffer: int) -> None: ...

class KalturaVendorLiveTranslationCatalogItem(KalturaVendorLiveCatalogItem):
    targetLanguage: KalturaCatalogItemLanguage
    def __init__(self,
            id: int = NotImplemented,
            vendorPartnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            status: KalturaVendorCatalogItemStatus = NotImplemented,
            serviceType: KalturaVendorServiceType = NotImplemented,
            serviceFeature: KalturaVendorServiceFeature = NotImplemented,
            turnAroundTime: KalturaVendorServiceTurnAroundTime = NotImplemented,
            pricing: KalturaVendorCatalogItemPricing = NotImplemented,
            engineType: KalturaReachVendorEngineType = NotImplemented,
            sourceLanguage: KalturaCatalogItemLanguage = NotImplemented,
            allowResubmission: bool = NotImplemented,
            requiresOverages: bool = NotImplemented,
            vendorData: str = NotImplemented,
            stage: KalturaVendorCatalogItemStage = NotImplemented,
            lastBulkUpdateId: int = NotImplemented,
            contract: str = NotImplemented,
            createdBy: str = NotImplemented,
            notes: str = NotImplemented,
            partnerId: int = NotImplemented,
            defaultReachProfileId: int = NotImplemented,
            adminTagsToExclude: str = NotImplemented,
            outputFormat: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            enableSpeakerId: KalturaNullableBoolean = NotImplemented,
            fixedPriceAddons: int = NotImplemented,
            minimalRefundTime: int = NotImplemented,
            minimalOrderTime: int = NotImplemented,
            durationLimit: int = NotImplemented,
            targetLanguage: KalturaCatalogItemLanguage = NotImplemented): ...

    def getTargetLanguage(self) -> KalturaCatalogItemLanguage: ...
    def setTargetLanguage(self, newTargetLanguage: KalturaCatalogItemLanguage) -> None: ...

class KalturaVendorCaptionsCatalogItemBaseFilter(KalturaVendorCatalogItemFilter):
    sourceLanguageEqual: KalturaCatalogItemLanguage
    sourceLanguageIn: str
    outputFormatEqual: KalturaVendorCatalogItemOutputFormat
    outputFormatIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented): ...

    def getSourceLanguageEqual(self) -> KalturaCatalogItemLanguage: ...
    def setSourceLanguageEqual(self, newSourceLanguageEqual: KalturaCatalogItemLanguage) -> None: ...
    def getSourceLanguageIn(self) -> str: ...
    def setSourceLanguageIn(self, newSourceLanguageIn: str) -> None: ...
    def getOutputFormatEqual(self) -> KalturaVendorCatalogItemOutputFormat: ...
    def setOutputFormatEqual(self, newOutputFormatEqual: KalturaVendorCatalogItemOutputFormat) -> None: ...
    def getOutputFormatIn(self) -> str: ...
    def setOutputFormatIn(self, newOutputFormatIn: str) -> None: ...

class KalturaVendorClipsCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented): ...
        pass

class KalturaVendorDubbingCatalogItemBaseFilter(KalturaVendorCatalogItemFilter):
    targetLanguageEqual: KalturaCatalogItemLanguage
    targetLanguageIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            targetLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            targetLanguageIn: str = NotImplemented): ...

    def getTargetLanguageEqual(self) -> KalturaCatalogItemLanguage: ...
    def setTargetLanguageEqual(self, newTargetLanguageEqual: KalturaCatalogItemLanguage) -> None: ...
    def getTargetLanguageIn(self) -> str: ...
    def setTargetLanguageIn(self, newTargetLanguageIn: str) -> None: ...

class KalturaVendorIntelligentTaggingCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented): ...
        pass

class KalturaVendorMetadataEnrichmentCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented): ...
        pass

class KalturaVendorModerationCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented): ...
        pass

class KalturaVendorQuizCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented): ...
        pass

class KalturaVendorSummaryCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented): ...
        pass

class KalturaVendorVideoAnalysisCatalogItemFilter(KalturaVendorCatalogItemFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented): ...
        pass

class KalturaVendorAlignmentCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented): ...
        pass

class KalturaVendorAudioDescriptionCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented): ...
        pass

class KalturaVendorCaptionsCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented): ...
        pass

class KalturaVendorChapteringCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented): ...
        pass

class KalturaVendorDubbingCatalogItemFilter(KalturaVendorDubbingCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            targetLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            targetLanguageIn: str = NotImplemented): ...
        pass

class KalturaVendorExtendedAudioDescriptionCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented): ...
        pass

class KalturaVendorLiveCaptionCatalogItemFilter(KalturaVendorCaptionsCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented): ...
        pass

class KalturaVendorTranslationCatalogItemBaseFilter(KalturaVendorCaptionsCatalogItemFilter):
    targetLanguageEqual: KalturaCatalogItemLanguage
    targetLanguageIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented,
            targetLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            targetLanguageIn: str = NotImplemented): ...

    def getTargetLanguageEqual(self) -> KalturaCatalogItemLanguage: ...
    def setTargetLanguageEqual(self, newTargetLanguageEqual: KalturaCatalogItemLanguage) -> None: ...
    def getTargetLanguageIn(self) -> str: ...
    def setTargetLanguageIn(self, newTargetLanguageIn: str) -> None: ...

class KalturaVendorLiveTranslationCatalogItemFilter(KalturaVendorTranslationCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented,
            targetLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            targetLanguageIn: str = NotImplemented): ...
        pass

class KalturaVendorTranslationCatalogItemFilter(KalturaVendorTranslationCatalogItemBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            vendorPartnerIdEqual: int = NotImplemented,
            vendorPartnerIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            statusEqual: KalturaVendorCatalogItemStatus = NotImplemented,
            statusIn: str = NotImplemented,
            serviceTypeEqual: KalturaVendorServiceType = NotImplemented,
            serviceTypeIn: str = NotImplemented,
            serviceFeatureEqual: KalturaVendorServiceFeature = NotImplemented,
            serviceFeatureIn: str = NotImplemented,
            turnAroundTimeEqual: KalturaVendorServiceTurnAroundTime = NotImplemented,
            turnAroundTimeIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            catalogItemIdEqual: int = NotImplemented,
            sourceLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            sourceLanguageIn: str = NotImplemented,
            outputFormatEqual: KalturaVendorCatalogItemOutputFormat = NotImplemented,
            outputFormatIn: str = NotImplemented,
            targetLanguageEqual: KalturaCatalogItemLanguage = NotImplemented,
            targetLanguageIn: str = NotImplemented): ...
        pass

class KalturaVendorCatalogItemService(KalturaServiceBase):
    def add(self, vendorCatalogItem: KalturaVendorCatalogItem) -> KalturaVendorCatalogItem: ...
    def addFromBulkUpload(self, fileData: IO[Any], bulkUploadData: KalturaBulkUploadJobData = NotImplemented, bulkUploadVendorCatalogItemData: KalturaBulkUploadVendorCatalogItemData = NotImplemented) -> KalturaBulkUpload: ...
    def delete(self, id: int) -> None: ...
    def get(self, id: int) -> KalturaVendorCatalogItem: ...
    def getServeUrl(self, vendorPartnerId: int = NotImplemented) -> str: ...
    def list(self, filter: KalturaVendorCatalogItemFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaVendorCatalogItemListResponse: ...
    def serve(self, vendorPartnerId: int = NotImplemented) -> IO[Any]: ...
    def update(self, id: int, vendorCatalogItem: KalturaVendorCatalogItem) -> KalturaVendorCatalogItem: ...
    def updateStatus(self, id: int, status: int) -> KalturaVendorCatalogItem: ...

class KalturaReachProfileService(KalturaServiceBase):
    def add(self, reachProfile: KalturaReachProfile) -> KalturaReachProfile: ...
    def delete(self, id: int) -> None: ...
    def get(self, id: int) -> KalturaReachProfile: ...
    def list(self, filter: KalturaReachProfileFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaReachProfileListResponse: ...
    def syncCredit(self, reachProfileId: int) -> KalturaReachProfile: ...
    def update(self, id: int, reachProfile: KalturaReachProfile) -> KalturaReachProfile: ...
    def updateStatus(self, id: int, status: int) -> KalturaReachProfile: ...

class KalturaEntryVendorTaskService(KalturaServiceBase):
    def abort(self, id: int, abortReason: str = NotImplemented) -> KalturaEntryVendorTask: ...
    def add(self, entryVendorTask: KalturaEntryVendorTask) -> KalturaEntryVendorTask: ...
    def approve(self, id: int) -> KalturaEntryVendorTask: ...
    def exportToCsv(self, filter: KalturaEntryVendorTaskFilter) -> str: ...
    def extendAccessKey(self, id: int) -> KalturaEntryVendorTask: ...
    def get(self, id: int) -> KalturaEntryVendorTask: ...
    def getJobs(self, filter: KalturaEntryVendorTaskFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaEntryVendorTaskListResponse: ...
    def getServeUrl(self, filterType: str = NotImplemented, filterInput: int = NotImplemented, status: int = NotImplemented, dueDate: str = NotImplemented) -> str: ...
    def list(self, filter: KalturaEntryVendorTaskFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaEntryVendorTaskListResponse: ...
    def reject(self, id: int, rejectReason: str = NotImplemented) -> KalturaEntryVendorTask: ...
    def serve(self, vendorPartnerId: int = NotImplemented, partnerId: int = NotImplemented, status: int = NotImplemented, dueDate: str = NotImplemented) -> IO[Any]: ...
    def serveCsv(self, id: str) -> str: ...
    def update(self, id: int, entryVendorTask: KalturaEntryVendorTask) -> KalturaEntryVendorTask: ...
    def updateJob(self, id: int, entryVendorTask: KalturaEntryVendorTask) -> KalturaEntryVendorTask: ...

class KalturaPartnerCatalogItemService(KalturaServiceBase):
    def add(self, id: int, defaultReachProfileId: int = NotImplemented) -> KalturaVendorCatalogItem: ...
    def delete(self, id: int) -> None: ...

class KalturaReachClientPluginServicesProxy:
    vendorCatalogItem: KalturaVendorCatalogItemService
    reachProfile: KalturaReachProfileService
    entryVendorTask: KalturaEntryVendorTaskService
    PartnerCatalogItem: KalturaPartnerCatalogItemService