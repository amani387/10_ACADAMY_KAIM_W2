# Handset Data Analysis

This repository contains a Python project focused on analyzing handset data to identify key insights, including the most popular handsets, top manufacturers, and targeted recommendations for marketing strategies.

## Project Overview

The objective of this analysis is to:

1. Identify the top 10 handsets used by customers.
2. Determine the top 3 handset manufacturers.
3. Identify the top 5 handsets for each of the top 3 manufacturers.
4. Provide actionable insights and recommendations for marketing teams.

## Dataset

The dataset includes details about:
- Handset Types
- Handset Manufacturers
- Usage metrics like upload/download volumes, RTTs, and other performance-related statistics.

> **Note:** Ensure the dataset file is in CSV format and matches the column requirements for the analysis.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/amani387/10_ACADAMY_KAIM_W2.git
   ```

2. Navigate to the project directory:
   ```bash
   cd task_1
   ```

3. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place the dataset file in the data directory and update the file path in the script.
2. Run the analysis script:
   ```bash
   create vertual enviroment and run it
   ```

## Results

### Top 10 Handsets
- Lists the 10 most commonly used handset models based on customer data.

### Top 3 Manufacturers
- Highlights the three leading handset manufacturers by usage count.

### Top 5 Handsets per Manufacturer
- Provides the five most popular handsets for each of the top 3 manufacturers.

### Insights and Recommendations
- **Interpretation:**
  1. Apple dominates with multiple handset models in the top 10 list, indicating strong user preference.
  2. Huawei has specific high-performing models, such as Huawei B528S-23A, which is the most used single handset.
  3. Samsung also has a diverse user base, with several models appearing in the top list.

- **Recommendations:**
  1. Focus marketing efforts on popular models, such as Apple iPhone 6S and Huawei B528S-23A, to target current users.
  2. Partner with Apple and Samsung to enhance customer offerings through exclusive deals or promotions.
  3. Analyze user preferences further for Huawei's dominance with the B528S-23A to explore related product promotions.

## File Structure

```
├── task1_user_overview.ipynb         # Main script for analysis
├── requirements.txt     # Python dependencies
├── dataset.csv          # Dataset (replace with your file)
├── README.md            # Project documentation
```

Install dependencies using:
```bash
pip install -r requirements.txt
```


## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request with your changes.

## Contact

For questions or feedback, please contact:
- **Author:** Amanuel Nega  
- **Email:** negaamanuel387@gmail.com  

---

### Acknowledgments
Special thanks to my-self who contributed to this project and provided support.
