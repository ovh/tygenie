from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_notification_rule_step_payload import CreateNotificationRuleStepPayload
from ...models.success_response import SuccessResponse
from ...types import Response


def _get_kwargs(
    identifier: str,
    rule_id: str,
    *,
    body: CreateNotificationRuleStepPayload,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v2/users/{identifier}/notification-rules/{rule_id}/steps",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json;charset=UTF-8"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SuccessResponse]]:
    if response.status_code == 201:
        response_201 = SuccessResponse.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
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
) -> Response[Union[Any, SuccessResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    rule_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateNotificationRuleStepPayload,
) -> Response[Union[Any, SuccessResponse]]:
    """Create Notification Rule Step

     Creates a new notification rule step

    Args:
        identifier (str):
        rule_id (str):
        body (CreateNotificationRuleStepPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SuccessResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        rule_id=rule_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    rule_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateNotificationRuleStepPayload,
) -> Optional[Union[Any, SuccessResponse]]:
    """Create Notification Rule Step

     Creates a new notification rule step

    Args:
        identifier (str):
        rule_id (str):
        body (CreateNotificationRuleStepPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SuccessResponse]
    """

    return sync_detailed(
        identifier=identifier,
        rule_id=rule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    rule_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateNotificationRuleStepPayload,
) -> Response[Union[Any, SuccessResponse]]:
    """Create Notification Rule Step

     Creates a new notification rule step

    Args:
        identifier (str):
        rule_id (str):
        body (CreateNotificationRuleStepPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SuccessResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        rule_id=rule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    rule_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateNotificationRuleStepPayload,
) -> Optional[Union[Any, SuccessResponse]]:
    """Create Notification Rule Step

     Creates a new notification rule step

    Args:
        identifier (str):
        rule_id (str):
        body (CreateNotificationRuleStepPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SuccessResponse]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            rule_id=rule_id,
            client=client,
            body=body,
        )
    ).parsed
