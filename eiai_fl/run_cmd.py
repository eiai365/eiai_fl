import os
from subprocess import run, PIPE
import time
import shlex


def run_interactive_command(*, command, log):
    command_fail = True
    command_result = 'FAILED'
    fl_interactive_command_retry_times = os.environ.get('EIAI_FL_INTERACTIVE_COMMAND_RETRY_TIMES')
    if fl_interactive_command_retry_times is None or fl_interactive_command_retry_times == '':
        retry_times = 11
    else:
        retry_times = int(fl_interactive_command_retry_times)
    for i in range(0, retry_times):
        command_fail = False
        command_result = 'FAILED'
        try:
            command_result = run(
                shlex.split(command),
                stdout=PIPE,
                stderr=PIPE,
                check=True,
            ).stdout.decode("utf-8")
        except Exception as e:
            command_fail = True
            log.critical(f"*********** Failure for time {(i + 1)} try...")
            log.critical(f"{e}")
            log.critical('CRITICAL', exc_info=True)
        if command_fail:
            log.error(f"Get error when run command {command}, please see above error message")
            if i < 10:
                time.sleep(10 * (i + 1))
        else:
            break
    return command_fail, command_result


def run_local_command(*, command, log):
    command_fail = False
    command_result = 'FAILED'
    try:
        command_result = run(
            shlex.split(command),
            stdout=PIPE,
            stderr=PIPE,
            check=True,
        ).stdout.decode("utf-8")
    except Exception as e:
        command_fail = True
        log.critical(f"{e}")
        log.critical('CRITICAL', exc_info=True)
    if command_fail:
        log.error(f"Get error when run command {command}, please see above error message")
    return command_fail, command_result
