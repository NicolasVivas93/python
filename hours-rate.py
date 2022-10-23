hours = input("Enter hours:")
rate = input("Enter rate:")

def computepay(hours, rate):
    hs_extra = hours - 40
    extra_rate = rate / 2
    extra_pay = hs_extra * extra_rate

    if hours <= 40:
        total_pay = hours * rate
    else:
        total_pay = (hours * rate) + extra_pay

    return total_pay


try:
    hs_conv = float(hours)
    rate_conv = float(rate)
except:
    hs_conv = -1
    rate_conv = -1

if hs_conv == -1 and rate_conv == -1:
    print("Please enter numeric data")
else:
    print("Payment: $",computepay(hs_conv, rate_conv))