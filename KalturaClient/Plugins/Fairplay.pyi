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

class KalturaFairplayDrmProfile(KalturaDrmProfile):
    publicCertificate: str
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
            publicCertificate: str = NotImplemented): ...

    def getPublicCertificate(self) -> str: ...
    def setPublicCertificate(self, newPublicCertificate: str) -> None: ...

class KalturaFairplayEntryContextPluginData(KalturaPluginData):
    publicCertificate: str
    def __init__(self,
            publicCertificate: str = NotImplemented): ...

    def getPublicCertificate(self) -> str: ...
    def setPublicCertificate(self, newPublicCertificate: str) -> None: ...

class KalturaFairplayClientPluginServicesProxy: