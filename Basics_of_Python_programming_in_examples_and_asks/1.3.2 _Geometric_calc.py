

def compute_resist(r_1, r_2):

   r = r_1 * r_2 / (r_1 + r_2)

   return r

res = compute_resist(12.0, 11.0)
print(res)
