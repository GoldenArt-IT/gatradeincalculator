# 📲 GA Trade-In Calculator

A **Streamlit** app to calculate trade-in values of products dynamically based on model, purchase year, NCD scoring, and bonus discounts. Integrates live data from **Google Sheets** and saves trade-in records with uploaded images.

---

✅ **Access the App:**  
[👉 **GA Trade-In Calculator**](https://ga-trade-in-calculator.streamlit.app/)

---

## 📑 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example Workflow](#example-workflow)
- [Project Structure](#project-structure)
- [Reference](#reference)

---

## ✨ Features

- Model selection with pre-loaded price and tier
- Interactive NCD scoring table with image upload per criterion
- Year of purchase selection to compute trade-in depreciation
- Automatic NCD deductions and bonus calculation
- Real-time total trade-in value computation
- Saves trade-in records including scores and images to Google Sheets

---

## ⚙️ Installation

1. **Clone the repository**

   ```
   git clone https://github.com/your-org/ga-trade-in-calculator.git
   cd ga-trade-in-calculator
   ```

2. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```

   Example `requirements.txt`:

   ```
   streamlit
   streamlit_gsheets
   pandas
   pillow
   ```

3. **Create `secrets.toml`**

   ```toml
   [connections.gsheets]
   email = "your_service_account_email"
   private_key = "-----BEGIN PRIVATE KEY-----\n..."

   [allowed_users]
   emails = ["user1@example.com", "user2@example.com"]
   ```

4. **Run the app**

   ```
   streamlit run app.py
   ```

---

## ⚙️ Configuration

- **Google Sheets**
  - Must contain:
    - A `DATA` worksheet with columns:
      - MODEL
      - PRICE VALUE
      - VALUE TIER
      - YEARS OF PURCHASED
      - TRADE IN VALUE
      - ADDITIONAL DISCOUNTS
      - NCD SCORE
      - NCD DEDUCT RATES
    - A `TRADE IN RECORDS` worksheet to store saved records.

- **NCD Requirements**
  - Frame (Wood Structure)
  - Sponge Condition
  - Fabric / Leather Wear
  - Fading / Discoloration
  - Odor / Smoke / Pets
  - Dent / Scratch / Stains
  - Cushion Bounce
  - Spring Noise / Sinking
  - Leg Stability
  - Overall Cleanliness

---

## 🛠️ Usage

1. **Select a Model**
   - Displays price and tier automatically.

2. **Fill NCD Scores**
   - For each requirement, pick a score and optionally upload an image.

3. **Enter Year of Purchase**
   - Determines depreciation and bonus.

4. **Review Calculations**
   - Trade-in value, deductions, and total are computed live.

5. **Save Record**
   - Press **Save Trade-in Records** to store results in Google Sheets.

---

## 💡 Example Workflow

**Scenario:**

- Model: A1 Classic Sofa
- Year Purchased: 8
- NCD Scores: Mostly Average
- Bonus: Loyalty bonus applied
- Uploaded images for scratches and fading

**Outcome:**

- Trade-in Value: RM1,500
- NCD Deduction: RM300
- Bonus Points: RM100
- **Total Trade-In Value:** RM1,300

---

## 📂 Project Structure

```
ga-trade-in-calculator/
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
└── README.md           # This README
```

---

## 📚 Reference

- [Streamlit Documentation](https://docs.streamlit.io)
- [streamlit_gsheets](https://github.com/streamlit/streamlit-gsheets)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [Pillow Docs](https://pillow.readthedocs.io)

---
