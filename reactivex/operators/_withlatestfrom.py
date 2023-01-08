from typing import Any, Callable, Tuple, TypeVar, overload

import reactivex
from reactivex import Observable

_A = TypeVar("_A")
_B = TypeVar("_B")
_C = TypeVar("_C")
_D = TypeVar("_D")
_E = TypeVar("_E")
_F = TypeVar("_F")
_G = TypeVar("_G")
_H = TypeVar("_H")
_T = TypeVar("_T")
_J = TypeVar("_J")


@overload
def with_latest_from_(
    __sourceA: Observable[_A],
) -> Callable[[Observable[_T]], Observable[Tuple[_T, _A]]]:
    ...


@overload
def with_latest_from_(
    __sourceA: Observable[_A], __sourceB: Observable[_B]
) -> Callable[[Observable[_T]], Observable[Tuple[_T, _A, _B]]]:
    ...


@overload
def with_latest_from_(
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
) -> Callable[[Observable[_T]], Observable[Tuple[_T, _A, _B, _C]]]:
    ...


@overload
def with_latest_from_(
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
) -> Callable[[Observable[_T]], Observable[Tuple[_T, _A, _B, _C, _D]]]:
    ...


@overload
def with_latest_from_(
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
) -> Callable[[Observable[_T]], Observable[Tuple[_T, _A, _B, _C, _D, _E]]]:
    ...


@overload
def with_latest_from_(
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
    __sourceF: Observable[_F],
) -> Callable[[Observable[_T]], Observable[Tuple[_T, _A, _B, _C, _D, _E, _F]]]:
    ...


@overload
def with_latest_from_(
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
    __sourceF: Observable[_F],
    __sourceG: Observable[_G],
) -> Callable[[Observable[_T]], Observable[Tuple[_T, _A, _B, _C, _D, _E, _F, _G]]]:
    ...


@overload
def with_latest_from_(
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
    __sourceF: Observable[_F],
    __sourceG: Observable[_G],
    __sourceH: Observable[_H],
) -> Callable[[Observable[_T]], Observable[Tuple[_T, _A, _B, _C, _D, _E, _F, _G, _H]]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[Any], *sources: Observable[Any]
) -> Callable[[Observable[Any]], Observable[Tuple[Any, ...]]]:
    ...


def with_latest_from_(
    *sources: Observable[Any],
) -> Callable[[Observable[Any]], Observable[Tuple[Any, ...]]]:
    """With latest from operator.

    Merges the specified observable sequences into one observable
    sequence by creating a tuple only when the first
    observable sequence produces an element. The observables can be
    passed either as seperate arguments or as a list.

    Examples:
        >>> op = with_latest_from(obs1)
        >>> op = with_latest_from(obs1, obs2, obs3)

    Returns:
        An observable sequence containing the result of combining
    elements of the sources into a tuple.
    """

    def with_latest_from(source: Observable[Any]) -> Observable[Any]:
        return reactivex.with_latest_from(source, *sources)

    return with_latest_from


__all__ = ["with_latest_from_"]
