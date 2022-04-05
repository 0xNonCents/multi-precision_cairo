%lang starknet
%builtins pedersen range_check bitwise

from starkware.cairo.common.cairo_builtins import HashBuiltin, BitwiseBuiltin
from lib.multi_precision import (
    multi_precision_add, multi_precision_sub, multi_precision_mul, sum_products)
from lib.BigInt6 import BigInt6, BigInt12

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

@view
func mul{
        syscall_ptr : felt*, pedersen_ptr : HashBuiltin*, range_check_ptr,
        bitwise_ptr : BitwiseBuiltin*}(x : BigInt6, y : BigInt6) -> (res : BigInt12):
    alloc_locals

    let (res) = multi_precision_mul(x, y)
    return (res)
end

@view
func sum_p{range_check_ptr}(
        p0 : BigInt6, p1 : BigInt6, p2 : BigInt6, p3 : BigInt6, p4 : BigInt6, p5 : BigInt6,
        c : felt) -> (sum : BigInt12):
    let (sum) = sum_products(p0, p1, p2, p3, p4, p5, c)
    return (sum)
end
