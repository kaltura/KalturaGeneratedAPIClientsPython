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
# Copyright (C) 2006-2017  Kaltura Inc.
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

from ..Base import *

API_VERSION = '3.6.287.20330'

########## enums ##########
# @package Kaltura
# @subpackage Client
class KalturaAnnouncementOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAnnouncementRecipientsType(object):
    ALL = "All"
    LOGGEDIN = "LoggedIn"
    GUESTS = "Guests"
    OTHER = "Other"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAnnouncementStatus(object):
    NOTSENT = "NotSent"
    SENDING = "Sending"
    SENT = "Sent"
    ABORTED = "Aborted"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaApiParameterPermissionItemAction(object):
    READ = "READ"
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    USAGE = "USAGE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAppTokenHashType(object):
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SHA512 = "SHA512"
    MD5 = "MD5"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAppTokenStatus(object):
    DELETED = 0
    DISABLED = 1
    ACTIVE = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetCommentOrderBy(object):
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetHistoryOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetOrderBy(object):
    RELEVANCY_DESC = "RELEVANCY_DESC"
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    VIEWS_DESC = "VIEWS_DESC"
    RATINGS_DESC = "RATINGS_DESC"
    VOTES_DESC = "VOTES_DESC"
    START_DATE_DESC = "START_DATE_DESC"
    START_DATE_ASC = "START_DATE_ASC"
    LIKES_DESC = "LIKES_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetReferenceType(object):
    MEDIA = "media"
    EPG_INTERNAL = "epg_internal"
    EPG_EXTERNAL = "epg_external"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetType(object):
    MEDIA = "media"
    RECORDING = "recording"
    EPG = "epg"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBillingAction(object):
    UNKNOWN = "unknown"
    PURCHASE = "purchase"
    RENEW_PAYMENT = "renew_payment"
    RENEW_CANCELED_SUBSCRIPTION = "renew_canceled_subscription"
    CANCEL_SUBSCRIPTION_ORDER = "cancel_subscription_order"
    SUBSCRIPTION_DATE_CHANGED = "subscription_date_changed"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBillingItemsType(object):
    UNKNOWN = "unknown"
    PPV = "ppv"
    SUBSCRIPTION = "subscription"
    PRE_PAID = "pre_paid"
    PRE_PAID_EXPIRED = "pre_paid_expired"
    COLLECTION = "collection"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBookmarkActionType(object):
    HIT = "HIT"
    PLAY = "PLAY"
    STOP = "STOP"
    PAUSE = "PAUSE"
    FIRST_PLAY = "FIRST_PLAY"
    SWOOSH = "SWOOSH"
    FULL_SCREEN = "FULL_SCREEN"
    SEND_TO_FRIEND = "SEND_TO_FRIEND"
    LOAD = "LOAD"
    FULL_SCREEN_EXIT = "FULL_SCREEN_EXIT"
    FINISH = "FINISH"
    ERROR = "ERROR"
    BITRATE_CHANGE = "BITRATE_CHANGE"
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBookmarkOrderBy(object):
    POSITION_ASC = "POSITION_ASC"
    POSITION_DESC = "POSITION_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBundleType(object):
    SUBSCRIPTION = "subscription"
    COLLECTION = "collection"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaChannelEnrichment(object):
    CLIENTLOCATION = "ClientLocation"
    USERID = "UserId"
    HOUSEHOLDID = "HouseholdId"
    DEVICEID = "DeviceId"
    DEVICETYPE = "DeviceType"
    UTCOFFSET = "UTCOffset"
    LANGUAGE = "Language"
    NPVRSUPPORT = "NPVRSupport"
    CATCHUP = "Catchup"
    PARENTAL = "Parental"
    DTTREGION = "DTTRegion"
    ATHOME = "AtHome"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCouponStatus(object):
    VALID = "VALID"
    NOT_EXISTS = "NOT_EXISTS"
    ALREADY_USED = "ALREADY_USED"
    EXPIRED = "EXPIRED"
    INACTIVE = "INACTIVE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaDeviceStatus(object):
    PENDING = "PENDING"
    ACTIVATED = "ACTIVATED"
    NOT_ACTIVATED = "NOT_ACTIVATED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEntitlementOrderBy(object):
    PURCHASE_DATE_ASC = "PURCHASE_DATE_ASC"
    PURCHASE_DATE_DESC = "PURCHASE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEntityReferenceBy(object):
    USER = "user"
    HOUSEHOLD = "household"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaExportDataType(object):
    VOD = "vod"
    EPG = "epg"
    USERS = "users"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaExportTaskOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaExportType(object):
    FULL = "full"
    INCREMENTAL = "incremental"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaFavoriteOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeriesOrderBy(object):
    START_DATE_DESC = "START_DATE_DESC"
    START_DATE_ASC = "START_DATE_ASC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdFrequencyType(object):
    DEVICES = "devices"
    USERS = "users"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentGatewaySelectedBy(object):
    NONE = "none"
    ACCOUNT = "account"
    HOUSEHOLD = "household"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdRestriction(object):
    NOT_RESTRICTED = "not_restricted"
    USER_MASTER_RESTRICTED = "user_master_restricted"
    DEVICE_MASTER_RESTRICTED = "device_master_restricted"
    DEVICE_USER_MASTER_RESTRICTED = "device_user_master_restricted"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdState(object):
    OK = "ok"
    CREATED_WITHOUT_NPVR_ACCOUNT = "created_without_npvr_account"
    SUSPENDED = "suspended"
    NO_USERS_IN_HOUSEHOLD = "no_users_in_household"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdSuspentionState(object):
    NOT_SUSPENDED = "not_suspended"
    SUSPENDED = "suspended"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdUserStatus(object):
    OK = "OK"
    PENDING = "PENDING"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaInboxMessageOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaInboxMessageStatus(object):
    UNREAD = "Unread"
    READ = "Read"
    DELETED = "Deleted"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaInboxMessageType(object):
    SYSTEMANNOUNCEMENT = "SystemAnnouncement"
    FOLLOWED = "Followed"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaNotificationType(object):
    ANNOUNCEMENT = "announcement"
    SYSTEM = "system"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaOTTAssetType(object):
    SERIES = 0

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaOTTUserBy(object):
    USER_NAME = "USER_NAME"
    EXTERNAL_ID = "EXTERNAL_ID"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaOTTUserOrderBy(object):
    ID_ASC = "ID_ASC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaParentalRuleOrderBy(object):
    PARTNER_SORT_VALUE = "PARTNER_SORT_VALUE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaParentalRuleType(object):
    ALL = "ALL"
    MOVIES = "MOVIES"
    TV_SERIES = "TV_SERIES"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPartnerConfigurationType(object):
    DEFAULTPAYMENTGATEWAY = "DefaultPaymentGateway"
    ENABLEPAYMENTGATEWAYSELECTION = "EnablePaymentGatewaySelection"
    OSSADAPTER = "OSSAdapter"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfileOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodType(object):
    UNKNOWN = "unknown"
    CREDIT_CARD = "credit_card"
    SMS = "sms"
    PAY_PAL = "pay_pal"
    DEBIT_CARD = "debit_card"
    IDEAL = "ideal"
    INCASO = "incaso"
    GIFT = "gift"
    VISA = "visa"
    MASTER_CARD = "master_card"
    IN_APP = "in_app"
    M1 = "m1"
    CHANGE_SUBSCRIPTION = "change_subscription"
    OFFLINE = "offline"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPersonalFeedOrderBy(object):
    RELEVANCY_DESC = "RELEVANCY_DESC"
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    VIEWS_DESC = "VIEWS_DESC"
    RATINGS_DESC = "RATINGS_DESC"
    VOTES_DESC = "VOTES_DESC"
    START_DATE_DESC = "START_DATE_DESC"
    START_DATE_ASC = "START_DATE_ASC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPinType(object):
    PURCHASE = "purchase"
    PARENTAL = "parental"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPositionOwner(object):
    HOUSEHOLD = "household"
    USER = "user"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaProductPriceOrderBy(object):
    PRODUCT_ID_ASC = "PRODUCT_ID_ASC"
    PRODUCT_ID_DESC = "PRODUCT_ID_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPurchaseSettingsType(object):
    BLOCK = "block"
    ASK = "ask"
    ALLOW = "allow"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPurchaseStatus(object):
    PPV_PURCHASED = "ppv_purchased"
    FREE = "free"
    FOR_PURCHASE_SUBSCRIPTION_ONLY = "for_purchase_subscription_only"
    SUBSCRIPTION_PURCHASED = "subscription_purchased"
    FOR_PURCHASE = "for_purchase"
    SUBSCRIPTION_PURCHASED_WRONG_CURRENCY = "subscription_purchased_wrong_currency"
    PRE_PAID_PURCHASED = "pre_paid_purchased"
    GEO_COMMERCE_BLOCKED = "geo_commerce_blocked"
    ENTITLED_TO_PREVIEW_MODULE = "entitled_to_preview_module"
    FIRST_DEVICE_LIMITATION = "first_device_limitation"
    COLLECTION_PURCHASED = "collection_purchased"
    USER_SUSPENDED = "user_suspended"
    NOT_FOR_PURCHASE = "not_for_purchase"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingOrderBy(object):
    TITLE_ASC = "TITLE_ASC"
    TITLE_DESC = "TITLE_DESC"
    START_DATE_ASC = "START_DATE_ASC"
    START_DATE_DESC = "START_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingStatus(object):
    SCHEDULED = "SCHEDULED"
    RECORDING = "RECORDING"
    RECORDED = "RECORDED"
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    DELETED = "DELETED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingType(object):
    SINGLE = "SINGLE"
    SEASON = "SEASON"
    SERIES = "SERIES"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRegionOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRuleLevel(object):
    INVALID = "invalid"
    USER = "user"
    HOUSEHOLD = "household"
    ACCOUNT = "account"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRuleType(object):
    PARENTAL = "parental"
    GEO = "geo"
    USER_TYPE = "user_type"
    DEVICE = "device"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSeriesRecordingOrderBy(object):
    START_DATE_ASC = "START_DATE_ASC"
    START_DATE_DESC = "START_DATE_DESC"
    ID_ASC = "ID_ASC"
    ID_DESC = "ID_DESC"
    SERIES_ID_ASC = "SERIES_ID_ASC"
    SERIES_ID_DESC = "SERIES_ID_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSessionType(object):
    USER = 0
    ADMIN = 2

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSocialNetwork(object):
    FACEBOOK = "facebook"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaStreamType(object):
    CATCHUP = "catchup"
    START_OVER = "start_over"
    TRICK_PLAY = "trick_play"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSubscriptionOrderBy(object):
    START_DATE_ASC = "START_DATE_ASC"
    START_DATE_DESC = "START_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTopicAutomaticIssueNotification(object):
    INHERIT = "Inherit"
    YES = "Yes"
    NO = "No"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTopicOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTransactionAdapterStatus(object):
    OK = "OK"
    PENDING = "PENDING"
    FAILED = "FAILED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTransactionHistoryOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTransactionType(object):
    PPV = "ppv"
    SUBSCRIPTION = "subscription"
    COLLECTION = "collection"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUserAssetRuleOrderBy(object):
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUserAssetsListItemType(object):
    ALL = "all"
    MEDIA = "media"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUserAssetsListType(object):
    ALL = "all"
    WATCH = "watch"
    PURCHASE = "purchase"
    LIBRARY = "library"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUserRoleOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUserState(object):
    OK = "ok"
    USER_WITH_NO_HOUSEHOLD = "user_with_no_household"
    USER_CREATED_WITH_NO_ROLE = "user_created_with_no_role"
    USER_NOT_ACTIVATED = "user_not_activated"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaWatchStatus(object):
    PROGRESS = "progress"
    DONE = "done"
    ALL = "all"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaAnnouncement(KalturaObjectBase):
    def __init__(self,
            name=NotImplemented,
            message=NotImplemented,
            enabled=NotImplemented,
            startTime=NotImplemented,
            timezone=NotImplemented,
            status=NotImplemented,
            recipients=NotImplemented,
            id=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.name = name

        # @var string
        self.message = message

        # @var bool
        self.enabled = enabled

        # @var int
        self.startTime = startTime

        # @var string
        self.timezone = timezone

        # @var KalturaAnnouncementStatus
        # @readonly
        self.status = status

        # @var KalturaAnnouncementRecipientsType
        self.recipients = recipients

        # @var int
        # @readonly
        self.id = id


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'message': getXmlNodeText, 
        'enabled': getXmlNodeBool, 
        'startTime': getXmlNodeInt, 
        'timezone': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createString, "KalturaAnnouncementStatus"), 
        'recipients': (KalturaEnumsFactory.createString, "KalturaAnnouncementRecipientsType"), 
        'id': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnouncement.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAnnouncement")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("message", self.message)
        kparams.addBoolIfDefined("enabled", self.enabled)
        kparams.addIntIfDefined("startTime", self.startTime)
        kparams.addStringIfDefined("timezone", self.timezone)
        kparams.addStringEnumIfDefined("recipients", self.recipients)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage):
        self.message = newMessage

    def getEnabled(self):
        return self.enabled

    def setEnabled(self, newEnabled):
        self.enabled = newEnabled

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, newStartTime):
        self.startTime = newStartTime

    def getTimezone(self):
        return self.timezone

    def setTimezone(self, newTimezone):
        self.timezone = newTimezone

    def getStatus(self):
        return self.status

    def getRecipients(self):
        return self.recipients

    def setRecipients(self, newRecipients):
        self.recipients = newRecipients

    def getId(self):
        return self.id


# @package Kaltura
# @subpackage Client
class KalturaFilter(KalturaObjectBase):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.orderBy = orderBy


    PROPERTY_LOADERS = {
        'orderBy': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFilter")
        kparams.addIntIfDefined("orderBy", self.orderBy)
        return kparams

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy


# @package Kaltura
# @subpackage Client
class KalturaAnnouncementFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnouncementFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAnnouncementFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaFilterPager(KalturaObjectBase):
    """The KalturaFilterPager object enables paging management to be applied upon service list actions"""

    def __init__(self,
            pageSize=NotImplemented,
            pageIndex=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The number of objects to retrieve. Possible range 1 ≤ value ≤ 50. If omitted or value &lt; 1 - will be set to 25. If a value &gt; 50 provided – will be set to 50
        # @var int
        self.pageSize = pageSize

        # The page number for which {pageSize} of objects should be retrieved
        # @var int
        self.pageIndex = pageIndex


    PROPERTY_LOADERS = {
        'pageSize': getXmlNodeInt, 
        'pageIndex': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFilterPager.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFilterPager")
        kparams.addIntIfDefined("pageSize", self.pageSize)
        kparams.addIntIfDefined("pageIndex", self.pageIndex)
        return kparams

    def getPageSize(self):
        return self.pageSize

    def setPageSize(self, newPageSize):
        self.pageSize = newPageSize

    def getPageIndex(self):
        return self.pageIndex

    def setPageIndex(self, newPageIndex):
        self.pageIndex = newPageIndex


# @package Kaltura
# @subpackage Client
class KalturaListResponse(KalturaObjectBase):
    """Base list wrapper"""

    def __init__(self,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Total items
        # @var int
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaListResponse")
        kparams.addIntIfDefined("totalCount", self.totalCount)
        return kparams

    def getTotalCount(self):
        return self.totalCount

    def setTotalCount(self, newTotalCount):
        self.totalCount = newTotalCount


# @package Kaltura
# @subpackage Client
class KalturaRegionalChannel(KalturaObjectBase):
    def __init__(self,
            linearChannelId=NotImplemented,
            channelNumber=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The identifier of the linear media representing the channel
        # @var int
        self.linearChannelId = linearChannelId

        # The number of the channel
        # @var int
        self.channelNumber = channelNumber


    PROPERTY_LOADERS = {
        'linearChannelId': getXmlNodeInt, 
        'channelNumber': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegionalChannel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRegionalChannel")
        kparams.addIntIfDefined("linearChannelId", self.linearChannelId)
        kparams.addIntIfDefined("channelNumber", self.channelNumber)
        return kparams

    def getLinearChannelId(self):
        return self.linearChannelId

    def setLinearChannelId(self, newLinearChannelId):
        self.linearChannelId = newLinearChannelId

    def getChannelNumber(self):
        return self.channelNumber

    def setChannelNumber(self, newChannelNumber):
        self.channelNumber = newChannelNumber


# @package Kaltura
# @subpackage Client
class KalturaRegion(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            externalId=NotImplemented,
            isDefault=NotImplemented,
            linearChannels=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Region identifier
        # @var int
        self.id = id

        # Region name
        # @var string
        self.name = name

        # Region external identifier
        # @var string
        self.externalId = externalId

        # Indicates whether this is the default region for the partner
        # @var bool
        self.isDefault = isDefault

        # List of associated linear channels
        # @var array of KalturaRegionalChannel
        self.linearChannels = linearChannels


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'externalId': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
        'linearChannels': (KalturaObjectFactory.createArray, KalturaRegionalChannel), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegion.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRegion")
        kparams.addIntIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        kparams.addArrayIfDefined("linearChannels", self.linearChannels)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getLinearChannels(self):
        return self.linearChannels

    def setLinearChannels(self, newLinearChannels):
        self.linearChannels = newLinearChannels


# @package Kaltura
# @subpackage Client
class KalturaRegionListResponse(KalturaListResponse):
    """Regions list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of regions
        # @var array of KalturaRegion
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaRegion), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRegionListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaUserAssetRule(KalturaObjectBase):
    """User asset rule - representing different type of rules on an asset(Parental, Geo, User Type, Device)"""

    def __init__(self,
            id=NotImplemented,
            ruleType=NotImplemented,
            name=NotImplemented,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique rule identifier
        # @var int
        # @readonly
        self.id = id

        # Rule type - possible values: Rule type – Parental, Geo, UserType, Device
        # @var KalturaRuleType
        self.ruleType = ruleType

        # Rule display name
        # @var string
        self.name = name

        # Additional description for the specific rule
        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'ruleType': (KalturaEnumsFactory.createString, "KalturaRuleType"), 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserAssetRule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserAssetRule")
        kparams.addStringEnumIfDefined("ruleType", self.ruleType)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getId(self):
        return self.id

    def getRuleType(self):
        return self.ruleType

    def setRuleType(self, newRuleType):
        self.ruleType = newRuleType

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaUserAssetRuleListResponse(KalturaListResponse):
    """GenericRules list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of generic rules
        # @var array of KalturaUserAssetRule
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUserAssetRule), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserAssetRuleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaUserAssetRuleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaValue(KalturaObjectBase):
    """A representation to return an array of values"""

    def __init__(self,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaValue")
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaLongValue(KalturaValue):
    """A string representation to return an array of longs"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # @var int
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLongValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaLongValue")
        kparams.addIntIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaDoubleValue(KalturaValue):
    """A string representation to return an array of doubles"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # @var float
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDoubleValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaDoubleValue")
        kparams.addFloatIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaBooleanValue(KalturaValue):
    """A string representation to return an array of booleans"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # @var bool
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBooleanValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaBooleanValue")
        kparams.addBoolIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaIntegerValue(KalturaValue):
    """A string representation to return an array of ints"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # @var int
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaIntegerValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaIntegerValue")
        kparams.addIntIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaStringValue(KalturaValue):
    """A string representation to return an array of strings"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStringValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaStringValue")
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaCDNAdapterProfile(KalturaObjectBase):
    """CDN Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            baseUrl=NotImplemented,
            settings=NotImplemented,
            systemName=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaObjectBase.__init__(self)

        # CDN adapter identifier
        # @var int
        # @readonly
        self.id = id

        # CDNR adapter name
        # @var string
        self.name = name

        # CDN adapter active status
        # @var bool
        self.isActive = isActive

        # CDN adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # CDN adapter base URL
        # @var string
        self.baseUrl = baseUrl

        # CDN adapter settings
        # @var map
        self.settings = settings

        # CDN adapter alias
        # @var string
        self.systemName = systemName

        # CDN shared secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'baseUrl': getXmlNodeText, 
        'settings': (KalturaObjectFactory.create, map), 
        'systemName': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDNAdapterProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCDNAdapterProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addStringIfDefined("baseUrl", self.baseUrl)
        kparams.addObjectIfDefined("settings", self.settings)
        kparams.addStringIfDefined("systemName", self.systemName)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getBaseUrl(self):
        return self.baseUrl

    def setBaseUrl(self, newBaseUrl):
        self.baseUrl = newBaseUrl

    def getSettings(self):
        return self.settings

    def setSettings(self, newSettings):
        self.settings = newSettings

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getSharedSecret(self):
        return self.sharedSecret


# @package Kaltura
# @subpackage Client
class KalturaCDNAdapterProfileListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Adapters
        # @var array of KalturaCDNAdapterProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaCDNAdapterProfile), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDNAdapterProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCDNAdapterProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSlimAsset(KalturaObjectBase):
    """Slim Asset Details"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Internal identifier of the asset
        # @var string
        # @insertonly
        self.id = id

        # The type of the asset. Possible values: media, recording, epg
        # @var KalturaAssetType
        # @insertonly
        self.type = type


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSlimAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSlimAsset")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaBaseOTTUser(KalturaObjectBase):
    """Slim user data"""

    def __init__(self,
            id=NotImplemented,
            username=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented):
        KalturaObjectBase.__init__(self)

        # User identifier
        # @var string
        # @readonly
        self.id = id

        # Username
        # @var string
        self.username = username

        # First name
        # @var string
        self.firstName = firstName

        # Last name
        # @var string
        self.lastName = lastName


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'username': getXmlNodeText, 
        'firstName': getXmlNodeText, 
        'lastName': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseOTTUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseOTTUser")
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("firstName", self.firstName)
        kparams.addStringIfDefined("lastName", self.lastName)
        return kparams

    def getId(self):
        return self.id

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName


# @package Kaltura
# @subpackage Client
class KalturaCountry(KalturaObjectBase):
    """Country details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            code=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Country identifier
        # @var int
        # @readonly
        self.id = id

        # Country name
        # @var string
        self.name = name

        # Country code
        # @var string
        self.code = code


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'code': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCountry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCountry")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("code", self.code)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getCode(self):
        return self.code

    def setCode(self, newCode):
        self.code = newCode


# @package Kaltura
# @subpackage Client
class KalturaOTTUserType(KalturaObjectBase):
    """User type"""

    def __init__(self,
            id=NotImplemented,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # User type identifier
        # @var int
        # @readonly
        self.id = id

        # User type description
        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTUserType.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaOTTUserType")
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getId(self):
        return self.id

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaOTTUser(KalturaBaseOTTUser):
    """User"""

    def __init__(self,
            id=NotImplemented,
            username=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented,
            householdId=NotImplemented,
            email=NotImplemented,
            address=NotImplemented,
            city=NotImplemented,
            country=NotImplemented,
            zip=NotImplemented,
            phone=NotImplemented,
            affiliateCode=NotImplemented,
            externalId=NotImplemented,
            userType=NotImplemented,
            dynamicData=NotImplemented,
            isHouseholdMaster=NotImplemented,
            suspentionState=NotImplemented,
            userState=NotImplemented):
        KalturaBaseOTTUser.__init__(self,
            id,
            username,
            firstName,
            lastName)

        # Household identifier
        # @var int
        # @readonly
        self.householdId = householdId

        # Email
        # @var string
        self.email = email

        # Address
        # @var string
        self.address = address

        # City
        # @var string
        self.city = city

        # Country
        # @var KalturaCountry
        self.country = country

        # Zip code
        # @var string
        self.zip = zip

        # Phone
        # @var string
        self.phone = phone

        # Affiliate code
        # @var string
        self.affiliateCode = affiliateCode

        # External user identifier
        # @var string
        self.externalId = externalId

        # User type
        # @var KalturaOTTUserType
        self.userType = userType

        # Dynamic data
        # @var map
        self.dynamicData = dynamicData

        # Is the user the household master
        # @var bool
        # @readonly
        self.isHouseholdMaster = isHouseholdMaster

        # Suspention state
        # @var KalturaHouseholdSuspentionState
        # @readonly
        self.suspentionState = suspentionState

        # User state
        # @var KalturaUserState
        # @readonly
        self.userState = userState


    PROPERTY_LOADERS = {
        'householdId': getXmlNodeInt, 
        'email': getXmlNodeText, 
        'address': getXmlNodeText, 
        'city': getXmlNodeText, 
        'country': (KalturaObjectFactory.create, KalturaCountry), 
        'zip': getXmlNodeText, 
        'phone': getXmlNodeText, 
        'affiliateCode': getXmlNodeText, 
        'externalId': getXmlNodeText, 
        'userType': (KalturaObjectFactory.create, KalturaOTTUserType), 
        'dynamicData': (KalturaObjectFactory.create, map), 
        'isHouseholdMaster': getXmlNodeBool, 
        'suspentionState': (KalturaEnumsFactory.createString, "KalturaHouseholdSuspentionState"), 
        'userState': (KalturaEnumsFactory.createString, "KalturaUserState"), 
    }

    def fromXml(self, node):
        KalturaBaseOTTUser.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseOTTUser.toParams(self)
        kparams.put("objectType", "KalturaOTTUser")
        kparams.addStringIfDefined("email", self.email)
        kparams.addStringIfDefined("address", self.address)
        kparams.addStringIfDefined("city", self.city)
        kparams.addObjectIfDefined("country", self.country)
        kparams.addStringIfDefined("zip", self.zip)
        kparams.addStringIfDefined("phone", self.phone)
        kparams.addStringIfDefined("affiliateCode", self.affiliateCode)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addObjectIfDefined("userType", self.userType)
        kparams.addObjectIfDefined("dynamicData", self.dynamicData)
        return kparams

    def getHouseholdId(self):
        return self.householdId

    def getEmail(self):
        return self.email

    def setEmail(self, newEmail):
        self.email = newEmail

    def getAddress(self):
        return self.address

    def setAddress(self, newAddress):
        self.address = newAddress

    def getCity(self):
        return self.city

    def setCity(self, newCity):
        self.city = newCity

    def getCountry(self):
        return self.country

    def setCountry(self, newCountry):
        self.country = newCountry

    def getZip(self):
        return self.zip

    def setZip(self, newZip):
        self.zip = newZip

    def getPhone(self):
        return self.phone

    def setPhone(self, newPhone):
        self.phone = newPhone

    def getAffiliateCode(self):
        return self.affiliateCode

    def setAffiliateCode(self, newAffiliateCode):
        self.affiliateCode = newAffiliateCode

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getUserType(self):
        return self.userType

    def setUserType(self, newUserType):
        self.userType = newUserType

    def getDynamicData(self):
        return self.dynamicData

    def setDynamicData(self, newDynamicData):
        self.dynamicData = newDynamicData

    def getIsHouseholdMaster(self):
        return self.isHouseholdMaster

    def getSuspentionState(self):
        return self.suspentionState

    def getUserState(self):
        return self.userState


# @package Kaltura
# @subpackage Client
class KalturaBookmarkPlayerData(KalturaObjectBase):
    def __init__(self,
            action=NotImplemented,
            averageBitrate=NotImplemented,
            totalBitrate=NotImplemented,
            currentBitrate=NotImplemented,
            fileId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Action
        # @var KalturaBookmarkActionType
        self.action = action

        # Average Bitrate
        # @var int
        self.averageBitrate = averageBitrate

        # Total Bitrate
        # @var int
        self.totalBitrate = totalBitrate

        # Current Bitrate
        # @var int
        self.currentBitrate = currentBitrate

        # Identifier of the file
        # @var int
        self.fileId = fileId


    PROPERTY_LOADERS = {
        'action': (KalturaEnumsFactory.createString, "KalturaBookmarkActionType"), 
        'averageBitrate': getXmlNodeInt, 
        'totalBitrate': getXmlNodeInt, 
        'currentBitrate': getXmlNodeInt, 
        'fileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBookmarkPlayerData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBookmarkPlayerData")
        kparams.addStringEnumIfDefined("action", self.action)
        kparams.addIntIfDefined("averageBitrate", self.averageBitrate)
        kparams.addIntIfDefined("totalBitrate", self.totalBitrate)
        kparams.addIntIfDefined("currentBitrate", self.currentBitrate)
        kparams.addIntIfDefined("fileId", self.fileId)
        return kparams

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getAverageBitrate(self):
        return self.averageBitrate

    def setAverageBitrate(self, newAverageBitrate):
        self.averageBitrate = newAverageBitrate

    def getTotalBitrate(self):
        return self.totalBitrate

    def setTotalBitrate(self, newTotalBitrate):
        self.totalBitrate = newTotalBitrate

    def getCurrentBitrate(self):
        return self.currentBitrate

    def setCurrentBitrate(self, newCurrentBitrate):
        self.currentBitrate = newCurrentBitrate

    def getFileId(self):
        return self.fileId

    def setFileId(self, newFileId):
        self.fileId = newFileId


# @package Kaltura
# @subpackage Client
class KalturaBookmark(KalturaSlimAsset):
    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            userId=NotImplemented,
            position=NotImplemented,
            positionOwner=NotImplemented,
            finishedWatching=NotImplemented,
            playerData=NotImplemented):
        KalturaSlimAsset.__init__(self,
            id,
            type)

        # User identifier
        # @var string
        # @readonly
        self.userId = userId

        # The position of the user in the specific asset (in seconds)
        # @var int
        # @insertonly
        self.position = position

        # Indicates who is the owner of this position
        # @var KalturaPositionOwner
        self.positionOwner = positionOwner

        # Specifies whether the user&#39;s current position exceeded 95% of the duration
        # @var bool
        self.finishedWatching = finishedWatching

        # Insert only player data
        # @var KalturaBookmarkPlayerData
        self.playerData = playerData


    PROPERTY_LOADERS = {
        'userId': getXmlNodeText, 
        'position': getXmlNodeInt, 
        'positionOwner': (KalturaEnumsFactory.createString, "KalturaPositionOwner"), 
        'finishedWatching': getXmlNodeBool, 
        'playerData': (KalturaObjectFactory.create, KalturaBookmarkPlayerData), 
    }

    def fromXml(self, node):
        KalturaSlimAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBookmark.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSlimAsset.toParams(self)
        kparams.put("objectType", "KalturaBookmark")
        kparams.addIntIfDefined("position", self.position)
        kparams.addStringEnumIfDefined("positionOwner", self.positionOwner)
        kparams.addBoolIfDefined("finishedWatching", self.finishedWatching)
        kparams.addObjectIfDefined("playerData", self.playerData)
        return kparams

    def getUserId(self):
        return self.userId

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition

    def getPositionOwner(self):
        return self.positionOwner

    def setPositionOwner(self, newPositionOwner):
        self.positionOwner = newPositionOwner

    def getFinishedWatching(self):
        return self.finishedWatching

    def setFinishedWatching(self, newFinishedWatching):
        self.finishedWatching = newFinishedWatching

    def getPlayerData(self):
        return self.playerData

    def setPlayerData(self, newPlayerData):
        self.playerData = newPlayerData


# @package Kaltura
# @subpackage Client
class KalturaBookmarkListResponse(KalturaListResponse):
    """List of assets and their bookmarks"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaBookmark
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBookmark), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBookmarkListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaBookmarkListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaStringValueArray(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented):
        KalturaObjectBase.__init__(self)

        # List of string values
        # @var array of KalturaStringValue
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaStringValue), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStringValueArray.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaStringValueArray")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaMediaImage(KalturaObjectBase):
    """Image details"""

    def __init__(self,
            ratio=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            url=NotImplemented,
            version=NotImplemented,
            id=NotImplemented,
            isDefault=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Image aspect ratio
        # @var string
        self.ratio = ratio

        # Image width
        # @var int
        self.width = width

        # Image height
        # @var int
        self.height = height

        # Image URL
        # @var string
        self.url = url

        # Image Version
        # @var int
        self.version = version

        # Image ID
        # @var string
        # @readonly
        self.id = id

        # Determined whether image was taken from default configuration or not
        # @var bool
        self.isDefault = isDefault


    PROPERTY_LOADERS = {
        'ratio': getXmlNodeText, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'url': getXmlNodeText, 
        'version': getXmlNodeInt, 
        'id': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaImage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaImage")
        kparams.addStringIfDefined("ratio", self.ratio)
        kparams.addIntIfDefined("width", self.width)
        kparams.addIntIfDefined("height", self.height)
        kparams.addStringIfDefined("url", self.url)
        kparams.addIntIfDefined("version", self.version)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        return kparams

    def getRatio(self):
        return self.ratio

    def setRatio(self, newRatio):
        self.ratio = newRatio

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getVersion(self):
        return self.version

    def setVersion(self, newVersion):
        self.version = newVersion

    def getId(self):
        return self.id

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault


# @package Kaltura
# @subpackage Client
class KalturaMediaFile(KalturaObjectBase):
    """Media file details"""

    def __init__(self,
            assetId=NotImplemented,
            id=NotImplemented,
            type=NotImplemented,
            url=NotImplemented,
            duration=NotImplemented,
            externalId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier for the asset
        # @var int
        self.assetId = assetId

        # File unique identifier
        # @var int
        # @readonly
        self.id = id

        # Device types as defined in the system
        # @var string
        self.type = type

        # URL of the media file to be played
        # @var string
        self.url = url

        # Duration of the media file
        # @var int
        self.duration = duration

        # External identifier for the media file
        # @var string
        self.externalId = externalId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
        'id': getXmlNodeInt, 
        'type': getXmlNodeText, 
        'url': getXmlNodeText, 
        'duration': getXmlNodeInt, 
        'externalId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaFile")
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addStringIfDefined("type", self.type)
        kparams.addStringIfDefined("url", self.url)
        kparams.addIntIfDefined("duration", self.duration)
        kparams.addStringIfDefined("externalId", self.externalId)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getDuration(self):
        return self.duration

    def setDuration(self, newDuration):
        self.duration = newDuration

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId


# @package Kaltura
# @subpackage Client
class KalturaBuzzScore(KalturaObjectBase):
    """Buzz score"""

    def __init__(self,
            normalizedAvgScore=NotImplemented,
            updateDate=NotImplemented,
            avgScore=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Normalized average score
        # @var float
        self.normalizedAvgScore = normalizedAvgScore

        # Update date
        # @var int
        self.updateDate = updateDate

        # Average score
        # @var float
        self.avgScore = avgScore


    PROPERTY_LOADERS = {
        'normalizedAvgScore': getXmlNodeFloat, 
        'updateDate': getXmlNodeInt, 
        'avgScore': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBuzzScore.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBuzzScore")
        kparams.addFloatIfDefined("normalizedAvgScore", self.normalizedAvgScore)
        kparams.addIntIfDefined("updateDate", self.updateDate)
        kparams.addFloatIfDefined("avgScore", self.avgScore)
        return kparams

    def getNormalizedAvgScore(self):
        return self.normalizedAvgScore

    def setNormalizedAvgScore(self, newNormalizedAvgScore):
        self.normalizedAvgScore = newNormalizedAvgScore

    def getUpdateDate(self):
        return self.updateDate

    def setUpdateDate(self, newUpdateDate):
        self.updateDate = newUpdateDate

    def getAvgScore(self):
        return self.avgScore

    def setAvgScore(self, newAvgScore):
        self.avgScore = newAvgScore


# @package Kaltura
# @subpackage Client
class KalturaAssetStatistics(KalturaObjectBase):
    """Asset statistics"""

    def __init__(self,
            assetId=NotImplemented,
            likes=NotImplemented,
            views=NotImplemented,
            ratingCount=NotImplemented,
            rating=NotImplemented,
            buzzScore=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier for the asset
        # @var int
        self.assetId = assetId

        # Total number of likes for this asset
        # @var int
        self.likes = likes

        # Total number of views for this asset
        # @var int
        self.views = views

        # Number of people that rated the asset
        # @var int
        self.ratingCount = ratingCount

        # Average rating for the asset
        # @var float
        self.rating = rating

        # Buzz score
        # @var KalturaBuzzScore
        self.buzzScore = buzzScore


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
        'likes': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'ratingCount': getXmlNodeInt, 
        'rating': getXmlNodeFloat, 
        'buzzScore': (KalturaObjectFactory.create, KalturaBuzzScore), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStatistics.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetStatistics")
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addIntIfDefined("likes", self.likes)
        kparams.addIntIfDefined("views", self.views)
        kparams.addIntIfDefined("ratingCount", self.ratingCount)
        kparams.addFloatIfDefined("rating", self.rating)
        kparams.addObjectIfDefined("buzzScore", self.buzzScore)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getLikes(self):
        return self.likes

    def setLikes(self, newLikes):
        self.likes = newLikes

    def getViews(self):
        return self.views

    def setViews(self, newViews):
        self.views = newViews

    def getRatingCount(self):
        return self.ratingCount

    def setRatingCount(self, newRatingCount):
        self.ratingCount = newRatingCount

    def getRating(self):
        return self.rating

    def setRating(self, newRating):
        self.rating = newRating

    def getBuzzScore(self):
        return self.buzzScore

    def setBuzzScore(self, newBuzzScore):
        self.buzzScore = newBuzzScore


# @package Kaltura
# @subpackage Client
class KalturaBaseAssetInfo(KalturaObjectBase):
    """Slim asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier for the asset
        # @var int
        # @readonly
        self.id = id

        # Identifies the asset type (EPG, Movie, TV Series, etc). 
        #             Possible values: 0 – EPG linear programs, or any asset type ID according to the asset types IDs defined in the system.
        # @var int
        self.type = type

        # Asset name
        # @var string
        self.name = name

        # Asset description
        # @var string
        self.description = description

        # Collection of images details that can be used to represent this asset
        # @var array of KalturaMediaImage
        self.images = images

        # Files
        # @var array of KalturaMediaFile
        self.mediaFiles = mediaFiles


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'type': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'images': (KalturaObjectFactory.createArray, KalturaMediaImage), 
        'mediaFiles': (KalturaObjectFactory.createArray, KalturaMediaFile), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseAssetInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseAssetInfo")
        kparams.addIntIfDefined("type", self.type)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addArrayIfDefined("images", self.images)
        kparams.addArrayIfDefined("mediaFiles", self.mediaFiles)
        return kparams

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getImages(self):
        return self.images

    def setImages(self, newImages):
        self.images = newImages

    def getMediaFiles(self):
        return self.mediaFiles

    def setMediaFiles(self, newMediaFiles):
        self.mediaFiles = newMediaFiles


# @package Kaltura
# @subpackage Client
class KalturaAsset(KalturaBaseAssetInfo):
    """Asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented,
            metas=NotImplemented,
            tags=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            enableCdvr=NotImplemented,
            enableCatchUp=NotImplemented,
            enableStartOver=NotImplemented,
            enableTrickPlay=NotImplemented):
        KalturaBaseAssetInfo.__init__(self,
            id,
            type,
            name,
            description,
            images,
            mediaFiles)

        # Dynamic collection of key-value pairs according to the String Meta defined in the system
        # @var map
        self.metas = metas

        # Dynamic collection of key-value pairs according to the Tag Types defined in the system
        # @var map
        self.tags = tags

        # Date and time represented as epoch. For VOD – since when the asset is available in the catalog. For EPG/Linear – when the program is aired (can be in the future).
        # @var int
        self.startDate = startDate

        # Date and time represented as epoch. For VOD – till when the asset be available in the catalog. For EPG/Linear – program end time and date
        # @var int
        self.endDate = endDate

        # Enable cDVR
        # @var bool
        self.enableCdvr = enableCdvr

        # Enable catch-up
        # @var bool
        self.enableCatchUp = enableCatchUp

        # Enable start over
        # @var bool
        self.enableStartOver = enableStartOver

        # Enable trick-play
        # @var bool
        self.enableTrickPlay = enableTrickPlay


    PROPERTY_LOADERS = {
        'metas': (KalturaObjectFactory.create, map), 
        'tags': (KalturaObjectFactory.create, map), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'enableCdvr': getXmlNodeBool, 
        'enableCatchUp': getXmlNodeBool, 
        'enableStartOver': getXmlNodeBool, 
        'enableTrickPlay': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaBaseAssetInfo.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseAssetInfo.toParams(self)
        kparams.put("objectType", "KalturaAsset")
        kparams.addObjectIfDefined("metas", self.metas)
        kparams.addObjectIfDefined("tags", self.tags)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addBoolIfDefined("enableCdvr", self.enableCdvr)
        kparams.addBoolIfDefined("enableCatchUp", self.enableCatchUp)
        kparams.addBoolIfDefined("enableStartOver", self.enableStartOver)
        kparams.addBoolIfDefined("enableTrickPlay", self.enableTrickPlay)
        return kparams

    def getMetas(self):
        return self.metas

    def setMetas(self, newMetas):
        self.metas = newMetas

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getEnableCdvr(self):
        return self.enableCdvr

    def setEnableCdvr(self, newEnableCdvr):
        self.enableCdvr = newEnableCdvr

    def getEnableCatchUp(self):
        return self.enableCatchUp

    def setEnableCatchUp(self, newEnableCatchUp):
        self.enableCatchUp = newEnableCatchUp

    def getEnableStartOver(self):
        return self.enableStartOver

    def setEnableStartOver(self, newEnableStartOver):
        self.enableStartOver = newEnableStartOver

    def getEnableTrickPlay(self):
        return self.enableTrickPlay

    def setEnableTrickPlay(self, newEnableTrickPlay):
        self.enableTrickPlay = newEnableTrickPlay


# @package Kaltura
# @subpackage Client
class KalturaAssetListResponse(KalturaListResponse):
    """Asset wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaAsset
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAsset), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaProgramAsset(KalturaAsset):
    """Program-asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented,
            metas=NotImplemented,
            tags=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            enableCdvr=NotImplemented,
            enableCatchUp=NotImplemented,
            enableStartOver=NotImplemented,
            enableTrickPlay=NotImplemented,
            epgChannelId=NotImplemented,
            epgId=NotImplemented,
            relatedMediaId=NotImplemented,
            crid=NotImplemented):
        KalturaAsset.__init__(self,
            id,
            type,
            name,
            description,
            images,
            mediaFiles,
            metas,
            tags,
            startDate,
            endDate,
            enableCdvr,
            enableCatchUp,
            enableStartOver,
            enableTrickPlay)

        # EPG channel identifier
        # @var int
        self.epgChannelId = epgChannelId

        # EPG identifier
        # @var string
        self.epgId = epgId

        # Ralated media identifier
        # @var int
        self.relatedMediaId = relatedMediaId

        # Unique identifier for the program
        # @var string
        self.crid = crid


    PROPERTY_LOADERS = {
        'epgChannelId': getXmlNodeInt, 
        'epgId': getXmlNodeText, 
        'relatedMediaId': getXmlNodeInt, 
        'crid': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProgramAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaProgramAsset")
        kparams.addIntIfDefined("epgChannelId", self.epgChannelId)
        kparams.addStringIfDefined("epgId", self.epgId)
        kparams.addIntIfDefined("relatedMediaId", self.relatedMediaId)
        kparams.addStringIfDefined("crid", self.crid)
        return kparams

    def getEpgChannelId(self):
        return self.epgChannelId

    def setEpgChannelId(self, newEpgChannelId):
        self.epgChannelId = newEpgChannelId

    def getEpgId(self):
        return self.epgId

    def setEpgId(self, newEpgId):
        self.epgId = newEpgId

    def getRelatedMediaId(self):
        return self.relatedMediaId

    def setRelatedMediaId(self, newRelatedMediaId):
        self.relatedMediaId = newRelatedMediaId

    def getCrid(self):
        return self.crid

    def setCrid(self, newCrid):
        self.crid = newCrid


# @package Kaltura
# @subpackage Client
class KalturaMediaAsset(KalturaAsset):
    """Media-asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented,
            metas=NotImplemented,
            tags=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            enableCdvr=NotImplemented,
            enableCatchUp=NotImplemented,
            enableStartOver=NotImplemented,
            enableTrickPlay=NotImplemented,
            systemStartDate=NotImplemented,
            systemFinalDate=NotImplemented,
            externalIds=NotImplemented,
            catchUpBuffer=NotImplemented,
            trickPlayBuffer=NotImplemented,
            enableRecordingPlaybackNonEntitledChannel=NotImplemented,
            enableRecordingPlaybackNonExistingChannel=NotImplemented):
        KalturaAsset.__init__(self,
            id,
            type,
            name,
            description,
            images,
            mediaFiles,
            metas,
            tags,
            startDate,
            endDate,
            enableCdvr,
            enableCatchUp,
            enableStartOver,
            enableTrickPlay)

        # Date and time represented as epoch.
        # @var int
        self.systemStartDate = systemStartDate

        # Date and time represented as epoch.
        # @var int
        self.systemFinalDate = systemFinalDate

        # External identifiers
        # @var string
        self.externalIds = externalIds

        # Catch-up buffer
        # @var int
        self.catchUpBuffer = catchUpBuffer

        # Trick-play buffer
        # @var int
        self.trickPlayBuffer = trickPlayBuffer

        # Enable Recording playback for non entitled channel
        # @var bool
        # @readonly
        self.enableRecordingPlaybackNonEntitledChannel = enableRecordingPlaybackNonEntitledChannel

        # Enable Recording playback for non existing channel
        # @var bool
        # @readonly
        self.enableRecordingPlaybackNonExistingChannel = enableRecordingPlaybackNonExistingChannel


    PROPERTY_LOADERS = {
        'systemStartDate': getXmlNodeInt, 
        'systemFinalDate': getXmlNodeInt, 
        'externalIds': getXmlNodeText, 
        'catchUpBuffer': getXmlNodeInt, 
        'trickPlayBuffer': getXmlNodeInt, 
        'enableRecordingPlaybackNonEntitledChannel': getXmlNodeBool, 
        'enableRecordingPlaybackNonExistingChannel': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaMediaAsset")
        kparams.addIntIfDefined("systemStartDate", self.systemStartDate)
        kparams.addIntIfDefined("systemFinalDate", self.systemFinalDate)
        kparams.addStringIfDefined("externalIds", self.externalIds)
        kparams.addIntIfDefined("catchUpBuffer", self.catchUpBuffer)
        kparams.addIntIfDefined("trickPlayBuffer", self.trickPlayBuffer)
        return kparams

    def getSystemStartDate(self):
        return self.systemStartDate

    def setSystemStartDate(self, newSystemStartDate):
        self.systemStartDate = newSystemStartDate

    def getSystemFinalDate(self):
        return self.systemFinalDate

    def setSystemFinalDate(self, newSystemFinalDate):
        self.systemFinalDate = newSystemFinalDate

    def getExternalIds(self):
        return self.externalIds

    def setExternalIds(self, newExternalIds):
        self.externalIds = newExternalIds

    def getCatchUpBuffer(self):
        return self.catchUpBuffer

    def setCatchUpBuffer(self, newCatchUpBuffer):
        self.catchUpBuffer = newCatchUpBuffer

    def getTrickPlayBuffer(self):
        return self.trickPlayBuffer

    def setTrickPlayBuffer(self, newTrickPlayBuffer):
        self.trickPlayBuffer = newTrickPlayBuffer

    def getEnableRecordingPlaybackNonEntitledChannel(self):
        return self.enableRecordingPlaybackNonEntitledChannel

    def getEnableRecordingPlaybackNonExistingChannel(self):
        return self.enableRecordingPlaybackNonExistingChannel


# @package Kaltura
# @subpackage Client
class KalturaAssetComment(KalturaObjectBase):
    """Asset Comment"""

    def __init__(self,
            id=NotImplemented,
            assetId=NotImplemented,
            assetType=NotImplemented,
            header=NotImplemented,
            subHeader=NotImplemented,
            text=NotImplemented,
            createDate=NotImplemented,
            writer=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Comment ID
        # @var int
        self.id = id

        # Asset identifier
        # @var string
        self.assetId = assetId

        # Asset Type
        # @var KalturaAssetType
        self.assetType = assetType

        # Header
        # @var string
        self.header = header

        # Sub Header
        # @var string
        self.subHeader = subHeader

        # Text
        # @var string
        self.text = text

        # CreateDate
        # @var int
        self.createDate = createDate

        # Writer
        # @var string
        self.writer = writer


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'assetId': getXmlNodeText, 
        'assetType': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
        'header': getXmlNodeText, 
        'subHeader': getXmlNodeText, 
        'text': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
        'writer': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetComment.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetComment")
        kparams.addIntIfDefined("id", self.id)
        kparams.addStringIfDefined("assetId", self.assetId)
        kparams.addStringEnumIfDefined("assetType", self.assetType)
        kparams.addStringIfDefined("header", self.header)
        kparams.addStringIfDefined("subHeader", self.subHeader)
        kparams.addStringIfDefined("text", self.text)
        kparams.addIntIfDefined("createDate", self.createDate)
        kparams.addStringIfDefined("writer", self.writer)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getAssetType(self):
        return self.assetType

    def setAssetType(self, newAssetType):
        self.assetType = newAssetType

    def getHeader(self):
        return self.header

    def setHeader(self, newHeader):
        self.header = newHeader

    def getSubHeader(self):
        return self.subHeader

    def setSubHeader(self, newSubHeader):
        self.subHeader = newSubHeader

    def getText(self):
        return self.text

    def setText(self, newText):
        self.text = newText

    def getCreateDate(self):
        return self.createDate

    def setCreateDate(self, newCreateDate):
        self.createDate = newCreateDate

    def getWriter(self):
        return self.writer

    def setWriter(self, newWriter):
        self.writer = newWriter


# @package Kaltura
# @subpackage Client
class KalturaAssetCommentListResponse(KalturaListResponse):
    """Asset Comment Response"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaAssetComment
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAssetComment), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetCommentListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetCommentListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSeriesRecording(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            epgId=NotImplemented,
            channelId=NotImplemented,
            seriesId=NotImplemented,
            seasonNumber=NotImplemented,
            type=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            excludedSeasons=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Kaltura unique ID representing the series recording identifier
        # @var int
        # @readonly
        self.id = id

        # Kaltura EpgId
        # @var int
        self.epgId = epgId

        # Kaltura ChannelId
        # @var int
        self.channelId = channelId

        # Kaltura SeriesId
        # @var string
        self.seriesId = seriesId

        # Kaltura SeasonNumber
        # @var int
        self.seasonNumber = seasonNumber

        # Recording Type: single/series/season
        # @var KalturaRecordingType
        self.type = type

        # Specifies when was the series recording created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the series recording last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate

        # List of the season numbers to exclude.
        # @var array of KalturaIntegerValue
        # @readonly
        self.excludedSeasons = excludedSeasons


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'epgId': getXmlNodeInt, 
        'channelId': getXmlNodeInt, 
        'seriesId': getXmlNodeText, 
        'seasonNumber': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaRecordingType"), 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
        'excludedSeasons': (KalturaObjectFactory.createArray, KalturaIntegerValue), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeriesRecording.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSeriesRecording")
        kparams.addIntIfDefined("epgId", self.epgId)
        kparams.addIntIfDefined("channelId", self.channelId)
        kparams.addStringIfDefined("seriesId", self.seriesId)
        kparams.addIntIfDefined("seasonNumber", self.seasonNumber)
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getId(self):
        return self.id

    def getEpgId(self):
        return self.epgId

    def setEpgId(self, newEpgId):
        self.epgId = newEpgId

    def getChannelId(self):
        return self.channelId

    def setChannelId(self, newChannelId):
        self.channelId = newChannelId

    def getSeriesId(self):
        return self.seriesId

    def setSeriesId(self, newSeriesId):
        self.seriesId = newSeriesId

    def getSeasonNumber(self):
        return self.seasonNumber

    def setSeasonNumber(self, newSeasonNumber):
        self.seasonNumber = newSeasonNumber

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate

    def getExcludedSeasons(self):
        return self.excludedSeasons


# @package Kaltura
# @subpackage Client
class KalturaSeriesRecordingListResponse(KalturaListResponse):
    """Series Recordings info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Series Recordings
        # @var array of KalturaSeriesRecording
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaSeriesRecording), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeriesRecordingListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSeriesRecordingListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPremiumService(KalturaObjectBase):
    """Premium service"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Service identifier
        # @var int
        # @readonly
        self.id = id

        # Service name / description
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPremiumService.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPremiumService")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPremiumService(KalturaPremiumService):
    """Houshold premium service"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaPremiumService.__init__(self,
            id,
            name)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPremiumService.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPremiumService.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPremiumService.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPremiumService")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPremiumServiceListResponse(KalturaListResponse):
    """Premium services list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of premium services
        # @var array of KalturaHouseholdPremiumService
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaHouseholdPremiumService), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPremiumServiceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPremiumServiceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaCDVRAdapterProfile(KalturaObjectBase):
    """C-DVR Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            settings=NotImplemented,
            externalIdentifier=NotImplemented,
            sharedSecret=NotImplemented,
            dynamicLinksSupport=NotImplemented):
        KalturaObjectBase.__init__(self)

        # C-DVR adapter identifier
        # @var int
        # @readonly
        self.id = id

        # C-DVR adapter name
        # @var string
        self.name = name

        # C-DVR adapter active status
        # @var bool
        self.isActive = isActive

        # C-DVR adapter adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # C-DVR adapter extra parameters
        # @var map
        self.settings = settings

        # C-DVR adapter external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # C-DVR shared secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret

        # Indicates whether the C-DVR adapter supports dynamic URLs
        # @var bool
        self.dynamicLinksSupport = dynamicLinksSupport


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'settings': (KalturaObjectFactory.create, map), 
        'externalIdentifier': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
        'dynamicLinksSupport': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDVRAdapterProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCDVRAdapterProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addObjectIfDefined("settings", self.settings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        kparams.addBoolIfDefined("dynamicLinksSupport", self.dynamicLinksSupport)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getSettings(self):
        return self.settings

    def setSettings(self, newSettings):
        self.settings = newSettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getSharedSecret(self):
        return self.sharedSecret

    def getDynamicLinksSupport(self):
        return self.dynamicLinksSupport

    def setDynamicLinksSupport(self, newDynamicLinksSupport):
        self.dynamicLinksSupport = newDynamicLinksSupport


# @package Kaltura
# @subpackage Client
class KalturaCDVRAdapterProfileListResponse(KalturaListResponse):
    """C-DVR adapter profiles"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # C-DVR adapter profiles
        # @var array of KalturaCDVRAdapterProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaCDVRAdapterProfile), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDVRAdapterProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCDVRAdapterProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaExportTask(KalturaObjectBase):
    """Bulk export task"""

    def __init__(self,
            id=NotImplemented,
            alias=NotImplemented,
            name=NotImplemented,
            dataType=NotImplemented,
            filter=NotImplemented,
            exportType=NotImplemented,
            frequency=NotImplemented,
            notificationUrl=NotImplemented,
            vodTypes=NotImplemented,
            isActive=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Task identifier
        # @var int
        # @readonly
        self.id = id

        # Alias for the task used to solicit an export using API
        # @var string
        self.alias = alias

        # Task display name
        # @var string
        self.name = name

        # The data type exported in this task
        # @var KalturaExportDataType
        self.dataType = dataType

        # Filter to apply on the export, utilize KSQL.
        #             Note: KSQL currently applies to media assets only. It cannot be used for USERS filtering
        # @var string
        self.filter = filter

        # Type of export batch – full or incremental
        # @var KalturaExportType
        self.exportType = exportType

        # How often the export should occur, reasonable minimum threshold should apply, configurable in minutes
        # @var int
        self.frequency = frequency

        # The URL for sending a notification when the task&#39;s export process is done
        # @var string
        self.notificationUrl = notificationUrl

        # List of media type identifiers (as configured in TVM) to export. used only in case data_type = vod
        # @var array of KalturaIntegerValue
        self.vodTypes = vodTypes

        # Indicates if the task is active or not
        # @var bool
        self.isActive = isActive


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'alias': getXmlNodeText, 
        'name': getXmlNodeText, 
        'dataType': (KalturaEnumsFactory.createString, "KalturaExportDataType"), 
        'filter': getXmlNodeText, 
        'exportType': (KalturaEnumsFactory.createString, "KalturaExportType"), 
        'frequency': getXmlNodeInt, 
        'notificationUrl': getXmlNodeText, 
        'vodTypes': (KalturaObjectFactory.createArray, KalturaIntegerValue), 
        'isActive': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExportTask.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaExportTask")
        kparams.addStringIfDefined("alias", self.alias)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringEnumIfDefined("dataType", self.dataType)
        kparams.addStringIfDefined("filter", self.filter)
        kparams.addStringEnumIfDefined("exportType", self.exportType)
        kparams.addIntIfDefined("frequency", self.frequency)
        kparams.addStringIfDefined("notificationUrl", self.notificationUrl)
        kparams.addArrayIfDefined("vodTypes", self.vodTypes)
        kparams.addBoolIfDefined("isActive", self.isActive)
        return kparams

    def getId(self):
        return self.id

    def getAlias(self):
        return self.alias

    def setAlias(self, newAlias):
        self.alias = newAlias

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDataType(self):
        return self.dataType

    def setDataType(self, newDataType):
        self.dataType = newDataType

    def getFilter(self):
        return self.filter

    def setFilter(self, newFilter):
        self.filter = newFilter

    def getExportType(self):
        return self.exportType

    def setExportType(self, newExportType):
        self.exportType = newExportType

    def getFrequency(self):
        return self.frequency

    def setFrequency(self, newFrequency):
        self.frequency = newFrequency

    def getNotificationUrl(self):
        return self.notificationUrl

    def setNotificationUrl(self, newNotificationUrl):
        self.notificationUrl = newNotificationUrl

    def getVodTypes(self):
        return self.vodTypes

    def setVodTypes(self, newVodTypes):
        self.vodTypes = newVodTypes

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive


# @package Kaltura
# @subpackage Client
class KalturaExportTaskListResponse(KalturaListResponse):
    """Export task list wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Export task items
        # @var array of KalturaExportTask
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaExportTask), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExportTaskListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaExportTaskListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaChannelEnrichmentHolder(KalturaObjectBase):
    """Holder object for channel enrichment enum"""

    def __init__(self,
            type=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var KalturaChannelEnrichment
        self.type = type


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createString, "KalturaChannelEnrichment"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelEnrichmentHolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaChannelEnrichmentHolder")
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaExternalChannelProfile(KalturaObjectBase):
    """OSS Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            externalIdentifier=NotImplemented,
            filterExpression=NotImplemented,
            recommendationEngineId=NotImplemented,
            enrichments=NotImplemented):
        KalturaObjectBase.__init__(self)

        # External channel id
        # @var int
        # @readonly
        self.id = id

        # External channel name
        # @var string
        self.name = name

        # External channel active status
        # @var bool
        self.isActive = isActive

        # External channel external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Filter expression
        # @var string
        self.filterExpression = filterExpression

        # Recommendation engine id
        # @var int
        self.recommendationEngineId = recommendationEngineId

        # Enrichments
        # @var array of KalturaChannelEnrichmentHolder
        self.enrichments = enrichments


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'externalIdentifier': getXmlNodeText, 
        'filterExpression': getXmlNodeText, 
        'recommendationEngineId': getXmlNodeInt, 
        'enrichments': (KalturaObjectFactory.createArray, KalturaChannelEnrichmentHolder), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExternalChannelProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaExternalChannelProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        kparams.addStringIfDefined("filterExpression", self.filterExpression)
        kparams.addIntIfDefined("recommendationEngineId", self.recommendationEngineId)
        kparams.addArrayIfDefined("enrichments", self.enrichments)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getFilterExpression(self):
        return self.filterExpression

    def setFilterExpression(self, newFilterExpression):
        self.filterExpression = newFilterExpression

    def getRecommendationEngineId(self):
        return self.recommendationEngineId

    def setRecommendationEngineId(self, newRecommendationEngineId):
        self.recommendationEngineId = newRecommendationEngineId

    def getEnrichments(self):
        return self.enrichments

    def setEnrichments(self, newEnrichments):
        self.enrichments = newEnrichments


# @package Kaltura
# @subpackage Client
class KalturaExternalChannelProfileListResponse(KalturaListResponse):
    """External channel profiles"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # External channel profiles
        # @var array of KalturaExternalChannelProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaExternalChannelProfile), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExternalChannelProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaExternalChannelProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaRecommendationProfile(KalturaObjectBase):
    """PaymentGW"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            recommendationEngineSettings=NotImplemented,
            externalIdentifier=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaObjectBase.__init__(self)

        # recommendation engine id
        # @var int
        # @readonly
        self.id = id

        # recommendation engine name
        # @var string
        self.name = name

        # recommendation engine is active status
        # @var bool
        self.isActive = isActive

        # recommendation engine adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # recommendation engine extra parameters
        # @var map
        self.recommendationEngineSettings = recommendationEngineSettings

        # recommendation engine external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Shared Secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'recommendationEngineSettings': (KalturaObjectFactory.create, map), 
        'externalIdentifier': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecommendationProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRecommendationProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addObjectIfDefined("recommendationEngineSettings", self.recommendationEngineSettings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getRecommendationEngineSettings(self):
        return self.recommendationEngineSettings

    def setRecommendationEngineSettings(self, newRecommendationEngineSettings):
        self.recommendationEngineSettings = newRecommendationEngineSettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getSharedSecret(self):
        return self.sharedSecret


# @package Kaltura
# @subpackage Client
class KalturaRecommendationProfileListResponse(KalturaListResponse):
    """List of recommendation profiles."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Recommendation profiles list
        # @var array of KalturaRecommendationProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaRecommendationProfile), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecommendationProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRecommendationProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaRegistrySettings(KalturaObjectBase):
    def __init__(self,
            key=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Permission item identifier
        # @var string
        self.key = key

        # Permission item name
        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'key': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegistrySettings.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRegistrySettings")
        kparams.addStringIfDefined("key", self.key)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaRegistrySettingsListResponse(KalturaListResponse):
    """List of registry settings."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Registry settings list
        # @var array of KalturaRegistrySettings
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaRegistrySettings), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegistrySettingsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRegistrySettingsListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentMethod(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            paymentGatewayId=NotImplemented,
            name=NotImplemented,
            allowMultiInstance=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Household payment method identifier (internal)
        # @var int
        # @readonly
        self.id = id

        # Payment-gateway identifier
        # @var int
        self.paymentGatewayId = paymentGatewayId

        # Payment method name
        # @var string
        self.name = name

        # Indicates whether the payment method allow multiple instances
        # @var bool
        self.allowMultiInstance = allowMultiInstance


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'paymentGatewayId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'allowMultiInstance': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPaymentMethod.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPaymentMethod")
        kparams.addIntIfDefined("paymentGatewayId", self.paymentGatewayId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("allowMultiInstance", self.allowMultiInstance)
        return kparams

    def getId(self):
        return self.id

    def getPaymentGatewayId(self):
        return self.paymentGatewayId

    def setPaymentGatewayId(self, newPaymentGatewayId):
        self.paymentGatewayId = newPaymentGatewayId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getAllowMultiInstance(self):
        return self.allowMultiInstance

    def setAllowMultiInstance(self, newAllowMultiInstance):
        self.allowMultiInstance = newAllowMultiInstance


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentMethodListResponse(KalturaListResponse):
    """List of household payment methods."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaHouseholdPaymentMethod
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaHouseholdPaymentMethod), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPaymentMethodListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPaymentMethodListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            paymentGatewayId=NotImplemented,
            name=NotImplemented,
            allowMultiInstance=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Payment method identifier (internal)
        # @var int
        # @readonly
        self.id = id

        # Payment gateway identifier (internal)
        # @var int
        self.paymentGatewayId = paymentGatewayId

        # Payment method name
        # @var string
        self.name = name

        # Indicates whether the payment method allow multiple instances
        # @var bool
        self.allowMultiInstance = allowMultiInstance


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'paymentGatewayId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'allowMultiInstance': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentMethodProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPaymentMethodProfile")
        kparams.addIntIfDefined("paymentGatewayId", self.paymentGatewayId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("allowMultiInstance", self.allowMultiInstance)
        return kparams

    def getId(self):
        return self.id

    def getPaymentGatewayId(self):
        return self.paymentGatewayId

    def setPaymentGatewayId(self, newPaymentGatewayId):
        self.paymentGatewayId = newPaymentGatewayId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getAllowMultiInstance(self):
        return self.allowMultiInstance

    def setAllowMultiInstance(self, newAllowMultiInstance):
        self.allowMultiInstance = newAllowMultiInstance


# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfileListResponse(KalturaListResponse):
    """List of payment method profiles."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Payment method profiles list
        # @var array of KalturaPaymentMethodProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPaymentMethodProfile), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentMethodProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPaymentMethodProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPrice(KalturaObjectBase):
    """Price"""

    def __init__(self,
            amount=NotImplemented,
            currency=NotImplemented,
            currencySign=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Price
        # @var float
        self.amount = amount

        # Currency
        # @var string
        self.currency = currency

        # Currency Sign
        # @var string
        self.currencySign = currencySign


    PROPERTY_LOADERS = {
        'amount': getXmlNodeFloat, 
        'currency': getXmlNodeText, 
        'currencySign': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPrice")
        kparams.addFloatIfDefined("amount", self.amount)
        kparams.addStringIfDefined("currency", self.currency)
        kparams.addStringIfDefined("currencySign", self.currencySign)
        return kparams

    def getAmount(self):
        return self.amount

    def setAmount(self, newAmount):
        self.amount = newAmount

    def getCurrency(self):
        return self.currency

    def setCurrency(self, newCurrency):
        self.currency = newCurrency

    def getCurrencySign(self):
        return self.currencySign

    def setCurrencySign(self, newCurrencySign):
        self.currencySign = newCurrencySign


# @package Kaltura
# @subpackage Client
class KalturaProductPrice(KalturaObjectBase):
    def __init__(self,
            productId=NotImplemented,
            productType=NotImplemented,
            price=NotImplemented,
            purchaseStatus=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Product identifier
        # @var string
        self.productId = productId

        # Product Type
        # @var KalturaTransactionType
        self.productType = productType

        # Product price
        # @var KalturaPrice
        self.price = price

        # Product purchase status
        # @var KalturaPurchaseStatus
        self.purchaseStatus = purchaseStatus


    PROPERTY_LOADERS = {
        'productId': getXmlNodeText, 
        'productType': (KalturaEnumsFactory.createString, "KalturaTransactionType"), 
        'price': (KalturaObjectFactory.create, KalturaPrice), 
        'purchaseStatus': (KalturaEnumsFactory.createString, "KalturaPurchaseStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaProductPrice")
        kparams.addStringIfDefined("productId", self.productId)
        kparams.addStringEnumIfDefined("productType", self.productType)
        kparams.addObjectIfDefined("price", self.price)
        kparams.addStringEnumIfDefined("purchaseStatus", self.purchaseStatus)
        return kparams

    def getProductId(self):
        return self.productId

    def setProductId(self, newProductId):
        self.productId = newProductId

    def getProductType(self):
        return self.productType

    def setProductType(self, newProductType):
        self.productType = newProductType

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getPurchaseStatus(self):
        return self.purchaseStatus

    def setPurchaseStatus(self, newPurchaseStatus):
        self.purchaseStatus = newPurchaseStatus


# @package Kaltura
# @subpackage Client
class KalturaTranslationToken(KalturaObjectBase):
    """Container for translation"""

    def __init__(self,
            language=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Language code
        # @var string
        self.language = language

        # Translated value
        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'language': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTranslationToken.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTranslationToken")
        kparams.addStringIfDefined("language", self.language)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaPpvPrice(KalturaProductPrice):
    """PPV price details"""

    def __init__(self,
            productId=NotImplemented,
            productType=NotImplemented,
            price=NotImplemented,
            purchaseStatus=NotImplemented,
            fileId=NotImplemented,
            ppvModuleId=NotImplemented,
            isSubscriptionOnly=NotImplemented,
            fullPrice=NotImplemented,
            subscriptionId=NotImplemented,
            collectionId=NotImplemented,
            prePaidId=NotImplemented,
            ppvDescriptions=NotImplemented,
            purchaseUserId=NotImplemented,
            purchasedMediaFileId=NotImplemented,
            relatedMediaFileIds=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            discountEndDate=NotImplemented,
            firstDeviceName=NotImplemented,
            isInCancelationPeriod=NotImplemented,
            ppvProductCode=NotImplemented):
        KalturaProductPrice.__init__(self,
            productId,
            productType,
            price,
            purchaseStatus)

        # Media file identifier
        # @var int
        self.fileId = fileId

        # The associated PPV module identifier
        # @var string
        self.ppvModuleId = ppvModuleId

        # Denotes whether this object is available only as part of a subscription or can be sold separately
        # @var bool
        self.isSubscriptionOnly = isSubscriptionOnly

        # The full price of the item (with no discounts)
        # @var KalturaPrice
        self.fullPrice = fullPrice

        # The identifier of the relevant subscription
        # @var string
        self.subscriptionId = subscriptionId

        # The identifier of the relevant collection
        # @var string
        self.collectionId = collectionId

        # The identifier of the relevant pre paid
        # @var string
        self.prePaidId = prePaidId

        # A list of the descriptions of the PPV module on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.ppvDescriptions = ppvDescriptions

        # If the item already purchased - the identifier of the user (in the household) who purchased this item
        # @var string
        self.purchaseUserId = purchaseUserId

        # If the item already purchased - the identifier of the purchased file
        # @var int
        self.purchasedMediaFileId = purchasedMediaFileId

        # Related media files identifiers (different types)
        # @var array of KalturaIntegerValue
        self.relatedMediaFileIds = relatedMediaFileIds

        # If the item already purchased - since when the user can start watching the item
        # @var int
        self.startDate = startDate

        # If the item already purchased - until when the user can watch the item
        # @var int
        self.endDate = endDate

        # Discount end date
        # @var int
        self.discountEndDate = discountEndDate

        # If the item already purchased and played - the name of the device on which it was first played
        # @var string
        self.firstDeviceName = firstDeviceName

        # If waiver period is enabled - donates whether the user is still in the cancelation window
        # @var bool
        self.isInCancelationPeriod = isInCancelationPeriod

        # The PPV product code
        # @var string
        self.ppvProductCode = ppvProductCode


    PROPERTY_LOADERS = {
        'fileId': getXmlNodeInt, 
        'ppvModuleId': getXmlNodeText, 
        'isSubscriptionOnly': getXmlNodeBool, 
        'fullPrice': (KalturaObjectFactory.create, KalturaPrice), 
        'subscriptionId': getXmlNodeText, 
        'collectionId': getXmlNodeText, 
        'prePaidId': getXmlNodeText, 
        'ppvDescriptions': (KalturaObjectFactory.createArray, KalturaTranslationToken), 
        'purchaseUserId': getXmlNodeText, 
        'purchasedMediaFileId': getXmlNodeInt, 
        'relatedMediaFileIds': (KalturaObjectFactory.createArray, KalturaIntegerValue), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'discountEndDate': getXmlNodeInt, 
        'firstDeviceName': getXmlNodeText, 
        'isInCancelationPeriod': getXmlNodeBool, 
        'ppvProductCode': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaProductPrice.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPpvPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaProductPrice.toParams(self)
        kparams.put("objectType", "KalturaPpvPrice")
        kparams.addIntIfDefined("fileId", self.fileId)
        kparams.addStringIfDefined("ppvModuleId", self.ppvModuleId)
        kparams.addBoolIfDefined("isSubscriptionOnly", self.isSubscriptionOnly)
        kparams.addObjectIfDefined("fullPrice", self.fullPrice)
        kparams.addStringIfDefined("subscriptionId", self.subscriptionId)
        kparams.addStringIfDefined("collectionId", self.collectionId)
        kparams.addStringIfDefined("prePaidId", self.prePaidId)
        kparams.addArrayIfDefined("ppvDescriptions", self.ppvDescriptions)
        kparams.addStringIfDefined("purchaseUserId", self.purchaseUserId)
        kparams.addIntIfDefined("purchasedMediaFileId", self.purchasedMediaFileId)
        kparams.addArrayIfDefined("relatedMediaFileIds", self.relatedMediaFileIds)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addIntIfDefined("discountEndDate", self.discountEndDate)
        kparams.addStringIfDefined("firstDeviceName", self.firstDeviceName)
        kparams.addBoolIfDefined("isInCancelationPeriod", self.isInCancelationPeriod)
        kparams.addStringIfDefined("ppvProductCode", self.ppvProductCode)
        return kparams

    def getFileId(self):
        return self.fileId

    def setFileId(self, newFileId):
        self.fileId = newFileId

    def getPpvModuleId(self):
        return self.ppvModuleId

    def setPpvModuleId(self, newPpvModuleId):
        self.ppvModuleId = newPpvModuleId

    def getIsSubscriptionOnly(self):
        return self.isSubscriptionOnly

    def setIsSubscriptionOnly(self, newIsSubscriptionOnly):
        self.isSubscriptionOnly = newIsSubscriptionOnly

    def getFullPrice(self):
        return self.fullPrice

    def setFullPrice(self, newFullPrice):
        self.fullPrice = newFullPrice

    def getSubscriptionId(self):
        return self.subscriptionId

    def setSubscriptionId(self, newSubscriptionId):
        self.subscriptionId = newSubscriptionId

    def getCollectionId(self):
        return self.collectionId

    def setCollectionId(self, newCollectionId):
        self.collectionId = newCollectionId

    def getPrePaidId(self):
        return self.prePaidId

    def setPrePaidId(self, newPrePaidId):
        self.prePaidId = newPrePaidId

    def getPpvDescriptions(self):
        return self.ppvDescriptions

    def setPpvDescriptions(self, newPpvDescriptions):
        self.ppvDescriptions = newPpvDescriptions

    def getPurchaseUserId(self):
        return self.purchaseUserId

    def setPurchaseUserId(self, newPurchaseUserId):
        self.purchaseUserId = newPurchaseUserId

    def getPurchasedMediaFileId(self):
        return self.purchasedMediaFileId

    def setPurchasedMediaFileId(self, newPurchasedMediaFileId):
        self.purchasedMediaFileId = newPurchasedMediaFileId

    def getRelatedMediaFileIds(self):
        return self.relatedMediaFileIds

    def setRelatedMediaFileIds(self, newRelatedMediaFileIds):
        self.relatedMediaFileIds = newRelatedMediaFileIds

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getDiscountEndDate(self):
        return self.discountEndDate

    def setDiscountEndDate(self, newDiscountEndDate):
        self.discountEndDate = newDiscountEndDate

    def getFirstDeviceName(self):
        return self.firstDeviceName

    def setFirstDeviceName(self, newFirstDeviceName):
        self.firstDeviceName = newFirstDeviceName

    def getIsInCancelationPeriod(self):
        return self.isInCancelationPeriod

    def setIsInCancelationPeriod(self, newIsInCancelationPeriod):
        self.isInCancelationPeriod = newIsInCancelationPeriod

    def getPpvProductCode(self):
        return self.ppvProductCode

    def setPpvProductCode(self, newPpvProductCode):
        self.ppvProductCode = newPpvProductCode


# @package Kaltura
# @subpackage Client
class KalturaPPVItemPriceDetails(KalturaObjectBase):
    """PPV item price details"""

    def __init__(self,
            ppvModuleId=NotImplemented,
            isSubscriptionOnly=NotImplemented,
            price=NotImplemented,
            fullPrice=NotImplemented,
            purchaseStatus=NotImplemented,
            subscriptionId=NotImplemented,
            collectionId=NotImplemented,
            prePaidId=NotImplemented,
            ppvDescriptions=NotImplemented,
            purchaseUserId=NotImplemented,
            purchasedMediaFileId=NotImplemented,
            relatedMediaFileIds=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            discountEndDate=NotImplemented,
            firstDeviceName=NotImplemented,
            isInCancelationPeriod=NotImplemented,
            ppvProductCode=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The associated PPV module identifier
        # @var string
        self.ppvModuleId = ppvModuleId

        # Denotes whether this object is available only as part of a subscription or can be sold separately
        # @var bool
        self.isSubscriptionOnly = isSubscriptionOnly

        # The calculated price of the item after discounts (as part of a purchased subscription by the user or by using a coupon)
        # @var KalturaPrice
        self.price = price

        # The full price of the item (with no discounts)
        # @var KalturaPrice
        self.fullPrice = fullPrice

        # Subscription purchase status
        # @var KalturaPurchaseStatus
        self.purchaseStatus = purchaseStatus

        # The identifier of the relevant subscription
        # @var string
        self.subscriptionId = subscriptionId

        # The identifier of the relevant collection
        # @var string
        self.collectionId = collectionId

        # The identifier of the relevant pre paid
        # @var string
        self.prePaidId = prePaidId

        # A list of the descriptions of the PPV module on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.ppvDescriptions = ppvDescriptions

        # If the item already purchased - the identifier of the user (in the household) who purchased this item
        # @var string
        self.purchaseUserId = purchaseUserId

        # If the item already purchased - the identifier of the purchased file
        # @var int
        self.purchasedMediaFileId = purchasedMediaFileId

        # Related media files identifiers (different types)
        # @var array of KalturaIntegerValue
        self.relatedMediaFileIds = relatedMediaFileIds

        # If the item already purchased - since when the user can start watching the item
        # @var int
        self.startDate = startDate

        # If the item already purchased - until when the user can watch the item
        # @var int
        self.endDate = endDate

        # Discount end date
        # @var int
        self.discountEndDate = discountEndDate

        # If the item already purchased and played - the name of the device on which it was first played
        # @var string
        self.firstDeviceName = firstDeviceName

        # If waiver period is enabled - donates whether the user is still in the cancelation window
        # @var bool
        self.isInCancelationPeriod = isInCancelationPeriod

        # The PPV product code
        # @var string
        self.ppvProductCode = ppvProductCode


    PROPERTY_LOADERS = {
        'ppvModuleId': getXmlNodeText, 
        'isSubscriptionOnly': getXmlNodeBool, 
        'price': (KalturaObjectFactory.create, KalturaPrice), 
        'fullPrice': (KalturaObjectFactory.create, KalturaPrice), 
        'purchaseStatus': (KalturaEnumsFactory.createString, "KalturaPurchaseStatus"), 
        'subscriptionId': getXmlNodeText, 
        'collectionId': getXmlNodeText, 
        'prePaidId': getXmlNodeText, 
        'ppvDescriptions': (KalturaObjectFactory.createArray, KalturaTranslationToken), 
        'purchaseUserId': getXmlNodeText, 
        'purchasedMediaFileId': getXmlNodeInt, 
        'relatedMediaFileIds': (KalturaObjectFactory.createArray, KalturaIntegerValue), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'discountEndDate': getXmlNodeInt, 
        'firstDeviceName': getXmlNodeText, 
        'isInCancelationPeriod': getXmlNodeBool, 
        'ppvProductCode': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPPVItemPriceDetails.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPPVItemPriceDetails")
        kparams.addStringIfDefined("ppvModuleId", self.ppvModuleId)
        kparams.addBoolIfDefined("isSubscriptionOnly", self.isSubscriptionOnly)
        kparams.addObjectIfDefined("price", self.price)
        kparams.addObjectIfDefined("fullPrice", self.fullPrice)
        kparams.addStringEnumIfDefined("purchaseStatus", self.purchaseStatus)
        kparams.addStringIfDefined("subscriptionId", self.subscriptionId)
        kparams.addStringIfDefined("collectionId", self.collectionId)
        kparams.addStringIfDefined("prePaidId", self.prePaidId)
        kparams.addArrayIfDefined("ppvDescriptions", self.ppvDescriptions)
        kparams.addStringIfDefined("purchaseUserId", self.purchaseUserId)
        kparams.addIntIfDefined("purchasedMediaFileId", self.purchasedMediaFileId)
        kparams.addArrayIfDefined("relatedMediaFileIds", self.relatedMediaFileIds)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addIntIfDefined("discountEndDate", self.discountEndDate)
        kparams.addStringIfDefined("firstDeviceName", self.firstDeviceName)
        kparams.addBoolIfDefined("isInCancelationPeriod", self.isInCancelationPeriod)
        kparams.addStringIfDefined("ppvProductCode", self.ppvProductCode)
        return kparams

    def getPpvModuleId(self):
        return self.ppvModuleId

    def setPpvModuleId(self, newPpvModuleId):
        self.ppvModuleId = newPpvModuleId

    def getIsSubscriptionOnly(self):
        return self.isSubscriptionOnly

    def setIsSubscriptionOnly(self, newIsSubscriptionOnly):
        self.isSubscriptionOnly = newIsSubscriptionOnly

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getFullPrice(self):
        return self.fullPrice

    def setFullPrice(self, newFullPrice):
        self.fullPrice = newFullPrice

    def getPurchaseStatus(self):
        return self.purchaseStatus

    def setPurchaseStatus(self, newPurchaseStatus):
        self.purchaseStatus = newPurchaseStatus

    def getSubscriptionId(self):
        return self.subscriptionId

    def setSubscriptionId(self, newSubscriptionId):
        self.subscriptionId = newSubscriptionId

    def getCollectionId(self):
        return self.collectionId

    def setCollectionId(self, newCollectionId):
        self.collectionId = newCollectionId

    def getPrePaidId(self):
        return self.prePaidId

    def setPrePaidId(self, newPrePaidId):
        self.prePaidId = newPrePaidId

    def getPpvDescriptions(self):
        return self.ppvDescriptions

    def setPpvDescriptions(self, newPpvDescriptions):
        self.ppvDescriptions = newPpvDescriptions

    def getPurchaseUserId(self):
        return self.purchaseUserId

    def setPurchaseUserId(self, newPurchaseUserId):
        self.purchaseUserId = newPurchaseUserId

    def getPurchasedMediaFileId(self):
        return self.purchasedMediaFileId

    def setPurchasedMediaFileId(self, newPurchasedMediaFileId):
        self.purchasedMediaFileId = newPurchasedMediaFileId

    def getRelatedMediaFileIds(self):
        return self.relatedMediaFileIds

    def setRelatedMediaFileIds(self, newRelatedMediaFileIds):
        self.relatedMediaFileIds = newRelatedMediaFileIds

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getDiscountEndDate(self):
        return self.discountEndDate

    def setDiscountEndDate(self, newDiscountEndDate):
        self.discountEndDate = newDiscountEndDate

    def getFirstDeviceName(self):
        return self.firstDeviceName

    def setFirstDeviceName(self, newFirstDeviceName):
        self.firstDeviceName = newFirstDeviceName

    def getIsInCancelationPeriod(self):
        return self.isInCancelationPeriod

    def setIsInCancelationPeriod(self, newIsInCancelationPeriod):
        self.isInCancelationPeriod = newIsInCancelationPeriod

    def getPpvProductCode(self):
        return self.ppvProductCode

    def setPpvProductCode(self, newPpvProductCode):
        self.ppvProductCode = newPpvProductCode


# @package Kaltura
# @subpackage Client
class KalturaItemPrice(KalturaProductPrice):
    """PPV price details"""

    def __init__(self,
            productId=NotImplemented,
            productType=NotImplemented,
            price=NotImplemented,
            purchaseStatus=NotImplemented,
            fileId=NotImplemented,
            ppvPriceDetails=NotImplemented):
        KalturaProductPrice.__init__(self,
            productId,
            productType,
            price,
            purchaseStatus)

        # Media file identifier
        # @var int
        self.fileId = fileId

        # PPV price details
        # @var array of KalturaPPVItemPriceDetails
        self.ppvPriceDetails = ppvPriceDetails


    PROPERTY_LOADERS = {
        'fileId': getXmlNodeInt, 
        'ppvPriceDetails': (KalturaObjectFactory.createArray, KalturaPPVItemPriceDetails), 
    }

    def fromXml(self, node):
        KalturaProductPrice.fromXml(self, node)
        self.fromXmlImpl(node, KalturaItemPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaProductPrice.toParams(self)
        kparams.put("objectType", "KalturaItemPrice")
        kparams.addIntIfDefined("fileId", self.fileId)
        kparams.addArrayIfDefined("ppvPriceDetails", self.ppvPriceDetails)
        return kparams

    def getFileId(self):
        return self.fileId

    def setFileId(self, newFileId):
        self.fileId = newFileId

    def getPpvPriceDetails(self):
        return self.ppvPriceDetails

    def setPpvPriceDetails(self, newPpvPriceDetails):
        self.ppvPriceDetails = newPpvPriceDetails


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionPrice(KalturaProductPrice):
    """Subscription price details"""

    def __init__(self,
            productId=NotImplemented,
            productType=NotImplemented,
            price=NotImplemented,
            purchaseStatus=NotImplemented):
        KalturaProductPrice.__init__(self,
            productId,
            productType,
            price,
            purchaseStatus)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaProductPrice.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaProductPrice.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionPrice")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentGateway(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isDefault=NotImplemented,
            selectedBy=NotImplemented):
        KalturaObjectBase.__init__(self)

        # payment gateway id
        # @var int
        # @readonly
        self.id = id

        # payment gateway name
        # @var string
        self.name = name

        # Payment gateway default (true/false)
        # @var bool
        self.isDefault = isDefault

        # distinction payment gateway selected by account or household
        # @var KalturaHouseholdPaymentGatewaySelectedBy
        self.selectedBy = selectedBy


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
        'selectedBy': (KalturaEnumsFactory.createString, "KalturaHouseholdPaymentGatewaySelectedBy"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPaymentGateway.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPaymentGateway")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        kparams.addStringEnumIfDefined("selectedBy", self.selectedBy)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getSelectedBy(self):
        return self.selectedBy

    def setSelectedBy(self, newSelectedBy):
        self.selectedBy = newSelectedBy


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentGatewayListResponse(KalturaListResponse):
    """List of household payment gateways."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaHouseholdPaymentGateway
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaHouseholdPaymentGateway), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPaymentGatewayListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPaymentGatewayListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPaymentGatewayBaseProfile(KalturaObjectBase):
    """Payment gateway base profile"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isDefault=NotImplemented,
            selectedBy=NotImplemented):
        KalturaObjectBase.__init__(self)

        # payment gateway id
        # @var int
        # @readonly
        self.id = id

        # payment gateway name
        # @var string
        self.name = name

        # Payment gateway default (true/false)
        # @var bool
        self.isDefault = isDefault

        # distinction payment gateway selected by account or household
        # @var KalturaHouseholdPaymentGatewaySelectedBy
        self.selectedBy = selectedBy


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
        'selectedBy': (KalturaEnumsFactory.createString, "KalturaHouseholdPaymentGatewaySelectedBy"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentGatewayBaseProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPaymentGatewayBaseProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        kparams.addStringEnumIfDefined("selectedBy", self.selectedBy)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getSelectedBy(self):
        return self.selectedBy

    def setSelectedBy(self, newSelectedBy):
        self.selectedBy = newSelectedBy


# @package Kaltura
# @subpackage Client
class KalturaPaymentGatewayProfile(KalturaPaymentGatewayBaseProfile):
    """Payment gateway profile"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isDefault=NotImplemented,
            selectedBy=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            transactUrl=NotImplemented,
            statusUrl=NotImplemented,
            renewUrl=NotImplemented,
            paymentGatewayeSettings=NotImplemented,
            externalIdentifier=NotImplemented,
            pendingInterval=NotImplemented,
            pendingRetries=NotImplemented,
            sharedSecret=NotImplemented,
            renewIntervalMinutes=NotImplemented,
            renewStartMinutes=NotImplemented):
        KalturaPaymentGatewayBaseProfile.__init__(self,
            id,
            name,
            isDefault,
            selectedBy)

        # Payment gateway is active status
        # @var int
        self.isActive = isActive

        # Payment gateway adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # Payment gateway transact URL
        # @var string
        self.transactUrl = transactUrl

        # Payment gateway status URL
        # @var string
        self.statusUrl = statusUrl

        # Payment gateway renew URL
        # @var string
        self.renewUrl = renewUrl

        # Payment gateway extra parameters
        # @var map
        self.paymentGatewayeSettings = paymentGatewayeSettings

        # Payment gateway external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Pending Interval in minutes
        # @var int
        self.pendingInterval = pendingInterval

        # Pending Retries
        # @var int
        self.pendingRetries = pendingRetries

        # Shared Secret
        # @var string
        self.sharedSecret = sharedSecret

        # Renew Interval Minutes
        # @var int
        self.renewIntervalMinutes = renewIntervalMinutes

        # Renew Start Minutes
        # @var int
        self.renewStartMinutes = renewStartMinutes


    PROPERTY_LOADERS = {
        'isActive': getXmlNodeInt, 
        'adapterUrl': getXmlNodeText, 
        'transactUrl': getXmlNodeText, 
        'statusUrl': getXmlNodeText, 
        'renewUrl': getXmlNodeText, 
        'paymentGatewayeSettings': (KalturaObjectFactory.create, map), 
        'externalIdentifier': getXmlNodeText, 
        'pendingInterval': getXmlNodeInt, 
        'pendingRetries': getXmlNodeInt, 
        'sharedSecret': getXmlNodeText, 
        'renewIntervalMinutes': getXmlNodeInt, 
        'renewStartMinutes': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaPaymentGatewayBaseProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentGatewayProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPaymentGatewayBaseProfile.toParams(self)
        kparams.put("objectType", "KalturaPaymentGatewayProfile")
        kparams.addIntIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addStringIfDefined("transactUrl", self.transactUrl)
        kparams.addStringIfDefined("statusUrl", self.statusUrl)
        kparams.addStringIfDefined("renewUrl", self.renewUrl)
        kparams.addObjectIfDefined("paymentGatewayeSettings", self.paymentGatewayeSettings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        kparams.addIntIfDefined("pendingInterval", self.pendingInterval)
        kparams.addIntIfDefined("pendingRetries", self.pendingRetries)
        kparams.addStringIfDefined("sharedSecret", self.sharedSecret)
        kparams.addIntIfDefined("renewIntervalMinutes", self.renewIntervalMinutes)
        kparams.addIntIfDefined("renewStartMinutes", self.renewStartMinutes)
        return kparams

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getTransactUrl(self):
        return self.transactUrl

    def setTransactUrl(self, newTransactUrl):
        self.transactUrl = newTransactUrl

    def getStatusUrl(self):
        return self.statusUrl

    def setStatusUrl(self, newStatusUrl):
        self.statusUrl = newStatusUrl

    def getRenewUrl(self):
        return self.renewUrl

    def setRenewUrl(self, newRenewUrl):
        self.renewUrl = newRenewUrl

    def getPaymentGatewayeSettings(self):
        return self.paymentGatewayeSettings

    def setPaymentGatewayeSettings(self, newPaymentGatewayeSettings):
        self.paymentGatewayeSettings = newPaymentGatewayeSettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getPendingInterval(self):
        return self.pendingInterval

    def setPendingInterval(self, newPendingInterval):
        self.pendingInterval = newPendingInterval

    def getPendingRetries(self):
        return self.pendingRetries

    def setPendingRetries(self, newPendingRetries):
        self.pendingRetries = newPendingRetries

    def getSharedSecret(self):
        return self.sharedSecret

    def setSharedSecret(self, newSharedSecret):
        self.sharedSecret = newSharedSecret

    def getRenewIntervalMinutes(self):
        return self.renewIntervalMinutes

    def setRenewIntervalMinutes(self, newRenewIntervalMinutes):
        self.renewIntervalMinutes = newRenewIntervalMinutes

    def getRenewStartMinutes(self):
        return self.renewStartMinutes

    def setRenewStartMinutes(self, newRenewStartMinutes):
        self.renewStartMinutes = newRenewStartMinutes


# @package Kaltura
# @subpackage Client
class KalturaPaymentGatewayProfileListResponse(KalturaListResponse):
    """PaymentGatewayProfile list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of payment-gateway profiles
        # @var array of KalturaPaymentGatewayProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPaymentGatewayProfile), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentGatewayProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPaymentGatewayProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaParentalRule(KalturaObjectBase):
    """Parental rule"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            order=NotImplemented,
            mediaTag=NotImplemented,
            epgTag=NotImplemented,
            blockAnonymousAccess=NotImplemented,
            ruleType=NotImplemented,
            mediaTagValues=NotImplemented,
            epgTagValues=NotImplemented,
            isDefault=NotImplemented,
            origin=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique parental rule identifier
        # @var int
        # @readonly
        self.id = id

        # Rule display name
        # @var string
        self.name = name

        # Explanatory description
        # @var string
        self.description = description

        # Rule order within the full list of rules
        # @var int
        self.order = order

        # Media asset tag ID to in which to look for corresponding trigger values
        # @var int
        self.mediaTag = mediaTag

        # EPG asset tag ID to in which to look for corresponding trigger values
        # @var int
        self.epgTag = epgTag

        # Content that correspond to this rule is not available for guests
        # @var bool
        self.blockAnonymousAccess = blockAnonymousAccess

        # Rule type – Movies, TV series or both
        # @var KalturaParentalRuleType
        self.ruleType = ruleType

        # Media tag values that trigger rule
        # @var array of KalturaStringValue
        self.mediaTagValues = mediaTagValues

        # EPG tag values that trigger rule
        # @var array of KalturaStringValue
        self.epgTagValues = epgTagValues

        # Is the rule the default rule of the account
        # @var bool
        self.isDefault = isDefault

        # Where was this rule defined account, household or user
        # @var KalturaRuleLevel
        self.origin = origin


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'order': getXmlNodeInt, 
        'mediaTag': getXmlNodeInt, 
        'epgTag': getXmlNodeInt, 
        'blockAnonymousAccess': getXmlNodeBool, 
        'ruleType': (KalturaEnumsFactory.createString, "KalturaParentalRuleType"), 
        'mediaTagValues': (KalturaObjectFactory.createArray, KalturaStringValue), 
        'epgTagValues': (KalturaObjectFactory.createArray, KalturaStringValue), 
        'isDefault': getXmlNodeBool, 
        'origin': (KalturaEnumsFactory.createString, "KalturaRuleLevel"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaParentalRule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaParentalRule")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntIfDefined("order", self.order)
        kparams.addIntIfDefined("mediaTag", self.mediaTag)
        kparams.addIntIfDefined("epgTag", self.epgTag)
        kparams.addBoolIfDefined("blockAnonymousAccess", self.blockAnonymousAccess)
        kparams.addStringEnumIfDefined("ruleType", self.ruleType)
        kparams.addArrayIfDefined("mediaTagValues", self.mediaTagValues)
        kparams.addArrayIfDefined("epgTagValues", self.epgTagValues)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        kparams.addStringEnumIfDefined("origin", self.origin)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getOrder(self):
        return self.order

    def setOrder(self, newOrder):
        self.order = newOrder

    def getMediaTag(self):
        return self.mediaTag

    def setMediaTag(self, newMediaTag):
        self.mediaTag = newMediaTag

    def getEpgTag(self):
        return self.epgTag

    def setEpgTag(self, newEpgTag):
        self.epgTag = newEpgTag

    def getBlockAnonymousAccess(self):
        return self.blockAnonymousAccess

    def setBlockAnonymousAccess(self, newBlockAnonymousAccess):
        self.blockAnonymousAccess = newBlockAnonymousAccess

    def getRuleType(self):
        return self.ruleType

    def setRuleType(self, newRuleType):
        self.ruleType = newRuleType

    def getMediaTagValues(self):
        return self.mediaTagValues

    def setMediaTagValues(self, newMediaTagValues):
        self.mediaTagValues = newMediaTagValues

    def getEpgTagValues(self):
        return self.epgTagValues

    def setEpgTagValues(self, newEpgTagValues):
        self.epgTagValues = newEpgTagValues

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getOrigin(self):
        return self.origin

    def setOrigin(self, newOrigin):
        self.origin = newOrigin


# @package Kaltura
# @subpackage Client
class KalturaParentalRuleListResponse(KalturaListResponse):
    """ParentalRules list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of parental rules
        # @var array of KalturaParentalRule
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaParentalRule), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaParentalRuleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaParentalRuleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaRecording(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            status=NotImplemented,
            assetId=NotImplemented,
            type=NotImplemented,
            viewableUntilDate=NotImplemented,
            isProtected=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Kaltura unique ID representing the recording identifier
        # @var int
        # @readonly
        self.id = id

        # Recording state: scheduled/recording/recorded/canceled/failed/does_not_exists/deleted
        # @var KalturaRecordingStatus
        # @readonly
        self.status = status

        # Kaltura unique ID representing the program identifier
        # @var int
        self.assetId = assetId

        # Recording Type: single/season/series
        # @var KalturaRecordingType
        # @readonly
        self.type = type

        # Specifies until when the recording is available for viewing. Date and time represented as epoch.
        # @var int
        # @readonly
        self.viewableUntilDate = viewableUntilDate

        # Specifies whether or not the recording is protected
        # @var bool
        # @readonly
        self.isProtected = isProtected

        # Specifies when was the recording created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the recording last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createString, "KalturaRecordingStatus"), 
        'assetId': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaRecordingType"), 
        'viewableUntilDate': getXmlNodeInt, 
        'isProtected': getXmlNodeBool, 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecording.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRecording")
        kparams.addIntIfDefined("assetId", self.assetId)
        return kparams

    def getId(self):
        return self.id

    def getStatus(self):
        return self.status

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getType(self):
        return self.type

    def getViewableUntilDate(self):
        return self.viewableUntilDate

    def getIsProtected(self):
        return self.isProtected

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate


# @package Kaltura
# @subpackage Client
class KalturaRecordingListResponse(KalturaListResponse):
    """Recordings info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Recordings
        # @var array of KalturaRecording
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaRecording), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecordingListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRecordingListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaBillingTransaction(KalturaObjectBase):
    """Billing Transaction"""

    def __init__(self,
            recieptCode=NotImplemented,
            purchasedItemName=NotImplemented,
            purchasedItemCode=NotImplemented,
            itemType=NotImplemented,
            billingAction=NotImplemented,
            price=NotImplemented,
            actionDate=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            paymentMethod=NotImplemented,
            paymentMethodExtraDetails=NotImplemented,
            isRecurring=NotImplemented,
            billingProviderRef=NotImplemented,
            purchaseId=NotImplemented,
            remarks=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Reciept Code
        # @var string
        # @readonly
        self.recieptCode = recieptCode

        # Purchased Item Name
        # @var string
        # @readonly
        self.purchasedItemName = purchasedItemName

        # Purchased Item Code
        # @var string
        # @readonly
        self.purchasedItemCode = purchasedItemCode

        # Item Type
        # @var KalturaBillingItemsType
        # @readonly
        self.itemType = itemType

        # Billing Action
        # @var KalturaBillingAction
        # @readonly
        self.billingAction = billingAction

        # price
        # @var KalturaPrice
        # @readonly
        self.price = price

        # Action Date
        # @var int
        # @readonly
        self.actionDate = actionDate

        # Start Date
        # @var int
        # @readonly
        self.startDate = startDate

        # End Date
        # @var int
        # @readonly
        self.endDate = endDate

        # Payment Method
        # @var KalturaPaymentMethodType
        # @readonly
        self.paymentMethod = paymentMethod

        # Payment Method Extra Details
        # @var string
        # @readonly
        self.paymentMethodExtraDetails = paymentMethodExtraDetails

        # Is Recurring
        # @var bool
        # @readonly
        self.isRecurring = isRecurring

        # Billing Provider Ref
        # @var int
        # @readonly
        self.billingProviderRef = billingProviderRef

        # Purchase ID
        # @var int
        # @readonly
        self.purchaseId = purchaseId

        # Remarks
        # @var string
        # @readonly
        self.remarks = remarks


    PROPERTY_LOADERS = {
        'recieptCode': getXmlNodeText, 
        'purchasedItemName': getXmlNodeText, 
        'purchasedItemCode': getXmlNodeText, 
        'itemType': (KalturaEnumsFactory.createString, "KalturaBillingItemsType"), 
        'billingAction': (KalturaEnumsFactory.createString, "KalturaBillingAction"), 
        'price': (KalturaObjectFactory.create, KalturaPrice), 
        'actionDate': getXmlNodeInt, 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'paymentMethod': (KalturaEnumsFactory.createString, "KalturaPaymentMethodType"), 
        'paymentMethodExtraDetails': getXmlNodeText, 
        'isRecurring': getXmlNodeBool, 
        'billingProviderRef': getXmlNodeInt, 
        'purchaseId': getXmlNodeInt, 
        'remarks': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBillingTransaction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBillingTransaction")
        return kparams

    def getRecieptCode(self):
        return self.recieptCode

    def getPurchasedItemName(self):
        return self.purchasedItemName

    def getPurchasedItemCode(self):
        return self.purchasedItemCode

    def getItemType(self):
        return self.itemType

    def getBillingAction(self):
        return self.billingAction

    def getPrice(self):
        return self.price

    def getActionDate(self):
        return self.actionDate

    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getPaymentMethod(self):
        return self.paymentMethod

    def getPaymentMethodExtraDetails(self):
        return self.paymentMethodExtraDetails

    def getIsRecurring(self):
        return self.isRecurring

    def getBillingProviderRef(self):
        return self.billingProviderRef

    def getPurchaseId(self):
        return self.purchaseId

    def getRemarks(self):
        return self.remarks


# @package Kaltura
# @subpackage Client
class KalturaBillingTransactionListResponse(KalturaListResponse):
    """Billing Transactions"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Transactions
        # @var array of KalturaBillingTransaction
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBillingTransaction), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBillingTransactionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaBillingTransactionListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPermissionItem(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Permission item identifier
        # @var int
        # @readonly
        self.id = id

        # Permission item name
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermissionItem")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaPermission(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            permissionItems=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Permission identifier
        # @var int
        # @readonly
        self.id = id

        # Permission name
        # @var string
        self.name = name

        # List of permission items associated with the permission
        # @var array of KalturaPermissionItem
        self.permissionItems = permissionItems


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'permissionItems': (KalturaObjectFactory.createArray, KalturaPermissionItem), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPermission.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPermission")
        kparams.addStringIfDefined("name", self.name)
        kparams.addArrayIfDefined("permissionItems", self.permissionItems)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPermissionItems(self):
        return self.permissionItems

    def setPermissionItems(self, newPermissionItems):
        self.permissionItems = newPermissionItems


# @package Kaltura
# @subpackage Client
class KalturaUserRole(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            permissions=NotImplemented):
        KalturaObjectBase.__init__(self)

        # User role identifier
        # @var int
        # @readonly
        self.id = id

        # User role name
        # @var string
        self.name = name

        # List of permissions associated with the user role
        # @var array of KalturaPermission
        self.permissions = permissions


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'permissions': (KalturaObjectFactory.createArray, KalturaPermission), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRole.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserRole")
        kparams.addStringIfDefined("name", self.name)
        kparams.addArrayIfDefined("permissions", self.permissions)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPermissions(self):
        return self.permissions

    def setPermissions(self, newPermissions):
        self.permissions = newPermissions


# @package Kaltura
# @subpackage Client
class KalturaUserRoleListResponse(KalturaListResponse):
    """User-roles list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of generic rules
        # @var array of KalturaUserRole
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUserRole), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaUserRoleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaGroupPermission(KalturaPermission):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            permissionItems=NotImplemented,
            group=NotImplemented):
        KalturaPermission.__init__(self,
            id,
            name,
            permissionItems)

        # Permission identifier
        # @var string
        self.group = group


    PROPERTY_LOADERS = {
        'group': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPermission.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGroupPermission.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermission.toParams(self)
        kparams.put("objectType", "KalturaGroupPermission")
        kparams.addStringIfDefined("group", self.group)
        return kparams

    def getGroup(self):
        return self.group

    def setGroup(self, newGroup):
        self.group = newGroup


# @package Kaltura
# @subpackage Client
class KalturaApiArgumentPermissionItem(KalturaPermissionItem):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            service=NotImplemented,
            action=NotImplemented,
            parameter=NotImplemented):
        KalturaPermissionItem.__init__(self,
            id,
            name)

        # API service name
        # @var string
        self.service = service

        # API action name
        # @var string
        self.action = action

        # API parameter name
        # @var string
        self.parameter = parameter


    PROPERTY_LOADERS = {
        'service': getXmlNodeText, 
        'action': getXmlNodeText, 
        'parameter': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPermissionItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiArgumentPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItem.toParams(self)
        kparams.put("objectType", "KalturaApiArgumentPermissionItem")
        kparams.addStringIfDefined("service", self.service)
        kparams.addStringIfDefined("action", self.action)
        kparams.addStringIfDefined("parameter", self.parameter)
        return kparams

    def getService(self):
        return self.service

    def setService(self, newService):
        self.service = newService

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getParameter(self):
        return self.parameter

    def setParameter(self, newParameter):
        self.parameter = newParameter


# @package Kaltura
# @subpackage Client
class KalturaApiParameterPermissionItem(KalturaPermissionItem):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            object=NotImplemented,
            parameter=NotImplemented,
            action=NotImplemented):
        KalturaPermissionItem.__init__(self,
            id,
            name)

        # API object name
        # @var string
        self.object = object

        # API parameter name
        # @var string
        self.parameter = parameter

        # API action type
        # @var KalturaApiParameterPermissionItemAction
        self.action = action


    PROPERTY_LOADERS = {
        'object': getXmlNodeText, 
        'parameter': getXmlNodeText, 
        'action': (KalturaEnumsFactory.createString, "KalturaApiParameterPermissionItemAction"), 
    }

    def fromXml(self, node):
        KalturaPermissionItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiParameterPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItem.toParams(self)
        kparams.put("objectType", "KalturaApiParameterPermissionItem")
        kparams.addStringIfDefined("object", self.object)
        kparams.addStringIfDefined("parameter", self.parameter)
        kparams.addStringEnumIfDefined("action", self.action)
        return kparams

    def getObject(self):
        return self.object

    def setObject(self, newObject):
        self.object = newObject

    def getParameter(self):
        return self.parameter

    def setParameter(self, newParameter):
        self.parameter = newParameter

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction


# @package Kaltura
# @subpackage Client
class KalturaApiActionPermissionItem(KalturaPermissionItem):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            service=NotImplemented,
            action=NotImplemented):
        KalturaPermissionItem.__init__(self,
            id,
            name)

        # API service name
        # @var string
        self.service = service

        # API action name
        # @var string
        self.action = action


    PROPERTY_LOADERS = {
        'service': getXmlNodeText, 
        'action': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPermissionItem.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiActionPermissionItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPermissionItem.toParams(self)
        kparams.put("objectType", "KalturaApiActionPermissionItem")
        kparams.addStringIfDefined("service", self.service)
        kparams.addStringIfDefined("action", self.action)
        return kparams

    def getService(self):
        return self.service

    def setService(self, newService):
        self.service = newService

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction


# @package Kaltura
# @subpackage Client
class KalturaInboxMessage(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            message=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            url=NotImplemented):
        KalturaObjectBase.__init__(self)

        # message id
        # @var string
        # @readonly
        self.id = id

        # message
        # @var string
        self.message = message

        # Status
        # @var KalturaInboxMessageStatus
        # @readonly
        self.status = status

        # Type
        # @var KalturaInboxMessageType
        self.type = type

        # Created at
        # @var int
        # @readonly
        self.createdAt = createdAt

        # url
        # @var string
        self.url = url


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'message': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createString, "KalturaInboxMessageStatus"), 
        'type': (KalturaEnumsFactory.createString, "KalturaInboxMessageType"), 
        'createdAt': getXmlNodeInt, 
        'url': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInboxMessage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaInboxMessage")
        kparams.addStringIfDefined("message", self.message)
        kparams.addStringEnumIfDefined("type", self.type)
        kparams.addStringIfDefined("url", self.url)
        return kparams

    def getId(self):
        return self.id

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage):
        self.message = newMessage

    def getStatus(self):
        return self.status

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getCreatedAt(self):
        return self.createdAt

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl


# @package Kaltura
# @subpackage Client
class KalturaInboxMessageListResponse(KalturaListResponse):
    """List of inbox message."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaInboxMessage
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaInboxMessage), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInboxMessageListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaInboxMessageListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaFollowDataBase(KalturaObjectBase):
    def __init__(self,
            announcementId=NotImplemented,
            status=NotImplemented,
            title=NotImplemented,
            timestamp=NotImplemented,
            followPhrase=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Announcement Id
        # @var int
        # @readonly
        self.announcementId = announcementId

        # Status
        # @var int
        # @readonly
        self.status = status

        # Title
        # @var string
        # @readonly
        self.title = title

        # Timestamp
        # @var int
        # @readonly
        self.timestamp = timestamp

        # Follow Phrase
        # @var string
        # @readonly
        self.followPhrase = followPhrase


    PROPERTY_LOADERS = {
        'announcementId': getXmlNodeInt, 
        'status': getXmlNodeInt, 
        'title': getXmlNodeText, 
        'timestamp': getXmlNodeInt, 
        'followPhrase': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFollowDataBase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFollowDataBase")
        return kparams

    def getAnnouncementId(self):
        return self.announcementId

    def getStatus(self):
        return self.status

    def getTitle(self):
        return self.title

    def getTimestamp(self):
        return self.timestamp

    def getFollowPhrase(self):
        return self.followPhrase


# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeries(KalturaFollowDataBase):
    def __init__(self,
            announcementId=NotImplemented,
            status=NotImplemented,
            title=NotImplemented,
            timestamp=NotImplemented,
            followPhrase=NotImplemented,
            assetId=NotImplemented):
        KalturaFollowDataBase.__init__(self,
            announcementId,
            status,
            title,
            timestamp,
            followPhrase)

        # Asset Id
        # @var int
        # @readonly
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFollowDataBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFollowTvSeries.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFollowDataBase.toParams(self)
        kparams.put("objectType", "KalturaFollowTvSeries")
        return kparams

    def getAssetId(self):
        return self.assetId


# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeriesListResponse(KalturaListResponse):
    """List of message follow data."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaFollowTvSeries
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaFollowTvSeries), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFollowTvSeriesListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaFollowTvSeriesListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAnnouncementListResponse(KalturaListResponse):
    """List of message announcements from DB."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Announcements
        # @var array of KalturaAnnouncement
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAnnouncement), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnouncementListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAnnouncementListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaFeed(KalturaObjectBase):
    def __init__(self,
            assetId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFeed")
        return kparams

    def getAssetId(self):
        return self.assetId


# @package Kaltura
# @subpackage Client
class KalturaPersonalFeed(KalturaFeed):
    def __init__(self,
            assetId=NotImplemented):
        KalturaFeed.__init__(self,
            assetId)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFeed.toParams(self)
        kparams.put("objectType", "KalturaPersonalFeed")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPersonalFeedListResponse(KalturaListResponse):
    """List of message follow data."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaPersonalFeed
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaPersonalFeed), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalFeedListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPersonalFeedListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaTopic(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            subscribersAmount=NotImplemented,
            automaticIssueNotification=NotImplemented,
            lastMessageSentDateSec=NotImplemented):
        KalturaObjectBase.__init__(self)

        # message id
        # @var string
        # @readonly
        self.id = id

        # message
        # @var string
        self.name = name

        # message
        # @var string
        self.subscribersAmount = subscribersAmount

        # automaticIssueNotification
        # @var KalturaTopicAutomaticIssueNotification
        self.automaticIssueNotification = automaticIssueNotification

        # lastMessageSentDateSec
        # @var int
        self.lastMessageSentDateSec = lastMessageSentDateSec


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'subscribersAmount': getXmlNodeText, 
        'automaticIssueNotification': (KalturaEnumsFactory.createString, "KalturaTopicAutomaticIssueNotification"), 
        'lastMessageSentDateSec': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTopic.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTopic")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("subscribersAmount", self.subscribersAmount)
        kparams.addStringEnumIfDefined("automaticIssueNotification", self.automaticIssueNotification)
        kparams.addIntIfDefined("lastMessageSentDateSec", self.lastMessageSentDateSec)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSubscribersAmount(self):
        return self.subscribersAmount

    def setSubscribersAmount(self, newSubscribersAmount):
        self.subscribersAmount = newSubscribersAmount

    def getAutomaticIssueNotification(self):
        return self.automaticIssueNotification

    def setAutomaticIssueNotification(self, newAutomaticIssueNotification):
        self.automaticIssueNotification = newAutomaticIssueNotification

    def getLastMessageSentDateSec(self):
        return self.lastMessageSentDateSec

    def setLastMessageSentDateSec(self, newLastMessageSentDateSec):
        self.lastMessageSentDateSec = newLastMessageSentDateSec


# @package Kaltura
# @subpackage Client
class KalturaTopicListResponse(KalturaListResponse):
    """List of inbox message."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaTopic
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaTopic), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTopicListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaTopicListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaProductPriceListResponse(KalturaListResponse):
    """Prices list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of prices
        # @var array of KalturaProductPrice
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaProductPrice), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductPriceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaProductPriceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaItemPriceListResponse(KalturaListResponse):
    """ItemPrice list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of item prices
        # @var array of KalturaItemPrice
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaItemPrice), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaItemPriceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaItemPriceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaBaseChannel(KalturaObjectBase):
    """Slim channel"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier for the channel
        # @var int
        # @readonly
        self.id = id

        # Channel name
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseChannel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseChannel")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaChannel(KalturaBaseChannel):
    """Channel details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            images=NotImplemented,
            assetTypes=NotImplemented,
            filterExpression=NotImplemented,
            isActive=NotImplemented,
            order=NotImplemented):
        KalturaBaseChannel.__init__(self,
            id,
            name)

        # Cannel description
        # @var string
        self.description = description

        # Channel images
        # @var array of KalturaMediaImage
        self.images = images

        # Asset types in the channel.
        #             -26 is EPG
        # @var array of KalturaIntegerValue
        self.assetTypes = assetTypes

        # Filter expression
        # @var string
        self.filterExpression = filterExpression

        # active status
        # @var bool
        self.isActive = isActive

        # Channel order
        # @var KalturaAssetOrderBy
        self.order = order


    PROPERTY_LOADERS = {
        'description': getXmlNodeText, 
        'images': (KalturaObjectFactory.createArray, KalturaMediaImage), 
        'assetTypes': (KalturaObjectFactory.createArray, KalturaIntegerValue), 
        'filterExpression': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'order': (KalturaEnumsFactory.createString, "KalturaAssetOrderBy"), 
    }

    def fromXml(self, node):
        KalturaBaseChannel.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseChannel.toParams(self)
        kparams.put("objectType", "KalturaChannel")
        kparams.addStringIfDefined("description", self.description)
        kparams.addArrayIfDefined("images", self.images)
        kparams.addArrayIfDefined("assetTypes", self.assetTypes)
        kparams.addStringIfDefined("filterExpression", self.filterExpression)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringEnumIfDefined("order", self.order)
        return kparams

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getImages(self):
        return self.images

    def setImages(self, newImages):
        self.images = newImages

    def getAssetTypes(self):
        return self.assetTypes

    def setAssetTypes(self, newAssetTypes):
        self.assetTypes = newAssetTypes

    def getFilterExpression(self):
        return self.filterExpression

    def setFilterExpression(self, newFilterExpression):
        self.filterExpression = newFilterExpression

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getOrder(self):
        return self.order

    def setOrder(self, newOrder):
        self.order = newOrder


# @package Kaltura
# @subpackage Client
class KalturaPriceDetails(KalturaObjectBase):
    """Price details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            price=NotImplemented,
            descriptions=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The price code identifier
        # @var int
        self.id = id

        # The price code name
        # @var string
        self.name = name

        # The price
        # @var KalturaPrice
        self.price = price

        # A list of the descriptions for this price on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.descriptions = descriptions


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'price': (KalturaObjectFactory.create, KalturaPrice), 
        'descriptions': (KalturaObjectFactory.createArray, KalturaTranslationToken), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPriceDetails.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPriceDetails")
        kparams.addIntIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        kparams.addObjectIfDefined("price", self.price)
        kparams.addArrayIfDefined("descriptions", self.descriptions)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getDescriptions(self):
        return self.descriptions

    def setDescriptions(self, newDescriptions):
        self.descriptions = newDescriptions


# @package Kaltura
# @subpackage Client
class KalturaDiscountModule(KalturaObjectBase):
    """Discount module"""

    def __init__(self,
            percent=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The discount percentage
        # @var float
        self.percent = percent

        # The first date the discount is available
        # @var int
        self.startDate = startDate

        # The last date the discount is available
        # @var int
        self.endDate = endDate


    PROPERTY_LOADERS = {
        'percent': getXmlNodeFloat, 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDiscountModule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDiscountModule")
        kparams.addFloatIfDefined("percent", self.percent)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        return kparams

    def getPercent(self):
        return self.percent

    def setPercent(self, newPercent):
        self.percent = newPercent

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate


# @package Kaltura
# @subpackage Client
class KalturaCouponsGroup(KalturaObjectBase):
    """Coupons group details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            descriptions=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            maxUsesNumber=NotImplemented,
            maxUsesNumberOnRenewableSub=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Coupon group identifier
        # @var string
        # @readonly
        self.id = id

        # Coupon group name
        # @var string
        self.name = name

        # A list of the descriptions of the coupon group on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.descriptions = descriptions

        # The first date the coupons in this coupons group are valid
        # @var int
        self.startDate = startDate

        # The last date the coupons in this coupons group are valid
        # @var int
        self.endDate = endDate

        # Maximum number of uses for each coupon in the group
        # @var int
        self.maxUsesNumber = maxUsesNumber

        # Maximum number of uses for each coupon in the group on a renewable subscription
        # @var int
        self.maxUsesNumberOnRenewableSub = maxUsesNumberOnRenewableSub


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'descriptions': (KalturaObjectFactory.createArray, KalturaTranslationToken), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'maxUsesNumber': getXmlNodeInt, 
        'maxUsesNumberOnRenewableSub': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCouponsGroup.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCouponsGroup")
        kparams.addStringIfDefined("name", self.name)
        kparams.addArrayIfDefined("descriptions", self.descriptions)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addIntIfDefined("maxUsesNumber", self.maxUsesNumber)
        kparams.addIntIfDefined("maxUsesNumberOnRenewableSub", self.maxUsesNumberOnRenewableSub)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescriptions(self):
        return self.descriptions

    def setDescriptions(self, newDescriptions):
        self.descriptions = newDescriptions

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getMaxUsesNumber(self):
        return self.maxUsesNumber

    def setMaxUsesNumber(self, newMaxUsesNumber):
        self.maxUsesNumber = newMaxUsesNumber

    def getMaxUsesNumberOnRenewableSub(self):
        return self.maxUsesNumberOnRenewableSub

    def setMaxUsesNumberOnRenewableSub(self, newMaxUsesNumberOnRenewableSub):
        self.maxUsesNumberOnRenewableSub = newMaxUsesNumberOnRenewableSub


# @package Kaltura
# @subpackage Client
class KalturaUsageModule(KalturaObjectBase):
    """Pricing usage module"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            maxViewsNumber=NotImplemented,
            viewLifeCycle=NotImplemented,
            fullLifeCycle=NotImplemented,
            couponId=NotImplemented,
            waiverPeriod=NotImplemented,
            isWaiverEnabled=NotImplemented,
            isOfflinePlayback=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Usage module identifier
        # @var int
        # @readonly
        self.id = id

        # Usage module name
        # @var string
        self.name = name

        # The maximum number of times an item in this usage module can be viewed
        # @var int
        self.maxViewsNumber = maxViewsNumber

        # The amount time an item is available for viewing since a user started watching the item
        # @var int
        self.viewLifeCycle = viewLifeCycle

        # The amount time an item is available for viewing
        # @var int
        self.fullLifeCycle = fullLifeCycle

        # Identifies a specific coupon linked to this object
        # @var int
        self.couponId = couponId

        # Time period during which the end user can waive his rights to cancel a purchase. When the time period is passed, the purchase can no longer be cancelled
        # @var int
        self.waiverPeriod = waiverPeriod

        # Indicates whether or not the end user has the right to waive his rights to cancel a purchase
        # @var bool
        self.isWaiverEnabled = isWaiverEnabled

        # Indicates that usage is targeted for offline playback
        # @var bool
        self.isOfflinePlayback = isOfflinePlayback


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'maxViewsNumber': getXmlNodeInt, 
        'viewLifeCycle': getXmlNodeInt, 
        'fullLifeCycle': getXmlNodeInt, 
        'couponId': getXmlNodeInt, 
        'waiverPeriod': getXmlNodeInt, 
        'isWaiverEnabled': getXmlNodeBool, 
        'isOfflinePlayback': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUsageModule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUsageModule")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("maxViewsNumber", self.maxViewsNumber)
        kparams.addIntIfDefined("viewLifeCycle", self.viewLifeCycle)
        kparams.addIntIfDefined("fullLifeCycle", self.fullLifeCycle)
        kparams.addIntIfDefined("couponId", self.couponId)
        kparams.addIntIfDefined("waiverPeriod", self.waiverPeriod)
        kparams.addBoolIfDefined("isWaiverEnabled", self.isWaiverEnabled)
        kparams.addBoolIfDefined("isOfflinePlayback", self.isOfflinePlayback)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getMaxViewsNumber(self):
        return self.maxViewsNumber

    def setMaxViewsNumber(self, newMaxViewsNumber):
        self.maxViewsNumber = newMaxViewsNumber

    def getViewLifeCycle(self):
        return self.viewLifeCycle

    def setViewLifeCycle(self, newViewLifeCycle):
        self.viewLifeCycle = newViewLifeCycle

    def getFullLifeCycle(self):
        return self.fullLifeCycle

    def setFullLifeCycle(self, newFullLifeCycle):
        self.fullLifeCycle = newFullLifeCycle

    def getCouponId(self):
        return self.couponId

    def setCouponId(self, newCouponId):
        self.couponId = newCouponId

    def getWaiverPeriod(self):
        return self.waiverPeriod

    def setWaiverPeriod(self, newWaiverPeriod):
        self.waiverPeriod = newWaiverPeriod

    def getIsWaiverEnabled(self):
        return self.isWaiverEnabled

    def setIsWaiverEnabled(self, newIsWaiverEnabled):
        self.isWaiverEnabled = newIsWaiverEnabled

    def getIsOfflinePlayback(self):
        return self.isOfflinePlayback

    def setIsOfflinePlayback(self, newIsOfflinePlayback):
        self.isOfflinePlayback = newIsOfflinePlayback


# @package Kaltura
# @subpackage Client
class KalturaPricePlan(KalturaUsageModule):
    """Price plan"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            maxViewsNumber=NotImplemented,
            viewLifeCycle=NotImplemented,
            fullLifeCycle=NotImplemented,
            couponId=NotImplemented,
            waiverPeriod=NotImplemented,
            isWaiverEnabled=NotImplemented,
            isOfflinePlayback=NotImplemented,
            isRenewable=NotImplemented,
            renewalsNumber=NotImplemented,
            priceId=NotImplemented,
            discountId=NotImplemented):
        KalturaUsageModule.__init__(self,
            id,
            name,
            maxViewsNumber,
            viewLifeCycle,
            fullLifeCycle,
            couponId,
            waiverPeriod,
            isWaiverEnabled,
            isOfflinePlayback)

        # Denotes whether or not this object can be renewed
        # @var bool
        self.isRenewable = isRenewable

        # Defines the number of times the module will be renewed (for the life_cycle period)
        # @var int
        self.renewalsNumber = renewalsNumber

        # Unique identifier associated with this object&#39;s price
        # @var int
        self.priceId = priceId

        # The discount module identifier of the price plan
        # @var int
        self.discountId = discountId


    PROPERTY_LOADERS = {
        'isRenewable': getXmlNodeBool, 
        'renewalsNumber': getXmlNodeInt, 
        'priceId': getXmlNodeInt, 
        'discountId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaUsageModule.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPricePlan.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUsageModule.toParams(self)
        kparams.put("objectType", "KalturaPricePlan")
        kparams.addBoolIfDefined("isRenewable", self.isRenewable)
        kparams.addIntIfDefined("renewalsNumber", self.renewalsNumber)
        kparams.addIntIfDefined("priceId", self.priceId)
        kparams.addIntIfDefined("discountId", self.discountId)
        return kparams

    def getIsRenewable(self):
        return self.isRenewable

    def setIsRenewable(self, newIsRenewable):
        self.isRenewable = newIsRenewable

    def getRenewalsNumber(self):
        return self.renewalsNumber

    def setRenewalsNumber(self, newRenewalsNumber):
        self.renewalsNumber = newRenewalsNumber

    def getPriceId(self):
        return self.priceId

    def setPriceId(self, newPriceId):
        self.priceId = newPriceId

    def getDiscountId(self):
        return self.discountId

    def setDiscountId(self, newDiscountId):
        self.discountId = newDiscountId


# @package Kaltura
# @subpackage Client
class KalturaPreviewModule(KalturaObjectBase):
    """Preview module"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            lifeCycle=NotImplemented,
            nonRenewablePeriod=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Preview module identifier
        # @var int
        # @readonly
        self.id = id

        # Preview module name
        # @var string
        self.name = name

        # Preview module life cycle - for how long the preview module is active
        # @var int
        self.lifeCycle = lifeCycle

        # The time you can&#39;t buy the item to which the preview module is assigned to again
        # @var int
        self.nonRenewablePeriod = nonRenewablePeriod


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'lifeCycle': getXmlNodeInt, 
        'nonRenewablePeriod': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPreviewModule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPreviewModule")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("lifeCycle", self.lifeCycle)
        kparams.addIntIfDefined("nonRenewablePeriod", self.nonRenewablePeriod)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getLifeCycle(self):
        return self.lifeCycle

    def setLifeCycle(self, newLifeCycle):
        self.lifeCycle = newLifeCycle

    def getNonRenewablePeriod(self):
        return self.nonRenewablePeriod

    def setNonRenewablePeriod(self, newNonRenewablePeriod):
        self.nonRenewablePeriod = newNonRenewablePeriod


# @package Kaltura
# @subpackage Client
class KalturaSubscription(KalturaObjectBase):
    """Subscription details"""

    def __init__(self,
            id=NotImplemented,
            channels=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            fileTypes=NotImplemented,
            isRenewable=NotImplemented,
            renewalsNumber=NotImplemented,
            isInfiniteRenewal=NotImplemented,
            price=NotImplemented,
            discountModule=NotImplemented,
            couponsGroup=NotImplemented,
            names=NotImplemented,
            descriptions=NotImplemented,
            mediaId=NotImplemented,
            prorityInOrder=NotImplemented,
            productCode=NotImplemented,
            pricePlans=NotImplemented,
            previewModule=NotImplemented,
            householdLimitationsId=NotImplemented,
            gracePeriodMinutes=NotImplemented,
            premiumServices=NotImplemented,
            maxViewsNumber=NotImplemented,
            viewLifeCycle=NotImplemented,
            waiverPeriod=NotImplemented,
            isWaiverEnabled=NotImplemented,
            userTypes=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Subscription identifier
        # @var string
        self.id = id

        # A list of channels associated with this subscription
        # @var array of KalturaBaseChannel
        self.channels = channels

        # The first date the subscription is available for purchasing
        # @var int
        self.startDate = startDate

        # The last date the subscription is available for purchasing
        # @var int
        self.endDate = endDate

        # A list of file types identifiers that are supported in this subscription
        # @var array of KalturaIntegerValue
        self.fileTypes = fileTypes

        # Denotes whether or not this subscription can be renewed
        # @var bool
        self.isRenewable = isRenewable

        # Defines the number of times this subscription will be renewed
        # @var int
        self.renewalsNumber = renewalsNumber

        # Indicates whether the subscription will renew forever
        # @var bool
        self.isInfiniteRenewal = isInfiniteRenewal

        # The price of the subscription
        # @var KalturaPriceDetails
        self.price = price

        # The internal discount module for the subscription
        # @var KalturaDiscountModule
        self.discountModule = discountModule

        # Coupons group for the subscription
        # @var KalturaCouponsGroup
        self.couponsGroup = couponsGroup

        # A list of the name of the subscription on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.names = names

        # A list of the descriptions of the subscriptions on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.descriptions = descriptions

        # Identifier of the media associated with the subscription
        # @var int
        self.mediaId = mediaId

        # Subscription order (when returned in methods that retrieve subscriptions)
        # @var int
        self.prorityInOrder = prorityInOrder

        # Product code for the subscription
        # @var string
        self.productCode = productCode

        # Subscription price plans
        # @var array of KalturaPricePlan
        self.pricePlans = pricePlans

        # Subscription preview module
        # @var KalturaPreviewModule
        self.previewModule = previewModule

        # The household limitation module identifier associated with this subscription
        # @var int
        self.householdLimitationsId = householdLimitationsId

        # The subscription grace period in minutes
        # @var int
        self.gracePeriodMinutes = gracePeriodMinutes

        # List of premium services included in the subscription
        # @var array of KalturaPremiumService
        self.premiumServices = premiumServices

        # The maximum number of times an item in this usage module can be viewed
        # @var int
        self.maxViewsNumber = maxViewsNumber

        # The amount time an item is available for viewing since a user started watching the item
        # @var int
        self.viewLifeCycle = viewLifeCycle

        # Time period during which the end user can waive his rights to cancel a purchase. When the time period is passed, the purchase can no longer be cancelled
        # @var int
        self.waiverPeriod = waiverPeriod

        # Indicates whether or not the end user has the right to waive his rights to cancel a purchase
        # @var bool
        self.isWaiverEnabled = isWaiverEnabled

        # List of permitted user types for the subscription
        # @var array of KalturaOTTUserType
        self.userTypes = userTypes


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'channels': (KalturaObjectFactory.createArray, KalturaBaseChannel), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'fileTypes': (KalturaObjectFactory.createArray, KalturaIntegerValue), 
        'isRenewable': getXmlNodeBool, 
        'renewalsNumber': getXmlNodeInt, 
        'isInfiniteRenewal': getXmlNodeBool, 
        'price': (KalturaObjectFactory.create, KalturaPriceDetails), 
        'discountModule': (KalturaObjectFactory.create, KalturaDiscountModule), 
        'couponsGroup': (KalturaObjectFactory.create, KalturaCouponsGroup), 
        'names': (KalturaObjectFactory.createArray, KalturaTranslationToken), 
        'descriptions': (KalturaObjectFactory.createArray, KalturaTranslationToken), 
        'mediaId': getXmlNodeInt, 
        'prorityInOrder': getXmlNodeInt, 
        'productCode': getXmlNodeText, 
        'pricePlans': (KalturaObjectFactory.createArray, KalturaPricePlan), 
        'previewModule': (KalturaObjectFactory.create, KalturaPreviewModule), 
        'householdLimitationsId': getXmlNodeInt, 
        'gracePeriodMinutes': getXmlNodeInt, 
        'premiumServices': (KalturaObjectFactory.createArray, KalturaPremiumService), 
        'maxViewsNumber': getXmlNodeInt, 
        'viewLifeCycle': getXmlNodeInt, 
        'waiverPeriod': getXmlNodeInt, 
        'isWaiverEnabled': getXmlNodeBool, 
        'userTypes': (KalturaObjectFactory.createArray, KalturaOTTUserType), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscription.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSubscription")
        kparams.addStringIfDefined("id", self.id)
        kparams.addArrayIfDefined("channels", self.channels)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addArrayIfDefined("fileTypes", self.fileTypes)
        kparams.addBoolIfDefined("isRenewable", self.isRenewable)
        kparams.addIntIfDefined("renewalsNumber", self.renewalsNumber)
        kparams.addBoolIfDefined("isInfiniteRenewal", self.isInfiniteRenewal)
        kparams.addObjectIfDefined("price", self.price)
        kparams.addObjectIfDefined("discountModule", self.discountModule)
        kparams.addObjectIfDefined("couponsGroup", self.couponsGroup)
        kparams.addArrayIfDefined("names", self.names)
        kparams.addArrayIfDefined("descriptions", self.descriptions)
        kparams.addIntIfDefined("mediaId", self.mediaId)
        kparams.addIntIfDefined("prorityInOrder", self.prorityInOrder)
        kparams.addStringIfDefined("productCode", self.productCode)
        kparams.addArrayIfDefined("pricePlans", self.pricePlans)
        kparams.addObjectIfDefined("previewModule", self.previewModule)
        kparams.addIntIfDefined("householdLimitationsId", self.householdLimitationsId)
        kparams.addIntIfDefined("gracePeriodMinutes", self.gracePeriodMinutes)
        kparams.addArrayIfDefined("premiumServices", self.premiumServices)
        kparams.addIntIfDefined("maxViewsNumber", self.maxViewsNumber)
        kparams.addIntIfDefined("viewLifeCycle", self.viewLifeCycle)
        kparams.addIntIfDefined("waiverPeriod", self.waiverPeriod)
        kparams.addBoolIfDefined("isWaiverEnabled", self.isWaiverEnabled)
        kparams.addArrayIfDefined("userTypes", self.userTypes)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getChannels(self):
        return self.channels

    def setChannels(self, newChannels):
        self.channels = newChannels

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getFileTypes(self):
        return self.fileTypes

    def setFileTypes(self, newFileTypes):
        self.fileTypes = newFileTypes

    def getIsRenewable(self):
        return self.isRenewable

    def setIsRenewable(self, newIsRenewable):
        self.isRenewable = newIsRenewable

    def getRenewalsNumber(self):
        return self.renewalsNumber

    def setRenewalsNumber(self, newRenewalsNumber):
        self.renewalsNumber = newRenewalsNumber

    def getIsInfiniteRenewal(self):
        return self.isInfiniteRenewal

    def setIsInfiniteRenewal(self, newIsInfiniteRenewal):
        self.isInfiniteRenewal = newIsInfiniteRenewal

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getDiscountModule(self):
        return self.discountModule

    def setDiscountModule(self, newDiscountModule):
        self.discountModule = newDiscountModule

    def getCouponsGroup(self):
        return self.couponsGroup

    def setCouponsGroup(self, newCouponsGroup):
        self.couponsGroup = newCouponsGroup

    def getNames(self):
        return self.names

    def setNames(self, newNames):
        self.names = newNames

    def getDescriptions(self):
        return self.descriptions

    def setDescriptions(self, newDescriptions):
        self.descriptions = newDescriptions

    def getMediaId(self):
        return self.mediaId

    def setMediaId(self, newMediaId):
        self.mediaId = newMediaId

    def getProrityInOrder(self):
        return self.prorityInOrder

    def setProrityInOrder(self, newProrityInOrder):
        self.prorityInOrder = newProrityInOrder

    def getProductCode(self):
        return self.productCode

    def setProductCode(self, newProductCode):
        self.productCode = newProductCode

    def getPricePlans(self):
        return self.pricePlans

    def setPricePlans(self, newPricePlans):
        self.pricePlans = newPricePlans

    def getPreviewModule(self):
        return self.previewModule

    def setPreviewModule(self, newPreviewModule):
        self.previewModule = newPreviewModule

    def getHouseholdLimitationsId(self):
        return self.householdLimitationsId

    def setHouseholdLimitationsId(self, newHouseholdLimitationsId):
        self.householdLimitationsId = newHouseholdLimitationsId

    def getGracePeriodMinutes(self):
        return self.gracePeriodMinutes

    def setGracePeriodMinutes(self, newGracePeriodMinutes):
        self.gracePeriodMinutes = newGracePeriodMinutes

    def getPremiumServices(self):
        return self.premiumServices

    def setPremiumServices(self, newPremiumServices):
        self.premiumServices = newPremiumServices

    def getMaxViewsNumber(self):
        return self.maxViewsNumber

    def setMaxViewsNumber(self, newMaxViewsNumber):
        self.maxViewsNumber = newMaxViewsNumber

    def getViewLifeCycle(self):
        return self.viewLifeCycle

    def setViewLifeCycle(self, newViewLifeCycle):
        self.viewLifeCycle = newViewLifeCycle

    def getWaiverPeriod(self):
        return self.waiverPeriod

    def setWaiverPeriod(self, newWaiverPeriod):
        self.waiverPeriod = newWaiverPeriod

    def getIsWaiverEnabled(self):
        return self.isWaiverEnabled

    def setIsWaiverEnabled(self, newIsWaiverEnabled):
        self.isWaiverEnabled = newIsWaiverEnabled

    def getUserTypes(self):
        return self.userTypes

    def setUserTypes(self, newUserTypes):
        self.userTypes = newUserTypes


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionListResponse(KalturaListResponse):
    """Subscriptions list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of subscriptions
        # @var array of KalturaSubscription
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaSubscription), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaProductsPriceListResponse(KalturaListResponse):
    """Prices list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of prices
        # @var array of KalturaProductPrice
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaProductPrice), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductsPriceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaProductsPriceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaEntitlement(KalturaObjectBase):
    """Entitlement"""

    def __init__(self,
            type=NotImplemented,
            entitlementId=NotImplemented,
            currentUses=NotImplemented,
            endDate=NotImplemented,
            currentDate=NotImplemented,
            lastViewDate=NotImplemented,
            purchaseDate=NotImplemented,
            purchaseId=NotImplemented,
            paymentMethod=NotImplemented,
            deviceUdid=NotImplemented,
            deviceName=NotImplemented,
            isCancelationWindowEnabled=NotImplemented,
            maxUses=NotImplemented,
            nextRenewalDate=NotImplemented,
            isRenewableForPurchase=NotImplemented,
            isRenewable=NotImplemented,
            mediaFileId=NotImplemented,
            mediaId=NotImplemented,
            isInGracePeriod=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Entitlement type
        # @var KalturaTransactionType
        # @readonly
        self.type = type

        # Entitlement identifier
        # @var string
        # @readonly
        self.entitlementId = entitlementId

        # The current number of uses
        # @var int
        # @readonly
        self.currentUses = currentUses

        # The end date of the entitlement
        # @var int
        # @readonly
        self.endDate = endDate

        # Current date
        # @var int
        # @readonly
        self.currentDate = currentDate

        # The last date the item was viewed
        # @var int
        # @readonly
        self.lastViewDate = lastViewDate

        # Purchase date
        # @var int
        # @readonly
        self.purchaseDate = purchaseDate

        # Purchase identifier (for subscriptions and collections only)
        # @var int
        # @readonly
        self.purchaseId = purchaseId

        # Payment Method
        # @var KalturaPaymentMethodType
        # @readonly
        self.paymentMethod = paymentMethod

        # The UDID of the device from which the purchase was made
        # @var string
        # @readonly
        self.deviceUdid = deviceUdid

        # The name of the device from which the purchase was made
        # @var string
        # @readonly
        self.deviceName = deviceName

        # Indicates whether a cancelation window period is enabled
        # @var bool
        # @readonly
        self.isCancelationWindowEnabled = isCancelationWindowEnabled

        # The maximum number of uses available for this item (only for subscription and PPV)
        # @var int
        # @readonly
        self.maxUses = maxUses

        # The date of the next renewal (only for subscription)
        # @var int
        # @readonly
        self.nextRenewalDate = nextRenewalDate

        # Indicates whether the subscription is renewable in this purchase (only for subscription)
        # @var bool
        # @readonly
        self.isRenewableForPurchase = isRenewableForPurchase

        # Indicates whether a subscription is renewable (only for subscription)
        # @var bool
        # @readonly
        self.isRenewable = isRenewable

        # Media file identifier (only for PPV)
        # @var int
        # @readonly
        self.mediaFileId = mediaFileId

        # Media identifier (only for PPV)
        # @var int
        # @readonly
        self.mediaId = mediaId

        # Indicates whether the user is currently in his grace period entitlement
        # @var bool
        # @readonly
        self.isInGracePeriod = isInGracePeriod


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createString, "KalturaTransactionType"), 
        'entitlementId': getXmlNodeText, 
        'currentUses': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'currentDate': getXmlNodeInt, 
        'lastViewDate': getXmlNodeInt, 
        'purchaseDate': getXmlNodeInt, 
        'purchaseId': getXmlNodeInt, 
        'paymentMethod': (KalturaEnumsFactory.createString, "KalturaPaymentMethodType"), 
        'deviceUdid': getXmlNodeText, 
        'deviceName': getXmlNodeText, 
        'isCancelationWindowEnabled': getXmlNodeBool, 
        'maxUses': getXmlNodeInt, 
        'nextRenewalDate': getXmlNodeInt, 
        'isRenewableForPurchase': getXmlNodeBool, 
        'isRenewable': getXmlNodeBool, 
        'mediaFileId': getXmlNodeInt, 
        'mediaId': getXmlNodeInt, 
        'isInGracePeriod': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntitlement.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntitlement")
        return kparams

    def getType(self):
        return self.type

    def getEntitlementId(self):
        return self.entitlementId

    def getCurrentUses(self):
        return self.currentUses

    def getEndDate(self):
        return self.endDate

    def getCurrentDate(self):
        return self.currentDate

    def getLastViewDate(self):
        return self.lastViewDate

    def getPurchaseDate(self):
        return self.purchaseDate

    def getPurchaseId(self):
        return self.purchaseId

    def getPaymentMethod(self):
        return self.paymentMethod

    def getDeviceUdid(self):
        return self.deviceUdid

    def getDeviceName(self):
        return self.deviceName

    def getIsCancelationWindowEnabled(self):
        return self.isCancelationWindowEnabled

    def getMaxUses(self):
        return self.maxUses

    def getNextRenewalDate(self):
        return self.nextRenewalDate

    def getIsRenewableForPurchase(self):
        return self.isRenewableForPurchase

    def getIsRenewable(self):
        return self.isRenewable

    def getMediaFileId(self):
        return self.mediaFileId

    def getMediaId(self):
        return self.mediaId

    def getIsInGracePeriod(self):
        return self.isInGracePeriod


# @package Kaltura
# @subpackage Client
class KalturaEntitlementListResponse(KalturaListResponse):
    """Entitlements list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of entitlements
        # @var array of KalturaEntitlement
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaEntitlement), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntitlementListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaEntitlementListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaHomeNetwork(KalturaObjectBase):
    """Home network details"""

    def __init__(self,
            externalId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            isActive=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Home network identifier
        # @var string
        self.externalId = externalId

        # Home network name
        # @var string
        self.name = name

        # Home network description
        # @var string
        self.description = description

        # Is home network is active
        # @var bool
        self.isActive = isActive


    PROPERTY_LOADERS = {
        'externalId': getXmlNodeText, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHomeNetwork.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHomeNetwork")
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addBoolIfDefined("isActive", self.isActive)
        return kparams

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive


# @package Kaltura
# @subpackage Client
class KalturaHomeNetworkListResponse(KalturaListResponse):
    """Home networks"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Home networks
        # @var array of KalturaHomeNetwork
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaHomeNetwork), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHomeNetworkListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHomeNetworkListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaFavorite(KalturaObjectBase):
    """Favorite details"""

    def __init__(self,
            assetId=NotImplemented,
            extraData=NotImplemented,
            createDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # AssetInfo Model
        # @var int
        self.assetId = assetId

        # Extra Value
        # @var string
        self.extraData = extraData

        # Specifies when was the favorite created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
        'extraData': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFavorite.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFavorite")
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addStringIfDefined("extraData", self.extraData)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getExtraData(self):
        return self.extraData

    def setExtraData(self, newExtraData):
        self.extraData = newExtraData

    def getCreateDate(self):
        return self.createDate


# @package Kaltura
# @subpackage Client
class KalturaFavoriteListResponse(KalturaListResponse):
    """Favorite list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of favorites
        # @var array of KalturaFavorite
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaFavorite), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFavoriteListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaFavoriteListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaOTTUserListResponse(KalturaListResponse):
    """Users list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of users
        # @var array of KalturaOTTUser
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaOTTUser), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTUserListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaOTTUserListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetStatisticsListResponse(KalturaListResponse):
    """List of assets statistics"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaAssetStatistics
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAssetStatistics), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStatisticsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetStatisticsListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSlimAssetInfoWrapper(KalturaListResponse):
    """Slim assets wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaBaseAssetInfo
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaBaseAssetInfo), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSlimAssetInfoWrapper.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSlimAssetInfoWrapper")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetHistory(KalturaObjectBase):
    """Watch history asset info"""

    def __init__(self,
            assetId=NotImplemented,
            position=NotImplemented,
            duration=NotImplemented,
            watchedDate=NotImplemented,
            finishedWatching=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Asset identifier
        # @var int
        # @readonly
        self.assetId = assetId

        # Position in seconds of the relevant asset
        # @var int
        # @readonly
        self.position = position

        # Duration in seconds of the relevant asset
        # @var int
        # @readonly
        self.duration = duration

        # The date when the media was last watched
        # @var int
        # @readonly
        self.watchedDate = watchedDate

        # Boolean which specifies whether the user finished watching the movie or not
        # @var bool
        # @readonly
        self.finishedWatching = finishedWatching


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
        'position': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'watchedDate': getXmlNodeInt, 
        'finishedWatching': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetHistory.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetHistory")
        return kparams

    def getAssetId(self):
        return self.assetId

    def getPosition(self):
        return self.position

    def getDuration(self):
        return self.duration

    def getWatchedDate(self):
        return self.watchedDate

    def getFinishedWatching(self):
        return self.finishedWatching


# @package Kaltura
# @subpackage Client
class KalturaAssetHistoryListResponse(KalturaListResponse):
    """Watch history asset wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # WatchHistoryAssets Models
        # @var array of KalturaAssetHistory
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaAssetHistory), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetHistoryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetHistoryListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAppToken(KalturaObjectBase):
    """Application token"""

    def __init__(self,
            id=NotImplemented,
            expiry=NotImplemented,
            partnerId=NotImplemented,
            sessionDuration=NotImplemented,
            hashType=NotImplemented,
            sessionPrivileges=NotImplemented,
            sessionType=NotImplemented,
            status=NotImplemented,
            token=NotImplemented,
            sessionUserId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The id of the application token
        # @var string
        # @readonly
        self.id = id

        # Expiry time of current token (unix timestamp in seconds)
        # @var int
        self.expiry = expiry

        # Partner identifier
        # @var int
        self.partnerId = partnerId

        # Expiry duration of KS (Kaltura Session) that created using the current token (in seconds)
        # @var int
        self.sessionDuration = sessionDuration

        # The hash type of the token
        # @var KalturaAppTokenHashType
        self.hashType = hashType

        # Comma separated privileges to be applied on KS (Kaltura Session) that created using the current token
        # @var string
        self.sessionPrivileges = sessionPrivileges

        # Type of KS (Kaltura Session) that created using the current token
        # @var KalturaSessionType
        self.sessionType = sessionType

        # Application token status
        # @var KalturaAppTokenStatus
        # @readonly
        self.status = status

        # The application token
        # @var string
        self.token = token

        # User id of KS (Kaltura Session) that created using the current token
        # @var string
        self.sessionUserId = sessionUserId


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'expiry': getXmlNodeInt, 
        'partnerId': getXmlNodeInt, 
        'sessionDuration': getXmlNodeInt, 
        'hashType': (KalturaEnumsFactory.createString, "KalturaAppTokenHashType"), 
        'sessionPrivileges': getXmlNodeText, 
        'sessionType': (KalturaEnumsFactory.createInt, "KalturaSessionType"), 
        'status': (KalturaEnumsFactory.createInt, "KalturaAppTokenStatus"), 
        'token': getXmlNodeText, 
        'sessionUserId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAppToken.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAppToken")
        kparams.addIntIfDefined("expiry", self.expiry)
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addIntIfDefined("sessionDuration", self.sessionDuration)
        kparams.addStringEnumIfDefined("hashType", self.hashType)
        kparams.addStringIfDefined("sessionPrivileges", self.sessionPrivileges)
        kparams.addIntEnumIfDefined("sessionType", self.sessionType)
        kparams.addStringIfDefined("token", self.token)
        kparams.addStringIfDefined("sessionUserId", self.sessionUserId)
        return kparams

    def getId(self):
        return self.id

    def getExpiry(self):
        return self.expiry

    def setExpiry(self, newExpiry):
        self.expiry = newExpiry

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getSessionDuration(self):
        return self.sessionDuration

    def setSessionDuration(self, newSessionDuration):
        self.sessionDuration = newSessionDuration

    def getHashType(self):
        return self.hashType

    def setHashType(self, newHashType):
        self.hashType = newHashType

    def getSessionPrivileges(self):
        return self.sessionPrivileges

    def setSessionPrivileges(self, newSessionPrivileges):
        self.sessionPrivileges = newSessionPrivileges

    def getSessionType(self):
        return self.sessionType

    def setSessionType(self, newSessionType):
        self.sessionType = newSessionType

    def getStatus(self):
        return self.status

    def getToken(self):
        return self.token

    def setToken(self, newToken):
        self.token = newToken

    def getSessionUserId(self):
        return self.sessionUserId

    def setSessionUserId(self, newSessionUserId):
        self.sessionUserId = newSessionUserId


# @package Kaltura
# @subpackage Client
class KalturaSession(KalturaObjectBase):
    """Kaltura Session"""

    def __init__(self,
            ks=NotImplemented,
            sessionType=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            expiry=NotImplemented,
            privileges=NotImplemented,
            udid=NotImplemented):
        KalturaObjectBase.__init__(self)

        # KS
        # @var string
        self.ks = ks

        # Session type
        # @var KalturaSessionType
        self.sessionType = sessionType

        # Partner identifier
        # @var int
        self.partnerId = partnerId

        # User identifier
        # @var string
        self.userId = userId

        # Expiry
        # @var int
        self.expiry = expiry

        # Privileges
        # @var string
        self.privileges = privileges

        # udid
        # @var string
        self.udid = udid


    PROPERTY_LOADERS = {
        'ks': getXmlNodeText, 
        'sessionType': (KalturaEnumsFactory.createInt, "KalturaSessionType"), 
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'expiry': getXmlNodeInt, 
        'privileges': getXmlNodeText, 
        'udid': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSession.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSession")
        kparams.addStringIfDefined("ks", self.ks)
        kparams.addIntEnumIfDefined("sessionType", self.sessionType)
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("userId", self.userId)
        kparams.addIntIfDefined("expiry", self.expiry)
        kparams.addStringIfDefined("privileges", self.privileges)
        kparams.addStringIfDefined("udid", self.udid)
        return kparams

    def getKs(self):
        return self.ks

    def setKs(self, newKs):
        self.ks = newKs

    def getSessionType(self):
        return self.sessionType

    def setSessionType(self, newSessionType):
        self.sessionType = newSessionType

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getExpiry(self):
        return self.expiry

    def setExpiry(self, newExpiry):
        self.expiry = newExpiry

    def getPrivileges(self):
        return self.privileges

    def setPrivileges(self, newPrivileges):
        self.privileges = newPrivileges

    def getUdid(self):
        return self.udid

    def setUdid(self, newUdid):
        self.udid = newUdid


# @package Kaltura
# @subpackage Client
class KalturaSessionInfo(KalturaSession):
    """Kaltura Session"""

    def __init__(self,
            ks=NotImplemented,
            sessionType=NotImplemented,
            partnerId=NotImplemented,
            userId=NotImplemented,
            expiry=NotImplemented,
            privileges=NotImplemented,
            udid=NotImplemented):
        KalturaSession.__init__(self,
            ks,
            sessionType,
            partnerId,
            userId,
            expiry,
            privileges,
            udid)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSession.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSessionInfo.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSession.toParams(self)
        kparams.put("objectType", "KalturaSessionInfo")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaAssetFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaBundleFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idEqual=NotImplemented,
            typeIn=NotImplemented,
            bundleTypeEqual=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy)

        # Bundle Id.
        # @var int
        self.idEqual = idEqual

        # Comma separated list of asset types to search within. 
        #             Possible values: 0 – EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted – all types should be included.
        # @var string
        self.typeIn = typeIn

        # bundleType - possible values: Subscription or Collection
        # @var KalturaBundleType
        self.bundleTypeEqual = bundleTypeEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'typeIn': getXmlNodeText, 
        'bundleTypeEqual': (KalturaEnumsFactory.createString, "KalturaBundleType"), 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBundleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaBundleFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addStringEnumIfDefined("bundleTypeEqual", self.bundleTypeEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getBundleTypeEqual(self):
        return self.bundleTypeEqual

    def setBundleTypeEqual(self, newBundleTypeEqual):
        self.bundleTypeEqual = newBundleTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaChannelExternalFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idEqual=NotImplemented,
            utcOffsetEqual=NotImplemented,
            freeText=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy)

        # External Channel Id.
        # @var int
        self.idEqual = idEqual

        # UtcOffsetEqual
        # @var string
        self.utcOffsetEqual = utcOffsetEqual

        # FreeTextEqual
        # @var string
        self.freeText = freeText


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'utcOffsetEqual': getXmlNodeText, 
        'freeText': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelExternalFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaChannelExternalFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("utcOffsetEqual", self.utcOffsetEqual)
        kparams.addStringIfDefined("freeText", self.freeText)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getUtcOffsetEqual(self):
        return self.utcOffsetEqual

    def setUtcOffsetEqual(self, newUtcOffsetEqual):
        self.utcOffsetEqual = newUtcOffsetEqual

    def getFreeText(self):
        return self.freeText

    def setFreeText(self, newFreeText):
        self.freeText = newFreeText


# @package Kaltura
# @subpackage Client
class KalturaChannelFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idEqual=NotImplemented,
            kSql=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy)

        # Channel Id
        # @var int
        self.idEqual = idEqual

        # @var string
        self.kSql = kSql


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'kSql': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaChannelFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("kSql", self.kSql)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql


# @package Kaltura
# @subpackage Client
class KalturaRelatedFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            kSql=NotImplemented,
            idEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy)

        # Search assets using dynamic criteria. Provided collection of nested expressions with key, comparison operators, value, and logical conjunction.
        #             Possible keys: any Tag or Meta defined in the system and the following reserved keys: start_date, end_date. 
        #             epg_id, media_id - for specific asset IDs.
        #             geo_block - only valid value is &quot;true&quot;: When enabled, only assets that are not restriced to the user by geo-block rules will return.
        #             parental_rules - only valid value is &quot;true&quot;: When enabled, only assets that the user doesn&#39;t need to provide PIN code will return.
        #             epg_channel_id – the channel identifier of the EPG program.
        #             entitled_assets - valid values: &quot;free&quot;, &quot;entitled&quot;, &quot;both&quot;. free - gets only free to watch assets. entitled - only those that the user is implicitly entitled to watch.
        #             Comparison operators: for numerical fields =, &gt;, &gt;=, &lt;, &lt;=, : (in). For alpha-numerical fields =, != (not), ~ (like), !~, ^ (starts with). Logical conjunction: and, or. 
        #             Search values are limited to 20 characters each.
        #             (maximum length of entire filter is 1024 characters)
        # @var string
        self.kSql = kSql

        # the ID of the asset for which to return related assets
        # @var string
        self.idEqual = idEqual

        # Comma separated list of asset types to search within. 
        #             Possible values: 0 – EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted – all types should be included.
        # @var string
        self.typeIn = typeIn


    PROPERTY_LOADERS = {
        'kSql': getXmlNodeText, 
        'idEqual': getXmlNodeText, 
        'typeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRelatedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaRelatedFilter")
        kparams.addStringIfDefined("kSql", self.kSql)
        kparams.addStringIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        return kparams

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn


# @package Kaltura
# @subpackage Client
class KalturaRelatedExternalFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idEqual=NotImplemented,
            typeIn=NotImplemented,
            utcOffsetEqual=NotImplemented,
            freeText=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy)

        # the External ID of the asset for which to return related assets
        # @var int
        self.idEqual = idEqual

        # Comma separated list of asset types to search within. 
        #             Possible values: 0 – EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted – all types should be included.
        # @var string
        self.typeIn = typeIn

        # UtcOffsetEqual
        # @var int
        self.utcOffsetEqual = utcOffsetEqual

        # FreeText
        # @var string
        self.freeText = freeText


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'typeIn': getXmlNodeText, 
        'utcOffsetEqual': getXmlNodeInt, 
        'freeText': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRelatedExternalFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaRelatedExternalFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntIfDefined("utcOffsetEqual", self.utcOffsetEqual)
        kparams.addStringIfDefined("freeText", self.freeText)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getUtcOffsetEqual(self):
        return self.utcOffsetEqual

    def setUtcOffsetEqual(self, newUtcOffsetEqual):
        self.utcOffsetEqual = newUtcOffsetEqual

    def getFreeText(self):
        return self.freeText

    def setFreeText(self, newFreeText):
        self.freeText = newFreeText


# @package Kaltura
# @subpackage Client
class KalturaSearchAssetFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            kSql=NotImplemented,
            typeIn=NotImplemented,
            idIn=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy)

        # Search assets using dynamic criteria. Provided collection of nested expressions with key, comparison operators, value, and logical conjunction.
        #             Possible keys: any Tag or Meta defined in the system and the following reserved keys: start_date, end_date. 
        #             epg_id, media_id - for specific asset IDs.
        #             geo_block - only valid value is &quot;true&quot;: When enabled, only assets that are not restriced to the user by geo-block rules will return.
        #             parental_rules - only valid value is &quot;true&quot;: When enabled, only assets that the user doesn&#39;t need to provide PIN code will return.
        #             epg_channel_id – the channel identifier of the EPG program.
        #             entitled_assets - valid values: &quot;free&quot;, &quot;entitled&quot;, &quot;both&quot;. free - gets only free to watch assets. entitled - only those that the user is implicitly entitled to watch.
        #             Comparison operators: for numerical fields =, &gt;, &gt;=, &lt;, &lt;=, : (in). For alpha-numerical fields =, != (not), ~ (like), !~, ^ (starts with). Logical conjunction: and, or. 
        #             Search values are limited to 20 characters each.
        #             (maximum length of entire filter is 1024 characters)
        # @var string
        self.kSql = kSql

        # Comma separated list of asset types to search within. 
        #             Possible values: 0 – EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted – all types should be included.
        # @var string
        self.typeIn = typeIn

        # Comma separated list of EPG channel ids to search within.
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'kSql': getXmlNodeText, 
        'typeIn': getXmlNodeText, 
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaSearchAssetFilter")
        kparams.addStringIfDefined("kSql", self.kSql)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaSearchExternalFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            query=NotImplemented,
            utcOffsetEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy)

        # Query
        # @var string
        self.query = query

        # UtcOffsetEqual
        # @var int
        self.utcOffsetEqual = utcOffsetEqual

        # Comma separated list of asset types to search within. 
        #             Possible values: 0 – EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted – all types should be included.
        # @var string
        self.typeIn = typeIn


    PROPERTY_LOADERS = {
        'query': getXmlNodeText, 
        'utcOffsetEqual': getXmlNodeInt, 
        'typeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchExternalFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaSearchExternalFilter")
        kparams.addStringIfDefined("query", self.query)
        kparams.addIntIfDefined("utcOffsetEqual", self.utcOffsetEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        return kparams

    def getQuery(self):
        return self.query

    def setQuery(self, newQuery):
        self.query = newQuery

    def getUtcOffsetEqual(self):
        return self.utcOffsetEqual

    def setUtcOffsetEqual(self, newUtcOffsetEqual):
        self.utcOffsetEqual = newUtcOffsetEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn


# @package Kaltura
# @subpackage Client
class KalturaAssetFileContext(KalturaObjectBase):
    def __init__(self,
            viewLifeCycle=NotImplemented,
            fullLifeCycle=NotImplemented,
            isOfflinePlayBack=NotImplemented):
        KalturaObjectBase.__init__(self)

        # viewLifeCycle
        # @var string
        # @readonly
        self.viewLifeCycle = viewLifeCycle

        # fullLifeCycle
        # @var string
        # @readonly
        self.fullLifeCycle = fullLifeCycle

        # isOfflinePlayBack
        # @var bool
        # @readonly
        self.isOfflinePlayBack = isOfflinePlayBack


    PROPERTY_LOADERS = {
        'viewLifeCycle': getXmlNodeText, 
        'fullLifeCycle': getXmlNodeText, 
        'isOfflinePlayBack': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetFileContext.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetFileContext")
        return kparams

    def getViewLifeCycle(self):
        return self.viewLifeCycle

    def getFullLifeCycle(self):
        return self.fullLifeCycle

    def getIsOfflinePlayBack(self):
        return self.isOfflinePlayBack


# @package Kaltura
# @subpackage Client
class KalturaAssetStatisticsQuery(KalturaObjectBase):
    def __init__(self,
            assetIdIn=NotImplemented,
            assetTypeEqual=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            endDateGreaterThanOrEqual=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Comma separated list of asset identifiers.
        # @var string
        self.assetIdIn = assetIdIn

        # Asset type
        # @var KalturaAssetType
        self.assetTypeEqual = assetTypeEqual

        # The beginning of the time window to get the statistics for (in epoch).
        # @var int
        self.startDateGreaterThanOrEqual = startDateGreaterThanOrEqual

        # /// The end of the time window to get the statistics for (in epoch).
        # @var int
        self.endDateGreaterThanOrEqual = endDateGreaterThanOrEqual


    PROPERTY_LOADERS = {
        'assetIdIn': getXmlNodeText, 
        'assetTypeEqual': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
        'startDateGreaterThanOrEqual': getXmlNodeInt, 
        'endDateGreaterThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStatisticsQuery.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetStatisticsQuery")
        kparams.addStringIfDefined("assetIdIn", self.assetIdIn)
        kparams.addStringEnumIfDefined("assetTypeEqual", self.assetTypeEqual)
        kparams.addIntIfDefined("startDateGreaterThanOrEqual", self.startDateGreaterThanOrEqual)
        kparams.addIntIfDefined("endDateGreaterThanOrEqual", self.endDateGreaterThanOrEqual)
        return kparams

    def getAssetIdIn(self):
        return self.assetIdIn

    def setAssetIdIn(self, newAssetIdIn):
        self.assetIdIn = newAssetIdIn

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual

    def getStartDateGreaterThanOrEqual(self):
        return self.startDateGreaterThanOrEqual

    def setStartDateGreaterThanOrEqual(self, newStartDateGreaterThanOrEqual):
        self.startDateGreaterThanOrEqual = newStartDateGreaterThanOrEqual

    def getEndDateGreaterThanOrEqual(self):
        return self.endDateGreaterThanOrEqual

    def setEndDateGreaterThanOrEqual(self, newEndDateGreaterThanOrEqual):
        self.endDateGreaterThanOrEqual = newEndDateGreaterThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaCDNPartnerSettings(KalturaObjectBase):
    def __init__(self,
            defaultAdapterId=NotImplemented,
            defaultRecordingAdapterId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Default CDN adapter identifier
        # @var int
        self.defaultAdapterId = defaultAdapterId

        # Default recording CDN adapter identifier
        # @var int
        self.defaultRecordingAdapterId = defaultRecordingAdapterId


    PROPERTY_LOADERS = {
        'defaultAdapterId': getXmlNodeInt, 
        'defaultRecordingAdapterId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDNPartnerSettings.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCDNPartnerSettings")
        kparams.addIntIfDefined("defaultAdapterId", self.defaultAdapterId)
        kparams.addIntIfDefined("defaultRecordingAdapterId", self.defaultRecordingAdapterId)
        return kparams

    def getDefaultAdapterId(self):
        return self.defaultAdapterId

    def setDefaultAdapterId(self, newDefaultAdapterId):
        self.defaultAdapterId = newDefaultAdapterId

    def getDefaultRecordingAdapterId(self):
        return self.defaultRecordingAdapterId

    def setDefaultRecordingAdapterId(self, newDefaultRecordingAdapterId):
        self.defaultRecordingAdapterId = newDefaultRecordingAdapterId


# @package Kaltura
# @subpackage Client
class KalturaRegionFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            externalIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # List of comma separated regions external identifiers
        # @var string
        self.externalIdIn = externalIdIn


    PROPERTY_LOADERS = {
        'externalIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaRegionFilter")
        kparams.addStringIfDefined("externalIdIn", self.externalIdIn)
        return kparams

    def getExternalIdIn(self):
        return self.externalIdIn

    def setExternalIdIn(self, newExternalIdIn):
        self.externalIdIn = newExternalIdIn


# @package Kaltura
# @subpackage Client
class KalturaAssetCommentFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            assetIdEqual=NotImplemented,
            assetTypeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Asset Id
        # @var int
        self.assetIdEqual = assetIdEqual

        # Asset Type
        # @var KalturaAssetType
        self.assetTypeEqual = assetTypeEqual


    PROPERTY_LOADERS = {
        'assetIdEqual': getXmlNodeInt, 
        'assetTypeEqual': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetCommentFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetCommentFilter")
        kparams.addIntIfDefined("assetIdEqual", self.assetIdEqual)
        kparams.addStringEnumIfDefined("assetTypeEqual", self.assetTypeEqual)
        return kparams

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaKeyValue(KalturaObjectBase):
    def __init__(self,
            key=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var string
        self.key = key

        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'key': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaKeyValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaKeyValue")
        kparams.addStringIfDefined("key", self.key)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaPaymentGatewayConfiguration(KalturaObjectBase):
    def __init__(self,
            paymentGatewayeConfiguration=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Payment gateway configuration
        # @var array of KalturaKeyValue
        self.paymentGatewayeConfiguration = paymentGatewayeConfiguration


    PROPERTY_LOADERS = {
        'paymentGatewayeConfiguration': (KalturaObjectFactory.createArray, KalturaKeyValue), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentGatewayConfiguration.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPaymentGatewayConfiguration")
        kparams.addArrayIfDefined("paymentGatewayeConfiguration", self.paymentGatewayeConfiguration)
        return kparams

    def getPaymentGatewayeConfiguration(self):
        return self.paymentGatewayeConfiguration

    def setPaymentGatewayeConfiguration(self, newPaymentGatewayeConfiguration):
        self.paymentGatewayeConfiguration = newPaymentGatewayeConfiguration


# @package Kaltura
# @subpackage Client
class KalturaProductPriceFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            subscriptionIdIn=NotImplemented,
            fileIdIn=NotImplemented,
            isLowest=NotImplemented,
            couponCodeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated subscriptions identifiers
        # @var string
        self.subscriptionIdIn = subscriptionIdIn

        # Comma separated media files identifiers
        # @var string
        self.fileIdIn = fileIdIn

        # A flag that indicates if only the lowest price of an item should return
        # @var bool
        self.isLowest = isLowest

        # Discount coupon code
        # @var string
        self.couponCodeEqual = couponCodeEqual


    PROPERTY_LOADERS = {
        'subscriptionIdIn': getXmlNodeText, 
        'fileIdIn': getXmlNodeText, 
        'isLowest': getXmlNodeBool, 
        'couponCodeEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductPriceFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaProductPriceFilter")
        kparams.addStringIfDefined("subscriptionIdIn", self.subscriptionIdIn)
        kparams.addStringIfDefined("fileIdIn", self.fileIdIn)
        kparams.addBoolIfDefined("isLowest", self.isLowest)
        kparams.addStringIfDefined("couponCodeEqual", self.couponCodeEqual)
        return kparams

    def getSubscriptionIdIn(self):
        return self.subscriptionIdIn

    def setSubscriptionIdIn(self, newSubscriptionIdIn):
        self.subscriptionIdIn = newSubscriptionIdIn

    def getFileIdIn(self):
        return self.fileIdIn

    def setFileIdIn(self, newFileIdIn):
        self.fileIdIn = newFileIdIn

    def getIsLowest(self):
        return self.isLowest

    def setIsLowest(self, newIsLowest):
        self.isLowest = newIsLowest

    def getCouponCodeEqual(self):
        return self.couponCodeEqual

    def setCouponCodeEqual(self, newCouponCodeEqual):
        self.couponCodeEqual = newCouponCodeEqual


# @package Kaltura
# @subpackage Client
class KalturaSeriesRecordingFilter(KalturaFilter):
    """Filtering recordings"""

    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeriesRecordingFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSeriesRecordingFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaHouseholdQuota(KalturaObjectBase):
    def __init__(self,
            householdId=NotImplemented,
            totalQuota=NotImplemented,
            availableQuota=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Household identifier
        # @var int
        # @readonly
        self.householdId = householdId

        # Total quota that is allocated to the household
        # @var int
        # @readonly
        self.totalQuota = totalQuota

        # Available quota that household has remaining
        # @var int
        # @readonly
        self.availableQuota = availableQuota


    PROPERTY_LOADERS = {
        'householdId': getXmlNodeInt, 
        'totalQuota': getXmlNodeInt, 
        'availableQuota': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdQuota.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdQuota")
        return kparams

    def getHouseholdId(self):
        return self.householdId

    def getTotalQuota(self):
        return self.totalQuota

    def getAvailableQuota(self):
        return self.availableQuota


# @package Kaltura
# @subpackage Client
class KalturaInboxMessageFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # List of inbox message types to search within.
        # @var string
        self.typeIn = typeIn

        # createdAtGreaterThanOrEqual
        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # createdAtLessThanOrEqual
        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'typeIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInboxMessageFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaInboxMessageFilter")
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        return kparams

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaMessageTemplate(KalturaObjectBase):
    def __init__(self,
            message=NotImplemented,
            dateFormat=NotImplemented,
            assetType=NotImplemented,
            sound=NotImplemented,
            action=NotImplemented,
            url=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The message template with placeholders
        # @var string
        self.message = message

        # Default date format for the date &amp; time entries used in the template
        # @var string
        self.dateFormat = dateFormat

        # Template type. Possible values: Series
        # @var KalturaOTTAssetType
        self.assetType = assetType

        # Sound file name to play upon message arrival to the device (if supported by target device)
        # @var string
        self.sound = sound

        # an optional action
        # @var string
        self.action = action

        # URL template for deep linking. Example - /app/location/{mediaId}
        # @var string
        self.url = url


    PROPERTY_LOADERS = {
        'message': getXmlNodeText, 
        'dateFormat': getXmlNodeText, 
        'assetType': (KalturaEnumsFactory.createInt, "KalturaOTTAssetType"), 
        'sound': getXmlNodeText, 
        'action': getXmlNodeText, 
        'url': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMessageTemplate.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMessageTemplate")
        kparams.addStringIfDefined("message", self.message)
        kparams.addStringIfDefined("dateFormat", self.dateFormat)
        kparams.addIntEnumIfDefined("assetType", self.assetType)
        kparams.addStringIfDefined("sound", self.sound)
        kparams.addStringIfDefined("action", self.action)
        kparams.addStringIfDefined("url", self.url)
        return kparams

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage):
        self.message = newMessage

    def getDateFormat(self):
        return self.dateFormat

    def setDateFormat(self, newDateFormat):
        self.dateFormat = newDateFormat

    def getAssetType(self):
        return self.assetType

    def setAssetType(self, newAssetType):
        self.assetType = newAssetType

    def getSound(self):
        return self.sound

    def setSound(self, newSound):
        self.sound = newSound

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl


# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeriesFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFollowTvSeriesFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaFollowTvSeriesFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPersonalFeedFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPersonalFeedFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPpv(KalturaObjectBase):
    """PPV details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            price=NotImplemented,
            fileTypes=NotImplemented,
            discountModules=NotImplemented,
            couponsGroup=NotImplemented,
            descriptions=NotImplemented,
            productCode=NotImplemented,
            isSubscriptionOnly=NotImplemented,
            firstDeviceLimitation=NotImplemented,
            usageModule=NotImplemented):
        KalturaObjectBase.__init__(self)

        # PPV identifier
        # @var string
        self.id = id

        # the name for the ppv
        # @var string
        self.name = name

        # The price of the ppv
        # @var KalturaPriceDetails
        self.price = price

        # A list of file types identifiers that are supported in this ppv
        # @var array of KalturaIntegerValue
        self.fileTypes = fileTypes

        # The internal discount module for the ppv
        # @var KalturaDiscountModule
        self.discountModules = discountModules

        # Coupons group for the ppv
        # @var KalturaCouponsGroup
        self.couponsGroup = couponsGroup

        # A list of the descriptions of the ppv on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.descriptions = descriptions

        # Product code for the ppv
        # @var string
        self.productCode = productCode

        # Indicates whether or not this ppv can be purchased standalone or only as part of a subscription
        # @var bool
        self.isSubscriptionOnly = isSubscriptionOnly

        # Indicates whether or not this ppv can be consumed only on the first device
        # @var bool
        self.firstDeviceLimitation = firstDeviceLimitation

        # PPV usage module
        # @var KalturaUsageModule
        self.usageModule = usageModule


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'price': (KalturaObjectFactory.create, KalturaPriceDetails), 
        'fileTypes': (KalturaObjectFactory.createArray, KalturaIntegerValue), 
        'discountModules': (KalturaObjectFactory.create, KalturaDiscountModule), 
        'couponsGroup': (KalturaObjectFactory.create, KalturaCouponsGroup), 
        'descriptions': (KalturaObjectFactory.createArray, KalturaTranslationToken), 
        'productCode': getXmlNodeText, 
        'isSubscriptionOnly': getXmlNodeBool, 
        'firstDeviceLimitation': getXmlNodeBool, 
        'usageModule': (KalturaObjectFactory.create, KalturaUsageModule), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPpv.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPpv")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        kparams.addObjectIfDefined("price", self.price)
        kparams.addArrayIfDefined("fileTypes", self.fileTypes)
        kparams.addObjectIfDefined("discountModules", self.discountModules)
        kparams.addObjectIfDefined("couponsGroup", self.couponsGroup)
        kparams.addArrayIfDefined("descriptions", self.descriptions)
        kparams.addStringIfDefined("productCode", self.productCode)
        kparams.addBoolIfDefined("isSubscriptionOnly", self.isSubscriptionOnly)
        kparams.addBoolIfDefined("firstDeviceLimitation", self.firstDeviceLimitation)
        kparams.addObjectIfDefined("usageModule", self.usageModule)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getFileTypes(self):
        return self.fileTypes

    def setFileTypes(self, newFileTypes):
        self.fileTypes = newFileTypes

    def getDiscountModules(self):
        return self.discountModules

    def setDiscountModules(self, newDiscountModules):
        self.discountModules = newDiscountModules

    def getCouponsGroup(self):
        return self.couponsGroup

    def setCouponsGroup(self, newCouponsGroup):
        self.couponsGroup = newCouponsGroup

    def getDescriptions(self):
        return self.descriptions

    def setDescriptions(self, newDescriptions):
        self.descriptions = newDescriptions

    def getProductCode(self):
        return self.productCode

    def setProductCode(self, newProductCode):
        self.productCode = newProductCode

    def getIsSubscriptionOnly(self):
        return self.isSubscriptionOnly

    def setIsSubscriptionOnly(self, newIsSubscriptionOnly):
        self.isSubscriptionOnly = newIsSubscriptionOnly

    def getFirstDeviceLimitation(self):
        return self.firstDeviceLimitation

    def setFirstDeviceLimitation(self, newFirstDeviceLimitation):
        self.firstDeviceLimitation = newFirstDeviceLimitation

    def getUsageModule(self):
        return self.usageModule

    def setUsageModule(self, newUsageModule):
        self.usageModule = newUsageModule


# @package Kaltura
# @subpackage Client
class KalturaRecordingFilter(KalturaFilter):
    """Filtering recordings"""

    def __init__(self,
            orderBy=NotImplemented,
            statusIn=NotImplemented,
            filterExpression=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Recording Statuses
        # @var string
        self.statusIn = statusIn

        # KSQL expression
        # @var string
        self.filterExpression = filterExpression


    PROPERTY_LOADERS = {
        'statusIn': getXmlNodeText, 
        'filterExpression': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecordingFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaRecordingFilter")
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("filterExpression", self.filterExpression)
        return kparams

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getFilterExpression(self):
        return self.filterExpression

    def setFilterExpression(self, newFilterExpression):
        self.filterExpression = newFilterExpression


# @package Kaltura
# @subpackage Client
class KalturaLicensedUrl(KalturaObjectBase):
    def __init__(self,
            mainUrl=NotImplemented,
            altUrl=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Main licensed URL
        # @var string
        self.mainUrl = mainUrl

        # An alternate URL to use in case the main fails
        # @var string
        self.altUrl = altUrl


    PROPERTY_LOADERS = {
        'mainUrl': getXmlNodeText, 
        'altUrl': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLicensedUrl.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLicensedUrl")
        kparams.addStringIfDefined("mainUrl", self.mainUrl)
        kparams.addStringIfDefined("altUrl", self.altUrl)
        return kparams

    def getMainUrl(self):
        return self.mainUrl

    def setMainUrl(self, newMainUrl):
        self.mainUrl = newMainUrl

    def getAltUrl(self):
        return self.altUrl

    def setAltUrl(self, newAltUrl):
        self.altUrl = newAltUrl


# @package Kaltura
# @subpackage Client
class KalturaLicensedUrlBaseRequest(KalturaObjectBase):
    def __init__(self,
            assetId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Asset identifier
        # @var string
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLicensedUrlBaseRequest.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLicensedUrlBaseRequest")
        kparams.addStringIfDefined("assetId", self.assetId)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId


# @package Kaltura
# @subpackage Client
class KalturaLicensedUrlMediaRequest(KalturaLicensedUrlBaseRequest):
    def __init__(self,
            assetId=NotImplemented,
            contentId=NotImplemented,
            baseUrl=NotImplemented):
        KalturaLicensedUrlBaseRequest.__init__(self,
            assetId)

        # Identifier of the content to get the link for (file identifier)
        # @var int
        self.contentId = contentId

        # Base URL for the licensed URLs
        # @var string
        self.baseUrl = baseUrl


    PROPERTY_LOADERS = {
        'contentId': getXmlNodeInt, 
        'baseUrl': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaLicensedUrlBaseRequest.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLicensedUrlMediaRequest.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLicensedUrlBaseRequest.toParams(self)
        kparams.put("objectType", "KalturaLicensedUrlMediaRequest")
        kparams.addIntIfDefined("contentId", self.contentId)
        kparams.addStringIfDefined("baseUrl", self.baseUrl)
        return kparams

    def getContentId(self):
        return self.contentId

    def setContentId(self, newContentId):
        self.contentId = newContentId

    def getBaseUrl(self):
        return self.baseUrl

    def setBaseUrl(self, newBaseUrl):
        self.baseUrl = newBaseUrl


# @package Kaltura
# @subpackage Client
class KalturaLicensedUrlEpgRequest(KalturaLicensedUrlMediaRequest):
    def __init__(self,
            assetId=NotImplemented,
            contentId=NotImplemented,
            baseUrl=NotImplemented,
            streamType=NotImplemented,
            startDate=NotImplemented):
        KalturaLicensedUrlMediaRequest.__init__(self,
            assetId,
            contentId,
            baseUrl)

        # The stream type to get the URL for
        # @var KalturaStreamType
        self.streamType = streamType

        # The start date of the stream (epoch)
        # @var int
        self.startDate = startDate


    PROPERTY_LOADERS = {
        'streamType': (KalturaEnumsFactory.createString, "KalturaStreamType"), 
        'startDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaLicensedUrlMediaRequest.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLicensedUrlEpgRequest.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLicensedUrlMediaRequest.toParams(self)
        kparams.put("objectType", "KalturaLicensedUrlEpgRequest")
        kparams.addStringEnumIfDefined("streamType", self.streamType)
        kparams.addIntIfDefined("startDate", self.startDate)
        return kparams

    def getStreamType(self):
        return self.streamType

    def setStreamType(self, newStreamType):
        self.streamType = newStreamType

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate


# @package Kaltura
# @subpackage Client
class KalturaLicensedUrlRecordingRequest(KalturaLicensedUrlBaseRequest):
    def __init__(self,
            assetId=NotImplemented,
            fileType=NotImplemented):
        KalturaLicensedUrlBaseRequest.__init__(self,
            assetId)

        # The file type for the URL
        # @var string
        self.fileType = fileType


    PROPERTY_LOADERS = {
        'fileType': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaLicensedUrlBaseRequest.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLicensedUrlRecordingRequest.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaLicensedUrlBaseRequest.toParams(self)
        kparams.put("objectType", "KalturaLicensedUrlRecordingRequest")
        kparams.addStringIfDefined("fileType", self.fileType)
        return kparams

    def getFileType(self):
        return self.fileType

    def setFileType(self, newFileType):
        self.fileType = newFileType


# @package Kaltura
# @subpackage Client
class KalturaRegistryResponse(KalturaObjectBase):
    def __init__(self,
            announcementId=NotImplemented,
            key=NotImplemented,
            url=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Announcement Id
        # @var int
        self.announcementId = announcementId

        # Key
        # @var string
        self.key = key

        # URL
        # @var string
        self.url = url


    PROPERTY_LOADERS = {
        'announcementId': getXmlNodeInt, 
        'key': getXmlNodeText, 
        'url': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegistryResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRegistryResponse")
        kparams.addIntIfDefined("announcementId", self.announcementId)
        kparams.addStringIfDefined("key", self.key)
        kparams.addStringIfDefined("url", self.url)
        return kparams

    def getAnnouncementId(self):
        return self.announcementId

    def setAnnouncementId(self, newAnnouncementId):
        self.announcementId = newAnnouncementId

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl


# @package Kaltura
# @subpackage Client
class KalturaNotificationsPartnerSettings(KalturaObjectBase):
    def __init__(self,
            pushNotificationEnabled=NotImplemented,
            pushSystemAnnouncementsEnabled=NotImplemented,
            pushStartHour=NotImplemented,
            pushEndHour=NotImplemented,
            inboxEnabled=NotImplemented,
            messageTTLDays=NotImplemented,
            automaticIssueFollowNotification=NotImplemented,
            topicExpirationDurationDays=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Push notification capability is enabled for the account
        # @var bool
        self.pushNotificationEnabled = pushNotificationEnabled

        # System announcement capability is enabled for the account
        # @var bool
        self.pushSystemAnnouncementsEnabled = pushSystemAnnouncementsEnabled

        # Window start time (UTC) for send automated push messages
        # @var int
        self.pushStartHour = pushStartHour

        # Window end time (UTC) for send automated push messages
        # @var int
        self.pushEndHour = pushEndHour

        # Inbox enabled
        # @var bool
        self.inboxEnabled = inboxEnabled

        # Message TTL in days
        # @var int
        self.messageTTLDays = messageTTLDays

        # Automatic issue follow notification
        # @var bool
        self.automaticIssueFollowNotification = automaticIssueFollowNotification

        # Topic expiration duration in days
        # @var int
        self.topicExpirationDurationDays = topicExpirationDurationDays


    PROPERTY_LOADERS = {
        'pushNotificationEnabled': getXmlNodeBool, 
        'pushSystemAnnouncementsEnabled': getXmlNodeBool, 
        'pushStartHour': getXmlNodeInt, 
        'pushEndHour': getXmlNodeInt, 
        'inboxEnabled': getXmlNodeBool, 
        'messageTTLDays': getXmlNodeInt, 
        'automaticIssueFollowNotification': getXmlNodeBool, 
        'topicExpirationDurationDays': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaNotificationsPartnerSettings.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaNotificationsPartnerSettings")
        kparams.addBoolIfDefined("pushNotificationEnabled", self.pushNotificationEnabled)
        kparams.addBoolIfDefined("pushSystemAnnouncementsEnabled", self.pushSystemAnnouncementsEnabled)
        kparams.addIntIfDefined("pushStartHour", self.pushStartHour)
        kparams.addIntIfDefined("pushEndHour", self.pushEndHour)
        kparams.addBoolIfDefined("inboxEnabled", self.inboxEnabled)
        kparams.addIntIfDefined("messageTTLDays", self.messageTTLDays)
        kparams.addBoolIfDefined("automaticIssueFollowNotification", self.automaticIssueFollowNotification)
        kparams.addIntIfDefined("topicExpirationDurationDays", self.topicExpirationDurationDays)
        return kparams

    def getPushNotificationEnabled(self):
        return self.pushNotificationEnabled

    def setPushNotificationEnabled(self, newPushNotificationEnabled):
        self.pushNotificationEnabled = newPushNotificationEnabled

    def getPushSystemAnnouncementsEnabled(self):
        return self.pushSystemAnnouncementsEnabled

    def setPushSystemAnnouncementsEnabled(self, newPushSystemAnnouncementsEnabled):
        self.pushSystemAnnouncementsEnabled = newPushSystemAnnouncementsEnabled

    def getPushStartHour(self):
        return self.pushStartHour

    def setPushStartHour(self, newPushStartHour):
        self.pushStartHour = newPushStartHour

    def getPushEndHour(self):
        return self.pushEndHour

    def setPushEndHour(self, newPushEndHour):
        self.pushEndHour = newPushEndHour

    def getInboxEnabled(self):
        return self.inboxEnabled

    def setInboxEnabled(self, newInboxEnabled):
        self.inboxEnabled = newInboxEnabled

    def getMessageTTLDays(self):
        return self.messageTTLDays

    def setMessageTTLDays(self, newMessageTTLDays):
        self.messageTTLDays = newMessageTTLDays

    def getAutomaticIssueFollowNotification(self):
        return self.automaticIssueFollowNotification

    def setAutomaticIssueFollowNotification(self, newAutomaticIssueFollowNotification):
        self.automaticIssueFollowNotification = newAutomaticIssueFollowNotification

    def getTopicExpirationDurationDays(self):
        return self.topicExpirationDurationDays

    def setTopicExpirationDurationDays(self, newTopicExpirationDurationDays):
        self.topicExpirationDurationDays = newTopicExpirationDurationDays


# @package Kaltura
# @subpackage Client
class KalturaNotificationsSettings(KalturaObjectBase):
    def __init__(self,
            pushNotificationEnabled=NotImplemented,
            pushFollowEnabled=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Specify if the user want to receive push notifications or not
        # @var bool
        self.pushNotificationEnabled = pushNotificationEnabled

        # Specify if the user will be notified for followed content via push. (requires push_notification_enabled to be enabled)
        # @var bool
        self.pushFollowEnabled = pushFollowEnabled


    PROPERTY_LOADERS = {
        'pushNotificationEnabled': getXmlNodeBool, 
        'pushFollowEnabled': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaNotificationsSettings.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaNotificationsSettings")
        kparams.addBoolIfDefined("pushNotificationEnabled", self.pushNotificationEnabled)
        kparams.addBoolIfDefined("pushFollowEnabled", self.pushFollowEnabled)
        return kparams

    def getPushNotificationEnabled(self):
        return self.pushNotificationEnabled

    def setPushNotificationEnabled(self, newPushNotificationEnabled):
        self.pushNotificationEnabled = newPushNotificationEnabled

    def getPushFollowEnabled(self):
        return self.pushFollowEnabled

    def setPushFollowEnabled(self, newPushFollowEnabled):
        self.pushFollowEnabled = newPushFollowEnabled


# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfileFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            paymentGatewayIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Payment gateway identifier to list the payment methods for
        # @var int
        self.paymentGatewayIdEqual = paymentGatewayIdEqual


    PROPERTY_LOADERS = {
        'paymentGatewayIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentMethodProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPaymentMethodProfileFilter")
        kparams.addIntIfDefined("paymentGatewayIdEqual", self.paymentGatewayIdEqual)
        return kparams

    def getPaymentGatewayIdEqual(self):
        return self.paymentGatewayIdEqual

    def setPaymentGatewayIdEqual(self, newPaymentGatewayIdEqual):
        self.paymentGatewayIdEqual = newPaymentGatewayIdEqual


# @package Kaltura
# @subpackage Client
class KalturaTimeShiftedTvPartnerSettings(KalturaObjectBase):
    def __init__(self,
            catchUpEnabled=NotImplemented,
            cdvrEnabled=NotImplemented,
            startOverEnabled=NotImplemented,
            trickPlayEnabled=NotImplemented,
            recordingScheduleWindowEnabled=NotImplemented,
            protectionEnabled=NotImplemented,
            catchUpBufferLength=NotImplemented,
            trickPlayBufferLength=NotImplemented,
            recordingScheduleWindow=NotImplemented,
            paddingBeforeProgramStarts=NotImplemented,
            paddingAfterProgramEnds=NotImplemented,
            protectionPeriod=NotImplemented,
            protectionQuotaPercentage=NotImplemented,
            recordingLifetimePeriod=NotImplemented,
            cleanupNoticePeroid=NotImplemented,
            seriesRecordingEnabled=NotImplemented,
            nonEntitledChannelPlaybackEnabled=NotImplemented,
            nonExistingChannelPlaybackEnabled=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Is catch-up enabled
        # @var bool
        self.catchUpEnabled = catchUpEnabled

        # Is c-dvr enabled
        # @var bool
        self.cdvrEnabled = cdvrEnabled

        # Is start-over enabled
        # @var bool
        self.startOverEnabled = startOverEnabled

        # Is trick-play enabled
        # @var bool
        self.trickPlayEnabled = trickPlayEnabled

        # Is recording schedule window enabled
        # @var bool
        self.recordingScheduleWindowEnabled = recordingScheduleWindowEnabled

        # Is recording protection enabled
        # @var bool
        self.protectionEnabled = protectionEnabled

        # Catch-up buffer length
        # @var int
        self.catchUpBufferLength = catchUpBufferLength

        # Trick play buffer length
        # @var int
        self.trickPlayBufferLength = trickPlayBufferLength

        # Recording schedule window. Indicates how long (in minutes) after the program starts it is allowed to schedule the recording
        # @var int
        self.recordingScheduleWindow = recordingScheduleWindow

        # Indicates how long (in seconds) before the program starts the recording will begin
        # @var int
        self.paddingBeforeProgramStarts = paddingBeforeProgramStarts

        # Indicates how long (in seconds) after the program ends the recording will end
        # @var int
        self.paddingAfterProgramEnds = paddingAfterProgramEnds

        # Specify the time in days that a recording should be protected. Start time begins at protection request.
        # @var int
        self.protectionPeriod = protectionPeriod

        # Indicates how many percent of the quota can be used for protection
        # @var int
        self.protectionQuotaPercentage = protectionQuotaPercentage

        # Specify the time in days that a recording should be kept for user. Start time begins with the program end date.
        # @var int
        self.recordingLifetimePeriod = recordingLifetimePeriod

        # The time in days before the recording lifetime is due from which the client should be able to warn user about deletion.
        # @var int
        self.cleanupNoticePeroid = cleanupNoticePeroid

        # Is recording of series enabled
        # @var bool
        self.seriesRecordingEnabled = seriesRecordingEnabled

        # Is recording playback for non-entitled channel enables
        # @var bool
        self.nonEntitledChannelPlaybackEnabled = nonEntitledChannelPlaybackEnabled

        # Is recording playback for non-existing channel enables
        # @var bool
        self.nonExistingChannelPlaybackEnabled = nonExistingChannelPlaybackEnabled


    PROPERTY_LOADERS = {
        'catchUpEnabled': getXmlNodeBool, 
        'cdvrEnabled': getXmlNodeBool, 
        'startOverEnabled': getXmlNodeBool, 
        'trickPlayEnabled': getXmlNodeBool, 
        'recordingScheduleWindowEnabled': getXmlNodeBool, 
        'protectionEnabled': getXmlNodeBool, 
        'catchUpBufferLength': getXmlNodeInt, 
        'trickPlayBufferLength': getXmlNodeInt, 
        'recordingScheduleWindow': getXmlNodeInt, 
        'paddingBeforeProgramStarts': getXmlNodeInt, 
        'paddingAfterProgramEnds': getXmlNodeInt, 
        'protectionPeriod': getXmlNodeInt, 
        'protectionQuotaPercentage': getXmlNodeInt, 
        'recordingLifetimePeriod': getXmlNodeInt, 
        'cleanupNoticePeroid': getXmlNodeInt, 
        'seriesRecordingEnabled': getXmlNodeBool, 
        'nonEntitledChannelPlaybackEnabled': getXmlNodeBool, 
        'nonExistingChannelPlaybackEnabled': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTimeShiftedTvPartnerSettings.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTimeShiftedTvPartnerSettings")
        kparams.addBoolIfDefined("catchUpEnabled", self.catchUpEnabled)
        kparams.addBoolIfDefined("cdvrEnabled", self.cdvrEnabled)
        kparams.addBoolIfDefined("startOverEnabled", self.startOverEnabled)
        kparams.addBoolIfDefined("trickPlayEnabled", self.trickPlayEnabled)
        kparams.addBoolIfDefined("recordingScheduleWindowEnabled", self.recordingScheduleWindowEnabled)
        kparams.addBoolIfDefined("protectionEnabled", self.protectionEnabled)
        kparams.addIntIfDefined("catchUpBufferLength", self.catchUpBufferLength)
        kparams.addIntIfDefined("trickPlayBufferLength", self.trickPlayBufferLength)
        kparams.addIntIfDefined("recordingScheduleWindow", self.recordingScheduleWindow)
        kparams.addIntIfDefined("paddingBeforeProgramStarts", self.paddingBeforeProgramStarts)
        kparams.addIntIfDefined("paddingAfterProgramEnds", self.paddingAfterProgramEnds)
        kparams.addIntIfDefined("protectionPeriod", self.protectionPeriod)
        kparams.addIntIfDefined("protectionQuotaPercentage", self.protectionQuotaPercentage)
        kparams.addIntIfDefined("recordingLifetimePeriod", self.recordingLifetimePeriod)
        kparams.addIntIfDefined("cleanupNoticePeroid", self.cleanupNoticePeroid)
        kparams.addBoolIfDefined("seriesRecordingEnabled", self.seriesRecordingEnabled)
        kparams.addBoolIfDefined("nonEntitledChannelPlaybackEnabled", self.nonEntitledChannelPlaybackEnabled)
        kparams.addBoolIfDefined("nonExistingChannelPlaybackEnabled", self.nonExistingChannelPlaybackEnabled)
        return kparams

    def getCatchUpEnabled(self):
        return self.catchUpEnabled

    def setCatchUpEnabled(self, newCatchUpEnabled):
        self.catchUpEnabled = newCatchUpEnabled

    def getCdvrEnabled(self):
        return self.cdvrEnabled

    def setCdvrEnabled(self, newCdvrEnabled):
        self.cdvrEnabled = newCdvrEnabled

    def getStartOverEnabled(self):
        return self.startOverEnabled

    def setStartOverEnabled(self, newStartOverEnabled):
        self.startOverEnabled = newStartOverEnabled

    def getTrickPlayEnabled(self):
        return self.trickPlayEnabled

    def setTrickPlayEnabled(self, newTrickPlayEnabled):
        self.trickPlayEnabled = newTrickPlayEnabled

    def getRecordingScheduleWindowEnabled(self):
        return self.recordingScheduleWindowEnabled

    def setRecordingScheduleWindowEnabled(self, newRecordingScheduleWindowEnabled):
        self.recordingScheduleWindowEnabled = newRecordingScheduleWindowEnabled

    def getProtectionEnabled(self):
        return self.protectionEnabled

    def setProtectionEnabled(self, newProtectionEnabled):
        self.protectionEnabled = newProtectionEnabled

    def getCatchUpBufferLength(self):
        return self.catchUpBufferLength

    def setCatchUpBufferLength(self, newCatchUpBufferLength):
        self.catchUpBufferLength = newCatchUpBufferLength

    def getTrickPlayBufferLength(self):
        return self.trickPlayBufferLength

    def setTrickPlayBufferLength(self, newTrickPlayBufferLength):
        self.trickPlayBufferLength = newTrickPlayBufferLength

    def getRecordingScheduleWindow(self):
        return self.recordingScheduleWindow

    def setRecordingScheduleWindow(self, newRecordingScheduleWindow):
        self.recordingScheduleWindow = newRecordingScheduleWindow

    def getPaddingBeforeProgramStarts(self):
        return self.paddingBeforeProgramStarts

    def setPaddingBeforeProgramStarts(self, newPaddingBeforeProgramStarts):
        self.paddingBeforeProgramStarts = newPaddingBeforeProgramStarts

    def getPaddingAfterProgramEnds(self):
        return self.paddingAfterProgramEnds

    def setPaddingAfterProgramEnds(self, newPaddingAfterProgramEnds):
        self.paddingAfterProgramEnds = newPaddingAfterProgramEnds

    def getProtectionPeriod(self):
        return self.protectionPeriod

    def setProtectionPeriod(self, newProtectionPeriod):
        self.protectionPeriod = newProtectionPeriod

    def getProtectionQuotaPercentage(self):
        return self.protectionQuotaPercentage

    def setProtectionQuotaPercentage(self, newProtectionQuotaPercentage):
        self.protectionQuotaPercentage = newProtectionQuotaPercentage

    def getRecordingLifetimePeriod(self):
        return self.recordingLifetimePeriod

    def setRecordingLifetimePeriod(self, newRecordingLifetimePeriod):
        self.recordingLifetimePeriod = newRecordingLifetimePeriod

    def getCleanupNoticePeroid(self):
        return self.cleanupNoticePeroid

    def setCleanupNoticePeroid(self, newCleanupNoticePeroid):
        self.cleanupNoticePeroid = newCleanupNoticePeroid

    def getSeriesRecordingEnabled(self):
        return self.seriesRecordingEnabled

    def setSeriesRecordingEnabled(self, newSeriesRecordingEnabled):
        self.seriesRecordingEnabled = newSeriesRecordingEnabled

    def getNonEntitledChannelPlaybackEnabled(self):
        return self.nonEntitledChannelPlaybackEnabled

    def setNonEntitledChannelPlaybackEnabled(self, newNonEntitledChannelPlaybackEnabled):
        self.nonEntitledChannelPlaybackEnabled = newNonEntitledChannelPlaybackEnabled

    def getNonExistingChannelPlaybackEnabled(self):
        return self.nonExistingChannelPlaybackEnabled

    def setNonExistingChannelPlaybackEnabled(self, newNonExistingChannelPlaybackEnabled):
        self.nonExistingChannelPlaybackEnabled = newNonExistingChannelPlaybackEnabled


# @package Kaltura
# @subpackage Client
class KalturaTopicFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTopicFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaTopicFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaUserAssetsListItem(KalturaObjectBase):
    """An item of user asset list"""

    def __init__(self,
            id=NotImplemented,
            orderIndex=NotImplemented,
            type=NotImplemented,
            userId=NotImplemented,
            listType=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Asset identifier
        # @var string
        self.id = id

        # The order index of the asset in the list
        # @var int
        self.orderIndex = orderIndex

        # The type of the asset
        # @var KalturaUserAssetsListItemType
        self.type = type

        # The identifier of the user who added the item to the list
        # @var string
        # @readonly
        self.userId = userId

        # The type of the list
        # @var KalturaUserAssetsListType
        self.listType = listType


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'orderIndex': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaUserAssetsListItemType"), 
        'userId': getXmlNodeText, 
        'listType': (KalturaEnumsFactory.createString, "KalturaUserAssetsListType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserAssetsListItem.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserAssetsListItem")
        kparams.addStringIfDefined("id", self.id)
        kparams.addIntIfDefined("orderIndex", self.orderIndex)
        kparams.addStringEnumIfDefined("type", self.type)
        kparams.addStringEnumIfDefined("listType", self.listType)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getOrderIndex(self):
        return self.orderIndex

    def setOrderIndex(self, newOrderIndex):
        self.orderIndex = newOrderIndex

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getUserId(self):
        return self.userId

    def getListType(self):
        return self.listType

    def setListType(self, newListType):
        self.listType = newListType


# @package Kaltura
# @subpackage Client
class KalturaDeviceFamilyBase(KalturaObjectBase):
    """Device family details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            deviceLimit=NotImplemented,
            concurrentLimit=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Device family identifier
        # @var int
        # @readonly
        self.id = id

        # Device family name
        # @var string
        self.name = name

        # Max number of devices allowed for this family
        # @var int
        self.deviceLimit = deviceLimit

        # Max number of streams allowed for this family
        # @var int
        self.concurrentLimit = concurrentLimit


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'deviceLimit': getXmlNodeInt, 
        'concurrentLimit': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeviceFamilyBase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDeviceFamilyBase")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("deviceLimit", self.deviceLimit)
        kparams.addIntIfDefined("concurrentLimit", self.concurrentLimit)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDeviceLimit(self):
        return self.deviceLimit

    def setDeviceLimit(self, newDeviceLimit):
        self.deviceLimit = newDeviceLimit

    def getConcurrentLimit(self):
        return self.concurrentLimit

    def setConcurrentLimit(self, newConcurrentLimit):
        self.concurrentLimit = newConcurrentLimit


# @package Kaltura
# @subpackage Client
class KalturaHouseholdDevice(KalturaObjectBase):
    """Device details"""

    def __init__(self,
            householdId=NotImplemented,
            udid=NotImplemented,
            name=NotImplemented,
            brand=NotImplemented,
            brandId=NotImplemented,
            activatedOn=NotImplemented,
            status=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Household identifier
        # @var int
        self.householdId = householdId

        # Device UDID
        # @var string
        self.udid = udid

        # Device name
        # @var string
        self.name = name

        # Device brand name
        # @var string
        self.brand = brand

        # Device brand identifier
        # @var int
        self.brandId = brandId

        # Device activation date (epoch)
        # @var int
        self.activatedOn = activatedOn

        # Device state
        # @var KalturaDeviceStatus
        # @readonly
        self.status = status


    PROPERTY_LOADERS = {
        'householdId': getXmlNodeInt, 
        'udid': getXmlNodeText, 
        'name': getXmlNodeText, 
        'brand': getXmlNodeText, 
        'brandId': getXmlNodeInt, 
        'activatedOn': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createString, "KalturaDeviceStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdDevice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdDevice")
        kparams.addIntIfDefined("householdId", self.householdId)
        kparams.addStringIfDefined("udid", self.udid)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("brand", self.brand)
        kparams.addIntIfDefined("brandId", self.brandId)
        kparams.addIntIfDefined("activatedOn", self.activatedOn)
        return kparams

    def getHouseholdId(self):
        return self.householdId

    def setHouseholdId(self, newHouseholdId):
        self.householdId = newHouseholdId

    def getUdid(self):
        return self.udid

    def setUdid(self, newUdid):
        self.udid = newUdid

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getBrand(self):
        return self.brand

    def setBrand(self, newBrand):
        self.brand = newBrand

    def getBrandId(self):
        return self.brandId

    def setBrandId(self, newBrandId):
        self.brandId = newBrandId

    def getActivatedOn(self):
        return self.activatedOn

    def setActivatedOn(self, newActivatedOn):
        self.activatedOn = newActivatedOn

    def getStatus(self):
        return self.status


# @package Kaltura
# @subpackage Client
class KalturaHouseholdDeviceFamilyLimitations(KalturaDeviceFamilyBase):
    """Device family limitations details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            deviceLimit=NotImplemented,
            concurrentLimit=NotImplemented,
            frequency=NotImplemented):
        KalturaDeviceFamilyBase.__init__(self,
            id,
            name,
            deviceLimit,
            concurrentLimit)

        # Allowed device change frequency code
        # @var int
        self.frequency = frequency


    PROPERTY_LOADERS = {
        'frequency': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaDeviceFamilyBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdDeviceFamilyLimitations.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDeviceFamilyBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdDeviceFamilyLimitations")
        kparams.addIntIfDefined("frequency", self.frequency)
        return kparams

    def getFrequency(self):
        return self.frequency

    def setFrequency(self, newFrequency):
        self.frequency = newFrequency


# @package Kaltura
# @subpackage Client
class KalturaHouseholdLimitations(KalturaObjectBase):
    """Household limitations details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            concurrentLimit=NotImplemented,
            deviceLimit=NotImplemented,
            deviceFrequency=NotImplemented,
            deviceFrequencyDescription=NotImplemented,
            userFrequency=NotImplemented,
            userFrequencyDescription=NotImplemented,
            npvrQuotaInSeconds=NotImplemented,
            usersLimit=NotImplemented,
            deviceFamiliesLimitations=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Household limitation module identifier
        # @var int
        # @readonly
        self.id = id

        # Household limitation module name
        # @var string
        self.name = name

        # Max number of streams allowed for the household
        # @var int
        self.concurrentLimit = concurrentLimit

        # Max number of devices allowed for the household
        # @var int
        self.deviceLimit = deviceLimit

        # Allowed device change frequency code
        # @var int
        self.deviceFrequency = deviceFrequency

        # Allowed device change frequency description
        # @var string
        self.deviceFrequencyDescription = deviceFrequencyDescription

        # Allowed user change frequency code
        # @var int
        self.userFrequency = userFrequency

        # Allowed user change frequency description
        # @var string
        self.userFrequencyDescription = userFrequencyDescription

        # Allowed NPVR Quota in Seconds
        # @var int
        self.npvrQuotaInSeconds = npvrQuotaInSeconds

        # Max number of users allowed for the household
        # @var int
        self.usersLimit = usersLimit

        # Device families limitations
        # @var array of KalturaHouseholdDeviceFamilyLimitations
        self.deviceFamiliesLimitations = deviceFamiliesLimitations


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'concurrentLimit': getXmlNodeInt, 
        'deviceLimit': getXmlNodeInt, 
        'deviceFrequency': getXmlNodeInt, 
        'deviceFrequencyDescription': getXmlNodeText, 
        'userFrequency': getXmlNodeInt, 
        'userFrequencyDescription': getXmlNodeText, 
        'npvrQuotaInSeconds': getXmlNodeInt, 
        'usersLimit': getXmlNodeInt, 
        'deviceFamiliesLimitations': (KalturaObjectFactory.createArray, KalturaHouseholdDeviceFamilyLimitations), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdLimitations.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdLimitations")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("concurrentLimit", self.concurrentLimit)
        kparams.addIntIfDefined("deviceLimit", self.deviceLimit)
        kparams.addIntIfDefined("deviceFrequency", self.deviceFrequency)
        kparams.addStringIfDefined("deviceFrequencyDescription", self.deviceFrequencyDescription)
        kparams.addIntIfDefined("userFrequency", self.userFrequency)
        kparams.addStringIfDefined("userFrequencyDescription", self.userFrequencyDescription)
        kparams.addIntIfDefined("npvrQuotaInSeconds", self.npvrQuotaInSeconds)
        kparams.addIntIfDefined("usersLimit", self.usersLimit)
        kparams.addArrayIfDefined("deviceFamiliesLimitations", self.deviceFamiliesLimitations)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getConcurrentLimit(self):
        return self.concurrentLimit

    def setConcurrentLimit(self, newConcurrentLimit):
        self.concurrentLimit = newConcurrentLimit

    def getDeviceLimit(self):
        return self.deviceLimit

    def setDeviceLimit(self, newDeviceLimit):
        self.deviceLimit = newDeviceLimit

    def getDeviceFrequency(self):
        return self.deviceFrequency

    def setDeviceFrequency(self, newDeviceFrequency):
        self.deviceFrequency = newDeviceFrequency

    def getDeviceFrequencyDescription(self):
        return self.deviceFrequencyDescription

    def setDeviceFrequencyDescription(self, newDeviceFrequencyDescription):
        self.deviceFrequencyDescription = newDeviceFrequencyDescription

    def getUserFrequency(self):
        return self.userFrequency

    def setUserFrequency(self, newUserFrequency):
        self.userFrequency = newUserFrequency

    def getUserFrequencyDescription(self):
        return self.userFrequencyDescription

    def setUserFrequencyDescription(self, newUserFrequencyDescription):
        self.userFrequencyDescription = newUserFrequencyDescription

    def getNpvrQuotaInSeconds(self):
        return self.npvrQuotaInSeconds

    def setNpvrQuotaInSeconds(self, newNpvrQuotaInSeconds):
        self.npvrQuotaInSeconds = newNpvrQuotaInSeconds

    def getUsersLimit(self):
        return self.usersLimit

    def setUsersLimit(self, newUsersLimit):
        self.usersLimit = newUsersLimit

    def getDeviceFamiliesLimitations(self):
        return self.deviceFamiliesLimitations

    def setDeviceFamiliesLimitations(self, newDeviceFamiliesLimitations):
        self.deviceFamiliesLimitations = newDeviceFamiliesLimitations


# @package Kaltura
# @subpackage Client
class KalturaExportTaskFilter(KalturaFilter):
    """Bulk export tasks filter"""

    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated tasks identifiers
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExportTaskFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaExportTaskFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaPartnerConfiguration(KalturaObjectBase):
    """Partner  base configuration"""

    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerConfiguration.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPartnerConfiguration")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaBillingPartnerConfig(KalturaPartnerConfiguration):
    """Partner billing configuration"""

    def __init__(self,
            value=NotImplemented,
            type=NotImplemented):
        KalturaPartnerConfiguration.__init__(self)

        # configuration value
        # @var string
        self.value = value

        # partner configuration type
        # @var KalturaPartnerConfigurationType
        self.type = type


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createString, "KalturaPartnerConfigurationType"), 
    }

    def fromXml(self, node):
        KalturaPartnerConfiguration.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBillingPartnerConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPartnerConfiguration.toParams(self)
        kparams.put("objectType", "KalturaBillingPartnerConfig")
        kparams.addStringIfDefined("value", self.value)
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaOSSAdapterBaseProfile(KalturaObjectBase):
    """OSS adapter basic"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # OSS adapter id
        # @var int
        # @readonly
        self.id = id

        # OSS adapter name
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOSSAdapterBaseProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaOSSAdapterBaseProfile")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaOSSAdapterProfile(KalturaOSSAdapterBaseProfile):
    """OSS Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            ossAdapterSettings=NotImplemented,
            externalIdentifier=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaOSSAdapterBaseProfile.__init__(self,
            id,
            name)

        # OSS adapter active status
        # @var bool
        self.isActive = isActive

        # OSS adapter adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # OSS adapter extra parameters
        # @var map
        self.ossAdapterSettings = ossAdapterSettings

        # OSS adapter external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Shared Secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'ossAdapterSettings': (KalturaObjectFactory.create, map), 
        'externalIdentifier': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaOSSAdapterBaseProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOSSAdapterProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaOSSAdapterBaseProfile.toParams(self)
        kparams.put("objectType", "KalturaOSSAdapterProfile")
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addObjectIfDefined("ossAdapterSettings", self.ossAdapterSettings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        return kparams

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getOssAdapterSettings(self):
        return self.ossAdapterSettings

    def setOssAdapterSettings(self, newOssAdapterSettings):
        self.ossAdapterSettings = newOssAdapterSettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getSharedSecret(self):
        return self.sharedSecret


# @package Kaltura
# @subpackage Client
class KalturaLoginSession(KalturaObjectBase):
    """Login response"""

    def __init__(self,
            ks=NotImplemented,
            refreshToken=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Access token in a KS format
        # @var string
        self.ks = ks

        # Refresh Token
        # @var string
        self.refreshToken = refreshToken


    PROPERTY_LOADERS = {
        'ks': getXmlNodeText, 
        'refreshToken': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLoginSession.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLoginSession")
        kparams.addStringIfDefined("ks", self.ks)
        kparams.addStringIfDefined("refreshToken", self.refreshToken)
        return kparams

    def getKs(self):
        return self.ks

    def setKs(self, newKs):
        self.ks = newKs

    def getRefreshToken(self):
        return self.refreshToken

    def setRefreshToken(self, newRefreshToken):
        self.refreshToken = newRefreshToken


# @package Kaltura
# @subpackage Client
class KalturaUserAssetRuleFilter(KalturaFilter):
    """User asset rule filter"""

    def __init__(self,
            orderBy=NotImplemented,
            assetIdEqual=NotImplemented,
            assetTypeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Asset identifier to filter by
        # @var int
        self.assetIdEqual = assetIdEqual

        # Asset type to filter by - 0 = EPG, 1 = media
        # @var int
        self.assetTypeEqual = assetTypeEqual


    PROPERTY_LOADERS = {
        'assetIdEqual': getXmlNodeInt, 
        'assetTypeEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserAssetRuleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserAssetRuleFilter")
        kparams.addIntIfDefined("assetIdEqual", self.assetIdEqual)
        kparams.addIntIfDefined("assetTypeEqual", self.assetTypeEqual)
        return kparams

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaAssetHistoryFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            typeIn=NotImplemented,
            assetIdIn=NotImplemented,
            statusEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated list of asset types to search within.
        #             Possible values: 0 – EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted – all types should be included.
        # @var string
        self.typeIn = typeIn

        # Comma separated list of asset identifiers.
        # @var string
        self.assetIdIn = assetIdIn

        # Which type of recently watched media to include in the result – those that finished watching, those that are in progress or both.
        #             If omitted or specified filter = all – return all types.
        #             Allowed values: progress – return medias that are in-progress, done – return medias that finished watching.
        # @var KalturaWatchStatus
        self.statusEqual = statusEqual


    PROPERTY_LOADERS = {
        'typeIn': getXmlNodeText, 
        'assetIdIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createString, "KalturaWatchStatus"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetHistoryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetHistoryFilter")
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addStringIfDefined("assetIdIn", self.assetIdIn)
        kparams.addStringEnumIfDefined("statusEqual", self.statusEqual)
        return kparams

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getAssetIdIn(self):
        return self.assetIdIn

    def setAssetIdIn(self, newAssetIdIn):
        self.assetIdIn = newAssetIdIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual


# @package Kaltura
# @subpackage Client
class KalturaHousehold(KalturaObjectBase):
    """Household details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            externalId=NotImplemented,
            householdLimitationsId=NotImplemented,
            devicesLimit=NotImplemented,
            usersLimit=NotImplemented,
            concurrentLimit=NotImplemented,
            regionId=NotImplemented,
            state=NotImplemented,
            isFrequencyEnabled=NotImplemented,
            frequencyNextDeviceAction=NotImplemented,
            frequencyNextUserAction=NotImplemented,
            restriction=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Household identifier
        # @var int
        # @readonly
        self.id = id

        # Household name
        # @var string
        self.name = name

        # Household description
        # @var string
        self.description = description

        # Household external identifier
        # @var string
        self.externalId = externalId

        # Household limitation module identifier
        # @var int
        self.householdLimitationsId = householdLimitationsId

        # The max number of the devices that can be added to the household
        # @var int
        self.devicesLimit = devicesLimit

        # The max number of the users that can be added to the household
        # @var int
        self.usersLimit = usersLimit

        # The max number of concurrent streams in the household
        # @var int
        self.concurrentLimit = concurrentLimit

        # The households region identifier
        # @var int
        self.regionId = regionId

        # Household state
        # @var KalturaHouseholdState
        # @readonly
        self.state = state

        # Is household frequency enabled
        # @var bool
        self.isFrequencyEnabled = isFrequencyEnabled

        # The next time a device is allowed to be removed from the household (epoch)
        # @var int
        self.frequencyNextDeviceAction = frequencyNextDeviceAction

        # The next time a user is allowed to be removed from the household (epoch)
        # @var int
        self.frequencyNextUserAction = frequencyNextUserAction

        # Household restriction
        # @var KalturaHouseholdRestriction
        self.restriction = restriction


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'externalId': getXmlNodeText, 
        'householdLimitationsId': getXmlNodeInt, 
        'devicesLimit': getXmlNodeInt, 
        'usersLimit': getXmlNodeInt, 
        'concurrentLimit': getXmlNodeInt, 
        'regionId': getXmlNodeInt, 
        'state': (KalturaEnumsFactory.createString, "KalturaHouseholdState"), 
        'isFrequencyEnabled': getXmlNodeBool, 
        'frequencyNextDeviceAction': getXmlNodeInt, 
        'frequencyNextUserAction': getXmlNodeInt, 
        'restriction': (KalturaEnumsFactory.createString, "KalturaHouseholdRestriction"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHousehold.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHousehold")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addIntIfDefined("householdLimitationsId", self.householdLimitationsId)
        kparams.addIntIfDefined("devicesLimit", self.devicesLimit)
        kparams.addIntIfDefined("usersLimit", self.usersLimit)
        kparams.addIntIfDefined("concurrentLimit", self.concurrentLimit)
        kparams.addIntIfDefined("regionId", self.regionId)
        kparams.addBoolIfDefined("isFrequencyEnabled", self.isFrequencyEnabled)
        kparams.addIntIfDefined("frequencyNextDeviceAction", self.frequencyNextDeviceAction)
        kparams.addIntIfDefined("frequencyNextUserAction", self.frequencyNextUserAction)
        kparams.addStringEnumIfDefined("restriction", self.restriction)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getHouseholdLimitationsId(self):
        return self.householdLimitationsId

    def setHouseholdLimitationsId(self, newHouseholdLimitationsId):
        self.householdLimitationsId = newHouseholdLimitationsId

    def getDevicesLimit(self):
        return self.devicesLimit

    def setDevicesLimit(self, newDevicesLimit):
        self.devicesLimit = newDevicesLimit

    def getUsersLimit(self):
        return self.usersLimit

    def setUsersLimit(self, newUsersLimit):
        self.usersLimit = newUsersLimit

    def getConcurrentLimit(self):
        return self.concurrentLimit

    def setConcurrentLimit(self, newConcurrentLimit):
        self.concurrentLimit = newConcurrentLimit

    def getRegionId(self):
        return self.regionId

    def setRegionId(self, newRegionId):
        self.regionId = newRegionId

    def getState(self):
        return self.state

    def getIsFrequencyEnabled(self):
        return self.isFrequencyEnabled

    def setIsFrequencyEnabled(self, newIsFrequencyEnabled):
        self.isFrequencyEnabled = newIsFrequencyEnabled

    def getFrequencyNextDeviceAction(self):
        return self.frequencyNextDeviceAction

    def setFrequencyNextDeviceAction(self, newFrequencyNextDeviceAction):
        self.frequencyNextDeviceAction = newFrequencyNextDeviceAction

    def getFrequencyNextUserAction(self):
        return self.frequencyNextUserAction

    def setFrequencyNextUserAction(self, newFrequencyNextUserAction):
        self.frequencyNextUserAction = newFrequencyNextUserAction

    def getRestriction(self):
        return self.restriction

    def setRestriction(self, newRestriction):
        self.restriction = newRestriction


# @package Kaltura
# @subpackage Client
class KalturaDevicePin(KalturaObjectBase):
    """Device pin"""

    def __init__(self,
            pin=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Device pin
        # @var string
        self.pin = pin


    PROPERTY_LOADERS = {
        'pin': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDevicePin.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDevicePin")
        kparams.addStringIfDefined("pin", self.pin)
        return kparams

    def getPin(self):
        return self.pin

    def setPin(self, newPin):
        self.pin = newPin


# @package Kaltura
# @subpackage Client
class KalturaBookmarkFilter(KalturaFilter):
    """Filtering Assets requests"""

    def __init__(self,
            orderBy=NotImplemented,
            assetIdIn=NotImplemented,
            assetTypeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated list of assets identifiers
        # @var string
        self.assetIdIn = assetIdIn

        # Asset type
        # @var KalturaAssetType
        self.assetTypeEqual = assetTypeEqual


    PROPERTY_LOADERS = {
        'assetIdIn': getXmlNodeText, 
        'assetTypeEqual': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBookmarkFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBookmarkFilter")
        kparams.addStringIfDefined("assetIdIn", self.assetIdIn)
        kparams.addStringEnumIfDefined("assetTypeEqual", self.assetTypeEqual)
        return kparams

    def getAssetIdIn(self):
        return self.assetIdIn

    def setAssetIdIn(self, newAssetIdIn):
        self.assetIdIn = newAssetIdIn

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaPin(KalturaObjectBase):
    """PIN and its origin of definition"""

    def __init__(self,
            pin=NotImplemented,
            origin=NotImplemented,
            type=NotImplemented):
        KalturaObjectBase.__init__(self)

        # PIN code
        # @var string
        self.pin = pin

        # Where the PIN was defined at – account, household or user
        # @var KalturaRuleLevel
        self.origin = origin

        # PIN type
        # @var KalturaPinType
        self.type = type


    PROPERTY_LOADERS = {
        'pin': getXmlNodeText, 
        'origin': (KalturaEnumsFactory.createString, "KalturaRuleLevel"), 
        'type': (KalturaEnumsFactory.createString, "KalturaPinType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPin.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPin")
        kparams.addStringIfDefined("pin", self.pin)
        kparams.addStringEnumIfDefined("origin", self.origin)
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getPin(self):
        return self.pin

    def setPin(self, newPin):
        self.pin = newPin

    def getOrigin(self):
        return self.origin

    def setOrigin(self, newOrigin):
        self.origin = newOrigin

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaPurchaseSettings(KalturaPin):
    """Purchase settings and PIN"""

    def __init__(self,
            pin=NotImplemented,
            origin=NotImplemented,
            type=NotImplemented,
            permission=NotImplemented):
        KalturaPin.__init__(self,
            pin,
            origin,
            type)

        # Purchase permission - block, ask or allow
        # @var KalturaPurchaseSettingsType
        self.permission = permission


    PROPERTY_LOADERS = {
        'permission': (KalturaEnumsFactory.createString, "KalturaPurchaseSettingsType"), 
    }

    def fromXml(self, node):
        KalturaPin.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPurchaseSettings.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPin.toParams(self)
        kparams.put("objectType", "KalturaPurchaseSettings")
        kparams.addStringEnumIfDefined("permission", self.permission)
        return kparams

    def getPermission(self):
        return self.permission

    def setPermission(self, newPermission):
        self.permission = newPermission


# @package Kaltura
# @subpackage Client
class KalturaHouseholdUser(KalturaObjectBase):
    """Household details"""

    def __init__(self,
            householdId=NotImplemented,
            userId=NotImplemented,
            isMaster=NotImplemented,
            householdMasterUsername=NotImplemented,
            status=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The identifier of the household
        # @var int
        self.householdId = householdId

        # The identifier of the user
        # @var string
        self.userId = userId

        # True if the user added as master use
        # @var bool
        self.isMaster = isMaster

        # The username of the household master for adding a user in status pending for the household master to approve
        # @var string
        # @insertonly
        self.householdMasterUsername = householdMasterUsername

        # The status of the user in the household
        # @var KalturaHouseholdUserStatus
        # @readonly
        self.status = status


    PROPERTY_LOADERS = {
        'householdId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'isMaster': getXmlNodeBool, 
        'householdMasterUsername': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createString, "KalturaHouseholdUserStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdUser")
        kparams.addIntIfDefined("householdId", self.householdId)
        kparams.addStringIfDefined("userId", self.userId)
        kparams.addBoolIfDefined("isMaster", self.isMaster)
        kparams.addStringIfDefined("householdMasterUsername", self.householdMasterUsername)
        return kparams

    def getHouseholdId(self):
        return self.householdId

    def setHouseholdId(self, newHouseholdId):
        self.householdId = newHouseholdId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getIsMaster(self):
        return self.isMaster

    def setIsMaster(self, newIsMaster):
        self.isMaster = newIsMaster

    def getHouseholdMasterUsername(self):
        return self.householdMasterUsername

    def setHouseholdMasterUsername(self, newHouseholdMasterUsername):
        self.householdMasterUsername = newHouseholdMasterUsername

    def getStatus(self):
        return self.status


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            subscriptionIdIn=NotImplemented,
            mediaFileIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated subscription identifiers or file identifier (only 1) to get the subscriptions by
        # @var string
        self.subscriptionIdIn = subscriptionIdIn

        # Media-file identifier to get the subscriptions by
        # @var int
        self.mediaFileIdEqual = mediaFileIdEqual


    PROPERTY_LOADERS = {
        'subscriptionIdIn': getXmlNodeText, 
        'mediaFileIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionFilter")
        kparams.addStringIfDefined("subscriptionIdIn", self.subscriptionIdIn)
        kparams.addIntIfDefined("mediaFileIdEqual", self.mediaFileIdEqual)
        return kparams

    def getSubscriptionIdIn(self):
        return self.subscriptionIdIn

    def setSubscriptionIdIn(self, newSubscriptionIdIn):
        self.subscriptionIdIn = newSubscriptionIdIn

    def getMediaFileIdEqual(self):
        return self.mediaFileIdEqual

    def setMediaFileIdEqual(self, newMediaFileIdEqual):
        self.mediaFileIdEqual = newMediaFileIdEqual


# @package Kaltura
# @subpackage Client
class KalturaOTTCategory(KalturaObjectBase):
    """Category details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            parentCategoryId=NotImplemented,
            childCategories=NotImplemented,
            channels=NotImplemented,
            images=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier for the category
        # @var int
        # @readonly
        self.id = id

        # Category name
        # @var string
        self.name = name

        # Category parent identifier
        # @var int
        self.parentCategoryId = parentCategoryId

        # Child categories
        # @var array of KalturaOTTCategory
        self.childCategories = childCategories

        # Category channels
        # @var array of KalturaChannel
        self.channels = channels

        # Category images
        # @var array of KalturaMediaImage
        self.images = images


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'parentCategoryId': getXmlNodeInt, 
        'childCategories': (KalturaObjectFactory.createArray, KalturaObjectBase), 
        'channels': (KalturaObjectFactory.createArray, KalturaChannel), 
        'images': (KalturaObjectFactory.createArray, KalturaMediaImage), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTCategory.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaOTTCategory")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("parentCategoryId", self.parentCategoryId)
        kparams.addArrayIfDefined("childCategories", self.childCategories)
        kparams.addArrayIfDefined("channels", self.channels)
        kparams.addArrayIfDefined("images", self.images)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getParentCategoryId(self):
        return self.parentCategoryId

    def setParentCategoryId(self, newParentCategoryId):
        self.parentCategoryId = newParentCategoryId

    def getChildCategories(self):
        return self.childCategories

    def setChildCategories(self, newChildCategories):
        self.childCategories = newChildCategories

    def getChannels(self):
        return self.channels

    def setChannels(self, newChannels):
        self.channels = newChannels

    def getImages(self):
        return self.images

    def setImages(self, newImages):
        self.images = newImages


# @package Kaltura
# @subpackage Client
class KalturaCoupon(KalturaObjectBase):
    """Coupon details container"""

    def __init__(self,
            couponsGroup=NotImplemented,
            status=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Coupons group details
        # @var KalturaCouponsGroup
        # @readonly
        self.couponsGroup = couponsGroup

        # Coupon status
        # @var KalturaCouponStatus
        # @readonly
        self.status = status


    PROPERTY_LOADERS = {
        'couponsGroup': (KalturaObjectFactory.create, KalturaCouponsGroup), 
        'status': (KalturaEnumsFactory.createString, "KalturaCouponStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCoupon.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCoupon")
        return kparams

    def getCouponsGroup(self):
        return self.couponsGroup

    def getStatus(self):
        return self.status


# @package Kaltura
# @subpackage Client
class KalturaEntitlementFilter(KalturaFilter):
    """Entitlements filter"""

    def __init__(self,
            orderBy=NotImplemented,
            entitlementTypeEqual=NotImplemented,
            entityReferenceEqual=NotImplemented,
            isExpiredEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # The type of the entitlements to return
        # @var KalturaTransactionType
        self.entitlementTypeEqual = entitlementTypeEqual

        # Reference type to filter by
        # @var KalturaEntityReferenceBy
        self.entityReferenceEqual = entityReferenceEqual

        # Is expired
        # @var bool
        self.isExpiredEqual = isExpiredEqual


    PROPERTY_LOADERS = {
        'entitlementTypeEqual': (KalturaEnumsFactory.createString, "KalturaTransactionType"), 
        'entityReferenceEqual': (KalturaEnumsFactory.createString, "KalturaEntityReferenceBy"), 
        'isExpiredEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntitlementFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaEntitlementFilter")
        kparams.addStringEnumIfDefined("entitlementTypeEqual", self.entitlementTypeEqual)
        kparams.addStringEnumIfDefined("entityReferenceEqual", self.entityReferenceEqual)
        kparams.addBoolIfDefined("isExpiredEqual", self.isExpiredEqual)
        return kparams

    def getEntitlementTypeEqual(self):
        return self.entitlementTypeEqual

    def setEntitlementTypeEqual(self, newEntitlementTypeEqual):
        self.entitlementTypeEqual = newEntitlementTypeEqual

    def getEntityReferenceEqual(self):
        return self.entityReferenceEqual

    def setEntityReferenceEqual(self, newEntityReferenceEqual):
        self.entityReferenceEqual = newEntityReferenceEqual

    def getIsExpiredEqual(self):
        return self.isExpiredEqual

    def setIsExpiredEqual(self, newIsExpiredEqual):
        self.isExpiredEqual = newIsExpiredEqual


# @package Kaltura
# @subpackage Client
class KalturaFavoriteFilter(KalturaFilter):
    """Favorite request filter"""

    def __init__(self,
            orderBy=NotImplemented,
            mediaTypeIn=NotImplemented,
            mediaIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Media type to filter by the favorite assets
        # @var int
        self.mediaTypeIn = mediaTypeIn

        # Media identifiers from which to filter the favorite assets
        # @var string
        self.mediaIdIn = mediaIdIn


    PROPERTY_LOADERS = {
        'mediaTypeIn': getXmlNodeInt, 
        'mediaIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFavoriteFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaFavoriteFilter")
        kparams.addIntIfDefined("mediaTypeIn", self.mediaTypeIn)
        kparams.addStringIfDefined("mediaIdIn", self.mediaIdIn)
        return kparams

    def getMediaTypeIn(self):
        return self.mediaTypeIn

    def setMediaTypeIn(self, newMediaTypeIn):
        self.mediaTypeIn = newMediaTypeIn

    def getMediaIdIn(self):
        return self.mediaIdIn

    def setMediaIdIn(self, newMediaIdIn):
        self.mediaIdIn = newMediaIdIn


# @package Kaltura
# @subpackage Client
class KalturaSocial(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented,
            email=NotImplemented,
            gender=NotImplemented,
            userId=NotImplemented,
            birthday=NotImplemented,
            status=NotImplemented,
            pictureUrl=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Facebook identifier
        # @var string
        # @readonly
        self.id = id

        # Full name
        # @var string
        self.name = name

        # First name
        # @var string
        self.firstName = firstName

        # Last name
        # @var string
        self.lastName = lastName

        # User email
        # @var string
        self.email = email

        # Gender
        # @var string
        self.gender = gender

        # User identifier
        # @var string
        # @readonly
        self.userId = userId

        # User birthday
        # @var string
        self.birthday = birthday

        # User model status
        #             Possible values: UNKNOWN, OK, ERROR, NOACTION, NOTEXIST, CONFLICT, MERGE, MERGEOK, NEWUSER, MINFRIENDS, INVITEOK, INVITEERROR, ACCESSDENIED, WRONGPASSWORDORUSERNAME, UNMERGEOK
        # @var string
        # @readonly
        self.status = status

        # Profile picture URL
        # @var string
        self.pictureUrl = pictureUrl


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'firstName': getXmlNodeText, 
        'lastName': getXmlNodeText, 
        'email': getXmlNodeText, 
        'gender': getXmlNodeText, 
        'userId': getXmlNodeText, 
        'birthday': getXmlNodeText, 
        'status': getXmlNodeText, 
        'pictureUrl': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocial.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSocial")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("firstName", self.firstName)
        kparams.addStringIfDefined("lastName", self.lastName)
        kparams.addStringIfDefined("email", self.email)
        kparams.addStringIfDefined("gender", self.gender)
        kparams.addStringIfDefined("birthday", self.birthday)
        kparams.addStringIfDefined("pictureUrl", self.pictureUrl)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName

    def getEmail(self):
        return self.email

    def setEmail(self, newEmail):
        self.email = newEmail

    def getGender(self):
        return self.gender

    def setGender(self, newGender):
        self.gender = newGender

    def getUserId(self):
        return self.userId

    def getBirthday(self):
        return self.birthday

    def setBirthday(self, newBirthday):
        self.birthday = newBirthday

    def getStatus(self):
        return self.status

    def getPictureUrl(self):
        return self.pictureUrl

    def setPictureUrl(self, newPictureUrl):
        self.pictureUrl = newPictureUrl


# @package Kaltura
# @subpackage Client
class KalturaFacebookSocial(KalturaSocial):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented,
            email=NotImplemented,
            gender=NotImplemented,
            userId=NotImplemented,
            birthday=NotImplemented,
            status=NotImplemented,
            pictureUrl=NotImplemented):
        KalturaSocial.__init__(self,
            id,
            name,
            firstName,
            lastName,
            email,
            gender,
            userId,
            birthday,
            status,
            pictureUrl)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSocial.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFacebookSocial.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSocial.toParams(self)
        kparams.put("objectType", "KalturaFacebookSocial")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaLoginResponse(KalturaObjectBase):
    def __init__(self,
            user=NotImplemented,
            loginSession=NotImplemented):
        KalturaObjectBase.__init__(self)

        # User
        # @var KalturaOTTUser
        self.user = user

        # Kaltura login session details
        # @var KalturaLoginSession
        self.loginSession = loginSession


    PROPERTY_LOADERS = {
        'user': (KalturaObjectFactory.create, KalturaOTTUser), 
        'loginSession': (KalturaObjectFactory.create, KalturaLoginSession), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLoginResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLoginResponse")
        kparams.addObjectIfDefined("user", self.user)
        kparams.addObjectIfDefined("loginSession", self.loginSession)
        return kparams

    def getUser(self):
        return self.user

    def setUser(self, newUser):
        self.user = newUser

    def getLoginSession(self):
        return self.loginSession

    def setLoginSession(self, newLoginSession):
        self.loginSession = newLoginSession


# @package Kaltura
# @subpackage Client
class KalturaSocialConfig(KalturaObjectBase):
    """Returns social configuration for the partner"""

    def __init__(self,
            appId=NotImplemented,
            permissions=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The application identifier
        # @var string
        self.appId = appId

        # List of application permissions
        # @var string
        self.permissions = permissions


    PROPERTY_LOADERS = {
        'appId': getXmlNodeText, 
        'permissions': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSocialConfig")
        kparams.addStringIfDefined("appId", self.appId)
        kparams.addStringIfDefined("permissions", self.permissions)
        return kparams

    def getAppId(self):
        return self.appId

    def setAppId(self, newAppId):
        self.appId = newAppId

    def getPermissions(self):
        return self.permissions

    def setPermissions(self, newPermissions):
        self.permissions = newPermissions


# @package Kaltura
# @subpackage Client
class KalturaPurchaseBase(KalturaObjectBase):
    def __init__(self,
            productId=NotImplemented,
            contentId=NotImplemented,
            productType=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Identifier for the package from which this content is offered
        # @var int
        self.productId = productId

        # Identifier for the content to purchase. Relevant only if Product type = PPV
        # @var int
        self.contentId = contentId

        # Package type. Possible values: PPV, Subscription, Collection
        # @var KalturaTransactionType
        self.productType = productType


    PROPERTY_LOADERS = {
        'productId': getXmlNodeInt, 
        'contentId': getXmlNodeInt, 
        'productType': (KalturaEnumsFactory.createString, "KalturaTransactionType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPurchaseBase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPurchaseBase")
        kparams.addIntIfDefined("productId", self.productId)
        kparams.addIntIfDefined("contentId", self.contentId)
        kparams.addStringEnumIfDefined("productType", self.productType)
        return kparams

    def getProductId(self):
        return self.productId

    def setProductId(self, newProductId):
        self.productId = newProductId

    def getContentId(self):
        return self.contentId

    def setContentId(self, newContentId):
        self.contentId = newContentId

    def getProductType(self):
        return self.productType

    def setProductType(self, newProductType):
        self.productType = newProductType


# @package Kaltura
# @subpackage Client
class KalturaPurchase(KalturaPurchaseBase):
    def __init__(self,
            productId=NotImplemented,
            contentId=NotImplemented,
            productType=NotImplemented,
            currency=NotImplemented,
            price=NotImplemented,
            paymentMethodId=NotImplemented,
            paymentGatewayId=NotImplemented,
            coupon=NotImplemented):
        KalturaPurchaseBase.__init__(self,
            productId,
            contentId,
            productType)

        # Identifier for paying currency, according to ISO 4217
        # @var string
        self.currency = currency

        # Net sum to charge – as a one-time transaction. Price must match the previously provided price for the specified content.
        # @var float
        self.price = price

        # Identifier for a pre-entered payment method. If not provided – the household’s default payment method is used
        # @var int
        self.paymentMethodId = paymentMethodId

        # Identifier for a pre-associated payment gateway. If not provided – the account’s default payment gateway is used
        # @var int
        self.paymentGatewayId = paymentGatewayId

        # Coupon code
        # @var string
        self.coupon = coupon


    PROPERTY_LOADERS = {
        'currency': getXmlNodeText, 
        'price': getXmlNodeFloat, 
        'paymentMethodId': getXmlNodeInt, 
        'paymentGatewayId': getXmlNodeInt, 
        'coupon': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPurchaseBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPurchase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPurchaseBase.toParams(self)
        kparams.put("objectType", "KalturaPurchase")
        kparams.addStringIfDefined("currency", self.currency)
        kparams.addFloatIfDefined("price", self.price)
        kparams.addIntIfDefined("paymentMethodId", self.paymentMethodId)
        kparams.addIntIfDefined("paymentGatewayId", self.paymentGatewayId)
        kparams.addStringIfDefined("coupon", self.coupon)
        return kparams

    def getCurrency(self):
        return self.currency

    def setCurrency(self, newCurrency):
        self.currency = newCurrency

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getPaymentMethodId(self):
        return self.paymentMethodId

    def setPaymentMethodId(self, newPaymentMethodId):
        self.paymentMethodId = newPaymentMethodId

    def getPaymentGatewayId(self):
        return self.paymentGatewayId

    def setPaymentGatewayId(self, newPaymentGatewayId):
        self.paymentGatewayId = newPaymentGatewayId

    def getCoupon(self):
        return self.coupon

    def setCoupon(self, newCoupon):
        self.coupon = newCoupon


# @package Kaltura
# @subpackage Client
class KalturaPurchaseSession(KalturaPurchase):
    def __init__(self,
            productId=NotImplemented,
            contentId=NotImplemented,
            productType=NotImplemented,
            currency=NotImplemented,
            price=NotImplemented,
            paymentMethodId=NotImplemented,
            paymentGatewayId=NotImplemented,
            coupon=NotImplemented,
            previewModuleId=NotImplemented):
        KalturaPurchase.__init__(self,
            productId,
            contentId,
            productType,
            currency,
            price,
            paymentMethodId,
            paymentGatewayId,
            coupon)

        # Preview module identifier (relevant only for subscription)
        # @var int
        self.previewModuleId = previewModuleId


    PROPERTY_LOADERS = {
        'previewModuleId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaPurchase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPurchaseSession.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPurchase.toParams(self)
        kparams.put("objectType", "KalturaPurchaseSession")
        kparams.addIntIfDefined("previewModuleId", self.previewModuleId)
        return kparams

    def getPreviewModuleId(self):
        return self.previewModuleId

    def setPreviewModuleId(self, newPreviewModuleId):
        self.previewModuleId = newPreviewModuleId


# @package Kaltura
# @subpackage Client
class KalturaExternalReceipt(KalturaPurchaseBase):
    def __init__(self,
            productId=NotImplemented,
            contentId=NotImplemented,
            productType=NotImplemented,
            receiptId=NotImplemented,
            paymentGatewayName=NotImplemented):
        KalturaPurchaseBase.__init__(self,
            productId,
            contentId,
            productType)

        # A unique identifier that was provided by the In-App billing service to validate the purchase
        # @var string
        self.receiptId = receiptId

        # The payment gateway name for the In-App billing service to be used. Possible values: Google/Apple
        # @var string
        self.paymentGatewayName = paymentGatewayName


    PROPERTY_LOADERS = {
        'receiptId': getXmlNodeText, 
        'paymentGatewayName': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPurchaseBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExternalReceipt.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPurchaseBase.toParams(self)
        kparams.put("objectType", "KalturaExternalReceipt")
        kparams.addStringIfDefined("receiptId", self.receiptId)
        kparams.addStringIfDefined("paymentGatewayName", self.paymentGatewayName)
        return kparams

    def getReceiptId(self):
        return self.receiptId

    def setReceiptId(self, newReceiptId):
        self.receiptId = newReceiptId

    def getPaymentGatewayName(self):
        return self.paymentGatewayName

    def setPaymentGatewayName(self, newPaymentGatewayName):
        self.paymentGatewayName = newPaymentGatewayName


# @package Kaltura
# @subpackage Client
class KalturaTransaction(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            paymentGatewayReferenceId=NotImplemented,
            paymentGatewayResponseId=NotImplemented,
            state=NotImplemented,
            failReasonCode=NotImplemented,
            createdAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Kaltura unique ID representing the transaction
        # @var string
        self.id = id

        # Transaction reference ID received from the payment gateway. 
        #             Value is available only if the payment gateway provides this information.
        # @var string
        self.paymentGatewayReferenceId = paymentGatewayReferenceId

        # Response ID received from by the payment gateway. 
        #             Value is available only if the payment gateway provides this information.
        # @var string
        self.paymentGatewayResponseId = paymentGatewayResponseId

        # Transaction state: OK/Pending/Failed
        # @var string
        self.state = state

        # Adapter failure reason code
        #             Insufficient funds = 20, Invalid account = 21, User unknown = 22, Reason unknown = 23, Unknown payment gateway response = 24,
        #             No response from payment gateway = 25, Exceeded retry limit = 26, Illegal client request = 27, Expired = 28
        # @var int
        self.failReasonCode = failReasonCode

        # Entitlement creation date
        # @var int
        self.createdAt = createdAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'paymentGatewayReferenceId': getXmlNodeText, 
        'paymentGatewayResponseId': getXmlNodeText, 
        'state': getXmlNodeText, 
        'failReasonCode': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTransaction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTransaction")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("paymentGatewayReferenceId", self.paymentGatewayReferenceId)
        kparams.addStringIfDefined("paymentGatewayResponseId", self.paymentGatewayResponseId)
        kparams.addStringIfDefined("state", self.state)
        kparams.addIntIfDefined("failReasonCode", self.failReasonCode)
        kparams.addIntIfDefined("createdAt", self.createdAt)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getPaymentGatewayReferenceId(self):
        return self.paymentGatewayReferenceId

    def setPaymentGatewayReferenceId(self, newPaymentGatewayReferenceId):
        self.paymentGatewayReferenceId = newPaymentGatewayReferenceId

    def getPaymentGatewayResponseId(self):
        return self.paymentGatewayResponseId

    def setPaymentGatewayResponseId(self, newPaymentGatewayResponseId):
        self.paymentGatewayResponseId = newPaymentGatewayResponseId

    def getState(self):
        return self.state

    def setState(self, newState):
        self.state = newState

    def getFailReasonCode(self):
        return self.failReasonCode

    def setFailReasonCode(self, newFailReasonCode):
        self.failReasonCode = newFailReasonCode

    def getCreatedAt(self):
        return self.createdAt

    def setCreatedAt(self, newCreatedAt):
        self.createdAt = newCreatedAt


# @package Kaltura
# @subpackage Client
class KalturaTransactionStatus(KalturaObjectBase):
    def __init__(self,
            adapterTransactionStatus=NotImplemented,
            externalId=NotImplemented,
            externalStatus=NotImplemented,
            externalMessage=NotImplemented,
            failReason=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Payment gateway adapter application state for the transaction to update
        # @var KalturaTransactionAdapterStatus
        self.adapterTransactionStatus = adapterTransactionStatus

        # External transaction identifier
        # @var string
        self.externalId = externalId

        # Payment gateway transaction status
        # @var string
        self.externalStatus = externalStatus

        # Payment gateway message
        # @var string
        self.externalMessage = externalMessage

        # The reason the transaction failed
        # @var int
        self.failReason = failReason


    PROPERTY_LOADERS = {
        'adapterTransactionStatus': (KalturaEnumsFactory.createString, "KalturaTransactionAdapterStatus"), 
        'externalId': getXmlNodeText, 
        'externalStatus': getXmlNodeText, 
        'externalMessage': getXmlNodeText, 
        'failReason': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTransactionStatus.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTransactionStatus")
        kparams.addStringEnumIfDefined("adapterTransactionStatus", self.adapterTransactionStatus)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addStringIfDefined("externalStatus", self.externalStatus)
        kparams.addStringIfDefined("externalMessage", self.externalMessage)
        kparams.addIntIfDefined("failReason", self.failReason)
        return kparams

    def getAdapterTransactionStatus(self):
        return self.adapterTransactionStatus

    def setAdapterTransactionStatus(self, newAdapterTransactionStatus):
        self.adapterTransactionStatus = newAdapterTransactionStatus

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getExternalStatus(self):
        return self.externalStatus

    def setExternalStatus(self, newExternalStatus):
        self.externalStatus = newExternalStatus

    def getExternalMessage(self):
        return self.externalMessage

    def setExternalMessage(self, newExternalMessage):
        self.externalMessage = newExternalMessage

    def getFailReason(self):
        return self.failReason

    def setFailReason(self, newFailReason):
        self.failReason = newFailReason


# @package Kaltura
# @subpackage Client
class KalturaUserLoginPin(KalturaObjectBase):
    """Log in pin code details"""

    def __init__(self,
            pinCode=NotImplemented,
            expirationTime=NotImplemented,
            userId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Generated login pin code
        # @var string
        self.pinCode = pinCode

        # Login pin expiration time (epoch)
        # @var int
        self.expirationTime = expirationTime

        # User Identifier
        # @var string
        # @readonly
        self.userId = userId


    PROPERTY_LOADERS = {
        'pinCode': getXmlNodeText, 
        'expirationTime': getXmlNodeInt, 
        'userId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserLoginPin.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserLoginPin")
        kparams.addStringIfDefined("pinCode", self.pinCode)
        kparams.addIntIfDefined("expirationTime", self.expirationTime)
        return kparams

    def getPinCode(self):
        return self.pinCode

    def setPinCode(self, newPinCode):
        self.pinCode = newPinCode

    def getExpirationTime(self):
        return self.expirationTime

    def setExpirationTime(self, newExpirationTime):
        self.expirationTime = newExpirationTime

    def getUserId(self):
        return self.userId


# @package Kaltura
# @subpackage Client
class KalturaParentalRuleFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            entityReferenceEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Reference type to filter by
        # @var KalturaEntityReferenceBy
        self.entityReferenceEqual = entityReferenceEqual


    PROPERTY_LOADERS = {
        'entityReferenceEqual': (KalturaEnumsFactory.createString, "KalturaEntityReferenceBy"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaParentalRuleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaParentalRuleFilter")
        kparams.addStringEnumIfDefined("entityReferenceEqual", self.entityReferenceEqual)
        return kparams

    def getEntityReferenceEqual(self):
        return self.entityReferenceEqual

    def setEntityReferenceEqual(self, newEntityReferenceEqual):
        self.entityReferenceEqual = newEntityReferenceEqual


# @package Kaltura
# @subpackage Client
class KalturaTransactionHistoryFilter(KalturaFilter):
    """Transactions filter"""

    def __init__(self,
            orderBy=NotImplemented,
            entityReferenceEqual=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Reference type to filter by
        # @var KalturaEntityReferenceBy
        self.entityReferenceEqual = entityReferenceEqual

        # Filter transactions later than specific date
        # @var int
        self.startDateGreaterThanOrEqual = startDateGreaterThanOrEqual

        # Filter transactions earlier than specific date
        # @var int
        self.endDateLessThanOrEqual = endDateLessThanOrEqual


    PROPERTY_LOADERS = {
        'entityReferenceEqual': (KalturaEnumsFactory.createString, "KalturaEntityReferenceBy"), 
        'startDateGreaterThanOrEqual': getXmlNodeInt, 
        'endDateLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTransactionHistoryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaTransactionHistoryFilter")
        kparams.addStringEnumIfDefined("entityReferenceEqual", self.entityReferenceEqual)
        kparams.addIntIfDefined("startDateGreaterThanOrEqual", self.startDateGreaterThanOrEqual)
        kparams.addIntIfDefined("endDateLessThanOrEqual", self.endDateLessThanOrEqual)
        return kparams

    def getEntityReferenceEqual(self):
        return self.entityReferenceEqual

    def setEntityReferenceEqual(self, newEntityReferenceEqual):
        self.entityReferenceEqual = newEntityReferenceEqual

    def getStartDateGreaterThanOrEqual(self):
        return self.startDateGreaterThanOrEqual

    def setStartDateGreaterThanOrEqual(self, newStartDateGreaterThanOrEqual):
        self.startDateGreaterThanOrEqual = newStartDateGreaterThanOrEqual

    def getEndDateLessThanOrEqual(self):
        return self.endDateLessThanOrEqual

    def setEndDateLessThanOrEqual(self, newEndDateLessThanOrEqual):
        self.endDateLessThanOrEqual = newEndDateLessThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaUserRoleFilter(KalturaFilter):
    """User roles filter"""

    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated roles identifiers
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserRoleFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaOTTUserFilter(KalturaFilter):
    """OTT User filter"""

    def __init__(self,
            orderBy=NotImplemented,
            userByEqual=NotImplemented,
            valueEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # User Filter By
        # @var KalturaOTTUserBy
        self.userByEqual = userByEqual

        # The User identifiers
        # @var string
        self.valueEqual = valueEqual


    PROPERTY_LOADERS = {
        'userByEqual': (KalturaEnumsFactory.createString, "KalturaOTTUserBy"), 
        'valueEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTUserFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaOTTUserFilter")
        kparams.addStringEnumIfDefined("userByEqual", self.userByEqual)
        kparams.addStringIfDefined("valueEqual", self.valueEqual)
        return kparams

    def getUserByEqual(self):
        return self.userByEqual

    def setUserByEqual(self, newUserByEqual):
        self.userByEqual = newUserByEqual

    def getValueEqual(self):
        return self.valueEqual

    def setValueEqual(self, newValueEqual):
        self.valueEqual = newValueEqual


########## services ##########

# @package Kaltura
# @subpackage Client
class KalturaAnnouncementService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, announcement):
        """Add a new future scheduled system announcement push notification"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("announcement", announcement)
        self.client.queueServiceActionCall("announcement", "add", KalturaAnnouncement, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAnnouncement)

    def delete(self, id):
        """Delete an existing announcing. Announcement cannot be delete while being sent."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("announcement", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def enableSystemAnnouncements(self):
        """Enable system announcements"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("announcement", "enableSystemAnnouncements", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self, filter, pager = NotImplemented):
        """Lists all announcements in the system."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("announcement", "list", KalturaAnnouncementListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAnnouncementListResponse)

    def update(self, announcementId, announcement):
        """Update an existing future system announcement push notification. Announcement can only be updated only before sending"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("announcementId", announcementId);
        kparams.addObjectIfDefined("announcement", announcement)
        self.client.queueServiceActionCall("announcement", "update", KalturaAnnouncement, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAnnouncement)

    def updateStatus(self, id, status):
        """Update a system announcement status"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addBoolIfDefined("status", status);
        self.client.queueServiceActionCall("announcement", "updateStatus", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaAppTokenService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, appToken):
        """Add new application authentication token"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("appToken", appToken)
        self.client.queueServiceActionCall("apptoken", "add", KalturaAppToken, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAppToken)

    def delete(self, id):
        """Delete application authentication token by id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("apptoken", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def get(self, id):
        """Get application authentication token by id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("apptoken", "get", KalturaAppToken, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAppToken)

    def startSession(self, id, tokenHash, userId = NotImplemented, type = NotImplemented, expiry = NotImplemented, udid = NotImplemented):
        """Starts a new KS (Kaltura Session) based on application authentication token id"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addStringIfDefined("tokenHash", tokenHash)
        kparams.addStringIfDefined("userId", userId)
        kparams.addIntIfDefined("type", type);
        kparams.addIntIfDefined("expiry", expiry);
        kparams.addStringIfDefined("udid", udid)
        self.client.queueServiceActionCall("apptoken", "startSession", KalturaSessionInfo, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSessionInfo)


# @package Kaltura
# @subpackage Client
class KalturaAssetCommentService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, comment):
        """Add asset comments by asset id"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("comment", comment)
        self.client.queueServiceActionCall("assetcomment", "add", KalturaAssetComment, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAssetComment)

    def list(self, filter, pager = NotImplemented):
        """Returns asset comments by asset id"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("assetcomment", "list", KalturaAssetCommentListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAssetCommentListResponse)


# @package Kaltura
# @subpackage Client
class KalturaAssetService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, id, assetReferenceType):
        """Returns media or EPG asset by media / EPG internal or external identifier"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addStringIfDefined("assetReferenceType", assetReferenceType)
        self.client.queueServiceActionCall("asset", "get", KalturaAsset, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAsset)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Returns media or EPG assets. Filters by media identifiers or by EPG internal or external identifier."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("asset", "list", KalturaAssetListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAssetListResponse)


# @package Kaltura
# @subpackage Client
class KalturaAssetFileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getContext(self, id):
        """get KalturaAssetFileContext"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("assetfile", "getContext", KalturaAssetFileContext, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAssetFileContext)


# @package Kaltura
# @subpackage Client
class KalturaAssetHistoryService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Get recently watched media for user, ordered by recently watched first."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("assethistory", "list", KalturaAssetHistoryListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAssetHistoryListResponse)


# @package Kaltura
# @subpackage Client
class KalturaAssetStatisticsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def query(self, query):
        """Returns statistics for given list of assets by type and / or time period"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("query", query)
        self.client.queueServiceActionCall("assetstatistics", "query", KalturaAssetStatisticsListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaAssetStatisticsListResponse)


# @package Kaltura
# @subpackage Client
class KalturaBookmarkService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, bookmark):
        """Report player position and action for the user on the watched asset. Player position is used to later allow resume watching."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("bookmark", bookmark)
        self.client.queueServiceActionCall("bookmark", "add", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self, filter):
        """Returns player position record/s for the requested asset and the requesting user. 
                    If default user makes the request – player position records are provided for all of the users in the household.
                    If non-default user makes the request - player position records are provided for the requesting user and the default user of the household."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("bookmark", "list", KalturaBookmarkListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBookmarkListResponse)


# @package Kaltura
# @subpackage Client
class KalturaCdnAdapterProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, adapter):
        """Insert new CDN adapter for partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("adapter", adapter)
        self.client.queueServiceActionCall("cdnadapterprofile", "add", KalturaCDNAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDNAdapterProfile)

    def delete(self, adapterId):
        """Delete CDN adapter by CDN adapter id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("adapterId", adapterId);
        self.client.queueServiceActionCall("cdnadapterprofile", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def generateSharedSecret(self, adapterId):
        """Generate CDN adapter shared secret"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("adapterId", adapterId);
        self.client.queueServiceActionCall("cdnadapterprofile", "generateSharedSecret", KalturaCDNAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDNAdapterProfile)

    def list(self):
        """Returns all CDN adapters for partner"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("cdnadapterprofile", "list", KalturaCDNAdapterProfileListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDNAdapterProfileListResponse)

    def update(self, adapterId, adapter):
        """Update CDN adapter details"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("adapterId", adapterId);
        kparams.addObjectIfDefined("adapter", adapter)
        self.client.queueServiceActionCall("cdnadapterprofile", "update", KalturaCDNAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDNAdapterProfile)


# @package Kaltura
# @subpackage Client
class KalturaCdnPartnerSettingsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self):
        """Retrieve the partner’s CDN settings (default adapters)"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("cdnpartnersettings", "get", KalturaCDNPartnerSettings, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDNPartnerSettings)

    def update(self, settings):
        """Configure the partner’s CDN settings (default adapters)"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("settings", settings)
        self.client.queueServiceActionCall("cdnpartnersettings", "update", KalturaCDNPartnerSettings, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDNPartnerSettings)


# @package Kaltura
# @subpackage Client
class KalturaCDVRAdapterProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, adapter):
        """Insert new C-DVR adapter for partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("adapter", adapter)
        self.client.queueServiceActionCall("cdvradapterprofile", "add", KalturaCDVRAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDVRAdapterProfile)

    def delete(self, adapterId):
        """Delete C-DVR adapter by C-DVR adapter id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("adapterId", adapterId);
        self.client.queueServiceActionCall("cdvradapterprofile", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def generateSharedSecret(self, adapterId):
        """Generate C-DVR adapter shared secret"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("adapterId", adapterId);
        self.client.queueServiceActionCall("cdvradapterprofile", "generateSharedSecret", KalturaCDVRAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDVRAdapterProfile)

    def list(self):
        """Returns all C-DVR adapters for partner"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("cdvradapterprofile", "list", KalturaCDVRAdapterProfileListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDVRAdapterProfileListResponse)

    def update(self, adapterId, adapter):
        """Update C-DVR adapter details"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("adapterId", adapterId);
        kparams.addObjectIfDefined("adapter", adapter)
        self.client.queueServiceActionCall("cdvradapterprofile", "update", KalturaCDVRAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCDVRAdapterProfile)


# @package Kaltura
# @subpackage Client
class KalturaChannelService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, channel):
        """Insert new channel for partner. Currently supports only KSQL channel"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("channel", channel)
        self.client.queueServiceActionCall("channel", "add", KalturaChannel, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaChannel)

    def delete(self, channelId):
        """Delete channel by its channel id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("channelId", channelId);
        self.client.queueServiceActionCall("channel", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def get(self, id):
        """Returns channel info"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("channel", "get", KalturaChannel, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaChannel)

    def update(self, channelId, channel):
        """Update channel details. Currently supports only KSQL channel"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("channelId", channelId);
        kparams.addObjectIfDefined("channel", channel)
        self.client.queueServiceActionCall("channel", "update", KalturaChannel, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaChannel)


# @package Kaltura
# @subpackage Client
class KalturaCouponService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, code):
        """Returns information about a coupon"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("code", code)
        self.client.queueServiceActionCall("coupon", "get", KalturaCoupon, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCoupon)


# @package Kaltura
# @subpackage Client
class KalturaEntitlementService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def cancel(self, assetId, transactionType):
        """Immediately cancel a subscription, PPV or collection. Cancel is possible only if within cancellation window and content not already consumed"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("assetId", assetId);
        kparams.addStringIfDefined("transactionType", transactionType)
        self.client.queueServiceActionCall("entitlement", "cancel", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def cancelRenewal(self, subscriptionId):
        """Cancel a household service subscription at the next renewal. The subscription stays valid till the next renewal."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("subscriptionId", subscriptionId)
        self.client.queueServiceActionCall("entitlement", "cancelRenewal", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def externalReconcile(self):
        """Reconcile the user household&#39;s entitlements with an external entitlements source. This request is frequency protected to avoid too frequent calls per household."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("entitlement", "externalReconcile", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def forceCancel(self, assetId, transactionType):
        """Immediately cancel a subscription, PPV or collection. Cancel applies regardless of cancellation window and content consumption status"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("assetId", assetId);
        kparams.addStringIfDefined("transactionType", transactionType)
        self.client.queueServiceActionCall("entitlement", "forceCancel", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def grant(self, productId, productType, history, contentId = 0):
        """Grant household for an entitlement for a PPV or Subscription."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("productId", productId);
        kparams.addStringIfDefined("productType", productType)
        kparams.addBoolIfDefined("history", history);
        kparams.addIntIfDefined("contentId", contentId);
        self.client.queueServiceActionCall("entitlement", "grant", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self, filter, pager = NotImplemented):
        """Gets all the entitled media items for a household"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("entitlement", "list", KalturaEntitlementListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaEntitlementListResponse)


# @package Kaltura
# @subpackage Client
class KalturaExportTaskService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, task):
        """Adds a new bulk export task"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("task", task)
        self.client.queueServiceActionCall("exporttask", "add", KalturaExportTask, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaExportTask)

    def delete(self, id):
        """Deletes an existing bulk export task by task identifier"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("exporttask", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def get(self, id):
        """Gets an existing bulk export task by task identifier"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("exporttask", "get", KalturaExportTask, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaExportTask)

    def list(self, filter = NotImplemented):
        """Returns bulk export tasks by tasks identifiers"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("exporttask", "list", KalturaExportTaskListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaExportTaskListResponse)

    def update(self, id, task):
        """Updates an existing bulk export task by task identifier"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("task", task)
        self.client.queueServiceActionCall("exporttask", "update", KalturaExportTask, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaExportTask)


# @package Kaltura
# @subpackage Client
class KalturaExternalChannelProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, externalChannel):
        """Insert new External channel for partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("externalChannel", externalChannel)
        self.client.queueServiceActionCall("externalchannelprofile", "add", KalturaExternalChannelProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaExternalChannelProfile)

    def delete(self, externalChannelId):
        """Delete External channel by External channel id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("externalChannelId", externalChannelId);
        self.client.queueServiceActionCall("externalchannelprofile", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self):
        """Returns all External channels for partner"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("externalchannelprofile", "list", KalturaExternalChannelProfileListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaExternalChannelProfileListResponse)

    def update(self, externalChannelId, externalChannel):
        """Update External channel details"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("externalChannelId", externalChannelId);
        kparams.addObjectIfDefined("externalChannel", externalChannel)
        self.client.queueServiceActionCall("externalchannelprofile", "update", KalturaExternalChannelProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaExternalChannelProfile)


# @package Kaltura
# @subpackage Client
class KalturaFavoriteService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, favorite):
        """Add media to user&#39;s favorite list"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("favorite", favorite)
        self.client.queueServiceActionCall("favorite", "add", KalturaFavorite, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFavorite)

    def delete(self, id):
        """Remove media from user&#39;s favorite list"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("favorite", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self, filter = NotImplemented):
        """Retrieving users&#39; favorites"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("favorite", "list", KalturaFavoriteListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFavoriteListResponse)


# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeriesService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, followTvSeries):
        """Add a user&#39;s tv series follow.
                    Possible status codes: UserAlreadyFollowing = 8013, NotFound = 500007, InvalidAssetId = 4024"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("followTvSeries", followTvSeries)
        self.client.queueServiceActionCall("followtvseries", "add", KalturaFollowTvSeries, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFollowTvSeries)

    def delete(self, assetId):
        """Delete a user&#39;s tv series follow.
                    Possible status codes: UserNotFollowing = 8012, NotFound = 500007, InvalidAssetId = 4024, AnnouncementNotFound = 8006"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("assetId", assetId);
        self.client.queueServiceActionCall("followtvseries", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self, filter, pager = NotImplemented):
        """List user&#39;s tv series follows.
                    Possible status codes:"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("followtvseries", "list", KalturaFollowTvSeriesListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaFollowTvSeriesListResponse)


# @package Kaltura
# @subpackage Client
class KalturaHomeNetworkService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, homeNetwork):
        """Add a new home network to a household"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("homeNetwork", homeNetwork)
        self.client.queueServiceActionCall("homenetwork", "add", KalturaHomeNetwork, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHomeNetwork)

    def delete(self, externalId):
        """Delete household’s existing home network"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("externalId", externalId)
        self.client.queueServiceActionCall("homenetwork", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self):
        """Retrieve the household’s home networks"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("homenetwork", "list", KalturaHomeNetworkListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHomeNetworkListResponse)

    def update(self, externalId, homeNetwork):
        """Update and existing home network for a household"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("externalId", externalId)
        kparams.addObjectIfDefined("homeNetwork", homeNetwork)
        self.client.queueServiceActionCall("homenetwork", "update", KalturaHomeNetwork, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHomeNetwork)


# @package Kaltura
# @subpackage Client
class KalturaHouseholdService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, household):
        """Creates a household for the user"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("household", household)
        self.client.queueServiceActionCall("household", "add", KalturaHousehold, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHousehold)

    def delete(self, id):
        """Fully delete a household. Delete all of the household information, including users, devices, transactions and assets."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("household", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def get(self, id = NotImplemented):
        """Returns the household model"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("household", "get", KalturaHousehold, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHousehold)

    def resetFrequency(self, frequencyType):
        """Reset a household’s time limitation for removing user or device"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("frequencyType", frequencyType)
        self.client.queueServiceActionCall("household", "resetFrequency", KalturaHousehold, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHousehold)

    def resume(self):
        """Resumed a given household service to its previous service settings"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("household", "resume", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def suspend(self):
        """Suspend a given household service. Sets the household status to “suspended&quot;.The household service settings are maintained for later resume"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("household", "suspend", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def update(self, household):
        """Update the household name and description"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("household", household)
        self.client.queueServiceActionCall("household", "update", KalturaHousehold, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHousehold)


# @package Kaltura
# @subpackage Client
class KalturaHouseholdDeviceService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, device):
        """Registers a device to a household using pin code"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("device", device)
        self.client.queueServiceActionCall("householddevice", "add", KalturaHouseholdDevice, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdDevice)

    def addByPin(self, deviceName, pin):
        """Registers a device to a household using pin code"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("deviceName", deviceName)
        kparams.addStringIfDefined("pin", pin)
        self.client.queueServiceActionCall("householddevice", "addByPin", KalturaHouseholdDevice, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdDevice)

    def delete(self, udid):
        """Removes a device from household"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("udid", udid)
        self.client.queueServiceActionCall("householddevice", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def generatePin(self, udid, brandId):
        """Generates device pin to use when adding a device to household by pin"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("udid", udid)
        kparams.addIntIfDefined("brandId", brandId);
        self.client.queueServiceActionCall("householddevice", "generatePin", KalturaDevicePin, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaDevicePin)

    def get(self):
        """Returns device registration status to the supplied household"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("householddevice", "get", KalturaHouseholdDevice, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdDevice)

    def update(self, udid, device):
        """Update the name of the device by UDID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("udid", udid)
        kparams.addObjectIfDefined("device", device)
        self.client.queueServiceActionCall("householddevice", "update", KalturaHouseholdDevice, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdDevice)

    def updateStatus(self, udid, status):
        """Update the name of the device by UDID"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("udid", udid)
        kparams.addStringIfDefined("status", status)
        self.client.queueServiceActionCall("householddevice", "updateStatus", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaHouseholdLimitationsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, id):
        """Get the limitation module by id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("householdlimitations", "get", KalturaHouseholdLimitations, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdLimitations)


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentGatewayService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def delete(self, paymentGatewayId):
        """Disable payment-gateway on the household"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        self.client.queueServiceActionCall("householdpaymentgateway", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def set(self, paymentGatewayId):
        """Enable a payment-gateway provider for the household."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        self.client.queueServiceActionCall("householdpaymentgateway", "set", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def getChargeID(self, paymentGatewayExternalId):
        """Get a household’s billing account identifier (charge ID) for a given payment gateway"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("paymentGatewayExternalId", paymentGatewayExternalId)
        self.client.queueServiceActionCall("householdpaymentgateway", "getChargeID", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def invoke(self, paymentGatewayId, intent, extraParameters):
        """Gets the Payment Gateway Configuration for the payment gateway identifier given"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        kparams.addStringIfDefined("intent", intent)
        kparams.addArrayIfDefined("extraParameters", extraParameters)
        self.client.queueServiceActionCall("householdpaymentgateway", "invoke", KalturaPaymentGatewayConfiguration, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentGatewayConfiguration)

    def list(self):
        """Get a list of all configured Payment Gateways providers available for the account. For each payment is provided with the household associated payment methods."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("householdpaymentgateway", "list", KalturaHouseholdPaymentGatewayListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdPaymentGatewayListResponse)

    def setChargeID(self, paymentGatewayExternalId, chargeId):
        """Set user billing account identifier (charge ID), for a specific household and a specific payment gateway"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("paymentGatewayExternalId", paymentGatewayExternalId)
        kparams.addStringIfDefined("chargeId", chargeId)
        self.client.queueServiceActionCall("householdpaymentgateway", "setChargeID", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentMethodService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def forceRemove(self, paymentGatewayId, paymentMethodId):
        """Force remove of a payment method of the household."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        kparams.addIntIfDefined("paymentMethodId", paymentMethodId);
        self.client.queueServiceActionCall("householdpaymentmethod", "forceRemove", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self):
        """Get a list of all configured Payment Gateways providers available for the account. For each payment is provided with the household associated payment methods."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("householdpaymentmethod", "list", KalturaHouseholdPaymentMethodListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdPaymentMethodListResponse)

    def remove(self, paymentGatewayId, paymentMethodId):
        """Removes a payment method of the household."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        kparams.addIntIfDefined("paymentMethodId", paymentMethodId);
        self.client.queueServiceActionCall("householdpaymentmethod", "remove", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def setAsDefault(self, paymentGatewayId, paymentMethodId):
        """Set a payment method as default for the household."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        kparams.addIntIfDefined("paymentMethodId", paymentMethodId);
        self.client.queueServiceActionCall("householdpaymentmethod", "setAsDefault", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPremiumServiceService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self):
        """Returns all the premium services allowed for the household"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("householdpremiumservice", "list", KalturaHouseholdPremiumServiceListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdPremiumServiceListResponse)


# @package Kaltura
# @subpackage Client
class KalturaHouseholdQuotaService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self):
        """Returns the household&#39;s quota data"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("householdquota", "get", KalturaHouseholdQuota, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdQuota)


# @package Kaltura
# @subpackage Client
class KalturaHouseholdUserService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, householdUser):
        """Adds a user to household"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("householdUser", householdUser)
        self.client.queueServiceActionCall("householduser", "add", KalturaHouseholdUser, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaHouseholdUser)

    def delete(self, userId):
        """Removes a user from household"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userId", userId)
        self.client.queueServiceActionCall("householduser", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaInboxMessageService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, id):
        """TBD"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        self.client.queueServiceActionCall("inboxmessage", "get", KalturaInboxMessage, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaInboxMessage)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List inbox messages"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("inboxmessage", "list", KalturaInboxMessageListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaInboxMessageListResponse)

    def updateStatus(self, id, status):
        """TBD"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("id", id)
        kparams.addStringIfDefined("status", status)
        self.client.queueServiceActionCall("inboxmessage", "updateStatus", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaLicensedUrlService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, request):
        """Get the URL for playing an asset - EPG or media (not available for recording for now)."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("request", request)
        self.client.queueServiceActionCall("licensedurl", "get", KalturaLicensedUrl, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLicensedUrl)


# @package Kaltura
# @subpackage Client
class KalturaMessageTemplateService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, assetType):
        """Retrieve a message template used in push notifications and inbox"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("assetType", assetType);
        self.client.queueServiceActionCall("messagetemplate", "get", KalturaMessageTemplate, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMessageTemplate)

    def update(self, assetType, template):
        """Set the account’s push notifications and inbox messages templates"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("assetType", assetType);
        kparams.addObjectIfDefined("template", template)
        self.client.queueServiceActionCall("messagetemplate", "update", KalturaMessageTemplate, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaMessageTemplate)


# @package Kaltura
# @subpackage Client
class KalturaNotificationService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def initiateCleanup(self):
        """TBD"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("notification", "initiateCleanup", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def register(self, identifier, type):
        """TBD"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("identifier", identifier)
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("notification", "register", KalturaRegistryResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRegistryResponse)

    def setDevicePushToken(self, pushToken):
        """Registers the device push token to the push service"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pushToken", pushToken)
        self.client.queueServiceActionCall("notification", "setDevicePushToken", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaNotificationsPartnerSettingsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self):
        """Retrieve the partner notification settings."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("notificationspartnersettings", "get", KalturaNotificationsPartnerSettings, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaNotificationsPartnerSettings)

    def update(self, settings):
        """Update the account notification settings"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("settings", settings)
        self.client.queueServiceActionCall("notificationspartnersettings", "update", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaNotificationsSettingsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self):
        """Retrieve the user’s notification settings."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("notificationssettings", "get", KalturaNotificationsSettings, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaNotificationsSettings)

    def update(self, settings):
        """Update the user’s notification settings."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("settings", settings)
        self.client.queueServiceActionCall("notificationssettings", "update", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaOssAdapterProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, ossAdapter):
        """Insert new OSS adapter for partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("ossAdapter", ossAdapter)
        self.client.queueServiceActionCall("ossadapterprofile", "add", KalturaOSSAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOSSAdapterProfile)

    def delete(self, ossAdapterId):
        """Delete OSS adapter by OSS adapter id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("ossAdapterId", ossAdapterId);
        self.client.queueServiceActionCall("ossadapterprofile", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def generateSharedSecret(self, ossAdapterId):
        """Generate oss adapter shared secret"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("ossAdapterId", ossAdapterId);
        self.client.queueServiceActionCall("ossadapterprofile", "generateSharedSecret", KalturaOSSAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOSSAdapterProfile)

    def update(self, ossAdapterId, ossAdapter):
        """Update OSS adapter details"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("ossAdapterId", ossAdapterId);
        kparams.addObjectIfDefined("ossAdapter", ossAdapter)
        self.client.queueServiceActionCall("ossadapterprofile", "update", KalturaOSSAdapterProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOSSAdapterProfile)


# @package Kaltura
# @subpackage Client
class KalturaOttCategoryService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, id):
        """Retrieve the list of categories (hierarchical) and their associated channels"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("ottcategory", "get", KalturaOTTCategory, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOTTCategory)


# @package Kaltura
# @subpackage Client
class KalturaOttUserService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def activate(self, partnerId, username, activationToken):
        """Activate the account by activation token"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("username", username)
        kparams.addStringIfDefined("activationToken", activationToken)
        self.client.queueServiceActionCall("ottuser", "activate", KalturaOTTUser, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOTTUser)

    def addRole(self, roleId):
        """Edit user details."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("roleId", roleId);
        self.client.queueServiceActionCall("ottuser", "addRole", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def anonymousLogin(self, partnerId, udid = NotImplemented):
        """Returns tokens (KS and refresh token) for anonymous access"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("udid", udid)
        self.client.queueServiceActionCall("ottuser", "anonymousLogin", KalturaLoginSession, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLoginSession)

    def delete(self):
        """Permanently delete a user. User to delete cannot be an exclusive household master, and cannot be default user."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("ottuser", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def get(self):
        """Retrieving users&#39; data"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("ottuser", "get", KalturaOTTUser, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOTTUser)

    def getEncryptedUserId(self):
        """Resend the activation token to a user"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("ottuser", "getEncryptedUserId", KalturaStringValue, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaStringValue)

    def list(self, filter):
        """Retrieve user by external identifier or username"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("ottuser", "list", KalturaOTTUserListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOTTUserListResponse)

    def login(self, partnerId, username = NotImplemented, password = NotImplemented, extraParams = NotImplemented, udid = NotImplemented):
        """User sign-in via a time-expired sign-in PIN."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("username", username)
        kparams.addStringIfDefined("password", password)
        kparams.addObjectIfDefined("extraParams", extraParams)
        kparams.addStringIfDefined("udid", udid)
        self.client.queueServiceActionCall("ottuser", "login", KalturaLoginResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLoginResponse)

    def loginWithPin(self, partnerId, pin, udid = NotImplemented, secret = NotImplemented):
        """User sign-in via a time-expired sign-in PIN."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("pin", pin)
        kparams.addStringIfDefined("udid", udid)
        kparams.addStringIfDefined("secret", secret)
        self.client.queueServiceActionCall("ottuser", "loginWithPin", KalturaLoginResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLoginResponse)

    def logout(self):
        """Logout the calling user."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("ottuser", "logout", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def refreshSession(self, refreshToken, udid = NotImplemented):
        """Returns new Kaltura session (ks) for the user, using the supplied refresh_token (only if it&#39;s valid and not expired)"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("refreshToken", refreshToken)
        kparams.addStringIfDefined("udid", udid)
        self.client.queueServiceActionCall("ottuser", "refreshSession", KalturaLoginSession, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLoginSession)

    def register(self, partnerId, user, password):
        """Sign up a new user."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addObjectIfDefined("user", user)
        kparams.addStringIfDefined("password", password)
        self.client.queueServiceActionCall("ottuser", "register", KalturaOTTUser, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOTTUser)

    def resendActivationToken(self, partnerId, username):
        """Resend the activation token to a user"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("username", username)
        self.client.queueServiceActionCall("ottuser", "resendActivationToken", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def resetPassword(self, partnerId, username):
        """Send an e-mail with URL to enable the user to set new password."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("username", username)
        self.client.queueServiceActionCall("ottuser", "resetPassword", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def setInitialPassword(self, partnerId, token, password):
        """Renew the user&#39;s password after validating the token that sent as part of URL in e-mail."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("token", token)
        kparams.addStringIfDefined("password", password)
        self.client.queueServiceActionCall("ottuser", "setInitialPassword", KalturaOTTUser, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOTTUser)

    def update(self, user):
        """Given a user name and existing password, change to a new password."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("user", user)
        self.client.queueServiceActionCall("ottuser", "update", KalturaOTTUser, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaOTTUser)

    def updateLoginData(self, username, oldPassword, newPassword):
        """Given a user name and existing password, change to a new password."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("username", username)
        kparams.addStringIfDefined("oldPassword", oldPassword)
        kparams.addStringIfDefined("newPassword", newPassword)
        self.client.queueServiceActionCall("ottuser", "updateLoginData", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaParentalRuleService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def disable(self, ruleId, entityReference):
        """Disables a parental rule that was previously defined by the household master. Disable can be at specific user or household level."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("ruleId", ruleId);
        kparams.addStringIfDefined("entityReference", entityReference)
        self.client.queueServiceActionCall("parentalrule", "disable", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def disableDefault(self, entityReference):
        """Disables a parental rule that was defined at account level. Disable can be at specific user or household level."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entityReference", entityReference)
        self.client.queueServiceActionCall("parentalrule", "disableDefault", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def enable(self, ruleId, entityReference):
        """Enable a parental rules for a user"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("ruleId", ruleId);
        kparams.addStringIfDefined("entityReference", entityReference)
        self.client.queueServiceActionCall("parentalrule", "enable", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self, filter):
        """Return the parental rules that applies for the user or household. Can include rules that have been associated in account, household, or user level.
                    Association level is also specified in the response."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("parentalrule", "list", KalturaParentalRuleListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaParentalRuleListResponse)


# @package Kaltura
# @subpackage Client
class KalturaPartnerConfigurationService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def update(self, configuration):
        """Update Partner Configuration"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("configuration", configuration)
        self.client.queueServiceActionCall("partnerconfiguration", "update", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaPaymentGatewayProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, paymentGateway):
        """Insert new payment gateway for partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("paymentGateway", paymentGateway)
        self.client.queueServiceActionCall("paymentgatewayprofile", "add", KalturaPaymentGatewayProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentGatewayProfile)

    def delete(self, paymentGatewayId):
        """Delete payment gateway by payment gateway id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        self.client.queueServiceActionCall("paymentgatewayprofile", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def generateSharedSecret(self, paymentGatewayId):
        """Generate payment gateway shared secret"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        self.client.queueServiceActionCall("paymentgatewayprofile", "generateSharedSecret", KalturaPaymentGatewayProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentGatewayProfile)

    def getConfiguration(self, alias, intent, extraParameters):
        """Gets the Payment Gateway Configuration for the payment gateway identifier given"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("alias", alias)
        kparams.addStringIfDefined("intent", intent)
        kparams.addArrayIfDefined("extraParameters", extraParameters)
        self.client.queueServiceActionCall("paymentgatewayprofile", "getConfiguration", KalturaPaymentGatewayConfiguration, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentGatewayConfiguration)

    def list(self):
        """Returns all payment gateways for partner : id + name"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("paymentgatewayprofile", "list", KalturaPaymentGatewayProfileListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentGatewayProfileListResponse)

    def update(self, paymentGatewayId, paymentGateway):
        """Update payment gateway details"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentGatewayId", paymentGatewayId);
        kparams.addObjectIfDefined("paymentGateway", paymentGateway)
        self.client.queueServiceActionCall("paymentgatewayprofile", "update", KalturaPaymentGatewayProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentGatewayProfile)


# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, paymentMethod):
        """TBD"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("paymentMethod", paymentMethod)
        self.client.queueServiceActionCall("paymentmethodprofile", "add", KalturaPaymentMethodProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentMethodProfile)

    def delete(self, paymentMethodId):
        """Delete payment method profile"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentMethodId", paymentMethodId);
        self.client.queueServiceActionCall("paymentmethodprofile", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def list(self, filter):
        """TBD"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("paymentmethodprofile", "list", KalturaPaymentMethodProfileListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentMethodProfileListResponse)

    def update(self, paymentMethodId, paymentMethod):
        """Update payment method"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("paymentMethodId", paymentMethodId);
        kparams.addObjectIfDefined("paymentMethod", paymentMethod)
        self.client.queueServiceActionCall("paymentmethodprofile", "update", KalturaPaymentMethodProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPaymentMethodProfile)


# @package Kaltura
# @subpackage Client
class KalturaPersonalFeedService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """List user&#39;s feeds.
                    Possible status codes:"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("personalfeed", "list", KalturaPersonalFeedListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPersonalFeedListResponse)


# @package Kaltura
# @subpackage Client
class KalturaPinService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, by, type, ruleId = NotImplemented):
        """Retrieve the parental or purchase PIN that applies for the household or user. Includes specification of where the PIN was defined at – account, household or user  level"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("by", by)
        kparams.addStringIfDefined("type", type)
        kparams.addIntIfDefined("ruleId", ruleId);
        self.client.queueServiceActionCall("pin", "get", KalturaPin, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPin)

    def update(self, by, type, pin, ruleId = NotImplemented):
        """Set the parental or purchase PIN that applies for the user or the household."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("by", by)
        kparams.addStringIfDefined("type", type)
        kparams.addObjectIfDefined("pin", pin)
        kparams.addIntIfDefined("ruleId", ruleId);
        self.client.queueServiceActionCall("pin", "update", KalturaPin, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPin)

    def validate(self, pin, type, ruleId = NotImplemented):
        """Validate a purchase or parental PIN for a user."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pin", pin)
        kparams.addStringIfDefined("type", type)
        kparams.addIntIfDefined("ruleId", ruleId);
        self.client.queueServiceActionCall("pin", "validate", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaPpvService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, id):
        """Returns ppv object by internal identifier"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("ppv", "get", KalturaPpv, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPpv)


# @package Kaltura
# @subpackage Client
class KalturaProductPriceService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter):
        """Returns a price and a purchase status for each subscription or/and media file, for a given user (if passed) and with the consideration of a coupon code (if passed)."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("productprice", "list", KalturaProductPriceListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaProductPriceListResponse)


# @package Kaltura
# @subpackage Client
class KalturaPurchaseSettingsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, by):
        """Retrieve the purchase settings.
                    Includes specification of where these settings were defined – account, household or user"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("by", by)
        self.client.queueServiceActionCall("purchasesettings", "get", KalturaPurchaseSettings, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPurchaseSettings)

    def update(self, entityReference, settings):
        """Set a purchase PIN for the household or user"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entityReference", entityReference)
        kparams.addObjectIfDefined("settings", settings)
        self.client.queueServiceActionCall("purchasesettings", "update", KalturaPurchaseSettings, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaPurchaseSettings)


# @package Kaltura
# @subpackage Client
class KalturaRecommendationProfileService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, recommendationEngine):
        """Insert new recommendation engine for partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("recommendationEngine", recommendationEngine)
        self.client.queueServiceActionCall("recommendationprofile", "add", KalturaRecommendationProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecommendationProfile)

    def delete(self, id):
        """Delete recommendation engine by recommendation engine id"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("recommendationprofile", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def generateSharedSecret(self, recommendationEngineId):
        """Generate recommendation engine  shared secret"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("recommendationEngineId", recommendationEngineId);
        self.client.queueServiceActionCall("recommendationprofile", "generateSharedSecret", KalturaRecommendationProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecommendationProfile)

    def list(self):
        """Returns all recommendation engines for partner"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("recommendationprofile", "list", KalturaRecommendationProfileListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecommendationProfileListResponse)

    def update(self, recommendationEngineId, recommendationEngine):
        """Update recommendation engine details"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("recommendationEngineId", recommendationEngineId);
        kparams.addObjectIfDefined("recommendationEngine", recommendationEngine)
        self.client.queueServiceActionCall("recommendationprofile", "update", KalturaRecommendationProfile, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecommendationProfile)


# @package Kaltura
# @subpackage Client
class KalturaRecordingService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, recording):
        """Issue a record request for a program"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("recording", recording)
        self.client.queueServiceActionCall("recording", "add", KalturaRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecording)

    def cancel(self, id):
        """Cancel a previously requested recording. Cancel recording can be called for recording in status Scheduled or Recording Only"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("recording", "cancel", KalturaRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecording)

    def delete(self, id):
        """Delete one or more user recording(s). Delete recording can be called only for recordings in status Recorded"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("recording", "delete", KalturaRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecording)

    def get(self, id):
        """Returns recording object by internal identifier"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("recording", "get", KalturaRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecording)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Return a list of recordings for the household with optional filter by status and KSQL."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("recording", "list", KalturaRecordingListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecordingListResponse)

    def protect(self, id):
        """Protects an existing recording from the cleanup process for the defined protection period"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("recording", "protect", KalturaRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRecording)


# @package Kaltura
# @subpackage Client
class KalturaRegionService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter):
        """Returns all regions for the partner"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("region", "list", KalturaRegionListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRegionListResponse)


# @package Kaltura
# @subpackage Client
class KalturaRegistrySettingsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self):
        """Retrieve the registry settings."""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("registrysettings", "list", KalturaRegistrySettingsListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaRegistrySettingsListResponse)


# @package Kaltura
# @subpackage Client
class KalturaSeriesRecordingService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, recording):
        """Issue a record request for a complete season or series"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("recording", recording)
        self.client.queueServiceActionCall("seriesrecording", "add", KalturaSeriesRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSeriesRecording)

    def cancel(self, id):
        """Cancel a previously requested series recording. Cancel series recording can be called for recording in status Scheduled or Recording Only"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("seriesrecording", "cancel", KalturaSeriesRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSeriesRecording)

    def cancelByEpgId(self, id, epgId):
        """Cancel EPG recording that was recorded as part of series"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("epgId", epgId);
        self.client.queueServiceActionCall("seriesrecording", "cancelByEpgId", KalturaSeriesRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSeriesRecording)

    def cancelBySeasonNumber(self, id, seasonNumber):
        """Cancel Season recording epgs that was recorded as part of series"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("seasonNumber", seasonNumber);
        self.client.queueServiceActionCall("seriesrecording", "cancelBySeasonNumber", KalturaSeriesRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSeriesRecording)

    def delete(self, id):
        """Delete series recording(s). Delete series recording can be called recordings in any status"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("seriesrecording", "delete", KalturaSeriesRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSeriesRecording)

    def deleteBySeasonNumber(self, id, seasonNumber):
        """Delete Season recording epgs that was recorded as part of series"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("seasonNumber", seasonNumber);
        self.client.queueServiceActionCall("seriesrecording", "deleteBySeasonNumber", KalturaSeriesRecording, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSeriesRecording)

    def list(self, filter = NotImplemented):
        """Return a list of series recordings for the household with optional filter by status and KSQL."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("seriesrecording", "list", KalturaSeriesRecordingListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSeriesRecordingListResponse)


# @package Kaltura
# @subpackage Client
class KalturaSessionService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, session = NotImplemented):
        """Parses KS"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("session", session)
        self.client.queueServiceActionCall("session", "get", KalturaSession, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSession)

    def switchUser(self, userIdToSwitch):
        """Switching the user in the session by generating a new session for a new user within the same household"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("userIdToSwitch", userIdToSwitch)
        self.client.queueServiceActionCall("session", "switchUser", KalturaLoginSession, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLoginSession)


# @package Kaltura
# @subpackage Client
class KalturaSocialService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, type):
        """Return the user object with social information according to a provided external social token"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("social", "get", KalturaSocial, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSocial)

    def getByToken(self, partnerId, token, type):
        """Return the user object with social information according to a provided external social token"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("token", token)
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("social", "getByToken", KalturaSocial, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSocial)

    def getConfiguration(self, partnerId, type):
        """Retrieve the social network’s configuration information"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("social", "getConfiguration", KalturaSocialConfig, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSocialConfig)

    def login(self, partnerId, token, type, udid = NotImplemented):
        """Login using social token"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("token", token)
        kparams.addStringIfDefined("type", type)
        kparams.addStringIfDefined("udid", udid)
        self.client.queueServiceActionCall("social", "login", KalturaLoginResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaLoginResponse)

    def merge(self, token, type):
        """Connect an existing user in the system to an external social network user"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("token", token)
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("social", "merge", KalturaSocial, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSocial)

    def register(self, partnerId, token, type):
        """Create a new user in the system using a provided external social token"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("partnerId", partnerId);
        kparams.addStringIfDefined("token", token)
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("social", "register", KalturaSocial, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSocial)

    def unmerge(self, type):
        """Disconnect an existing user in the system from its external social network user"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("type", type)
        self.client.queueServiceActionCall("social", "unmerge", KalturaSocial, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSocial)


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter):
        """Returns a list of subscriptions requested by Subscription ID or file ID"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("subscription", "list", KalturaSubscriptionListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaSubscriptionListResponse)


# @package Kaltura
# @subpackage Client
class KalturaSystemService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getCountry(self, ip = NotImplemented):
        """Returns country details by the provided IP, if not provided - by the client IP"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("ip", ip)
        self.client.queueServiceActionCall("system", "getCountry", KalturaCountry, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaCountry)

    def getTime(self):
        """Returns current server timestamp"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("system", "getTime", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def getVersion(self):
        """Returns current server version"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("system", "getVersion", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

    def ping(self):
        """Returns true"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("system", "ping", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaTimeShiftedTvPartnerSettingsService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self):
        """Retrieve the account’s time-shifted TV settings (catch-up and C-DVR, Trick-play, Start-over)"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("timeshiftedtvpartnersettings", "get", KalturaTimeShiftedTvPartnerSettings, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaTimeShiftedTvPartnerSettings)

    def update(self, settings):
        """Configure the account’s time-shifted TV settings (catch-up and C-DVR, Trick-play, Start-over)"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("settings", settings)
        self.client.queueServiceActionCall("timeshiftedtvpartnersettings", "update", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaTopicService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def delete(self, id):
        """TBD"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("topic", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def get(self, id):
        """TBD"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("topic", "get", KalturaTopic, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaTopic)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """TBD"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("topic", "list", KalturaTopicListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaTopicListResponse)

    def updateStatus(self, id, automaticIssueNotification):
        """TBD"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addStringIfDefined("automaticIssueNotification", automaticIssueNotification)
        self.client.queueServiceActionCall("topic", "updateStatus", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)


# @package Kaltura
# @subpackage Client
class KalturaTransactionService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def getPurchaseSessionId(self, purchaseSession):
        """Retrieve the purchase session identifier"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("purchaseSession", purchaseSession)
        self.client.queueServiceActionCall("transaction", "getPurchaseSessionId", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeInt(resultNode)

    def purchase(self, purchase):
        """Purchase specific product or subscription for a household. Upon successful charge entitlements to use the requested product or subscription are granted."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("purchase", purchase)
        self.client.queueServiceActionCall("transaction", "purchase", KalturaTransaction, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaTransaction)

    def setWaiver(self, assetId, transactionType):
        """This method shall set the waiver flag on the user entitlement table and the waiver date field to the current date."""

        kparams = KalturaParams()
        kparams.addIntIfDefined("assetId", assetId);
        kparams.addStringIfDefined("transactionType", transactionType)
        self.client.queueServiceActionCall("transaction", "setWaiver", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def updateStatus(self, paymentGatewayId, externalTransactionId, signature, status):
        """Updates a pending purchase transaction state."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("paymentGatewayId", paymentGatewayId)
        kparams.addStringIfDefined("externalTransactionId", externalTransactionId)
        kparams.addStringIfDefined("signature", signature)
        kparams.addObjectIfDefined("status", status)
        self.client.queueServiceActionCall("transaction", "updateStatus", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def validateReceipt(self, externalReceipt):
        """Verifies PPV/Subscription/Collection client purchase (such as InApp) and entitles the user."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("externalReceipt", externalReceipt)
        self.client.queueServiceActionCall("transaction", "validateReceipt", KalturaTransaction, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaTransaction)


# @package Kaltura
# @subpackage Client
class KalturaTransactionHistoryService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Gets user or household transaction history."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("transactionhistory", "list", KalturaBillingTransactionListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBillingTransactionListResponse)


# @package Kaltura
# @subpackage Client
class KalturaUserAssetRuleService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter):
        """Retrieve all the rules (parental, geo, device or user-type) that applies for this user and asset."""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("userassetrule", "list", KalturaUserAssetRuleListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserAssetRuleListResponse)


# @package Kaltura
# @subpackage Client
class KalturaUserAssetsListItemService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, userAssetsListItem):
        """Adds a new item to user’s private asset list"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("userAssetsListItem", userAssetsListItem)
        self.client.queueServiceActionCall("userassetslistitem", "add", KalturaUserAssetsListItem, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserAssetsListItem)

    def delete(self, assetId, listType):
        """Deletes an item from user’s private asset list"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("assetId", assetId)
        kparams.addStringIfDefined("listType", listType)
        self.client.queueServiceActionCall("userassetslistitem", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def get(self, assetId, listType, itemType):
        """Get an item from user’s private asset list"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("assetId", assetId)
        kparams.addStringIfDefined("listType", listType)
        kparams.addStringIfDefined("itemType", itemType)
        self.client.queueServiceActionCall("userassetslistitem", "get", KalturaUserAssetsListItem, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserAssetsListItem)


# @package Kaltura
# @subpackage Client
class KalturaUserLoginPinService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, secret = NotImplemented):
        """Generate a time and usage expiry login-PIN that can allow a single login per PIN. If an active login-PIN already exists. Calling this API again for same user will add another login-PIN"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("secret", secret)
        self.client.queueServiceActionCall("userloginpin", "add", KalturaUserLoginPin, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserLoginPin)

    def delete(self, pinCode):
        """Immediately expire all active login-PINs for a user"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pinCode", pinCode)
        self.client.queueServiceActionCall("userloginpin", "delete", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def deleteAll(self):
        """Immediately expire all active login-PINs for a user"""

        kparams = KalturaParams()
        self.client.queueServiceActionCall("userloginpin", "deleteAll", None, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeBool(resultNode)

    def update(self, pinCode, secret = NotImplemented):
        """Set a time and usage expiry login-PIN that can allow a single login per PIN. If an active login-PIN already exists. Calling this API again for same user will add another login-PIN"""

        kparams = KalturaParams()
        kparams.addStringIfDefined("pinCode", pinCode)
        kparams.addStringIfDefined("secret", secret)
        self.client.queueServiceActionCall("userloginpin", "update", KalturaUserLoginPin, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserLoginPin)


# @package Kaltura
# @subpackage Client
class KalturaUserRoleService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def list(self, filter = NotImplemented):
        """Retrieving user roles by identifiers, if filter is empty, returns all partner roles"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        self.client.queueServiceActionCall("userrole", "list", KalturaUserRoleListResponse, kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUserRoleListResponse)

########## main ##########
class KalturaCoreClient(KalturaClientPlugin):
    # KalturaCoreClient
    instance = None

    # @return KalturaCoreClient
    @staticmethod
    def get():
        if KalturaCoreClient.instance == None:
            KalturaCoreClient.instance = KalturaCoreClient()
        return KalturaCoreClient.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'announcement': KalturaAnnouncementService,
            'appToken': KalturaAppTokenService,
            'assetComment': KalturaAssetCommentService,
            'asset': KalturaAssetService,
            'assetFile': KalturaAssetFileService,
            'assetHistory': KalturaAssetHistoryService,
            'assetStatistics': KalturaAssetStatisticsService,
            'bookmark': KalturaBookmarkService,
            'cdnAdapterProfile': KalturaCdnAdapterProfileService,
            'cdnPartnerSettings': KalturaCdnPartnerSettingsService,
            'cDVRAdapterProfile': KalturaCDVRAdapterProfileService,
            'channel': KalturaChannelService,
            'coupon': KalturaCouponService,
            'entitlement': KalturaEntitlementService,
            'exportTask': KalturaExportTaskService,
            'externalChannelProfile': KalturaExternalChannelProfileService,
            'favorite': KalturaFavoriteService,
            'followTvSeries': KalturaFollowTvSeriesService,
            'homeNetwork': KalturaHomeNetworkService,
            'household': KalturaHouseholdService,
            'householdDevice': KalturaHouseholdDeviceService,
            'householdLimitations': KalturaHouseholdLimitationsService,
            'householdPaymentGateway': KalturaHouseholdPaymentGatewayService,
            'householdPaymentMethod': KalturaHouseholdPaymentMethodService,
            'householdPremiumService': KalturaHouseholdPremiumServiceService,
            'householdQuota': KalturaHouseholdQuotaService,
            'householdUser': KalturaHouseholdUserService,
            'inboxMessage': KalturaInboxMessageService,
            'licensedUrl': KalturaLicensedUrlService,
            'messageTemplate': KalturaMessageTemplateService,
            'notification': KalturaNotificationService,
            'notificationsPartnerSettings': KalturaNotificationsPartnerSettingsService,
            'notificationsSettings': KalturaNotificationsSettingsService,
            'ossAdapterProfile': KalturaOssAdapterProfileService,
            'ottCategory': KalturaOttCategoryService,
            'ottUser': KalturaOttUserService,
            'parentalRule': KalturaParentalRuleService,
            'partnerConfiguration': KalturaPartnerConfigurationService,
            'paymentGatewayProfile': KalturaPaymentGatewayProfileService,
            'paymentMethodProfile': KalturaPaymentMethodProfileService,
            'personalFeed': KalturaPersonalFeedService,
            'pin': KalturaPinService,
            'ppv': KalturaPpvService,
            'productPrice': KalturaProductPriceService,
            'purchaseSettings': KalturaPurchaseSettingsService,
            'recommendationProfile': KalturaRecommendationProfileService,
            'recording': KalturaRecordingService,
            'region': KalturaRegionService,
            'registrySettings': KalturaRegistrySettingsService,
            'seriesRecording': KalturaSeriesRecordingService,
            'session': KalturaSessionService,
            'social': KalturaSocialService,
            'subscription': KalturaSubscriptionService,
            'system': KalturaSystemService,
            'timeShiftedTvPartnerSettings': KalturaTimeShiftedTvPartnerSettingsService,
            'topic': KalturaTopicService,
            'transaction': KalturaTransactionService,
            'transactionHistory': KalturaTransactionHistoryService,
            'userAssetRule': KalturaUserAssetRuleService,
            'userAssetsListItem': KalturaUserAssetsListItemService,
            'userLoginPin': KalturaUserLoginPinService,
            'userRole': KalturaUserRoleService,
        }

    def getEnums(self):
        return {
            'KalturaAnnouncementOrderBy': KalturaAnnouncementOrderBy,
            'KalturaAnnouncementRecipientsType': KalturaAnnouncementRecipientsType,
            'KalturaAnnouncementStatus': KalturaAnnouncementStatus,
            'KalturaApiParameterPermissionItemAction': KalturaApiParameterPermissionItemAction,
            'KalturaAppTokenHashType': KalturaAppTokenHashType,
            'KalturaAppTokenStatus': KalturaAppTokenStatus,
            'KalturaAssetCommentOrderBy': KalturaAssetCommentOrderBy,
            'KalturaAssetHistoryOrderBy': KalturaAssetHistoryOrderBy,
            'KalturaAssetOrderBy': KalturaAssetOrderBy,
            'KalturaAssetReferenceType': KalturaAssetReferenceType,
            'KalturaAssetType': KalturaAssetType,
            'KalturaBillingAction': KalturaBillingAction,
            'KalturaBillingItemsType': KalturaBillingItemsType,
            'KalturaBookmarkActionType': KalturaBookmarkActionType,
            'KalturaBookmarkOrderBy': KalturaBookmarkOrderBy,
            'KalturaBundleType': KalturaBundleType,
            'KalturaChannelEnrichment': KalturaChannelEnrichment,
            'KalturaCouponStatus': KalturaCouponStatus,
            'KalturaDeviceStatus': KalturaDeviceStatus,
            'KalturaEntitlementOrderBy': KalturaEntitlementOrderBy,
            'KalturaEntityReferenceBy': KalturaEntityReferenceBy,
            'KalturaExportDataType': KalturaExportDataType,
            'KalturaExportTaskOrderBy': KalturaExportTaskOrderBy,
            'KalturaExportType': KalturaExportType,
            'KalturaFavoriteOrderBy': KalturaFavoriteOrderBy,
            'KalturaFollowTvSeriesOrderBy': KalturaFollowTvSeriesOrderBy,
            'KalturaHouseholdFrequencyType': KalturaHouseholdFrequencyType,
            'KalturaHouseholdPaymentGatewaySelectedBy': KalturaHouseholdPaymentGatewaySelectedBy,
            'KalturaHouseholdRestriction': KalturaHouseholdRestriction,
            'KalturaHouseholdState': KalturaHouseholdState,
            'KalturaHouseholdSuspentionState': KalturaHouseholdSuspentionState,
            'KalturaHouseholdUserStatus': KalturaHouseholdUserStatus,
            'KalturaInboxMessageOrderBy': KalturaInboxMessageOrderBy,
            'KalturaInboxMessageStatus': KalturaInboxMessageStatus,
            'KalturaInboxMessageType': KalturaInboxMessageType,
            'KalturaNotificationType': KalturaNotificationType,
            'KalturaOTTAssetType': KalturaOTTAssetType,
            'KalturaOTTUserBy': KalturaOTTUserBy,
            'KalturaOTTUserOrderBy': KalturaOTTUserOrderBy,
            'KalturaParentalRuleOrderBy': KalturaParentalRuleOrderBy,
            'KalturaParentalRuleType': KalturaParentalRuleType,
            'KalturaPartnerConfigurationType': KalturaPartnerConfigurationType,
            'KalturaPaymentMethodProfileOrderBy': KalturaPaymentMethodProfileOrderBy,
            'KalturaPaymentMethodType': KalturaPaymentMethodType,
            'KalturaPersonalFeedOrderBy': KalturaPersonalFeedOrderBy,
            'KalturaPinType': KalturaPinType,
            'KalturaPositionOwner': KalturaPositionOwner,
            'KalturaProductPriceOrderBy': KalturaProductPriceOrderBy,
            'KalturaPurchaseSettingsType': KalturaPurchaseSettingsType,
            'KalturaPurchaseStatus': KalturaPurchaseStatus,
            'KalturaRecordingOrderBy': KalturaRecordingOrderBy,
            'KalturaRecordingStatus': KalturaRecordingStatus,
            'KalturaRecordingType': KalturaRecordingType,
            'KalturaRegionOrderBy': KalturaRegionOrderBy,
            'KalturaRuleLevel': KalturaRuleLevel,
            'KalturaRuleType': KalturaRuleType,
            'KalturaSeriesRecordingOrderBy': KalturaSeriesRecordingOrderBy,
            'KalturaSessionType': KalturaSessionType,
            'KalturaSocialNetwork': KalturaSocialNetwork,
            'KalturaStreamType': KalturaStreamType,
            'KalturaSubscriptionOrderBy': KalturaSubscriptionOrderBy,
            'KalturaTopicAutomaticIssueNotification': KalturaTopicAutomaticIssueNotification,
            'KalturaTopicOrderBy': KalturaTopicOrderBy,
            'KalturaTransactionAdapterStatus': KalturaTransactionAdapterStatus,
            'KalturaTransactionHistoryOrderBy': KalturaTransactionHistoryOrderBy,
            'KalturaTransactionType': KalturaTransactionType,
            'KalturaUserAssetRuleOrderBy': KalturaUserAssetRuleOrderBy,
            'KalturaUserAssetsListItemType': KalturaUserAssetsListItemType,
            'KalturaUserAssetsListType': KalturaUserAssetsListType,
            'KalturaUserRoleOrderBy': KalturaUserRoleOrderBy,
            'KalturaUserState': KalturaUserState,
            'KalturaWatchStatus': KalturaWatchStatus,
        }

    def getTypes(self):
        return {
            'KalturaAnnouncement': KalturaAnnouncement,
            'KalturaFilter': KalturaFilter,
            'KalturaAnnouncementFilter': KalturaAnnouncementFilter,
            'KalturaFilterPager': KalturaFilterPager,
            'KalturaListResponse': KalturaListResponse,
            'KalturaRegionalChannel': KalturaRegionalChannel,
            'KalturaRegion': KalturaRegion,
            'KalturaRegionListResponse': KalturaRegionListResponse,
            'KalturaUserAssetRule': KalturaUserAssetRule,
            'KalturaUserAssetRuleListResponse': KalturaUserAssetRuleListResponse,
            'KalturaValue': KalturaValue,
            'KalturaLongValue': KalturaLongValue,
            'KalturaDoubleValue': KalturaDoubleValue,
            'KalturaBooleanValue': KalturaBooleanValue,
            'KalturaIntegerValue': KalturaIntegerValue,
            'KalturaStringValue': KalturaStringValue,
            'KalturaCDNAdapterProfile': KalturaCDNAdapterProfile,
            'KalturaCDNAdapterProfileListResponse': KalturaCDNAdapterProfileListResponse,
            'KalturaSlimAsset': KalturaSlimAsset,
            'KalturaBaseOTTUser': KalturaBaseOTTUser,
            'KalturaCountry': KalturaCountry,
            'KalturaOTTUserType': KalturaOTTUserType,
            'KalturaOTTUser': KalturaOTTUser,
            'KalturaBookmarkPlayerData': KalturaBookmarkPlayerData,
            'KalturaBookmark': KalturaBookmark,
            'KalturaBookmarkListResponse': KalturaBookmarkListResponse,
            'KalturaStringValueArray': KalturaStringValueArray,
            'KalturaMediaImage': KalturaMediaImage,
            'KalturaMediaFile': KalturaMediaFile,
            'KalturaBuzzScore': KalturaBuzzScore,
            'KalturaAssetStatistics': KalturaAssetStatistics,
            'KalturaBaseAssetInfo': KalturaBaseAssetInfo,
            'KalturaAsset': KalturaAsset,
            'KalturaAssetListResponse': KalturaAssetListResponse,
            'KalturaProgramAsset': KalturaProgramAsset,
            'KalturaMediaAsset': KalturaMediaAsset,
            'KalturaAssetComment': KalturaAssetComment,
            'KalturaAssetCommentListResponse': KalturaAssetCommentListResponse,
            'KalturaSeriesRecording': KalturaSeriesRecording,
            'KalturaSeriesRecordingListResponse': KalturaSeriesRecordingListResponse,
            'KalturaPremiumService': KalturaPremiumService,
            'KalturaHouseholdPremiumService': KalturaHouseholdPremiumService,
            'KalturaHouseholdPremiumServiceListResponse': KalturaHouseholdPremiumServiceListResponse,
            'KalturaCDVRAdapterProfile': KalturaCDVRAdapterProfile,
            'KalturaCDVRAdapterProfileListResponse': KalturaCDVRAdapterProfileListResponse,
            'KalturaExportTask': KalturaExportTask,
            'KalturaExportTaskListResponse': KalturaExportTaskListResponse,
            'KalturaChannelEnrichmentHolder': KalturaChannelEnrichmentHolder,
            'KalturaExternalChannelProfile': KalturaExternalChannelProfile,
            'KalturaExternalChannelProfileListResponse': KalturaExternalChannelProfileListResponse,
            'KalturaRecommendationProfile': KalturaRecommendationProfile,
            'KalturaRecommendationProfileListResponse': KalturaRecommendationProfileListResponse,
            'KalturaRegistrySettings': KalturaRegistrySettings,
            'KalturaRegistrySettingsListResponse': KalturaRegistrySettingsListResponse,
            'KalturaHouseholdPaymentMethod': KalturaHouseholdPaymentMethod,
            'KalturaHouseholdPaymentMethodListResponse': KalturaHouseholdPaymentMethodListResponse,
            'KalturaPaymentMethodProfile': KalturaPaymentMethodProfile,
            'KalturaPaymentMethodProfileListResponse': KalturaPaymentMethodProfileListResponse,
            'KalturaPrice': KalturaPrice,
            'KalturaProductPrice': KalturaProductPrice,
            'KalturaTranslationToken': KalturaTranslationToken,
            'KalturaPpvPrice': KalturaPpvPrice,
            'KalturaPPVItemPriceDetails': KalturaPPVItemPriceDetails,
            'KalturaItemPrice': KalturaItemPrice,
            'KalturaSubscriptionPrice': KalturaSubscriptionPrice,
            'KalturaHouseholdPaymentGateway': KalturaHouseholdPaymentGateway,
            'KalturaHouseholdPaymentGatewayListResponse': KalturaHouseholdPaymentGatewayListResponse,
            'KalturaPaymentGatewayBaseProfile': KalturaPaymentGatewayBaseProfile,
            'KalturaPaymentGatewayProfile': KalturaPaymentGatewayProfile,
            'KalturaPaymentGatewayProfileListResponse': KalturaPaymentGatewayProfileListResponse,
            'KalturaParentalRule': KalturaParentalRule,
            'KalturaParentalRuleListResponse': KalturaParentalRuleListResponse,
            'KalturaRecording': KalturaRecording,
            'KalturaRecordingListResponse': KalturaRecordingListResponse,
            'KalturaBillingTransaction': KalturaBillingTransaction,
            'KalturaBillingTransactionListResponse': KalturaBillingTransactionListResponse,
            'KalturaPermissionItem': KalturaPermissionItem,
            'KalturaPermission': KalturaPermission,
            'KalturaUserRole': KalturaUserRole,
            'KalturaUserRoleListResponse': KalturaUserRoleListResponse,
            'KalturaGroupPermission': KalturaGroupPermission,
            'KalturaApiArgumentPermissionItem': KalturaApiArgumentPermissionItem,
            'KalturaApiParameterPermissionItem': KalturaApiParameterPermissionItem,
            'KalturaApiActionPermissionItem': KalturaApiActionPermissionItem,
            'KalturaInboxMessage': KalturaInboxMessage,
            'KalturaInboxMessageListResponse': KalturaInboxMessageListResponse,
            'KalturaFollowDataBase': KalturaFollowDataBase,
            'KalturaFollowTvSeries': KalturaFollowTvSeries,
            'KalturaFollowTvSeriesListResponse': KalturaFollowTvSeriesListResponse,
            'KalturaAnnouncementListResponse': KalturaAnnouncementListResponse,
            'KalturaFeed': KalturaFeed,
            'KalturaPersonalFeed': KalturaPersonalFeed,
            'KalturaPersonalFeedListResponse': KalturaPersonalFeedListResponse,
            'KalturaTopic': KalturaTopic,
            'KalturaTopicListResponse': KalturaTopicListResponse,
            'KalturaProductPriceListResponse': KalturaProductPriceListResponse,
            'KalturaItemPriceListResponse': KalturaItemPriceListResponse,
            'KalturaBaseChannel': KalturaBaseChannel,
            'KalturaChannel': KalturaChannel,
            'KalturaPriceDetails': KalturaPriceDetails,
            'KalturaDiscountModule': KalturaDiscountModule,
            'KalturaCouponsGroup': KalturaCouponsGroup,
            'KalturaUsageModule': KalturaUsageModule,
            'KalturaPricePlan': KalturaPricePlan,
            'KalturaPreviewModule': KalturaPreviewModule,
            'KalturaSubscription': KalturaSubscription,
            'KalturaSubscriptionListResponse': KalturaSubscriptionListResponse,
            'KalturaProductsPriceListResponse': KalturaProductsPriceListResponse,
            'KalturaEntitlement': KalturaEntitlement,
            'KalturaEntitlementListResponse': KalturaEntitlementListResponse,
            'KalturaHomeNetwork': KalturaHomeNetwork,
            'KalturaHomeNetworkListResponse': KalturaHomeNetworkListResponse,
            'KalturaFavorite': KalturaFavorite,
            'KalturaFavoriteListResponse': KalturaFavoriteListResponse,
            'KalturaOTTUserListResponse': KalturaOTTUserListResponse,
            'KalturaAssetStatisticsListResponse': KalturaAssetStatisticsListResponse,
            'KalturaSlimAssetInfoWrapper': KalturaSlimAssetInfoWrapper,
            'KalturaAssetHistory': KalturaAssetHistory,
            'KalturaAssetHistoryListResponse': KalturaAssetHistoryListResponse,
            'KalturaAppToken': KalturaAppToken,
            'KalturaSession': KalturaSession,
            'KalturaSessionInfo': KalturaSessionInfo,
            'KalturaAssetFilter': KalturaAssetFilter,
            'KalturaBundleFilter': KalturaBundleFilter,
            'KalturaChannelExternalFilter': KalturaChannelExternalFilter,
            'KalturaChannelFilter': KalturaChannelFilter,
            'KalturaRelatedFilter': KalturaRelatedFilter,
            'KalturaRelatedExternalFilter': KalturaRelatedExternalFilter,
            'KalturaSearchAssetFilter': KalturaSearchAssetFilter,
            'KalturaSearchExternalFilter': KalturaSearchExternalFilter,
            'KalturaAssetFileContext': KalturaAssetFileContext,
            'KalturaAssetStatisticsQuery': KalturaAssetStatisticsQuery,
            'KalturaCDNPartnerSettings': KalturaCDNPartnerSettings,
            'KalturaRegionFilter': KalturaRegionFilter,
            'KalturaAssetCommentFilter': KalturaAssetCommentFilter,
            'KalturaKeyValue': KalturaKeyValue,
            'KalturaPaymentGatewayConfiguration': KalturaPaymentGatewayConfiguration,
            'KalturaProductPriceFilter': KalturaProductPriceFilter,
            'KalturaSeriesRecordingFilter': KalturaSeriesRecordingFilter,
            'KalturaHouseholdQuota': KalturaHouseholdQuota,
            'KalturaInboxMessageFilter': KalturaInboxMessageFilter,
            'KalturaMessageTemplate': KalturaMessageTemplate,
            'KalturaFollowTvSeriesFilter': KalturaFollowTvSeriesFilter,
            'KalturaPersonalFeedFilter': KalturaPersonalFeedFilter,
            'KalturaPpv': KalturaPpv,
            'KalturaRecordingFilter': KalturaRecordingFilter,
            'KalturaLicensedUrl': KalturaLicensedUrl,
            'KalturaLicensedUrlBaseRequest': KalturaLicensedUrlBaseRequest,
            'KalturaLicensedUrlMediaRequest': KalturaLicensedUrlMediaRequest,
            'KalturaLicensedUrlEpgRequest': KalturaLicensedUrlEpgRequest,
            'KalturaLicensedUrlRecordingRequest': KalturaLicensedUrlRecordingRequest,
            'KalturaRegistryResponse': KalturaRegistryResponse,
            'KalturaNotificationsPartnerSettings': KalturaNotificationsPartnerSettings,
            'KalturaNotificationsSettings': KalturaNotificationsSettings,
            'KalturaPaymentMethodProfileFilter': KalturaPaymentMethodProfileFilter,
            'KalturaTimeShiftedTvPartnerSettings': KalturaTimeShiftedTvPartnerSettings,
            'KalturaTopicFilter': KalturaTopicFilter,
            'KalturaUserAssetsListItem': KalturaUserAssetsListItem,
            'KalturaDeviceFamilyBase': KalturaDeviceFamilyBase,
            'KalturaHouseholdDevice': KalturaHouseholdDevice,
            'KalturaHouseholdDeviceFamilyLimitations': KalturaHouseholdDeviceFamilyLimitations,
            'KalturaHouseholdLimitations': KalturaHouseholdLimitations,
            'KalturaExportTaskFilter': KalturaExportTaskFilter,
            'KalturaPartnerConfiguration': KalturaPartnerConfiguration,
            'KalturaBillingPartnerConfig': KalturaBillingPartnerConfig,
            'KalturaOSSAdapterBaseProfile': KalturaOSSAdapterBaseProfile,
            'KalturaOSSAdapterProfile': KalturaOSSAdapterProfile,
            'KalturaLoginSession': KalturaLoginSession,
            'KalturaUserAssetRuleFilter': KalturaUserAssetRuleFilter,
            'KalturaAssetHistoryFilter': KalturaAssetHistoryFilter,
            'KalturaHousehold': KalturaHousehold,
            'KalturaDevicePin': KalturaDevicePin,
            'KalturaBookmarkFilter': KalturaBookmarkFilter,
            'KalturaPin': KalturaPin,
            'KalturaPurchaseSettings': KalturaPurchaseSettings,
            'KalturaHouseholdUser': KalturaHouseholdUser,
            'KalturaSubscriptionFilter': KalturaSubscriptionFilter,
            'KalturaOTTCategory': KalturaOTTCategory,
            'KalturaCoupon': KalturaCoupon,
            'KalturaEntitlementFilter': KalturaEntitlementFilter,
            'KalturaFavoriteFilter': KalturaFavoriteFilter,
            'KalturaSocial': KalturaSocial,
            'KalturaFacebookSocial': KalturaFacebookSocial,
            'KalturaLoginResponse': KalturaLoginResponse,
            'KalturaSocialConfig': KalturaSocialConfig,
            'KalturaPurchaseBase': KalturaPurchaseBase,
            'KalturaPurchase': KalturaPurchase,
            'KalturaPurchaseSession': KalturaPurchaseSession,
            'KalturaExternalReceipt': KalturaExternalReceipt,
            'KalturaTransaction': KalturaTransaction,
            'KalturaTransactionStatus': KalturaTransactionStatus,
            'KalturaUserLoginPin': KalturaUserLoginPin,
            'KalturaParentalRuleFilter': KalturaParentalRuleFilter,
            'KalturaTransactionHistoryFilter': KalturaTransactionHistoryFilter,
            'KalturaUserRoleFilter': KalturaUserRoleFilter,
            'KalturaOTTUserFilter': KalturaOTTUserFilter,
        }

    # @return string
    def getName(self):
        return ''

