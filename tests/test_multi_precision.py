"""contract.cairo test file."""

import pytest
from utils import split, pack, max_base_bigint6_sum
from hypothesis import given, strategies as st, settings



@given (x=st.integers(min_value=0, max_value=(2**384) / 2),
        y=st.integers(min_value=0, max_value=(2**384) / 2),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_multi_precision_sub(multi_precision_factory, x , y):
    contract = multi_precision_factory

    execution_info = await contract.sub(split(x), split(y)).call()

    print("res ")
    print( execution_info.result[0])
    result = pack(execution_info.result[0])
    if x - y < 0:
        assert result == 0
    else:
        assert result == x - y

@given(
    x=st.integers(min_value=0, max_value=(2**384) / 2),
    y=st.integers(min_value=0, max_value=(2**384) / 2),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_multi_precision_add(multi_precision_factory, x, y):
    contract = multi_precision_factory

    execution_info = await contract.add(split(x), split(y)).call()

    result = pack(execution_info.result[0])
    assert result ==  x + y 

@given(
    x=st.integers(min_value=1, max_value=2**384 - 1),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_multi_precision_add_overflow(multi_precision_factory, x):
    contract = multi_precision_factory

    execution_info = await contract.add(split(x), split(max_base_bigint6_sum)).call()

    result = pack(execution_info.result[0])
    assert result == x - 1



