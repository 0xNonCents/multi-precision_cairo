"""contract.cairo test file."""

import pytest
from utils import split, packEnum,  pack,pack12, max_base_bigint6_sum, base
from math import sqrt
from hypothesis import given, strategies as st, settings

largest_factor = sqrt(2**(64 * 11))


@given(
    x=st.integers(min_value=1,  max_value=(10)),
    y=st.integers(min_value=1,  max_value=(10)),
    base = st.integers(min_value=0, max_value=(5))
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_simple_div(multi_precision_factory, x, y, base):
    contract = multi_precision_factory
    execution_info = await contract.div(split(x * 2 ** (64 * base)), split(y * 2 ** (64 * base))).call()

    q = pack(execution_info.result[0])
    r = pack(execution_info.result[1])   
    assert q == x // y
    assert r == x % y

@given(
    x=st.integers(min_value=1,  max_value=(10)),
    y=st.integers(min_value=1,  max_value=(10)),
    base = st.integers(min_value=0, max_value=(5))
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_simple_div(multi_precision_factory, x, y, base):
    contract = multi_precision_factory
    execution_info = await contract.div_same_limb(split(x * 2 ** (64 * base)), split(y * 2 ** (64 * base))).call()

    result = execution_info.result[0]

    print(result)
    
    assert result == x // y
    

@given(
    x=st.integers(min_value=0,  max_value=(2**384)),
    y=st.integers(min_value=0,  max_value=(2**384))
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_ge(multi_precision_factory, x, y):
    contract = multi_precision_factory
    execution_info = await contract.ge(split(x), split(y)).call()

    result = execution_info.result[0]

    if x >= y:
        assert result == 1
    else:
        assert result == 0
        
@given(
    x=st.integers(min_value=0,  max_value=(2**384)),
)
@settings(deadline=None)
@pytest.mark.asyncio
async def test_find_lead_limb(multi_precision_factory, x):
    contract = multi_precision_factory

    execution_info = await contract.lead_limb(split(x)).call()

    result = execution_info.result[0]
    
    index = 0
    if x >= 2**320:
        index = 5
    elif x >= 2**256:
        index = 4
    elif x >= 2**192:
        index = 3
    elif x >= 2**128:
        index = 2
    elif x >= 2**64:
        index = 1
    assert result == index


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

