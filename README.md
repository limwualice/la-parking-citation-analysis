# LA Parking Citation Analysis

This project focuses on analyzing LA parking citation data using the Socrata API and storing the data in Google BigQuery for further analysis and visualization.

![laparking](https://github.com/limwualice/la-parking-citation-analysis/assets/125330688/c0731fa4-a84f-473d-b5ea-c286ccc6475b)


## Project Overview

The LA Parking Citation Analysis project aims to explore and gain insights from the parking citation data provided by the City of Los Angeles. The project involves fetching the data from the Socrata API, storing it in Google Cloud Storage, and loading it into Google BigQuery for analysis.

## API

The project relies on the Socrata API to access the LA parking citation data. The API provides a convenient way to retrieve the data in a structured format. You can find the API documentation and information about the dataset at the following link:

- [LA Parking Citation Dataset on Socrata](https://dev.socrata.com/foundry/data.lacity.org/wjz9-h9np)

## Usage

To use this project, follow these steps:

1. Clone the repository:

git clone https://github.com/your-username/la-parking-citation-analysis.git

markdown


2. Install the required dependencies:

pip install -r requirements.txt



3. Authenticate the Socrata API by providing your app token, username, and password. Modify the `auth()` function in `api_to_gcs_to_bigquery.py` accordingly.

4. Set up your Google Cloud project and enable the BigQuery API. Create a service account and generate a JSON key file.

5. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of your JSON key file:

export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/keyfile.json



6. Configure the necessary parameters in `api_to_gcs_to_bigquery.py` such as the bucket name, dataset ID, and table ID.

7. Run the script to fetch the data from the API, store it in Google Cloud Storage, and load it into BigQuery:

python api_to_gcs_to_bigquery.py

python


8. Analyze and visualize the data in BigQuery using SQL queries or other visualization tools.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
