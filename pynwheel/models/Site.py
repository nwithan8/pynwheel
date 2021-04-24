# generated by datamodel-codegen:
#   filename:  model.json
#   timestamp: 2021-04-24T01:30:24+00:00

from __future__ import annotations

from uuid import UUID

from pydantic import AnyUrl, BaseModel, Field


class Site(BaseModel):
    id: UUID = Field(..., description='UUID of the link token.', title='Id')
    token_id: UUID = Field(
        ...,
        description='UUID of the link token. Identical to the id.',
        title='Token Id',
    )
    url: AnyUrl = Field(
        ...,
        description='URL of the generated site you can send your users.',
        title='Url',
    )
    expires: int = Field(
        ...,
        description='Token expiration timestamp in Unix time in seconds.',
        title='Expires',
    )