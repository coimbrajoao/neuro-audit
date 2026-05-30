from typing import Dict, Any
from core.interfaces import IGitService


class SubprocessGitService(IGitService):
    def execute_command(self, command: str, working_directory: str) -> Dict[str, Any]:
        raise NotImplementedError(
            "SubprocessGitService.execute_command aguardando integração."
        )

    def get_user_info(self, working_directory: str) -> Dict[str, str]:
        raise NotImplementedError(
            "SubprocessGitService.get_user_info aguardando integração."
        )
