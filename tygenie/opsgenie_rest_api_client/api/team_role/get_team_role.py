from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_team_role_identifier_type import GetTeamRoleIdentifierType
from ...models.get_team_role_response import GetTeamRoleResponse
from ...models.get_team_role_team_identifier_type import GetTeamRoleTeamIdentifierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    team_role_identifier: str,
    *,
    team_identifier_type: Union[Unset, GetTeamRoleTeamIdentifierType] = GetTeamRoleTeamIdentifierType.ID,
    identifier_type: Union[Unset, GetTeamRoleIdentifierType] = GetTeamRoleIdentifierType.ID,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_team_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(team_identifier_type, Unset):
        json_team_identifier_type = team_identifier_type.value

    params["teamIdentifierType"] = json_team_identifier_type

    json_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(identifier_type, Unset):
        json_identifier_type = identifier_type.value

    params["identifierType"] = json_identifier_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/teams/{identifier}/roles/{team_role_identifier}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetTeamRoleResponse]]:
    if response.status_code == 200:
        response_200 = GetTeamRoleResponse.from_dict(response.json())

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
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetTeamRoleResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    team_role_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    team_identifier_type: Union[Unset, GetTeamRoleTeamIdentifierType] = GetTeamRoleTeamIdentifierType.ID,
    identifier_type: Union[Unset, GetTeamRoleIdentifierType] = GetTeamRoleIdentifierType.ID,
) -> Response[Union[Any, GetTeamRoleResponse]]:
    """Get Team Role

     Returns team role with given 'id' or 'name'

    Args:
        identifier (str):
        team_role_identifier (str):
        team_identifier_type (Union[Unset, GetTeamRoleTeamIdentifierType]):  Default:
            GetTeamRoleTeamIdentifierType.ID.
        identifier_type (Union[Unset, GetTeamRoleIdentifierType]):  Default:
            GetTeamRoleIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTeamRoleResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        team_role_identifier=team_role_identifier,
        team_identifier_type=team_identifier_type,
        identifier_type=identifier_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    team_role_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    team_identifier_type: Union[Unset, GetTeamRoleTeamIdentifierType] = GetTeamRoleTeamIdentifierType.ID,
    identifier_type: Union[Unset, GetTeamRoleIdentifierType] = GetTeamRoleIdentifierType.ID,
) -> Optional[Union[Any, GetTeamRoleResponse]]:
    """Get Team Role

     Returns team role with given 'id' or 'name'

    Args:
        identifier (str):
        team_role_identifier (str):
        team_identifier_type (Union[Unset, GetTeamRoleTeamIdentifierType]):  Default:
            GetTeamRoleTeamIdentifierType.ID.
        identifier_type (Union[Unset, GetTeamRoleIdentifierType]):  Default:
            GetTeamRoleIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetTeamRoleResponse]
    """

    return sync_detailed(
        identifier=identifier,
        team_role_identifier=team_role_identifier,
        client=client,
        team_identifier_type=team_identifier_type,
        identifier_type=identifier_type,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    team_role_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    team_identifier_type: Union[Unset, GetTeamRoleTeamIdentifierType] = GetTeamRoleTeamIdentifierType.ID,
    identifier_type: Union[Unset, GetTeamRoleIdentifierType] = GetTeamRoleIdentifierType.ID,
) -> Response[Union[Any, GetTeamRoleResponse]]:
    """Get Team Role

     Returns team role with given 'id' or 'name'

    Args:
        identifier (str):
        team_role_identifier (str):
        team_identifier_type (Union[Unset, GetTeamRoleTeamIdentifierType]):  Default:
            GetTeamRoleTeamIdentifierType.ID.
        identifier_type (Union[Unset, GetTeamRoleIdentifierType]):  Default:
            GetTeamRoleIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetTeamRoleResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        team_role_identifier=team_role_identifier,
        team_identifier_type=team_identifier_type,
        identifier_type=identifier_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    team_role_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    team_identifier_type: Union[Unset, GetTeamRoleTeamIdentifierType] = GetTeamRoleTeamIdentifierType.ID,
    identifier_type: Union[Unset, GetTeamRoleIdentifierType] = GetTeamRoleIdentifierType.ID,
) -> Optional[Union[Any, GetTeamRoleResponse]]:
    """Get Team Role

     Returns team role with given 'id' or 'name'

    Args:
        identifier (str):
        team_role_identifier (str):
        team_identifier_type (Union[Unset, GetTeamRoleTeamIdentifierType]):  Default:
            GetTeamRoleTeamIdentifierType.ID.
        identifier_type (Union[Unset, GetTeamRoleIdentifierType]):  Default:
            GetTeamRoleIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetTeamRoleResponse]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            team_role_identifier=team_role_identifier,
            client=client,
            team_identifier_type=team_identifier_type,
            identifier_type=identifier_type,
        )
    ).parsed
