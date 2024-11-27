from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_alert_attachments_response import ListAlertAttachmentsResponse
from ...models.list_attachments_alert_identifier_type import ListAttachmentsAlertIdentifierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    alert_identifier_type: Union[Unset, ListAttachmentsAlertIdentifierType] = ListAttachmentsAlertIdentifierType.ID,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_alert_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(alert_identifier_type, Unset):
        json_alert_identifier_type = alert_identifier_type.value

    params["alertIdentifierType"] = json_alert_identifier_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/alerts/{identifier}/attachments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListAlertAttachmentsResponse]]:
    if response.status_code == 200:
        response_200 = ListAlertAttachmentsResponse.from_dict(response.json())

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
) -> Response[Union[Any, ListAlertAttachmentsResponse]]:
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
    alert_identifier_type: Union[Unset, ListAttachmentsAlertIdentifierType] = ListAttachmentsAlertIdentifierType.ID,
) -> Response[Union[Any, ListAlertAttachmentsResponse]]:
    """List Alert Attachments

     List alert attachment names and urls for related alert

    Args:
        identifier (str):
        alert_identifier_type (Union[Unset, ListAttachmentsAlertIdentifierType]):  Default:
            ListAttachmentsAlertIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListAlertAttachmentsResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        alert_identifier_type=alert_identifier_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    alert_identifier_type: Union[Unset, ListAttachmentsAlertIdentifierType] = ListAttachmentsAlertIdentifierType.ID,
) -> Optional[Union[Any, ListAlertAttachmentsResponse]]:
    """List Alert Attachments

     List alert attachment names and urls for related alert

    Args:
        identifier (str):
        alert_identifier_type (Union[Unset, ListAttachmentsAlertIdentifierType]):  Default:
            ListAttachmentsAlertIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListAlertAttachmentsResponse]
    """

    return sync_detailed(
        identifier=identifier,
        client=client,
        alert_identifier_type=alert_identifier_type,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    alert_identifier_type: Union[Unset, ListAttachmentsAlertIdentifierType] = ListAttachmentsAlertIdentifierType.ID,
) -> Response[Union[Any, ListAlertAttachmentsResponse]]:
    """List Alert Attachments

     List alert attachment names and urls for related alert

    Args:
        identifier (str):
        alert_identifier_type (Union[Unset, ListAttachmentsAlertIdentifierType]):  Default:
            ListAttachmentsAlertIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListAlertAttachmentsResponse]]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        alert_identifier_type=alert_identifier_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    alert_identifier_type: Union[Unset, ListAttachmentsAlertIdentifierType] = ListAttachmentsAlertIdentifierType.ID,
) -> Optional[Union[Any, ListAlertAttachmentsResponse]]:
    """List Alert Attachments

     List alert attachment names and urls for related alert

    Args:
        identifier (str):
        alert_identifier_type (Union[Unset, ListAttachmentsAlertIdentifierType]):  Default:
            ListAttachmentsAlertIdentifierType.ID.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListAlertAttachmentsResponse]
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            client=client,
            alert_identifier_type=alert_identifier_type,
        )
    ).parsed
