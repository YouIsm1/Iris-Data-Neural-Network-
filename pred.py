from NN_IrisDataSetV2_frGt1v3 import *

# Prédictions sur les données de test
predictions = model.predict(test_x)

# Convertir les prédictions en classes
predicted_classes = np.argmax(predictions, axis=1)

# Comparer les prédictions avec les classes réelles
print('Prédictions: ' + str(predicted_classes))
print('Classes réelles: ' + str(test_y))