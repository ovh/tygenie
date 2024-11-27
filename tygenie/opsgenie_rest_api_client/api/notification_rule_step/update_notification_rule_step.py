from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_notification_rule_step_payload import UpdateNotificationRuleStepPayload
from ...types import Response


def _get_kwargs(
    identifier: str,
    rule_id: str,
    id: str,
    *,
    body: UpdateNotificationRuleStepPayload,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/v2/users/{identifier}/notification-rules/{rule_id}/steps/{id}",
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
    rule_id: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateNotificationRuleStepPayload,
) -> Response[Any]:
    """Update Notification Rule Step (Partial)

     Update a notification rule step with given user identifier, rule id, and notification rule step id

    Args:
        identifier (str):
        rule_id (str):
        id (str):
        body (UpdateNotificationRuleStepPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        rule_id=rule_id,
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    identifier: str,
    rule_id: str,
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateNotificationRuleStepPayload,
) -> Response[Any]:
    """Update Notification Rule Step (Partial)

     Update a notification rule step with given user identifier, rule id, and notification rule step id

    Args:
        identifier (str):
        rule_id (str):
        id (str):
        body (UpdateNotificationRuleStepPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        rule_id=rule_id,
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
