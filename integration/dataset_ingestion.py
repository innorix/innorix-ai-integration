"""
INNORIX AI Integration
Dataset Ingestion Workflow

Reference Workflow

Enterprise Data
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

This reference workflow demonstrates how enterprise datasets
are transferred into an AI platform using the INNORIX SDK.
"""

import logging
from pathlib import Path

import yaml

from sdk.transfer import TransferService
from sdk.pipeline import PipelineFactory

logger = logging.getLogger(__name__)


class DatasetIngestionWorkflow:
    """Reference workflow for AI dataset ingestion."""

    def __init__(
        self,
        transfer_config="../config/transfer.example.yaml",
        pipeline_config="../config/pipeline.example.yaml",
    ):

        self.transfer_config = Path(transfer_config)
        self.pipeline_config = Path(pipeline_config)

        self.transfer = TransferService()

        self.transfer_settings = self._load_yaml(self.transfer_config)
        self.pipeline_settings = self._load_yaml(self.pipeline_config)

        provider = self.pipeline_settings["pipeline"]["provider"]
        self.pipeline = PipelineFactory.create(provider)

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    def _load_yaml(self, path: Path):

        logger.info(f"Loading configuration: {path}")

        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self):

        logger.info("Validating configuration...")

        # TODO
        # Validate source path
        # Validate destination path
        # Validate pipeline configuration

        return True

    # ------------------------------------------------------------------
    # Transfer Dataset
    # ------------------------------------------------------------------

    def transfer_dataset(self):

        source = self.transfer_settings["source"]["path"]
        destination = self.transfer_settings["destination"]["path"]

        logger.info("Starting dataset transfer...")

        self.transfer.connect()

        self.transfer.transfer(
            source=source,
            destination=destination,
        )

        self.transfer.verify(
            source=source,
            destination=destination,
        )

        self.transfer.disconnect()

    # ------------------------------------------------------------------
    # Trigger Pipeline
    # ------------------------------------------------------------------

    def trigger_pipeline(self):

        if not self.pipeline_settings["pipeline"]["enabled"]:
            logger.info("Pipeline integration is disabled.")
            return

        self.pipeline.connect()

        execution_id = self.pipeline.trigger()

        logger.info(f"Pipeline execution started: {execution_id}")

        self.pipeline.disconnect()

    # ------------------------------------------------------------------
    # Execute Workflow
    # ------------------------------------------------------------------

    def execute(self):

        logger.info("==========================================")
        logger.info("Dataset Ingestion Started")
        logger.info("==========================================")

        self.validate()

        self.transfer_dataset()

        self.trigger_pipeline()

        logger.info("==========================================")
        logger.info("Dataset Ingestion Completed")
        logger.info("==========================================")


def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    workflow = DatasetIngestionWorkflow()

    workflow.execute()


if __name__ == "__main__":
    main()