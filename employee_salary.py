from math import isfinite


def calculate_gross_salary(base_pay, extra_pay):
    return base_pay + extra_pay


def calculate_tax(gross_pay, percentage):
    return gross_pay * (percentage / 100)


def calculate_net_salary(gross_pay, deduction):
    return gross_pay - deduction


def check_payroll_inputs(base_pay, extra_pay, percentage):
    for amount in (base_pay, extra_pay, percentage):
        if not isfinite(amount):
            raise ValueError("A finite numeric value is required.")
    if base_pay < 0 or extra_pay < 0:
        raise ValueError("Pay amounts must be zero or positive.")
    if percentage < 0 or percentage > 100:
        raise ValueError("Use a tax percentage from 0 to 100.")


def print_pay_statement(employee, gross_pay, deduction, take_home):
    print("\nSalary Statement")
    print("Employee name:", employee)
    print(f"Gross pay = PKR {gross_pay:.2f}")
    print(f"Tax = PKR {deduction:.2f}")
    print(f"Take-home pay = PKR {take_home:.2f}")


def main():
    employee = input("Name of employee: ")
    try:
        base_pay = float(input("Enter basic pay: "))
        extra_pay = float(input("Enter allowance: "))
        percentage = float(input("Enter tax percentage: "))
        check_payroll_inputs(base_pay, extra_pay, percentage)
        gross_pay = calculate_gross_salary(base_pay, extra_pay)
        deduction = calculate_tax(gross_pay, percentage)
        take_home = calculate_net_salary(gross_pay, deduction)
        print_pay_statement(employee, gross_pay, deduction, take_home)
    except ValueError as problem:
        print("Input error:", problem)


if __name__ == "__main__":
    main()
