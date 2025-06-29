### Machine Learning Models

This project leverages machine learning to predict rental prices and classify flats by quality. The models are trained on features like number of rooms, area, floor, total floors, and price per square meter.

#### 1. **Random Forest Regressor**
- **Goal**: Estimate rental prices from flat features.
- **Results**:
    - **R² Score**: 0.97 (explains 97% of price variance)
    - **MAE**: 6,668 KZT (average error)
    - **RMSE**: 54,083 KZT (prediction error spread)
- **Key Features**: `Price_per_m2` (53%) and `Area` (46%) are most influential.
- **Use Cases**:
    - Price prediction for new listings
    - Helping landlords set competitive prices

#### 2. **Gradient Boosting Classifier**
- **Goal**: Categorize flats as `Low`, `Medium`, or `High` quality.
- **Results**:
    - High classification accuracy
    - Strong precision, recall, and F1-scores for all categories
- **Use Cases**:
    - Assisting renters in finding flats by quality
    - Helping agencies categorize properties

#### 3. **Model Evaluation**
- Confusion matrices show minimal misclassifications, indicating reliable predictions.
- Random Forest also accurately predicts quality categories.

#### 4. **Practical Applications**
- **Renters**: Estimate prices and find suitable quality categories.
- **Landlords**: Gain insights for pricing and property categorization.
- **Agencies**: Streamline property evaluation and client recommendations.

#### Future Directions
- Add features like building age, amenities, and transport proximity.
- Explore advanced models (e.g., XGBoost, neural networks).
- Expand dataset to cover more cities for broader use.
