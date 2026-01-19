def brew_chai(flavour):
    if flavour not in ["lemon", "ginger", "cardamom"]:
        raise ValueError(f"Unsupported chai flavour: {flavour}")
    return f"Brewed a cup of {flavour} chai!"


brew_chai("mint")