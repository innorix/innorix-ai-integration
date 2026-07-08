# INNORIX Agent

The INNORIX Agent is responsible for securely transferring enterprise data between enterprise infrastructure and AI platforms.

Installed on enterprise servers, the Agent communicates with the INNORIX Platform to execute high-performance file transfers for AI dataset ingestion and AI result distribution.

---

## Responsibilities

The INNORIX Agent is responsible for:

* Connecting to the INNORIX Platform
* Receiving transfer requests
* Reading enterprise datasets
* Transferring datasets to AI shared storage
* Retrieving AI-generated outputs
* Delivering AI results to enterprise systems
* Reporting transfer status and progress

---

## Architecture

```text id="dw3es7"
Enterprise Storage
        │
        ▼
 INNORIX Agent
        │
        ▼
INNORIX Platform
        │
        ▼
AI Shared Storage
```

---

## Supported Platforms

The reference installer currently supports RPM-based Linux distributions.

* Rocky Linux
* Red Hat Enterprise Linux
* Oracle Linux
* CentOS
* AlmaLinux

---

## Installation

Install the latest INNORIX Agent.

```bash id="xdboea"
chmod +x install.sh
./install.sh
```

---

## Verification

Verify that the Agent has been installed successfully.

```bash id="bgnnzm"
chmod +x verify.sh
./verify.sh
```

---

## Configuration

Update the Agent configuration before running any integration workflow.

```text id="l8vbl4"
agent.yaml
```

Configuration includes:

* Agent Information
* INNORIX Platform Connection
* Storage Settings
* Transfer Settings
* Logging
* Health Check
* Security

---

## Integration Workflow

After the Agent has been configured:

1. Configure `config/transfer.example.yaml`
2. Configure `config/pipeline.example.yaml`
3. Run `integration/dataset_ingestion.py`
4. Run `integration/result_distribution.py`

---

## Directory Structure

```text id="wvl88y"
agent/
    README.md
    install.sh
    verify.sh
    agent.yaml
```

---

## Related Components

```text id="9jln0n"
config/
    Integration configuration

sdk/
    Reference SDK

integration/
    AI workflow examples
```
