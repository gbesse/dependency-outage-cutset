# dependency-outage-cutset

## Français

Trouver les coupures minimales de dépendances d’un service.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m dependency_outage_cutset examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Transforme un graphe de disponibilité monotone AND/OR en coupures minimales, en conservant les causes communes partagées. Chaque ensemble coupe le service ; les sur-ensembles redondants sont retirés. Complète les modèles de capacité par un diagnostic de disponibilité logique.

### Limites

200 nœuds, 4 096 coupures maximum ; dépendances déclarées sans probabilité, temps de réparation ni capacité partielle. Cycles refusés.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Find minimal dependency cut sets for a service.

Synthetic data; no network access or secret required.

```sh
python -m dependency_outage_cutset examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Transforms a monotone AND/OR availability graph into minimal cut sets, retaining shared common causes. Every set cuts the service; redundant supersets are removed. Complements capacity models with logical availability diagnosis.

### Limits

At most 200 nodes and 4,096 cut sets; declared dependencies without probabilities, repair times or partial capacity. Cycles rejected.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Encontrar conjuntos mínimos de corte de dependencias.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m dependency_outage_cutset examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Transforma un grafo monotónico AND/OR de disponibilidad en conjuntos mínimos de corte conservando causas comunes. Cada conjunto corta servicio; elimina superconjuntos redundantes. Complementa capacidad con diagnóstico lógico.

### Límites

Máximo 200 nodos y 4.096 cortes; dependencias declaradas sin probabilidades, tiempos de reparación ni capacidad parcial. Rechaza ciclos.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/gbesse/resource-outage-explorer
