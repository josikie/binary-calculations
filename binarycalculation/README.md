## Binary Number Calculations
Binary number calculations is python module for binary number calculations. This library could calculate binary addition, binary subtraction, binary multiplication, binary division. For bonus part, this library could help to convert decimal number into binary number, and vice-versa.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Binary Number Calculations.
To install, run this command:
```
pip install binarycalculation
```

## Usage
```
# import BinaryNumber module
from binarycalculation import binarycalculation

binaryOne = "11110001"
binaryTwo = "11101110"

# binary addition
# result: 111011111
binaryAddition = binarycalculation.processBinaryAddition(binaryOne, binaryTwo)
print(binaryAddition)

# binary subtraction
# result: 11
binarySubtraction = binarycalculation.processBinarySubtraction(binaryOne, binaryTwo)
print(binarySubtraction)

# binary multiplication
# result: 1110000000001110
binaryMultiplication = binarycalculation.processBinaryMultiplication(binaryOne, binaryTwo)
print(binaryMultiplication)

# binary subtraction
# result: 1 
# Remainder : 11
# the processBinaryDivision function return two value, result and remainder.
binaryDivision = binarycalculation.processBinaryDivision(binaryOne, binaryTwo)
print(binaryDivision)

# convert binary number to decimal
# result: 241
binaryToDecimal = binarycalculation.convertBinaryToDecimal(binaryOne)
print(binaryToDecimal)

# convert decimal number to binary
# result: 11110001
decimalToBinary = binarycalculation.convertDecimalToBinary(241)
print(decimalToBinary)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Bug and Issues
If you discover bug, please create issue on [Github](https://github.com/josikie/binary-calculations.git). You are also welcome to contribute if you want.

## License
MIT License

Copyright (c) 2023 Josi Kie N.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.