arn = "arn:aws:iam::123456789012:user/john"
print(arn)

a = arn.split("/")[0]
b = arn.split("/")[1]
print(a)
print(b)

print(arn.upper())
print(arn.lower())
length = len(arn)
print("Length of the ARN is:", length)

c = a + b
print(c)
