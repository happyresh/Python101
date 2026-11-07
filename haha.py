def magician_hat_probability():
    print("🎩 Magician Hat Probability Calculator")
    
    # Hat 1 input
    squares_hat1 = int(input("Enter number of squares in Hat 1: "))
    triangles_hat1 = int(input("Enter number of triangles in Hat 1: "))
    
    # Hat 2 input (before transfer)
    squares_hat2 = int(input("Enter number of squares in Hat 2: "))
    triangles_hat2 = int(input("Enter number of triangles in Hat 2: "))

    total_hat1 = squares_hat1 + triangles_hat1

    # Case 1: Square is transferred
    prob_square_hat1 = squares_hat1 / total_hat1
    new_squares_hat2_1 = squares_hat2 + 1
    new_triangles_hat2_1 = triangles_hat2
    total_hat2_case1 = new_squares_hat2_1 + new_triangles_hat2_1
    prob_square_hat2_case1 = new_squares_hat2_1 / total_hat2_case1

    # Case 2: Triangle is transferred
    prob_triangle_hat1 = triangles_hat1 / total_hat1
    new_squares_hat2_2 = squares_hat2
    new_triangles_hat2_2 = triangles_hat2 + 1
    total_hat2_case2 = new_squares_hat2_2 + new_triangles_hat2_2
    prob_square_hat2_case2 = new_squares_hat2_2 / total_hat2_case2

    # Total probability
    final_probability = (prob_square_hat1 * prob_square_hat2_case1) + (prob_triangle_hat1 * prob_square_hat2_case2)

    print("\n🎯 Final Probability that a square is drawn from Hat 2: {:.4f}".format(final_probability))

# Run the function
magician_hat_probability()
