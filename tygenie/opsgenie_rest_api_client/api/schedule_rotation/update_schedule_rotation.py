from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.success_response import SuccessResponse
from ...models.update_schedule_rotation_payload import UpdateScheduleRotationPayload
from ...models.update_schedule_rotation_schedule_identifier_type import UpdateScheduleRotationScheduleIdentifierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    id: str,
    *,
    body: UpdateScheduleRotationPayload,
    schedule_identifier_type: Union[
        Unset, UpdateScheduleRotationScheduleIdentifierType
    ] = UpdateScheduleRotationScheduleIdentifierType.ID,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_schedule_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(schedule_identifier_type, Unset):
        json_schedule_identifier_type = schedule_identifier_type.value

    params["scheduleIdentifierType"] = json_schedule_identifier_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/v2/schedules/{identifier}/rotations/{id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SuccessResponse]]:
    if response.status_code == 200:
        response_200 = SuccessResponse.from_dict(response.json())

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
) -> Response[Union[Any, SuccessResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateScheduleRotationPayload,
    schedule_identifier_type: Union[
        Unset, UpdateScheduleRotationScheduleIdentifierType
    ] = UpdateScheduleRotationScheduleIdentifierType.ID,
) -> Response[Union[Any, SuccessResponse]]:
    """Update Schedule Rotation (Partial)

     Update schedule rotation with given id

    Args:
        identifier (str):
        id (str):
        schedule_identifier_type (Union[Unset, UpdateScheduleRotationScheduleIdentifierType]):
            Default: UpdateScheduleRotationScheduleIdentifierType.ID.
        body (UpdateScheduleRotationPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SuccessResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        id=id,
        body=body,
        schedule_identifier_type=schedule_identifier_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateScheduleRotationPayload,
    schedule_identifier_type: Union[
        Unset, UpdateScheduleRotationScheduleIdentifierType
    ] = UpdateScheduleRotationScheduleIdentifierType.ID,
) -> Optional[Union[Any, SuccessResponse]]:
    """Update Schedule Rotation (Partial)

     Update schedule rotation with given id

    Args:
        identifier (str):
        id (str):
        schedule_identifier_type (Union[Unset, UpdateScheduleRotationScheduleIdentifierType]):
            Default: UpdateScheduleRotationScheduleIdentifierType.ID.
        body (UpdateScheduleRotationPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SuccessResponse]
    """

    return sync_detailed(
        identifier=identifier,
        id=id,
        client=client,
        body=body,
        schedule_identifier_type=schedule_identifier_type,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateScheduleRotationPayload,
    schedule_identifier_type: Union[
        Unset, UpdateScheduleRotationScheduleIdentifierType
    ] = UpdateScheduleRotationScheduleIdentifierType.ID,
) -> Response[Union[Any, SuccessResponse]]:
    """Update Schedule Rotation (Partial)

     Update schedule rotation with given id

    Args:
        identifier (str):
        id (str):
        schedule_identifier_type (Union[Unset, UpdateScheduleRotationScheduleIdentifierType]):
            Default: UpdateScheduleRotationScheduleIdentifierType.ID.
        body (UpdateScheduleRotationPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SuccessResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        id=id,
        body=body,
        schedule_identifier_type=schedule_identifier_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateScheduleRotationPayload,
    schedule_identifier_type: Union[
        Unset, UpdateScheduleRotationScheduleIdentifierType
    ] = UpdateScheduleRotationScheduleIdentifierType.ID,
) -> Optional[Union[Any, SuccessResponse]]:
    """Update Schedule Rotation (Partial)

     Update schedule rotation with given id

    Args:
        identifier (str):
        id (str):
        schedule_identifier_type (Union[Unset, UpdateScheduleRotationScheduleIdentifierType]):
            Default: UpdateScheduleRotationScheduleIdentifierType.ID.
        body (UpdateScheduleRotationPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SuccessResponse]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            id=id,
            client=client,
            body=body,
            schedule_identifier_type=schedule_identifier_type,
        )
    ).parsed
