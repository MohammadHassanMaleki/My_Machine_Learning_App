"""
WSGI config for MachineLearningApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MachineLearningApp.settings')
application = get_wsgi_application()

# ML registry
import inspect
from mlaps.registry import MLRegistry
from mlaps.income_classifier.random_forest import RandomForestClassifier
from mlaps.income_classifier.extra_tree import ExtraTreesClassifier

try:
    registry = MLRegistry() #create ML registry
    rf = RandomForestClassifier() # RandomForestClassifier
    # add to Ml registry
    registry.add_algorithm(endpoint_name= 'income_classifier',
                           algorithm_object= rf,
                           algorithm_name= 'random forest',
                           algorithm_statuse= 'production',
                           algorithm_version= '0.0.1',
                           owner='Hassan',
                           algorithm_description= "Random Forest with simple pre- and post-processing",
                           algorithm_code= inspect.getsource(RandomForestClassifier)
                           )
    # Extra Trees classifier
    et = ExtraTreesClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="testing",
                            algorithm_version="0.0.1",
                            owner="Hassan",
                            algorithm_description="Extra Trees with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))



