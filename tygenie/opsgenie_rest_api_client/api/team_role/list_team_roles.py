from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_team_role_response import ListTeamRoleResponse
from ...models.list_team_roles_team_identifier_type import ListTeamRolesTeamIdentifierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    team_identifier_type: Union[Unset, ListTeamRolesTeamIdentifierType] = ListTeamRolesTeamIdentifierType.ID,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_team_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(team_identifier_type, Unset):
        json_team_identifier_type = team_identifier_type.value

    params["teamIdentifierType"] = json_team_identifier_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/teams/{identifier}/roles",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListTeamRoleResponse]]:
    if response.status_code == 200:
        response_200 = ListTeamRoleResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListTeamRoleResponse]]:
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
    team_identifier_type: Union[Unset, ListTeamRolesTeamIdentifierType] = ListTeamRolesTeamIdentifierType.ID,
) -> Response[Union[Any, ListTeamRoleResponse]]:
    """List Team Roles

     Returns list of team roles

    Args:
        identifier (str):
        team_identifier_type (Union[Unset, ListTeamRolesTeamIdentifierType]):  Default:
            ListTeamRolesTeamIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListTeamRoleResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        team_identifier_type=team_identifier_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    team_identifier_type: Union[Unset, ListTeamRolesTeamIdentifierType] = ListTeamRolesTeamIdentifierType.ID,
) -> Optional[Union[Any, ListTeamRoleResponse]]:
    """List Team Roles

     Returns list of team roles

    Args:
        identifier (str):
        team_identifier_type (Union[Unset, ListTeamRolesTeamIdentifierType]):  Default:
            ListTeamRolesTeamIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListTeamRoleResponse]
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        team_identifier_type=team_identifier_type,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    team_identifier_type: Union[Unset, ListTeamRolesTeamIdentifierType] = ListTeamRolesTeamIdentifierType.ID,
) -> Response[Union[Any, ListTeamRoleResponse]]:
    """List Team Roles

     Returns list of team roles

    Args:
        identifier (str):
        team_identifier_type (Union[Unset, ListTeamRolesTeamIdentifierType]):  Default:
            ListTeamRolesTeamIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListTeamRoleResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        team_identifier_type=team_identifier_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    team_identifier_type: Union[Unset, ListTeamRolesTeamIdentifierType] = ListTeamRolesTeamIdentifierType.ID,
) -> Optional[Union[Any, ListTeamRoleResponse]]:
    """List Team Roles

     Returns list of team roles

    Args:
        identifier (str):
        team_identifier_type (Union[Unset, ListTeamRolesTeamIdentifierType]):  Default:
            ListTeamRolesTeamIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListTeamRoleResponse]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            team_identifier_type=team_identifier_type,
        )
    ).parsed
