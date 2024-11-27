from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_team_routing_rule_payload import UpdateTeamRoutingRulePayload
from ...models.update_team_routing_rule_team_identifier_type import UpdateTeamRoutingRuleTeamIdentifierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    id: str,
    *,
    body: UpdateTeamRoutingRulePayload,
    team_identifier_type: Union[
        Unset, UpdateTeamRoutingRuleTeamIdentifierType
    ] = UpdateTeamRoutingRuleTeamIdentifierType.ID,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_team_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(team_identifier_type, Unset):
        json_team_identifier_type = team_identifier_type.value

    params["teamIdentifierType"] = json_team_identifier_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/v2/teams/{identifier}/routing-rules/{id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
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
    if response.status_code == 422:
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
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTeamRoutingRulePayload,
    team_identifier_type: Union[
        Unset, UpdateTeamRoutingRuleTeamIdentifierType
    ] = UpdateTeamRoutingRuleTeamIdentifierType.ID,
) -> Response[Any]:
    """Update Team Routing Rule (Partial)

     Update routing rule of the team

    Args:
        identifier (str):
        id (str):
        team_identifier_type (Union[Unset, UpdateTeamRoutingRuleTeamIdentifierType]):  Default:
            UpdateTeamRoutingRuleTeamIdentifierType.ID.
        body (UpdateTeamRoutingRulePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        id=id,
        body=body,
        team_identifier_type=team_identifier_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    identifier: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTeamRoutingRulePayload,
    team_identifier_type: Union[
        Unset, UpdateTeamRoutingRuleTeamIdentifierType
    ] = UpdateTeamRoutingRuleTeamIdentifierType.ID,
) -> Response[Any]:
    """Update Team Routing Rule (Partial)

     Update routing rule of the team

    Args:
        identifier (str):
        id (str):
        team_identifier_type (Union[Unset, UpdateTeamRoutingRuleTeamIdentifierType]):  Default:
            UpdateTeamRoutingRuleTeamIdentifierType.ID.
        body (UpdateTeamRoutingRulePayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        id=id,
        body=body,
        team_identifier_type=team_identifier_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
