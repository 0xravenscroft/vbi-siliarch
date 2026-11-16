import unittest


from siliarch.profile import max_memory_bytes, validate_memory_bytes, validate_profile

class MemoryBytesTests(unittest.TestCase):

    def test_valid_values(self):
        for value in (1, 65536, max_memory_bytes):
            with self.subTest(value=value):
                self.assertEqual(validate_memory_bytes(value), value)

    def test_invalid_values(self):
        invalid_values = (
            0,
            -1,
            max_memory_bytes + 1,
            True,
            1.5,
            "65536",
            None,
        )

        for value in invalid_values:
            with self.subTest(value=repr(value)):
                with self.assertRaises(ValueError):
                    validate_memory_bytes(value)



class DeviceProfileTests(unittest.TestCase):
    def setUp(self):
        self.profile = {
            "schema_version": "0.1",
            "device_id": "lab-board-01",
            "architecture": "riscv64",
            "memory_bytes": 65536,
            "capabilities": ["uart", "spi"],
        }

    def test_valid_profile(self):
        self.assertIsNone(validate_profile(self.profile))

    def test_missing_field_is_rejected(self):
        del self.profile["device_id"]
        with self.assertRaises(ValueError):
            validate_profile(self.profile)

    def test_unknown_field_is_rejected(self):
        self.profile["firmware_hash"] = "unverified"
        with self.assertRaises(ValueError):
            validate_profile(self.profile)

    def test_invalid_values_are_rejected(self):
        cases = [
            ("schema_version", "0.2"),
            ("device_id", "bad id"),
            ("architecture", "mips"),
            ("memory_bytes", True),
            ("capabilities", ["uart", "uart"]),
            ("capabilities", ["ethernet"]),
            ("capabilities", "uart"),
        ]
        for field, bad_value in cases:
            with self.subTest(field=field, bad_value=bad_value):
                candidate = self.profile.copy()
                candidate[field] = bad_value
                with self.assertRaises(ValueError):
                    validate_profile(candidate)

    def test_empty_capabilities_are_allowed(self):
        self.profile["capabilities"] = []
        self.assertIsNone(validate_profile(self.profile))
