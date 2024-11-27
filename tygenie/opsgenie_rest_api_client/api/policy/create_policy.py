from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_policy_response import CreatePolicyResponse
from ...models.policy import Policy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: Policy,
    team_id: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["teamId"] = team_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v2/policies",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CreatePolicyResponse]]:
    if response.status_code == 201:
        response_201 = CreatePolicyResponse.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, CreatePolicyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Policy,
    team_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreatePolicyResponse]]:
    """Create Policy

     Creates a new policy

    Args:
        team_id (Union[Unset, str]):
        body (Policy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreatePolicyResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        team_id=team_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Policy,
    team_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreatePolicyResponse]]:
    """Create Policy

     Creates a new policy

    Args:
        team_id (Union[Unset, str]):
        body (Policy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreatePolicyResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        team_id=team_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Policy,
    team_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CreatePolicyResponse]]:
    """Create Policy

     Creates a new policy

    Args:
        team_id (Union[Unset, str]):
        body (Policy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CreatePolicyResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        team_id=team_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Policy,
    team_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CreatePolicyResponse]]:
    """Create Policy

     Creates a new policy

    Args:
        team_id (Union[Unset, str]):
        body (Policy):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CreatePolicyResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            team_id=team_id,
        )
    ).parsed
