# Quick Start

This guide demonstrates the basic workflow for integrating enterprise data with AI platforms using the INNORIX SDK.

---

## Prerequisites

* Install the INNORIX Agent
* Configure `agent/agent.yaml`
* Configure `config/transfer.example.yaml`
* Configure `config/pipeline.example.yaml`

---

## Dataset Ingestion

Transfer enterprise datasets into AI shared storage and trigger an AI pipeline.

```python
from sdk.transfer import TransferService
from sdk.pipeline import PipelineFactory

transfer = TransferService()

transfer.connect()

transfer.transfer(
    source="/enterprise/datasets",
    destination="/ai/shared-storage/datasets"
)

transfer.verify(
    source="/enterprise/datasets",
    destination="/ai/shared-storage/datasets"
)

transfer.disconnect()

pipeline = PipelineFactory.create("kubeflow")

pipeline.connect()

execution_id = pipeline.trigger()

pipeline.disconnect()

print(f"Pipeline started: {execution_id}")
```

---

## Result Distribution

Wait for the AI pipeline to finish and transfer the generated outputs back to the enterprise environment.

```python
from sdk.transfer import TransferService
from sdk.pipeline import PipelineFactory

pipeline = PipelineFactory.create("kubeflow")

pipeline.connect()

execution_id = "PIPELINE-000001"

pipeline.wait(execution_id)

result = pipeline.result(execution_id)

pipeline.disconnect()

transfer = TransferService()

transfer.connect()

transfer.transfer(
    source=result["output_path"],
    destination="/enterprise/results"
)

transfer.verify(
    source=result["output_path"],
    destination="/enterprise/results"
)

transfer.disconnect()
```

---

## Supported Pipeline Providers

The same application code can be used with different AI platforms by changing only the provider.

```python
pipeline = PipelineFactory.create("kubeflow")
```

```python
pipeline = PipelineFactory.create("airflow")
```

```python
pipeline = PipelineFactory.create("sagemaker")
```

```python
pipeline = PipelineFactory.create("vertex")
```

```python
pipeline = PipelineFactory.create("azureml")
```

```python
pipeline = PipelineFactory.create("custom")
```

---

## Typical Workflow

```text
Enterprise Data
        │
        ▼
TransferService
        │
        ▼
AI Shared Storage
        │
        ▼
PipelineFactory
        │
        ▼
AI Pipeline
        │
        ▼
AI Results
        │
        ▼
TransferService
        │
        ▼
Enterprise Systems
```

---

## Next Steps

* Configure the INNORIX Agent
* Configure transfer settings
* Configure the pipeline provider
* Replace the reference implementation with the production SDK
* Integrate the workflow into your AI platform
