from subprocess import getstatusoutput
from pathlib import Path

# Simple (A)DB (Sh)ell for internal use by Pulley.
class Ash():
    package: str | None = None

    def __init__(self, as_package: str | None = None) -> None:
        self.package = as_package

    def run_as_device(self, command: str) -> tuple[int, str]:
        return getstatusoutput(Pulley.base + command) # type: ignore

    def run_as_package(self, command: str) -> tuple[int, str]:
        if self.package is None:
            raise PulleyException(f"Ash.package must be set before invoking .run_as_package()")
        
        return self.run_as_device(f"run-as {self.package} {command}")

    def run(self, command: str) -> tuple[int, str]:
        return (
            self.run_as_device(command)
            if self.package is None
            else self.run_as_package(command)
        )

class PulleyException(Exception):
    pass

class Pulley():
    base: str = r'adb shell '
    shell: Ash | None = None

    def __init__(self, as_package: str | None = None) -> None:
        self.shell = Ash(as_package)

    def pull_file(self, remote_path: str, local_path: str) -> str | None:
        remote_path, local_path = remote_path, local_path
        target_path = f"./{local_path}/{remote_path}"
        
        Path(target_path).parent.mkdir(exist_ok=True, parents=True)
        
        code, err = self.shell.run(
            f'cat "{remote_path}" > '
            f'"{target_path}"'
        )

        return err if code else None 

    def read_file(self, remote_path: str) -> str:
        code, contents_or_err = self.shell.run(
            f'cat "{remote_path}"'
        )
        if code:
            raise PulleyException(contents_or_err)

        return contents_or_err

    def pull_dir(self, remote_path: str, local_path: str):
        code, message = self.shell.run(f"ls {remote_path}")
        assert not code, message

        children = message.split("\n")

        for child in children:
            if not child: continue
            
            child_path = f"{remote_path}/{child}"
            
            is_file, _ = self.shell.run(f'test -d "{child_path}"')

            if not is_file:
                self.pull_dir(
                    remote_path=child_path,
                    local_path=local_path
                )
                continue
            
            print(child_path)
            err = self.pull_file(
                remote_path=child_path,
                local_path=local_path
            )
            if err: print(err)