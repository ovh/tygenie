from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_alert_notes_response import ListAlertNotesResponse
from ...models.list_notes_direction import ListNotesDirection
from ...models.list_notes_identifier_type import ListNotesIdentifierType
from ...models.list_notes_order import ListNotesOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    identifier_type: Union[Unset, ListNotesIdentifierType] = ListNotesIdentifierType.ID,
    offset: Union[Unset, str] = UNSET,
    direction: Union[Unset, ListNotesDirection] = ListNotesDirection.NEXT,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ListNotesOrder] = ListNotesOrder.DESC,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(identifier_type, Unset):
        json_identifier_type = identifier_type

    params["identifierType"] = json_identifier_type

    params["offset"] = offset

    json_direction: Union[Unset, str] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction

    params["direction"] = json_direction

    params["limit"] = limit

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/alerts/{identifier}/notes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListAlertNotesResponse]]:
    if response.status_code == 200:
        response_200 = ListAlertNotesResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListAlertNotesResponse]]:
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
    identifier_type: Union[Unset, ListNotesIdentifierType] = ListNotesIdentifierType.ID,
    offset: Union[Unset, str] = UNSET,
    direction: Union[Unset, ListNotesDirection] = ListNotesDirection.NEXT,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ListNotesOrder] = ListNotesOrder.DESC,
) -> Response[Union[Any, ListAlertNotesResponse]]:
    """List Alert Notes

     List alert notes for the given alert identifier

    Args:
        identifier (str):
        identifier_type (Union[Unset, ListNotesIdentifierType]):  Default:
            ListNotesIdentifierType.ID.
        offset (Union[Unset, str]):
        direction (Union[Unset, ListNotesDirection]):  Default: ListNotesDirection.NEXT.
        limit (Union[Unset, int]):
        order (Union[Unset, ListNotesOrder]):  Default: ListNotesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListAlertNotesResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        identifier_type=identifier_type,
        offset=offset,
        direction=direction,
        limit=limit,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    identifier_type: Union[Unset, ListNotesIdentifierType] = ListNotesIdentifierType.ID,
    offset: Union[Unset, str] = UNSET,
    direction: Union[Unset, ListNotesDirection] = ListNotesDirection.NEXT,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ListNotesOrder] = ListNotesOrder.DESC,
) -> Optional[Union[Any, ListAlertNotesResponse]]:
    """List Alert Notes

     List alert notes for the given alert identifier

    Args:
        identifier (str):
        identifier_type (Union[Unset, ListNotesIdentifierType]):  Default:
            ListNotesIdentifierType.ID.
        offset (Union[Unset, str]):
        direction (Union[Unset, ListNotesDirection]):  Default: ListNotesDirection.NEXT.
        limit (Union[Unset, int]):
        order (Union[Unset, ListNotesOrder]):  Default: ListNotesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListAlertNotesResponse]
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        identifier_type=identifier_type,
        offset=offset,
        direction=direction,
        limit=limit,
        order=order,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    identifier_type: Union[Unset, ListNotesIdentifierType] = ListNotesIdentifierType.ID,
    offset: Union[Unset, str] = UNSET,
    direction: Union[Unset, ListNotesDirection] = ListNotesDirection.NEXT,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ListNotesOrder] = ListNotesOrder.DESC,
) -> Response[Union[Any, ListAlertNotesResponse]]:
    """List Alert Notes

     List alert notes for the given alert identifier

    Args:
        identifier (str):
        identifier_type (Union[Unset, ListNotesIdentifierType]):  Default:
            ListNotesIdentifierType.ID.
        offset (Union[Unset, str]):
        direction (Union[Unset, ListNotesDirection]):  Default: ListNotesDirection.NEXT.
        limit (Union[Unset, int]):
        order (Union[Unset, ListNotesOrder]):  Default: ListNotesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListAlertNotesResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        identifier_type=identifier_type,
        offset=offset,
        direction=direction,
        limit=limit,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    identifier_type: Union[Unset, ListNotesIdentifierType] = ListNotesIdentifierType.ID,
    offset: Union[Unset, str] = UNSET,
    direction: Union[Unset, ListNotesDirection] = ListNotesDirection.NEXT,
    limit: Union[Unset, int] = UNSET,
    order: Union[Unset, ListNotesOrder] = ListNotesOrder.DESC,
) -> Optional[Union[Any, ListAlertNotesResponse]]:
    """List Alert Notes

     List alert notes for the given alert identifier

    Args:
        identifier (str):
        identifier_type (Union[Unset, ListNotesIdentifierType]):  Default:
            ListNotesIdentifierType.ID.
        offset (Union[Unset, str]):
        direction (Union[Unset, ListNotesDirection]):  Default: ListNotesDirection.NEXT.
        limit (Union[Unset, int]):
        order (Union[Unset, ListNotesOrder]):  Default: ListNotesOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListAlertNotesResponse]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            identifier_type=identifier_type,
            offset=offset,
            direction=direction,
            limit=limit,
            order=order,
        )
    ).parsed
