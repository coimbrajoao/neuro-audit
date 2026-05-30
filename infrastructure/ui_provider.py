from core.interfaces import IWindowDialogService


class PyWebViewDialogService(IWindowDialogService):
    def __init__(self):
        self._window = None

    def set_window(self, window) -> None:
        self._window = window

    def ask_for_folder(self) -> str:
        raise NotImplementedError("PyWebViewDialogService.ask_for_folder pendente.")

    def ask_for_save_file(self, default_name: str) -> str:
        raise NotImplementedError("PyWebViewDialogService.ask_for_save_file pendente.")
