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
from .CuePoint import *
from KalturaClient.Base import KalturaObjectBase, KalturaServiceBase

class KalturaAnswerCuePointOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    INT_ID_ASC = "+intId"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    START_TIME_ASC = "+startTime"
    TRIGGERED_AT_ASC = "+triggeredAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    INT_ID_DESC = "-intId"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"
    START_TIME_DESC = "-startTime"
    TRIGGERED_AT_DESC = "-triggeredAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaQuestionCuePointOrderBy(object):
    CREATED_AT_ASC = "+createdAt"
    INT_ID_ASC = "+intId"
    PARTNER_SORT_VALUE_ASC = "+partnerSortValue"
    START_TIME_ASC = "+startTime"
    TRIGGERED_AT_ASC = "+triggeredAt"
    UPDATED_AT_ASC = "+updatedAt"
    CREATED_AT_DESC = "-createdAt"
    INT_ID_DESC = "-intId"
    PARTNER_SORT_VALUE_DESC = "-partnerSortValue"
    START_TIME_DESC = "-startTime"
    TRIGGERED_AT_DESC = "-triggeredAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value: str): ...

    def getValue(self) -> str: ...

class KalturaOptionalAnswer(KalturaObjectBase):
    key: str
    text: str
    weight: float
    isCorrect: KalturaNullableBoolean
    def __init__(self,
            key: str = NotImplemented,
            text: str = NotImplemented,
            weight: float = NotImplemented,
            isCorrect: KalturaNullableBoolean = NotImplemented): ...

    def getKey(self) -> str: ...
    def setKey(self, newKey: str) -> None: ...
    def getText(self) -> str: ...
    def setText(self, newText: str) -> None: ...
    def getWeight(self) -> float: ...
    def setWeight(self, newWeight: float) -> None: ...
    def getIsCorrect(self) -> KalturaNullableBoolean: ...
    def setIsCorrect(self, newIsCorrect: KalturaNullableBoolean) -> None: ...

class KalturaQuiz(KalturaObjectBase):
    version: int
    uiAttributes: List[KalturaKeyValue]
    showResultOnAnswer: KalturaNullableBoolean
    showCorrectKeyOnAnswer: KalturaNullableBoolean
    allowAnswerUpdate: KalturaNullableBoolean
    showCorrectAfterSubmission: KalturaNullableBoolean
    allowDownload: KalturaNullableBoolean
    showGradeAfterSubmission: KalturaNullableBoolean
    attemptsAllowed: int
    scoreType: KalturaScoreType
    def __init__(self,
            version: int = NotImplemented,
            uiAttributes: List[KalturaKeyValue] = NotImplemented,
            showResultOnAnswer: KalturaNullableBoolean = NotImplemented,
            showCorrectKeyOnAnswer: KalturaNullableBoolean = NotImplemented,
            allowAnswerUpdate: KalturaNullableBoolean = NotImplemented,
            showCorrectAfterSubmission: KalturaNullableBoolean = NotImplemented,
            allowDownload: KalturaNullableBoolean = NotImplemented,
            showGradeAfterSubmission: KalturaNullableBoolean = NotImplemented,
            attemptsAllowed: int = NotImplemented,
            scoreType: KalturaScoreType = NotImplemented): ...

    def getVersion(self) -> int: ...
    def getUiAttributes(self) -> List[KalturaKeyValue]: ...
    def setUiAttributes(self, newUiAttributes: List[KalturaKeyValue]) -> None: ...
    def getShowResultOnAnswer(self) -> KalturaNullableBoolean: ...
    def setShowResultOnAnswer(self, newShowResultOnAnswer: KalturaNullableBoolean) -> None: ...
    def getShowCorrectKeyOnAnswer(self) -> KalturaNullableBoolean: ...
    def setShowCorrectKeyOnAnswer(self, newShowCorrectKeyOnAnswer: KalturaNullableBoolean) -> None: ...
    def getAllowAnswerUpdate(self) -> KalturaNullableBoolean: ...
    def setAllowAnswerUpdate(self, newAllowAnswerUpdate: KalturaNullableBoolean) -> None: ...
    def getShowCorrectAfterSubmission(self) -> KalturaNullableBoolean: ...
    def setShowCorrectAfterSubmission(self, newShowCorrectAfterSubmission: KalturaNullableBoolean) -> None: ...
    def getAllowDownload(self) -> KalturaNullableBoolean: ...
    def setAllowDownload(self, newAllowDownload: KalturaNullableBoolean) -> None: ...
    def getShowGradeAfterSubmission(self) -> KalturaNullableBoolean: ...
    def setShowGradeAfterSubmission(self, newShowGradeAfterSubmission: KalturaNullableBoolean) -> None: ...
    def getAttemptsAllowed(self) -> int: ...
    def setAttemptsAllowed(self, newAttemptsAllowed: int) -> None: ...
    def getScoreType(self) -> KalturaScoreType: ...
    def setScoreType(self, newScoreType: KalturaScoreType) -> None: ...

class KalturaAnswerCuePoint(KalturaCuePoint):
    parentId: str
    quizUserEntryId: str
    answerKey: str
    openAnswer: str
    isCorrect: KalturaNullableBoolean
    correctAnswerKeys: List[KalturaString]
    explanation: str
    feedback: str
    def __init__(self,
            id: str = NotImplemented,
            intId: int = NotImplemented,
            cuePointType: KalturaCuePointType = NotImplemented,
            status: KalturaCuePointStatus = NotImplemented,
            entryId: str = NotImplemented,
            partnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            triggeredAt: int = NotImplemented,
            tags: str = NotImplemented,
            startTime: int = NotImplemented,
            userId: str = NotImplemented,
            partnerData: str = NotImplemented,
            partnerSortValue: int = NotImplemented,
            forceStop: KalturaNullableBoolean = NotImplemented,
            thumbOffset: int = NotImplemented,
            systemName: str = NotImplemented,
            isMomentary: bool = NotImplemented,
            copiedFrom: str = NotImplemented,
            parentId: str = NotImplemented,
            quizUserEntryId: str = NotImplemented,
            answerKey: str = NotImplemented,
            openAnswer: str = NotImplemented,
            isCorrect: KalturaNullableBoolean = NotImplemented,
            correctAnswerKeys: List[KalturaString] = NotImplemented,
            explanation: str = NotImplemented,
            feedback: str = NotImplemented): ...

    def getParentId(self) -> str: ...
    def setParentId(self, newParentId: str) -> None: ...
    def getQuizUserEntryId(self) -> str: ...
    def setQuizUserEntryId(self, newQuizUserEntryId: str) -> None: ...
    def getAnswerKey(self) -> str: ...
    def setAnswerKey(self, newAnswerKey: str) -> None: ...
    def getOpenAnswer(self) -> str: ...
    def setOpenAnswer(self, newOpenAnswer: str) -> None: ...
    def getIsCorrect(self) -> KalturaNullableBoolean: ...
    def getCorrectAnswerKeys(self) -> List[KalturaString]: ...
    def getExplanation(self) -> str: ...
    def getFeedback(self) -> str: ...
    def setFeedback(self, newFeedback: str) -> None: ...

class KalturaQuestionCuePoint(KalturaCuePoint):
    optionalAnswers: List[KalturaOptionalAnswer]
    hint: str
    question: str
    explanation: str
    questionType: KalturaQuestionType
    presentationOrder: int
    excludeFromScore: KalturaNullableBoolean
    def __init__(self,
            id: str = NotImplemented,
            intId: int = NotImplemented,
            cuePointType: KalturaCuePointType = NotImplemented,
            status: KalturaCuePointStatus = NotImplemented,
            entryId: str = NotImplemented,
            partnerId: int = NotImplemented,
            createdAt: int = NotImplemented,
            updatedAt: int = NotImplemented,
            triggeredAt: int = NotImplemented,
            tags: str = NotImplemented,
            startTime: int = NotImplemented,
            userId: str = NotImplemented,
            partnerData: str = NotImplemented,
            partnerSortValue: int = NotImplemented,
            forceStop: KalturaNullableBoolean = NotImplemented,
            thumbOffset: int = NotImplemented,
            systemName: str = NotImplemented,
            isMomentary: bool = NotImplemented,
            copiedFrom: str = NotImplemented,
            optionalAnswers: List[KalturaOptionalAnswer] = NotImplemented,
            hint: str = NotImplemented,
            question: str = NotImplemented,
            explanation: str = NotImplemented,
            questionType: KalturaQuestionType = NotImplemented,
            presentationOrder: int = NotImplemented,
            excludeFromScore: KalturaNullableBoolean = NotImplemented): ...

    def getOptionalAnswers(self) -> List[KalturaOptionalAnswer]: ...
    def setOptionalAnswers(self, newOptionalAnswers: List[KalturaOptionalAnswer]) -> None: ...
    def getHint(self) -> str: ...
    def setHint(self, newHint: str) -> None: ...
    def getQuestion(self) -> str: ...
    def setQuestion(self, newQuestion: str) -> None: ...
    def getExplanation(self) -> str: ...
    def setExplanation(self, newExplanation: str) -> None: ...
    def getQuestionType(self) -> KalturaQuestionType: ...
    def setQuestionType(self, newQuestionType: KalturaQuestionType) -> None: ...
    def getPresentationOrder(self) -> int: ...
    def setPresentationOrder(self, newPresentationOrder: int) -> None: ...
    def getExcludeFromScore(self) -> KalturaNullableBoolean: ...
    def setExcludeFromScore(self, newExcludeFromScore: KalturaNullableBoolean) -> None: ...

class KalturaQuizAdvancedFilter(KalturaSearchItem):
    isQuiz: KalturaNullableBoolean
    def __init__(self,
            isQuiz: KalturaNullableBoolean = NotImplemented): ...

    def getIsQuiz(self) -> KalturaNullableBoolean: ...
    def setIsQuiz(self, newIsQuiz: KalturaNullableBoolean) -> None: ...

class KalturaQuizListResponse(KalturaListResponse):
    objects: List[KalturaQuiz]
    def __init__(self,
            totalCount: int = NotImplemented,
            objects: List[KalturaQuiz] = NotImplemented): ...

    def getObjects(self) -> List[KalturaQuiz]: ...

class KalturaQuizFilter(KalturaRelatedFilter):
    entryIdEqual: str
    entryIdIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented): ...

    def getEntryIdEqual(self) -> str: ...
    def setEntryIdEqual(self, newEntryIdEqual: str) -> None: ...
    def getEntryIdIn(self) -> str: ...
    def setEntryIdIn(self, newEntryIdIn: str) -> None: ...

class KalturaAnswerCuePointBaseFilter(KalturaCuePointFilter):
    parentIdEqual: str
    parentIdIn: str
    quizUserEntryIdEqual: str
    quizUserEntryIdIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            cuePointTypeEqual: KalturaCuePointType = NotImplemented,
            cuePointTypeIn: str = NotImplemented,
            statusEqual: KalturaCuePointStatus = NotImplemented,
            statusIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            triggeredAtGreaterThanOrEqual: int = NotImplemented,
            triggeredAtLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            startTimeGreaterThanOrEqual: int = NotImplemented,
            startTimeLessThanOrEqual: int = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            partnerSortValueEqual: int = NotImplemented,
            partnerSortValueIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            forceStopEqual: KalturaNullableBoolean = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            freeText: str = NotImplemented,
            userIdEqualCurrent: KalturaNullableBoolean = NotImplemented,
            userIdCurrent: KalturaNullableBoolean = NotImplemented,
            parentIdEqual: str = NotImplemented,
            parentIdIn: str = NotImplemented,
            quizUserEntryIdEqual: str = NotImplemented,
            quizUserEntryIdIn: str = NotImplemented): ...

    def getParentIdEqual(self) -> str: ...
    def setParentIdEqual(self, newParentIdEqual: str) -> None: ...
    def getParentIdIn(self) -> str: ...
    def setParentIdIn(self, newParentIdIn: str) -> None: ...
    def getQuizUserEntryIdEqual(self) -> str: ...
    def setQuizUserEntryIdEqual(self, newQuizUserEntryIdEqual: str) -> None: ...
    def getQuizUserEntryIdIn(self) -> str: ...
    def setQuizUserEntryIdIn(self, newQuizUserEntryIdIn: str) -> None: ...

class KalturaQuestionCuePointBaseFilter(KalturaCuePointFilter):
    questionLike: str
    questionMultiLikeOr: str
    questionMultiLikeAnd: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            cuePointTypeEqual: KalturaCuePointType = NotImplemented,
            cuePointTypeIn: str = NotImplemented,
            statusEqual: KalturaCuePointStatus = NotImplemented,
            statusIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            triggeredAtGreaterThanOrEqual: int = NotImplemented,
            triggeredAtLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            startTimeGreaterThanOrEqual: int = NotImplemented,
            startTimeLessThanOrEqual: int = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            partnerSortValueEqual: int = NotImplemented,
            partnerSortValueIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            forceStopEqual: KalturaNullableBoolean = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            freeText: str = NotImplemented,
            userIdEqualCurrent: KalturaNullableBoolean = NotImplemented,
            userIdCurrent: KalturaNullableBoolean = NotImplemented,
            questionLike: str = NotImplemented,
            questionMultiLikeOr: str = NotImplemented,
            questionMultiLikeAnd: str = NotImplemented): ...

    def getQuestionLike(self) -> str: ...
    def setQuestionLike(self, newQuestionLike: str) -> None: ...
    def getQuestionMultiLikeOr(self) -> str: ...
    def setQuestionMultiLikeOr(self, newQuestionMultiLikeOr: str) -> None: ...
    def getQuestionMultiLikeAnd(self) -> str: ...
    def setQuestionMultiLikeAnd(self, newQuestionMultiLikeAnd: str) -> None: ...

class KalturaAnswerCuePointFilter(KalturaAnswerCuePointBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            cuePointTypeEqual: KalturaCuePointType = NotImplemented,
            cuePointTypeIn: str = NotImplemented,
            statusEqual: KalturaCuePointStatus = NotImplemented,
            statusIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            triggeredAtGreaterThanOrEqual: int = NotImplemented,
            triggeredAtLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            startTimeGreaterThanOrEqual: int = NotImplemented,
            startTimeLessThanOrEqual: int = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            partnerSortValueEqual: int = NotImplemented,
            partnerSortValueIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            forceStopEqual: KalturaNullableBoolean = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            freeText: str = NotImplemented,
            userIdEqualCurrent: KalturaNullableBoolean = NotImplemented,
            userIdCurrent: KalturaNullableBoolean = NotImplemented,
            parentIdEqual: str = NotImplemented,
            parentIdIn: str = NotImplemented,
            quizUserEntryIdEqual: str = NotImplemented,
            quizUserEntryIdIn: str = NotImplemented): ...
        pass

class KalturaQuestionCuePointFilter(KalturaQuestionCuePointBaseFilter):
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: str = NotImplemented,
            idIn: str = NotImplemented,
            cuePointTypeEqual: KalturaCuePointType = NotImplemented,
            cuePointTypeIn: str = NotImplemented,
            statusEqual: KalturaCuePointStatus = NotImplemented,
            statusIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            triggeredAtGreaterThanOrEqual: int = NotImplemented,
            triggeredAtLessThanOrEqual: int = NotImplemented,
            tagsLike: str = NotImplemented,
            tagsMultiLikeOr: str = NotImplemented,
            tagsMultiLikeAnd: str = NotImplemented,
            startTimeGreaterThanOrEqual: int = NotImplemented,
            startTimeLessThanOrEqual: int = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            partnerSortValueEqual: int = NotImplemented,
            partnerSortValueIn: str = NotImplemented,
            partnerSortValueGreaterThanOrEqual: int = NotImplemented,
            partnerSortValueLessThanOrEqual: int = NotImplemented,
            forceStopEqual: KalturaNullableBoolean = NotImplemented,
            systemNameEqual: str = NotImplemented,
            systemNameIn: str = NotImplemented,
            freeText: str = NotImplemented,
            userIdEqualCurrent: KalturaNullableBoolean = NotImplemented,
            userIdCurrent: KalturaNullableBoolean = NotImplemented,
            questionLike: str = NotImplemented,
            questionMultiLikeOr: str = NotImplemented,
            questionMultiLikeAnd: str = NotImplemented): ...
        pass

class KalturaQuizUserEntryFilter(KalturaQuizUserEntryBaseFilter):
    extendedStatusEqual: KalturaUserEntryExtendedStatus
    extendedStatusIn: str
    extendedStatusNotIn: str
    def __init__(self,
            orderBy: str = NotImplemented,
            advancedSearch: KalturaSearchItem = NotImplemented,
            idEqual: int = NotImplemented,
            idIn: str = NotImplemented,
            idNotIn: str = NotImplemented,
            entryIdEqual: str = NotImplemented,
            entryIdIn: str = NotImplemented,
            entryIdNotIn: str = NotImplemented,
            userIdEqual: str = NotImplemented,
            userIdIn: str = NotImplemented,
            userIdNotIn: str = NotImplemented,
            statusEqual: KalturaUserEntryStatus = NotImplemented,
            createdAtLessThanOrEqual: int = NotImplemented,
            createdAtGreaterThanOrEqual: int = NotImplemented,
            updatedAtLessThanOrEqual: int = NotImplemented,
            updatedAtGreaterThanOrEqual: int = NotImplemented,
            typeEqual: KalturaUserEntryType = NotImplemented,
            userIdEqualCurrent: KalturaNullableBoolean = NotImplemented,
            isAnonymous: KalturaNullableBoolean = NotImplemented,
            privacyContextEqual: str = NotImplemented,
            privacyContextIn: str = NotImplemented,
            partnerId: int = NotImplemented,
            extendedStatusEqual: KalturaUserEntryExtendedStatus = NotImplemented,
            extendedStatusIn: str = NotImplemented,
            extendedStatusNotIn: str = NotImplemented): ...

    def getExtendedStatusEqual(self) -> KalturaUserEntryExtendedStatus: ...
    def setExtendedStatusEqual(self, newExtendedStatusEqual: KalturaUserEntryExtendedStatus) -> None: ...
    def getExtendedStatusIn(self) -> str: ...
    def setExtendedStatusIn(self, newExtendedStatusIn: str) -> None: ...
    def getExtendedStatusNotIn(self) -> str: ...
    def setExtendedStatusNotIn(self, newExtendedStatusNotIn: str) -> None: ...

class KalturaQuizService(KalturaServiceBase):
    def add(self, entryId: str, quiz: KalturaQuiz) -> KalturaQuiz: ...
    def get(self, entryId: str) -> KalturaQuiz: ...
    def getUrl(self, entryId: str, quizOutputType: int) -> str: ...
    def list(self, filter: KalturaQuizFilter = NotImplemented, pager: KalturaFilterPager = NotImplemented) -> KalturaQuizListResponse: ...
    def serve(self, entryId: str, quizOutputType: int) -> IO[Any]: ...
    def update(self, entryId: str, quiz: KalturaQuiz) -> KalturaQuiz: ...

class KalturaQuizClientPluginServicesProxy:
    quiz: KalturaQuizService