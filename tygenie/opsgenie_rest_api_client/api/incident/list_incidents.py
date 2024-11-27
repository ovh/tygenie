from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_incidents_order import ListIncidentsOrder
from ...models.list_incidents_response import ListIncidentsResponse
from ...models.list_incidents_sort import ListIncidentsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = ListIncidentsSort.CREATEDAT,
    order: Union[Unset, ListIncidentsOrder] = ListIncidentsOrder.DESC,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query"] = query

    params["offset"] = offset

    params["limit"] = limit

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/incidents/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListIncidentsResponse]]:
    if response.status_code == 200:
        response_200 = ListIncidentsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListIncidentsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = ListIncidentsSort.CREATEDAT,
    order: Union[Unset, ListIncidentsOrder] = ListIncidentsOrder.DESC,
) -> Response[Union[Any, ListIncidentsResponse]]:
    """List incidents

     Return list of incidents

    Args:
        query (str):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort (Union[Unset, ListIncidentsSort]):  Default: ListIncidentsSort.CREATEDAT.
        order (Union[Unset, ListIncidentsOrder]):  Default: ListIncidentsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListIncidentsResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = ListIncidentsSort.CREATEDAT,
    order: Union[Unset, ListIncidentsOrder] = ListIncidentsOrder.DESC,
) -> Optional[Union[Any, ListIncidentsResponse]]:
    """List incidents

     Return list of incidents

    Args:
        query (str):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort (Union[Unset, ListIncidentsSort]):  Default: ListIncidentsSort.CREATEDAT.
        order (Union[Unset, ListIncidentsOrder]):  Default: ListIncidentsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListIncidentsResponse]
    """

    return sync_detailed(
        client=client,
        query=query,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = ListIncidentsSort.CREATEDAT,
    order: Union[Unset, ListIncidentsOrder] = ListIncidentsOrder.DESC,
) -> Response[Union[Any, ListIncidentsResponse]]:
    """List incidents

     Return list of incidents

    Args:
        query (str):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort (Union[Unset, ListIncidentsSort]):  Default: ListIncidentsSort.CREATEDAT.
        order (Union[Unset, ListIncidentsOrder]):  Default: ListIncidentsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListIncidentsResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListIncidentsSort] = ListIncidentsSort.CREATEDAT,
    order: Union[Unset, ListIncidentsOrder] = ListIncidentsOrder.DESC,
) -> Optional[Union[Any, ListIncidentsResponse]]:
    """List incidents

     Return list of incidents

    Args:
        query (str):
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort (Union[Unset, ListIncidentsSort]):  Default: ListIncidentsSort.CREATEDAT.
        order (Union[Unset, ListIncidentsOrder]):  Default: ListIncidentsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListIncidentsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            offset=offset,
            limit=limit,
            sort=sort,
            order=order,
        )
    ).parsed
