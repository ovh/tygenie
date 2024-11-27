from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.close_incident_identifier_type import CloseIncidentIdentifierType
from ...models.incident_action_payload import IncidentActionPayload
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    body: IncidentActionPayload,
    identifier_type: Union[Unset, CloseIncidentIdentifierType] = CloseIncidentIdentifierType.ID,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    json_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(identifier_type, Unset):
        json_identifier_type = identifier_type.value

    params["identifierType"] = json_identifier_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/incidents/{identifier}/close",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 202:
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentActionPayload,
    identifier_type: Union[Unset, CloseIncidentIdentifierType] = CloseIncidentIdentifierType.ID,
) -> Response[Any]:
    """Close Incident

     Closes incident with given identifier

    Args:
        identifier (str):
        identifier_type (Union[Unset, CloseIncidentIdentifierType]):  Default:
            CloseIncidentIdentifierType.ID.
        body (IncidentActionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        identifier_type=identifier_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: IncidentActionPayload,
    identifier_type: Union[Unset, CloseIncidentIdentifierType] = CloseIncidentIdentifierType.ID,
) -> Response[Any]:
    """Close Incident

     Closes incident with given identifier

    Args:
        identifier (str):
        identifier_type (Union[Unset, CloseIncidentIdentifierType]):  Default:
            CloseIncidentIdentifierType.ID.
        body (IncidentActionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        body=body,
        identifier_type=identifier_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)