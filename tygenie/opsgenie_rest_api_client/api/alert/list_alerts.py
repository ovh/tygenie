from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_alerts_order import ListAlertsOrder
from ...models.list_alerts_response import ListAlertsResponse
from ...models.list_alerts_search_identifier_type import ListAlertsSearchIdentifierType
from ...models.list_alerts_sort import ListAlertsSort
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: Union[Unset, str] = UNSET,
    search_identifier: Union[Unset, str] = UNSET,
    search_identifier_type: Union[
        Unset, ListAlertsSearchIdentifierType
    ] = ListAlertsSearchIdentifierType.ID,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListAlertsSort] = ListAlertsSort.CREATEDAT,
    order: Union[Unset, ListAlertsOrder] = ListAlertsOrder.DESC,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["query"] = query

    params["searchIdentifier"] = search_identifier

    json_search_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(search_identifier_type, Unset):
        json_search_identifier_type = search_identifier_type

    params["searchIdentifierType"] = json_search_identifier_type

    params["offset"] = offset

    params["limit"] = limit

    json_sort: Union[Unset, str] = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    json_order: Union[Unset, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order

    params["order"] = json_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/alerts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListAlertsResponse]]:
    if response.status_code == 200:
        response_200 = ListAlertsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListAlertsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    search_identifier: Union[Unset, str] = UNSET,
    search_identifier_type: Union[
        Unset, ListAlertsSearchIdentifierType
    ] = ListAlertsSearchIdentifierType.ID,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListAlertsSort] = ListAlertsSort.CREATEDAT,
    order: Union[Unset, ListAlertsOrder] = ListAlertsOrder.DESC,
) -> Response[Union[Any, ListAlertsResponse]]:
    """List Alerts

     Returns list of alerts

    Args:
        query (Union[Unset, str]):
        search_identifier (Union[Unset, str]):
        search_identifier_type (Union[Unset, ListAlertsSearchIdentifierType]):  Default:
            ListAlertsSearchIdentifierType.ID.
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort (Union[Unset, ListAlertsSort]):  Default: ListAlertsSort.CREATEDAT.
        order (Union[Unset, ListAlertsOrder]):  Default: ListAlertsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListAlertsResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        search_identifier=search_identifier,
        search_identifier_type=search_identifier_type,
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
    query: Union[Unset, str] = UNSET,
    search_identifier: Union[Unset, str] = UNSET,
    search_identifier_type: Union[
        Unset, ListAlertsSearchIdentifierType
    ] = ListAlertsSearchIdentifierType.ID,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListAlertsSort] = ListAlertsSort.CREATEDAT,
    order: Union[Unset, ListAlertsOrder] = ListAlertsOrder.DESC,
) -> Optional[Union[Any, ListAlertsResponse]]:
    """List Alerts

     Returns list of alerts

    Args:
        query (Union[Unset, str]):
        search_identifier (Union[Unset, str]):
        search_identifier_type (Union[Unset, ListAlertsSearchIdentifierType]):  Default:
            ListAlertsSearchIdentifierType.ID.
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort (Union[Unset, ListAlertsSort]):  Default: ListAlertsSort.CREATEDAT.
        order (Union[Unset, ListAlertsOrder]):  Default: ListAlertsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListAlertsResponse]
    """

    return sync_detailed(
        client=client,
        query=query,
        search_identifier=search_identifier,
        search_identifier_type=search_identifier_type,
        offset=offset,
        limit=limit,
        sort=sort,
        order=order,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: Union[Unset, str] = UNSET,
    search_identifier: Union[Unset, str] = UNSET,
    search_identifier_type: Union[
        Unset, ListAlertsSearchIdentifierType
    ] = ListAlertsSearchIdentifierType.ID,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListAlertsSort] = ListAlertsSort.CREATEDAT,
    order: Union[Unset, ListAlertsOrder] = ListAlertsOrder.DESC,
) -> Response[Union[Any, ListAlertsResponse]]:
    """List Alerts

     Returns list of alerts

    Args:
        query (Union[Unset, str]):
        search_identifier (Union[Unset, str]):
        search_identifier_type (Union[Unset, ListAlertsSearchIdentifierType]):  Default:
            ListAlertsSearchIdentifierType.ID.
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort (Union[Unset, ListAlertsSort]):  Default: ListAlertsSort.CREATEDAT.
        order (Union[Unset, ListAlertsOrder]):  Default: ListAlertsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListAlertsResponse]]
    """

    kwargs = _get_kwargs(
        query=query,
        search_identifier=search_identifier,
        search_identifier_type=search_identifier_type,
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
    query: Union[Unset, str] = UNSET,
    search_identifier: Union[Unset, str] = UNSET,
    search_identifier_type: Union[
        Unset, ListAlertsSearchIdentifierType
    ] = ListAlertsSearchIdentifierType.ID,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    sort: Union[Unset, ListAlertsSort] = ListAlertsSort.CREATEDAT,
    order: Union[Unset, ListAlertsOrder] = ListAlertsOrder.DESC,
) -> Optional[Union[Any, ListAlertsResponse]]:
    """List Alerts

     Returns list of alerts

    Args:
        query (Union[Unset, str]):
        search_identifier (Union[Unset, str]):
        search_identifier_type (Union[Unset, ListAlertsSearchIdentifierType]):  Default:
            ListAlertsSearchIdentifierType.ID.
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort (Union[Unset, ListAlertsSort]):  Default: ListAlertsSort.CREATEDAT.
        order (Union[Unset, ListAlertsOrder]):  Default: ListAlertsOrder.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListAlertsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            search_identifier=search_identifier,
            search_identifier_type=search_identifier_type,
            offset=offset,
            limit=limit,
            sort=sort,
            order=order,
        )
    ).parsed
