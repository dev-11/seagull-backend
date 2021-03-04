import enum
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List

from dataclasses_json import config, dataclass_json
from marshmallow import fields


class TideType(int, enum.Enum):
    Undefined = 0
    High = 1
    Low = 2
    Raising = 3
    Falling = 4


@dataclass_json
@dataclass
class TideEvent:
    type: TideType
    time: datetime = field(
        metadata=config(
            encoder=datetime.isoformat, decoder=datetime.fromisoformat, mm_field=fields.DateTime(format='iso')
        )
    )
    height: float


@dataclass
class TideEvents:
    date: date
    events: List[TideEvent]


tide_events = TideEvents(
    date(2021, 3, 2),
    [
        TideEvent(TideType.Low, datetime(2021, 3, 2, hour=0, minute=13, second=59), 0.04281385004939631,),
        TideEvent(TideType.High, datetime(2021, 3, 2, hour=4, minute=26, second=20), 5.832805198778108,),
        TideEvent(TideType.Low, datetime(2021, 3, 2, hour=12, minute=41, second=19), -0.19908685388005984,),
        TideEvent(TideType.High, datetime(2021, 3, 2, hour=16, minute=48, second=2), 5.838791925941982,),
    ],
)
