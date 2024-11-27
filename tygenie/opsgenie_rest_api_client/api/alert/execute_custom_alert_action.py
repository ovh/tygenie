from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.alert_action_payload import AlertActionPayload
from ...models.execute_custom_alert_action_identifier_type import ExecuteCustomAlertActionIdentifierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    action_name: str,
    *,
    body: AlertActionPayload,
    identifier_type: Union[Unset, ExecuteCustomAlertActionIdentifierType] = ExecuteCustomAlertActionIdentifierType.ID,
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
        "url": f"/v2/alerts/{identifier}/actions/{action_name}",
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
    action_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertActionPayload,
    identifier_type: Union[Unset, ExecuteCustomAlertActionIdentifierType] = ExecuteCustomAlertActionIdentifierType.ID,
) -> Response[Any]:
    """Custom Alert Action

     Custom actions for the alert

    Args:
        identifier (str):
        action_name (str):
        identifier_type (Union[Unset, ExecuteCustomAlertActionIdentifierType]):  Default:
            ExecuteCustomAlertActionIdentifierType.ID.
        body (AlertActionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        action_name=action_name,
        body=body,
        identifier_type=identifier_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    identifier: str,
    action_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AlertActionPayload,
    identifier_type: Union[Unset, ExecuteCustomAlertActionIdentifierType] = ExecuteCustomAlertActionIdentifierType.ID,
) -> Response[Any]:
    """Custom Alert Action

     Custom actions for the alert

    Args:
        identifier (str):
        action_name (str):
        identifier_type (Union[Unset, ExecuteCustomAlertActionIdentifierType]):  Default:
            ExecuteCustomAlertActionIdentifierType.ID.
        body (AlertActionPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        action_name=action_name,
        body=body,
        identifier_type=identifier_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
