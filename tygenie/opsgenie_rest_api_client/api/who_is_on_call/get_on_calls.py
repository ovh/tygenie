import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_on_call_response import GetOnCallResponse
from ...models.get_on_calls_schedule_identifier_type import (
    GetOnCallsScheduleIdentifierType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    schedule_identifier_type: Union[
        Unset, GetOnCallsScheduleIdentifierType
    ] = GetOnCallsScheduleIdentifierType.ID,
    flat: Union[Unset, bool] = UNSET,
    date: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_schedule_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(schedule_identifier_type, Unset):
        json_schedule_identifier_type = schedule_identifier_type

    params["scheduleIdentifierType"] = json_schedule_identifier_type

    params["flat"] = flat

    json_date: Union[Unset, str] = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/schedules/{identifier}/on-calls",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetOnCallResponse]]:
    if response.status_code == 200:
        response_200 = GetOnCallResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 402:
        response_402 = cast(Any, None)
        return response_402
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetOnCallResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    schedule_identifier_type: Union[
        Unset, GetOnCallsScheduleIdentifierType
    ] = GetOnCallsScheduleIdentifierType.ID,
    flat: Union[Unset, bool] = UNSET,
    date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, GetOnCallResponse]]:
    """Get On Calls

     Gets current on-call participants of a specific schedule

    Args:
        identifier (str):
        schedule_identifier_type (Union[Unset, GetOnCallsScheduleIdentifierType]):  Default:
            GetOnCallsScheduleIdentifierType.ID.
        flat (Union[Unset, bool]):
        date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOnCallResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        schedule_identifier_type=schedule_identifier_type,
        flat=flat,
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    schedule_identifier_type: Union[
        Unset, GetOnCallsScheduleIdentifierType
    ] = GetOnCallsScheduleIdentifierType.ID,
    flat: Union[Unset, bool] = UNSET,
    date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, GetOnCallResponse]]:
    """Get On Calls

     Gets current on-call participants of a specific schedule

    Args:
        identifier (str):
        schedule_identifier_type (Union[Unset, GetOnCallsScheduleIdentifierType]):  Default:
            GetOnCallsScheduleIdentifierType.ID.
        flat (Union[Unset, bool]):
        date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOnCallResponse]
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        schedule_identifier_type=schedule_identifier_type,
        flat=flat,
        date=date,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    schedule_identifier_type: Union[
        Unset, GetOnCallsScheduleIdentifierType
    ] = GetOnCallsScheduleIdentifierType.ID,
    flat: Union[Unset, bool] = UNSET,
    date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, GetOnCallResponse]]:
    """Get On Calls

     Gets current on-call participants of a specific schedule

    Args:
        identifier (str):
        schedule_identifier_type (Union[Unset, GetOnCallsScheduleIdentifierType]):  Default:
            GetOnCallsScheduleIdentifierType.ID.
        flat (Union[Unset, bool]):
        date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetOnCallResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        schedule_identifier_type=schedule_identifier_type,
        flat=flat,
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    schedule_identifier_type: Union[
        Unset, GetOnCallsScheduleIdentifierType
    ] = GetOnCallsScheduleIdentifierType.ID,
    flat: Union[Unset, bool] = UNSET,
    date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, GetOnCallResponse]]:
    """Get On Calls

     Gets current on-call participants of a specific schedule

    Args:
        identifier (str):
        schedule_identifier_type (Union[Unset, GetOnCallsScheduleIdentifierType]):  Default:
            GetOnCallsScheduleIdentifierType.ID.
        flat (Union[Unset, bool]):
        date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetOnCallResponse]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            schedule_identifier_type=schedule_identifier_type,
            flat=flat,
            date=date,
        )
    ).parsed
