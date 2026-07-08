"""
INNORIX AI Integration
Pipeline Base Interface

Defines the abstract interface that all AI pipeline adapters
must implement.
"""

from abc import ABC, abstractmethod
from typing import Optional


class PipelineClient(ABC):
    """
    Abstract base class for AI pipeline integrations.

    All AI orchestration platform adapters should inherit from
    this class and implement the required methods.
    """

    @abstractmethod
    def connect(self) -> bool:
        """
        Initialize the pipeline client.

        Returns:
            bool: True if the connection succeeds.
        """
        raise NotImplementedError

    @abstractmethod
    def disconnect(self) -> None:
        """
        Disconnect from the pipeline.
        """
        raise NotImplementedError

    @abstractmethod
    def trigger(self) -> Optional[str]:
        """
        Start a new pipeline execution.

        Returns:
            Optional[str]:
                Pipeline execution ID.
        """
        raise NotImplementedError

    @abstractmethod
    def status(self, execution_id: str) -> dict:
        """
        Retrieve the current pipeline execution status.

        Args:
            execution_id:
                Pipeline execution identifier.

        Returns:
            dict:
                Pipeline status information.
        """
        raise NotImplementedError

    @abstractmethod
    def wait(self, execution_id: str) -> bool:
        """
        Wait until the pipeline execution completes.

        Args:
            execution_id:
                Pipeline execution identifier.

        Returns:
            bool:
                True when execution completes successfully.
        """
        raise NotImplementedError

    @abstractmethod
    def result(self, execution_id: str) -> dict:
        """
        Retrieve the pipeline execution result.

        Args:
            execution_id:
                Pipeline execution identifier.

        Returns:
            dict:
                Pipeline output information.
        """
        raise NotImplementedError

    @abstractmethod
    def cancel(self, execution_id: str) -> bool:
        """
        Cancel a running pipeline execution.

        Args:
            execution_id:
                Pipeline execution identifier.

        Returns:
            bool:
                True if the pipeline was cancelled successfully.
        """
        raise NotImplementedError