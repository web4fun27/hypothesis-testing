import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers

total_visitor_count = len(all_visitors)
print('Total visitors count:')
print(total_visitor_count)

paying_visitor_count = len(paying_visitors)
print('Total paying visitors:')
print(paying_visitor_count)

baseline_percent = paying_visitor_count / total_visitor_count * 100
print('Baseline conversion rate:')
print(baseline_percent)

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print('Average payment:')
print(average_payment)

new_customers_needed = np.ceil(1240 / average_payment)
print('New customers needed:')
print(new_customers_needed)

percentage_point_increase = new_customers_needed / total_visitor_count * 100
print('Percentage point increase:')
print(percentage_point_increase)

mde = percentage_point_increase / baseline_percent * 100
print('Minimum detectable effect:')
print(mde)

ab_sample_size = 490