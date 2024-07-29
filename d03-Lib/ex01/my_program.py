from local_lib.path import Path

if __name__ == "__main__":
    dir = Path("test")
    dir.mkdir_p()
    f = dir / "Hello.txt"
    f.touch()
    f.write_text("Hello World!")
    print(f.read_bytes().decode("utf-8"))