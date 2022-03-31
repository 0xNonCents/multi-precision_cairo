# The base of the representation.
const BASE = 2 ** 64

const BASE_SECOND = (2 ** (64 * 2))

const BASE_THIRD = (2 ** (64 * 3))

const BASE_FOURTH = (2 ** (64 * 4))

const BASE_FIFTH = (2 ** (64 * 5))

const BASE_SIXTH = (2 ** (64 * 6))

const BASE_SEVENTH = (2 ** (64 * 7))

struct BigInt6:
    member d0 : felt
    member d1 : felt
    member d2 : felt
    member d3 : felt
    member d4 : felt
    member d5 : felt
end

struct UnreducedBigInt10:
    member d0 : felt
    member d1 : felt
    member d2 : felt
    member d3 : felt
    member d4 : felt
    member d5 : felt
    member d6 : felt
    member d7 : felt
    member d8 : felt
    member d9 : felt
end

func bigint_mul(x : BigInt6, y : BigInt6) -> (res : UnreducedBigInt10):
    return (
        UnreducedBigInt10(
        d0=x.d0 * y.d0,
        d1=x.d0 * y.d1 + x.d1 * y.d0,
        d2=x.d0 * y.d2 + x.d2 * y.d0 + x.d1 * y.d1,
        d3=x.d0 * y.d3 + x.d3 * y.d0 + x.d1 * y.d2 + x.d2 * y.d1,
        d4=x.d0 * y.d4 + x.d4 * y.d0 + x.d1 * y.d3 + x.d3 * y.d1 + x.d2 * y.d2,
        d5=x.d0 * y.d5 + x.d5 * y.d0 + x.d1 * y.d4 + x.d4 * y.d1 + x.d2 * y.d3 + x.d3 * y.d2,
        d6=x.d1 * y.d5 + x.d5 * y.d1 + x.d2 * y.d4 + x.d4 * y.d2 + x.d3 * y.d3,
        d7=x.d2 * y.d5 + x.d5 * y.d2 + x.d3 * y.d4 + x.d3 * y.d4,
        d8=x.d3 * y.d5 + x.d5 * y.d3 + x.d4 * y.d4,
        d9=x.d5 * y.d4 + x.d4 * y.d5,
        # d10=x.d5 * y.d5,
        ))
end

func assert_bigint_is_equal(x : BigInt6, y : BigInt6):
    assert x.d0 = y.d0
    assert x.d1 = y.d1
    assert x.d2 = y.d2
    assert x.d3 = y.d3
    assert x.d4 = y.d4
    assert x.d5 = y.d5
    return ()
end
