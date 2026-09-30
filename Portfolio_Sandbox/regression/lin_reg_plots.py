############################################
# Visualization of Linear Regression Results
############################################

# to use these functions in other files, >> import lin_reg_plots as lrp

def plot_linear_performance(y_train, y_test, y_pred_train, y_pred_test, r2_train, r2_test):
    import matplotlib.pyplot as plt
    
    # Create a figure with multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Linear Regression: CLTV Prediction (Demographic & Tenure Data)', 
                 fontsize=16, fontweight='bold', y=1.00)
    
    # ===== SUBPLOT 1: Actual vs Predicted (Train Set) =====
    ax1 = axes[0, 0]
    ax1.scatter(y_train, y_pred_train, alpha=0.5, s=30, color='steelblue', edgecolors='navy', linewidth=0.5)
    min_val = min(y_train.min(), y_pred_train.min())
    max_val = max(y_train.max(), y_pred_train.max())
    ax1.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    ax1.set_xlabel('Actual CLTV ($)', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Predicted CLTV ($)', fontsize=11, fontweight='bold')
    ax1.set_title(f'Train Set: Actual vs Predicted\nR² = {r2_train:.4f}', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # ===== SUBPLOT 2: Actual vs Predicted (Test Set) =====
    ax2 = axes[0, 1]
    ax2.scatter(y_test, y_pred_test, alpha=0.5, s=30, color='darkorange', edgecolors='darkred', linewidth=0.5)
    min_val = min(y_test.min(), y_pred_test.min())
    max_val = max(y_test.max(), y_pred_test.max())
    ax2.plot([min_val, max_val], [min_val, max_val], 'r--', lw=2, label='Perfect Prediction')
    ax2.set_xlabel('Actual CLTV ($)', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Predicted CLTV ($)', fontsize=11, fontweight='bold')
    ax2.set_title(f'Test Set: Actual vs Predicted\nR² = {r2_test:.4f}', fontsize=12, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # ===== SUBPLOT 3: Residuals vs Predicted (Test Set) =====
    ax3 = axes[1, 0]
    residuals = y_test - y_pred_test
    ax3.scatter(y_pred_test, residuals, alpha=0.5, s=30, color='green', edgecolors='darkgreen', linewidth=0.5)
    ax3.axhline(y=0, color='r', linestyle='--', lw=2)
    ax3.set_xlabel('Predicted CLTV ($)', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Residuals ($)', fontsize=11, fontweight='bold')
    ax3.set_title('Residual Plot (Test Set)\nShould show random scatter around zero', fontsize=12, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    
    # ===== SUBPLOT 4: Distribution of Residuals =====
    ax4 = axes[1, 1]
    ax4.hist(residuals, bins=30, color='purple', alpha=0.7, edgecolor='black')
    ax4.axvline(x=0, color='r', linestyle='--', lw=2, label='Zero Error')
    ax4.set_xlabel('Residuals ($)', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax4.set_title(f'Distribution of Residuals\nMean = ${residuals.mean():.2f}, Std = ${residuals.std():.2f}', 
                  fontsize=12, fontweight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3, axis='y')
    
def plot_feature_importance(num_vars, encoder_feature_names, regressor):
    import matplotlib.pyplot as plt
    import numpy as np
    
    # ===== BONUS: Feature Importance (Coefficients) =====
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Get feature names (numeric + encoded categorical)
    feature_names = num_vars + list(encoder_feature_names)
    coefficients = regressor.coef_
    
    # Sort by absolute value for better visualization
    sorted_idx = np.argsort(np.abs(coefficients))
    sorted_features = [feature_names[i] for i in sorted_idx]
    sorted_coefs = coefficients[sorted_idx]
    
    # Color code: positive = blue, negative = orange
    colors = ['steelblue' if x > 0 else 'darkorange' for x in sorted_coefs]
    
    ax.barh(sorted_features, sorted_coefs, color=colors, edgecolor='black', linewidth=0.7)
    ax.set_xlabel('Coefficient Value', fontsize=12, fontweight='bold')
    ax.set_title('Feature Importance: Regression Coefficients\n(Standardized Impact on CLTV)', 
                 fontsize=13, fontweight='bold')
    ax.axvline(x=0, color='black', linestyle='-', lw=0.8)
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.show()