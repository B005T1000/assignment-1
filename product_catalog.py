from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print("Sample products data:")
for product in products[:3]:
    print(product)

# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.


customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input()
    # Add the customer preference to the list
    customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_tags = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    # Assume each product is a dictionary with a 'tags' key containing a list of tags
    product_copy = product.copy()
    product_copy['tags'] = set(product_copy['tags'])
    converted_products.append(product_copy)




# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags & customer_tags)
    pass




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        match_count = count_matches(product['tags'], customer_tags)
        recommendations.append({
            'name': product['name'],
            'match_score': match_count
        })
    return recommendations
    pass



# TODO: Step 7 - Call your function and print the results
results = recommend_products(converted_products, customer_tags)
print("\nRecommended products with match scores:")
for item in results:
    print(f"Product: {item['name']}, Match Score: {item['match_score']}")




# DESIGN MEMO (write below in a comment):
# 1. I used loops to iterate through products and collect user preferences,
#  and set intersections to efficiently compare customer preferences with product tags. Loops allow processing each item individually, while set intersections quickly find common tags, making matching faster and simpler. These operations are both readable and scalable for larger datasets.
# 2. The data would be best if it was in a database so that it can be updated easily.
