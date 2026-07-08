# Pipeline Integration

## Overview

INNORIX integrates with AI orchestration platforms by transferring enterprise datasets into AI environments and distributing AI-generated outputs back to enterprise systems.

The integration is platform-independent through the Pipeline SDK interface.

---

## Supported Platforms

* Kubeflow
* Apache Airflow
* Amazon SageMaker Pipelines
* Google Vertex AI Pipelines
* Azure Machine Learning
* Custom AI Platforms

---

## Dataset Ingestion

```text id="pqdfna"
Enterprise
    │
    ▼
INNORIX
    │
    ▼
AI Shared Storage
    │
    ▼
AI Pipeline
```

Workflow:

1. Transfer enterprise datasets.
2. Store datasets in AI shared storage.
3. Trigger the AI pipeline.

---

## Result Distribution

```text id="yrqthj"
AI Pipeline
    │
    ▼
AI Shared Storage
    │
    ▼
INNORIX
    │
    ▼
Enterprise
```

Workflow:

1. Wait for pipeline completion.
2. Retrieve AI-generated outputs.
3. Transfer outputs to enterprise systems.

---

## Pipeline SDK

The integration examples use the Pipeline SDK abstraction.

```text id="jlwm9x"
PipelineFactory
        │
        ▼
PipelineClient
        │
        ├── Kubeflow
        ├── Airflow
        ├── SageMaker
        ├── Vertex AI
        ├── Azure ML
        └── Custom
```

Each pipeline adapter implements the same interface, allowing workflow code to remain unchanged regardless of the underlying AI platform.
