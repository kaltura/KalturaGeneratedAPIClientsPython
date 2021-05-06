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
class KalturaSsoStatus(object):
    DISABLED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaSso(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            applicationType=NotImplemented,
            partnerId=NotImplemented,
            domain=NotImplemented,
            status=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            redirectUrl=NotImplemented,
            data=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var string
        self.applicationType = applicationType

        # @var int
        # @insertonly
        self.partnerId = partnerId

        # @var string
        self.domain = domain

        # @var KalturaSsoStatus
        self.status = status

        # Creation date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.createdAt = createdAt

        # Last update date as Unix timestamp (In seconds)
        # @var int
        # @readonly
        self.updatedAt = updatedAt

        # Redirect URL for a specific application type and (partner id or domain)
        # @var string
        self.redirectUrl = redirectUrl

        # @var string
        self.data = data


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'applicationType': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'domain': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createInt, "KalturaSsoStatus"), 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'redirectUrl': getXmlNodeText, 
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSso.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSso")
        kparams.addStringIfDefined("applicationType", self.applicationType)
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("domain", self.domain)
        kparams.addIntEnumIfDefined("status", self.status)
        kparams.addStringIfDefined("redirectUrl", self.redirectUrl)
        kparams.addStringIfDefined("data", self.data)
        return kparams

    def getId(self):
        return self.id

    def getApplicationType(self):
        return self.applicationType

    def setApplicationType(self, newApplicationType):
        self.applicationType = newApplicationType

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getDomain(self):
        return self.domain

    def setDomain(self, newDomain):
        self.domain = newDomain

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getCreatedAt(self):
        return self.createdAt

    def getUpdatedAt(self):
        return self.updatedAt

    def getRedirectUrl(self):
        return self.redirectUrl

    def setRedirectUrl(self, newRedirectUrl):
        self.redirectUrl = newRedirectUrl

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


# @package Kaltura
# @subpackage Client
class KalturaSsoListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # @var array of KalturaSso
        # @readonly
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSso'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSsoListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSsoListResponse")
        return kparams

    def getObjects(self):
        return self.objects


# @package Kaltura
# @subpackage Client
class KalturaSsoBaseFilter(KalturaRelatedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            applicationTypeEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            domainEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            redirectUrlEqual=NotImplemented):
        KalturaRelatedFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var string
        self.applicationTypeEqual = applicationTypeEqual

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.domainEqual = domainEqual

        # @var KalturaSsoStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var string
        self.redirectUrlEqual = redirectUrlEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'applicationTypeEqual': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'domainEqual': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaSsoStatus"), 
        'statusIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'redirectUrlEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaRelatedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSsoBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedFilter.toParams(self)
        kparams.put("objectType", "KalturaSsoBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("applicationTypeEqual", self.applicationTypeEqual)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("domainEqual", self.domainEqual)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addStringIfDefined("redirectUrlEqual", self.redirectUrlEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getApplicationTypeEqual(self):
        return self.applicationTypeEqual

    def setApplicationTypeEqual(self, newApplicationTypeEqual):
        self.applicationTypeEqual = newApplicationTypeEqual

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getDomainEqual(self):
        return self.domainEqual

    def setDomainEqual(self, newDomainEqual):
        self.domainEqual = newDomainEqual

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getRedirectUrlEqual(self):
        return self.redirectUrlEqual

    def setRedirectUrlEqual(self, newRedirectUrlEqual):
        self.redirectUrlEqual = newRedirectUrlEqual


# @package Kaltura
# @subpackage Client
class KalturaSsoFilter(KalturaSsoBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            applicationTypeEqual=NotImplemented,
            partnerIdEqual=NotImplemented,
            domainEqual=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            redirectUrlEqual=NotImplemented):
        KalturaSsoBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            applicationTypeEqual,
            partnerIdEqual,
            domainEqual,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            redirectUrlEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSsoBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSsoFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSsoBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaSsoFilter")
        return kparams


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaSsoService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, sso):
        """Adds a new sso configuration."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("sso", sso)
        self.client.queueServiceActionCall("sso_sso", "add", "KalturaSso", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaSso')

    def delete(self, ssoId):
        """Delete sso by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("ssoId", ssoId);
        self.client.queueServiceActionCall("sso_sso", "delete", "KalturaSso", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaSso')

    def get(self, ssoId):
        """Retrieves sso object"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("ssoId", ssoId);
        self.client.queueServiceActionCall("sso_sso", "get", "KalturaSso", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaSso')

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Lists sso objects that are associated with an account."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("sso_sso", "list", "KalturaSsoListResponse", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaSsoListResponse')

    def login(self, userId, applicationType, partnerId = NotImplemented):
        """Login with SSO, getting redirect url according to application type and partner Id
        	 or according to application type and domain"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        kparams.addStringIfDefined("applicationType", applicationType)
        kparams.addIntIfDefined("partnerId", partnerId);
        self.client.queueServiceActionCall("sso_sso", "login", "None", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def update(self, ssoId, sso):
        """Update sso by ID"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("ssoId", ssoId);
        kparams.addObjectIfDefined("sso", sso)
        self.client.queueServiceActionCall("sso_sso", "update", "KalturaSso", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, 'KalturaSso')

########## main ##########
class KalturaSsoClientPlugin(KalturaClientPlugin):
    # KalturaSsoClientPlugin
    instance = None

    # @return KalturaSsoClientPlugin
    @staticmethod
    def get():
        if KalturaSsoClientPlugin.instance == None:
            KalturaSsoClientPlugin.instance = KalturaSsoClientPlugin()
        return KalturaSsoClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'sso': KalturaSsoService,
        }

    def getEnums(self):
        return {
            'KalturaSsoStatus': KalturaSsoStatus,
        }

    def getTypes(self):
        return {
            'KalturaSso': KalturaSso,
            'KalturaSsoListResponse': KalturaSsoListResponse,
            'KalturaSsoBaseFilter': KalturaSsoBaseFilter,
            'KalturaSsoFilter': KalturaSsoFilter,
        }

    # @return string
    def getName(self):
        return 'sso'

