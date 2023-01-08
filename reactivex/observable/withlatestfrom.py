from typing import Any, List, Optional, Tuple, TypeVar, overload

from reactivex import Observable, abc
from reactivex.disposable import CompositeDisposable, SingleAssignmentDisposable
from reactivex.internal.utils import NotSet

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
    __parent: Observable[_T], __sourceA: Observable[_A]
) -> Observable[Tuple[_T, _A]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T], __sourceA: Observable[_A], __sourceB: Observable[_B]
) -> Observable[Tuple[_T, _A, _B]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T],
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
) -> Observable[Tuple[_T, _A, _B, _C]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T],
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
) -> Observable[Tuple[_T, _A, _B, _C, _D]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T],
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
) -> Observable[Tuple[_T, _A, _B, _C, _D, _E]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T],
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
    __sourceF: Observable[_F],
) -> Observable[Tuple[_T, _A, _B, _C, _D, _E, _F]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T],
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
    __sourceF: Observable[_F],
    __sourceG: Observable[_G],
) -> Observable[Tuple[_T, _A, _B, _C, _D, _E, _F, _G]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T],
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
    __sourceF: Observable[_F],
    __sourceG: Observable[_G],
    __sourceH: Observable[_H],
) -> Observable[Tuple[_T, _A, _B, _C, _D, _E, _F, _G, _H]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T],
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
    __sourceF: Observable[_F],
    __sourceG: Observable[_G],
    __sourceH: Observable[_H],
    __sourceT: Observable[_T],
) -> Observable[Tuple[_T, _A, _B, _C, _D, _E, _F, _G, _H, _T]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[_T],
    __sourceA: Observable[_A],
    __sourceB: Observable[_B],
    __sourceC: Observable[_C],
    __sourceD: Observable[_D],
    __sourceE: Observable[_E],
    __sourceF: Observable[_F],
    __sourceG: Observable[_G],
    __sourceH: Observable[_H],
    __sourceT: Observable[_T],
    __sourceJ: Observable[_J],
) -> Observable[Tuple[_T, _A, _B, _C, _D, _E, _F, _G, _H, _T, _J]]:
    ...


@overload
def with_latest_from_(
    __parent: Observable[Any], *sources: Observable[Any]
) -> Observable[Tuple[Any, ...]]:
    ...


def with_latest_from_(
    parent: Observable[Any], *sources: Observable[Any]
) -> Observable[Tuple[Any, ...]]:
    NO_VALUE = NotSet()

    def subscribe(
        observer: abc.ObserverBase[Any], scheduler: Optional[abc.SchedulerBase] = None
    ) -> abc.DisposableBase:
        def subscribeall(
            __parent: Observable[Any], *children: Observable[Any]
        ) -> List[SingleAssignmentDisposable]:

            values = [NO_VALUE for _ in children]

            def subscribechild(
                i: int, child: Observable[Any]
            ) -> SingleAssignmentDisposable:
                subscription = SingleAssignmentDisposable()

                def on_next(value: Any) -> None:
                    with parent.lock:
                        values[i] = value

                subscription.disposable = child.subscribe(
                    on_next, observer.on_error, scheduler=scheduler
                )
                return subscription

            parent_subscription = SingleAssignmentDisposable()

            def on_next(value: Any) -> None:
                with parent.lock:
                    if NO_VALUE not in values:
                        result = (value,) + tuple(values)
                        observer.on_next(result)

            children_subscription = [
                subscribechild(i, child) for i, child in enumerate(children)
            ]
            disp = parent.subscribe(
                on_next, observer.on_error, observer.on_completed, scheduler=scheduler
            )
            parent_subscription.disposable = disp

            return [parent_subscription] + children_subscription

        return CompositeDisposable(subscribeall(parent, *sources))

    return Observable(subscribe)


__all__ = ["with_latest_from_"]
