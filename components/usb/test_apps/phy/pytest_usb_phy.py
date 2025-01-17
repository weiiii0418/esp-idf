# SPDX-FileCopyrightText: 2025 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0
import pytest
from pytest_embedded import Dut


@pytest.mark.esp32s2
@pytest.mark.esp32s3
@pytest.mark.esp32p4
@pytest.mark.generic
@pytest.mark.temp_skip_ci(targets=['esp32p4'], reason='P4 PHY not yet migrated')
def test_usb_phy(dut: Dut) -> None:
    dut.run_all_single_board_cases(group='phy')
