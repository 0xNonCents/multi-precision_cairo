from lib.BigInt6 import BigInt6, BASE
from starkware.cairo.common.math_cmp import is_le
from starkware.cairo.common.math import unsigned_div_rem
from starkware.cairo.common.bitwise import bitwise_and
from starkware.cairo.common.cairo_builtins import HashBuiltin, BitwiseBuiltin

const MASK = 2 ** 64 - 1

func mod_range{range_check_ptr}(dividend : felt) -> (remainder : felt):
    alloc_locals

    let (_, remainder) = unsigned_div_rem(dividend, BASE)

    return (remainder)
end

# @dev truncates overflow on most signifigant bit
func multi_precision_add{range_check_ptr, bitwise_ptr : BitwiseBuiltin*}(
        x : BigInt6, y : BigInt6) -> (res : BigInt6):
    alloc_locals

    let res_0 = x.d0 + y.d0

    # If x + y = sum, sum >= BASE then remainder
    # sum = 2^64 - 1 : No Remainder
    # sum = 2^64 : Remainder
    let (has_remainder_0) = is_le(BASE, res_0)

    let res_1 = x.d1 + y.d1 + has_remainder_0

    let (has_remainder_1) = is_le(BASE, res_1)

    let res_2 = x.d2 + y.d2 + has_remainder_1

    let (has_remainder_2) = is_le(BASE, res_2)

    let res_3 = x.d3 + y.d3 + has_remainder_2

    let (has_remainder_3) = is_le(BASE, res_3)

    let res_4 = x.d4 + y.d4 + has_remainder_3

    let (has_remainder_4) = is_le(BASE, res_4)

    let res_5 = x.d5 + y.d5 + has_remainder_4

    # Overflow trunaction
    let (d0) = bitwise_and(res_0, MASK)
    let (d1) = bitwise_and(res_1, MASK)
    let (d2) = bitwise_and(res_2, MASK)
    let (d3) = bitwise_and(res_3, MASK)
    let (d4) = bitwise_and(res_4, MASK)
    let (trunacted_d5) = bitwise_and(res_5, MASK)

    return (
        BigInt6(
        d0=d0,
        d1=d1,
        d2=d2,
        d3=d3,
        d4=d4,
        d5=trunacted_d5
        ))
end
