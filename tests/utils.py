from typing import List

one_bigint6 = ( 1, 0, 0, 0, 0, 0 )

max_base_bigint6 = (2 ** 64 - 1, 0, 0, 0, 0, 0)
max_base_bigint6_sum =( 2 ** 384 ) - 1

def split(num: int) -> List[int]:
    BASE = 2 ** 64
    a = []
    for _ in range(6):
        num, residue = divmod(num, BASE)
        a.append(residue)
    assert num == 0
    return tuple(a)


def pack(z):

    limbs = z.d0, z.d1, z.d2, z.d3, z.d4, z.d5

    return sum(limb * 2 ** (64 * i) for i, limb in enumerate(limbs))


def pack10(z):
    limbs = z.d0, z.d1, z.d2, z.d3, z.d4, z.d5, z.d6, z.d7, z.d8, z.d9, z.d10, z.d11
    return sum(limb * 2 ** (64 * i) for i, limb in enumerate(limbs))