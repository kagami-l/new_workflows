import sys

def main() -> str:
    print(f"\n\n## Hi from the MERICO workflow!\n\n", flush=True)

    print(f"\n\npython version: {sys.version}\n\n")
    for p in sys.path:
        print(f"- {p}")
    print("\n\n", flush=True)

    print("\n\n### Checking additional packages\n\n")
    try:
        import typer
        print(f"\n\n- typer version: {typer.__version__}")
    except ImportError:
        print("\n\n- typer not found")

    try:
        import numpy
        print(f"\n\n- numpy version: {numpy.__version__}")
    except ImportError:
        print("\n\n- numpy not found")


if __name__ == "__main__":
    main()
