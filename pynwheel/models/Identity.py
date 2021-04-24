# generated by datamodel-codegen:
#   filename:  model.json
#   timestamp: 2021-04-24T01:32:00+00:00

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Country(Enum):
    US = 'US'


class Address(BaseModel):
    raw: str = Field(..., description='The raw address.', title='Raw')
    line1: Optional[str] = Field(
        None, description='The first line of the address.', title='Line1'
    )
    line2: Optional[str] = Field(
        None, description='The second line of the address.', title='Line2'
    )
    city: Optional[str] = Field(
        None, description='The city of the address.', title='City'
    )
    state: Optional[str] = Field(
        None, description='The state of the address.', title='State'
    )
    postal_code: Optional[str] = Field(
        None, description='The postal code of the address.', title='Postal Code'
    )
    country: Optional[Country] = Field(
        None, description='The country of the address.', title='Country'
    )


class Type(Enum):
    home = 'home'
    work = 'work'
    mobile = 'mobile'


class PhoneNumber(BaseModel):
    value: str = Field(
        ..., description='The E.164 formatted phone number.', title='Value'
    )
    type: Optional[Type] = Field(
        None, description='home, mobile, work, etc.', title='Type'
    )


class Identity(BaseModel):
    id: UUID = Field(..., description='Unique identifier for the object.', title='Id')
    created_at: datetime = Field(
        ..., description='ISO 8601 timestamp of created time.', title='Created At'
    )
    account_id: UUID = Field(
        ..., description='Unique identifier for the object.', title='Account Id'
    )
    full_name: str = Field(
        ..., description='The full name of the employee.', title='Full Name'
    )
    emails: Optional[List[str]] = Field(
        None, description='The emails associated with the employee.', title='Emails'
    )
    date_of_birth: Optional[date] = Field(
        None, description='The date the employee was born.', title='Date Of Birth'
    )
    last_four_ssn: Optional[str] = Field(
        None,
        description="The last four digits of the employee's social security number (SSN).",
        title='Last Four Ssn',
    )
    address: Optional[Address] = Field(
        None, description='The address of the employee.', title='Address'
    )
    phone_numbers: Optional[List[PhoneNumber]] = Field(
        None, description='The phone numbers of the employee.', title='Phone Numbers'
    )