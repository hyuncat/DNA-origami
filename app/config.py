class AppConfig:
    """
    Configuration File
    """
    APP_NAME: str = "Lattice Designer"
    # Default to False, will be updated in initialize() based on the environment
    RUNNING_IN_JUPYTER: bool = False

    @classmethod
    def initialize(cls) -> None:
        """
        Perform any necessary initializations here, e.g.:
        - Loading settings from a file
        - Determining the runtime environment
        """
        try:
            from IPython import get_ipython
            if get_ipython() is not None:
                cls.RUNNING_IN_JUPYTER = True
        except ImportError:
            # IPython is not installed, so we're not running in a Jupyter environment
            cls.RUNNING_IN_JUPYTER = False
