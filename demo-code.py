import ansify


def main():
    # Core functions
    print(ansify.boldText("Core Functions"))
    ansify.banner("Hello, world!")
    ansify.success("Success!")
    ansify.warn("Warning!")
    ansify.error("Something went wrong.")
    print(ansify.boldText("Bold text example"))

    # Paint engine
    print("\n" + ansify.boldText("Paint Engine"))

    critical = ansify.paint(
        " Critical Error ",
        colour=ansify.white,
        bg=ansify.bg_red,
        is_bold=True,
    )
    print(critical)

    underlined = ansify.paint(
        "Read Online",
        colour=ansify.cyan,
        is_underline=True,
    )
    print(underlined)


if __name__ == "__main__":
    main()
