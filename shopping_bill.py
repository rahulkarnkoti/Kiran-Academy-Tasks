def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst

def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst

def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst

def totalBill(a, b, c, d, e):
    return calculateElectronicsGST(a, b) + calculateFashionGST(c, d) + calculateFoodGST(e)

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount

total = totalBill(100, 100, 100, 100, 100)
final_amount = calculateDiscountedBill(100, 100, 100, 100, 100)
discount = total - final_amount
print("Total after GST = %.2f" % total)
print("Discount = %.2f" % discount)
print("Final payable amount = %.2f" % final_amount)
