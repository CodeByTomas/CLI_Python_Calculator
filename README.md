 ### Simple CLI Calculator

This repository contains a simple command-line interface (CLI) calculator implemented in Python. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

#### Features:
- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second, with error handling for division by zero.

#### Usage:
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/simple-cli-calculator.git
    cd simple-cli-calculator
    ```

2. Run the calculator:
    ```sh
    python calculator.py
    ```

3. Follow the on-screen prompts to select an operation and input numbers.

#### Example:
```sh
Simple CLI Calculator by @CodeByTomas
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice(1/2/3/4): 1
Enter first number: 5
Enter second number: 3
Result: 8.0
```

#### Functions:
- [`add(x, y)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A4%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition"): Returns the sum of [`x`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A8%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition") and [`y`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A11%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition").
- [`subtract(x, y)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A13%2C%22character%22%3A4%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition"): Returns the difference of [`x`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A8%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition") and [`y`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A11%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition").
- [`multiply(x, y)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A26%2C%22character%22%3A4%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition"): Returns the product of [`x`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A8%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition") and [`y`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A11%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition").
- [`divide(x, y)`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A39%2C%22character%22%3A4%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition"): Returns the quotient of [`x`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A8%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition") and [`y`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A11%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition"). If [`y`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2Fpython%2Ftest_folder%2Fcalculator.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A11%7D%7D%5D%2C%220f0b40fb-7275-488a-ac83-e66aa0c4f3bf%22%5D "Go to definition") is 0, returns an error message.

#### License:
This project is licensed under the MIT License. See the LICENSE file for details.
