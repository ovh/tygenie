from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_team_role_identifier_type import DeleteTeamRoleIdentifierType
from ...models.delete_team_role_team_identifier_type import DeleteTeamRoleTeamIdentifierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    team_role_identifier: str,
    *,
    team_identifier_type: Union[Unset, DeleteTeamRoleTeamIdentifierType] = DeleteTeamRoleTeamIdentifierType.ID,
    identifier_type: Union[Unset, DeleteTeamRoleIdentifierType] = DeleteTeamRoleIdentifierType.ID,
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
        "method": "delete",
        "url": f"/v2/teams/{identifier}/roles/{team_role_identifier}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 402:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 429:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    team_identifier_type: Union[Unset, DeleteTeamRoleTeamIdentifierType] = DeleteTeamRoleTeamIdentifierType.ID,
    identifier_type: Union[Unset, DeleteTeamRoleIdentifierType] = DeleteTeamRoleIdentifierType.ID,
) -> Response[Any]:
    """Delete Team Role

     Deletes a team role using team role 'id' or 'name'

    Args:
        identifier (str):
        team_role_identifier (str):
        team_identifier_type (Union[Unset, DeleteTeamRoleTeamIdentifierType]):  Default:
            DeleteTeamRoleTeamIdentifierType.ID.
        identifier_type (Union[Unset, DeleteTeamRoleIdentifierType]):  Default:
            DeleteTeamRoleIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    identifier: str,
    team_role_identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    team_identifier_type: Union[Unset, DeleteTeamRoleTeamIdentifierType] = DeleteTeamRoleTeamIdentifierType.ID,
    identifier_type: Union[Unset, DeleteTeamRoleIdentifierType] = DeleteTeamRoleIdentifierType.ID,
) -> Response[Any]:
    """Delete Team Role

     Deletes a team role using team role 'id' or 'name'

    Args:
        identifier (str):
        team_role_identifier (str):
        team_identifier_type (Union[Unset, DeleteTeamRoleTeamIdentifierType]):  Default:
            DeleteTeamRoleTeamIdentifierType.ID.
        identifier_type (Union[Unset, DeleteTeamRoleIdentifierType]):  Default:
            DeleteTeamRoleIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        team_role_identifier=team_role_identifier,
        team_identifier_type=team_identifier_type,
        identifier_type=identifier_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
