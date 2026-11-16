import re 
max_memory_bytes = 2**63 - 1


def validate_memory_bytes(value: object) -> int:
    if type(value) is not int:
        raise ValueError("memory_bytes must be an integer")

    if not 1 <= value <= max_memory_bytes:
        raise ValueError("memory_bytes is outside the allowed range")

    return value


ALLOWED_ARCHITECTURES = frozenset({"arm64", "riscv64", "x86_64"})
ALLOWED_CAPABILITIES = frozenset({"uart", "spi", "i2c"})

REQUIRED_PROFILE_FIELDS = frozenset({
    "schema_version",
    "device_id",
    "architecture",
    "memory_bytes",
    "capabilities",
})



def validate_profile(profile: object) -> None:
    if type(profile) is not dict:
        raise ValueError("profile must be a dictionary")

    if set(profile) != REQUIRED_PROFILE_FIELDS:
        raise ValueError("profile keys must match schema v0.1")

    version = profile["schema_version"]
    if type(version) is not str or version != "0.1":
        raise ValueError("unsupported schema_version")

    device_id = profile["device_id"]
    if type(device_id) is not str or re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", device_id
    ) is None:
        raise ValueError("invalid device_id")

    architecture = profile["architecture"]
    if type(architecture) is not str or architecture not in ALLOWED_ARCHITECTURES:
        raise ValueError("unsupported architecture")

    validate_memory_bytes(profile["memory_bytes"])


def validate_profile(profile: object) -> None:
    if type(profile) is not dict:
        raise ValueError("profile must be a dictionary")

    if set(profile) != REQUIRED_PROFILE_FIELDS:
        raise ValueError("profile keys must match schema v0.1")

    version = profile["schema_version"]
    if type(version) is not str or version != "0.1":
        raise ValueError("unsupported schema_version")

    device_id = profile["device_id"]
    if type(device_id) is not str or re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9._-]{0,63}", device_id
    ) is None:
        raise ValueError("invalid device_id")

    architecture = profile["architecture"]
    if type(architecture) is not str or architecture not in ALLOWED_ARCHITECTURES:
        raise ValueError("unsupported architecture")

    validate_memory_bytes(profile["memory_bytes"])

    capabilities = profile["capabilities"]
    if type(capabilities) is not list:
        raise ValueError("capabilities must be a list")

    seen = set()
    for capability in capabilities:
        if type(capability) is not str or capability not in ALLOWED_CAPABILITIES:
            raise ValueError("unsupported capability")

        if capability in seen:
            raise ValueError("duplicate capability")

        seen.add(capability)


    capabilities = profile["capabilities"]
    if type(capabilities) is not list:
        raise ValueError("capabilities must be a list")

    seen = set()
    for capability in capabilities:
        if type(capability) is not str or capability not in ALLOWED_CAPABILITIES:
            raise ValueError("unsupported capability")
        if capability in seen:
            raise ValueError("duplicate capability")
        seen.add(capability)


