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
from .Metadata import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaIntegrationProviderType(object):
    CIELO24 = "cielo24.Cielo24"
    DEXTER = "dexterIntegration.Dexter"
    EXAMPLE = "exampleIntegration.Example"
    VOICEBASE = "voicebase.Voicebase"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaIntegrationTriggerType(object):
    BPM_EVENT_NOTIFICATION = "bpmEventNotificationIntegration.BpmEventNotification"
    MANUAL = "1"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaIntegrationJobProviderData(KalturaObjectBase):
    def __init__(self): ...
        pass

class KalturaIntegrationJobTriggerData(KalturaObjectBase):
    def __init__(self): ...
        pass

class KalturaIntegrationJobData(KalturaJobData):
    callbackNotificationUrl: str
    providerType: KalturaIntegrationProviderType
    providerData: KalturaIntegrationJobProviderData
    triggerType: KalturaIntegrationTriggerType
    triggerData: KalturaIntegrationJobTriggerData
    def __init__(self,
            callbackNotificationUrl: str = NotImplemented,
            providerType: KalturaIntegrationProviderType = NotImplemented,
            providerData: KalturaIntegrationJobProviderData = NotImplemented,
            triggerType: KalturaIntegrationTriggerType = NotImplemented,
            triggerData: KalturaIntegrationJobTriggerData = NotImplemented): ...

    def getCallbackNotificationUrl(self) -> str: ...
    def getProviderType(self) -> KalturaIntegrationProviderType: ...
    def setProviderType(self, newProviderType: KalturaIntegrationProviderType) -> None: ...
    def getProviderData(self) -> KalturaIntegrationJobProviderData: ...
    def setProviderData(self, newProviderData: KalturaIntegrationJobProviderData) -> None: ...
    def getTriggerType(self) -> KalturaIntegrationTriggerType: ...
    def setTriggerType(self, newTriggerType: KalturaIntegrationTriggerType) -> None: ...
    def getTriggerData(self) -> KalturaIntegrationJobTriggerData: ...
    def setTriggerData(self, newTriggerData: KalturaIntegrationJobTriggerData) -> None: ...

class KalturaIntegrationService(KalturaServiceBase):
    def dispatch(self, data: KalturaIntegrationJobData, objectType: str, objectId: str) -> int: ...
    def notify(self, id: int) -> None: ...

class KalturaIntegrationClientPluginServicesProxy:
    integration: KalturaIntegrationService