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
from .Drm import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaPlayReadyAnalogVideoOPL(object):
    MIN_100 = 100
    MIN_150 = 150
    MIN_200 = 200

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaPlayReadyCompressedDigitalVideoOPL(object):
    MIN_400 = 400
    MIN_500 = 500

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaPlayReadyDigitalAudioOPL(object):
    MIN_100 = 100
    MIN_150 = 150
    MIN_200 = 200
    MIN_250 = 250
    MIN_300 = 300

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaPlayReadyLicenseRemovalPolicy(object):
    FIXED_FROM_EXPIRATION = 1
    ENTRY_SCHEDULING_END = 2
    NONE = 3

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaPlayReadyMinimumLicenseSecurityLevel(object):
    NON_COMMERCIAL_QUALITY = 150
    COMMERCIAL_QUALITY = 2000

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaPlayReadyUncompressedDigitalVideoOPL(object):
    MIN_100 = 100
    MIN_250 = 250
    MIN_270 = 270
    MIN_300 = 300

    def __init__(self, value: int): ...

    def getValue(self) -> int: ...

class KalturaPlayReadyAnalogVideoOPId(object):
    EXPLICIT_ANALOG_TV = "2098DE8D-7DDD-4BAB-96C6-32EBB6FABEA3"
    BEST_EFFORT_EXPLICIT_ANALOG_TV = "225CD36F-F132-49EF-BA8C-C91EA28E4369"
    IMAGE_CONSTRAINT_VIDEO = "811C5110-46C8-4C6E-8163-C0482A15D47E"
    AGC_AND_COLOR_STRIPE = "C3FD11C6-F8B7-4D20-B008-1DB17D61F2DA"
    IMAGE_CONSTRAINT_MONITOR = "D783A191-E083-4BAF-B2DA-E69F910B3772"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPlayReadyCopyEnablerType(object):
    CSS = "3CAF2814-A7AB-467C-B4DF-54ACC56C66DC"
    PRINTER = "3CF2E054-F4D5-46cd-85A6-FCD152AD5FBE"
    DEVICE = "6848955D-516B-4EB0-90E8-8F6D5A77B85F"
    CLIPBOARD = "6E76C588-C3A9-47ea-A875-546D5209FF38"
    SDC = "79F78A0D-0B69-401e-8A90-8BEF30BCE192"
    SDC_PREVIEW = "81BD9AD4-A720-4ea1-B510-5D4E6FFB6A4D"
    AACS = "C3CF56E0-7FF2-4491-809F-53E21D3ABF07"
    HELIX = "CCB0B4E3-8B46-409e-A998-82556E3F5AF4"
    CPRM = "CDD801AD-A577-48DB-950E-46D5F1592FAE"
    PC = "CE480EDE-516B-40B3-90E1-D6CFC47630C5"
    SDC_LIMITED = "E6785609-64CC-4bfa-B82D-6B619733B746"
    ORANGE_BOOK_CD = "EC930B7D-1F2D-4682-A38B-8AB977721D0D"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPlayReadyDigitalAudioOPId(object):
    SCMS = "6D5CFA59-C250-4426-930E-FAC72C8FCFA6"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPlayReadyPlayEnablerType(object):
    HELIX = "002F9772-38A0-43E5-9F79-0F6361DCC62A"
    HDCP_WIVU = "1B4542E3-B5CF-4C99-B3BA-829AF46C92F8"
    AIRPLAY = "5ABF0F0D-DC29-4B82-9982-FD8E57525BFC"
    UNKNOWN = "786627D8-C2A6-44BE-8F88-08AE255B01A"
    HDCP_MIRACAST = "A340C256-0941-4D4C-AD1D-0B6735C0CB24"
    UNKNOWN_520 = "B621D91F-EDCC-4035-8D4B-DC71760D43E9"
    DTCP = "D685030B-0F4F-43A6-BBAD-356F1EA0049A"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPlayReadyPolicyOrderBy(object):

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPlayReadyProfileOrderBy(object):
    ID_ASC = "+id"
    NAME_ASC = "+name"
    ID_DESC = "-id"
    NAME_DESC = "-name"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaPlayReadyAnalogVideoOPIdHolder(KalturaObjectBase):
    type: KalturaPlayReadyAnalogVideoOPId
    def __init__(self,
            type: KalturaPlayReadyAnalogVideoOPId = NotImplemented): ...

    def getType(self) -> KalturaPlayReadyAnalogVideoOPId: ...
    def setType(self, newType: KalturaPlayReadyAnalogVideoOPId) -> None: ...

class KalturaPlayReadyContentKey(KalturaObjectBase):
    keyId: str
    contentKey: str
    def __init__(self,
            keyId: str = NotImplemented,
            contentKey: str = NotImplemented): ...

    def getKeyId(self) -> str: ...
    def setKeyId(self, newKeyId: str) -> None: ...
    def getContentKey(self) -> str: ...
    def setContentKey(self, newContentKey: str) -> None: ...

class KalturaPlayReadyCopyEnablerHolder(KalturaObjectBase):
    type: KalturaPlayReadyCopyEnablerType
    def __init__(self,
            type: KalturaPlayReadyCopyEnablerType = NotImplemented): ...

    def getType(self) -> KalturaPlayReadyCopyEnablerType: ...
    def setType(self, newType: KalturaPlayReadyCopyEnablerType) -> None: ...

class KalturaPlayReadyDigitalAudioOPIdHolder(KalturaObjectBase):
    type: KalturaPlayReadyDigitalAudioOPId
    def __init__(self,
            type: KalturaPlayReadyDigitalAudioOPId = NotImplemented): ...

    def getType(self) -> KalturaPlayReadyDigitalAudioOPId: ...
    def setType(self, newType: KalturaPlayReadyDigitalAudioOPId) -> None: ...

class KalturaPlayReadyRight(KalturaObjectBase):
    def __init__(self): ...
        pass

class KalturaPlayReadyPolicy(KalturaDrmPolicy):
    gracePeriod: int
    licenseRemovalPolicy: KalturaPlayReadyLicenseRemovalPolicy
    licenseRemovalDuration: int
    minSecurityLevel: KalturaPlayReadyMinimumLicenseSecurityLevel
    rights: List[KalturaPlayReadyRight]
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            systemName: str = NotImplemented,
            description: str = NotImplemented,
            provider: KalturaDrmProviderType = NotImplemented,
            status: KalturaDrmPolicyStatus = NotImplemented,
            scenario: KalturaDrmLicenseScenario = NotImplemented,
            licenseType: KalturaDrmLicenseType = NotImplemented,
            licenseExpirationPolicy: KalturaDrmLicenseExpirationPolicy = NotImplemented,
            duration: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            licenseParams: List[KalturaKeyValue] = NotImplemented,
            gracePeriod: int = NotImplemented,
            licenseRemovalPolicy: KalturaPlayReadyLicenseRemovalPolicy = NotImplemented,
            licenseRemovalDuration: int = NotImplemented,
            minSecurityLevel: KalturaPlayReadyMinimumLicenseSecurityLevel = NotImplemented,
            rights: List[KalturaPlayReadyRight] = NotImplemented): ...

    def getGracePeriod(self) -> int: ...
    def setGracePeriod(self, newGracePeriod: int) -> None: ...
    def getLicenseRemovalPolicy(self) -> KalturaPlayReadyLicenseRemovalPolicy: ...
    def setLicenseRemovalPolicy(self, newLicenseRemovalPolicy: KalturaPlayReadyLicenseRemovalPolicy) -> None: ...
    def getLicenseRemovalDuration(self) -> int: ...
    def setLicenseRemovalDuration(self, newLicenseRemovalDuration: int) -> None: ...
    def getMinSecurityLevel(self) -> KalturaPlayReadyMinimumLicenseSecurityLevel: ...
    def setMinSecurityLevel(self, newMinSecurityLevel: KalturaPlayReadyMinimumLicenseSecurityLevel) -> None: ...
    def getRights(self) -> List[KalturaPlayReadyRight]: ...
    def setRights(self, newRights: List[KalturaPlayReadyRight]) -> None: ...

class KalturaPlayReadyLicenseDetails(KalturaObjectBase):
    policy: KalturaPlayReadyPolicy
    beginDate: int
    expirationDate: int
    removalDate: int
    def __init__(self,
            policy: KalturaPlayReadyPolicy = NotImplemented,
            beginDate: int = NotImplemented,
            expirationDate: int = NotImplemented,
            removalDate: int = NotImplemented): ...

    def getPolicy(self) -> KalturaPlayReadyPolicy: ...
    def setPolicy(self, newPolicy: KalturaPlayReadyPolicy) -> None: ...
    def getBeginDate(self) -> int: ...
    def setBeginDate(self, newBeginDate: int) -> None: ...
    def getExpirationDate(self) -> int: ...
    def setExpirationDate(self, newExpirationDate: int) -> None: ...
    def getRemovalDate(self) -> int: ...
    def setRemovalDate(self, newRemovalDate: int) -> None: ...

class KalturaPlayReadyPlayEnablerHolder(KalturaObjectBase):
    type: KalturaPlayReadyPlayEnablerType
    def __init__(self,
            type: KalturaPlayReadyPlayEnablerType = NotImplemented): ...

    def getType(self) -> KalturaPlayReadyPlayEnablerType: ...
    def setType(self, newType: KalturaPlayReadyPlayEnablerType) -> None: ...

class KalturaPlayReadyCopyRight(KalturaPlayReadyRight):
    copyCount: int
    copyEnablers: List[KalturaPlayReadyCopyEnablerHolder]
    def __init__(self,
            copyCount: int = NotImplemented,
            copyEnablers: List[KalturaPlayReadyCopyEnablerHolder] = NotImplemented): ...

    def getCopyCount(self) -> int: ...
    def setCopyCount(self, newCopyCount: int) -> None: ...
    def getCopyEnablers(self) -> List[KalturaPlayReadyCopyEnablerHolder]: ...
    def setCopyEnablers(self, newCopyEnablers: List[KalturaPlayReadyCopyEnablerHolder]) -> None: ...

class KalturaPlayReadyPlayRight(KalturaPlayReadyRight):
    analogVideoOPL: KalturaPlayReadyAnalogVideoOPL
    analogVideoOutputProtectionList: List[KalturaPlayReadyAnalogVideoOPIdHolder]
    compressedDigitalAudioOPL: KalturaPlayReadyDigitalAudioOPL
    compressedDigitalVideoOPL: KalturaPlayReadyCompressedDigitalVideoOPL
    digitalAudioOutputProtectionList: List[KalturaPlayReadyDigitalAudioOPIdHolder]
    uncompressedDigitalAudioOPL: KalturaPlayReadyDigitalAudioOPL
    uncompressedDigitalVideoOPL: KalturaPlayReadyUncompressedDigitalVideoOPL
    firstPlayExpiration: int
    playEnablers: List[KalturaPlayReadyPlayEnablerHolder]
    def __init__(self,
            analogVideoOPL: KalturaPlayReadyAnalogVideoOPL = NotImplemented,
            analogVideoOutputProtectionList: List[KalturaPlayReadyAnalogVideoOPIdHolder] = NotImplemented,
            compressedDigitalAudioOPL: KalturaPlayReadyDigitalAudioOPL = NotImplemented,
            compressedDigitalVideoOPL: KalturaPlayReadyCompressedDigitalVideoOPL = NotImplemented,
            digitalAudioOutputProtectionList: List[KalturaPlayReadyDigitalAudioOPIdHolder] = NotImplemented,
            uncompressedDigitalAudioOPL: KalturaPlayReadyDigitalAudioOPL = NotImplemented,
            uncompressedDigitalVideoOPL: KalturaPlayReadyUncompressedDigitalVideoOPL = NotImplemented,
            firstPlayExpiration: int = NotImplemented,
            playEnablers: List[KalturaPlayReadyPlayEnablerHolder] = NotImplemented): ...

    def getAnalogVideoOPL(self) -> KalturaPlayReadyAnalogVideoOPL: ...
    def setAnalogVideoOPL(self, newAnalogVideoOPL: KalturaPlayReadyAnalogVideoOPL) -> None: ...
    def getAnalogVideoOutputProtectionList(self) -> List[KalturaPlayReadyAnalogVideoOPIdHolder]: ...
    def setAnalogVideoOutputProtectionList(self, newAnalogVideoOutputProtectionList: List[KalturaPlayReadyAnalogVideoOPIdHolder]) -> None: ...
    def getCompressedDigitalAudioOPL(self) -> KalturaPlayReadyDigitalAudioOPL: ...
    def setCompressedDigitalAudioOPL(self, newCompressedDigitalAudioOPL: KalturaPlayReadyDigitalAudioOPL) -> None: ...
    def getCompressedDigitalVideoOPL(self) -> KalturaPlayReadyCompressedDigitalVideoOPL: ...
    def setCompressedDigitalVideoOPL(self, newCompressedDigitalVideoOPL: KalturaPlayReadyCompressedDigitalVideoOPL) -> None: ...
    def getDigitalAudioOutputProtectionList(self) -> List[KalturaPlayReadyDigitalAudioOPIdHolder]: ...
    def setDigitalAudioOutputProtectionList(self, newDigitalAudioOutputProtectionList: List[KalturaPlayReadyDigitalAudioOPIdHolder]) -> None: ...
    def getUncompressedDigitalAudioOPL(self) -> KalturaPlayReadyDigitalAudioOPL: ...
    def setUncompressedDigitalAudioOPL(self, newUncompressedDigitalAudioOPL: KalturaPlayReadyDigitalAudioOPL) -> None: ...
    def getUncompressedDigitalVideoOPL(self) -> KalturaPlayReadyUncompressedDigitalVideoOPL: ...
    def setUncompressedDigitalVideoOPL(self, newUncompressedDigitalVideoOPL: KalturaPlayReadyUncompressedDigitalVideoOPL) -> None: ...
    def getFirstPlayExpiration(self) -> int: ...
    def setFirstPlayExpiration(self, newFirstPlayExpiration: int) -> None: ...
    def getPlayEnablers(self) -> List[KalturaPlayReadyPlayEnablerHolder]: ...
    def setPlayEnablers(self, newPlayEnablers: List[KalturaPlayReadyPlayEnablerHolder]) -> None: ...

class KalturaPlayReadyProfile(KalturaDrmProfile):
    keySeed: str
    def __init__(self,
            id: int = NotImplemented,
            partnerId: int = NotImplemented,
            name: str = NotImplemented,
            description: str = NotImplemented,
            provider: KalturaDrmProviderType = NotImplemented,
            status: KalturaDrmProfileStatus = NotImplemented,
            licenseServerUrl: str = NotImplemented,
            defaultPolicy: str = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            signingKey: str = NotImplemented,
            keySeed: str = NotImplemented): ...

    def getKeySeed(self) -> str: ...
    def setKeySeed(self, newKeySeed: str) -> None: ...

class KalturaPlayReadyPolicyBaseFilter(KalturaDrmPolicyFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            systemNameLike: str = NotImplemented,
            providerEqual: KalturaDrmProviderType = NotImplemented,
            providerIn: str = NotImplemented,
            statusEqual: KalturaDrmPolicyStatus = NotImplemented,
            statusIn: str = NotImplemented,
            scenarioEqual: KalturaDrmLicenseScenario = NotImplemented,
            scenarioIn: str = NotImplemented): ...
        pass

class KalturaPlayReadyProfileBaseFilter(KalturaDrmProfileFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            providerEqual: KalturaDrmProviderType = NotImplemented,
            providerIn: str = NotImplemented,
            statusEqual: KalturaDrmProfileStatus = NotImplemented,
            statusIn: str = NotImplemented): ...
        pass

class KalturaPlayReadyPolicyFilter(KalturaPlayReadyPolicyBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            systemNameLike: str = NotImplemented,
            providerEqual: KalturaDrmProviderType = NotImplemented,
            providerIn: str = NotImplemented,
            statusEqual: KalturaDrmPolicyStatus = NotImplemented,
            statusIn: str = NotImplemented,
            scenarioEqual: KalturaDrmLicenseScenario = NotImplemented,
            scenarioIn: str = NotImplemented): ...
        pass

class KalturaPlayReadyProfileFilter(KalturaPlayReadyProfileBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            partnerIdEqual: int = NotImplemented,
            partnerIdIn: str = NotImplemented,
            nameLike: str = NotImplemented,
            providerEqual: KalturaDrmProviderType = NotImplemented,
            providerIn: str = NotImplemented,
            statusEqual: KalturaDrmProfileStatus = NotImplemented,
            statusIn: str = NotImplemented): ...
        pass

class KalturaPlayReadyDrmService(KalturaServiceBase):
    def generateKey(self) -> KalturaPlayReadyContentKey: ...
    def getContentKeys(self, keyIds: str) -> List[KalturaPlayReadyContentKey]: ...
    def getEntryContentKey(self, entryId: str, createIfMissing: bool = False) -> KalturaPlayReadyContentKey: ...
    def getLicenseDetails(self, keyId: str, deviceId: str, deviceType: int, entryId: str = NotImplemented, referrer: str = NotImplemented) -> KalturaPlayReadyLicenseDetails: ...

class KalturaPlayReadyClientPluginServicesProxy:
    playReadyDrm: KalturaPlayReadyDrmService