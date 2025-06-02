#!/usr/bin/env python3
"""
E-commerce Sales Performance Analysis
Customer Segmentation & Revenue Optimization

Author: Dinesh Royal
Date: $(date +%Y-%m-%d)
Version: 1.0.0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

def main():
    """Main analysis pipeline"""
    print("🚀 Starting E-commerce Analysis Pipeline...")
    print("=" * 60)
    
    # Generate synthetic data
    customers_df, transactions_df = generate_ecommerce_data()
    
    # Run analysis components
    perform_eda(customers_df, transactions_df)
    rfm_results = perform_rfm_analysis(customers_df, transactions_df)
    model_results = build_clv_model(customers_df, rfm_results)
    generate_business_recommendations(customers_df, transactions_df, rfm_results)
    
    print("\n✅ Analysis Complete!")
    print("📊 Check results/ folder for outputs")

if __name__ == "__main__":
    main()
