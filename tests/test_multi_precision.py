"""contract.cairo test file."""

import pytest
from utils import split, packEnum,  pack,pack12, max_base_bigint6_sum, base
from math import sqrt
from hypothesis import given, strategies as st, settings

largest_factor = sqrt(2**(64 * 11))


@given(
    x=st.integers(min_value=0, max_value=largest_factor),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_multi_precision_square(multi_precision_factory, x):
    contract = multi_precision_factory

    execution_info = await contract.square(split(x)).call()

    result = pack12(execution_info.result[0])
    assert result == x * x



@given(
    x=st.integers(min_value=0, max_value=largest_factor),
    y=st.integers(min_value=0, max_value=largest_factor),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_multi_precision_sum_products(multi_precision_factory, x, y):
    contract = multi_precision_factory

    x_bigint = split(x)
    products = []
    carry = 0
    print(x_bigint)
    for limb in x_bigint:
        num = limb * y + carry * (2 ** (64 * 5 ))
        a = []
        for _ in range(6):
            num, residue = divmod(num, base)
            a.append(residue)
        products.append(tuple(a))
        carry = num

    p0, p1, p2, p3, p4, p5 = [products[i] for i in (0, 1, 2, 3, 4, 5)]

    print(products)
    print("packed")
    print(p1[0])
    print(packEnum(p0) + p1[0] * (2 ** (64 * 2)))
    print(x * y)
    execution_info = await contract.sum_p(p0, p1, p2, p3, p4, p5, carry).call()

    result = pack12(execution_info.result[0])
    product = x * y

    
    assert result == product

 
@given(
    x=st.integers(min_value=0, max_value=largest_factor),
    y=st.integers(min_value=0, max_value=largest_factor)
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_multi_precision_mul(multi_precision_factory, x, y):
    contract = multi_precision_factory

    execution_info = await contract.mul(split(x), split(y)).call()

    result = pack12(execution_info.result[0])
    print(execution_info.result[0])
    assert result == x * y

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

