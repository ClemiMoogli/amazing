from typing import Sequence, Optional


class TerminalMenu:
    def __init__(
        self,
        entries: Sequence[str],
        *,
        title: Optional[str] = ...,
        cursor_index: int = ...,
        multi_select: bool = ...,
        show_multi_select_hint: bool = ...
    ) -> None: ...

    def show(self) -> Optional[int]: ...
