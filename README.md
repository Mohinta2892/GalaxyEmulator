We created a Galaxy Power Spectrum Emulator given a set of 6 input variables that define an 80D spectrum.

Total dataset size:260K 
- Input shape: `260K x 6`
- Output shape: `260K x 80`
- Datatype: Real (FP)

Trained two models:
- Random Forest Regressor (sklearn)
- 4-layer (2 hidden) MLP (PyTorch)

Metric and Loss: MSE

The MLP outperformed the RFRegressor given that it could be trained with more data on a 16GB RAM Mac Pro.

