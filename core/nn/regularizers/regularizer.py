import torch


class Regularizer:
    """
    An abstract class representing a regularizer. It must implement
    call, returning a scalar tensor.
    """
    default_implementation = 'l2'

    def __call__(self, parameter: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError