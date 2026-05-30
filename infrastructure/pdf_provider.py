from typing import Dict
from core.interfaces import IPdfService


class FpdfCyberpunkService(IPdfService):
    def generate_report(
        self, filepath: str, content: str, meta_info: Dict[str, str]
    ) -> None:
        raise NotImplementedError(
            "FpdfCyberpunkService.generate_report aguardando motor FPDF2."
        )
