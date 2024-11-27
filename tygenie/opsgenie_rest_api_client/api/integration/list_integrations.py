from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_integrations_response import ListIntegrationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type: Union[Unset, str] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["type"] = type

    params["teamId"] = team_id

    params["teamName"] = team_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v2/integrations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListIntegrationsResponse]]:
    if response.status_code == 200:
        response_200 = ListIntegrationsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListIntegrationsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, str] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListIntegrationsResponse]]:
    """List Integrations

     Returns list of integrations with given parameters

    Args:
        type (Union[Unset, str]):
        team_id (Union[Unset, str]):
        team_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListIntegrationsResponse]]
    """

    kwargs = _get_kwargs(
        type=type,
        team_id=team_id,
        team_name=team_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, str] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListIntegrationsResponse]]:
    """List Integrations

     Returns list of integrations with given parameters

    Args:
        type (Union[Unset, str]):
        team_id (Union[Unset, str]):
        team_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListIntegrationsResponse]
    """

    return sync_detailed(
        client=client,
        type=type,
        team_id=team_id,
        team_name=team_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, str] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ListIntegrationsResponse]]:
    """List Integrations

     Returns list of integrations with given parameters

    Args:
        type (Union[Unset, str]):
        team_id (Union[Unset, str]):
        team_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListIntegrationsResponse]]
    """

    kwargs = _get_kwargs(
        type=type,
        team_id=team_id,
        team_name=team_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type: Union[Unset, str] = UNSET,
    team_id: Union[Unset, str] = UNSET,
    team_name: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ListIntegrationsResponse]]:
    """List Integrations

     Returns list of integrations with given parameters

    Args:
        type (Union[Unset, str]):
        team_id (Union[Unset, str]):
        team_name (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListIntegrationsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            type=type,
            team_id=team_id,
            team_name=team_name,
        )
    ).parsed
