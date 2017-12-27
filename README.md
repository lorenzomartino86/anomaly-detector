[![CircleCI](https://circleci.com/gh/lorenzomartino86/anomaly-detector.svg?style=shield&circle-token=:circle-token)](https://circleci.com/gh/lorenzomartino86/anomaly-detector)
[![codecov](https://codecov.io/gh/lorenzomartino86/anomaly-detector/branch/master/graph/badge.svg)](https://codecov.io/gh/lorenzomartino86/anomaly-detector)

# Anomaly Classifier
This is an anomaly classifier agent designed with a hexagonal architecture in order to decouple domain stuff from any external adapter.

## Algorithms
This project organizes the high level operational step of the algorithms inside classes called *pipelines*:
* **Cluster pipeline:** These algorithms classify raw input into clusters with a given technique and then retrieve the outliers comparing train and test clusters.
  * *Cosine Similarity:* It's a measure of similarity between two non-zero vectors of a inner product space that measures the cosine of the angle between them. If you want to find out more please check more details on the *sklearn* documentation: [cosine_similarity](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html)

### Project Structure
The agent is divided by following main packages:
* **Domain**: It includes domain layers such as algorithmic pipelines, delegations objects and the use cases.
* **Adapter**: It contains all the classes with the responsibility to retrieve, store, persist and publish analyzed data.
* **Decorator**: A package with all utility functions used as decorator by domain and adapter classes.


### Instructions
The most simple classification usage is the one that use in-memory datasource
 
* Generate training and test data as collections:
```
    train_data = list()
    train_data.append("Hello world")
    train_data.append("Uncle Bob")
    
    test_data = list()
    test_data.append("It's an outlier")
    test_data.append("Hello world")
```

* Compilation of cluster classifier with the mandatory fields, pipeline is set to ClusterPipeline by default: 

```
    classifier = LogClassifier(train_repository=InMemoryRepository(data=train_data),
                               test_repository=InMemoryRepository(data=test_data),
                               notifier=InMemoryBroker(),
                               pipeline=ClusterPipeline())
    classifier = classifier.compile()
```


* Outlier detection: 

```
    outliers = classifier.detect_anomaly()
```

* Getting the corpus of detected outliers:

```
    >>  for outlier in outliers:
            print (outlier.records)
    [{'corpus': "It's an outlier"}]
```


