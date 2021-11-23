def SievePrimeNumber(SieveLimit):
    # Sieve of Eratosthene itself

    IsPrimeList = [True] * (SieveLimit + 1)

    IndexNumberToTest = 2
    while IndexNumberToTest ** 2 <= SieveLimit:
        if IsPrimeList[IndexNumberToTest]:
            IndexMultipleToMark = 2 * IndexNumberToTest
            while IndexMultipleToMark <= SieveLimit:
                IsPrimeList[IndexMultipleToMark] = False
                IndexMultipleToMark += IndexNumberToTest

        IndexNumberToTest += 1

    # Transformation of the IsPrimeList in a list of prime number

    PrimeNumberList = []
    IndexNumberToTest = 2
    while IndexNumberToTest <= SieveLimit:
        if IsPrimeList[IndexNumberToTest]:
            PrimeNumberList.append(IndexNumberToTest)
        IndexNumberToTest += 1

    return PrimeNumberList


print(SievePrimeNumber(100))

IsPrime = [True]*(SieveLimit + 1)