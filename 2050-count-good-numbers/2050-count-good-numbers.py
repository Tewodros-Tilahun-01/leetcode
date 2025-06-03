class Solution:
    def countGoodNumbers(self, n: int) -> int:
        prime = 4
        even = 5
        modulo = pow(10,9)+ 7
        evenPos = math.ceil(n / 2)
        primePos = n - evenPos
        return (pow(prime,primePos,modulo) * pow(even,evenPos,modulo) )% (modulo)


        