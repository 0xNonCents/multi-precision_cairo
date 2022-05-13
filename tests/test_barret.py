import pytest
from utils import (
    split,
    packEnum,
    pack,
    pack12,
    max_base_bigint6_sum,
    max_base_bigint12_sum,
    field_modulus,
)
from math import sqrt
from hypothesis import given, strategies as st, settings

largest_factor = sqrt(2 ** (64 * 11))

@given(number=st.integers(min_value=1, max_value=2**(64*7)))
@settings(deadline=None)
@pytest.mark.asyncio
async def test_barret_reduction(reduction_factory, number):

    contract = reduction_factory
    number_bigint12 = split(number, length=12)
    execution_info = await contract.reduce(
        number_bigint12 ).call()
    msg = f"Input number: {number}\nSplit input number: {split(number, 12)}\nResult: {execution_info.result[0]}\n"
    print(msg)
    result = pack(execution_info.result[0])
    assert result == number %field_modulus

@pytest.mark.asyncio
async def test_barret_reduction_specific_number(reduction_factory):
    number= 20042277575013791667125926197955011048719829756306435301145390326721041016076443063112985210850570485217514554359039978576402621831

    contract = reduction_factory
    number_bigint12 = split(number, length=12)
    execution_info = await contract.reduce(
        number_bigint12).call()
    msg = f"Input number: {number}\nSplit input number: {split(number, 12)}\nResult: {execution_info.result[0]}\n"
    print(msg)
    result = pack(execution_info.result[0])
    assert result == number %field_modulus