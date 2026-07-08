"""
INNORIX AI Integration
Pipeline Factory

Creates the appropriate pipeline adapter based on the configured
AI platform.
"""

from .airflow import AirflowPipelineClient
from .azureml import AzureMLPipelineClient
from .custom import CustomPipelineClient
from .kubeflow import KubeflowPipelineClient
from .sagemaker import SageMakerPipelineClient
from .vertex import VertexPipelineClient


class PipelineFactory:
    """
    Factory class for creating AI pipeline clients.
    """

    @staticmethod
    def create(provider: str):

        provider = provider.lower()

        if provider == "kubeflow":
            return KubeflowPipelineClient()

        if provider == "airflow":
            return AirflowPipelineClient()

        if provider == "sagemaker":
            return SageMakerPipelineClient()

        if provider in ("vertex", "vertex-ai"):
            return VertexPipelineClient()

        if provider in ("azureml", "azure-machine-learning"):
            return AzureMLPipelineClient()

        if provider == "custom":
            return CustomPipelineClient()

        raise ValueError(
            f"Unsupported pipeline provider: {provider}"
        )