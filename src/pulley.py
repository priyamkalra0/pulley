from subprocess import getstatusoutput

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