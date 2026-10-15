import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

def clip_z(a, c):
    """Cap standardised values at ±c so one extreme property cannot extrapolate a linear model."""
    return np.clip(a, -c, c)

class GarageYearFoldImputer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        d = pd.DataFrame(X).copy(); d.columns = ['BasementYrBlt', 'BasementCars']
        yr = pd.to_numeric(d['BasementYrBlt'], errors='coerce')
        cars = pd.to_numeric(d['BasementCars'], errors='coerce')
        self.median_ = float(yr[(cars > 0) & yr.notna()].median())
        return self

    def transform(self, X):
        d = pd.DataFrame(X).copy(); d.columns = ['BasementYrBlt', 'BasementCars']
        yr = pd.to_numeric(d['BasementYrBlt'], errors='coerce')
        cars = pd.to_numeric(d['BasementCars'], errors='coerce').fillna(0)
        present = (cars > 0).astype(float)
        yr = yr.where(present.eq(1), 0).fillna(self.median_)
        return np.column_stack([yr.to_numpy(), present.to_numpy()])
