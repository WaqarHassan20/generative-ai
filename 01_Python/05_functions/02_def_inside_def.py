# ============================================
# Function Composition and Modularity
# ============================================
# KEY POINTS:
# - Break complex tasks into smaller functions
# - Each function should do one thing well
# - Main function orchestrates sub-functions
# - Improves code readability and maintainability
# ============================================

def fetch_sales():
    """Simulate fetching sales data from database."""
    print("Fetching the sales data...")


def filter_valid_sales():
    """Filter out invalid or incomplete sales records."""
    print("Filtering the sales data...")


def summarize_data():
    """Calculate summary statistics from sales data."""
    print("Summarizing sales data...")


def generate_report():
    """Main function that orchestrates the report generation process."""
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready now!")


# Execute the report generation
generate_report()