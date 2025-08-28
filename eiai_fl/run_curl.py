import enum
from eiai_fl import run_cmd


class CurlHttpEnum(enum.Enum):
    GET = enum.auto()
    DELETE = enum.auto()
    PATCH = enum.auto()
    POST = enum.auto()
    PUT = enum.auto()


class RunCurl:
    def __init__(self):
        pass

    @staticmethod
    def github(*, operation, url, github_token, body, log):
        match CurlHttpEnum[operation]:
            case CurlHttpEnum.GET:
                command = f'curl -L -H "Accept: application/vnd.github+json" -H "Authorization: Bearer {github_token}" -H "X-GitHub-Api-Version: 2022-11-28" {url}'
            case CurlHttpEnum.POST:
                command = f'curl -L -X POST -H "Accept: application/vnd.github+json" -H "Authorization: Bearer {github_token}" -H "X-GitHub-Api-Version: 2022-11-28" {url} -d {body}'
            case CurlHttpEnum.PATCH:
                command = f'curl -L -X PATCH -H "Accept: application/vnd.github+json" -H "Authorization: Bearer {github_token}" -H "X-GitHub-Api-Version: 2022-11-28" {url} -d {body}'
            case _:
                raise KeyError(
                    f'Operation {operation} is not supported.'
                )
        command_fail, command_result = run_cmd.run_interactive_command(command=command, log=log)
        return command_fail, command_result
