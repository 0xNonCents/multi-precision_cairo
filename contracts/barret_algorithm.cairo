%lang starknet
%builtins pedersen range_check bitwise

from starkware.cairo.common.cairo_builtins import HashBuiltin, BitwiseBuiltin
from lib.barret_algorithm import barret_reduction
from lib.BigInt6 import BigInt12, BigInt6

@view
func reduce{range_check_ptr, bitwise_ptr : BitwiseBuiltin*}(x : BigInt12) -> (res : BigInt6):
    let (res : BigInt6) = barret_reduction(x)

    return (res)
end
