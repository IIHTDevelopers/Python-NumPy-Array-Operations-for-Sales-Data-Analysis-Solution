import numpy as np

class SalesAnalysis:
    def __init__(self, product1_sales, product2_sales):
        """Initialize two NumPy arrays for daily sales data."""
        self.product1_sales = np.array(product1_sales, dtype=np.int32)
        self.product2_sales = np.array(product2_sales, dtype=np.int32)

    def find_max(self):
        """Find the maximum sales value from the combined sales data."""
        if self.product1_sales.size == 0 or self.product2_sales.size == 0:
            raise ValueError("Sales data cannot be empty")
        combined_sales = np.concatenate((self.product1_sales, self.product2_sales))
        return np.max(combined_sales)

    def find_min(self):
        """Find the minimum sales value from the combined sales data."""
        if self.product1_sales.size == 0 or self.product2_sales.size == 0:
            raise ValueError("Sales data cannot be empty")
        combined_sales = np.concatenate((self.product1_sales, self.product2_sales))
        return np.min(combined_sales)

    def find_sum(self):
        """Find the sum of sales data from both products."""
        if self.product1_sales.size == 0 or self.product2_sales.size == 0:
            raise ValueError("Sales data cannot be empty")
        combined_sales = np.concatenate((self.product1_sales, self.product2_sales))
        return np.sum(combined_sales)
