import sys
import os

modulepath = os.path.dirname(__file__)

sys.path.insert(0, os.path.join(modulepath, "..", "..", "src"))

import sdata
import pandas as pd
import numpy as np

def test_metadata():

    r1 = {"name":"otto", "value":10.2, "description":"baz"}
    r2 = {"name":"jack", "value":2.3, "unit":"kN"}
    rows = {r1["name"]:r1,
            r2["name"]:r2,
            }

    metadata = sdata.Metadata()
    metadata.update_value(name="otto", value="a")
    print(metadata.data.head())
    print(metadata.data.loc["otto"])
    assert metadata.data.loc["otto"].value=="a"
    metadata.update_value(name="otto", value=1.2, description="bar")
    print(metadata.data.head())
    metadata.update_value(name="foo", value=2, unit="MPa", description="foo")
    print(metadata.data.head())
    metadata.update_value(name="otto", value=2.2, unit="K")
    assert np.isclose(metadata.data.loc["otto"].value, 2.2)

    metadata.from_dict(rows)
    print(metadata.data.head())
    assert np.isclose(metadata.data.loc["otto"].value, 10.2)

def test_io_csv():
    metadata = sdata.Metadata()
    metadata.update_value(name="otto", value="a")
    metadata.update_value(name="foo", value=2, unit="MPa", description="foo")
    metadata.update_value(name="bar", value=2.2, unit="MPa", description="bar")
    print(metadata.data.head())
    filepath="/tmp/metadata.csv"
    metadata.to_csv(filepath)

    metadata2 = sdata.Metadata()
    metadata2.from_csv(filepath)
    print(metadata2.data.head())
    assert all(metadata.data.loc["otto"] == metadata2.data.loc["otto"])
    assert all(metadata.data.loc["foo"] == metadata2.data.loc["foo"])
    assert all(metadata.data.loc["bar"] == metadata2.data.loc["bar"])

if __name__ == '__main__':
    # test_metadata()
    test_io_csv()