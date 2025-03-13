def progress_cb(dfProgress: float, message = None, cb_data = None):
    """Simplifed but hopefully smoother looking callback
    """
    bar_prog = int(dfProgress*20)
    p_bar = f"[{"#"*bar_prog + " "*(20 - bar_prog)}]"
    print(p_bar, end="\r")