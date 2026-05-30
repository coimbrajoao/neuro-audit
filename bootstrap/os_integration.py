import ctypes
import platform


class OsIntegrationService:
    @staticmethod
    def configure_windows_taskbar_icon(app_id: str) -> None:
        if platform.system() != "Windows":
            return

        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
        except AttributeError:
            print(
                "[SISTEMA] Aviso: Sistema Operacional não suporta AppUserModelID explícito."
            )
