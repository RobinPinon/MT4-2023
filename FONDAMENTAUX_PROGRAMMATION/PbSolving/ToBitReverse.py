# --< Bit-Reversal Permutation Generator >------------------------------------------------------------------------------
#
#               Compute the reversed binary representation of a unsigned integer
#
# Parameters :  Natural -> unsigned Value to reverse
#               Range   -> number of permutation of the input binary word
# Return :      Bit-Reversed value of Natural
#
# ----------------------------------------------------------------------------------------------------------------------

def ToBitReversedIndex(Natural, Range):
    if Range < 4:
        return Natural

    Reversed = Natural & 1
    Natural >>= 1
    Range >>= 1
    while Range != 2:
        Reversed <<= 1
        Reversed += Natural & 1
        Natural >>= 1
        Range >>= 1

    Reversed <<= 1
    Reversed += Natural & 1

    return Reversed

# --< Bit-Reversal Permutation List Generator >-------------------------------------------------------------------------
#
#               Compute the list of swap index
#
# Parameters :  Range   -> number of permutation of the input binary word
#
# Return :      List of tuples ( Natural Bit Order, Reversed Bit Order)
#
# ----------------------------------------------------------------------------------------------------------------------


def GenerateBitReversedSwapList(Range):
    IsSwaped = [False]*Range
    ListSwap = []
    for n in range(Range) :
        r = ToBitReversedIndex(n, Range)
        if (r!=n) and (not IsSwaped[n]) :
            ListSwap.append((r,n))
            IsSwaped[n] = True
            IsSwaped[r] = True
    return ListSwap

# --< Reverse List In Bit-Reversal Index Order >------------------------------------------------------------------------
#
#               Reorder the list in-place from natural bit indexing to reversed bit indexing
#
# Parameters :  List     -> List to reorder
#               ListSwap -> List of tuples ( Natural Bit Order, Reversed Bit Order)
#
# Return :      Reordered List
#
# ----------------------------------------------------------------------------------------------------------------------

