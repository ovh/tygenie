from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_services_order import ListServicesOrder
from ...models.list_services_response import ListServicesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    sort_field: Union[Unset, str] = UNSET,
    order: Union[Unset, ListServicesOrder] = ListServicesOrder.ASC,
    query: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["sortField"] = sort_field

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params["query"] = query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/services",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListServicesResponse]]:
    if response.status_code == 200:
        response_200 = ListServicesResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListServicesResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    sort_field: Union[Unset, str] = UNSET,
    order: Union[Unset, ListServicesOrder] = ListServicesOrder.ASC,
    query: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListServicesResponse]]:
    """List services

     Return list of services

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        sort_field (Union[Unset, str]):
        order (Union[Unset, ListServicesOrder]):  Default: ListServicesOrder.ASC.
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListServicesResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_field=sort_field,
        order=order,
        query=query,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    sort_field: Union[Unset, str] = UNSET,
    order: Union[Unset, ListServicesOrder] = ListServicesOrder.ASC,
    query: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListServicesResponse]]:
    """List services

     Return list of services

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        sort_field (Union[Unset, str]):
        order (Union[Unset, ListServicesOrder]):  Default: ListServicesOrder.ASC.
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListServicesResponse]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        sort_field=sort_field,
        order=order,
        query=query,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    sort_field: Union[Unset, str] = UNSET,
    order: Union[Unset, ListServicesOrder] = ListServicesOrder.ASC,
    query: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListServicesResponse]]:
    """List services

     Return list of services

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        sort_field (Union[Unset, str]):
        order (Union[Unset, ListServicesOrder]):  Default: ListServicesOrder.ASC.
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListServicesResponse]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        sort_field=sort_field,
        order=order,
        query=query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 100,
    offset: Union[Unset, int] = 0,
    sort_field: Union[Unset, str] = UNSET,
    order: Union[Unset, ListServicesOrder] = ListServicesOrder.ASC,
    query: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListServicesResponse]]:
    """List services

     Return list of services

    Args:
        limit (Union[Unset, int]):  Default: 100.
        offset (Union[Unset, int]):  Default: 0.
        sort_field (Union[Unset, str]):
        order (Union[Unset, ListServicesOrder]):  Default: ListServicesOrder.ASC.
        query (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListServicesResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            sort_field=sort_field,
            order=order,
            query=query,
        )
    ).parsed
