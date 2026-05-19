from types import TracebackType
from typing import IO, Iterable, Iterator, List, Optional, Type


class NullFile(IO[str]):
    def close(self) -> None:
        pass









    def truncate(self, __size: Optional[int] = 1) -> int:
        return 0


    def writelines(self, __lines: Iterable[str]) -> None:
        pass

    def __next__(self) -> str:
        return ""

    def __iter__(self) -> Iterator[str]:
        return iter([""])

    def __enter__(self) -> IO[str]:
        return self

    def __exit__(
        self,
        __t: Optional[Type[BaseException]],
        __value: Optional[BaseException],
        __traceback: Optional[TracebackType],
    ) -> None:
        pass

    def write(self, text: str) -> int:
        return 0

    def flush(self) -> None:
        pass

    def fileno(self) -> int:
        return -1


NULL_FILE = NullFile()
