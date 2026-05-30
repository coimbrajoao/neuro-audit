from core.interfaces import IFileSystemService


class OsFileSystemService(IFileSystemService):
    def list_directory(self, target_path: str) -> list:
        raise NotImplementedError(
            "OsFileSystemService.list_directory aguardando codificação."
        )

    def read_file(self, file_path: str) -> str:
        raise NotImplementedError(
            "OsFileSystemService.read_file aguardando codificação."
        )

    def write_file(self, file_path: str, content: str) -> None:
        raise NotImplementedError(
            "OsFileSystemService.write_file aguardando codificação."
        )
