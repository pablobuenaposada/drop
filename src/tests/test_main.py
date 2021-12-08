import tempfile

import pytest

from constants import NO_SOLUTION
from main import main


class TestMain:
    @pytest.mark.parametrize(
        "file, expected",
        (("1\n1 V\n1 V\n", "V"), ("1\n1 V\n1 M\n", NO_SOLUTION), ("", "")),
    )
    def test_main(self, file, expected):
        with tempfile.NamedTemporaryFile(mode="w") as temp:
            temp.write(file)
            temp.flush()
            assert main(temp.name) == expected
