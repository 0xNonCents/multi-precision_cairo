# @title Big Int 6
# @author Non
# @notice Unigned 384 bit number split into six 64-bit limbs

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

struct BigInt12:
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
    member d10 : felt
    member d11 : felt
end

struct BigInt18:
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
    member d10 : felt
    member d11 : felt
    member d12 : felt
    member d13 : felt
    member d14 : felt
    member d15 : felt
    member d16 : felt
    member d17 : felt
end

func big_int_12_zero() -> (res : BigInt12):
    return (
        res=BigInt12(
        d0=0,
        d1=0,
        d2=0,
        d3=0,
        d4=0,
        d5=0,
        d6=0,
        d7=0,
        d8=0,
        d9=0,
        d10=0,
        d11=0
        ),
    )
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

func is_equal(x : BigInt6, y : BigInt6) -> (res : felt):
    if x.d0 != y.d0:
        return (0)
    end

    if x.d1 != y.d1:
        return (0)
    end

    if x.d2 != y.d2:
        return (0)
    end

    if x.d3 != y.d3:
        return (0)
    end

    if x.d4 != y.d4:
        return (0)
    end

    if x.d5 != y.d5:
        return (0)
    end

    return (1)
end

# @albert_g takes a BigInt12 and forms a BigInt6 with the first 6 limbs of the BigInt12. It is supposed to be used on BigInt12's where d6 = ... = d11 = 0
func from_bigint12_to_bigint6(num : BigInt12) -> (new_num : BigInt6):
    let new_num = BigInt6(d0=num.d0, d1=num.d1, d2=num.d2, d3=num.d3, d4=num.d4, d5=num.d5)
    return (new_num)
end

func from_bigint6_to_bigint12(num : BigInt6) -> (new_num : BigInt12):
    let new_num = BigInt12(
        d0=num.d0,
        d1=num.d1,
        d2=num.d2,
        d3=num.d3,
        d4=num.d4,
        d5=num.d5,
        d6=0,
        d7=0,
        d8=0,
        d9=0,
        d10=0,
        d11=0,
    )
    return (new_num)
end
