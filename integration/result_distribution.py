"""
INNORIX AI Integration
Result Distribution Workflow

Reference Workflow

AI Pipeline
        │
        ▼
AI Shared Storage
        │
        ▼
INNORIX Platform
        │
        ▼
INNORIX Agent
        │
        ▼
Enterprise Systems

This reference workflow demonstrates how AI-generated outputs
are transferred back to enterprise systems using the INNORIX SDK.
"""

import logging
from pathlib import Path

import yaml

from sdk.transfer import TransferService
from sdk.pipeline import PipelineFactory

logger = logging.getLogger(__name__)


class ResultDistributionWorkflow:
    """Reference workflow for AI result distribution."""

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
        # Validate transfer configuration
        # Validate pipeline configuration

        return True

    # ------------------------------------------------------------------
    # Wait for Pipeline Completion
    # ------------------------------------------------------------------

    def wait_for_pipeline(self):

        monitoring = self.pipeline_settings["monitoring"]

        if not monitoring["enabled"]:
            logger.info("Pipeline monitoring is disabled.")
            return

        self.pipeline.connect()

        # TODO
        # Retrieve execution ID from the pipeline or workflow manager
        execution_id = "PIPELINE-000001"

        self.pipeline.wait(execution_id)

        result = self.pipeline.result(execution_id)

        logger.info(f"Pipeline Status : {result['status']}")
        logger.info(f"Output Path     : {result['output_path']}")

        self.pipeline.disconnect()

    # ------------------------------------------------------------------
    # Transfer Results
    # ------------------------------------------------------------------

    def transfer_results(self):

        source = self.transfer_settings["source"]["path"]
        destination = self.transfer_settings["destination"]["path"]

        logger.info("Starting AI result distribution...")

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
    # Execute Workflow
    # ------------------------------------------------------------------

    def execute(self):

        logger.info("==========================================")
        logger.info("Result Distribution Started")
        logger.info("==========================================")

        self.validate()

        self.wait_for_pipeline()

        self.transfer_results()

        logger.info("==========================================")
        logger.info("Result Distribution Completed")
        logger.info("==========================================")


def main():

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    workflow = ResultDistributionWorkflow()

    workflow.execute()


if __name__ == "__main__":
    main()