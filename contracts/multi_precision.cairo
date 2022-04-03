%lang starknet
%builtins pedersen range_check bitwise

from starkware.cairo.common.cairo_builtins import HashBuiltin, BitwiseBuiltin
from lib.multi_precision import multi_precision_add, multi_precision_sub
from lib.BigInt6 import BigInt6

@view
func add{
        syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr,
        bitwise_ptr : BitwiseBuiltin*}(x : BigInt6, y : BigInt6) -> (res : BigInt6):
    alloc_locals

    let (res) = multi_precision_add(x, y)
    return (res)
end

@view
func sub{
        syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr,
        bitwise_ptr : BitwiseBuiltin*}(x : BigInt6, y : BigInt6) -> (res : BigInt6):
    alloc_locals

    let (res) = multi_precision_sub(x, y)
    return (res)
end
