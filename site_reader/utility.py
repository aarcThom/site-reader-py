
def progress_cb(dfProgress: float, message = None, cb_data = None):
    """Simplifed but hopefully smoother looking callback
    """
    print(f"{dfProgress*100:0.0f}")
