# torch_utils.py

def count_parameters(model, include_constants=False):
    return sum(
        p.numel() for p in model.parameters()
        if include_constants or p.requires_grad
    )
