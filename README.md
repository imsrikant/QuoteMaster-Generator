# QuoteMaster Generator

#### Description:

The QuoteMaster Generator is a Python project that fetches and displays quotes from Kanye West using the [Kanye Rest API](https://kanye.rest). The script allows the user to specify the number of quotes to fetch and display via command line arguments.

## Project Structure

- `quote_generator.py`: The main Python script that contains the logic for fetching and displaying Kanye West quotes.
- `README.md`: The documentation file that provides an overview of the project, its structure, and usage.

## Files Explanation

### `quote_generator.py`

This is the main script for the QuoteMaster Generator project. It includes the following functions:

- `main()`: The entry point of the script. It orchestrates the flow of the program by calling other functions.
- `generate_quote(numbers=1)`: Fetches quotes from the Kanye Rest API. The number of quotes fetched is determined by the `numbers` parameter.
- `clean_data(raw_quotes)`: Processes the raw JSON data fetched from the API to extract the quotes.
- `check_argv(argv)`: Validates and processes command line arguments. Ensures that only one argument is passed and that it is a valid number.
- `display_quotes(quotes)`: Prints the fetched quotes to the console.

### Design Choices

1. **API Integration**: The project integrates with the Kanye Rest API to fetch quotes. The choice of using this API was based on its simplicity and the uniqueness of the content.
2. **Command Line Arguments**: The script accepts a single command line argument to specify the number of quotes to fetch. This design choice allows for flexibility in the number of quotes displayed without modifying the code.
3. **Error Handling**: The script includes basic error handling for HTTP request failures and invalid command line arguments. If the API request fails, the script exits with a "Failed" message. If the command line arguments are invalid, the script exits with an appropriate error message.

## Usage

1. **Install the required dependencies**:
   Ensure you have the `requests` module installed. You can install it using pip:

   ```bash
   pip install requests
