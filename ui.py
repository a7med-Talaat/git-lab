def render_header(title):
    border = "=" * 40
    return f"{border}\n  {title}\n{border}"

def show_banner():
    print(render_header("GIT LAB CLI INTERFACE"))
