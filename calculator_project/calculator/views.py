from django.shortcuts import render

def calculator(request):
    result = None  # Initialize result to None

    # Check if the request is a POST request
    if request.method == 'POST':
        num1 = request.POST.get('num1')  # Get the first number
        num2 = request.POST.get('num2')  # Get the second number
        operation = request.POST.get('operation')  # Get the operation

        try:
            # Convert inputs to numbers
            num1 = float(num1)
            num2 = float(num2)

            # Perform the calculation based on the selected operation
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            else:
                result = "Invalid operation"
        except ValueError:
            result = "Error: Invalid input"

    # Render the HTML template and pass the result as context
    return render(request, 'calculator/calculator.html', {'result': result})
