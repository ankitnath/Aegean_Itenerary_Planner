# Project Name: Aegean Itinerary Planner
# Developed by : Ankit Nath
# Description: Plans transportation itinerary based on customer preferences with validation

import sys
from collections import defaultdict

def main():
    try:
        # Read input lines, ignoring empty ones
        input_lines = []
        for line in sys.stdin:
            stripped_line = line.strip()
            if stripped_line:
                input_lines.append(stripped_line)

        # Validate basic input structure
        if len(input_lines) < 2:
            print("NO ITINERARY")
            return

        try:
            num_hops = int(input_lines[0])  
            num_customers = int(input_lines[1])
        except ValueError:
            print("INVALID INPUT")
            return

        if len(input_lines) < 2 + num_customers:
            print("NO ITINERARY")
            return

        customers = []

        # Parse each customer's hop preferences
        for line in input_lines[2:2 + num_customers]:
            entries = line.split(', ')
            preferences = []
            airborne_count = 0
            for entry in entries:
                try:
                    hop_index_str, mode = entry.split()
                    hop_index = int(hop_index_str)
                    if mode not in ['airborne', 'by-sea']:
                        print("INVALID INPUT")
                        return
                    if mode == 'airborne':
                        airborne_count += 1
                    preferences.append((hop_index, mode))
                except:
                    print("INVALID INPUT")
                    return
            if airborne_count > 1:
                print("INVALID INPUT")
                return
            customers.append(preferences)

        itinerary = ['by-sea'] * num_hops

        forced_airborne_hops = set()
        for customer in customers:
            if len(customer) == 1 and customer[0][1] == 'airborne':
                forced_airborne_hops.add(customer[0][0])

        for hop_index in forced_airborne_hops:
            if hop_index >= num_hops or hop_index < 0:
                print("NO ITINERARY")
                return
            itinerary[hop_index] = 'airborne'

        # Check which customers are satisfied
        satisfied = [False] * num_customers
        for i, customer in enumerate(customers):
            for hop_index, mode in customer:
                if hop_index >= num_hops or hop_index < 0:
                    print("NO ITINERARY")
                    return
                if itinerary[hop_index] == mode:
                    satisfied[i] = True
                    break

        # Check for unsatisfied customers and their airborne options
        unsatisfied_customers = []
        hop_to_customers = defaultdict(list)

        for i, customer in enumerate(customers):
            if not satisfied[i]:
                airborne_hops = [h for h, m in customer if m == 'airborne']
                if not airborne_hops:
                    print("NO ITINERARY")
                    return
                unsatisfied_customers.append(i)
                for hop_index in airborne_hops:
                    if hop_index >= num_hops or hop_index < 0:
                        print("NO ITINERARY")
                        return
                    hop_to_customers[hop_index].append(i)

        # Allocate airborne to the hops that benefit the greatest number of unhappy customers
        while unsatisfied_customers:
            best_hop = None
            max_helped = 0
            for hop_index in hop_to_customers:
                helped = sum(1 for c in hop_to_customers[hop_index] if c in unsatisfied_customers)
                if helped > max_helped:
                    max_helped = helped
                    best_hop = hop_index

            if best_hop is None:
                print("NO ITINERARY")
                return

            itinerary[best_hop] = 'airborne'
            for cust_id in hop_to_customers[best_hop]:
                if cust_id in unsatisfied_customers:
                    unsatisfied_customers.remove(cust_id)

        # Ensure all customers have at least one matching hop
        for customer in customers:
            fulfilled = False
            for hop_index, mode in customer:
                if hop_index >= num_hops or hop_index < 0:
                    print("NO ITINERARY")
                    return
                if itinerary[hop_index] == mode:
                    fulfilled = True
                    break
            if not fulfilled:
                print("NO ITINERARY")
                return

        # Final itinerary
        output = [f"{i} {mode}" for i, mode in enumerate(itinerary)]
        print(', '.join(output))

    except Exception:
        print("INVALID INPUT")

if __name__ == "__main__":
    main()