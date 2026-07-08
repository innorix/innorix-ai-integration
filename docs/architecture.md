# Architecture

## Overview

The INNORIX AI Integration architecture enables reliable data movement between enterprise environments and AI platforms.

```text
Enterprise Systems
        │
        ▼
 INNORIX Agent
        │
        ▼
INNORIX Platform
        │
        ▼
AI Shared Storage
        │
        ▼
AI Pipeline
        │
        ▼
AI Models / Results
        │
        ▼
INNORIX Platform
        │
        ▼
Enterprise Systems
```

## Components

### Enterprise Systems

Enterprise data sources such as:

* NAS
* Local Storage
* Edge Devices
* Enterprise Applications
* Cloud Storage

### INNORIX Agent

Executes secure and high-performance file transfers between enterprise environments and AI platforms.

### INNORIX Platform

Coordinates transfer requests, monitors transfer status, and manages communication with Agents.

### AI Shared Storage

Shared storage used by AI platforms for datasets, models, and generated outputs.

### AI Pipeline

AI orchestration platforms responsible for training, validation, and inference workflows.

Supported examples include:

* Kubeflow
* Apache Airflow
* Amazon SageMaker Pipelines
* Google Vertex AI Pipelines
* Azure Machine Learning
* Custom AI Platforms

## Integration Workflows

### Dataset Ingestion

```text
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

### Result Distribution

```text
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
