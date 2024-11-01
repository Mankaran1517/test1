# Mankaran Singh Chattha
# 100944566
# Tprg test-1 2024
import pytest
from cylinder1 import volume_cylinder, area_cylinder

def test_volume_cylinder():
    assert round(volume_cylinder(1, 2), 4) == 1.5708
    assert round(volume_cylinder(0.1, 4), 4) == 0.0314
    assert round(volume_cylinder(2, 1), 4) == 3.1416

def test_area_cylinder():
    assert round(area_cylinder(1, 2), 4) == 7.8540
    assert round(area_cylinder(0.1, 4), 4) == 1.2723
    assert round(area_cylinder(2, 1), 4) == 12.5664

def test_negative_height_volume():
    with pytest.raises(ValueError):
        volume_cylinder(1, -1)

def test_negative_height_area():
    with pytest.raises(ValueError):
        area_cylinder(1, -1)