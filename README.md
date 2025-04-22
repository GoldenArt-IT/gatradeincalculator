# 📲 GA Trade-In Calculator (Streamlit App)

## 🔧 Overview
This Streamlit app calculates trade-in values for GoldenArt sofa models based on:

- Model price and tier
- Year of purchase
- NCD (Non-Conformance Deduction) scoring
- Loyalty bonus (>10 years)
- File uploads for visual proof

It writes trade-in records into a connected Google Sheet, including scores and base64 image data for review purposes.

---

## 💡 Key Features
- Dropdown model selection from Google Sheets
- NCD Scoring Table with:
  - Point-based checkboxes (Perfect/Average/Bad)
  - File uploader for images (JPEG/PNG/PDF)
- Auto-calculation:
  - Trade-in value after depreciation
  - NCD deduction
  - Loyalty bonus
  - Final value
- Save button to append data to `TRADE IN RECORDS` sheet
- Image conversion to Base64 for direct embedding into Sheets

---

## 🧠 How It Works

1. User selects model → app fetches price & tier
2. User scores furniture condition → NCD scores calculated
3. User inputs year purchased → value depreciated accordingly
4. Loyalty bonus applied if eligible
5. Final value displayed
6. Upon save:
   - App encodes uploaded images to base64
   - App logs all data into the Google Sheet

---

## 🛠️ Run the App

```bash
streamlit run app.py