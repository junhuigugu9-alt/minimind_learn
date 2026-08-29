import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-L','--load_from', type=int, help="模型加载路径（model=原生torch权重，其他路径=transformers格式）")
    args = parser.parse_args()
    print(f"args.load_from:{args.load_from}")
    print(f"type:{type(args.load_from)}")

if __name__ == "__main__":
    main()