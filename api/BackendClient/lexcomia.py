import os
from django.conf import settings
import joblib


class LexComIA_Client:

    def transformers(self, data):
        values_array = []
        values_array.extend(1 if value else 0 for value in data[0:])
        return values_array

    def get_prediction_five_class(self, data):
        model = os.path.join(settings.STATIC_MODELS_IA,
                             'IAmodels', 'random_forest.joblib')
        values_array = list(data.values())
        transformer_array = self.transformers(values_array)
        vector_features = [transformer_array]
        loaded = joblib.load(model)
        loaded_rf_probabilities = loaded.predict_proba(
            vector_features)
        return loaded_rf_probabilities

    def get_prediction_binary_class(self, data):
        model = os.path.join(settings.STATIC_MODELS_IA,
                             'IAmodels', 'logistic_regresion.joblib')
        values_array = list(data.values())
        transformer_array = self.transformers(values_array)
        vector_features = [transformer_array]
        loaded = joblib.load(model)
        loaded_lr_probabilities = loaded.predict_proba(
            vector_features)
        return loaded_lr_probabilities
