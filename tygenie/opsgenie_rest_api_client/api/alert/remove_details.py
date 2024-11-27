from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_details_identifier_type import RemoveDetailsIdentifierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    *,
    identifier_type: Union[Unset, RemoveDetailsIdentifierType] = RemoveDetailsIdentifierType.ID,
    user: Union[Unset, str] = UNSET,
    note: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    keys: List[str],
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_identifier_type: Union[Unset, str] = UNSET
    if not isinstance(identifier_type, Unset):
        json_identifier_type = identifier_type.value

    params["identifierType"] = json_identifier_type

    params["user"] = user

    params["note"] = note

    params["source"] = source

    json_keys = keys

    params["keys"] = json_keys

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/v2/alerts/{identifier}/details",
        "params": params,
    }

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
    identifier_type: Union[Unset, RemoveDetailsIdentifierType] = RemoveDetailsIdentifierType.ID,
    user: Union[Unset, str] = UNSET,
    note: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    keys: List[str],
) -> Response[Any]:
    """Remove Details

     Remove details of the alert with given identifier

    Args:
        identifier (str):
        identifier_type (Union[Unset, RemoveDetailsIdentifierType]):  Default:
            RemoveDetailsIdentifierType.ID.
        user (Union[Unset, str]):
        note (Union[Unset, str]):
        source (Union[Unset, str]):
        keys (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        identifier_type=identifier_type,
        user=user,
        note=note,
        source=source,
        keys=keys,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    identifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    identifier_type: Union[Unset, RemoveDetailsIdentifierType] = RemoveDetailsIdentifierType.ID,
    user: Union[Unset, str] = UNSET,
    note: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    keys: List[str],
) -> Response[Any]:
    """Remove Details

     Remove details of the alert with given identifier

    Args:
        identifier (str):
        identifier_type (Union[Unset, RemoveDetailsIdentifierType]):  Default:
            RemoveDetailsIdentifierType.ID.
        user (Union[Unset, str]):
        note (Union[Unset, str]):
        source (Union[Unset, str]):
        keys (List[str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        identifier_type=identifier_type,
        user=user,
        note=note,
        source=source,
        keys=keys,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
