from pycaret.datasets import get_data
from pycaret.regression import *
import pandas as pd

insurance = get_data('insurance')

r1 = setup(insurance, target = 'charges', session_id = 123)

# compare baseline models
best = compare_models()

best

# plot feature importance
plot_model(best, plot = 'feature')

save_model(best, model_name = 'model')

# load pipeline
loaded_best_pipeline = load_model('model')
loaded_best_pipeline

